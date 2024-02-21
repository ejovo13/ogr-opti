import ogr
import polars
import altair as alt

def solve():
    """Test solving suite for Optimal Golomb Rulers."""

    max_order = 7

    for order in range(2, max_order):

        ruler = ogr.solve(order, verbose = True)
        print()


def generate_rulers():

    # Start off using a naive method
    max_order = 20

    naive_rulers = [ogr.GolombRuler(ogr.generate_golomb_ruler_naive(order)) for order in range(1, max_order + 1)]
    naive_orders = [ruler.order() for ruler in naive_rulers]
    naive_lengths = [ruler.length() for ruler in naive_rulers]

    improved_rulers = [ogr.GolombRuler(ogr.generate_golomb_ruler_improved(order)) for order in range(1, max_order + 1)]
    improved_orders = [ruler.order() for ruler in improved_rulers]
    improved_lengths = [ruler.length() for ruler in improved_rulers]

    print(f"Naive generation:")
    print(naive_rulers[-1])

    print(f"Improved generation:")
    print(improved_rulers[-1])



    df_naive = polars.DataFrame(dict(order=naive_orders, length=naive_lengths))
    df_improved = polars.DataFrame(dict(order=improved_orders, length=improved_lengths))

    # Now let's compare our naive method with
    print(df_naive)

    print(df_improved)

    print(df_improved["length"])
    # chart = alt.Chart(df_naive).mark_point().encode(
    #     x="order",
    #     y="length"
    # )

