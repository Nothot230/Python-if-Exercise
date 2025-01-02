Vowels = ['a', 'e', 'i', 'o', 'u']
B = input('Enter word: ')
if any(Vowel in B for Vowel in Vowels):
    print('The word contains vowels')
else:
    print('The word not contains any vowels')
