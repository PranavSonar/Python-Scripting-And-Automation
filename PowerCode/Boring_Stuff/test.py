a = [1, 2,3,4]


def short(a):
    k = len(a)-1
    for i in range(len(a)):
        temp = a[i]
        a[i] = a[k-i]

        a[k-i] = temp
        b = a
        print(b)
    print(a)


short(a)


#! python3
# import sys
# print( "Hello World")
# # print(sys.argv[1])


# print(2**7)
# print(9%2)
# a=[1,2,3]
# b=[2,3,4]
# c=a+b

# print(a[1:0])


# A='3 5 7 11 5 8'.split(' ',)
# B='5 7 11 10 5 8'.split(' ',)
# def beautifulPairs(A, B):
#     # print (A)
#     count=0
#     p=[]
#     for i in range(len(A)):
#         for k in range(len(B)):
#             if A[i]==B[k]:
#                 count+=1
#                 p+=[(A[i],i,k)]
#                 # print("count %s,i %s,A[i] %s,k %s,B[k] %s" %(count,i,A[i],k,B[k]))
#     for i in range(len(p)):
#         print(p[i][2])

#     print(p)
#     print(len(p))

#     return count


# print(beautifulPairs(A, B))
