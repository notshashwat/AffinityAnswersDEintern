# AffinityAnswersDEintern
##Introduction

There can be various techniques of NLP that can be used to solve this task - Tranformers, Seq-toSeq models but I settled on a simple information retrieval approach after reading a [tweet analysis research paper](https://www.nature.com/articles/s41599-019-0280-3), particularly - on average 10-15 words are used in a tweet , which means a simple vector similarity approach without even considering the TFiDF score would work well enough for this use case as almost all words in a tweet are used only once.


##Data set

I used a kaggle dataset of bad words

##Results

Input - 

this is a good sentence with no bad words

this has the bad words incest and shiting

this is really obscene jeez, scum AND sodomize


Output -

this is a good sentence with no bad words
 = 0.0

this has the bad words incest and shiting
 = 0.25

this is really obscene jeez, scum AND sodomize
 = 0.3333333333333333


##Problems with this approach - 

This approach is context agnostic which can give wrong results. For example, the term 'monkey' might be a racial slur when talking about a person but not a racial slur when talking about the animal. For training a model that can work with context we would need large amount of data to train the model on and more advanced models like attention, LSTMs, etc.
