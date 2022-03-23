def find_underpaid_customers(text_file):
    melon_cost = 1.00
    #variable for set melon cost
    customer_orders = open(text_file)

    for line in customer_orders:
        line = line.rstrip()
        words = line.split('|')

        customer_num = words[0]
        customer_name = words[1]
        customer_order = float(words[2])
        customer_paid = float(words[3])

        customer_expected = customer_order * melon_cost
        #if customer1expected is not what customer paid print statement
        if customer_expected != customer_paid:
            print(f"Customer: {customer_num} {customer_name} paid ${customer_paid:.2f},",
                f"expected ${customer_expected:.2f}"



    #customer1_expected is customer melons times cost
   
            )

find_underpaid_customers("customer-orders.txt")

    # customer2_expected = customer2_melons * melon_cost
    # if customer2_expected != customer2_paid:
    #     print(f"{customer2_name} paid ${customer2_paid:.2f},",
    #         f"expected ${customer2_expected:.2f}"
    #         )

    # customer3_expected = customer3_melons * melon_cost
    # if customer3_expected != customer3_paid:
    #     print(f"{customer3_name} paid ${customer3_paid:.2f},",
    #         f"expected ${customer3_expected:.2f}"
    #         )

    # customer4_expected = customer4_melons * melon_cost
    # if customer4_expected != customer4_paid:
    #     print(f"{customer4_name} paid ${customer4_paid:.2f},",
    #         f"expected ${customer4_expected:.2f}"
    #         )

    # customer5_expected = customer5_melons * melon_cost
    # if customer5_expected != customer5_paid:
    #     print(f"{customer5_name} paid ${customer5_paid:.2f},",
    #         f"expected ${customer5_expected:.2f}"
    #         )

    # customer6_expected = customer6_melons * melon_cost
    # if customer6_expected != customer6_paid:
    #     print(f"{customer6_name} paid ${customer6_paid:.2f},",
    #         f"expected ${customer6_expected:.2f}"
    #         )
#variables for customer name, ammount of melons and what paid
    # customer1_name = "Joe"
    # customer1_melons = 5
    # customer1_paid = 5.00

    # customer2_name = "Frank"
    # customer2_melons = 6
    # customer2_paid = 6.00

    # customer3_name = "Sally"
    # customer3_melons = 3
    # customer3_paid = 3.00

    # customer4_name = "Sean"
    # customer4_melons = 9
    # customer4_paid = 9.50

    # customer5_name = "David"
    # customer5_melons = 4
    # customer5_paid = 4.00

    # customer6_name = "Ashley"
    # customer6_melons = 3
    # customer6_paid = 2.00