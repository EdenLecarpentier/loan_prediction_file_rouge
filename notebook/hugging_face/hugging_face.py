from transformers import pipeline , AutoTokenizer , AutoModelForSequenceClassification

import torch 
import torch.nn.functional as f

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("sentiment-analysis" , model= model_name , tokenizer=tokenizer)

results = classifier("We are verry unhappy but happy to be alive ")
for result in results :   
    print(result)
tokens = tokenizer.tokenize("We are verry unhappy but happy to be alive ")
token_ids = tokenizer.convert_tokens_to_ids(tokens)
input_ids = tokenizer("We are verry unhappy but happy to be alive ")
print(tokens)
print(token_ids)
print(input_ids)

X_train = "We are verry unhappy but happy to be alive "

batch = tokenizer(X_train , padding=True , truncation=True , max_length=512 , return_tensors="pt")
print(batch)

with torch.no_grad():
    outputs = model(**batch)
    #, labels=torch.tensor([1,0])
    #when using pytorch you need to put the **
    print(outputs)
    predictions = torch.softmax(outputs.logits , dim=1)
    print(predictions)
    labels = torch.argmax(predictions , dim=1)
    print(labels)
    labels = [model.config.id2label[label_id] for label_id in labels.tolist()]
    print(labels)

save_directory = "projet_sentimen_analysis_e2"
tokenizer.save_pretrained(save_directory)
model.save_pretrained(save_directory)

tokenizer = AutoTokenizer.from_pretrained(save_directory)
model = AutoModelForSequenceClassification.from_pretrained(save_directory)