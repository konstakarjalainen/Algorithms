import sys


def qsort(s, e, V, d):
    if s >= e:
        print(f"Immediate return from subarray {s}...{e} with depth {d}")
        return []
    pivot = V[e//2]
    print(f"Sorting subarray {s}...{e} with depth {d} and pivot {pivot}")
    if len(pivot) > d:
        pivot_char = pivot[d]
    else:
        pivot_char = ' '
    left_arr = []
    middle_arr = []
    right_arr = []
    for word in V:
        if len(word) > d:
            compare_char = word[d]
        else:
            compare_char = ' '
        if compare_char == pivot_char:
            middle_arr.append(word)    
        elif compare_char < pivot_char:
            left_arr.append(word)
        else:
            right_arr.append(word)
    
    left_len = len(left_arr)
    middle_len = len(middle_arr)
    left_arr = qsort(0, left_len-1, left_arr, d)
    if pivot_char != " ":
        middle_arr = qsort(left_len, left_len+middle_len-1, middle_arr, d+1)
    right_arr = qsort(left_len+middle_len, left_len+middle_len+len(right_arr)-1, right_arr, d)
    return [left_arr, middle_arr, right_arr]

file_name = sys.argv[1]

file = open(file_name, "r")

string_arr = []

for word in file:
    string_arr.append(word.split()[0])

print("Original: " + " ".join(map(str, string_arr)))

sorted_arr = qsort(s=0, e=len(string_arr)-1, V=string_arr, d=0)
print("Sorted: " + " ".join(map(str, sorted_arr)))