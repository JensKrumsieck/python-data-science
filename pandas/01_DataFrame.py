import pandas as pd

df = pd.DataFrame(
    {
        "id": [0, 1, 2],
        "name": ["Cedric", "Morpheus", "Morph"],
        "age": [28, 28, 28]
    }
)

print(df)
print(df["age"].describe())
print(pd.Series([1, 2, 3], name="lol"))
