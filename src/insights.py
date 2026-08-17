from __future__ import annotations
import pandas as pd

def negative_review_rate(predictions) -> float:
    s=pd.Series(predictions)
    return float((s.astype(str).str.lower().isin(['negative','1','neg'])).mean())

def top_error_examples(texts,y_true,y_pred,n=20):
    df=pd.DataFrame({'text':list(texts),'actual':list(y_true),'predicted':list(y_pred)})
    return df[df.actual!=df.predicted].head(n)
