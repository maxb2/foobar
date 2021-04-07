# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -ExecuteTime,-execute,-execution
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
The cake is not a lie!
======================

Commander Lambda has had an incredibly successful week: she completed the first test run of her LAMBCHOP doomsday device, she captured six key members
of the Bunny Rebellion, and she beat her personal high score in Tetris. To celebrate, she's ordered cake for everyone - even the lowliest of
minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone, you'll get in big trouble.

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are
multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so
you also want to make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z)
corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

Write a function called answer(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the
maximum number of equal parts that can be cut from the cake without leaving any leftovers.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) s = "abccbaabccba"
Output: 2

Inputs:
    (string) s = "abcabcabcabc"
Output: 4

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your
solution passes the test cases, it will be removed from your home folder.


# %%
def solution(s):
    string_length = len(s)
    if s.isalpha() == False:
        return "oops...you can't put other candies on the cake! Only M&Ms allowed."
    elif string_length > 200:
        return "oops...provided string is too long. The minions will have a sugar crash with that many M&Ms!"
    elif string_length == 0:
        return "oops...empty string provided. Your cake can't be missing M&Ms!"
    else:
        string_twice = s + s
        max_subseq_count=0
        for start_pos in range(string_length):
            end_pos = start_pos+string_length
            sub_string = string_twice[start_pos:end_pos]
            for k in range(string_length):
                sub_string_length = k+1
                if string_length % (sub_string_length) == 0:
                    subseq_count = int(string_length/(sub_string_length))
                    s_subseq_count=0
                    for m in range(subseq_count):
                        if (sub_string[m*sub_string_length:m*sub_string_length+sub_string_length]==sub_string[m*sub_string_length+sub_string_length:m*sub_string_length+2*sub_string_length]):
                            s_subseq_count+=1
                    if s_subseq_count+1 == subseq_count:
                        if max_subseq_count < subseq_count:
                            max_subseq_count=subseq_count
        return max_subseq_count
    

                            

#                     print(string_length)

#                     print(k+1)

#             print(sub_string)
# print(solution('abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'))
# print(solution(''))
print(solution('abcabcabcabc'))
print(solution('abccbaabccba'))
print(solution('abcdefabcdefghijklmnopqrstuvwxyzabcdefabcdef'))

print(solution('abccbaabccbaabccbaabccba'))


# %%
