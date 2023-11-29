from Q_details import *
school = 0
gen = 0

for i in range(1, 211):
    with open( f'../responses/response{i}.txt', 'w') as file:
        # Write school and gender to file
        file.write(f"{name_of_schools[school]}\n")
        file.write(f"{gender[gen]}\n")
        # On the 21st run, change gender for the next run, select teacher occupation and teacher age
        if i % 21 == 0:
            gen += 1
            file.write(f"{age_ranges[select_number(2)]}\n")
            file.write(f"{occupation[1]}\n")
        else:
            # select student occupation and student age
            file.write(f"{age_ranges[select_number()]}\n")
            file.write(f"{occupation[0]}\n")

        # Change school after 42 runs and change the gender back
        if i % 42 == 0 and i != 210:
            gen -= 2
            school += 1
        # Randomly fill the rest
        for _ in range(len(The_extent_of_Pidgin_English_usage_in_Junior_Secondary_Schools)):
            file.write(f"{The_extent_of_Pidgin_English_usage_in_Junior_Secondary_Schools[_]} : {resp[select_number(3)]}\n")

        for _ in range(len(Attitudes_and_Perceptions)):
            file.write(f"{Attitudes_and_Perceptions[_]} : {resp_op[select_number(3)]}\n")  
        
        for _ in range(len(Positive_Effects_of_Pidgin_English_Language_usage_in_Junior_Secondary_Schools)):
            file.write(f"{Positive_Effects_of_Pidgin_English_Language_usage_in_Junior_Secondary_Schools[_]} : {resp_op[select_number(3)]}\n")
        
        for _ in range(len(Negative_Effects_of_Pidgin_English_Language_usage_in_Junior_Secondary_Schools)):
            file.write(f"{Negative_Effects_of_Pidgin_English_Language_usage_in_Junior_Secondary_Schools[_]} : {resp_op[select_number(3)]}\n")