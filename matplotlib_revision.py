
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read transaction data
df = pd.read_csv("transactions.csv")

# Step 2: Calculate transaction status counts
status_count = df["status"].value_counts()

# Step 3: Calculate total amount by payment mode
payment_total = df.groupby("payment_mode")["amount"].sum()

# Step 4: Create three subplots
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Chart 1: Transaction Status Bar Chart
bars = axes[0].bar(
    status_count.index,
    status_count.values,
    color=["green", "red", "orange"]
)

axes[0].set_title("Transaction Status")
axes[0].set_xlabel("Status")
axes[0].set_ylabel("Count")
axes[0].bar_label(bars)

# Chart 2: Payment Mode Pie Chart
axes[1].pie(
    payment_total.values,
    labels=payment_total.index,
    autopct="%1.1f%%",
    startangle=90
)

axes[1].set_title("Payment Mode Distribution")

# Chart 3: Transaction Amount Histogram
axes[2].hist(
    df["amount"],
    bins=5,
    edgecolor="black"
)

axes[2].set_title("Transaction Amount Distribution")
axes[2].set_xlabel("Amount (₹)")
axes[2].set_ylabel("Frequency")

# Step 5: Dashboard title and layout
fig.suptitle(
    "Payment Transaction Analytics Dashboard",
    fontsize=16
)

plt.tight_layout()

# Step 6: Save dashboard as an image
plt.savefig(
    "matplotlib_revision_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

# Step 7: Display dashboard
plt.show()
