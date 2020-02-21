from html.parser import HTMLParser
from html.entities import name2codepoint


class XueqiuHTMLParser(HTMLParser):

    ## get SNB.data.quote
    def handle_data(self, data):
        if 'SNB' in data:
            for line in data.split('\n'):
                print('1', line)
                if 'quote' in line:
                    return(line)
