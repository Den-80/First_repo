sentence_one = 'Hello world'
sentence_two = 'Hello ' + 'world'

print(sentence_one, sentence_two, sep='\n')

print(f'Sentences equal? {sentence_one == sentence_two}')
print(f'Sentences identical? {sentence_one is sentence_two}')

print(f'Path in memory {id(sentence_one)}')
print(f'Path in memory {id(sentence_two)}')