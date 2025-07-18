import pandas

data = pandas.read_csv("original.csv")

data.drop(columns=["app_id", "app_name", "review_votes"], inplace=True)

data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

data["review_score"] = data["review_score"].replace(-1, 0)

positive_reviews = data[data["review_score"] == 1].sample(10000, random_state=32)
negative_reviews = data[data["review_score"] == 0].sample(10000, random_state=32)

cleaned_data = pandas.concat([positive_reviews, negative_reviews]).sample(20000, random_state=32)

cleaned_data.to_csv("steam.csv", index=False)
