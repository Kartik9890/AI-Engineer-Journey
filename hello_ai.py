import pandas as pd

df = pd.read_csv("transactions.csv")

print(df.head())

print("total transactions:", df.shape)

print("total amount:", df["amount"].sum() )

status_count = df["status"].value_counts()
total_transactions = df.shape[0]

print("\nTransaction status count:")
print(status_count)

status_percentage = df["status"].value_counts(normalize = True)*100

print("\nTransaction Status Percentage:")
print(status_percentage)

payment_analysis = df.groupby("payment_mode")["amount"].agg(["count", "sum", "mean"])

print("\nPayment Mode Analysis:")
print(payment_analysis)

failed_transctions = df[df["status"] == "FAILED"]

print("\nFailed Transaction Report")
print(failed_transctions)

failed_amount = failed_transctions["amount"].sum()

print("\nTotal Failed Amount: ", failed_amount)

successful_transactions = df[df["status"] == "SUCCESS"]

print("\nSuccessful Transaction Report:")
print(successful_transactions)

successful_amount = successful_transactions["amount"].sum()

print("\nTotal Successful Amount:", successful_amount)

successful_count = (df["status"] == "SUCCESS").sum()
failed_count = (df["status"] == "FAILED").sum()
pending_count = (df["status"] == "PENDING").sum()

success_rate = (successful_count / total_transactions) * 100
failure_rate = (failed_count / total_transactions) * 100

print("\nTransaction Summary")
print("Total Transactions:", total_transactions)
print("Successful:", successful_count)
print("Failed:", failed_count)
print("Pending:", pending_count)

print("Success Rate:", success_rate, "%")
print("Failure Rate:", failure_rate, "%")

# Filter high-value transactions
high_value_transactions = df[df["amount"] > 1500]

print("\nHigh Value Transactions:")
print(high_value_transactions)

print("\nTotal High Value Amount:",
      high_value_transactions["amount"].sum())

summary = df.groupby("status").agg(
    transaction_count=("txn_id", "count"),
    total_amount=("amount", "sum"),
    average_amount=("amount", "mean")
)

print("\nConsolidated Transaction Report:")
print(summary)

# Export failed transactions
failed_transctions.to_csv("failed_transactions.csv", index=False)

# Export payment mode analysis
payment_analysis.to_csv("payment_mode_report.csv")

# Export consolidated summary
summary.to_csv("transaction_summary.csv")

print("All reports exported successfully!")