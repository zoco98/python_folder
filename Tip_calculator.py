billAmount = float(input("What is the amount of your bill: "))
tipPercentage = float(input("How much you want to tip in percentage(%): "))
headsCount = int(input("How many people wants to split bills: "))

billAmountWithTip = billAmount * (1 + (tipPercentage/100))
perHeadBill = billAmountWithTip / float(headsCount)

roundPerHeadBill1 = round(perHeadBill,2)
roundPerHeadBill2 = "{:.2f}".format(perHeadBill)
print(f"Each of the person needs to contribute {roundPerHeadBill1} rupees")

print(f"Each of the person needs to contribute {roundPerHeadBill2} rupees")
