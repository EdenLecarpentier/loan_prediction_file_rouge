from transformers import pipeline , AutoTokenizer , AutoModelForSequenceClassification

import torch 
import torch.nn.functional as f





#save_directory = "projet_sentimen_analysis_e2"
#tokenizer.save_pretrained(save_directory)
#model.save_pretrained(save_directory)
#
#tokenizer = AutoTokenizer.from_pretrained(save_directory)
#model = AutoModelForSequenceClassification.from_pretrained(save_directory)

model_name = "palakagl/bert_TextClassification"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSequenceClassification.from_pretrained(model_name)

X_train = ["Hello i am Eden and i hate you !"]

batch = tokenizer(X_train , padding=True , truncation=True , max_length=512 , return_tensors="pt")
print(batch)

with torch.no_grad():
    outputs = model(**batch)
    labels_ids = torch.argmax(outputs.logits, dim=1)
    print(labels_ids)
    labels = [model.config.id2label[labels_ids] for labels_ids in labels_ids.tolist()]
    print(labels)