import os
import pandas as pd


FILE = "telemetry.csv"


def save(data):

    df = pd.DataFrame([data])

    if os.path.exists(FILE):

        df.to_csv(
            FILE,
            mode="a",
            index=False,
            header=False
        )

    else:

        df.to_csv(
            FILE,
            index=False
        )