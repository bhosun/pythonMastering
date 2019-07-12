row_num = 12
col_num = 12

row_index = 1
col_index = 2
table = ""

while True:
    if row_index > row_num:
        break
    table += str(row_index * col_index) + "\t"
    col_index += 1

    if col_index > col_num:
        col_index = 2
        row_index += 1
        table += "\n"

print(table)