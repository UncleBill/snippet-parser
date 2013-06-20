#!/usr/bin/python
# -*- coding: utf-8 -*-

class builder():
    """buil"""
    def __init__(self, snippets, leader = 'snippet'):
        self.snippets = snippets
        self.leader = 'snippet'

    def builder(self):
        """builder method"""
        snippet_content = ''
        for snippet in self.snippets:
            snippet_content += "snippet" + self.snippets[k] + '\n' * 2

        return snippet_content

    def build2file(self, fhandler):
        """build snippets and write to fhandler"""
        fhandler.write(self.builder())
        fhandler.close()
