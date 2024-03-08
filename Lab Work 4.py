"""
    Program Purpose: To calculate the total units sold calculation, highest sales identification, above average customer reviews identification,
                    average customer review score calculation and below average sales identification.
    Programmer: MUHAMMAD AFIF NAQIUDDIN BIN OTHMAN
    Date: 8 March 2024
"""

# Sample lists of flower names, units sold, and customer reviews
flower_names = ["Rose", "Chrysanthemum", "Sunflower", "Tulip", "Carnation"]
units_sold = [121, 145, 132, 200, 69]
customer_reviews = [3.8, 3.6, 1.4, 4.0, 2.6]

# Additional data for 15 more flowers
additional_flower_names = ["Daffodil", "Daisy", "Snapdragon", "Azalea", "Calla lily", "Marigold", "Peony", "Zinnia",
                            "Hyacinth", "Lavender", "Pansy", "Aconite", "Adam's Needle", "Adder's Tongue", "Agapanthus"]
additional_units_sold = [141, 90, 55, 128, 267, 100, 30, 47, 80, 135, 235, 210, 65, 70,270]
additional_customer_reviews = [1.7, 4.8, 2.3, 3.1, 2.6, 1.1, 2.9, 1.5, 2.6, 1.9, 3.1, 4.0, 3.4, 3.2, 2.4]

# Combining the lists for all flowers
all_flower_names = flower_names + additional_flower_names
all_units_sold = units_sold + additional_units_sold
all_customer_reviews = customer_reviews + additional_customer_reviews

# Calculate the total number of units sold for all flowers
total_units_sold = sum(all_units_sold)
print("Total units sold for all flowers:", total_units_sold)

# Determine the flower with the highest sales
max_units_sold = max(all_units_sold)
index_of_max = all_units_sold.index(max_units_sold)
flower_with_highest_sales = all_flower_names[index_of_max]
print("Flower with the highest sales:", flower_with_highest_sales)

# Identify flowers with the average customer reviews above 3
above_avg_reviews_flowers = [flower for flower, review in zip(all_flower_names, all_customer_reviews) if review > 3]
print("Flowers with average customer reviews above 3:", above_avg_reviews_flowers)

# Calculate the average customer review score for all flowers
average_review_score = sum(all_customer_reviews) / len(all_customer_reviews)
print("Average customer review score for all flowers:", average_review_score)

# Identify flowers with below average sales
below_avg_sales_flowers = [(name, sold, review) for name, sold, review in zip(all_flower_names, all_units_sold, all_customer_reviews) if sold < total_units_sold / len(all_units_sold)]
print("Flowers with below-average sales:")
for flower in below_avg_sales_flowers:
    print("Flower Name:", flower[0])
    print("Units Sold:", flower[1])
    print("Customer Review:", flower[2])
