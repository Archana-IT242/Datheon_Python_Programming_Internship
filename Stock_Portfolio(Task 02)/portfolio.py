import csv

# 1. User se holdings ka input lena
ticker = input("Enter Stock Ticker Symbol (e.g. AAPL, TSLA): ").upper()
shares = float(input(f"Enter number of shares for {ticker}: "))
buy_price = float(input(f"Enter buy price per share ($): "))
current_price = float(input(f"Enter current market price ($): "))

# 2. Calculations (Total value aur Gain/Loss)
total_invested = shares * buy_price
current_value = shares * current_price
profit_loss = current_value - total_invested
gain_loss_pct = (profit_loss / total_invested) * 100

# 3. Terminal par summary dikhana
print("\n--- PORTFOLIO SUMMARY ---")
print(f"Stock: {ticker}")
print(f"Total Invested: ${total_invested:.2f}")
print(f"Current Value: ${current_value:.2f}")
print(f"Profit/Loss: ${profit_loss:.2f} ({gain_loss_pct:.2f}%)")

# 4. Results ko CSV file mein save karna
with open("portfolio_summary.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    # File Header
    writer.writerow(["Ticker", "Shares", "Buy Price", "Current Price", "Total Invested", "Current Value", "Profit/Loss", "Gain/Loss %"])
    # File Row Data
    writer.writerow([ticker, shares, buy_price, current_price, total_invested, current_value, profit_loss, f"{gain_loss_pct:.2f}%"])

print("\nSaved to portfolio_summary.csv successfully!")