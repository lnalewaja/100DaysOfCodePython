# "What is your current age?"
# "You have ___ days, ____ weeks, and ____ months left"

# 1 year = 365 days, 52 weeks, 1 year

def Life_In_Weeks():
    total_days = 90 * 365
    total_weeks = 90 * 52
    total_months = 90 * 12
    
    age = int(input("What is your current age? (Years): "))

    rem_days = total_days - (age * 365)
    rem_weeks = total_weeks - (age * 52)
    rem_months = total_months - (age * 12)

    print(f"You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left!")


Life_In_Weeks()
