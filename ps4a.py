# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    def put_string_first_letter (first_letter, word_list):
        list_listed_list = []
        return_list =[]


        for words in word_list:
            list_listed_list.append(list(words))
        
        for listed_word in list_listed_list:

           for i in range(len(listed_word)+1):
                listed_word.insert(i, first_letter)
               
                return_list.append(''.join(listed_word))
                listed_word.remove(first_letter)

              
        return return_list      


    if len(sequence) == 1:
        return list(sequence) 
    else:

        return put_string_first_letter(sequence[0], get_permutations(sequence[1::1]))


 

print(get_permutations("band"))
    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

