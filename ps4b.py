# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: start 11am

import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        #makes input a message class   initialise the vars/methods
        # i assume text is the userinput of word
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        # this gets the load_words to get the wordlist



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
        return self.valid_words.copy[:]


    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string).          
        '''
        count = 0
        Upper_count = 0
        alphabet ="abcdefghijklmnopqrstuvwxyz"
        Lower_alphabet_list = list(alphabet)
        Upper_alphabet_list = list(alphabet.upper())

        lower_dict = {j:i for i,j in enumerate(Lower_alphabet_list)}

        for lower_alphabet_keys in lower_dict:
            letta = lower_alphabet_keys      # iternates throguh all letters
            lower_dict.update({letta: count + shift})   # updates letter and value with the shift
            count +=1                                  # count increase
            if lower_dict[lower_alphabet_keys] > 25:    #  if above 25(0-25 range = 26)
                count -= 25+ shift                          # gives value of 0             
                lower_dict.update({letta:count + shift})         # assign value of 0
                count += 1


        upper_dict = {j:i for i,j in enumerate(Upper_alphabet_list)}

        for upper_alphabet_keys in upper_dict:
            Upper_letta = upper_alphabet_keys      # iternates throguh all letters
            upper_dict.update({Upper_letta: Upper_count + shift})   # updates letter and value with the shift
            Upper_count +=1                                  # count increase
            if upper_dict[upper_alphabet_keys] > 25:    #  if above 25(0-25 range = 26)
                Upper_count -= 25+ shift                          # gives value of 0             
                upper_dict.update({Upper_letta:count + shift})         # assign value of 0
                Upper_count += 1

        

        Full_Dict = upper_dict + lower_dict
        return Full_Dict

 
        #perhaps there is only 1 dictionary with A:0  and a:0   an  d B:1 and b:1
        #oh no i misunderstood.  it maps a letter to another letter
        # so already applies the shift on the dctionary,
        # so would make A:E    and have a:e    in the same dictionary when applying shift of 4
        #where A:1 becomes A:5
        
        # define list, turn into dictionary, set corresponding letter to the alphanumerical number, difine the shift number and implement the shift to the dictionary
            

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        applied_shift = ""
        shift_dictionary = self.build_shift_dict(shift)

        
        for letters in self.message_text:
            try:
                shifted_letter = shift_dictionary[letters]
                applied_shift += shifted_letter
            except KeyError:
                applied_shift += letters

        return applied_shift     

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

         

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift


    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        # copy because its mutable
        return self.encryption_dict[:]

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted

        '''
        return self.message_text_encrypted
        

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''

        # this touches on class variables
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)
        #legit do not under stand this 



        


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

        

    def decrypt_message(self):
        '''
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        valid_count = 0
        biggest_valid_count = 0
        decrypted_return = {} # create a tuple, dict or list or smthing) to return both shift value and text msg


        # should this be a letter or the number corresponding to the letter   i think its the numhber
        # but its default assignment is letter corresponding ot 0?!
        # there can be multiple number, so create a tuple.
        decrypted_list = []
        wordlist =load_words(WORDLIST_FILENAME)



        for shift_count in range(26):
            # iterate through the alphabet range

            # then decrypt 
            decrypt_msg = self.apply_shift(shift_count) # need to call this right? itssfrom a diffrernt class
            decrypted_list = decrypt_msg.split()
            # also have to split the decrypted string into a list?   use split

            for words in decrypted_list : # self msg is not converted yet and not listed format

                if is_word(wordlist, words) == True:     # need to call this right? itssfrom a diffrernt class
                    valid_count +=1

        
            if valid_count > biggest_valid_count:
                biggest_valid_count = valid_count
                return_value = shift_count
            valid_count = 0   
        decrypted_return ["FinalValue"] = return_value
        return (decrypted_return["FinalValue"],self.apply_shift(return_value) ) 
        
        


reveal_secret_msg  = CiphertextMessage(get_story_string())
print (reveal_secret_msg)




if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())
    pass

