#!/usr/bin/env python3


def main(data: str) -> int:
    total_area = 0
    for line in data.splitlines():
        l, w, h = list(map(int, line.split("x")))

        side_areas = l * w, w * h, l * h
        total_area += 2 * sum(side_areas) + min(side_areas)

    return total_area


if __name__ == "__main__":
    from aocd import data, submit

    # data = "2x3x4\n1x1x10"
    ans = main(data)

    print(f"ANSWER = {ans}")
    submit(ans)
