total_tickets = 0
total_price = 0
total_a = 0
total_s = 0
total_c = 0
total_g = 0
how_many_times = 0
while True:
    if how_many_times == 0:
        buy_or_not = input("Do you want to sell a ticket? (Y/N):")
    else:
        buy_or_not = input("Do you want to sell another ticket? (Y/N):")
    if buy_or_not == "n":
        break
    if buy_or_not == "y":
        what_kind_tickets = input(f"What kind of ticket do you want:\nA for Adult, or\nS for student, or\nC for Child, or\nG for Gift voucher\n")
        how_many_tickets = int(input("How many of these tickets do you want:"))
        confirm = input(f"Confirm purchase of {how_many_tickets} type {what_kind_tickets} ticket(s)? (Y/N):")
        if confirm == "y":
            if what_kind_tickets == "a":
                total_price += 12.5*how_many_tickets
                total_a += how_many_tickets
            elif what_kind_tickets == "s":
                total_price += 9*how_many_tickets
                total_s += how_many_tickets
            elif what_kind_tickets == "c":
                total_price += 7*how_many_tickets
                total_c += how_many_tickets
            elif what_kind_tickets == "g":
                total_price += 0
                total_g += how_many_tickets
    how_many_times += 1
print(f"==================================================\nThe total tickets sold today was {total_tickets}\nThis was made up of:\n{total_a} for adults; and\n{total_s} for students; and\n{total_c} for children; and\n{total_g} gift vouchers\n\nSales for the day came to ${total_price:.2f}\n==================================================")
