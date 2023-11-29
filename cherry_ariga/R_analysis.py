from table_m import *
from cronbach import array, framer

EU_dFrame = []
AP_dFrame = []
PE_dFrame = []
NE_dFrame = []

EU_cae = []
AP_cae = []
PE_cae = []
NE_cae = []

students = {
    "gender": [],
    "age_range": [],
    "occupation": []
}
teachers = {
    "gender": [],
    "age_range": [],
    "occupation": []
}
result = {}
var = ["students", "teachers", "result"]

for i in range(1, 211):
    with open( f'responses/response{i}.txt', 'r') as file:
        if i % 21 == 0:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if line_number == 2:
                    teachers["gender"].append(line)
                if line_number == 3:
                    teachers["age_range"].append(line)
                if line_number == 4:
                    teachers["occupation"].append(line)
                if line_number >= 5:
                    key, value = line.split(":")
                    if key not in teachers:
                        teachers[key] = []
                    teachers[key].append(value)
                    result[key].append(value)
                    ###############
                    if key.strip() in eu:
                        EU_cae.append(value.strip())
                    elif key.strip() in ap:
                        AP_cae.append(value.strip())
                    elif key.strip() in pe:
                        PE_cae.append(value.strip())
                    elif key.strip() in ne:
                        NE_cae.append(value.strip())
                    ################
        else:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if line_number == 2:
                    students["gender"].append(line)
                if line_number == 3:
                    students["age_range"].append(line)
                if line_number == 4:
                    students["occupation"].append(line)
                if line_number >= 5:
                    key, value = line.split(":")
                    if key not in students:
                        students[key] = []
                        result[key] = []
                    students[key].append(value)
                    result[key].append(value)
                    ###############
                    if key.strip() in eu:
                        EU_cae.append(value.strip())
                    elif key.strip() in ap:
                        AP_cae.append(value.strip())
                    elif key.strip() in pe:
                        PE_cae.append(value.strip())
                    elif key.strip() in ne:
                        NE_cae.append(value.strip())
        #############
        EU_dFrame.append(list(array(EU_cae)))
        AP_dFrame.append(list(array(AP_cae)))
        PE_dFrame.append(list(array(PE_cae)))
        NE_dFrame.append(list(array(NE_cae)))
        #########
        EU_cae.clear()
        AP_cae.clear()
        PE_cae.clear()
        NE_cae.clear()
################
framer(EU_dFrame, 0, eu)
framer(AP_dFrame, 1, ap)
framer(PE_dFrame, 2, pe)
framer(NE_dFrame, 3, ne)
#####################

with open("teachers.txt", "w") as file:
    for key, value in teachers.items():
        file.write(f"{key}:{value}\n")

with open("students.txt", "w") as file:
    for key, value in students.items():
        file.write(f"{key}:{value}\n")

with open("result.txt", "w") as file:
    for key, value in result.items():
        file.write(f"{key}:{value}\n")

for i in range(3):
    with open(f"{var[i]}.txt", "r") as Ifile, open(f"C_{var[i]}.txt", "w") as Ofile:
        data = Ifile.read()
        data_list = data.split("\n")
        for row in data_list:
            if ":" not in row:
                continue
            key, value = row.split(":")
            value = value[1:-1]
            options = value.split(", ")
            counts = {}
            for option in options:
                if option in counts:
                    counts[option] += 1
                else:
                    counts[option] = 1
            total_responses = len(options)  # Total number of responses for this key
            # Calculate and write counts and percentages
            Ofile.write(f"{key} \n")
            for option, count in counts.items():
                percentage = (count / total_responses) * 100
                Ofile.write(f"{option} - Count: {count}, Percentage: {percentage:.2f}%\n")

    if os.path.exists(f"{var[i]}.txt"):
        os.remove(f"{var[i]}.txt")
