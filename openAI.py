import os
import time

import openai
import wandb as wandb

import pandas as pd

data=pd.read_excel("zhihu-gpt3.xlsx",usecols="B")
openai.api_key = "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"
prediction_table = wandb.Table(columns=["prompt", "completion"])
for kw in data["itemLabel"][:20]:
  gpt_prompt="Classify this keyword to a category."+"\n\nKeyword:"+kw+"\nCategory:"
  response = openai.Completion.create(
    model="text-davinci-003",
    # model ="ada:ft-personal-2022-11-29-12-37-22",
    # model="davinci:ft-personal-2022-11-29-12-52-01", #training data with noise -->,/n, etc
    # model="davinci:ft-personal-2022-11-29-13-02-17",
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
    time.sleep(60)