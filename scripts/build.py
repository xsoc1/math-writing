#!/usr/bin/env python3
"""Build this package's controlled specimens; never accepts arbitrary source filenames."""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]

def run(command: list[str], cwd: Path) -> None:
    try:
        p=subprocess.run(command,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                         text=True,errors='replace',timeout=180,check=False)
    except (OSError,subprocess.TimeoutExpired) as exc:
        raise RuntimeError(f'Cannot complete {command[0]}: {exc}') from exc
    if p.returncode:
        raise RuntimeError(f'Build failed ({p.returncode}):\n'+p.stdout[-18000:])


def compile_tex(name: str, folder: Path, latexmk: str) -> Path:
    out=ROOT/'.build'/name
    out.mkdir(parents=True,exist_ok=True)
    command=[latexmk,'-norc','-xelatex','-e',
             "$xelatex = 'xelatex -no-shell-escape %O %S';",
             '-interaction=nonstopmode','-halt-on-error','-file-line-error',
             '-synctex=1',f'-outdir={out}',name+'.tex']
    run(command,folder)
    result=out/(name+'.pdf')
    if not result.is_file():
        raise RuntimeError(f'Expected output is missing: {result}')
    return result


def export_svg(pdf: Path, executable: str) -> None:
    svg=ROOT/'assets/diagrams/quotient.svg'
    run([executable,'-svg',str(pdf),str(svg)],ROOT)
    # Add an explicit paper background so black diagram labels remain visible in dark themes.
    ns='http://www.w3.org/2000/svg'
    ET.register_namespace('',ns)
    tree=ET.parse(svg);root=tree.getroot()
    root.insert(0,ET.Element('{'+ns+'}rect',{'width':'100%','height':'100%','fill':'white'}))
    tree.write(svg,encoding='utf-8',xml_declaration=True)
    shutil.copy2(svg,ROOT/'assets/obsidian/quotient.svg')


def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--language',choices=['zh','en','both'],default='both')
    ap.add_argument('--templates',action='store_true',help='Also compile the placeholder document skeletons.')
    ap.add_argument('--skip-diagram',action='store_true',help='Do not rebuild/export the existing diagram.')
    args=ap.parse_args()
    latexmk=shutil.which('latexmk')
    if not latexmk or not shutil.which('xelatex'):
        print('Need latexmk and xelatex on PATH. Run check_env.py; nothing was installed.',file=sys.stderr)
        return 2
    if not args.skip_diagram and not shutil.which('pdftocairo'):
        print('Diagram export needs pdftocairo. Install Poppler or explicitly use --skip-diagram.',file=sys.stderr)
        return 2
    output=ROOT/'examples-output';output.mkdir(exist_ok=True)
    languages=['zh','en'] if args.language=='both' else [args.language]
    try:
        for lang in languages:
            for stem in (['main','template'] if args.templates else ['main']):
                name=f'{stem}-{lang}'
                pdf=compile_tex(name,ROOT/'assets/latex',latexmk)
                shutil.copy2(pdf,output/pdf.name)
                print(f'Built {output/pdf.name}')
        if not args.skip_diagram:
            pdf=compile_tex('quotient',ROOT/'assets/diagrams',latexmk)
            shutil.copy2(pdf,ROOT/'assets/diagrams/quotient.pdf')
            export_svg(pdf,shutil.which('pdftocairo') or 'pdftocairo')
            print('Built quotient.pdf and quotient.svg (also copied into the specimen vault).')
    except (RuntimeError,OSError,ET.ParseError) as exc:
        print(str(exc),file=sys.stderr)
        return 1
    print('Compilation is not a mathematical or visual correctness check. Inspect logs and rendered pages.')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
