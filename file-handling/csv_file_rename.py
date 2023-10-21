with open("sample.csv", "r") as sample_csv:
    for line in sample_csv:
        line_list = line.split(',')
        print(line_list)
        print(line)

