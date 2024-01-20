
Pounds_Per_Talent = 20
Lots_Per_Pound = 32
Grams_Per_Lot = 13.3


talents = int(input("Enter the number of talents: "))
pounds = int(input("Enter the number of pounds: "))
lots = int(input("Enter the number of lots: "))


total_grams = (
    (talents * Pounds_Per_Talent + pounds) * Lots_Per_Pound + lots
) * Grams_Per_Lot

kilograms = total_grams // 1000
grams = total_grams % 1000


print(f"{talents} talents, {pounds} pounds, and {lots} lots is equal to:")
print(f"{kilograms} kilograms and {grams} grams.")
