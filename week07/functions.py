# Self-Assessment Responses

#1.) The fist bug I spotted was the missing colon. I found it because 
# my Visual Studio Code highlighted the line in red. This shows that
#  I need a bunch of help from my AI tools and that I need to work on
#  finding and debugging codes on my own. I was able to realize the 
# total error on my own when I spoke out loud to myself.

#2.) apply_discount(price, tier) takes the price and tier of an item, 
# applies a dsicount based on it's tier and returns the new price. 
# The inputs are the original price and the item's tier is. The function
#  returns the new discounted price. Yes, a colleague could use the 
# function without reading the body as long as they knew what the price
#  and tiers were and what the return value would tell them.

#3.) AI use: aked ChatGPT to help me understand the TypeError's and
#  where to look to find the fix in exercise 5. The AI helped build 
# my understanding of what to look for when I get that type of error.
#  The error was one that dealt with a list.

# --- Exercise 1 ---

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# --- Exercise 3 ---

# Write out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")


# --- Exercise 5 ---

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # the + makes the total be cummalitive not the final total of the last sale.
print(f"Total: ${total}")

count = 0
for sale in sales: # added a : to fix the error.
     count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # deleted the equal sign to fix the error.
    print(sales[i])
    i += 1

# --- Exercise 6 ---

x = 100 # apple # global

def double_it():
    # global x # apple (same as above)
    x = 999 # another apple (not the same as apple above)
    return x * 2

print(x)
print(double_it())
print(x)

# The outcome of the machine is not 100 because the global variable 
# x is being modified inside the function double_it(). When the 
# function is called, it changes the value of x to 999, so when we
#  print x after calling the function, it outputs 999 instead of 100.
# Scope is when a variable inside a function or machine are only 
# seen there and not seen outside of it in any other code.