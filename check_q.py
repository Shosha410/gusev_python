def check_q(s):
  stack = ''
  op,cl = '([{ )]}'.split()
  for c in s:
    if c in op:
      stack += c
    elif c in cl:
      if stack == '':
        return False
      elif op[cl.index(c)] == stack[-1]:
        stack = stack[:-1]
  return stack == ''    
 
a = input()

 
print(f'В строке "{a}" скобки расставлены {"" if check_q(a) else "не "}правильно.')

// [((())()(())]] - Данную скобочную последовательность нельзя считать правильной. 
// Правильный вариант : [((())()(()))] или [[(())()(())]]
// Правильность скобочной последовательности проверялась алгоритмом выше.
