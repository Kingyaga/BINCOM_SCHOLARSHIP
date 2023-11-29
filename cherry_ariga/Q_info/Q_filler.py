from Q_details import *
school = 0
gen = 0

transposed_data = answers()
# Define the questions (columns) based on the column names in 'transposed_data'
questions = transposed_data.columns
# Iterate through each respondent
for i, row in transposed_data.iterrows():
    i +=1
    if i == 211:
        break
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
        # Write questions and responses for the current respondent
        for question in questions:
            response = int(row[question]) - 1
            if question in The_extent_of_Pidgin_English_usage_in_Junior_Secondary_Schools:
                file.write(f"{question} : {resp[response]}\n")
            else:
                file.write(f"{question} : {resp_op[response]}\n")