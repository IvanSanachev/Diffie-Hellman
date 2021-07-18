p, a, b = int(input('Пожалуйста, введите целое число p.\n')), int(input('Пожалуйста, введите целое число a.\n')), int(input('Пожалуйста, введите целое число b.\n'))
print(a ** b % p)
ab2, message = int(input('Пожалуйста, введите число ab2.\n')), input('Пожалуйтса, введите сообщение, чтобы зашифровать его\n')
key, codemessage = ab2 ** b % p, [ord(message[i]) for i in range(len(message))]
print(*[key ** codemessage[i] % p for i in range(len(codemessage))], sep=' ')
code, x = [int(s) for s in input('Пожалуйтса, введите код-сообщение, чтобы расшифровать его\n').split()], [key ** i % p for i in range(1200)]
print(*[chr(x.index(code[i])) for i in range(len(code))], sep='')