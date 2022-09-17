import random

articles=('The', 'A', 'Are', 'They')
subjects=('dog', 'cat', 'man', 'woman')
verbs=('sang', 'ran', 'jumped', 'goes')
adverbs=('loudly', 'quietly', 'well', 'badly')

i = 0

for _ in [1, 2, 3, 4, 5]:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    if random.randint(0, 1) == 0:
        print(article, subject, verb)
    else:
        adverb = random.choice(adverbs)
        print(article, subject, verb, adverb)