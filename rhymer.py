
import nltk
import string

class Rhymer():

	def __init__(self, vocab):
		self.entries = nltk.corpus.cmudict.entries()
		
		print("Building corpus...")
		self.vocab = vocab.translate(string.maketrans("",""), string.punctuation)
		self.vocab = self.vocab.lower()
		self.cleaned_text = self.vocab.split()
		self.vocab = list(set(self.cleaned_text))
		print("Done!")

					#out = s.translate(string.maketrans("",""), string.punctuation)

		#self.vocab = set(self.vocab)
		# self.vocab should now represent all possible words in source text

	def rhyme(self, inp):
		try:
			syllables = self.get_syllables(inp)
		except:
			return Exception("That word is not in the lexicon")
		level = self.last_vowel_position(syllables)
		rhymes = []
		for (word, syllable) in syllables:
			rhymes += [word for word, pron in self.entries if pron[-level:] == syllable[-level:]]


		return list(set(rhymes) & set(self.vocab))
	
	def get_syllables(self, inp):
		syllables = [(word, syl) for word, syl in self.entries if word == inp]
		if not syllables:
			return Exception('Word does not exist in corpus!')
		return syllables
	
	def last_vowel_position(self, syll_inp):
		phonemes = syll_inp[0][1]
		for i in range(len(phonemes)):
			if phonemes[-i][-1].isdigit():
				return i
	
	def cadence(self, inp):
		raw_syllables = self.get_syllables(inp)
		#print raw_syllables
		syllable_count = 0
		for phoneme in raw_syllables[0][1]:
			if phoneme[-1].isdigit():
				syllable_count += 1
		return syllable_count