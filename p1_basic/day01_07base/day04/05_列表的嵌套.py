lst = ['admin', 'gay', 'root', ['范冰冰', '唐嫣', [1, '火锅', 'Superman', '凤爪'], '杨幂']]
print(lst[3][2][1])  # 火锅
lst[3][2][2] = lst[3][2][2].upper()
print(lst)

lst[3][2][0] = lst[3][2][0] + 99
print(lst)
