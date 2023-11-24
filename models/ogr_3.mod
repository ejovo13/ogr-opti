# Linear Programming model of a hardcoded order 3 golomb ruler.

# Tasks for generalization:
# express the distance variables as an upper triangualar matrix?
reset;

option solver cplex;

param upper_bound = 10;
param order = 3;

set pairs = {i in 1..order, j in (i + 1)..order};
set V = {1..upper_bound};

var d {pairs} in V;
var e {pairs, V} binary;

minimize total_length: sum{i in 1..order - 1} d[i, i + 1];
subject to distance_assignment {(i, j) in pairs}:
    sum{v in V} e[i, j, v] = 1;
subject to distance_uniqueness {v in V}:
    sum {(i, j) in pairs} e[i, j, v] <= 1;
