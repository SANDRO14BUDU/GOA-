# საკლასო დავალება: შექმენით ფუნქცია სახელად manual_index, რომელსაც ექნება 2 პარამეტრი - მთავარი სთრინგი და საძიებელი სთრინგი.
# თქვენი დავალებაა რომ დააბრუნოთ მთავარ სთრინგში საძიებელი სთრინგი მერამდენე ინდექსზეა



def manual_index(main_string, search_string):
    i = 0
    while i < (main_string + '\0').index('\0'):
        j = 0
        while j < (search_string + '\0').index('\0') and main_string[i + j] == search_string[j]:
            j += 1
        if (search_string + '\0').index('\0') == j:
            print(i)
            break
        i += 1
    else:
        print(-1)

main_string = "მაგარია?"
search_string = "რია"
manual_index(main_string, search_string)  

main_string = "იმენა ლოლ"
search_string = "პითონი"
manual_index(main_string, search_string)  
