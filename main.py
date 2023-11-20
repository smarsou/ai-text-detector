import torch
from transformers import pipeline
import csv
import os

def is_generated_by_ai(paragraph,model):
    # Load the text classification pipeline
    text_classifier = pipeline("text-classification", model=model)

    # Classify the input paragraph
    result = text_classifier(paragraph)

    # You can adjust this threshold based on experimentation
    confidence_threshold = 0.5

    # Check if the label is consistent with AI-generated text
    label = result[0]['label']
    confidence = result[0]['score']
    if label == 'LABEL_1' and confidence >= confidence_threshold:
        return ["AI",confidence]
    else:
        return ["Human",confidence]
    
def analyse_data(filename):
    file_path = os.path.join(os.path.dirname(__file__),"data",filename)
    i=0
    with open(file_path, "r", encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            print(row)
            i+=1
            if i>5:
                break
    

analyse_data("train_essays.csv")

if __name__ == "__main__" :
    input_text = "This is an example paragraph."
    model = "nlptown/bert-base-multilingual-uncased-sentiment"
    #generated_by_ai = is_generated_by_ai(input_text,model)
    #print("The text seems to be generated by " + generated_by_ai[0] + " with a confidence of "+ str(generated_by_ai[1]))

    