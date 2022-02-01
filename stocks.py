#CS175L-01
#Julia Salerno
#stocks
COMMISSION_RATE = float(input("What was the comission rate?: "))
NUM_SHARES= int(input("How many shares did you purchase?: "))
PURCHASE_PRICE= float(input("What was the purchase price?: "))
SELLING_PRICE= float(input("What was the selling price?: "))
                    
amountPaidForStock= NUM_SHARES * PURCHASE_PRICE
purchaseCommission= COMMISSION_RATE * amountPaidForStock
totalPaid = amountPaidForStock+ purchaseCommission
stockSoldFor= SELLING_PRICE * NUM_SHARES
sellingCommission = stockSoldFor * COMMISSION_RATE
totalRecieved= stockSoldFor - sellingCommission
profitOrLoss= totalRecieved - totalPaid

print(f"Amount paid for stock: ${amountPaidForStock:,.1f}")
print(f"Commission paid of the purchase: ${purchaseCommission:,.1f}")
print(f"Amount the stock sold for: ${stockSoldFor:,.1f}")
print(f"Commission paid on the sale: ${sellingCommission:,.1f}")
print(f"Profit (or loss if negative): ${profitOrLoss:,.1f}")                     


                     
