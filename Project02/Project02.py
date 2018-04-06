# To run: python Project02.py name_for_an_output_file name_for_an_image
import numpy as np
from sys import argv
import io
import re
import matplotlib.pyplot as plt


def Step1(tabline):
    if tabline[4].find("*") != -1:
        return False
    elif tabline[4].find("+") != -1:
        return False
    elif tabline[4].find("-") != -1:
        return False
    elif tabline[4].find("<") != -1:
        return False
    elif tabline[4].find(">") != -1:
        return False
    elif tabline[3] < 10:
        return False
    else:
        return True

def Step2(tabline):
    # Remove $
    rem1 = re.sub('\^[\S]','', tabline[4], re.M)
    #tabline[4] = rem1
    # Remove ^ and following characters
    rem2 = rem1.replace("$", "")
    #tabline[4] = rem2
    # Convert quality scores
    q = tabline[5].strip()
    qual = list(q)
    i = 0
    quality = []
    for i in range(0, len(qual)):
        char = qual[i]
        score = ord(char) - 33
        quality.append(score)
    tabline[5] = quality
   # Does the base count?
    t5 = tabline[5]
    # Set the variables at 0
    match = 0
    varA = 0
    varT = 0
    varG = 0
    varC = 0
    if len(rem2) != tabline[3]:
        print("Error, lengths do not match")
        print(tabline)
        print(rem2)
        quit
    t4 = list(rem2)
    #print(t4)
    for i in range(0, tabline[3]):
        if (t5[i] >= 30):
            if t4[i] == '.' or t4[i] == ',':
                match = match + 1
            if t4[i] == "A" or t4[i] == "a":
                varA = varA + 1
            if t4[i] == "T" or t4[i] == "t":
                varT = varT + 1
            if t4[i] == "G" or t4[i] == "g":
                varG = varG + 1
            if t4[i] == "C" or t4[i] == "c":
                # print("C")
                varC = varC + 1
    variant = varA + varT + varG + varC
    tabline.append(varA)
    tabline.append(varT)
    tabline.append(varG)
    tabline.append(varC)
    #print(tabline, match, variant, varA, varT, varG, varC)
    return tabline
#return as a list
def Step3(tabline):
    # Filter out any SNPs less than 3
    if tabline[6] >= 3:
        return True
    if tabline[7] >= 3:
        return True
    if tabline[8] >= 3:
        return True
    if tabline[9] >= 3:
        return True
    else:
        return False

def Step4(tabline, out_file):
    #Output file
    freqA = tabline[6]/tabline[3]
    freqT = tabline[7]/tabline[3]
    freqG = tabline[8]/tabline[3]
    freqC = tabline[9]/tabline[3]
    OF = open(out_file, 'a')
    if tabline[6] >=3:
        OF.write(f"{tabline[0]}\t{tabline[1]}\t{tabline[2]}\tA\t{freqA}\n")
    if tabline[7] >=3:
        OF.write(f"{tabline[0]}\t{tabline[1]}\t{tabline[2]}\tT\t{freqT}\n")
    if tabline[8] >=3:
        OF.write(f"{tabline[0]}\t{tabline[1]}\t{tabline[2]}\tG\t{freqG}\n")
    if tabline[9] >=3:
        OF.write(f"{tabline[0]}\t{tabline[1]}\t{tabline[2]}\tC\t{freqC}\n")

def main(argv):
    script, in_file, out_file, image = argv


    with open(in_file, 'r') as ifh:
        line = ifh.readline()
        #Iterate through each line of the file. Anything relating to the lines.
        while(line):
            tabline =  line.split("\t")
            tabline[3] = int(tabline[3])

            #Step 1: Line Filters
            S1 = Step1(tabline)
            if S1 == True:
                #Step 2: Counting
                Step2(tabline)
                #print(tabline)
            #Step 3: SNP Detection
                S3 = Step3(tabline)
                if S3 == True:
                    Step4(tabline, out_file)
            line = ifh.readline()
        print("End of output file. Begin image generation.")

    print("End")
main(argv)
