import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("transactions.csv")

status_counts = df["status"].value_counts()

plt.bar(
    status_counts.index,
    status_counts.values,
    color=["green", "red", "orange"]
)

plt.title("Payment Transaction Status")
plt.xlabel("Status")
plt.ylabel("Number of Transactions")

plt.show()