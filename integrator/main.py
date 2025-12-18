from dataclasses import dataclass

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
class Mul(Expr):
    left: Expr
    right: Expr

@dataclass(frozen=True)
class Pow(Expr):
    base: Expr
    exp: int | float # should be expression later

expr=Add(
    Pow(Var('x'),2),
    Mul(Const(2),Var('x'))
    )

def D(expr:Expr):
    if isinstance(expr,Add):
        return Add(D(expr.left),D(expr.right))
    if isinstance(expr,Const):
        return Const(0)
    if isinstance(expr,Var):
        return Const(1)
    if isinstance(expr,Pow):
        return Mul(Const(expr.exp),Pow(expr.base,expr.exp-1))
    if isinstance(expr,Mul):
        return Add(Mul(expr.left,D(expr.right)),Mul(expr.right,D(expr.left)))
    else:
        pass


def show(expr: Expr):
    match expr:
        case Const(value)    : return str(value)
        case Mul(Const(value),right) : return f"{value}{show(right)}"
        case Mul(left,Const(value)) : return f"{value}{show(left)}"
        case Pow(Var(name),exp) : return f"{name}^{exp}"
        case Mul(left,right) : return f"({show(left)})*({show(right)})"
        case Pow(base,exp)   : return f"({show(base)})^{exp}"
        case Add(left,right) : return f"({show(left)} + {show(right)})"
        case Var(name)       : return name

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
            if a == Const(0) or b == Const(0): return Const(0)
            if a == Const(1): return b
            if b == Const(1): return a
            if isinstance(a, Const) and isinstance(b, Const):
                return Const(a.value * b.value)
            return Mul(a, b)

        case Pow(base, exp):
            base = simplify(base)
            if exp == 0: return Const(1)
            if exp == 1: return base
            return Pow(base, exp)

        case _:
            return expr



print(show(simplify(expr)))
print(show(simplify(D(expr))))    