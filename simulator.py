import random


def generate_data():

    return {

        "temperature":
        round(
            random.uniform(
                22,
                35
            ),
            1
        ),

        "acceleration":
        round(
            random.uniform(
                1,
                10
            ),
            1
        ),

        "altitude":
        round(
            random.uniform(
                80,
                110
            ),
            1
        ),

        "source":
        "SIMULATION"
    }