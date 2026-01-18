import math

def f(x):
    """
    Define your function here.
    Example: f(x) = cos(x) - x
    """
    return math.cos(x) - x

def secant(x0, x1, tol=10**-6, max_iter=100):
    """
    Secant Method
    - Does NOT require bracketing
    - Uses two previous points to approximate derivative (no f'(x) needed)
    """
    for i in range(1, max_iter + 1):
        f0 = f(x0)
        f1 = f(x1)

        if (f1 - f0) == 0:
            raise ZeroDivisionError("Secant failed: f(x1) - f(x0) = 0")

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        err = abs(x2 - x1)

        print(f"iter={i:3d} x0={x0:.10f} x1={x1:.10f} x2={x2:.10f} err={err:.3e}")

        if err < tol:
            return x2

        x0, x1 = x1, x2

    return x1

if __name__ == "__main__":
    root = secant(x0=0.5, x1=1.0, tol=10**-6, max_iter=100)
    print("\nroot ≈", root)
