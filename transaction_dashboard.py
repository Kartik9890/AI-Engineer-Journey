
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("transactions.csv")

# 2. Calculate KPIs
total_transactions = len(df)
total_amount = df["amount"].sum()

success_count = (df["status"] == "SUCCESS").sum()
failed_count = (df["status"] == "FAILED").sum()
pending_count = (df["status"] == "PENDING").sum()

success_rate = success_count / total_transactions * 100
failure_rate = failed_count / total_transactions * 100

# 3. Prepare chart data
status_counts = df["status"].value_counts()
payment_counts = df["payment_mode"].value_counts()
mode_amounts = df.groupby("payment_mode")["amount"].sum()

# 4. Create figure
fig = plt.figure(figsize=(14, 9))
fig.suptitle("Payment Transaction Dashboard", fontsize=18)

# 5. KPI cards
kpis = [
    ("Total Transactions", f"{total_transactions}"),
    ("Total Amount", f"₹{total_amount:,}"),
    ("Success Rate", f"{success_rate:.1f}%"),
    ("Failure Rate", f"{failure_rate:.1f}%")
]

for i, (label, value) in enumerate(kpis):
    fig.text(
        0.13 + i * 0.24, 0.88,
        f"{label}\n{value}",
        ha="center",
        fontsize=13
    )

# 6. Create four charts
axes = [
    fig.add_axes([0.08, 0.55, 0.38, 0.23]),
    fig.add_axes([0.55, 0.55, 0.38, 0.23]),
    fig.add_axes([0.08, 0.12, 0.38, 0.28]),
    fig.add_axes([0.55, 0.12, 0.38, 0.28])
]

# Chart 1: Transaction status
bars = axes[0].bar(
    status_counts.index,
    status_counts.values
)
axes[0].bar_label(bars)
axes[0].set_title("Transaction Status")
axes[0].set_ylabel("Count")

# Chart 2: Payment mode distribution
axes[1].pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct="%1.1f%%"
)
axes[1].set_title("Payment Mode Distribution")

# Chart 3: Transaction amount distribution
axes[2].hist(df["amount"], bins=5, edgecolor="black")
axes[2].set_title("Transaction Amount Distribution")
axes[2].set_xlabel("Amount")

# Chart 4: Total amount by payment mode
bars = axes[3].bar(
    mode_amounts.index,
    mode_amounts.values
)
axes[3].bar_label(bars, fmt="%.0f")
axes[3].set_title("Total Amount by Payment Mode")
axes[3].set_ylabel("Amount (₹)")

# 7. Display dashboard
plt.show()

# Save dashboard as PNG
plt.savefig("payment_dashboard.png", dpi=300, bbox_inches="tight")

# Save dashboard as PDF
plt.savefig("payment_dashboard.pdf", bbox_inches="tight")

plt.show()