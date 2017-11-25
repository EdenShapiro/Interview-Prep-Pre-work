
def prettyPrint(A):

    def prettyPrint2(A, arr = [[1]], counter = 1):
        if A == counter:
            return arr
        else:
            counter+=1

            length = len(arr)
            new_length = length + 2

            for i in range(length):
                arr[i].insert(0, counter)
                arr[i].append(counter)
            arr_top = []
            arr_bottom = []
            for i in range(new_length):
                arr_top.append(counter)
                arr_bottom.append(counter)
            arr.insert(0, arr_top)
            arr.append(arr_bottom)

            return prettyPrint2(A, arr, counter)

    return prettyPrint2(A)




# print prettyPrint(3)
# print ""
print prettyPrint(5)
print ""
# print prettyPrint(2)
# print ""
# print prettyPrint(1)
# print ""
