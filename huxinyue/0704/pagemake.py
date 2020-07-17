# -*- coding: utf-8 -*-
# __file__  : pagemake.py
# __time__  : 2020/7/4 6:29 PM

from xml.sax.handler import ContentHandler
from xml.sax import parse


class PageMaker(ContentHandler):
    passthrough = False

    def startElement(self, name, attrs):
        if name == 'page':
            self.passthrough = True
            self.out = open(attrs['name'] + '.html', 'w')
            self.out.write('<html><head>\n')
            self.out.write('<title>{}</title>\n'.format(attrs['title']))
            self.out.write('</head><body>\n')
        elif self.passthrough:
            self.out.write('<' + name)
            if not attrs.items():
                self.out.write('>')
            for key, val in attrs.items():
                self.out.write(' {}="{}"'.format(key, val))
                self.out.write('>')

    def endElement(self, name):
        if name == 'page':
            self.passthrough = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.passthrough:
            self.out.write('</{}>'.format(name))

    def characters(self, chars):
        if self.passthrough:
            self.out.write(chars)


if __name__ == '__main__':
    parse('website.xml', PageMaker())
