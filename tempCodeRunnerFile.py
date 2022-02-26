from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
df['sentiment']=sentiment_pipeline(df['Content'])
df.to_csv("sentinet.csv")