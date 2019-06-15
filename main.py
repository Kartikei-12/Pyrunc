"""main.py file representingcomparison statistics for Pyrunc module"""


# Python module(s)
from timeit import timeit


# Project module(s)
from Pyrunc import Pyrunc


def main():
    """Main Method"""

    pr_c = Pyrunc()
    # --------------------------------------------------------------------------------
    # ----------------Example 1: 2 Number adder---------------------------------------
    # --------------------------------------------------------------------------------
    print("Example 1:-")
    obj_id, obj = pr_c.build(
        """int two_number_adder(int a, int b) {
        return a+b;
    }"""
    )
    print(
        "\tTwo number adder demonstrating sum of 5 and 3, result:",
        obj.two_number_adder(5, 3),
    )

    # Comparison Example 1
    psetup = """def padder(a,b):
        return a+b"""

    csetup = """
from Pyrunc import Pyrunc
pr_c = Pyrunc()
obj_id, obj = pr_c.build('''int cadder(int a, int b) {
    return a+b;
}''')
cadder = obj.cadder
"""
    print("Comparison:-")
    print(
        "\tC code:", timeit(stmt="cadder(30, 10)", setup=csetup, number=1000) * 10 ** 5
    )
    print(
        "\tPython:", timeit(stmt="padder(30, 10)", setup=psetup, number=1000) * 10 ** 5
    )

    # ---------------------------------------------------------------------------------
    # ----------------Example 2: Sum of first n natural number calculator--------------
    # ---------------------------------------------------------------------------------
    print("\n\nExample 2:-")
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
        "\tSum of first n natural numbers with nuber 30, result:",
        obj2.sum_n_natural_numbers(30),
    )
    # Comparison
    c_setup = """
from Pyrunc import Pyrunc
pr_c = Pyrunc()
obj_id, obj = pr_c.build('''int csummer(int a) {
    int i, ans=0;
    for(i=0; i<=a; ++i)
        ans += i;
    return ans;
}''')
csummer = obj.csummer
"""
    psetup1 = """def psummer(a):
    ans = 0
    for i in range(a):
        ans += i
    return ans"""

    psetup2 = """def psummer(a):
    return sum(list(range(a)))"""

    psetup3 = """def psummer(a):
    return sum([i for i in range(a)])"""

    print("Comparison:-")
    print(
        "\tC  code:", timeit(stmt="csummer(30)", setup=c_setup, number=1000) * 10 ** 5
    )
    print(
        "\tPython1:", timeit(stmt="psummer(30)", setup=psetup1, number=1000) * 10 ** 5
    )
    print(
        "\tPython2:", timeit(stmt="psummer(30)", setup=psetup2, number=1000) * 10 ** 5
    )
    print(
        "\tPython3:", timeit(stmt="psummer(30)", setup=psetup3, number=1000) * 10 ** 5
    )


if __name__ == "__main__":
    main()
