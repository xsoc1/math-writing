#!/usr/bin/env node
/* Optional smoke test for the bundled specimens' dollar-math subset.
 * This is not a general Markdown parser, proof check, or Obsidian GUI test.
 * Requires an already installed, resolvable mathjax-full package; no installs. */
'use strict';
const fs = require('fs');
let mathjax, TeX, SVG, liteAdaptor, RegisterHTMLHandler, version;
try {
  ({mathjax} = require('mathjax-full/js/mathjax.js'));
  ({TeX} = require('mathjax-full/js/input/tex.js'));
  ({SVG} = require('mathjax-full/js/output/svg.js'));
  ({liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js'));
  ({RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js'));
  require('mathjax-full/js/input/tex/AllPackages.js');
  version = require('mathjax-full/package.json').version;
} catch (error) {
  console.error('Optional test needs mathjax-full resolvable by Node. Nothing was installed.');
  console.error(error.message);
  process.exit(2);
}
const files = process.argv.slice(2);
if (!files.length) {
  console.error('Usage: node scripts/check_mathjax.cjs specimen.md [specimen.md ...]');
  process.exit(2);
}
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const document = mathjax.document('', {
  InputJax: new TeX({packages: ['base', 'ams']}),
  OutputJax: new SVG({fontCache: 'none'})
});
const report = {engine: 'mathjax-full', version, packages: ['base', 'ams'],
  scope: 'Bundled specimen math conversion only; not Obsidian or proof verification.', files: []};
let failed = false;
for (const file of files) {
  const result = {file, formulas: 0, failures: []};
  try {
    const input = fs.readFileSync(file, 'utf8').replace(/^>\s?/gm, '')
      .replace(/^---\n[\s\S]*?\n---\n/, '')
      .replace(/^```[^\n]*\n[\s\S]*?^```\s*$/gm, '');
    for (const match of input.matchAll(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g)) {
      result.formulas++;
      const formula = match[1] === undefined ? match[2] : match[1];
      try {
        const output = adaptor.outerHTML(document.convert(formula, {display: match[1] !== undefined}));
        if (output.includes('data-mml-node="merror"')) throw new Error('MathJax emitted merror');
      } catch (error) { result.failures.push({formula, error: error.message}); }
    }
  } catch (error) { result.failures.push({error: error.message}); }
  if (result.failures.length) failed = true;
  report.files.push(result);
}
console.log(JSON.stringify(report, null, 2));
process.exit(failed ? 1 : 0);
