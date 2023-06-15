def sum_of_first_elements_of_tuples_with_even_no_as_second_element(tuples_list):
    total = 0
    for tuple in tuples_list:
        if tuple[1] % 2 == 0:
            total += tuple[0]
    return total
tuples = [(4, 7), (6, 8), (9, 10), (12, 9), (14, 18)]
total = sum_of_first_elements_of_tuples_with_even_second_element(tuples)
print(total) 
