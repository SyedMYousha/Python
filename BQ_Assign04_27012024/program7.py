#  program to create a file where all letters of the English alphabet are listed by a specified number of letters on each line


letters_per_line = int(input("enter the number of letter per line: "))
alpha_file = open("program7exFile.txt", "w")

def alphabet_sequence_Handler(alpha_file, letters_per_line):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, len(alphabet), letters_per_line ):
        line = alphabet[i: i+letters_per_line]
        alpha_file.write(line + '\n')

alphabet_sequence_Handler(alpha_file, letters_per_line)