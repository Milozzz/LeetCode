def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
           'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    num = []
    s_list = [e for e in s]
    print(s_list)
    index = 0
    while index < len(s_list):
        if index + 1 < len(s_list):
            if dic[s_list[index]] >= dic[s_list[index + 1]]:
                num.append(dic[s_list[index]])
                index += 1
            else:
                num.append(dic[s_list[index] + s_list[index + 1]])
                index += 2
        else:
            num.append(dic[s_list[index]])
            index += 1
        print(num)
    print(num, sum(num))


romanToInt("III")