import timeit


setup1 = """def adder(a, b):
    return a * b + a - b"""

print("Hello World!!")
setup = """from Pyrunc import Pyrunc
pr_c = Pyrunc()
obj_id, obj = pr_c.build('''int adder(int a, int b) {
    
    return a * b + a - b;}''')
adder = obj.adder
"""
# print(pr_c.objs[obj_id].adder(2, 3))
# print('OR')
# print(obj.adder(3, 5))
print("-------------------------------------------------------------------")
print("A", timeit.timeit(stmt="adder(30, 15)", setup=setup, number=1000) * 10 ** 4)
print("B", timeit.timeit(stmt="adder(30, 15)", setup=setup1, number=1000) * 10 ** 4)
