import pandas as pd
#DataFrame from a list
df = pd.DataFrame()
bikes = ["Bajaj","Tvs","Hero","Kawasaki","BMW"]
cars = ["Lamborghini","Hyundai","Ferrari","Ford","Masserati"]
df["Cars"] = cars
df["Bikes"] = bikes
print(df)
