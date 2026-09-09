import math, re

def tokenize(text): return re.findall(r"[a-z0-9]+", text.lower())
def score(query, doc):
    q=set(tokenize(query)); d=set(tokenize(doc))
    return len(q & d) / max(1, math.sqrt(len(q)*max(1,len(d))))
def retrieve(query, docs, k=3):
    ranked=sorted(((score(query,d),d) for d in docs), reverse=True)
    return [d for s,d in ranked[:k] if s>0]
