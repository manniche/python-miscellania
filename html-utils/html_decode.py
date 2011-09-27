#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- mode: python -*-
import sys, urllib, re

def usage():
    import os.path
    scriptname = os.path.basename(sys.argv[0])
    ret = """Usage: cat STRING_TO_ENCODE | {0}

The program returns a html encoded string based on STRING_TO_ENCODE

Example:
echo "%28" | python {0}
Out: (
""".format( scriptname )
    return ret

def html_decode(args):    
    try:
        return urllib.unquote( args )
    except Exception, e:
        sys.stderr.write(" ".join( ["Error!", e.__str__(), "\n"] ) )
        return None


def process_htmlencoded_text( coded_text ):
    output = list()
    for tok in tokenize( coded_text ):
        if tok[0] == 'html_entity':
            output.append( html_decode( tok[1] ) )
        else:
            output.append( tok[1] )
                                  
    return output


token_pattern = r"""
 (?P<html_entity>%[A-Z0-9]{2})
|(?P<text>[a-zA-Z0-9\+-\\*]+)
"""
token_re = re.compile(token_pattern, re.VERBOSE)

class TokenizerException( Exception ): pass

def tokenize(text):
    pos = 0
    while True:
        m = token_re.match(text, pos)
        if not m: break
        pos = m.end()
        tokname = m.lastgroup
        tokvalue = m.group(tokname)
        yield tokname, tokvalue
    if pos != len(text):
        print (pos, len(text))
        raise TokenizerException('tokenizer stopped at pos %r of %r: %s' % ( pos, len( text ), text[ pos ] ) )

if __name__ == '__main__':

    infile = list()
    for line in sys.stdin:
        infile.append( line.strip( '\n' ) )

    ret = 1
    if len(sys.argv) == 1:
        output = process_htmlencoded_text( infile[0] )

    else:
        sys.exit( usage() )
        
    if output is not None:
        ret = 0
        print( "".join( output) )
    else:
        print usage()

    sys.exit(ret)
