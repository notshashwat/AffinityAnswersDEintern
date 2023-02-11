
def main():
		
	import pandas
	import nltk
	from nltk.stem.porter import PorterStemmer
	# nltk.data.path.append('/home/shashwat/nltk_data/tokenizers')
	nltk.download('punkt')
	from nltk.tokenize import word_tokenize

	## Stemming using Porter Stemmer
	stemmer = PorterStemmer()
	df = pandas.read_csv('bad-words.csv')
	slur = set(stemmer.stem(x) for x in df['jigaboo'])
	
	#makign a set of the bad words for O(1) look up


	f_tweet = open("tweets.txt","r")
	#read file  of tweets

	raw = []
	final_data=[]
	for tweet in f_tweet:
		raw.append(tweet)
		
		tokenized_tweet = word_tokenize(tweet)


		stemmed_tweet = [stemmer.stem(word) for word in tokenized_tweet]
		final_data.append(stemmed_tweet)
	f_tweet.close()


	score = list()#used to store the profanity score of sentence i 
	for tweet in final_data:
		slur_count=0
		total_words=0
		for word in tweet:
			
			if word in slur:
				# print(word)
				slur_count+=1
			total_words+=1
		score.append(slur_count/total_words)

	ans_file = open("ans.txt","w")

	for i in range(len(final_data)):
		ans=raw[i]+" = "+str(score[i])+"\n"
		# print(ans)
		ans_file.write(ans)

	ans_file.close()

if __name__ == "__main__":
	main()

