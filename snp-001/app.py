#!/usr/bin/env python3

from pathlib import Path

OUTPUT = Path("../numbers/nums.txt")
PER_TIER = 1000
GRAHAM = "G"

OUTPUT.parent.mkdir(parents=True, exist_ok=True)


def snp_name(tier, index):
    return f"SNP-{tier}-{index:04d}"


def make_number(previous):
    return f"3 ↑^({previous}) 3"


def generate(tiers):
    lines = [
        "SNP — Study of Numbers & Programming",
        "",
        "G = Graham's number",
        ""
    ]

    seed = GRAHAM

    for tier in range(tiers):
        lines.append(f"===== TIER {tier} =====")
        lines.append("")

        previous = seed

        for i in range(1, PER_TIER + 1):
            name = snp_name(tier, i)
            value = make_number(previous)

            lines.append(f"{name} = {value}")

            previous = name

        seed = snp_name(tier, 1000)

        lines.append("")
        lines.append(
            f"{seed} becomes the seed for Tier {tier + 1}"
        )
        lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {tiers * 1000:,} SNP numbers to:")
    print(OUTPUT)


def main():
    print("SNP Number Generator")

    try:
        tiers = int(input("How many 1,000-number tiers? "))
    except ValueError:
        print("Enter a number.")
        return

    generate(tiers)


if __name__ == "__main__":
    main()