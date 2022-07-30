def sortByLengthFunction(e):
    return len(e)


f = open('crossword_words.txt', 'r')
words = f.readlines()
for i in range(len(words)):
    if('\n' in words[i]):
        words[i] = words[i][:-1]
    words[i] = words[i].upper()
uniq_words = set(words)
words = list(uniq_words)
f.close()

answers = []
alphabets = input(
    "Input your alphabets you have (Ex. A B C D) : ").upper()
alphabets_list = []
for alphabet in alphabets:
    if(alphabet != ' '):
        alphabets_list.append(alphabet)
alphabets = alphabets_list
alphabets_count = {}

for word in words:
    if(len(word) <= len(alphabets)):
        answers.append(word)

for alphabet in alphabets:
    alphabets_count[alphabet] = alphabets.count(alphabet)

deleted_words = []
for answer in answers:
    for alphabet in answer:
        if((alphabet not in alphabets_count) or (answer.count(alphabet) > alphabets_count[alphabet])):
            deleted_words.append(answer)
            break


answers = list(set(answers).difference(set(deleted_words)))
answers.sort(key=sortByLengthFunction, reverse=True)
answers_length_count = {}
for answer in answers:
    answers_length_count[str(len(answer))] = []

for answer in answers:
    answers_length_count[str(len(answer))].append(answer)

for length in answers_length_count:
    print(f"{length} : {answers_length_count[str(length)]}")
