# # GARNER lib
#     x_p = exp_modulara_lib(y % p, d % (p - 1), p)
#     x_q = exp_modulara_lib(y % q, d % (q - 1), q)
#     x_r = exp_modulara_lib(y % r, d % (r - 1), r)

#     x1 = x_p
#     alpha = ((x_q - x1) * exp_modulara_lib(p, -1, x_r)) % x_r
#     x2 = x1 + alpha * p
#     alpha = ((x_q - x2) * exp_modulara_lib(p * r, -1, x_q)) % x_q
#     x_lib = x2 + alpha * p * q

# # Timpul de finish