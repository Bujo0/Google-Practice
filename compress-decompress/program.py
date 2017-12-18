ent = input()

def find_substring(s, digit_flag):
    if digit_flag:
        balance = 0
        for x in range(len(s)):
            if s[x] is "[":
                balance += 1
            if s[x] is "]":
                balance -= 1
            if balance == 0:
                break

        return s[1:x], x + 2

    else:
        for x in range(len(s)):
            if s[x] is "[" or s[x] is "]" or s[x].isdigit():
                return s[:x], x
        return s, x + 1

# expand particular substring, using the outer function below when the substring needs to also be parsed
def expand(s, res):
    i = 0
    j = i
    digit_flag = False
    if s[0].isdigit():
        digit_flag = True
        while s[i] is not '[':
            i += 1

    if i > 0:
        reps = int(s[j:i])
    else:
        reps = 1

    to_repeat, to_continue = find_substring(s[i:], digit_flag)

    if not to_repeat:
        return -1

    if digit_flag is False:
        res += to_repeat
        return res, to_continue

    iter = res
    for i in range(reps):

        if expand(to_repeat, iter) == -1:
            res += to_repeat

        else:
            expanded = outer(to_repeat)
            res += expanded

    return res, to_continue


def outer(s):
    result = ""
    while 0 < len(s):
        ret, cont = expand(s, "")
        result += ret
        s = s[cont:]

    return result

print(outer(ent))
