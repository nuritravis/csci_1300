input_str = input("What is your name? ")
split_str = input_str.split()
split_str[1] = split_str[1][0]
print(f"{split_str[0]} {split_str[1]}. {split_str[2]}")