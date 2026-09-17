# Create a Flask API that reads sales_data.csv file and returns total revenue
# the API should have an endpoint /total_revenue that returns the total revenue as a JSON response
# the structure of the sales_data.csv file is as follows:
# order_id,product,region,sales,order_date
# 1001,Monitor,South,1306,2024-12-26
# the total revenue can be calculated by summing up the sales column
# convert the total revenue to an integer and return it as a JSON response.
# Additionally, create another endpoint /highest_region that returns the region 
# with the highest sales along with the total sales for that region as a JSON response.

from flask import Flask, jsonify
import csv

app = Flask(__name__)

def read_sales_data():
    with open("sales_data.csv", newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)

@app.route("/total_revenue")
def total_revenue():
    sales_data = read_sales_data()
    total = sum(int(row["sales"]) for row in sales_data)
    return jsonify({
        "message": f"The total revenue for all regions is {total}",
        "total_revenue": total,
    })

@app.route("/highest_region")
def highest_region():
    sales_data = read_sales_data()
    region_totals = {}
    for row in sales_data:
        region = row["region"]
        sales = int(row["sales"])
        region_totals[region] = region_totals.get(region, 0) + sales
    if not region_totals:
        return jsonify({"region": None, "total_sales": 0})
    highest_region = max(region_totals, key=region_totals.get)
    return jsonify({"region": highest_region, "total_sales": region_totals[highest_region]})

if __name__ == "__main__":
    app.run(debug=True)