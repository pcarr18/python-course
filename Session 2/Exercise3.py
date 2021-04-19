spent_on_goods = 300
spent_on_store_rent = 250
spent_on_wages = 500
made_on_sales = 1300
made_on_advertising = 200
total_spend = spent_on_goods+spent_on_store_rent+spent_on_wages
print(total_spend)
total_income = made_on_sales+made_on_advertising
print(f'The grocery shop made £{total_income-total_spend} in June')