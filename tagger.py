#! /usr/bin/env python
'''
Tagger Extension for Inscape.
Simply adds attributes for name or class to editable text elements.
Useful for later manipulation with javascript using a browser.
'''

import inkex
import os
from inkex import elements
from inkex import styles
import pdb
__version__ = '0.1'

inkex.localization.localize()

class Tagger(inkex.EffectExtension):
    def __init__(self):
        inkex.extensions.EffectExtension.__init__(self)
        try:
            self.tty = open("/dev/tty", 'w')
        except:
            self.tty = open(os.devnull, 'w')


    def effect(self):
        """ Add class or name to selected text objects.
            Adds class='editable' or  name='editable' to selected text
            elements.
        """
        for elId in self.svg.selected: 
            el = self.svg.getElementById(elId)
            if el.tag_name is "text":
                el.set("name","editable")
                el.set("class","editable")
            

            
if __name__ == '__main__':
    e = Tagger()
    e.run()

