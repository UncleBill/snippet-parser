#!/usr/bin/env python
# -*- coding: utf-8 -*-

class parser():
    """parser snippet file"""
    def __init__(self, f):
        """initialize"""
        self.snippet_file = file(f)
        self.leader = 'snippet'

    def parser(self):
        """
        parser(self)
        return: dict: {trigger:{content:content}}
        """
        snippets = {}
        all_lines = self.snippet_file.readlines()
        for line in all_lines:
            if line.startswith('#'): continue

            elif line.startswith(self.leader):
                trigger = line.split(' ')[1]
                snippets[trigger] = ''   # create a key
                snippets[trigger] = {}

            else:
                snippets[trigger]['content'] += line + '\n'

        return snippets

class neoparser(parser):
    """parser for neosnippet"""
    def __init__(self, f,):
        super.__init__()
        self.token = ['abbr','alias','options']

    def parser(self):
        """
        parser(self)
        return: dict: {trigger:{content:content}}
        """
        snippets = {}
        all_lines = self.snippet_file.readlines()
        for line in all_lines:
            if line.startswith('#'): continue

            elif line.startswith(self.leader):
                trigger = line.split(' ')[1]
                snippets[trigger] = ''   # create a key
                snippets[trigger] = {}

            else:
                for tk in token:
                    if line.startswith(tk):
                        snippets[trigger][tk] = line.split(' ')[1]

                snippets[trigger]['content'] += line + '\n'

        return snippets


# test
if __name__ == '__main__':
    snippets = parser('./javascript.snipmate.snippets').parser()
    for k in snippets:
        print '=-'*20
        print 'snippet' , k
        print snippets[k]
