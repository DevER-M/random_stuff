from dataclasses import dataclass
from typing import Union

class Expr:
    pass

@dataclass(frozen=True)
class Const(Expr):
    value: int | float

@dataclass(frozen=True)
class Var(Expr):
    name: str

@dataclass(frozen=True)
class Add(Expr):
    left: Expr
    right: Expr

@dataclass(frozen=True)
class Sub(Expr):
    left: Expr
    right: Expr

@dataclass(frozen=True)
class Mul(Expr):
    left: Expr
    right: Expr

@dataclass(frozen=True)
class Div(Expr):
    numerator: Expr | float
    denominator: Expr | float

@dataclass(frozen=True)
class Pow(Expr):
    base: Expr
    exp: int | float | Expr

@dataclass(frozen=True)
class Sin(Expr):
    expr:Expr

@dataclass(frozen=True)
class Cos(Expr):
    expr:Expr

@dataclass(frozen=True)
class Tan(Expr):
    expr:Expr

@dataclass(frozen=True)
class Cosec(Expr):
    expr:Expr

@dataclass(frozen=True)
class Sec(Expr):
    expr:Expr

@dataclass(frozen=True)
class Cot(Expr):
    expr:Expr

@dataclass(frozen=True)
class Log(Expr):
    expr:Expr


def D(expr:Expr):
    match expr:
        case Add(left,right)    : return Add(D(left), D(right))
        case Const(value)       : return Const(0)
        case Var(name)          : return Const(1)
        case Log(Const(value))  : return Const(0)
        case Log(x)             : return Mul(Div(Const(1),x),D(x))
        case Mul(left,right)    : return Add(Mul(left, D(right)), Mul(right, D(left)))
        case Sin(x)             : return Mul(Cos(x),D(x))
        case Cos(x)             : return Mul(Mul(Const(-1),Sin(x)),D(x))
        case Tan(x)             : return Mul(Pow(Sec(x),Const(2)),D(x))
        case Cosec(x)           : return Mul(Mul(Mul(Const(-1),Cosec(x)),Cot(x)),D(x))
        case Sec(x)             : return Mul(Mul(Sec(x),Tan(x)),D(x))
        case Cot(x)             : return Mul(Mul(Const(-1),Pow(Cosec(x),Const(2))),D(x))

        case Pow(base, int(exp)|float(exp)):
            return Mul(Const(expr.exp), Pow(expr.base, expr.exp-1))
        case Pow(base, exp): 
            return Mul(Pow(base, exp), D(Mul(exp, Log(base))))
        
        case _                  : raise ValueError("unknown function")


def show(expr: Expr):
    match expr:
        case Const(value)            : return str(value)
        case Mul(Const(value),right) : return f"{value}{show(right)}"
        case Mul(left,Const(value))  : return f"{value}{show(left)}"
        case Mul(left,right)         : return f"({show(left)})*({show(right)})"
        case Add(left,right)         : return f"({show(left)} + {show(right)})"
        case Sub(left,right)         : return f"({show(left)} - {show(right)})"
        case Var(name)               : return name
        case Sin(x)                  : return f"sin({show(x)})"
        case Cos(x)                  : return f"cos({show(x)})"
        case Tan(x)                  : return f"tan({show(x)})"
        case Cosec(x)                : return f"cosec({show(x)})"
        case Sec(x)                  : return f"sec({show(x)})"
        case Cot(x)                  : return f"cot({show(x)})"
        case Log(x)                  : return f"log({show(x)})"

        case Div(float(numerator),float(denominator)):
            return f"{numerator/denominator}"
        case Div(numerator,denominator):
            return f"({show(numerator)})/({show(denominator)})"

        case Pow(Var(name), exp) if isinstance(exp,(int,float)): 
            return f"{name}^{exp}"
        case Pow(base,exp):
            return f"({show(base)})^({show(exp)})"
        case other:
            return other

def simplify(expr: Expr):
    match expr:
        case Add(a, b):
            a, b = simplify(a), simplify(b)
            if a == Const(0): return b
            if b == Const(0): return a
            if isinstance(a, Const) and isinstance(b, Const):
                return Const(a.value + b.value)
            return Add(a, b)

        case Mul(a, b):
            a, b = simplify(a), simplify(b)
            match a,b:
                case Const(1),b:
                    return b
                case a,Const(1):
                    return a
                case a,b if a==Const(0) or b==Const(0):
                    return Const(0)
                case Const(a_value),Const(b_value):
                    return Const(a_value * b_value)
                case a,Div(numerator,denominator):
                    return simplify(Div(simplify(Mul(numerator,a)),denominator))
                case b,Div(numerator,denominator):
                    return simplify(Div(simplify(Mul(numerator,b)),denominator))
                case _:
                    return Mul(a, b)

        case Div(numerator,denominator):
            numerator,denominator=simplify(numerator),simplify(denominator)
            match numerator,denominator:
                case numerator,Const(1):
                    return numerator
                case Pow(x1,n),Pow(x2,m) \
                    if x1==x2 and isinstance(n,(int,float)) and isinstance(m,(int,float)) and n>m:
                    return simplify(Pow(x1,n-m))

                case Pow(x1,n),Pow(x2,m) \
                    if x1==x2 and isinstance(n,(int,float)) and isinstance(m,(int,float)) and m>n:
                    return simplify(Div(1,Pow(x2,m-n)))

                case Pow(x1,n),Var(x2):
                    return simplify(Pow(x1,n-1))
                case _:
                    return Div(numerator,denominator)

        case Pow(base, exp):
            base = simplify(base)
            if exp == 0: return Const(1)
            if exp == 1: return base
            return Pow(base, exp)

        case _:
            return expr


expr=Add(
    Pow(Var('x'),Pow(Var('x'),2)),
    Mul(Const(2),Var('x'))
    )
print(show(simplify(expr)))
print(show(simplify(D(expr))))    
print(show(simplify(Div(Pow(Var('x'),3),Pow(Var('x'),4)))))