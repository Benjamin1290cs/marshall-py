# Lesson 5
start_money = float(input('Enter initial ammount: ')) 
cookies_sold = input("Enter combination of cookies: ")

# processing

big_cookies = cookies_sold.count("b")
cookies = cookies_sold.count("c")

total_cookies = big_cookies + cookies
profit = ((big_cookies * 2) + (cookies * 1.25)) - ((big_cookies * 0.75) + (cookies * 0.5))
end_day = start_money + profit

# output

print(f'We sold {total_cookies} cookies. We made ${profit}. We now have ${end_day}.')