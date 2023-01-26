import sys
import math

x = int(sys.argv[1])
y = int(sys.argv[2])
t = float(sys.argv[3])
delta_x = int(sys.argv[4])

# we represent the natural log function as ln(x) for ease
def ln(x):
  return math.log(x)

print("\nMake sure that your arguments are in the order quantity of X, quantity of Y, t,
      delta x (or delta y)")

delta_y = t*y * ( ln( 1/(x + delta_x) + t/y) - ln( 1/x + t/y ) ) \
-(y/t)*( ln(1 + (t/y) * (x + delta_x) ) - ln( 1 + (t/y) * x ) )

print(delta_y)
