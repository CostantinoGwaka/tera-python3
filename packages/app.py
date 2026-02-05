# from sales import cal_tax, cal_shipping
# from sales import * -- import everything from sales


# as import sales as s
import ecommerce.shopping.sales as sales
import sys
sales.cal_shipping()
sales.cal_tax()


# print(sys.path)

# print(dir(sales))
print(sales.__name__)
print(sales.__file__)
print(sales.__package__)


# cal_shipping()
# cal_tax()
