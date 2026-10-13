#!/usr/bin/env python3
"""Limited static checks for mathematical .md/.tex. Not a parser or proof verifier."""
from __future__ import annotations
import argparse
from dataclasses import dataclass, asdict
import json
from pathlib import Path
import re

@dataclass(frozen=True)
class Issue:
    line: int
    severity: str
    code: str
    message: str


def visible_lines(text: str, markdown: bool) -> list[tuple[int, str]]:
    """Skip frontmatter and fenced code; preserve source line numbers."""
    out=[]
    fence_char=None
    fence_len=0
    front=False
    for number, raw in enumerate(text.splitlines(), 1):
        line=re.sub(r'^\s*(?:>\s?)+', '', raw) if markdown else raw
        stripped=line.strip()
        if markdown:
            if number == 1 and stripped == '---':
                front=True
                continue
            if front:
                if stripped=='---':
                    front=False
                continue
            match=re.match(r'^\s*(`{3,}|~{3,})', line)
            if match:
                seq=match.group(1)
                if fence_char is None:
                    fence_char, fence_len=seq[0], len(seq)
                elif seq[0]==fence_char and len(seq)>=fence_len:
                    fence_char=None
                continue
            if fence_char is not None:
                continue
        else:
            line=re.split(r'(?<!\\)%', line, maxsplit=1)[0]
        out.append((number,line))
    return out


def check_text(text: str, kind: str) -> list[Issue]:
    markdown=kind.lower().lstrip('.')=='md'
    issues=[]
    display_start=None
    ids={}
    env_stack=[]
    for n,line in visible_lines(text,markdown):
        plain=re.sub(r'`[^`]*`','',line) if markdown else line
        if markdown:
            if plain.strip()=='$$':
                display_start=n if display_start is None else None
            elif re.search(r'(?<!\\)\$\$',plain):
                issues.append(Issue(n,'warning','MD-DISPLAY-LINE',
                                    'Use separate $$ delimiter lines in the portable profile.'))
            if re.search(r'\\(?:documentclass|usepackage)\b',plain):
                issues.append(Issue(n,'error','MD-FULL-TEX','Full LaTeX document commands in Markdown.'))
            if re.search(r'\\begin\{(?:theorem|lemma|proposition|proof|tikzcd)\}',plain):
                issues.append(Issue(n,'error','MD-ENV','Use Markdown structure or an exported diagram.'))
            if re.search(r'\\(?:newcommand|renewcommand|def|gdef|label|eqref|cref|tag)\b',plain):
                issues.append(Issue(n,'warning','MD-PORTABILITY',
                                    'Macro/label behavior needs explicit runtime configuration; no cross-note assumption.'))
            match=re.fullmatch(r'\s*\^(\S+)\s*',plain)
            if match:
                key=match.group(1)
                if not re.fullmatch(r'[A-Za-z0-9-]+',key):
                    issues.append(Issue(n,'error','MD-ID','Block IDs use ASCII letters, digits, and hyphens.'))
                if key in ids:
                    issues.append(Issue(n,'error','DUP-ID',f'Duplicate block ID (first at line {ids[key]}).'))
                ids[key]=n
        else:
            if re.search(r'(?<!\\)\$\$',plain):
                issues.append(Issue(n,'warning','TEX-DISPLAY','Use \\[...\\] or AMS display environments, not $$.'))
        # Only literal begin/end tokens are recognized. Macro-generated environments are outside scope.
        for match in re.finditer(r'\\(begin|end)\{([A-Za-z*]+)\}',plain):
            op,env=match.groups()
            if op=='begin':
                env_stack.append((env,n))
            elif not env_stack or env_stack[-1][0]!=env:
                issues.append(Issue(n,'error','ENV-MISMATCH',f'Unmatched \\end{{{env}}}.'))
            else:
                env_stack.pop()
        if re.search(r'显然|不妨设|\b(?:clearly|obvious(?:ly)?|without loss of generality)\b',plain,re.I):
            issues.append(Issue(n,'review','LOGIC-TRIGGER',
                                'Check the justification for this audience; this phrase is not automatically wrong.'))
    if display_start is not None:
        issues.append(Issue(display_start,'error','MD-DISPLAY-OPEN','Unclosed standalone $$ display delimiter.'))
    for env,n in env_stack:
        issues.append(Issue(n,'error','ENV-OPEN',f'Unclosed literal \\begin{{{env}}}.'))
    return issues


def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('files',nargs='+',type=Path)
    ap.add_argument('--json',action='store_true')
    args=ap.parse_args()
    records=[]
    has_errors=False
    for path in args.files:
        try:
            if path.suffix.lower() not in ('.md','.tex','.sty'):
                raise ValueError('Expected .md, .tex, or .sty')
            issues=check_text(path.read_text(encoding='utf-8'),path.suffix)
        except (OSError,UnicodeError,ValueError) as exc:
            issues=[Issue(0,'error','READ',str(exc))]
        has_errors |= any(x.severity=='error' for x in issues)
        records.append({'file':str(path),'issues':[asdict(x) for x in issues]})
    if args.json:
        print(json.dumps(records,ensure_ascii=False,indent=2))
    else:
        for record in records:
            print(record['file'])
            for issue in record['issues']:
                print(f"  {issue['line']}: {issue['severity']} {issue['code']}: {issue['message']}")
            if not record['issues']:
                print('  No issues found by these limited checks; not a correctness certification.')
    return 1 if has_errors else 0

if __name__=='__main__':
    raise SystemExit(main())
