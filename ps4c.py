# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res



### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)

        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        modified_transposed_dict = {}
        modified_upper_transposed_dict = {}
        modified_lower_transposed_dict = {}
        permutation_count = 0
        listed_vowels_permutation = list(vowels_permutation)

        for vowel_letters in VOWELS_LOWER:
            modified_lower_transposed_dict[vowel_letters] = listed_vowels_permutation[permutation_count]
            permutation_count +=1

        for con_letters in CONSONANTS_LOWER:
            modified_lower_transposed_dict[con_letters] = con_letters
        permutation_count = 0
        for u_vowel_letters in VOWELS_UPPER:
            upper_vowel = listed_vowels_permutation[permutation_count]
            modified_upper_transposed_dict[u_vowel_letters] = upper_vowel.upper()
            permutation_count +=1

        for u_con_letters in CONSONANTS_UPPER:
            modified_upper_transposed_dict[u_con_letters] = u_con_letters

        modified_transposed_dict = Merge(modified_lower_transposed_dict, modified_upper_transposed_dict)

        return modified_transposed_dict    


            
        
        
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''

        non_interesting_char = " ' !@#$%^&*()-_=+{}[]|;:',.<>/?\""
        encrpyted_list = [char if char in non_interesting_char else transpose_dict[char] for char in self.message_text]
        return ''.join(encrpyted_list)
        #applied_cipher = []
        #raw_message = self.get_message_text()

        #for character in raw_message:
            #try:
               # applied_cipher.append(transpose_dict[character])
        # get the transposed dicitonary value in bracket
          #  except KeyError:
            # any other character thats not in alphabet.
          #      applied_cipher.append(character)
        #print(applied_cipher)
        #return applied_cipher



        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)
        #self.message_text = text
        #self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        word_list = load_words(WORDLIST_FILENAME)
        valid_count = 0
        max_count = 0
        most_correct_perm = ""
        decyphered_text  = ''
        Crip_text = ""
        #Crip_text = self.get_message_text()

        # now i know that im having trouble splitting the sentence into individual words!! 
        
        vowel_permutations = get_permutations(VOWELS_LOWER)

        for permutations in vowel_permutations:
            
            Crip_text = self.apply_transpose(self.build_transpose_dict(permutations))
            for words in Crip_text.split():   # dumbass, how iterate through a string?
                if is_word(word_list, words):
                    valid_count += 1
                    #this is not counting!! oml
                    # becuase i can't immediately pull WORDLIST_FILENAMEm need to initialise it at the top, dumbasss
            if valid_count > max_count:
                max_count = valid_count   #  this is only value of 1 in test case (its the ! that gives the one)
                most_correct_perm = permutations
            valid_count = 0
        
        decyphered_text =  self.apply_transpose(self.build_transpose_dict(most_correct_perm))
                
        print (max_count)        
        return decyphered_text          



            ## perm_list = list(permutations) 
            #perm_dict = {j:i for i,j in enumerate(VOWELS_LOWER)}
            #for keys in perm_dict.keys():
                #perm_dict.update({keys: perm_list[perm_dict[keys]]})
            # from this line and above, returns as expected   (all permutations)                



            
if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))   # yeah this returns a dictionary print instead of a string but whatevs
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    
    print("Decrypted message:", enc_message.decrypt_message())     # but this returns Hallu Wurld! not hello world. 
                                                                    # so part 1 works all fine, part 2 is the only problem
    
     


    #TODO: WRITE YOUR TEST CASES HERE




#YEAHHHHH COMPLETERED