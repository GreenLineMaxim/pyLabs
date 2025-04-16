if __name__ == "__main__":
    number = {i for i in range(10000 + 1)}
    array = []
    for n in range(0, 100):
        for m in range(0, 100):
            if n * n + m * m in number:
                if not(n * n + m * m in array): 
                    array.append(n * n + m * m)
    array.sort()
    print(array)



            
