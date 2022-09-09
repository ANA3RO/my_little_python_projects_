'''
this program counts words in each file given
'''
def count(filename):
    #counting words in a file
    try:
        with open(filename,'r',encoding='cp1252') as f:
            read_content = f.read()
    except FileNotFoundError:
        print(f'{filename} not found')
    else:
        words = read_content.split()
        print(f'"{filename}" contains {len(words)} words!')

file_list = [r'files\file\car_name.txt',r'files\file\file.txt',r'files\file\guest_ist.txt']

for files in file_list:
    count(files)