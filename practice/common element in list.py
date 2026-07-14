def common(list1,list2):
    return list(set(list1) & set(list2))
list1 = ("ddoj","hhp")
list2 = ("hph","hhp")
result = common(list1, list2)
print(result)