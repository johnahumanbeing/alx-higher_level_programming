#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dic = sorted(a_dictionary.keys())
    for j in sort_dic:
        print(j, ":", a_dictionary[j])
