principal_amount = input("Enter the Principal Amount: ")
rate_of_interest = input("Enter the Rate of Interest (%): ")
time_period = input("Enter the Time Period (in years): ")

principal_amount = float(principal_amount)
rate_of_interest = float(rate_of_interest)
time_period = float(time_period)

simple_interest = (principal_amount * rate_of_interest * time_period) / 100

print("The Simple Interest is =", simple_interest)
