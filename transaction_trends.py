import pandas as pd
import matplotlib.pyplot as plt

data = {
    "date": [
        "2026-11-01", "2026-11-01",
        "2026-11-02", "2026-11-02",
        "2026-11-03", "2026-11-03",
        "2026-11-04", "2026-11-04"
    ],
    "txn_id": [
        "TXN301", "TXN302",
        "TXN303", "TXN304",
        "TXN305", "TXN306",
        "TXN307", "TXN308"
    ],
    "amount": [500, 800, 1200, 600, 1500, 900, 2000, 700]
}

df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date"])

daily_transactions = df.groupby("date")["txn_id"].count()

plt.plot(
    daily_transactions.index,
    daily_transactions.values,
    marker="o"
)

plt.title("Daily Transaction Volume")
plt.xlabel("Date")
plt.ylabel("Number of Transactions")

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
