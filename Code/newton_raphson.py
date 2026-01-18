import math

def f(x):
    """
    Define your function here.
    Example: f(x) = x^3 - 2x - 5
    """
    return x**3 - 2*x - 5

def df(x):
    """
    Define derivative of f(x) here.
    Example: f'(x) = 3x^2 - 2
    """
    return 3*x**2 - 2

def newton_raphson(x0, tol=10**-6, max_iter=100):
    """
    Newton-Raphson Method
    - Requires derivative f'(x)
    - Usually converges fast if initial guess is close to the root
    """
    x = x0

    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ZeroDivisionError("Newton-Raphson failed: f'(x) = 0")

        x_new = x - fx / dfx
        err = abs(x_new - x)

        print(f"iter={i:3d} x={x:.10f} x_new={x_new:.10f} f(x)={fx:.3e} err={err:.3e}")

        if err < tol:
            return x_new

        x = x_new

    return x

if __name__ == "__main__":
    root = newton_raphson(x0=2.0, tol=10**-6, max_iter=100)
    print("\nroot ≈", root)
