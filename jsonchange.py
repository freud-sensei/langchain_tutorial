import pandas as pd
from tqdm.auto import tqdm
empathy_df = pd.read_csv("empathy_corpus.csv")
validation_df = pd.read_csv("validation_corpus.csv")

def csv2jsonl(df, outname):
    with open(outname, "w", encoding="utf-8") as f:
        for line in tqdm(df.iterrows()):
            question = line[1]["hs"].replace("'", "''").replace("\n", " ")
            answer = line[1]["ss"].replace("'", "''").replace("\n", " ")
            prompt = "You are a counselling psychologist speaking in Korean."
            script = f'{{"messages": [{{"role": "system", "content": "{prompt}"}}, {{"role": "user", "content": "{question}"}}, {{"role": "assistant", "content": "{answer}"}}]}}\n'
            f.write(script)

csv2jsonl(empathy_df, "empathy_corpus.jsonl")
csv2jsonl(validation_df, "validation_corpus.jsonl")