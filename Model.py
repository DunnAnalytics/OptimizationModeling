"""
Created on Monday March 24 15:06:53 2025

@author: ashtondunn
"""
from pyomo.environ import *
model = AbstractModel()

# SETS
model.I = RangeSet(1,3)
model.J = RangeSet(1,5)
model.K = RangeSet(1,3)
model.T = RangeSet(1,2)

# PARAMETERS
model.p = Param(model.I, model.J, model.K, model.T)
model.pen = Param(model.I, model.J, model.T)
model.d = Param(model.J, model.T)
model.LT  = Param(model.I, model.K)
model.UT = Param(model.I, model.K)
model.LB = Param(model.I, model.T)
model.UB = Param(model.I, model.T)

# DECISION VARIABLES
model.x = Var(model.I, model.J, model.K, model.T, domain = NonNegativeReals)
model.y = Var(model.I, model.K, domain = Binary)

# OBJECTIVE
def objective(model):
    return sum(sum(sum(sum(model.x[i,j,k,t] * (model.p[i,j,k,t] + model.pen[i,j,t]) for i in model.I) for j in model.J) for k in model.K) for t in model.T)
model.objfn = Objective(rule = objective, sense = minimize)

# CONSTRAINTS
def lowcapcons(model, i, t):
    return sum(sum(model.x[i,j,k,t] for j in model.J) for k in model.K) >= model.LB[i,t]
model.lowcapsontr = Constraint(model.I, model.T, rule = lowcapcons)

def upcapcons(model, i, t):
    return sum(sum(model.x[i,j,k,t] for j in model.J) for k in model.K) <= model.UB[i,t]
model.upcapsontr = Constraint(model.I, model.T, rule = upcapcons)

def demcons(model, j, t):
    return sum(sum(model.x[i,j,k,t] for i in model.I) for k in model.K) >= model.d[j,t]
model.demconstr = Constraint(model.J, model.T, rule = demcons)

def lowcarthresh(model, i, k):
    return sum(sum(model.x[i,j,k,t] for j in model.J) for t in model.T) >= model.LT[i,k] * model.y[i,k]
model.lowcarthresh = Constraint(model.I, model.K, rule = lowcarthresh)

def upcarthresh(model, i, k):
    return sum(sum(model.x[i,j,k, t] for j in model.J) for t in model.T) <= model.UT[i,k] * model.y[i,k]
model.upcarthresh = Constraint(model.I, model.K, rule = upcarthresh)

def oneintcons(model, i):
    return sum( model.y[i,k] for k in model.K) <= 1
model.oneintconstr = Constraint(model.I, rule = oneintcons)
