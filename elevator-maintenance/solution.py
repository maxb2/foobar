def version_string_to_list(x):
    v_list = [None,None,None]
    x_split = x.split(".")
    for i in range(len(x_split)):
        v_list[i] = int(x_split[i])
    return v_list

def sorter(v_list):
    if v_list[1] is None:
        minor = 0
    else:
        minor = v_list[1] +1

    if v_list[2] is None:
        rev = 0
    else:
        rev = v_list[2] +1

    return (v_list[0], minor, rev)

def solution(l):
    return sorted(l, key=lambda x: sorter(version_string_to_list(x)) )