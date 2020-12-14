
def operator_deletion(operator, sorted_lines):
    # Удаления из оператора всех символов, кроме букв, цифр и нижнего подчеркивания
    sorted_operator = ""
    for i in range(len(operator)):
        if operator[i].isalnum() or operator[i] == '_':
            sorted_operator += operator[i]

    # Изменение названия оператора во всех строках кода
    for i in range(len(sorted_lines)):
        line = sorted_lines[i]
        u = 0
        flag = True
        while flag:
            n = line.find(sorted_operator, u)
            u = n + len(sorted_operator)
            if n == -1:
                flag = False
            elif n == 0 and (line[n + len(sorted_operator)].isalnum() or line[n + len(sorted_operator)] == "_") is False:
                line = "OPR{}".format(line[(n + len(sorted_operator)):])
            elif n + len(sorted_operator) - 1 < len(line) - 1:
                if ((line[n - 1].isalnum() or line[n - 1] == "_") or (line[n + len(sorted_operator)].isalnum() or line[n + len(sorted_operator)] == "_")) is False:
                    line = "{}OPR{}".format(line[:n], line[(n + len(sorted_operator)):])
            elif n + len(sorted_operator) - 1 == len(line) - 1 and (line[n - 1].isalnum() or line[n - 1] == "_") is False:
                line = "{}OPR".format(line[:n])
        sorted_lines[i] = line
    return sorted_lines


def file_sorting(file_name):
    # Чтение файла
    file = open(file_name)
    lines = file.read().splitlines()
    file.close()

    # Удаление всех пустых строк и пробелов вначале кода
    new_lines = []
    for line in lines:
        if line == '':
            pass
        elif line[0] == " ":
            while line[0] == " ":
                line = line[1:]
            new_lines.append(line)
        else:
            new_lines.append(line)

    sorted_lines = new_lines

    # Поиск всех операторов и их игнорирование с помощью метода operator_deletion
    for line in new_lines:
        for i in range(len(line)):
            if i <= len(line) - 1:
                if line[i] == "O" and line[i + 1] == "P" and line[i + 2] == "R":
                    pass
                elif line[i] == "=" and line[i + 1] != "=":
                    sorted_lines = operator_deletion(line[:i], sorted_lines)
                elif line[i] == "f" and line[i + 1] == "o" and line[i + 2] == "r":
                    n = line.find("in")
                    sorted_lines = operator_deletion(line[(i + 3):n], sorted_lines)
                elif line[i] == "d" and line[i + 1] == "e" and line[i + 2] == "f":
                    n = line.find("(")
                    sorted_lines = operator_deletion(line[(i + 3):n], sorted_lines)

                    k = line.find("()")
                    param = ""
                    if k < 0:
                        short_line = line[n + 1:]
                        for j in short_line:
                            if j.isalnum() or j == "_":
                                param += j
                            elif j == ",":
                                sorted_lines = operator_deletion(param, sorted_lines)
                                param = ""
                            elif j == ")":
                                sorted_lines = operator_deletion(param, sorted_lines)
                                break

    # Удаление всех пробелов между словами
    for l in range(len(sorted_lines)):
        line = sorted_lines[l]
        line = line.replace(" ", "")
        sorted_lines[l] = line

    # Удаление всех комментариев
    for l in range(len(sorted_lines)):
        line = sorted_lines[l]
        n = line.find("#")
        if n >= 0:
            line = line[:n]
            sorted_lines[l] = line
    new_sorted_lines = []
    for line in sorted_lines:
        if line == '':
            pass
        else:
            new_sorted_lines.append(line)

    return sorted_lines


# Подсчет на плагиат
def counting(sorted_file_1, sorted_file_2):
    k = 0
    file_1 = sorted_file_1
    file_2 = sorted_file_2

    for i in range(len(file_1)):
        for j in range(len(file_2)):
            if file_1[i] == file_2[j]:
                k += 1
                file_2[j] = 'London is the capital of Great Britain 1'
                break

    if len(sorted_file_1) < len(sorted_file_2):
        q = len(sorted_file_2)
    else:
        q = len(sorted_file_1)

    return k / q
