#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:56:48 2020

@author: cartervandemoore
"""
#create an initial version of a TextModel class,
#which will serve as a blueprint for objects that model a body of text

#returns a list of words after 'cleaning' out a string txt
def clean_text(txt):
    txt=txt.lower()
    txt=txt.replace('.', '')
    txt=txt.replace(',', '')
    txt=txt.replace('?', '')
    txt=txt.replace('!', '')
    txt=txt.replace(';', '')
    txt=txt.replace(':', '')
    txt=txt.replace('"', '')
    lst_ans=txt.split(" ")
    return lst_ans
  
class TextModel():
    
    #Constructor
    def __init__(self, model_name):
        self.name=model_name
        self.words={}
        self.word_lengths={}
    
    
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        return s
    
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
        to all of the dictionaries in this text model."""
        word_list=clean_text(s)
        for w in word_list:
            if w not in self.words:
                self.words[w]=1
            else:
                self.words[w]+=1
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)]=1
            else:
                self.word_lengths[len(w)]+=1

        # Add code to update other feature dictionaries.
    
    #adds all of the text in the file identified by filename to the model
    def add_file(self, filename):
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()      # read it all in at once!
        f.close()
        self.add_string(text)
            
    #saves the TextModel object self by writing its various 
    #feature dictionaries to files
    def save_model(self):
        d = self.words                              # Create a sample dictionary.
        f = open(self.name + '_' + 'words', 'w')              # Open file for writing.
        f.write(str(d))                             # Writes the dictionary to the file.
        f.close()                                   # Close the file.
        d1 = self.word_lengths                      # Create a sample dictionary.
        f = open(self.name + '_' + 'word_lengths', 'w')      # Open file for writing.
        f.write(str(d1))                           # Writes the dictionary to the file.
        f.close()                                  # Close the file.
        
    #reads the stored dictionaries for the called TextModel object from their 
    #files and assigns them to the attributes of the called TextModel
    def read_model(self):
        f = open(self.name + '_' + 'words', 'r')                  # Open for reading.
        d_str = f.read()                                # Read in a string that represents a dict.
        f.close()
        self.words = dict(eval(d_str))                           # Convert the string to a dictionary.
        print("Inside the newly-read dictionary, d, we have:")
        print(self.words)
        f = open(self.name + '_' + 'word_lengths', 'r')          # Open for reading.
        d1_str = f.read()                              # Read in a string that represents a dict.
        f.close()
        self.word_lengths = dict(eval(d1_str))                         # Convert the string to a dictionary.
        print("Inside the newly-read dictionary, d, we have:")
        print(self.word_lengths)
        