# Integrator
*Only got differentiation working though :)*

## Example
$$f(x)
= x^{(\sin(\cos(x^2)))^{\log(\tan(x^2))}}$$


$$\frac{df}{dx} =(\sin(\cos(x^2)))^{\log(\tan(x^2))}
\left[
\frac{2x\sec^2(x^2)}{\tan(x^2)}\ln(\sin(\cos(x^2)))
+
\log(\tan(x^2))\frac{-2x\sin(x^2)\cos(\cos(x^2))}{\sin(\cos(x^2))}
\right]$$

## AST EXAMPLE
```py
Add(
    left=Mul(
        left=Pow(
            base=Var(name='x'), 
            exp=Pow(
                base=Var(name='x'), 
                exp=2)), 
        right=Add(
            left=Mul(
                left=Pow(
                    base=Var(name='x'), 
                    exp=2), 
                right=Div(
                    numerator=Const(value=1), 
                    denominator=Var(name='x'))), 
            right=Mul(
                left=Log(expr=Var(name='x')), 
                right=Mul(
                    left=Const(value=2), 
                    right=Var(name='x'))))), 
    right=Const(value=2))


Mul(
    left=Pow(
        base=Var(name='x'), 
        exp=Pow(
            base=Sin(expr=Cos(expr=Pow(
                        base=Var(name='x'), 
                        exp=2))), 
            exp=Log(expr=Tan(expr=Pow(
                base=Var(name='x'), 
                exp=2))))), 
    right=Add(
        left=Mul(
            left=Pow(
                base=Sin(expr=Cos(expr=Pow(
                    base=Var(name='x'), 
                    exp=2))), exp=Log(expr=Tan(expr=Pow(
                        base=Var(name='x'), 
                        exp=2)))), 
            right=Mul(
                left=Div(
                    numerator=Const(value=1), 
                    denominator=Var(name='x')), 
                right=Const(value=1))), 
        right=Mul(
            left=Log(expr=Var(name='x')), 
            right=Mul(left=Pow(
                base=Sin(expr=Cos(expr=Pow(
                    base=Var(name='x'), 
                    exp=2))), 
                exp=Log(expr=Tan(expr=Pow(
                    base=Var(name='x'), 
                    exp=2)))), 
                    right=Add(
                        left=Mul(
                            left=Log(expr=Tan(expr=Pow(
                                base=Var(name='x'), 
                                exp=2))), 
                            right=Mul(
                                left=Div(
                                    numerator=Const(value=1), 
                                    denominator=Sin(expr=Cos(expr=Pow(
                                        base=Var(name='x'), 
                                        exp=2)))), 
                                right=Mul(
                                    left=Cos(expr=Cos(expr=Pow(
                                        base=Var(name='x'), 
                                        exp=2))), 
                                    right=Mul(
                                        left=Mul(
                                            left=Const(value=-1), 
                                            right=Sin(expr=Pow(
                                                base=Var(name='x'), 
                                                exp=2))), 
                                        right=Mul(
                                            left=Const(value=2), 
                                            right=Pow(
                                                base=Var(name='x'), 
                                                exp=1)))))), 
                            right=Mul(
                                left=Log(expr=Sin(expr=Cos(expr=Pow(
                                    base=Var(name='x'), 
                                    exp=2)))), 
                                right=Mul(
                                    left=Div(
                                        numerator=Const(value=1), 
                                        denominator=Tan(expr=Pow(
                                            base=Var(name='x'), 
                                            exp=2))), 
                                    right=Mul(
                                        left=Pow(
                                            base=Sec(expr=Pow(
                                                base=Var(name='x'), 
                                                exp=2)), 
                                                exp=Const(value=2)), 
                                        right=Mul(
                                            left=Const(value=2), 
                                            right=Pow(
                                                base=Var(name='x'), 
                                                exp=1))))))))))
```
