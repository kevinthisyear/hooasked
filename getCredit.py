# initialize user inputs
x = int(input("What is the length of your credit history (in years): "))
y = int(input("How many accounts do you have? "))
z = int(input("How many hard inquiries have you had within the last 2 years? "))
a = int(input("What is your credit limit? "))
b = int(input("What is your amount of credit owed? "))
c = int(input("How many payments have you missed in the last 24 months? "))


def Calculate(lengthOfCreditHistory, totalAccounts, Inquiries, creditLimit, owed, History):

    # initialize users credit score
    score = 0

    # length of credit history affects 15% of your credit score ~127.5 points
    if lengthOfCreditHistory <= 3:
        score = score + 20
    if 3 < lengthOfCreditHistory < 15:
        score = score + 89
    if lengthOfCreditHistory >= 15:
        score = score + 127

    # total accounts affects 10% of your credit score ~85 points
    if totalAccounts <= 5:
        score += 85
    if 5 < totalAccounts < 10:
        score = score + 60
    if totalAccounts >= 10:
        score = score + 0

    # Inquiries affects 10% of your credit score ~85 points
    if Inquiries == 0:
        score += 85
    if Inquiries == 1:
        score = score + 60
    if Inquiries > 1:
        score = score + 0

    # Amount Owed affects 30% of your credit score ~255 points
    if owed == 0:
        score += 255

    # Payment History affects 35% of your credit score ~297 points
    if History == 0:
        score += 297

    return score

total = Calculate(x,y,z,a,b,c)

if total == 0:
    print(str(total) + ": How does this happen; your score is impossibly low")

if total < 580:
    print(str(total) + ": Poor | Your score is worse than the majority of US consumers. Lenders may be wary")

if 580 < total < 669:
    print(str(total) + ": Fair | Your score is below the average of US consumers. Many lenders will still accept this score.")

if 670 < total < 739:
    print(str(total) + ": Good | Your score is near or slightly above the average of US consumers. Most lenders will find this a good score.")

if 740 < total < 799:
    print(str(total) + ": Very Good | Your score is above the average of US consumers. Lenders will consider you a dependable borrower.")

if total > 800:
    print(str(total) + ": Exceptional | Your score is better than the majority of US consumers. Lenders will consider you an exceptional borrower.")