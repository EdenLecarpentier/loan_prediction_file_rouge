from pathlib import Path 
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset
from transformers import DistilBertTokenizerFast , DistilBertForSequenceClassification
from transformers import Trainer , TrainingArguments

# prepare dataset 
# load pretrained tokenizer , encoding 
# Build pytorch datataset with encoding 
#load pretrained model 
#load trainer and train it
# or use pytorch pipeline 

model_name = "distilbert-base-uncased"

def read_imdb_split(split_dir):
    split_dir = Path(split_dir)
    texts = []
    labels = []
    for label_dir in ["pos" , "neg"]:

        for text_file in (split_dir/label_dir).iterdir():
            texts.append(text_file.read_text())
            labels.append(0 if label_dir == "neg" else 1)
            
    return texts , labels

train_text , train_label = read_imdb_split("aclImdb")


test_text , test_label = read_imdb_split("aclImdb")


train_texts , val_texts , train_labels , val_labels = train_test_split(train_text , train_label , test_size=2)

class imdbdataset(Dataset): 
    def __init__(self , encodings , labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, index):
        item = {key: torch.tensor(val[index]) for key, val in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[index])
        return item

    def __len__(self):
        return len(self.labels)

tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)

train_encodings = tokenizer(train_texts , trucation=True , padding=True)
val_encodings = tokenizer(val_texts , trucation=True , padding=True)
test_encodings = tokenizer(test_text , trucation=True , padding=True)

train_dataset = imdbdataset(train_encodings , train_labels)
val_dataset = imdbdataset(val_encodings , val_labels)
test_dataset = imdbdataset(test_encodings , test_label)

training_args = TrainingArguments(
    output_dir="projet_sentimen_analysis_e2", 
    per_device_train_batch_size=16, 
    per_device_eval_batch_size=16, 
    warmup_steps=500,
    learning_rate=5e-5, 
    weight_decay=0.01,
    logging_dir="projet_sentimen_analysis_e2", 
    logging_steps=10,


)

model = DistilBertForSequenceClassification.from_pretrained(model_name)
trainer = Trainer(
    model=model,
    args=training_args, 
    train_dataset=train_dataset,
    eval_dataset=val_dataset

)

trainer.train()

