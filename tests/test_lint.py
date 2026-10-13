from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from lint_math import check_text

class LintTests(unittest.TestCase):
    def codes(self,text,kind='md'):
        return {x.code for x in check_text(text,kind)}
    def test_valid_callout_math(self):
        text='> [!theorem] A\n> $$\n> \\begin{aligned}x&=y\\\\&=z\\end{aligned}\n> $$\n\n^thm-a'
        self.assertEqual(self.codes(text),set())
    def test_open_display(self):
        self.assertIn('MD-DISPLAY-OPEN',self.codes('$$\nx=1'))
    def test_code_is_ignored(self):
        self.assertEqual(self.codes('```latex\n\\usepackage{x}\n$$\n```'),set())
    def test_frontmatter_ignored(self):
        self.assertEqual(self.codes('---\ntitle: clearly\n---\nText'),set())
    def test_full_tex_in_md(self):
        self.assertIn('MD-FULL-TEX',self.codes(r'\documentclass{article}'))
    def test_unsupported_env(self):
        self.assertIn('MD-ENV',self.codes(r'\begin{tikzcd}A\end{tikzcd}'))
    def test_duplicate_id(self):
        self.assertIn('DUP-ID',self.codes('A\n\n^thm-a\n\nB\n\n^thm-a'))
    def test_invalid_id(self):
        self.assertIn('MD-ID',self.codes('^thm:a'))
    def test_wrong_environment_end(self):
        self.assertIn('ENV-MISMATCH',self.codes(r'\begin{aligned}x\end{matrix}'))
    def test_tex_dollar_warning(self):
        issues=check_text('$$x=1$$','tex')
        self.assertTrue(any(i.code=='TEX-DISPLAY' and i.severity=='warning' for i in issues))
    def test_logic_phrase_not_error(self):
        issues=check_text('Clearly, the identity is linear.','md')
        self.assertTrue(any(i.severity=='review' for i in issues))
        self.assertFalse(any(i.severity=='error' for i in issues))
    def test_comments_ignored_in_tex(self):
        self.assertEqual(self.codes('% $$\nText','tex'),set())

if __name__=='__main__':
    unittest.main()
