# Song Word Embeddings

This is the repository that holds the work from the Neuroecon lab for **Song Word Embedding**. The premise of the project was to use songs to predict popular culture changes because songs may be a leading indicator and have the ability to influence culture. The corpus was taken from the Billboard Top 100 songs from 1958 - 2019. Feel free to reach out to albert_su@berkeley.edu for any questions.


# To Do List

1. Data Cleaning: Triple check data by hand to get rid of artist names, make everything lowercase, check why certain corpuses have more words than others and try to fix this problem.
2. Redo the closest words by comparing analogies and words using cosine similarity instead of euclidean distance(see 8/24 presentation for what was done using Euclidean distance)
3. To find most similar words to emotion, get use a basket of synonyms instead of just one word. (Look at gender stereotype papers for more)
4. Change word frequency proportions by normalizing # of words(see 8/24 presentation)
5.  Figure out what went wrong with dynamic word embeddings and re-train glove vectors using dynamic word embeddings. (See vincent's dynamicword2vec github repo for training instructions)

# Explanations of Content

The folder has most scripts that are required to continue the research, however, most pre-trained vectors, lyrics corpuses, and other large files are not on the github due to the 100MB max repository size rule. Reach out to albert_su@berkeley.edu and we can figure something out to get you the vectors and data.

### Drugs of Abuse

This holds the majority of the things used in the drugs of abuse project, where we tried to use the song corpus to predict the popularity of certain illegal drugs over time. The .ipynb are jupyter notebooks which were mostly used to scrape, clean, and merge different songs from the LyricsGenius API. One important file is the *billboard.py* script which is the scraper that gets data from the LyricsGenius API. Run this with **py billboard.py** to start scraping songs. However, you need the list of songs to do this which is not in the github repo. 

### Glove

This folder has everything required to train glove vectors. Simply add a corpus to the folder and modify the *demo.sh* file accordingly. Then run *make* and *demo.sh* in terminal to start training vectors. There are also instructions [here](https://github.com/stanfordnlp/GloVe) but they are not too clear so reach out if you have any questions.

# Other
Email albert_su@berkeley.edu if you have any questions and if you need the data.
