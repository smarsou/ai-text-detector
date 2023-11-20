# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:59:03 2023

@author: leo-t
"""

import torch
from transformers import pipeline,BertTokenizer,BertForQuestionAnswering,BertConfig
from transformers import LlamaForCausalLM, LlamaTokenizer
import csv
import os

def generate(N):
    R = [["id","prompt_id","text","generated"]]
    #model=BertForQuestionAnswering(BertConfig())
    tokenizer = LlamaTokenizer.from_pretrained("/output/path")
    model = LlamaForCausalLM.from_pretrained("/output/path")
    text_genere = pipeline("question-answering", model=model,tokenizer=BertTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment"))
    file_path = os.path.join(os.path.dirname(__file__),"data","train_prompts.csv")
    file_output = os.path.join(os.path.dirname(__file__),"data","train_prompts_result.csv")
    n = 1
    with open(file_path, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            i=0
            for row in csv_reader:
                if i==0:
                    i+=1
                else:
                    for i in range(int(N/2)):
                        output = text_genere(question=row[2][:20],context=row[3][:20])
                        print(output)
                        reponse = output["answer"]
                        R.append([n,row[0],reponse,1])
                        n+=1
    with open(file_output,"w",encoding='utf-8') as f:
        csv_writer=csv.writer(f)
        csv_writer.writerows(R)
                
    
if __name__ == "__main__" :
    generate(2)