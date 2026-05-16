def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return (Unknown(X + 1, Y) * 2)
    else:
        if X == Y:
            return 1
        else:
            print(X + Y)
            return (Unknown(X - 1, Y) // 2)
    

parameters1 = [10, 15]
print(f"Parameters: X: {parameters1[0]} and Y: {parameters1[1]}")
result1 = Unknown(parameters1[0], parameters1[1])
print(result1)

parameters2 = [10, 10]
print(f"Parameters: X: {parameters2[0]} and Y: {parameters2[1]}")
result2 = Unknown(parameters2[0], parameters2[1])
print(result2)

parameters3 = [15, 10]
print(f"Parameters: X: {parameters3[0]} and Y: {parameters3[1]}")
result3 = Unknown(parameters3[0], parameters3[1])
print(result3)

def IterativeUnknown(X, Y):
    for i in range(X, Y+1):
        if X < Y:
            print(X + Y)
        else:
            if X == Y:
                return 1
            else:
                print(X + Y)



# 12 / 17