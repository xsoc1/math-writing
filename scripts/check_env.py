#!/usr/bin/env python3
"""Read-only tool/TeX capability inventory. No installs or configuration changes."""
from __future__ import annotations
import argparse
import datetime as dt
import json
from pathlib import Path
import platform
import shutil
import subprocess

TOOLS = {
    'xelatex': ['--version'], 'latexmk': ['-v'], 'lualatex': ['--version'],
    'pandoc': ['--version'], 'biber': ['--version'], 'chktex': ['--version'],
    'pdftoppm': ['-v'], 'pdftocairo': ['-v'], 'node': ['--version'],
}
TEX_FILES = ['ctexart.cls','mathtools.sty','amsthm.sty','unicode-math.sty',
             'hyperref.sty','cleveref.sty','aliascnt.sty','tikz-cd.sty',
             'standalone.cls','STIXTwoText-Regular.otf','STIXTwoMath-Regular.otf',
             'FandolSong-Regular.otf']

def collect() -> dict:
    result = {'executed_at_system_clock': dt.datetime.now(dt.timezone.utc).isoformat(),
              'platform': platform.platform(), 'python': platform.python_version(),
              'tools': {}, 'tex_files': {},
              'note': 'Detection is not a compilation, visual, or mathematical correctness test.'}
    for name, args in TOOLS.items():
        path = shutil.which(name)
        row: dict = {'path': path, 'available': path is not None}
        if path:
            try:
                p = subprocess.run([path, *args], capture_output=True, text=True,
                                   errors='replace', timeout=10, check=False)
                lines = (p.stdout + '\n' + p.stderr).strip().splitlines()
                row.update(version_banner=lines[:4], returncode=p.returncode)
            except (OSError, subprocess.TimeoutExpired) as exc:
                row['error'] = str(exc)
        result['tools'][name] = row
    kpse = shutil.which('kpsewhich')
    for name in TEX_FILES:
        if not kpse:
            result['tex_files'][name] = {'available': None, 'reason': 'kpsewhich not found'}
            continue
        try:
            p = subprocess.run([kpse, name], capture_output=True, text=True,
                               timeout=10, check=False)
            result['tex_files'][name] = {'available': p.returncode == 0,
                                         'path': p.stdout.strip() or None}
        except (OSError, subprocess.TimeoutExpired) as exc:
            result['tex_files'][name] = {'available': None, 'error': str(exc)}
    return result

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path)
    args=ap.parse_args()
    text=json.dumps(collect(), ensure_ascii=False, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
