# condition:
# if applicant has high income and good credit
#       Eligible for loan

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

# and, both statements have to be true
# or, one statement has to be true
# not, if its not true = false then if not false = true


# another example:
# if the applicant has good credit and does not has a criminal background
# then they are eligible for loan

has_criminal_record= False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
