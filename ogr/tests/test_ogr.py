from .. import *

import pytest


def test_enumeration():
    rlr = generate_golomb_ruler_improved(10)
    r = GolombRuler(rlr, assert_golomb_property=True)
    print(f"Golomb ruler with length: {r.length()} order: {r.order()}")
    print(r)
