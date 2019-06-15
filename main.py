"""main.py file representingcomparison statistics for Pyrunc module"""


# Python module(s)
import timeit


# Project module(s)
from Pyrunc import Pyrunc


def main():
    """Main Method"""

    # Example 1: 2 Number adder
    pr_c = Pyrunc()
    obj_id, obj = pr_c.build(
        """int two_number_adder(int a, int b) {
        return a+b;
    }"""
    )
    print(
        "Two number adder demonstrating sum of 5 and 3, result:",
        obj.two_number_adder(5, 3),
    )

    # Comparison
    psetup = """def adder(a,b):
        return a+b"""

    csetup = """
from Pyrunc import Pyrunc
pr_c = Pyrunc()
obj_id, obj = pr_c.build('''int adder(int a, int b) {
    return a+b;
}''')
adder = obj.adder
"""
    print("Comparison:-")
    print("C code:", timeit.timeit(stmt="adder(30, 10)", setup=csetup, number=1000))
    print("Python:", timeit.timeit(stmt="adder(30, 10)", setup=psetup, number=1000))

    # Example 2: Sum of first n natural number calculator
    obj_id2, obj2 = pr_c.build(
        """int sum_n_natural_numbers(int a)
    {
        int i,ans=0;
        for(i=1; i<=a; ++i)
            ans += i;
        return ans;
    }"""
    )
    print(
        "Sum of first n natural numbers with nuber 30, result:",
        obj2.sum_n_natural_numbers(30),
    )


if __name__ == "__main__":
    main()


# import timeit
# setu1 = """def adder(a):
#     return mul(i for i in range(1, a))"""
# setu2 = """def adder(a):
#     ans=1
#     for i in range(1, a):
#         ans *= i
#     return ans"""
# setup = """from Pyrunc import Pyrunc
# pr_c = Pyrunc()
# obj_id, obj = pr_c.build('''int adder(int a) {
#     int i, ans=1;
#     for(i=1; i<a; ++i)
#         ans *= i;
# }''')
# adder = obj.adder
# """
# print("-------------------------------------------------------------------")
# print("A", timeit.timeit(stmt="adder(30)", setup=setup, number=1000) * 10 ** 4)
# print("B", timeit.timeit(stmt="adder(30)", setup=setu1, number=1000) * 10 ** 4)
# print("C", timeit.timeit(stmt="adder(30)", setup=setu2, number=1000) * 10 ** 4)
