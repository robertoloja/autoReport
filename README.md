-Project on-hold due to school work.

# autoReport
## Summary
This program generates an engineering report in .docx format. That is, 
Given a number of raw text files and some shell arguments, it assembles
a nicely formated .docx with an auto-generated table of contents and 
references section.


## Usage
The Title page is generated from arguments passed at program invocation.

Most other sections are taken from files named 'section.txt' in the present
directory. For example, the Summary is generated from file 'summary.txt', 
the Introduction is generated from 'introduction.txt', etc.

The Body of the report is taken from file 'body.txt', but this file
must be formatted in a specific way, in order to correctly generate headings,
subheadings, and the Table of Contents.

In 'body.txt', any lines beginning with '##' are used as section headings,
where the ## is replaced by progressive section numberings (e.g. the line
'## Methods', if it is the second use of ## in the text file, becomes 
'2. Methods' in the final document). Similarly, '###' are sub-headings. Thus,
the line '### Sampling', if it comes after '## Methods' and before another
heading or subheading, becomes '2.1 Sampling'. There may be paragraph text
between headings and subheadings; this does not affect the count.

(The following is not yet implemented.)
The optional References section is also generated from 'body.txt'. In that file,
any use of '_*' in the text will create a footnote and reference. The reference
itself should then be included at the end of 'body.txt', in the same order as
they appear in the text. When the References section is generated, these will
be arranged in alphabetical order by Author.

The optional Appendices section are taken from 'appendices.txt' if it
exists in the current directory.


## Arguments

| Flag |     Meaning     | Required |
|------|-----------------|----------|
|  -t  | Title of report |    Yes   |
|  -c  |   Course Code   |    Yes   |
|  -n  |      Name       |    Yes   |
|  -s  | Student Number  |    No    |  Default is blank.
|  -d  |      Date       |    No    |  Default is today's date.

## Requirements

- Python3.4 (Any version of Python 3 should be fine)
- [python-docx](https://github.com/python-openxml/python-docx)
