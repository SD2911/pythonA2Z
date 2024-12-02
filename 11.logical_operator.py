#if applicant has high income AND good credit eligible for loan.
high_income = True
good_credit = True

if high_income and good_credit: 
        print("eligible for loan")

high_income = False
good_credit = True

if high_income or good_credit: 
    print("Eligible for loan")  


high_income = True
good_credit = False

if high_income and not good_credit: 
    print("Eligible for loan")           