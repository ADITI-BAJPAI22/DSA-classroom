
'''
Given a number n, print 1-n.


def print_numbers(n):
    if n <= 0:
        return
    print_numbers(n-1)
    print(n)

n = int(input("Enter the value of n: "))
print("Numbers are:")
print_numbers(n)


'''

'''
Given a number n, print n-1.


def print_numbers(n):
  if n > 1:
    print_numbers(n-1)
    print(n-1)

n = int(input("Enter a number: "))
if n > 1:
  print_numbers(n)
else:
  print("The number should be greater than 1.")


'''


'''
Given an array print array.

def print_array(arr, idx):
    if idx == len(arr):
        return
    print(arr[idx])
    print_array(arr, idx+1)

arr = [1, 2, 3, 4, 5]
print_array(arr, 0)

'''

'''
Print the array in reverse.

def print_array_reverse(arr, idx):
    if idx < 0:
        return
    print(arr[idx])
    print_array_reverse(arr, idx-1)

arr = [1, 2, 3, 4, 5]
print_array_reverse(arr, len(arr)-1)


'''

'''

Find the maximum of an array.

def find_max(arr, idx):

    if idx == 0:
        return arr[0]

    return max(arr[idx], find_max(arr, idx-1))

arr = [5, 9, 3, 7, 2]

max_val = find_max(arr, len(arr)-1)

print("Maximum Value:", max_val)


'''