"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = set((1, 3, 4, 7, 12))


def f(x):
    return x * 4 + 6

def add_entry(
    a,
    f_a,
    b,
    f_b,
    c,
    f_c,
    d,
    f_d,
):
    entries = {}
    entries[f'f({a}) + f({b}) = f({c}) - f({d})'] = f'{f_a} + {f_b} = {f_c} - {f_d}'
    entries[f'f({a}) + f({d}) = f({c}) - f({b})'] = f'{f_a} + {f_d} = {f_c} - {f_b}'
    entries[f'f({b}) + f({a}) = f({c}) - f({d})'] = f'{f_b} + {f_a} = {f_c} - {f_d}'
    entries[f'f({b}) + f({d}) = f({c}) - f({a})'] = f'{f_b} + {f_d} = {f_c} - {f_a}'
    entries[f'f({d}) + f({b}) = f({c}) - f({a})'] = f'{f_d} + {f_b} = {f_c} - {f_a}'
    entries[f'f({d}) + f({a}) = f({c}) - f({b})'] = f'{f_d} + {f_a} = {f_c} - {f_b}'
    for (k, v) in entries.items():
        print(f'{k}   {v}')

SORTED_Q = list(q)
SORTED_Q.sort()
C_MAP = {f(c): c for c in SORTED_Q}
HIGHEST = f(max(C_MAP.keys()))
for (a_index, a) in enumerate(SORTED_Q):
    f_a = f(a)
    for (b_index, b) in enumerate(SORTED_Q[a_index : ]):
        f_b = f(b)
        for d in SORTED_Q[a_index + b_index : ]:
            f_d = f(d)
            f_c = f_a + f_b + f_d
            if f_c in C_MAP:
                add_entry(a, f_a, b, f_b, C_MAP[f_c], f_c, d, f_d)
            elif f_c > HIGHEST:
                break
