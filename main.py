def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
    result.append(a1)
    result.append(a2)
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    for i in range(3, N + 1):
        result.append((result[i - 3] + result[i - 2]))
    print(result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result



if __name__ == '__main__':
    main()
