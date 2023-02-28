import os
import time

import openai
import wandb as wandb

import pandas as pd

#data=pd.read (the prepared data that is ready for classification)
openai.api_key = "" #openai API
prediction_table = wandb.Table(columns=["prompt", "completion"])
for kw in data["itemLabel"][:20]:
  gpt_prompt="Classify this keyword to a category."+"\n\nKeyword:"+kw+"\nCategory:"
  response = openai.Completion.create(
    model="text-davinci-003",
    # swap model selection after fine-tuning
    prompt=gpt_prompt,
    temperature=0,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
  )
  print(len(prediction_table.data))
  prediction_table.add_data(kw,response['choices'][0]['text'])
  if len(prediction_table.data)%30==0:
    time.sleep(60) #set up the sleep interval to avoid a rate limit error
