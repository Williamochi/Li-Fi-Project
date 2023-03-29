print('End of Receiving')
print(len(RECEIVE))
colormode = RECEIVE[0:4]
if colormode == '1010':
    colormode = 'L'
else:
    colormode = 'RGB'
RECEIVE = RECEIVE[4:] + ['31']
print('End of Receiving')
print(len(RECEIVE))
rec_word = string.join(RECEIVE)
rec_word = rec_word.replace('131','')
counter = counter + 1
print(len(rec_word))
text_file = open("code.txt", "wt")
n = text_file.write(rec_word)
text_file.close()