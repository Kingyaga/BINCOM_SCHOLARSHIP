import pandas as pd
import pingouin as pg
import numpy as np

def array(caa):
    conv = {
        "SA": 4,
        "VHE": 4,
        "A": 3,
        "HE": 3,
        "D": 2,
        "VLE": 2,
        "SD": 1,
        "LE": 1
    }
    for item in caa:
        for key in conv.keys():
            if item == key:
                caa[caa.index(item)] = conv[key]
    return caa

def framer(dFrame, num, hd):
    sap=["eu", "ap", "pe", "ne"]
    data = np.array(dFrame)
    df = pd.DataFrame(data, columns=hd)
    df.to_excel(f"{sap[num].upper()}_output.xlsx", index=False)
    alpha = pg.cronbach_alpha(df)
    print(f"{sap[num]}_alpha: {alpha}")
    # Calculate the mean and standard deviation for each column
    mean_values = df.mean().round(2)
    std_values = df.std().round(2)
    # Create a new DataFrame for mean and std
    summary_df = pd.DataFrame({'Column Name': mean_values.index,'Mean': mean_values, 'Std Dev': std_values})
    # Write the combined DataFrame to a CSV file
    summary_df.to_csv(f"{sap[num]}_data.csv", index=False)
