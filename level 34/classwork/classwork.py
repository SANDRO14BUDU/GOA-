# def remove_elements(main_list, indexes_list):
#     for index in sorted(indexes_list, reverse=True):
#         if 0 <= index < len(main_list):
#             main_list.pop(index)
#     return main_list

# main_list = [1, 2, 3, 4, 5]
# indexes_list = [1, 3]
# result = remove_elements(main_list, indexes_list)
# print(result)


def remove_one_element(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    print(lst)
    
my_list = [10, 20, 30, 40, 50]
remove_one_element(my_list, 2)
