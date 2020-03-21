import sys

fichier = "C:/Users/loicm/projects/MyRepository/Epreuve_du_feu/sources_sudoku"


def file_to_list(file):
    with open(fichier, "r") as f:
        lst = f.read()
        lst = []

        for l in f:
            l = l.replace('\n', '')
            l = l.replace('|', '')
            l = l.replace('-', '')
            l = l.replace('+', '')
            if l != '':
                lst.append(l)

        return lst

def check_num_in_row(lst, row, num):
    if lst[row].count(num) > 0:
        return False
    return True


def check_num_in_columns(lst, col, num):
    for i in range(9):
        if lst[i][col] == num:
            return False
    return True

def check_case(lst, row, col, num):
    x = row/3
    y = col/3
    for i in range(3*x, 3*(x+1)):
        for j in range(3*y, 3*(y+1)):
            if lst[i][j] == num:
                return False
    return True



def get_misses(lst):
    misses = []
    for row in range(len(lst)):
        for col in range(len(lst)):
            if lst[row][col] == '_':
                misses.append([row, col,[]])
    return misses

def remove_uniques(lst, misses):
    for tpl in misses:
        choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        x, y = tpl[0], tpl[1]

        for e in lst[x]:
            if e in choice:
                choice.remove(e)
        
        for i in range(9):
            if lst[i][tpl[1]] in choice:
                choice.remove(lst[i][y])
        
        if len(choice) == 1:
            lst[x] = lst[x][:y] + choice[0] + lst[x][y+1:]
            misses.remove(tpl)
            remove_uniques(lst, misses)

    return misses

def print_grid(lst):
    print('')
    for l in range(len(lst)):
        print(lst[l][:3] + '|' + lst[l][3:6] + '|' + lst[l][6:9])

        if l == 2 or l == 5:
            print('---+---+---')
    print('')

    

def resolve(lst):
    misses = get_misses(lst)

    if misses == []:
        print_grid(lst)
        return True

    x = misses[0][0]
    y = misses[0][1]

    for num in range(1,10):

        if check_num_in_row(lst, x, str(num)) and check_num_in_columns(lst, y, str(num)) and check_case(lst, x, y, str(num)):

            lst[x] = lst[x][:y] + str(num) + lst[x][y+1:]

            if(resolve(lst)):
                return True

            lst[x] = lst[x][:y] + '_' + lst[x][y+1:]

    return False
    



if __name__ == "__main__":
    lst = file_to_list(sys.argv[1])

    resolve(lst)