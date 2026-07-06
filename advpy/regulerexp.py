import re
#print(dir(re))
#'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 
# 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sub', 
# 'subn'

pat = 'abcd'
print(re.match(pat, 'abcdhhpow'))  # returns a match object
print(re.match(pat ,'abcdhhpow').span ())# returns a tuple (0, 4) indicating the start and end positions of the match
print(re.match(pat ,'abcdhhpow').group()) # returns the matched string 'abcd'
print(re.match(pat ,'abcdhhpow').start()) # returns the starting position of the match, which is 0
print(re.findall(pat, 'abcdhhpow')) # returns a list of all matches ['abcd']
print(re.search(pat, 'abcdhhpow')) # returns a match object
print(re.search(pat, 'abcdhhpow').span()) # returns a tuple (0, 4) indicating the start and end positions of the match
print(re.split(pat, 'abcdhhpow')) # returns a list of substrings ['abcdhhpow'] since the pattern 'abcd' is not found in the string
print(re.fullmatch(pat, 'abcd')) # returns None since the entire string does not match the pattern
print(re.fullmatch(pat, 'abcdhhpow'))





