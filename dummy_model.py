import pandas as pd
from sklearn.linear_model import LogisticRegression
import mlflow.sklearn

df = pd.read_csv("https://github.com/bgweber/Twitch/raw/master/Recommendations/games-expand.csv")

local_path = "serialized_model"
x = df.drop(['label'], axis=1)
y = df['label']
model = LogisticRegression()
model.fit(x, y)

mlflow.sklearn.save_model(model, local_path)