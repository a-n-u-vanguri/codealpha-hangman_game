import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=["Ticker", "Shares", "Purchase Price", "Current Price", "Current Value", "Profit/Loss"])

    def add_stock(self, ticker, shares, purchase_price):
        if ticker in self.portfolio['Ticker'].values:
            print(f"Stock {ticker} already exists in the portfolio.")
            return

        new_stock = pd.DataFrame([[ticker, shares, purchase_price, None, None, None]], 
                                 columns=["Ticker", "Shares", "Purchase Price", "Current Price", "Current Value", "Profit/Loss"])
        self.portfolio = pd.concat([self.portfolio, new_stock], ignore_index=True)
        print(f"Added {shares} shares of {ticker} at ${purchase_price} each to the portfolio.")

    def remove_stock(self, ticker):
        if ticker in self.portfolio['Ticker'].values:
            self.portfolio = self.portfolio[self.portfolio['Ticker'] != ticker]
            print(f"Removed {ticker} from the portfolio.")
        else:
            print(f"Stock {ticker} not found in the portfolio.")

    def update_portfolio_value(self):
        total_value = 0

        for index, row in self.portfolio.iterrows():
            ticker = row['Ticker']
            shares = row['Shares']

            stock = yf.Ticker(ticker)
            stock_info = stock.history(period="1d")
            current_price = stock_info['Close'].iloc[0]

            self.portfolio.loc[self.portfolio['Ticker'] == ticker, 'Current Price'] = current_price
            current_value = shares * current_price
            self.portfolio.loc[self.portfolio['Ticker'] == ticker, 'Current Value'] = current_value

            purchase_price = row['Purchase Price']
            profit_loss = (current_price - purchase_price) * shares
            self.portfolio.loc[self.portfolio['Ticker'] == ticker, 'Profit/Loss'] = profit_loss

            total_value += current_value

        return total_value

    def display_portfolio(self):
        if self.portfolio.empty:
            print("Your portfolio is empty.")
        else:
            print(self.portfolio)
            print("\n")

    def calculate_total_profit_loss(self):
        total_profit_loss = self.portfolio['Profit/Loss'].sum()
        return total_profit_loss

def main():
    portfolio = StockPortfolio()

    portfolio.add_stock('AAPL', 10, 150)  # Apple, 10 shares at $150 each
    portfolio.add_stock('GOOGL', 5, 2800)  # Google, 5 shares at $2800 each
    portfolio.add_stock('AMZN', 3, 3400)   # Amazon, 3 shares at $3400 each

    portfolio.display_portfolio()

    total_value = portfolio.update_portfolio_value()
    print(f"Total Portfolio Value: ${total_value:.2f}")

    total_profit_loss = portfolio.calculate_total_profit_loss()
    print(f"Total Profit/Loss: ${total_profit_loss:.2f}")

    portfolio.remove_stock('GOOGL')

    portfolio.display_portfolio()

if __name__ == "__main__":
    main()
