import numpy as np  
import json
def save_sales_data(products, sales):
    data = {"products": products.tolist(), "sales": sales.tolist()}
    with open("sales_data.json", "w") as f:
        json.dump(data, f, indent=4)
        print("Sales data saved to sales_data.json")
def load_sales_data():
    try:
        with open("sales_data.json", "r") as f:
            data = json.load(f)
            products = np.array(data["products"])
            sales = np.array(data["sales"])
            print("Sales data loaded from sales_data.json")
            return products, sales
    except FileNotFoundError:
        print("No saved sales data found.")
        return None, None
month = np.array(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
def get_sales_data(month):
    products = np.array([input("Enter product 1: "), input("Enter product 2: "), input("Enter product 3: "), input("Enter product 4: "), input("Enter product 5: ")])
    sales = np.array([[float(input(f"Enter sales for month 1, {products[0]}: ")), float(input(f"Enter sales for month 1, {products[1]}: ")), float(input(f"Enter sales for month 1, {products[2]}: ")), float(input(f"Enter sales for month 1, {products[3]}: ")), float(input(f"Enter sales for month 1, {products[4]}: "))],
                  [float(input(f"Enter sales for month 2, {products[0]}: ")), float(input(f"Enter sales for month 2, {products[1]}: ")), float(input(f"Enter sales for month 2, {products[2]}: ")), float(input(f"Enter sales for month 2, {products[3]}: ")), float(input(f"Enter sales for month 2, {products[4]}: "))],
                  [float(input(f"Enter sales for month 3, {products[0]}: ")), float(input(f"Enter sales for month 3, {products[1]}: ")), float(input(f"Enter sales for month 3, {products[2]}: ")), float(input(f"Enter sales for month 3, {products[3]}: ")), float(input(f"Enter sales for month 3, {products[4]}: "))],
                  [float(input(f"Enter sales for month 4, {products[0]}: ")), float(input(f"Enter sales for month 4, {products[1]}: ")), float(input(f"Enter sales for month 4, {products[2]}: ")), float(input(f"Enter sales for month 4, {products[3]}: ")), float(input(f"Enter sales for month 4, {products[4]}: "))],
                  [float(input(f"Enter sales for month 5, {products[0]}: ")), float(input(f"Enter sales for month 5, {products[1]}: ")), float(input(f"Enter sales for month 5, {products[2]}: ")), float(input(f"Enter sales for month 5, {products[3]}: ")), float(input(f"Enter sales for month 5, {products[4]}: "))],
                  [float(input(f"Enter sales for month 6, {products[0]}: ")), float(input(f"Enter sales for month 6, {products[1]}: ")), float(input(f"Enter sales for month 6, {products[2]}: ")), float(input(f"Enter sales for month 6, {products[3]}: ")), float(input(f"Enter sales for month 6, {products[4]}: "))],
                  [float(input(f"Enter sales for month 7, {products[0]}: ")), float(input(f"Enter sales for month 7, {products[1]}: ")), float(input(f"Enter sales for month 7, {products[2]}: ")), float(input(f"Enter sales for month 7, {products[3]}: ")), float(input(f"Enter sales for month 7, {products[4]}: "))],
                  [float(input(f"Enter sales for month 8, {products[0]}: ")), float(input(f"Enter sales for month 8, {products[1]}: ")), float(input(f"Enter sales for month 8, {products[2]}: ")), float(input(f"Enter sales for month 8, {products[3]}: ")), float(input(f"Enter sales for month 8, {products[4]}: "))],
                  [float(input(f"Enter sales for month 9, {products[0]}: ")), float(input(f"Enter sales for month 9, {products[1]}: ")), float(input(f"Enter sales for month 9, {products[2]}: ")), float(input(f"Enter sales for month 9, {products[3]}: ")), float(input(f"Enter sales for month 9, {products[4]}: "))],
                  [float(input(f"Enter sales for month 10, {products[0]}: ")), float(input(f"Enter sales for month 10, {products[1]}: ")), float(input(f"Enter sales for month 10, {products[2]}: ")), float(input(f"Enter sales for month 10, {products[3]}: ")), float(input(f"Enter sales for month 10, {products[4]}: "))],
                  [float(input(f"Enter sales for month 11, {products[0]}: ")), float(input(f"Enter sales for month 11, {products[1]}: ")), float(input(f"Enter sales for month 11, {products[2]}: ")), float(input(f"Enter sales for month 11, {products[3]}: ")), float(input(f"Enter sales for month 11, {products[4]}: "))],
                  [float(input(f"Enter sales for month 12, {products[0]}: ")), float(input(f"Enter sales for month 12, {products[1]}: ")), float(input(f"Enter sales for month 12, {products[2]}: ")), float(input(f"Enter sales for month 12, {products[3]}: ")), float(input(f"Enter sales for month 12, {products[4]}: "))]])
    print(f"Sales data shape: {sales.shape}")
    print(f"Sales data type: {sales.dtype}")
    print("=" *50)
    print("Sales Data Analysis".center(50))
    print("=" *50)
    print(f"Sales of {month[0]}: {sales[0]}")
    print("Yearly Sales of each product: ")
    for i, product in enumerate(products):
        yearly_sales = np.sum(sales[:, i])
        print(f"{product}: {yearly_sales}")
    save_sales_data(products, sales)
    return products, sales
def report_sales(products, sales):
    if sales is None or products is None:
        print("Sales data is not available. Please get sales data first.")
        return
    print("=" *50)
    print("Sales Report: ".center(50))
    print("=" *50)
    average_sales_per_product = np.mean(sales, axis=0)
    yearly_sales_per_product = np.sum(sales, axis=0)
    Highest_sales = np.max(sales)
    print(f"Product with highest sales: {Highest_sales}")
    Lowest_sales = np.min(sales)
    print(f"Product with lowest sales: {Lowest_sales}")
    print("Average sales per product: ")
    for i, product in enumerate(products):
        print(f"{product}: {average_sales_per_product[i]}")
    while True:
        print("1.View Product\n2.View Month\n3.View Best Product/ Worst Product\n4.View Best Month/ Worst Month\n5.Exit")
        user_input = input("What would you like to do? ").strip().lower()
        if user_input == "1":
            product_index = int(input("Enter product index (0-4): "))
            if 0 <= product_index < len(products):
                print("-" *50)
                print(f"Product: {products[product_index]}")
                print("-" *50)
                print(f"Sales for {products[product_index]}: {sales[:, product_index]}")
                print(f"Average sales for {products[product_index]}: {average_sales_per_product[product_index]}")
                print(f"Highest sales: {np.max(sales[:, product_index])}")
                print(f"Lowest sales: {np.min(sales[:, product_index])}")
            else:
                print("Invalid product index.")
        elif user_input == "2":
            month_index = int(input("Enter month index (0-11): "))
            if 0 <= month_index < len(month):
                print(f"Sales for {month[month_index]}: {sales[month_index, :]}")
            else:
                print("Invalid month index.")
        elif user_input == "3":
            best_product = np.argmax(yearly_sales_per_product)
            worst_product = np.argmin(yearly_sales_per_product)
            print(f"Best Product: {products[best_product]} with sales of {yearly_sales_per_product[best_product]}")
            print(f"Worst Product: {products[worst_product]} with sales of {yearly_sales_per_product[worst_product]}")
        elif user_input == "4":
            best_month = np.argmax(np.sum(sales, axis=1))
            worst_month = np.argmin(np.sum(sales, axis=1))
            print(f"Best Month: {month[best_month]} with sales of {np.sum(sales[best_month, :])}")
            print(f"Worst Month: {month[worst_month]} with sales of {np.sum(sales[worst_month, :])}")
        elif user_input == "5":
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
    sales_performance = np.where(sales > average_sales_per_product, 'sales increased', 'sales decreased')
    print("Sales Performance per Product per Month: ")
    for i, product in enumerate(products):
        print(f"{product}: {sales_performance[:, i]}")
    bonus = np.array([50, 100, 150, 200, 250])
    print("Bonus for each product: ")
    sales = sales + bonus
    print(sales)
    sales= sales + 100
    print(sales)
def monthly_sales_analysis(products, sales):
    if sales is None or products is None:
        print("Sales data is not available. Please get sales data first.")
        return
    print("=" *50)
    print("Monthly Sales Analysis: ".center(50))
    print("=" *50)
    yearly_sales_per_product = np.sum(sales, axis=0)
    for i, product in enumerate(products):
        print(f"Monthly sales for {product}: {sales[:, i]}")
    best_sales_month = np.argmax(yearly_sales_per_product)
    worst_sales_month = np.argmin(yearly_sales_per_product)
    print(f"Best Sales Month: Month {month[best_sales_month]} with sales of {yearly_sales_per_product[best_sales_month]}")
    print(f"Worst Sales Month: Month {month[worst_sales_month]} with sales of {yearly_sales_per_product[worst_sales_month]}")
def profit_analysis(products, sales):
    if sales is None or products is None:
        print("Sales data is not available. Please get sales data first.")
        return
    profit_per_unit = np.array([10000, 15000, 20000, 25000, 30000])
    monthly_profit = sales * profit_per_unit
    total_profit = np.sum(monthly_profit, axis=0)
    most_profitable_product_index = np.argmax(total_profit)
    least_profitable_product_index = np.argmin(total_profit)
    print("=" *50)
    print("Profit Analysis: ".center(50))
    print("=" *50)
    total_profit_per_product = np.sum(monthly_profit, axis=0)
    for i, product in enumerate(products):
        print(f"Total profit for {product}: {total_profit_per_product[i]}")
    print(f"Most Profitable Product: {products[most_profitable_product_index]} with profit of {total_profit[most_profitable_product_index]}")
    print(f"Least Profitable Product: {products[least_profitable_product_index]} with profit of {total_profit[least_profitable_product_index]}")
def growth_analysis(products, sales):
    if sales is None or products is None:
        print("Sales data is not available. Please get sales data first.")
        return
    growth_rate = np.zeros_like(sales, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        growth_rate[1:] = np.divide(
            sales[1:] - sales[:-1],
            sales[:-1],
            out=np.zeros_like(sales[1:], dtype=float),
            where=sales[:-1] != 0,
        ) * 100
    print("=" *50)
    print("Growth Analysis: ".center(50))
    print("=" *50)
    for i, product in enumerate(products):
        print(f"Growth rates for {product}: {growth_rate[:, i].round(2)}%")
    product_growth = np.mean(growth_rate[1:], axis=0)
    highest_growth_product_index = np.argmax(product_growth)
    lowest_growth_product_index = np.argmin(product_growth)
    print(
        f"Highest Growth Product: {products[highest_growth_product_index]} "
        f"with growth rate of {product_growth[highest_growth_product_index]:.2f}%"
    )
    print(
        f"Lowest Growth Product: {products[lowest_growth_product_index]} "
        f"with growth rate of {product_growth[lowest_growth_product_index]:.2f}%"
    )
def sales_normalization(sales):
    if sales is None:
        print("Sales data is not available. Please get sales data first.")
        return
    normalized_sales = ((sales - np.min(sales, axis=0)) / (np.max(sales, axis=0) - np.min(sales, axis=0))).round(2)
    print("=" *50)
    print("Sales Normalization: ".center(50))
    print("=" *50)
    print(normalized_sales)
def main():
    while True:
        print("=" *50)
        print("Sales Data Analytics".center(50))
        print("1.Get Sales Data\n2.Load Sales Data\n3Report Sales\n4.Profit Analysis\n5.Growth Analysis\n6.Monthly Sales Analysis\n7.Sales Normalization\n8.Exit")
        user_input = input("What do you want to do? ").strip()
        if user_input.lower() == '1':
            products, sales = get_sales_data(month)
        elif user_input.lower() == '2':
            products, sales = load_sales_data()
        elif user_input.lower() == '3':
            report_sales(products, sales)
        elif user_input.lower() == '4':
            profit_analysis(products, sales)
        elif user_input.lower() == '5':
            growth_analysis(products, sales)
        elif user_input.lower() == '6':
            monthly_sales_analysis(products, sales)
        elif user_input.lower() == '7':
            sales_normalization(sales)
        elif user_input.lower() == '8':
            print("Exiting the program.")
            return
        else:
            print("Invalid input. Please enter a number between 1 and 7.")
if __name__ == "__main__":
    main()