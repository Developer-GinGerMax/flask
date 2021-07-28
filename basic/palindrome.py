def str_to_list(payload: str) -> [] :
    return [i for i in payload if i.isalnum()]


def isPalindrome(ls: []) -> bool:
    return {"RESULT": False for i in ls if ls.pop(0) != ls.pop()}


if __name__ == '__main__':
    ls = str_to_list("A man, a plan, a canal: Panama")
    print(ls)
    isPal = isPalindrome(ls)
    print(isPal["RESULT"])