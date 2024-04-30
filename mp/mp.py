import sys


def precomputeFMP(P):
    fmp = [0] * len(P)
    T_P = P[1:]
    n = len(P) - 1
    i = 0
    j = 0
    while i < n:
        while i < n and T_P[i].lower() == P[j].lower():
            i += 1
            j += 1
            fmp[i] = j
        if j > 0:
            j = fmp[j-1]
        else:
            i += 1
    return fmp


def MP(P, T, fmp):
    n = len(T) - 1
    m = len(P) - 1
    i = 0
    j = 0
    while i - j <= n - m:
        start_j = j
        start_i = i
        print(f"P at pos {i-j} with i = {i} and j = {j}")
        while j <= m and T[i].lower() == P[j].lower():
            i += 1
            j += 1
        if j > start_j:
            print(f"  matched T[{start_i}..{i-1}] = {T[start_i:i]} = P[{start_j}..{j-1}] = {P[start_j:j]}")
        if j-1 == m:
            print("  found an occurrence of P")
        else:
            print(f"  mismatch T[{i}] = {T[i]} != P[{j}] = {P[j]}")
        if j == 0:
            i += 1
            j = 0
            print(f"  incremented i from {i-1} to {i}")
        else:
            print(f"  updated j from {j} to fm[{j-1}] = {fmp[j-1]}")
            j = fmp[j-1]


filename = sys.argv[1]

with open(filename, 'r') as file:
    i = 0
    P = file.readline().strip()
    T = file.readline().strip()

print(f"P: {P}")
fmp = precomputeFMP(P)
fmp_string = " ".join(map(str,fmp))
print(f"Function fm: {fmp_string}")

MP(P, T, fmp)
