def calculate_percentage(country_name, area):
    world_area = 148940000  # Total area of the world in square kilometers
    country_percentage = (area / world_area) * 100
    return f"{country_name} occupies {country_percentage:.2f}% of the total world's land"


country = "Oman"
area = 309501
percentage = calculate_percentage(country, area)
print(percentage)

country = "China"
area = 9562910
percentage_2 = calculate_percentage(country, area)
print(percentage_2)