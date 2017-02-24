#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from grako.buffering import Buffer
from grako.parsing import graken, Parser
from grako.util import re, RE_FLAGS, generic_main  # noqa


__all__ = [
    'TeXTokenParser',
    'TeXTokenSemantics',
    'main'
]

KEYWORDS = {}


class TeXTokenBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re='%.*?$',
        ignorecase=None,
        namechars='',
        **kwargs
    ):
        super(TeXTokenBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class TeXTokenParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re='%.*?$',
        ignorecase=None,
        left_recursion=False,
        parseinfo=True,
        keywords=None,
        namechars='',
        buffer_class=TeXTokenBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(TeXTokenParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
            **kwargs
        )

    @graken()
    def _start_(self):
        self._DOC_()
        self._check_eof()

    @graken()
    def _DOC_(self):

        def block0():
            self._ELEMENT_()
        self._closure(block0)

    @graken()
    def _ELEMENT_(self):
        with self._choice():
            with self._option():
                self._GROUP_()
            with self._option():
                self._CMD_()
            with self._option():
                self._MARKER_()
            with self._option():
                self._TEXT_()
            self._error('no available options')

    @graken()
    def _GROUP_(self):
        self._token('{')

        def block0():
            self._ELEMENT_()
        self._positive_closure(block0)
        self._token('}')

    @graken()
    def _CMD_(self):
        with self._choice():
            with self._option():
                self._MACRO_DEF_CMD_()
            with self._option():
                self._BREAK_CMD_()
            with self._option():
                self._CONTROL_CMD_()
            with self._option():
                self._SYMBOL_CMD_()
            self._error('no available options')

    @graken()
    def _LATEX_MACRO_DEF_CMD_(self):
        self._token('\\newcommand')
        self._ARG_()
        with self._optional():
            self._OPT_()
        self._ARG_()

    @graken()
    def _TEX_MACRO_DEF_CMD_(self):
        self._token('\\def')
        self._token('\\')

        def block0():
            self._pattern(r'[a-zA-Z]')
        self._positive_closure(block0)

        def block1():
            self._MARKER_()
        self._closure(block1)
        self._ARG_()

    @graken()
    def _BREAK_CMD_(self):

        def block0():
            with self._choice():
                with self._option():
                    self._pattern(r'\n')
                with self._option():
                    self._pattern(r'\r\n')
                self._error('expecting one of: \\n \\r\\n')
        self._positive_closure(block0)

    @graken()
    def _CONTROL_CMD_(self):
        self._token('\\')

        def block0():
            self._pattern(r'[a-zA-Z]')
        self._positive_closure(block0)

        def block1():
            with self._choice():
                with self._option():
                    self._ARG_()
                with self._option():
                    self._OPT_()
                self._error('no available options')
        self._closure(block1)

    @graken()
    def _SYMBOL_CMD_(self):
        self._token('\\')

        def block0():
            self._pattern(r'[^a-zA-Z0-9]')
        self._positive_closure(block0)
        with self._group():
            with self._choice():
                with self._option():
                    self._ARG_()
                with self._option():
                    self._OPT_()
                with self._option():
                    self._pattern(r'[a-zA-Z]')
                self._error('expecting one of: [a-zA-Z]')

    @graken()
    def _MACRO_DEF_CMD_(self):
        with self._choice():
            with self._option():
                self._LATEX_MACRO_DEF_CMD_()
            with self._option():
                self._TEX_MACRO_DEF_CMD_()
            self._error('no available options')

    @graken()
    def _ARG_(self):
        self._token('{')

        def block0():
            self._ELEMENT_()
        self._closure(block0)
        self._token('}')

    @graken()
    def _OPT_(self):
        self._token('[')

        def block0():
            self._ELEMENT_()
        self._closure(block0)
        self._token(']')

    @graken()
    def _MARKER_(self):
        self._token('#')
        self._pattern(r'[0-9]')

    @graken()
    def _TEXT_(self):

        def block0():
            self._pattern(r'[^\\\#\{\}\[\]]')
        self._positive_closure(block0)


class TeXTokenSemantics(object):
    def start(self, ast):
        return ast

    def DOC(self, ast):
        return ast

    def ELEMENT(self, ast):
        return ast

    def GROUP(self, ast):
        return ast

    def CMD(self, ast):
        return ast

    def LATEX_MACRO_DEF_CMD(self, ast):
        return ast

    def TEX_MACRO_DEF_CMD(self, ast):
        return ast

    def BREAK_CMD(self, ast):
        return ast

    def CONTROL_CMD(self, ast):
        return ast

    def SYMBOL_CMD(self, ast):
        return ast

    def MACRO_DEF_CMD(self, ast):
        return ast

    def ARG(self, ast):
        return ast

    def OPT(self, ast):
        return ast

    def MARKER(self, ast):
        return ast

    def TEXT(self, ast):
        return ast


def main(filename, startrule, **kwargs):
    with open(filename) as f:
        text = f.read()
    parser = TeXTokenParser(parseinfo=False)
    return parser.parse(text, startrule, filename=filename, **kwargs)


if __name__ == '__main__':
    import json
    ast = generic_main(main, TeXTokenParser, name='TeXToken')
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()
