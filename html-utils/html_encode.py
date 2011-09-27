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
echo "(" | python {0}
Out: %28
""".format( scriptname )
    return ret

def html_encode(args):
    try:
        return urllib.quote_plus( args )
    except Exception, e:
        sys.stderr.write(" ".join( ["Error!", e.__str__(), "\n"] ) )
        return None


if __name__ == '__main__':

    infile = list()
    for line in sys.stdin:
        infile.append( line.strip( '\n' ) )

    ret = 1
    if len(sys.argv) == 1:
        output = html_encode( infile[0] )

    else:
        sys.exit( usage() )
        
    if output is not None:
        ret = 0
        print( "".join( output) )
    else:
        print usage()

    sys.exit(ret)
