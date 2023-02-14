#get some words translate

words = {'paper':'qog\'oz', 'bread':'non', 'soup':'sho\'rva'}
user_words = ['paper', 'bread', 'soup']
user_word = input('Type just simple words \n... ')
if user_word.lower() in words:
    print(f'Here is your word\'s translate: \n{words[user_word]}')
else:
    print(f'This word does not exist in there! \nOnly this words in there:\n{user_words}')

