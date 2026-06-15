import serial
import serial.tools.list_ports


def detect():

    ports=(
        serial.tools
        .list_ports
        .comports()
    )

    for p in ports:

        if (
            "CH340"
            in
            p.description
        ):

            return p.device

    return None


PORT=detect()



def get_sensor():

    if PORT is None:

        return None

    try:

        ser=serial.Serial(
            PORT,
            115200,
            timeout=1
        )

        while True:

            line=(
                ser.readline()
                .decode(
                    errors="ignore"
                )
                .strip()
            )

            if (
                "X:"
                in
                line
            ):

                values=(
                    line
                    .replace(
                        ":",
                        ""
                    )
                    .split()
                )

                x=float(
                    values[1]
                )

                y=float(
                    values[3]
                )

                z=float(
                    values[5]
                )

                return {

                    "temperature":25,

                    "acceleration":
                    round(
                        abs(x)
                        +
                        abs(y),
                        1
                    ),

                    "altitude":
                    round(
                        z*10,
                        1
                    ),

                    "source":
                    "LIVE SENSOR"
                }

    except:

        return None