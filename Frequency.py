def most_frequent(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


def sorted_value(d, reverse=True):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


string = input("Please enter the string")
print(sorted_value(most_frequent(string)))
