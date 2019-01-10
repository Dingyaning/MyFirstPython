def addTwoNums(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    ten_flag = 0;
    return_node = {}
    min_length = min(len(l1), len(l2))
    print(min_length)
    for i in range(min_length):
        count = l1.val + l2.val + ten_flag
        if count > 10:
            ten_flag = 1
            current_count = count - 10
        else:
            current_count = count

        return_node[i] = current_count

    if len(l1) > min_length:
        for i in range(min_length, len(l1)):
            return_node[i] = l1[i]

    if len(l2) > min_length:
        for i in range(min_length, len(l2)):
            return_node[i] = l2[i]

    return return_node


l1 = {2, 4, 3}
l2 = {5, 6, 4}
print(addTwoNums(l1, l2))
