nouns = ['cats', 'sheep', 'dogs', 'people', 'glass']
plural = [nouns[i] for i in range(0, len(nouns)) if nouns[i][-1]=='s']
print(plural)