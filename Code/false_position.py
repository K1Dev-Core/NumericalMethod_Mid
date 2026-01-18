import math

def f(x):
    """
    Define your function here.
    Example: f(x) = e^(-x) - x
    """
    return math.exp(-x) - x

def false_position(a, b, tol=10**-6, max_iter=100):
    """
    False Position (Regula Falsi) Method
    - Requires f(a)*f(b) < 0 (root is bracketed in [a,b])
    - Uses a line between (a,f(a)) and (b,f(b)) to estimate root
    """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("False position needs f(a)*f(b) < 0 to guarantee a root in [a,b].")

    xr = None
    for i in range(1, max_iter + 1):
        xr = (a * fb - b * fa) / (fb - fa)
        fxr = f(xr)

        print(f"iter={i:3d} a={a:.10f} b={b:.10f} xr={xr:.10f} f(xr)={fxr:.3e}")

        if abs(fxr) < tol:
            return xr

        if fa * fxr < 0:
            b = xr
            fb = fxr
        else:
            a = xr
            fa = fxr

    return xr

if __name__ == "__main__":
    root = false_position(a=0, b=1, tol=10**-6, max_iter=100)
    print("\nroot ≈", root)
