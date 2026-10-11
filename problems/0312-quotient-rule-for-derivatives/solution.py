import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g_dash = sum(g_coeffs[i]*(len(g_coeffs)-1-i)*x**(len(g_coeffs)-2-i) for i in range(len(g_coeffs)) if len(g_coeffs) - 1 - i > 0)
    g = sum(g_coeffs[i]*x**(len(g_coeffs)-1-i) for i in range(len(g_coeffs)))
    h_dash = sum(h_coeffs[i]*(len(h_coeffs)-1-i)*x**(len(h_coeffs)-2-i) for i in range(len(h_coeffs)) if len(h_coeffs) - 1 - i > 0)
    h = sum(h_coeffs[i]*x**(len(h_coeffs)-1-i) for i in range(len(h_coeffs)))
    return (g_dash*h - g*h_dash)/h**2