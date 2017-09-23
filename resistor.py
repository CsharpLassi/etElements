#!/usr/bin/python3

import argparse


def main():
    parser = argparse.ArgumentParser(description="etElements Resistor")

    parser.add_argument('-v', dest='voltage', help='Resistor Voltage', type=float)
    parser.add_argument('-r', dest='value', help='Resistor Value', type=float)
    parser.add_argument('-i', dest='current', help='Resistor Current', type=float)
    parser.add_argument('-d', default=0.1, dest='diff', help='Validation Range', type=float)

    result = parser.parse_args()
    if result.voltage and result.value and result.current:
        calcValue = result.voltage / result.current
        print(abs(calcValue - result.value) < result.diff)
    elif result.voltage and result.value:
        print(result.voltage/result.value)
    elif result.value and result.current:
        print(result.value * result.current)
    elif result.voltage and result.current:
        print(result.voltage / result.current)
    else:
        parser.parse_args(['--help'])


if __name__ == '__main__':
    main();
