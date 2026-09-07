from statistics import mean, stdev


def calculate_returns(prices):
    """Calculate percentage returns between consecutive prices."""
    return [
        ((prices[i] - prices[i - 1]) / prices[i - 1]) * 100
        for i in range(1, len(prices))
    ]


def moving_average(prices, period=5):
    """Calculate the simple moving average."""
    if len(prices) < period:
        raise ValueError("Not enough data for this period.")

    return mean(prices[-period:])


def market_summary(prices):
    """Return a basic market summary."""
    returns = calculate_returns(prices)

    return {
        "current_price": prices[-1],
        "average_price": mean(prices),
        "moving_average_5": moving_average(prices, 5),
        "volatility": stdev(returns) if len(returns) > 1 else 0,
        "total_return": ((prices[-1] / prices[0]) - 1) * 100,
    }


if __name__ == "__main__":
    # Example price data
    prices = [
        100, 101, 99, 102, 104,
        103, 106, 105, 108, 110
    ]

    summary = market_summary(prices)

    print("Market Analysis")
    print("-" * 30)

    for key, value in summary.items():
        print(f"{key}: {value:.2f}")