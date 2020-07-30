"""code for embedded activity in Min and Max built-in functions part II"""
# Mailing list sign-ups per month over 12 months.
# new_monthly_signups[0] = "January", new_monthly_signups[1] = "February"

new_monthly_signups = [225, 100, 125, 427, 568, 679, 800, 523, 354, 300, 219, 196]
max_signups = max(new_monthly_signups)
min_signups = min(new_monthly_signups)
print(list(range(min_signups, max_signups, 100)))
def signup_stats(signups):
    max_signups = max(signups)
    min_signups = min(signups)
    return max_signups, min_signups, range(max_signups, min_signups)
print(signup_stats(new_monthly_signups))

"""code for embedded activity in Sort an Iterable in Part II"""
# Mailing list sign-ups per month over 12 months.
# new_monthly_signups[0] = "January", new_monthly_signups[1] = "February"

new_monthly_signups = [225, 100, 125, 427, 568, 679, 800, 523, 354, 300, 219, 196]
sorted_signups = sorted(new_monthly_signups)
list_length = len(sorted_signups)
median_one = sorted_signups[list_length//2]
median_two = sorted_signups[(list_length//2)-1]
avg_median = (median_two + median_one)/2


def sort_signups(signups):
    sorted_signups = sorted(signups)
    list_length = len(sorted_signups)
    median_one = sorted_signups[list_length//2]
    median_two = sorted_signups[(list_length//2)-1]
    avg_median = (median_two + median_one)/2
    return avg_median
print(sort_signups(new_monthly_signups))

"""code for embedded activity on sum() and round()"""
# Mailing list sign-ups per month over 12 months.
# new_monthly_signups[0] = "January", new_monthly_signups[1] = "February"

new_monthly_signups = [225, 100, 125, 427, 568, 679, 800, 523, 354, 300, 219, 196]
sum_signups = sum(new_monthly_signups)
mean_signups = sum_signups/len(new_monthly_signups)
# adding round here to clean up the output
print(f"The total signups were {sum_signups} and the average signups were {round(mean_signups, 2)}")

def avg_signups(signups):
    sum_signups = sum(signups)
    return round(sum_signups/len(signups),2) # adding round here to clean up the output
print(avg_signups(new_monthly_signups))


"""code for embedded activity on zip"""

sales_east = [550, 287, 510, 891, 341, 663, 812]
sales_west = [651, 254, 901, 796, 205, 522, 966]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for western_sales, eastern_sales in zip(sales_west, sales_east):
    print(eastern_sales - western_sales)

print(dict(zip(weekdays, sales_east)))


"""Code for embedded activity on filtering data"""
sales_east = [550, 287, 510, 891, 341, 663, 812]
sales_west = [651, 254, 901, 796, 205, 522, 966]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def is_below_avg(item):
    return item < 596
low_sales_east = list(filter(is_below_avg, sales_east))
# low_sales_east = list(filter(lambda sales: sales < 596, sales_east))
print(low_sales_east)
low_sales_west = list(filter(is_below_avg, sales_west))
# low_sales_west = list(filter(lambda sales: sales < 596, sales_west))
print(low_sales_west)


"""Code for embedded activity on map()"""
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sales_east = [550, 287, 510, 891, 341, 663, 812]
sales_west = [651, 254, 901, 796, 205, 522, 966]
def remove_tax(num):
    return round(num / 1.10, 2)

before_tax_east = list(map(remove_tax, sales_east))
before_tax_west = list(map(remove_tax, sales_west))
print(before_tax_east)
print(before_tax_west)
