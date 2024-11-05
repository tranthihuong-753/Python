""" 
Bài tập 2. Cho mảng a các số nguyên. Yêu cầu in lên số lớn thứ nhì của mảng.
"""

def printsolonthuhai(arr):
    max1 = max2 = 0
    for x in arr:
        if(x > max2 and x < max1):
            max2 = x
        elif( x > max1):
            max2 = max1
            max1 = x 
    print(f"So lon thu 2 trong mang {arr} la ", max2)

arr = [2, 4, 3, 4, 2, 5, -5, 4, 4, 5, 6, 6]
printsolonthuhai(arr)