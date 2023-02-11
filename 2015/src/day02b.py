#!/usr/bin/env python3


def main(data: str) -> int:
    total_ribbon = 0
    for line in data.splitlines():
        l, w, h = list(map(int, line.split("x")))

        perimeter_lengths = l + l + w + w, l + l + h + h, w + w + h + h
        volume = l * w * h
        minimum_perimeter = min(perimeter_lengths)
        print(minimum_perimeter, volume)
        total_ribbon += minimum_perimeter + volume

    return total_ribbon


if __name__ == "__main__":
    from aocd import data, submit

    # data = "2x3x4\n1x1x10"
    ans = main(data)

    print(f"ANSWER = {ans}")
    submit(ans)
