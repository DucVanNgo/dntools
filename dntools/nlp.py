import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def clean_and_tokenize(sentence,
                       language='english',
                       lowercase=True,
                       remove_digits=True,
                       remove_punctuation=True,
                       ):
    """Takes a string of a sentence as input and preprocesses the sentence for NLP.
    Outputs list of lemmatized words.

    sentence -> str: Input of a sentence with multiple words as string.

    language -> str - default is 'english': Language for which stopwords should be removed from the sentence.

    lowercase -> bool - default is True: Choose if tokens should be all lowercase.

    remove_digits -> bool - default is True: Choose if digits should be removed.


    """

    sentence = sentence.strip() ## remove whitespaces

    if lowercase:
        sentence = sentence.lower() ## lowercase

    if remove_digits:
        sentence = ''.join(char for char in sentence if not char.isdigit()) ## remove numbers

    if remove_punctuation:
        for punctuation in string.punctuation:
            sentence = sentence.replace(punctuation, '') ## remove punctuation

    tokenized_sentence = word_tokenize(sentence) ## tokenize
    stop_words = set(stopwords.words(language)) ## define stopwords

    tokenized_sentence_cleaned = [ ## remove stopwords
        w for w in tokenized_sentence if not w in stop_words
    ]

    lemmatized = [
        WordNetLemmatizer().lemmatize(word, pos = "v")
        for word in tokenized_sentence_cleaned
    ]

    lemmatized = [
        WordNetLemmatizer().lemmatize(word, pos = "n")
        for word in tokenized_sentence_cleaned
    ]

    cleaned_sentence = ' '.join(word for word in lemmatized)

    return cleaned_sentence
