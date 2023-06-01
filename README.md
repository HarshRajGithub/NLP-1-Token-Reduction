# NLP-1-Token-Reduction
A python program to reduce token using NLTK library. This can be used to reduce token from a file or chat entered further a code to use the reduced prompt for GPT-3 is given.
To use the program just enter the text in input or upload the file and the token reduction works.This Program on an average reduces the token count by 27 to 33 percent without losing any meaning.

The following program uses lemmatization and removal of stop words concept for token reduction.
This methods can be easily applied using NLTK library available for python.

Lemmatization - Is a natural language processing technique used to reduce words to their base or root form. The goal of lemmatization is to group together different forms of a word so that they can be analyzed as a single item.

The algorithm for lemmatization involves several steps:

1.)Tokenization: The text is first broken down into individual words or tokens.

2.)Part-of-speech (POS) tagging: Each word is then tagged with its part of speech, such as noun, verb, adjective, or adverb.

3.)Lemmatization: The lemmatization algorithm then uses a dictionary or rule-based system to convert each word to its base form, or lemma, based on its part of speech. For example, the word "running" would be converted to "run" as a verb, but not as a noun.

4.)Stemming: In some cases, the lemmatization algorithm may also use stemming, which involves removing the suffixes from words to reduce them to their base form.

However, stemming can sometimes result in incorrect or non-existent words, so it is not always used.
Overall, the lemmatization algorithm is designed to improve the accuracy and efficiency of natural language processing tasks by reducing the complexity of the text and grouping together related words.
Applied by using NLTK library

Stopwords - The algorithm for NLTK (Natural Language Toolkit) stopwords, which is a technique used to remove common words from text that are not useful for analysis. The goal of stopwords is to reduce the size of the text and improve the accuracy of natural language processing tasks.

The algorithm for NLTK stopwords involves several steps:

1.)Tokenization: The text is first broken down into individual words or tokens.

2.)Stopword removal: The NLTK stopwords algorithm then uses a predefined list of common words, such as "the", "and", "a", and "in", to remove them from the text. These words are considered to be "stopwords" because they do not carry much meaning and are not useful for analysis.

3.)Filtering: After the stopwords have been removed, the NLTK stopwords algorithm may also apply additional filtering to remove words that are too short or too long, or that contain numbers or special characters.

4.)Lemmatization or stemming: Finally, the NLTK stopwords algorithm may also apply lemmatization or stemming to reduce the remaining words to their base form, as described in my previous response.

Overall, the NLTK stopwords algorithm is designed to improve the accuracy and efficiency of natural language processing tasks by removing common words that are not useful for analysis. By reducing the size of the text and focusing on the most meaningful words, the algorithm can help to improve the accuracy of text classification, sentiment analysis, and other natural language processing tasks.

Applied by using NLTK library

# The program asks the user to give input whose token is to be reduced 

input_prompt = input("Please start the chat- ")

# If one wnats they can upload file instead by uncommenting

'''input_prompt = 'filename.txt'
file = open(input_prompt , 'rt')

text = file.read()

file.close()

split into words by white space

words = text.split()

split based on words only

import re

words = re.split(r'\W+', text)
'''

# This is to remove punctuation -

table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

Now one can use RegexpTokenizer which is beneficial for for regular expression or wordtokenizer which tokenizes all words. The program uses word Tokenizer by default.

#tokens = RegexpTokenizer("[\w']+")

#tokens.tokenize(input_prompt)

tokens = word_tokenize(input_prompt)  #split into words

# To removal of stop words-

stop_words = set(stopwords.words('english'))

words = [w for w in words if not w in stop_words]

To perform Stemming on the prompt after removing stopwords

stemmer = PorterStemmer()

stemmed_tokens = [stemmer.stem(words) for words in words]

# To perform Lemmatization on the prompt after removing stopwords

lemmatizer = WordNetLemmatizer()

lemmatized_tokens = [lemmatizer.lemmatize(words) for words in words]

Now the following code is used for Conversion of tokens back to sentences

text_final = nltk.Text(lemmatized_tokens)

# The obtained text can be used as input for GPT-3 by uncommenting the following code-

'''import openai

def askGPT(text):
    openai.api_key = "your_api_key"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
    )
    return print(response.choices[0].text)
def main():
    while True:
        askGPT(text_final)

main()
'''

To use this program one needs to install the library NLTK by pasting the following command in command prompt-

python.exe -m pip install nltk
