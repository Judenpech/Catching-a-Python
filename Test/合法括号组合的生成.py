def foo(output, open, close, pairs):
    if open == pairs and close == pairs:
        ls.append(output)
    else:
        if open < pairs:
            foo(output + "(", open + 1, close, pairs)
        if close < open:
            foo(output + ")", open, close + 1, pairs)


n = eval(input())
ls = []
foo('', 0, 0, n)
print(ls)