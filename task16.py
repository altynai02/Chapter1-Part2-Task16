# 16. If you were on the moon now, your weight will be 16,5% of your earth weight.
# To calculate it you have to multiple to 0,165. If next 15 years your weight will
# increase 1 kg each year. What will be your weight each year on the moon next
# 15 years?

your_weight = int(input("Enter your weight: "))
moon_weight = your_weight * 0.165
year = 0
cur_moon_weight = moon_weight
while year <= 14:
    year+=1
    cur_moon_weight+=0.165
    print("The year is",year,"your weight",cur_moon_weight)