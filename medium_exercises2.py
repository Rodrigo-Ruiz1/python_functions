list = ["apple", "zoom", "pop", "computer", "a", "whippersnapper"]


def shortest(list):
    shortest_string = list[0]
    string_length = len(list[0])
    for word in list:
        if (len(word) < string_length):
            shortest_string = word
            string_length = len(word)
    return shortest_string

#print(shortest(list))



def longest(list):
    longest_string = list[0]
    string_length_two = len(list[0])
    for word in list:
        if (len(word) > string_length_two):
            longest_string = word
            string_length_two = len(word)
    return longest_string

print(longest(list))