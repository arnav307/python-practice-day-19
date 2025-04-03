def reduce_spaces():
    with open ('text_file.txt','r') as input_file:
        output=input_file.readline()
        combine=' '.join(output.split())
        print(combine)
reduce_spaces()
