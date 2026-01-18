import math

def f(x):
    """
    Define your function here.
    Example: f(x) = x^3 - 4x - 9
    """
    return x**3 - 4*x - 9

def bisection(a, b, tol=10**-6, max_iter=100):
    """
    Bisection Method
    - Requires f(a)*f(b) < 0 (root is bracketed in [a,b])
    - Stops when |f(c)| < tol or interval width is smaller than tol
    """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("Bisection needs f(a)*f(b) < 0 to guarantee a root in [a,b].")

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)

        print(f"iter={i:3d} a={a:.10f} b={b:.10f} c={c:.10f} f(c)={fc:.3e}")

        if abs(fc) < tol or abs(b - a) < tol:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return c

if __name__ == "__main__":
    root = bisection(a=2, b=3, tol=10**-6, max_iter=100)
    print("\nroot ≈", root)
