# UNIT 9


# EX 9.1.1
def are_files_equal(file1, file2):
    with open(file1, "r") as opened_file1:
        file1_data = opened_file1.read()
    with open(file2, "r") as opened_file2:
        file2_data = opened_file2.read()
    return file1_data == file2_data


# EX 9.1.2
def main():
    filepath = input("Enter file path: ")
    function = input("Enter the function you ant to preform on the file data: ")
    file = open(filepath,"r")
    if function == 'sort':
        file_data = file.read()
        splitted = file_data.split(" ")
        words = []
        for word in splitted:
            if word.isalpha() and word not in words:
                words.append(word)
        print(sorted(words))
    elif function == 'rev':
        for line in file:
            print(line[::-1])
    elif function == 'last':
        n = int(input("Enter amount of rows "))
        last_n_lines = []
        for line in file:
            last_n_lines.append(line.strip())
            if len(last_n_lines) > n:
                last_n_lines.pop(0)
        for line in last_n_lines:
            print(line)


if __name__ == "__main__":
    main()



# EX 9.2.1
# תודפס הודעת שגיאה


# EX 9.2.2
def copy_file_content(source, destination):
    with open(source,"r") as sourcefile:
        data = sourcefile.read()
    with open(destination,"w") as destinationfile:
        destinationfile.write(data)


# EX 9.2.3
def who_is_missing(file_name):
    with open(file_name, 'r') as file:
        numbers = file.read().split(',')
    numbers = [int(num) for num in numbers if num]
    missing_number = None
    for i in range(1, len(numbers) + 2):
        if i not in numbers:
            missing_number = i
            break
    
    with open('found.txt', 'w') as file:
        file.write(str(missing_number))
    return missing_number



# EX 9.3.1
def my_mp3_playlist(file_path):
    songs = []
    with open(file_path,"r") as file:
        for line in file:
            splitted = line.split(";")
            dict = {"song":splitted[0],"writer":splitted[1],"length":splitted[2]}
            songs.append(dict)

    longest_song = None
    max_length = 0
    prolific_writer = None
    max_song_count = 0
    writer_count = {}

    for song in songs:
        minutes, seconds = map(int, song['length'].split(':'))
        song_length = minutes * 60 + seconds
        if song_length > max_length:
            longest_song = song
            max_length = song_length
        writer = song['writer']
        if writer in writer_count:
            writer_count[writer] += 1
        else:
            writer_count[writer] = 1
        if writer_count[writer] > max_song_count:
            prolific_writer = writer
            max_song_count = writer_count[writer]

    return (longest_song["song"],len(songs),prolific_writer)


# EX 9.3.2
def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if len(lines) >= 3:
        splitted = lines[2].split(";")
        splitted[0] = new_song
        lines[2] = ";".join(splitted)
    elif len(lines) == 2:
        lines.append(f"{new_song};;\n")
    else:
        while len(lines) <=2:
            lines.append(";;;\n")
        lines.append(f"{new_song};;\n")
    with open(file_path, 'w') as file:
        file.writelines(lines)
    with open(file_path, 'r') as file:
        data = file.read()
    print(data)



# EX 9.4.1
def choose_word(file_path, index):
    with open(file_path,"r") as file:
        file_data = file.read()
    words = file_data.split(" ")
    i=0
    while index>1:
        if i+1==len(words):
            i=0
        else:
            i+=1
        index-=1
    lst = []
    for word in words:
        if word not in lst:
            lst.append(word)
    return (len(lst),words[i])
