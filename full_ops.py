# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
# Determines the output shape and oepration count of a fully-connected layer
# Parameters:
# c_in: input channel count
# n_wv: number of weight vectors
# Output:
# Produces output channel count, output height count, output weight count, number of additions performed, number of multiplications performed, and number of divisions performed
#
# Written by Celia Sterthous
# Other contributors: None
#
# See the LICENSE file for the license.
# import Python modules
import sys # argv

# parse script arguments
if len(sys.argv)==3:
    c_in = int(sys.argv[1])
    n_wv = int(sys.argv[2])
else:
 print(\
 'Usage: '\
 'python3 full_ops.py c_in n_wv'\
 )
 exit()
# write script below this line
c_out = n_wv
h_out = 1
w_out = 1
muls = n_wv*c_in
adds = muls
divs = 0

# Print the results
print(int(c_out))  # output channel count
print(int(h_out))  # output height count
print(int(w_out))  # output width count
print(int(adds))   # number of additions performed
print(int(muls))   # number of multiplications performed
print(int(divs))   # number of divisions performed
