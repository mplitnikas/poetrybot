import nltk
import string
import random

class Markov():

	def __init__(self, text, corpus=None):
		if corpus:
			self.words = corpus

		if text:
			self.text = text
			print("Splitting words...")
			self.words = self.split_text(text)
	
		self.word_size = len(self.words)
		print("%d words." % self.word_size)
		self.chains = list(self.build_rev_ngram_triples(self.words))


		self.db = {}
		print("Compiling database...(this may take a while)")
		self.database()
		self.save_db()

	def save_db(self):
		pass

	def split_text(self, text_input):
		#words = nltk.word_tokenize(text_input)
		words = text_input.split()
		#words = [word.lower() for word in words]
		#words = [word.translate(string.maketrans("",""), string.punctuation) for word in words]
		return words

	def build_ngram_triples(self, corpus):

		for i in range(len(corpus)-2):
			yield (corpus[i], corpus[i+1], corpus[i+2])

	def build_rev_ngram_triples(self, corpus):

		for i in range(2, len(corpus)):
			yield (corpus[i], corpus[i-1], corpus[i-2])


	def database(self):
		number_finished = 1
		db_num = self.word_size - 2
		for triple in self.chains:
			#if len(triple) < 3:
			#	continue
			
			# using two root words to determine the next one
			key = (triple[0], triple[1])

			if key in self.db.keys():
				self.db[key].append(triple[2])
			else:
				self.db[key] = [triple[2]]

			print("DB entry number %d / %d" % (number_finished, db_num))
			number_finished += 1

	def find(self, lst, a):
		return random.choice([i for i,x in enumerate(lst) if x==a])

	def constuct_chain(self, length=25, seed_choice=None):
		if (seed_choice is not None): # takes seed_choice as a tuple
			print('using ' + str(seed_choice))
			w1, w2 = seed_choice
		else:
			seed = random.randint(0, self.word_size - 2)
			seed_word, next_word = self.words[seed], self.words[seed-1] # changed sign
			w1, w2 = seed_word, next_word

		gen_words = []
		for i in xrange(length):
			gen_words.append(w1)
			w1, w2 = w2, random.choice(self.db[(w1, w2)])
		gen_words.append(w2)
		return ' '.join(gen_words[::-1]) # flip order of words since string is built backwards