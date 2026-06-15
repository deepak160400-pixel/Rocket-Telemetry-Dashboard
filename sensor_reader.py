import serial
import serial.tools.list_ports
import time


ports=list(
serial.tools.list_ports.comports()
)

print("\nAvailable Ports:\n")

for p in ports:
    print(
        p.device,
        p.description
    )


port=input(
"\nEnter COM: "
)


ser=serial.Serial(
port,
115200,
timeout=1
)

time.sleep(2)

print("\nCONNECTED\n")


while True:

    line=(
        ser.readline()
        .decode(
            errors="ignore"
        )
        .strip()
    )

    if line:

        print(
            line
        )