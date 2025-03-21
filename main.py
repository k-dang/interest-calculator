import math
import csv
import sys


def get_annual_rate_from_csv(
    principal: float, filename: str = "interest_rates.csv"
) -> float:
    """Retrieve the annual interest rate based on loan amount from a CSV file."""
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            amount, rate = map(float, row)
            if principal <= amount:
                return rate
    return 4.83  # Default rate if no match is found


def calculate_monthly_interest(principal: float, annual_rate: float) -> float:
    r = annual_rate / 100  # Convert percentage to decimal
    t = 1 / 12  # One month in years

    # Compute amount after one month with daily compounding
    A = principal * math.exp(r * t)

    # Interest accrued in one month
    return A - principal


def calculate_daily_interest(principal: float, annual_rate: float) -> float:
    r = annual_rate / 100  # Convert percentage to decimal
    daily_rate = r / 365  # Daily interest rate
    return principal * daily_rate


# Example usage
if __name__ == "__main__":
    print(sys.version)

    principal = float(input("Enter loan amount: "))
    annual_rate = get_annual_rate_from_csv(principal)
    print(f"Determined annual interest rate: {annual_rate}%")

    monthly_interest = calculate_monthly_interest(principal, annual_rate)
    daily_interest = calculate_daily_interest(principal, annual_rate)
    print(f"Monthly interest accrued: ${monthly_interest:.2f}")
    print(f"Daily interest accrued: ${daily_interest:.2f}")
