def print_list_items(lst):
    for i in range (len(lst)):
        print(f"item{i+1}:{lst[i]}")
        my_list = ['apple','banana','orange']
        print_list_items(my_list)