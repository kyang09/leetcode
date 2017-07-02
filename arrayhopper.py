import sys
__author__ = 'spencertank'

# min jumps to A[n-1]
def findMinHops(inp):
    jumps = [float("inf") for i in range(0, len(inp) + 1)]
    locations = []

    if (len(inp) == 0 or inp[0] == 0):
        return -2
    
    jumps[0] = 0
    locations.append(0)
    for i in range(1, len(inp) + 1):
        for j in range(0, i):
            if (i <= j + inp[j]) and (jumps[j] != float("inf")):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                locations.append(j)
                break
    print(locations)
    return jumps[-1]

if __name__ == "__main__":
    try:
        a = 1
    except ZeroDivisionError:
        print("hi")

    print(a)
    output = findMinHops([2, 1, 1, 5])
    if output == -2:
        print ("not possible!")
    print (output)