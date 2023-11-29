import random
import numpy as np
import pingouin as pg
import pandas as pd

def select_number(val=1):
    if val == 1:
        return 1 if random.randint(0, 99) == 0 else 0
    elif val == 2:
        return random.randint(2, 4)
    else:
        return random.randint(0, 3)
    
def answers():
    # Set the number of respondents and items
    num_respondents = 211
    num_items = 38
    # Generate a covariance matrix with the appropriate shape
    correlation_matrix = np.eye(num_items)
    # Increase correlations between items
    for i in range(num_items):
        for j in range(i + 1, num_items):
            correlation_matrix[i, j] = 0.15  # Adjust the correlation coefficient as needed
            correlation_matrix[j, i] = 0.85
    # Generate random data
    data = np.random.multivariate_normal(
        # Generate a list of 38 random mean values within the specified range
        mean = np.linspace(1.63, 3.45, num_items),
        cov=correlation_matrix,  # Use the 38x38 covariance matrix
        size=num_respondents
    )
    # Loop through the data and adjust values
    for i in range(num_respondents):
        for j in range(num_items):
            data[i][j] = adjust_value(data[i][j])

    transposed_data = pd.DataFrame(data, columns=Questions)
    transposed_data.to_csv("Q_data.csv", index=False)
    transposed_data.to_excel("Q_data.xlsx", index=False)
    with open("Q_data.txt", "w") as file:
        file.write(f"{pg.cronbach_alpha(transposed_data)}\n")
    return transposed_data
# Define a function to check and adjust values
def adjust_value(value):
    if value < 1:
        return 3
    elif value > 4:
        return 4
    else:
        return int(value)
# Define lists to be used in the code
name_of_schools = [
    "Community Junior Secondary School , Choba, Uniport road",
    "Community Secondary School , Rukpokwu",
    "Community Secondary School , Rumuaghaolu",
    "Community Comprehensive Secondary School ,Rumuokwurushi",
    "Community Secondary School , Rumuekini"
    ]

age_ranges = [
    "12-18",
    "18-24",
    "25-34",
    "35-44",
    "45 & above"
    ]

gender = ["Male", "Female"]

occupation = ["Student", "Teacher"]

resp_op = ["SD", "D", "A", "SA"]

resp = ["VLE", "LE", "HE", "VHE"]

The_extent_of_Pidgin_English_usage_in_Junior_Secondary_Schools = [
    "Pidgin English Language is commonly spoken in Junior Secondary Schools in Obio/Akpor Local Government Area.",
    "Pidgin English Language is being used in educational settings by students and teachers in Junior Secondary Schools.",
    "The primary reason for using Pidgin English Language in teaching and learning in Junior Secondary Schools by students and teachers is for facilitating faster and easier communication.",
    "Pidgin English Language is currently being used in the classroom to what extent?",
    "There are challenges or drawbacks associated with using Pidgin English Language in educational settings.",
    "There are specific subjects or areas where Pidgin English Language could be more effectively used in teaching and learning.",
    "There are some cultural considerations that should be taken into account when using Pidgin English Language in educational settings.",
    "Some steps should be taken to further include Pidgin English Language usage into teaching and learning practices.",
    ]

Attitudes_and_Perceptions = [
    "Students and teachers are familiar with the concept of Pidgin English Language.",
    "There are potential benefits of including Pidgin English Language in the classroom.",
    "The use of Pidgin English Language can compromise students' performance in formal English.",
    "It is preferable to use Pidgin English Language for better communication in educational settings.",
    "There is an improvement in students' learning outcomes when Pidgin English Language is utilized.",
    "With appropriate effort, Pidgin English Language can be effectively integrated into the curriculum.",
    "Teachers should receive training on how to effectively use Pidgin English Language in teaching.",
    "There's positive impact of Pidgin English Language on teaching and learning.",
    "There is serious negative impact of Pidgin English Language on teaching and learning.",
    "Junior Secondary School education can progress successfully without the use of Pidgin English Language during teaching and learning."
    ]

Positive_Effects_of_Pidgin_English_Language_usage_in_Junior_Secondary_Schools  = [
    "The use of Pidgin English Language facilitates teaching and learning.",
    "You have personally experienced some positive effects of using Pidgin English Language in your education or teaching practices.",
    "Pidgin English Language should be included as a legitimate language of instruction.",
    "The use of Pidgin English Language affects students' motivation to learn positively.",
    "Some strategies can be carried out by educators to effectively include Pidgin English Language without compromising standard language proficiency.",
    "The use of Pidgin English Language during instruction fosters successful communication.",
    "Utilization of Pidgin English Language by the teachers and students helps to form a bond and establish closeness between them.",
    "Pidgin English Language is mostly used for instruction because it helps for clarification of difficult concepts.",
    "The teachers and students engage in more friendly conversations when using the Pidgin English Language during instruction.",
    "You have personally benefitted from the use of Pidgin English Language during instruction."
    ]

Negative_Effects_of_Pidgin_English_Language_usage_in_Junior_Secondary_Schools = [ 
    "Pidgin English Language hinders students' proficiency in standard English.",
    "Pidgin English Language leads to poor communication skills among students.",
    "The use of Pidgin English Language negatively impacts students' ability to perform effectively in other subjects.",
    "Teachers find it challenging to change from Pidgin English Language to standard English during instruction.",
    "Pidgin English Language affects students' overall performance, especially in English language exams or assessments.",
    "Pidgin English Language creates a barrier to understanding and comprehending complex academic concepts.",
    "Pidgin English Language creates language inequalities and thereby, causes social divisions in education.",
    "Teachers face challenges when students use Pidgin English Language in the classroom.",
    "You have experienced a situation where Pidgin English Language negatively impacted teaching or learning outcomes.",
    "Attempts have been made to address the negative effects of Pidgin English Language on teaching and learning in your educational context."
    ]

Questions = [
    "Pidgin English Language is commonly spoken in Junior Secondary Schools in Obio/Akpor Local Government Area.",
    "Pidgin English Language is being used in educational settings by students and teachers in Junior Secondary Schools.",
    "The primary reason for using Pidgin English Language in teaching and learning in Junior Secondary Schools by students and teachers is for facilitating faster and easier communication.",
    "Pidgin English Language is currently being used in the classroom to what extent?",
    "There are challenges or drawbacks associated with using Pidgin English Language in educational settings.",
    "There are specific subjects or areas where Pidgin English Language could be more effectively used in teaching and learning.",
    "There are some cultural considerations that should be taken into account when using Pidgin English Language in educational settings.",
    "Some steps should be taken to further include Pidgin English Language usage into teaching and learning practices.",
    "Students and teachers are familiar with the concept of Pidgin English Language.",
    "There are potential benefits of including Pidgin English Language in the classroom.",
    "The use of Pidgin English Language can compromise students' performance in formal English.",
    "It is preferable to use Pidgin English Language for better communication in educational settings.",
    "There is an improvement in students' learning outcomes when Pidgin English Language is utilized.",
    "With appropriate effort, Pidgin English Language can be effectively integrated into the curriculum.",
    "Teachers should receive training on how to effectively use Pidgin English Language in teaching.",
    "There's positive impact of Pidgin English Language on teaching and learning.",
    "There is serious negative impact of Pidgin English Language on teaching and learning.",
    "Junior Secondary School education can progress successfully without the use of Pidgin English Language during teaching and learning.",
    "The use of Pidgin English Language facilitates teaching and learning.",
    "You have personally experienced some positive effects of using Pidgin English Language in your education or teaching practices.",
    "Pidgin English Language should be included as a legitimate language of instruction.",
    "The use of Pidgin English Language affects students' motivation to learn positively.",
    "Some strategies can be carried out by educators to effectively include Pidgin English Language without compromising standard language proficiency.",
    "The use of Pidgin English Language during instruction fosters successful communication.",
    "Utilization of Pidgin English Language by the teachers and students helps to form a bond and establish closeness between them.",
    "Pidgin English Language is mostly used for instruction because it helps for clarification of difficult concepts.",
    "The teachers and students engage in more friendly conversations when using the Pidgin English Language during instruction.",
    "You have personally benefitted from the use of Pidgin English Language during instruction.",
    "Pidgin English Language hinders students' proficiency in standard English.",
    "Pidgin English Language leads to poor communication skills among students.",
    "The use of Pidgin English Language negatively impacts students' ability to perform effectively in other subjects.",
    "Teachers find it challenging to change from Pidgin English Language to standard English during instruction.",
    "Pidgin English Language affects students' overall performance, especially in English language exams or assessments.",
    "Pidgin English Language creates a barrier to understanding and comprehending complex academic concepts.",
    "Pidgin English Language creates language inequalities and thereby, causes social divisions in education.",
    "Teachers face challenges when students use Pidgin English Language in the classroom.",
    "You have experienced a situation where Pidgin English Language negatively impacted teaching or learning outcomes.",
    "Attempts have been made to address the negative effects of Pidgin English Language on teaching and learning in your educational context."
]

eper = [
    "Students and teachers are familiar with the concept of Pidgin English Language.",
    "There are potential benefits of including Pidgin English Language in the classroom.",
    "The use of Pidgin English Language can compromise students' performance in formal English.",
    "It is preferable to use Pidgin English Language for better communication in educational settings.",
    "There is an improvement in students' learning outcomes when Pidgin English Language is utilized.",
    "With appropriate effort, Pidgin English Language can be effectively integrated into the curriculum.",
    "Teachers should receive training on how to effectively use Pidgin English Language in teaching.",
    "There's positive impact of Pidgin English Language on teaching and learning.",
    "There is serious negative impact of Pidgin English Language on teaching and learning.",
    "Junior Secondary School education can progress successfully without the use of Pidgin English Language during teaching and learning.",
    "The use of Pidgin English Language facilitates teaching and learning.",
    "You have personally experienced some positive effects of using Pidgin English Language in your education or teaching practices.",
    "Pidgin English Language should be included as a legitimate language of instruction.",
    "The use of Pidgin English Language affects students' motivation to learn positively.",
    "Some strategies can be carried out by educators to effectively include Pidgin English Language without compromising standard language proficiency.",
    "The use of Pidgin English Language during instruction fosters successful communication.",
    "Utilization of Pidgin English Language by the teachers and students helps to form a bond and establish closeness between them.",
    "Pidgin English Language is mostly used for instruction because it helps for clarification of difficult concepts.",
    "The teachers and students engage in more friendly conversations when using the Pidgin English Language during instruction.",
    "You have personally benefitted from the use of Pidgin English Language during instruction.",
    "Pidgin English Language hinders students' proficiency in standard English.",
    "Pidgin English Language leads to poor communication skills among students.",
    "The use of Pidgin English Language negatively impacts students' ability to perform effectively in other subjects.",
    "Teachers find it challenging to change from Pidgin English Language to standard English during instruction.",
    "Pidgin English Language affects students' overall performance, especially in English language exams or assessments.",
    "Pidgin English Language creates a barrier to understanding and comprehending complex academic concepts.",
    "Pidgin English Language creates language inequalities and thereby, causes social divisions in education.",
    "Teachers face challenges when students use Pidgin English Language in the classroom.",
    "You have experienced a situation where Pidgin English Language negatively impacted teaching or learning outcomes.",
    "Attempts have been made to address the negative effects of Pidgin English Language on teaching and learning in your educational context."
]