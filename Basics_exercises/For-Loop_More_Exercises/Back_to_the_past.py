received_money = float(input())
year_till_live = int(input())

# , че за всяка четна (1800, 1802 и т.н.) година ще харчи 12 000 лева. За всяка нечетна (1801,1803  и т.н.)
# ще харчи 12 000 + 50 * [годините, които е навършил през дадената година].
age_completed = 18
spend = 0
for i in range(1800, year_till_live + 1):
    age_completed += 1
    if i % 2 == 0:
        spend += 12000
    else:
        spend += 12000 + (50 * (age_completed - 1))
if received_money >= spend:
    print(f"Yes! He will live a carefree life and will have {abs(received_money - spend):.2f} dollars left.")
else:
    print(f"He will need {abs(received_money - spend):.2f} dollars to survive.")
