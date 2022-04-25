import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import sys


def train():
    df = pd.read_csv("SBP.csv")

    x = df[["Age", "Weight"]]
    y = df["SBP"]

    regr = LinearRegression()
    regr.fit(x, y)

    joblib.dump(regr, "regr.pkl")


def load(age, weight) -> float:
    clf = joblib.load("regr.pkl")

    x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
    prediction = clf.predict(x)[0]
    return(prediction)


if __name__ == "__main__":
    train()
    print(load(sys.argv[1], sys.argv[2]))
