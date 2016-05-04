import pprint
import random
import rhymer, chainer


with open('bernie.txt', 'r') as fo:
#with open('sunalso.txt', 'r') as fo:
	content = fo.read()

#content = content.decode('utf-8')

r = rhymer.Rhymer(content)
lexicon = r.vocab	# set of all words (no duplicates)
clean_text = r.cleaned_text		# all words in order, lowercase and no punctuation
c = chainer.Markov(None, clean_text)


print c.find(clean_text, 'disease')
#print c.constuct_chain(length=10, seed_choice=('and', 'Jerry'))