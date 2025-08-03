def number_diamond_triangle():
    n = int(input("Enter the number of lines for the top half of the diamond: "))

    # Top half
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        inc_numbers = ''.join(str(j) for j in range(1, i + 1))
        dec_numbers = ''.join(str(j) for j in range(i - 1, 0, -1))
        print(spaces + inc_numbers + dec_numbers)

    # Bottom half
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        inc_numbers = ''.join(str(j) for j in range(1, i + 1))
        dec_numbers = ''.join(str(j) for j in range(i - 1, 0, -1))
        print(spaces + inc_numbers + dec_numbers)

# Run the function
number_diamond_triangle()

