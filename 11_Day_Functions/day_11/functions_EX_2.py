# 1

def evens_and_odds(n):

    even_lst = []

    odd_lst = []

    for i in range(n + 1):
        
        if i % 2 == 0:
            
            even_lst.append(i)

        else:
            odd_lst.append(i)

    print("Number of Even numbers: ", len(even_lst))

    print("Number of Odd numbers: ", len(odd_lst))

evens_and_odds(100)