# Find the total costs and total customers acquired in each year
# Easy
# ID 10009

# Find the total costs and total customers acquired in each year.
# Output the year along with corresponding total money spent and total acquired customers.

# uber_advertising
# year: int64
# advertising_channel:object
# money_spent:int64
# customers_acquired:int64

import pandas as pd 
uber_advertising = pd.read_csv("uber_advertising.csv")

uber_advertising.head()

df = uber_advertising.groupby('year')[['money_spent','customers_acquired']].sum().reset_index()

print(df)

# Average Cost Of Each Request

# Easy
# ID 10007


# Find the average cost of each request status.
# Request status can be either 'success' or 'fail'.
# Output the request status along with the average cost.

# uber_ride_requests
# request_id:int64
# request_status:object
# distance_to_travel:float64
# monetary_cost:float64
# driver_to_client_distance:float64

result = df.groupby('request_status')['monetary_cost'].mean().reset_index()


# Find the advertising channel where Uber spent more than 100k USD in 2019


# Easy
# ID 10002

# Find the advertising channel(s) where Uber spent more than 100k USD in 2019.


# uber_advertising

result= uber_advertising[(uber_advertising['money_spent']>100000) & (uber_advertising['year']==2019)]['advertising_channel']

# Find the cost per customer for advertising via public transport

# Easy
# ID 10001


# Find the cost per customer for each advertising channel and year combination . Include only channels that are advertised via public transport (advertising channel includes "bus" substring).
# The cost per customer is equal to the total spent money divided by the total number of acquired customers through that advertising channel. Output advertising channel, year and its cost per customer.


# uber_advertising

result = uber_advertising[uber_advertising['advertising_channel'].str.contains('bus')]

result['cost_per_customer'] = result['money_spent']/result['customers_acquired']

a = result.groupby(['advertising_channel','year']).apply(
    lambda x:x['money_spent'].sum()/x['customers_acquired'].sum()
    ).reset_index()

# Find the year that Uber acquired more than 2000 customers through celebrities

# Easy
# ID 10000

# Find the year that Uber acquired more than 2000 customers through advertising using celebrities.

# uber_advertising

df=uber_advertising[
    
    uber_advertising['advertising_channel'] == 'celebrities'
    
    ]

result= df[
    
    df['customers_acquired'] == df['customers_acquired'].max()
    
    ]['year']



# Total Order Per Status Per Service

# Easy
# ID 2049

# Uber is interested in identifying gaps in their business. Calculate the count of orders for each status of each service. Your output should include the service name, status of the order, and the number of orders.

# DataFrame
# uber_orders
# order_date:datetime64[ns]
# number_of_orders:int64
# status_of_order:object
# monetary_value:float64
# service_name:object

result = uber_orders.groupby(
    ['service_name','status_of_order']
    )['number_of_orders'].sum().reset_index(name='orders_sum')



# Employees' Without Annual Review

# Easy
# ID 2043

# Return all employees who have never had an annual review. Your output should include the employee's first name, last name, hiring date, and termination date. List the most recently hired employees first.

# DataFrames
# uber_employees
# first_name:object
# last_name:object
# id:int64
# hire_date:datetime64[ns]
# termination_date:datetime64[ns]
# salary:int64

# uber_annual_review

# id:int64
# emp_id:int64
# review_date:datetime64[ns]

review_ids = uber_annual_review['emp_id'].unique()
df = uber_employees[~uber_employees['id'].isin(review_ids)][['first_name','last_name','hire_date','termination_date']].sort_values('hire_date',ascending = False)
