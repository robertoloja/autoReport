import sys
import argparse

 # Command line argument parsing.
description = '''Generate an engineering report in .odt format.

The Title page is generated from arguments passed at program invocation, as
explained below.

The Summary is taken from file 'summary.txt' in the present directory.

The Table of Contents is auto-generated.

The Introduction is taken from the file 'introduction.txt' in the present
directory.

The Body of the report is taken from file 'body.txt' in the present directory.
All lines beginning with '#x' are used as section headings ('#x' is replaced
with progressive section numberings). These will be used in auto-generating
the table of contents.

The Conclusions section is taken from file 'conclusion.txt'.

The optional References section will be generated from 'body.txt' from any use
of '_x*' in the text, where 'x' is a number. The actual references should then
be included at the end of 'body.txt'.

The optional Appendices section are taken from 'appendices.txt' if it exists
in the current directory.'''

options = argparse.ArgumentParser(description=description,
            formatter_class=argparse.RawTextHelpFormatter)

options.add_argument('-n', required=True, help='Name for Title Page. Surround \
        by double quotes. E.g. "John Smith".', dest='name', nargs=1)

options.add_argument('-c', required=True, help='Course Code. E.g. CENG251.',
        nargs=1, dest='course_code')

options.add_argument('-t', required=True, help='Title of the report. Surround \
        by double quotes. E.g. "Implementing getopt()".', dest='title', nargs=1)

options.add_argument('-d', help='Optional date. If not supplied, today\'s date \
        will be used, in format MONTH DAY(st|nd|rd|th), YEAR). Surround by \
        double quotes. E.g. "12/31/2000".', dest='date', nargs=1)

arguments = vars(options.parse_args())
print(arguments)
