print("Start entering words: ")
words_list = []
while True:
    word = input()
    if word not in words_list:
        words_list.append(word)
    else:
        print(f'You already entered {word}.')
        print(f'You listed {len(words_list)} distinct words.')



        
    
