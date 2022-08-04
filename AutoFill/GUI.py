# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:33:43 2022

@author: Mohamad Idrees
"""

from tkinter import *                                                   
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image
import googlesearch   #pip install google
import numpy as np
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import re
from operator import itemgetter


class Google_Search:
    def __init__(self):
        #creating main window
            window = Tk()
            #title of window
            window.title("Google Search Engine")
            #window size
            window.geometry("1000x500")

            window.resizable(0,0)

            window.iconbitmap('Google.ico')

            #google logo

            g_logo=ImageTk.PhotoImage(Image.open('google logo.png'))
            l2=Label(window,image=g_logo)
            l2.pack()
            # variables to store inputs
            self.pv = StringVar()

            # varianbles for outputs
            self.output = StringVar()

            # text boxes to hold inputs and outputs
            entry1 =Entry(window,width=95,textvariable=self.pv)
            entry1.pack(pady=(20, 0), padx=50)
            Label(window, textvariable =self.output,font ="Helvetica 12 bold",justify=RIGHT).pack()

            Button(window, text="Show result", command=self.calcPayment).pack()
            window.mainloop()
    def calcPayment(self):
        output = self.pv.get()
        ngrams = {}
        words = 1
        real_dic={}
        with open('Data_Eco.txt',encoding="utf8") as f:
            contents = f.read()    
            
        contents = re.sub(r'[^A-Za-z. ]', '', contents)

        words_tokens=nltk.word_tokenize(contents)
        for i in range(len(words_tokens)-words):
            seq = ' '.join(words_tokens[i:i+words])
            if  seq not in ngrams.keys():
                ngrams[seq] = []
                real_dic[seq]=[]
            ngrams[seq].append(words_tokens[i+words])
            Prop=[]
            Prop.append((words_tokens[i+words]))
            temp=seq+" "
            Prop.append(contents.count(temp+words_tokens[i+words])/contents.count(words_tokens[i+words]))
            real_dic[seq].append(Prop)
            
        curr_sequence=output
        check=0
        the_real_output=[]
        for i in range(1):
            if curr_sequence not in real_dic.keys():
                possible_words="The data was not find your word"
                break
            check=1
            possible_words = real_dic[curr_sequence]

        if (check==1):
            final_result=sorted(possible_words,key=itemgetter(0))
            print(possible_words)
            

            for x in final_result:
                the_real_output.append(x[0])
          
        else:
            the_real_output.append(possible_words)
            
        
        
        self.output.set(the_real_output)


Google_Search()
