import random
from argparse import ArgumentParser


parser = ArgumentParser(description="Simulate coin flips and optionally show statistics.")


parser.add_argument("-v", "--verbose", action="store_true", default=False,
                    help="show result of all coin flips, even if stats=True")

parser.add_argument("-n", "--num-flips", type=int, default=1,
                    help="specify the number of coin flips [default %(default)s]")
parser.add_argument("-s", "--stats", action="store_true", default=False,
                    help="compute and show stats")
args = parser.parse_args()


if args.num_flips < 1:
  print(f"Expected a positive number of flips, not {args.num_flips}")
  exit(1)

total = 0
for _ in range(args.num_flips):
  flip = random.randint(0, 1)
  total += flip
  if args.verbose or not args.stats:
    print('H' if flip else 'T')
if args.stats:
  print(f"Results: {total} heads, {args.num_flips-total} tails. "
        f"({total/args.num_flips*100:.2f}% heads)") 