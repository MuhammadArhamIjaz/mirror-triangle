def vertical_mirror_triangle():
    n = int(input("Enter the number of lines for the triangle: "))
    
    # Top half
    for i in range(1, n + 1):
        print('*' * i)
    
    # Bottom half
    for i in range(n - 1, 0, -1):
        print('*' * i)

# Run the function
vertical_mirror_triangle()


