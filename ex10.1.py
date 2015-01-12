

#two backslashes tell python to print one
backslash = 'www.newsnet5.com\\%s' % 'decodedc'

#
single_quote = 'Luke, I am your %r.' % 'father'

double_quote = 'Luke, I am your \"%s.\"' % 'father'

triple_single = '''
Here are triple single quotes!
Two lines!
'''

triple_double = """
Here are triple double quotes!
Two lines!
"""

print backslash
print single_quote
print double_quote
print triple_single
print triple_double