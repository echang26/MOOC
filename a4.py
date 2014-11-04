# a4.py
""" Functions for Assignment A4"""


# Task 1: Word Lists

def build_word_list(filename):
    """Returns a list of words from the given file
    
    Each word in the file should stored on a separate line. The lines are trimmed 
    to remove trailing spaces and line returns. 
    
    Example: build_word_list('short.txt') returns the 10 element list of words
    ['the','be','to','of','and','a','in','that','have','it'].
    
    Precondition: filename is the name of a text file storing a list of words.
    
    Enforced Precondition: filename is a string"""
    # IMPLEMENT ME
    word_list = []
    file = open(filename)
    for line in file:
        real_line = line.strip()
        word_list.append(real_line)
    file.close()
    return word_list


def word_list_by_size(words, size):
    """Returns the elements of words that have length size
    
    The words in the resulting list should be in the same order as the original list.
    
    Example: word_list_by_size(['a', 'at', 'axe', 'by'], 2) returns ['at','by']
    
    Precondition: words is a list of strings. size is a positive int.
    
    Enforced Precondition: words a list. size is a positive int."""
    list_by_size = []
    for word in words:
        if len(word) == size:
            list_by_size.append(word)
    return list_by_size


def word_list_extend(words, prefix):
    """Returns the word list that is the result of adding prefix to the start of 
    every word in the list words.
    
    The resulting word list is sorted alphabetically.
    
    Example: word_list_extend(['at', 'rap'], 'c') returns ['cat', 'crap'].
    
    Precondition: words is a list of strings. prefix is a string.
    
    Enforced Precondition: words is a list. prefix is a string."""
    extended_list = []
    for word in words:
        extended_list.append(prefix + word)
    return extended_list



# Task 2: Prefix Maps

def pmap_add_word(pmap,word):
    """Adds a single word to a prefix map.
    
    This is a procedure.  It modifies the contents of pmap. It does not return.
    a new prefix map.  
    
    This function will add the word AND all of its prefixes to pmap.  For each
    prefix it will add the next letter to the list of values.  For the complete word, 
    it will add '' to the list of values. 
    
    This function does not add duplicates to the prefix map.  If a letter is already
    in the list for a given prefix map, then it will not add it a second time.
    
    Example: If pmap is the empty map {}, then pmap_add_word(pmap,'at') changes
    pmap to the dictionary { '':['a'], 'a':['t'], 'at':[''] }.

    Example: If pmap is { '':['a'], 'a':['t'], 'at':[''] }, pmap_add_word(pmap,'as') 
    changes pmap to { '':['a'], 'a':['s', 't'], 'at':[''], 'as':[''] }.
    
    Precondition: pmap is a prefix map.  word is a string with only letters.
    
    Enforced Precondition: pmap is a dict. word is a string with only letters."""
    if word not in pmap:
        pmap[word] = ['']
        word_length = len(word)
        if word[0 : word_length - 1] in pmap.keys():
            if word[-1] not in pmap[word[0 : word_length - 1]]:
                pmap[word[0 : word_length - 1]].append(word[-1])
        else:
            pmap[word[0 : word_length - 1]] = [word[-1]]

    elif word in pmap:
        if '' not in pmap[word]:
            pmap[word].append('')
    if '' in pmap:
        if word[0] not in pmap['']:
            pmap[''].append(word[0])
    else:
        pmap[''] = [word[0]]        

    
def word_list_to_pmap(words):
    """Returns the prefix map for the given word list.
    
    Hint: pmap_add_word is a useful helper function.
    
    Precondition: words is a list of strings with only letters.
    
    Enforced precondition: words is a list."""
    # IMPLEMENT ME
    prefixes = {}
    for word in words:
        pmap_add_word(prefixes, word)
    return prefixes

def pmap_to_word_list(pmap):
    """Returns the word list for the given prefix map.
    
    The word list should contain only those prefixes which have a next character
    of '' (the empty string) in the prefix map.
    
    Precondition: pmap is a prefix map.
    
    Enforced Precondition: pmap is a dict."""
    # IMPLEMENT ME
    words = []
    for prefix in pmap:
        if '' in pmap[prefix]:
            words.append(prefix)
    return words


def pmap_has_word(pmap,word):
    """Returns True if word is in the prefix map.
    
    Precondition: pmap is a prefix map.  word is a string.
    
    Enforced Precondition: pmap is a dict. word is a string."""
    # IMPLEMENT ME
    if word in pmap.keys():
        if '' in pmap[word]:
            return True
    return False

# PART C: Word Completions

def autocomplete(prefix, pmap):
    """Returns the list of all words the complete prefix in pmap
    
    If there are no words completing prefix in pmap, this function returns the
    empty list.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    autocomplete('th',pmap) returns the list ['the', 'that'].  
    Similarly, autocomplete('x',pmap) returns the empty list []
    
    Precondition: prefix is a string that is either empty or has only letters. 
    pmap is a prefix map.
    
    Enforced Preconditions: We enforce the preconditions for prefix, but only
    enforce that pmap is a dict."""
    # This function will require recursion combined with a for-loop.  The base
    # case is when prefix is not in the prefix map.  Otherwise, you will need
    # to process all of the values in the list pmap[prefix].
    
    # Be careful with pmap[prefix]. If prefix is an actual word then '' is in this
    # list.  If you are not careful with your recursive call, then you will find
    # yourself in an infinite recursion.
    
    # NOTE: This function MUST be recurse, and you are not allowed to add any
    # helper functions to implement this function.
    
    if prefix not in pmap:
        return []
    else:
        final_words = []
        for item in pmap[prefix]:
            new_prefix = prefix + item
            if item != '':
                final_words += autocomplete(new_prefix, pmap)
            else:
                final_words.append(new_prefix)
    return final_words     



# PART D: Scrabble Puzzles

def scrabble(rack,size,pmap):
    """Returns the list of all valid words that you can form from the tile rack
    using EXACTLY size letters.
    
    The prefix map pmap is used to determine whether or not a word is valid.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    scrabble('theob',2,pmap) returns ['be', 'to'].
    
    Precondition: rack is a string that is either empty or has only letters. 
    size is a nonnegative integer. pmap is a prefix map.
   
    Enforced Precondition: We enforce the complete precondition for rack and size.
    We only enforce that pmap is a dict."""
    # We are not going to assert the preconditions here
    # We will let you do that in the helper function.

    return scrabble_helper('',rack,size,pmap)


def scrabble_helper(prefix,rack,size,pmap):
    """"Returns the list of all valid words extending prefix that you can form from
    the tile rack using EXACTLY size ADDITIONAL letters.
    
    The prefix map pmap is used to determine whether or not a word is valid.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    scrabble_helper('t','heob',1,pmap) returns ['to'], while 
    scrabble_helper('t','heob',2,pmap) returns ['the']

    Precondition: prefix and rack are a strings with only letters, but which may
    be empty. size is a nonnegative integer. pmap is a prefix map.
   
    Enforced Precondition: We enforce the complete precondition for prefix, rack, 
    and size. We only enforce that pmap is a dict."""
    # This function is to be implemented recursively using the process that was
    # described in the assignment overview.  At each recursive call, you will remove 
    # a letter from the rack and add it to the prefix.  Note that,  unlike scramble, 
    # size is not the number of letters in the word. It is the number of letters 
    # REMAINING to pick from the rack. So you must decrease it in the recursive call
    # as well.
    
    # This recursive function will have multiple base cases:
    
    #     1. size is 0 (so no letter left to pick)
    #     2. size > 0, but rack is empty (so there is nothing left to pick from)
    #     3. there are no words that complete prefix
    
    # In the case of 2 and 3, you should return the empty list.
    words = []
    if size == 0:
        return []
    elif len(rack) == 0:
        return []
    elif len(autocomplete(prefix, pmap)) < 1:
        return []
    else:
        for letter in rack:            
            new_rack = rack.replace(letter, '')
            new_prefix = prefix + letter
            if size == 1:
                if new_prefix in pmap:
                    if '' in pmap[new_prefix]:
                        words.append(new_prefix)
            else:
                words += scrabble_helper(new_prefix, new_rack, size - 1, pmap)
    return words


def match(template,pmap):
    """Returns the list of all valid words that match the given template.
    
    A template is a string combining letters and the '?' character.  A
    word is a match of for a template if it is the same length, and agrees
    with the template on every character that is not '?'. For example,
    'ate' matches the template 'a?e', as does 'axe'.
    
    The prefix map pmap is used to determine whether or not a word is valid.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    match('i?',pmap) returns ['in', 'it'].
    
    Precondition: template is a string of letters and '?'. pmap is a
    prefix map.
    
    Enforced Precondition: template is a string. pmap is a dict."""
    # We are not going to assert the preconditions here
    # We will let you do that in the helper function.
    return match_helper('',template,pmap)


def match_helper(prefix,template,pmap):
    """Returns the list of all valid words that start with the given prefix, and
    whose remaining letters match the given template.
    
    Unlike match, the template in this case is not supposed to match the whole
    string. It is only supposed to match the remaining part of the string after
    the prefix.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    match_helper('i','?',pmap) returns ['in', 'it'].
    
    Precondition: prefix is a string of letters or empty. template is either empty or
    string of letters and '?'. pmap is a prefix map.
    
    Enforced Precondition: prefix is a string of letters or empty. template is a string. 
    pmap is a dict."""
    # This function is to be implemented recursively using a process that is similar
    # to, but not the same as scrabble.  At each recursive call, you will remove
    # the first element from template.  If it is a letter, you add it to the prefix.
    # If it is a '?', you must try each valid extension of the prefix.
    
    # There are two base cases: when there are no word that complete the prefix, and 
    # when the template is empty.  In that second case, what you do depends on whether 
    # or not prefix is a word.
    final_matches = []
    if len(autocomplete(prefix, pmap)) < 1: 
        return []
    elif len(template) == 0:
        if '' in pmap[prefix]:
            final_matches.append(prefix)
            return final_matches
        else:
            return []            
    else:
        for letter in template:
            if letter != '?':
                new_prefix = prefix + letter
                new_template = template.replace(letter, '')
                if new_prefix not in pmap:
                    return []
                elif '' in pmap[new_prefix]:
                    if len(new_template) == 0:
                        final_matches += new_prefix
                else:
                    final_matches += match_helper(new_prefix, new_template, pmap)
            else:
                prefix_options = pmap[prefix]
                options = [prefix + option for option in pmap[prefix]]
                new_template = template.replace(letter, '')
                for item in options:
                    final_matches += match_helper(item, new_template, pmap)
        return final_matches
