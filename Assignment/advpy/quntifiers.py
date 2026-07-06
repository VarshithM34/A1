#quantifiers
import re
'''
+ one or more occurrences of the preceding element
* zero or more occurrences of the preceding element
? zero or one occurrence of the preceding element
'''
pat = r'[abc]+'
print(re.match(pat, 'aaabbbccc'))  # returns a match object
pat1 = r'[a-z]*'
print(re.match(pat1, 'arjun'))  # returns a match object
pat2 = r'[a-zA-Z]?'
print(re.match(pat2,'Arjun'))  # returns a match object
pat3 = r'[a-zA-Z]+[0-9]$'
print(re.match(pat3,'Arjun1'))  # returns a match object


'''
\d digits
\D non-digits
\w word characters (alphanumeric + underscore)
\W non-word characters
\s whitespace characters
\S non-whitespace characters    
'''
pat4 = r'^\w{5}\d{4}\w{1}$'
print(re.fullmatch(pat4,'ABCDE1234A'))

pat5 = r'^[6-9]\d{9}$'
print(re.fullmatch(pat5 , '9581850778'))