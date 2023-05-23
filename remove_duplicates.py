def remove_duplicates(lst):
    lst[:] = sorted(set(lst))
    return len(lst)