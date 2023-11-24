# Linear Programming model of a hardcoded order 3 golomb ruler.

# Tasks for generalization:
# express the distance variables as an upper triangualar matrix?
reset;

param upper_bound = 10;
param order = 3;

set pairs = {i in 1..order, j in (i + 1)..order};
set v = {1..upper_bound};

var d {pairs} in v;
var e {pairs, v} binary;
