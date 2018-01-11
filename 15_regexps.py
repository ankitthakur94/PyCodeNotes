import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890

Ha HaHa

MetaCharacters (Need to be escaped while compiling regexps if they are to be explicitly searched for):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.I)

matches = pattern.search(sentence)

print(matches)


## Raw string in python
 # strings in python by default non-raw we can make them raw  by adding \r'<string>'
    # Python does no special handling of escape chars for raw strings.
    # i.e \t in raw string will not be interpreted as as tab spacing instead as raw '\t'
    # This is important because the regexps we will create will have special chars for which we do not want python to do any special handling.

print ( ' Normal string -> ')
print ( '\t Tab' )

print ( ' Raw string -> ')
print ( r'\t Tab' )


# re.compile
    # compiles regexp pattern to a variable for replicated use.

# <regexp_pattern>.finditer(<text_to_search>)
    # returns an iterator which contains all the matches of regexp in the text_to_search.
    # when iterated upon each object will be a match object.
        # So if finditer found 4 matches, iterating on its output will give 4 match objects each one containing information of the match found.
    # outputs  : match object
        # span = (start_index , end_index)
        # these index values can be plugged in directly to the 'text_to_search' to get the pattern we were grepping.
            # Ex : text_to_search [1:4]


pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
print ( ' output of find iter ->  ', matches )

print ( ' ---- ')
print ( ' -- Printing all the matches of abc using find iter -- ' )
for match in matches :
    print (match)



# Searching special chars
# Ex : searching for '.'
    # we will have the use '\.' instead of only '.' while compiling regexp.
    # otherwise it will output all chars in the text as matched value. (This is because '.' is used to match any char

pattern = re.compile(r'\.com')
matches = pattern.finditer(text_to_search)

print ( ' ---- ')
print ( ' -- Printing all the matches of . using find iter -- ' )
for match in matches :
    print (match)



################################################################
################ SPECIAL CHARACTERS MAP ########################
################################################################

#.       - Any Character Except New Line
#\d      - Digit (0-9)
#\D      - Not a Digit (0-9)
#\w      - Word Character (a-z, A-Z, 0-9, _)
#\W      - Not a Word Character
#\s      - Whitespace (space, tab, newline)
#\S      - Not Whitespace (space, tab, newline)


#### ANCHORS  :  Do not match any chars but some invisible positions before / after characters
#\b      - Word Boundary
                # White-space / non-alphanumeric character.
                # Ex : re.compile (r'\bHa')
                    # Will match 'Ha' which has a word boundary before it.
#\B      - Not a Word Boundary
#^       - Beginning of a String
                # pattern following this ^<> must be present at the start of the string.
#$       - End of a String
                # pattern following this $<> must be present at the end of the string.

#
#[]      - Matches Characters in brackets
#[^ ]    - Matches Characters NOT in brackets
#|       - Either Or
#( )     - Group
#
#Quantifiers:
    # we can append quantifiers after a patern to tell the number of occurrences
    # Ex : re.compile (r'\d\d\d')   -> can be written as -> re.compile(r'\d{3})
#*       - 0 or More
#+       - 1 or More
#?       - 0 or One (Makes something optional)
                # Ex  : re.compile(r'Mr\.?')
                    # will match <Mr.> and <Mr> both.
#{3}     - Exact Number
#{3,4}   - Range of Numbers (Minimum, Maximum)

# Character set :
    # denoted by [<char1><char2> .. and so on]
    # will match to any 1 char in the set.
    # chars which were originally needed to be escaped ( Ex : to match '.' in text we will have to enter '\.' in re.compile()
    # in a character set writing only . in [.] will match '.'  (For the sake of writing we can escape the dot in character set also)
    # remember normally given a range / multiple chars in a character set it will only match 1 character.

    # specifying a range in character set.
        # The '-' when placed at the start or end in a character will will tell to match the '-' in the set but it can also be used to specify a range.
        # [a-z] : match any lower case char (match only 1)
        # [a-zA-Z] : match lower / upper case
        # [a0xA-A0-9] : char or number.

    # Using carrot in character set.
        # ^ when used outside the character set will match the pattern following it at the start of thr string.
        # but when used in character sey it inverts the set and makes it match the inverse of character set given in []
        # [^a-zA-Z]  : match everything except characters.

### Matching multiple chars
    # So far now we have seen how to match a single char. to match multiple use quantifiers.


### Using Groups  via ()
    # This allows us to match multiple patterns
        # Ex : re.compile (r'M(r|s|rs)') : match if either of Ms / Mrs / Mr
            # This allows us to match Mr / Ms / Mrs  all three.

    # Ex : re.compile ( r'(www\.)?')
        # makes www. optional (i.e 0 or 1 match will work)



## Flags
    # Ignore case flag :
        # re.complie (r'start', re.IGNORECASE)      (can also use I instead of IGNORE CASE)

    # multiple such flags available.


#### Sample Regexs ####
#[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
################################################################
################################################################




pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)

print ( ' ---- ')
print ( ' -- Printing all the matches of Ha starting with word boundary using find iter -- ' )
for match in matches :
    print (match)



pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)

print ( ' ---- ')
print ( ' -- Printing all the matches of phone number -- ' )
for match in matches :
    print (match)


# what if we want to match phone numbers separated by dot (.) or dash (-)
# specify these characters in a character set [.-]
    # Now we will match either . or -

pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
matches = pattern.finditer(text_to_search)

print ( ' ---- ')
print ( ' -- Printing all the matches of phone number but separated by a dot (.) or dash (-) -- ' )
for match in matches :
    print (match)



## match phone nums starting from 800 or 900
    # Solution : Use character set to specify [89]

pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d')
matches = pattern.finditer(text_to_search)

print ( ' ---- ')
print ( ' -- Printing all the matches of phone numbers separated by a dot (.) or dash (-) and starting from 800 / 900 --  - ' )
for match in matches :
    print (match)


################################################
## match names with the syntax of Mr. T*
# Solution : Use character set to specify [89]
################################################

pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

print ( ' ---- ')
print ( ' -- Printing all the matches of Mr. names --  - ' )
for match in matches :
    print (match)

################################################
# match Mr. <> and Mrs. <> and Ms. <>
################################################

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

print ( ' ---- ')
print ( ' -- Printing all the matches of Mr / Ms / Mrs names --  - ' )
for match in matches :
    print (match)


emails = '''
AnkitThakur@gmail.com
AnkitThakur94@gmail.com
ankit.thakur@thapar.edu
ankit_thankur-24-01-1994@my-work.net
'''


################################################
## Writing a regular expression which can match all the above 3 emails.
################################################

pattern = re.compile(r'[a-zA-z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
    # first charaacter set explanation : [a-zA-Z0-9.-] : match the range of a-z / A-Z / 0-9 / '.' / '-'
matches = pattern.finditer(emails)

print ( ' ---- ')
print ( ' -- Matching emails  --  - ' )
for match in matches :
    print (match)


################################################
# capturing information from regexps.
################################################

urls = '''
https://www.google.com
http://something.com
https://youtube.com
https://www.google.gov
'''

# we need to compile a regular expression which can match these url's and extract the website name and domain name from them (Ex : google.com)


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')      # we have placed 2nd and 3rd ()'s because we want to capture the website and domain name.
    # The above patern has 4 groups (i.e set of patterns placed b.w () )
        # group 0 : the entire pattern
        # group 1 : (www\.)
        # group 2 : (\w+)
        # group 3 : (\.\w+)

matches = pattern.finditer(urls)

print ( ' ---- ')
print ( ' -- Matching urls --  - ' )
for match in matches :
    print ( ' group 0 : ' , match.group(0) )
    print ( ' group 1 (www : optional) : ' , match.group(1) )
    print ( ' group 2 (website name) : ' , match.group(2) )
    print ( ' group 3 (domain name) : ' , match.group(3) )



# Using backreferences for substitution. ( \1 \2 \3 .. and so on)

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')      # we have placed 2nd and 3rd ()'s because we want to capture the website and domain name.
subbed_urls = pattern.sub(r'\2\3', urls)

print ( ' ---- ')
print ( ' -- Substituting urls --  - ' )
print ( subbed_urls)


#######################################
# Checking if a pattern exists or not
    # Use pattern.search instead of pattern.finditer
    # returns None if no match found.
########################################

pattern = re.compile(r'dne')
matches = pattern.search(text_to_search)

if (matches == None):
    print ( ' No matchh ')


