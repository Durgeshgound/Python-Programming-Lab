#Write functions to organize a program that performs basic operations on strings and lists.

# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Function to count characters in string
def count_characters(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Function to concatenate two strings
def concatenate_strings(s1, s2):
    return s1 + s2

# Function to slice a string
def slice_string(s, start, end):
    return s[start:end]


# Function to find maximum element
def find_max(lst):
    return max(lst)

# Function to reverse list
def reverse_list(lst):
    return lst[::-1]

# Function to sort list
def sort_list(lst):
    return sorted(lst)

# Function to merge two lists
def merge_lists(lst1, lst2):
    return lst1 + lst2


# String operations
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print("Reversed string:", reverse_string(s1))
print("Character frequency:", count_characters(s1))
print("Concatenated string:", concatenate_strings(s1, s2))
print("Sliced string (0 to 3):", slice_string(s1, 0, 3))

# List operations
lst1 = list(map(int, input("Enter list elements: ").split()))
lst2 = list(map(int, input("Enter another list: ").split()))

print("Maximum element:", find_max(lst1))
print("Reversed list:", reverse_list(lst1))
print("Sorted list:", sort_list(lst1))
print("Merged list:", merge_lists(lst1, lst2))