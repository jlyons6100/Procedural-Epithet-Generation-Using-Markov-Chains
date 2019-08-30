# Procedural-Epithet-Generation-Using-Markov-Chains

### Introduction:
As an amateur writer, I have a lot of trouble coming up with excellent epithets. In an effort to streamline the process of creating epithets, I'm going to use Markov Chains to procedurally generate epithets instead of coming up with them on my own. 

### Related Work:
Simple epithet generators are common online. However, I don't really like the epithets created by these generators. They aren't nearly as complex as the epithets created by great authors like R.R. Martin. My goal is to create something that I would like to use as a writer. 

### Dataset:
I have difficulty finding a dataset containing example epithets (See Issue 1). At first my idea was to use Natural Language Text Processing to extract sentences containing names/epithets from PDFs of the Game of Thrones books. However, I realized that there is an easier way to do things. I can scrape a webpage containing the character list, store the character list in a database and use a hashmap/dictionary to see if sentence from the PDFs contains a name. Better idea would be a trie. O(n) when n is the length of the string, instead of O(1) access in a hashmap, but in order to use a hashmap of names, I'd have to split every string in O(m), where m is the number of words in the string, then iterate back over the words AGAIN. Strictly slower to use a hashmap in this case. 

### Methods:


### Results:


### Summary / Issues:
#### 1. No great public data set for epithets.
To start the project I need a data set to create the probability distribution for the transitions in my Markov chain. After not finding a data set, my second idea was that I could just write out thousands of epithets myself. I quickly scrapped that idea because I don't have that much free time (Technically I do, but I don't wishto spend it doing that). Also, if I wanted to just create my own epithets why would I be trying to generate them?! One possible workaround I've thought of would be to download PDF versions of the Game of Thrones books, extracting text from the PDFs, using Natural Language Text Processing to extract sentences containing names/epithets, and building a data base of character names mapped to their epithets


### Plan of Attack:
#### 1. Scrape wiki of character names
#### 2. Save scrapped names to database
#### 3. Using pandas, insert character names into a Trie
#### 4. Find PDFs of Game of Thrones books
#### 5. Use trie to extract sentences containing names
#### 6. Manually search sentences for epithets
#### 7. Create epithet Database
#### 8. Create code to procedurally generate epithets using Markov Chains
#### 9. See if I actually like the generated epithets.
#### 10. Iteratively improve project
### How to Use:


### File Descriptions:
