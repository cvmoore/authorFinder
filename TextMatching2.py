#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:56:48 2020

@author: cartervandemoore
"""
#create an initial version of a TextModel class,
#which will serve as a blueprint for objects that model a body of text

import math

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

#returns the stem / root of a given word
def stem(s):
    if len(s)>4 and s[-1]=="s" and s[-3]!="ies":
        s=s[:-1]
    if len(s)>4 and s[:2]=="un":
        s=s[2:]
    elif len(s)>4 and s[:3]=="dis":
        s=s[3:]
    elif len(s)>4 and s[:3]=="non":
        s=s[3:]
    elif len(s)>4 and s[:3]=="mis":
        s=s[3:]
    if len(s)>5 and s[-3:] == 'ing':
        if s[-4] == s[-5] and s[-4]!="l":
            s = s[:-4]
        elif s[-4] == s[-5] and s[-4]=="l":
            s = s[:-3]
        else:
            s = s[:-3]
    elif s[-2:] == 'er':
        if(len(s[:-2])==4):
            s = s[:-2]
        else:
            s = s[:-3]
    elif len(s)>4 and s[-3:] == 'ies':
        s=s[:-3]
        s=s+"y"
    return s

#returns the similarity score of two dictionaries
def compare_dictionaries(d1, d2):
    score=0
    total=0
    for key in d1:
        total+=d1[key]
    if total==0 or total==1:
        total=1.01
    for key in d2:
        if key in d1:
            score+=d2[key]*math.log(d1[key]/total)
        else:
            score+=d2[key]*math.log(.5/total)
    return score
  
class TextModel():
    
    #Constructor
    def __init__(self, model_name):
        self.name=model_name
        self.words={}
        self.word_lengths={}
        self.stems={}
        self.sentence_lengths={}
        self.conjunctions={}
    
    
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  the number of coordinating conjunctions is: ' + str(len(self.conjunctions)) + '\n'
        return s
    
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
        to all of the dictionaries in this text model."""
        s_length=1
        for c in s:
            if c==" ":
                s_length+=1
            elif "." in c or "!" in c or "?" in c:
                if s_length not in self.sentence_lengths:
                    self.sentence_lengths[s_length]=1
                else:
                    self.sentence_lengths[s_length]+=1
                s_length=0
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
            if stem(w) not in self.stems:
                self.stems[stem(w)]=1
            else:
                self.stems[stem(w)]+=1
            if w in "for and nor but or yet so":
                if w not in self.conjunctions:
                    self.conjunctions[w]=1
                else:
                    self.conjunctions[w]+=1

    
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
        d2 = self.stems                      # Create a sample dictionary.
        f = open(self.name + '_' + 'stems', 'w')      # Open file for writing.
        f.write(str(d2))                           # Writes the dictionary to the file.
        f.close()
        d3 = self.sentence_lengths                      # Create a sample dictionary.
        f = open(self.name + '_' + 'sentence_lengths', 'w')      # Open file for writing.
        f.write(str(d3))                           # Writes the dictionary to the file.
        f.close()
        d4 = self.conjunctions                      # Create a sample dictionary.
        f = open(self.name + '_' + 'conjunctions', 'w')      # Open file for writing.
        f.write(str(d4))                           # Writes the dictionary to the file.
        f.close()
        
    #reads the stored dictionaries for the called TextModel object from their 
    #files and assigns them to the attributes of the called TextModel
    def read_model(self):
        f = open(self.name + '_' + 'words', 'r')                  # Open for reading.
        d_str = f.read()                                # Read in a string that represents a dict.
        f.close()
        self.words = dict(eval(d_str))                           # Convert the string to a dictionary.
        f = open(self.name + '_' + 'word_lengths', 'r')          # Open for reading.
        d1_str = f.read()                              # Read in a string that represents a dict.
        f.close()
        self.word_lengths = dict(eval(d1_str))                         # Convert the string to a dictionary.
        f = open(self.name + '_' + 'stems', 'r')          # Open for reading.
        d2_str = f.read()                              # Read in a string that represents a dict.
        f.close()
        self.stems = dict(eval(d2_str))                         # Convert the string to a dictionary.
        f = open(self.name + '_' + 'sentence_lengths', 'r')          # Open for reading.
        d3_str = f.read()                              # Read in a string that represents a dict.
        f.close()
        self.sentence_lengths = dict(eval(d3_str))                         # Convert the string to a dictionary.
        f = open(self.name + '_' + 'conjunctions', 'r')          # Open for reading.
        d4_str = f.read()                              # Read in a string that represents a dict.
        f.close()
        self.conjunctions = dict(eval(d4_str))                         # Convert the string to a dictionary.
    
    #computes and returns a list of log similarity scores measuring the 
    #similarity of self and other â€“ one score for each type of feature 
    #(words, word lengths, stems, sentence lengths, and your additional feature)
    def similarity_scores(self, other):
        list1=[compare_dictionaries(other.words, self.words)]
        list2=[compare_dictionaries(other.word_lengths, self.word_lengths)]
        list3=[compare_dictionaries(other.stems, self.stems)]
        list4=[compare_dictionaries(other.sentence_lengths, self.sentence_lengths)]
        list5=[compare_dictionaries(other.conjunctions, self.conjunctions)]
        ans=list1+list2+list3+list4+list5
        return ans
    
    #compares the called TextModel object (self) to two other â€œsourceâ€ 
    #TextModel objects (source1 and source2) and determines which of these 
    #other TextModels is the more likely source of the called TextModel
    def classify(self, source1, source2):
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print("scores for "+source1.name+": "+str(scores1))
        print("scores for "+source2.name+": "+str(scores2))
        total1=0
        total2=0
        for x in range(len(scores1)):
            if scores1[x]>scores2[x]:
                total1+=1
            elif scores2[x]>scores1[x]:
                total2+=1
        if total1>total2:
            print(str(self.name)+" is more likely to have come from "+str(source1.name))
        else:
            print(str(self.name)+" is more likely to have come from "+str(source2.name))


def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
        

def run_tests():
    """ your docstring goes here """
    source1 = TextModel('TenthOfDecemberPart1')
    source1.add_file('TenthOfDecemberPart1.txt')

    source2 = TextModel('TheTellTaleHeartPart1')
    source2.add_file('TheTellTaleHeartPart1.txt')

    new1 = TextModel('TellTaleHeartPart2')
    new1.add_file('TellTaleHeartPart2.txt')
    new1.classify(source1, source2)   

    new2 = TextModel('TenthOfDecemberPart2')
    new2.add_file('TenthOfDecemberPart2.txt')
    new2.classify(source1, source2)

    new3 = TextModel('TheRaven')
    new3.add_file('TheRaven.txt')
    new3.classify(source1, source2)

    new4 = TextModel('HanselAndGretel')
    new4.add_file('HanselAndGretel.txt')
    new4.classify(source1, source2)     
        
        
        
        