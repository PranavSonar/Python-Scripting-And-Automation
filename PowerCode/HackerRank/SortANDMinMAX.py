a = '11 4 5 2 3 4'
a = a.split()
print(a)


def sort_arr(arr):
    for i in range(len(arr)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            print(a)
            sort_arr(a)

    return(a)


a = sort_arr(a)

# def miniMaxSum(arr):
#     l_summin=0
#     l_summax=0
#     def sort_arr(arr):
#         for i in range(len(arr)-1):
#             if a[i]>a[i+1]:
#                 a[i],a[i+1]=a[i+1],a[i]
#                 sort_arr(a)
#         arr=a
#     sort_arr(arr)
#     for i in range(len(arr)-1):
#         l_summin+=int(a[i])
#     for i in range(1,len(arr)):
#         l_summax+=int(a[i])
#     return(l_summin,l_summax)

# print(l_min,l_max)
print(a)

# miniMaxSum(a)
