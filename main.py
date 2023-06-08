import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import string
from flask import Flask, render_template, request
import requests
import openai
import os
from dotenv import load_dotenv


#remove  if these are already up to date
'''nltk.download('punkt')
nltk.download('stopwords')
nltk.download('corpus')
nltk.download('wordnet')'''


#load openai api key
load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

#set up Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Render the index template with the form
     return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get the user's input from the form
     user_input=request.form["message"]
     table = str.maketrans('', '', string.punctuation) # remove punctuation

# Tokenize input prompt
#sentences = sent_tokenize(input_prompt)   #split into sentences

#if one wants to use RegexpTokenizer
#tokens = RegexpTokenizer("[\w']+")
#tokens.tokenize(input_prompt)

     tokens = word_tokenize(user_input)  #split into words
     stripped = [w.translate(table) for w in tokens]
     words = [word for word in stripped if word.isalpha()]
     # Stop words
     stop_words = set(stopwords.words('english'))
     words = [w for w in words if not w in stop_words]

    # Perform stemming on tokens
     stemmer = PorterStemmer()
     stemmed_tokens = [stemmer.stem(words) for words in words]

# Perform lemmatization on tokens
     lemmatizer = WordNetLemmatizer()
     lemmatized_tokens = [lemmatizer.lemmatize(words) for words in words]

# Conversion of tokens back to sentences

# Convert list of tokens to NLTK text object
     text_final = nltk.Text(lemmatized_tokens)
    # Use the OpenAI API to generate a response
     prompt = f"User: {text_final}\nChatbot:"
     response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=prompt,
          temperature=0.5,
          max_tokens=60,
          top_p=1,
          frequency_penalty=0,
          stop=["\nUser: ","\nChatbot: "]
    )

    # Extract response from OpenAI API result
     bot_response=response.choices[0].text.strip()

    #Render the template with the response text
     return render_template(
        "response.html",
        user_input=f"{text_final}",
        bot_response=bot_response,
    )

# start the Flask app
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000, debug=True)
        
    
'''
For only Token Optimization
# Define input prompt
input_prompt = input("Please start the chat- ")

#for a text file
# load text
input_prompt = 'filename.txt'
file = open(input_prompt , 'rt')
text = file.read()
file.close()
# split into words by white space
words = text.split()
# split based on words only
import re
words = re.split(r'\W+', text)


table = str.maketrans('', '', string.punctuation) # remove punctuation

# Tokenize input prompt
#sentences = sent_tokenize(input_prompt)   #split into sentences

#if one wants to use RegexpTokenizer
#tokens = RegexpTokenizer("[\w']+")
#tokens.tokenize(input_prompt)

tokens = word_tokenize(input_prompt)  #split into words
stripped = [w.translate(table) for w in tokens]
words = [word for word in stripped if word.isalpha()]
# Stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

# Perform stemming on tokens
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(words) for words in words]

# Perform lemmatization on tokens
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(words) for words in words]

# Conversion of tokens back to sentences

# Convert list of tokens to NLTK text object
text_final = nltk.Text(lemmatized_tokens)


# Print results (Token)
print("Original tokens:", tokens)
print("After Removing Stop Words:",words)
print("Stemmed tokens:", stemmed_tokens)
print("Lemmatized tokens:", lemmatized_tokens)

# Print the resulting sentencesfor sentence in sentences_final:
print("Final text is:", text_final)
# For working with gpt-3


import openai

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
