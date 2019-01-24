def load():
    """name of dataset: rental
    no of variables: 23
    no of observations: 128

    +----------+--------------------------------+
    | variable | label                          |
    +----------+--------------------------------+
    | city     | city label, 1 to 64            |
    | year     | 80 or 90                       |
    | pop      | city population                |
    | enroll   | # college students enrolled    |
    | rent     | average rent                   |
    | rnthsg   | renter occupied units          |
    | tothsg   | occupied housing units         |
    | avginc   | per capita income              |
    | lenroll  | log(enroll)                    |
    | lpop     | log(pop)                       |
    | lrent    | log(rent)                      |
    | ltothsg  | log(tothsg)                    |
    | lrnthsg  | log(rnthsg)                    |
    | lavginc  | log(avginc)                    |
    | clenroll | change in lrent from 80 to 90  |
    | clpop    | change in lpop                 |
    | clrent   | change in lrent                |
    | cltothsg | change in ltothsg              |
    | clrnthsg | change in lrnthsg              |
    | clavginc | change in lavginc              |
    | pctstu   | percent of population students |
    | cpctstu  | change in pctstu               |
    | y90      | =1 if year == 90               |
    +----------+--------------------------------+

    David Harvey, a former MSU undergraduate, collected the data for 64
    “college towns” from the 1980 and 1990 United States censuses."""

    import wooldridge
    return wooldridge.load(__file__, "rental.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()