import math

def ind_t_test_2tail(x, x2, nx, y, y2, ny):

   #this function runs an independent groups 2-tailed t-test with an alpha of 0.05
   #the function works for values of nx and ny (sample sizes) between 2 and 10
   #x is the sum of x values and x2 is the sum of x-squared values; the same for y and y2; enter all values as floats

   #this section defines the null hypothesis
    nullhyp = 0

   #this section calculates degrees of freedom and the critical t-value
    df = (nx - 1) + (ny - 1)
    if df == 2:
        tcrit = 4.303
    elif df == 4:
        tcrit = 2.776
    elif df == 6:
        tcrit = 2.447
    elif df == 8:
        tcrit = 2.306
    elif df == 10:
        tcrit = 2.228
    elif df == 12:
        tcrit = 2.179
    elif df == 14:
        tcrit = 2.145
    elif df == 16:
        tcrit = 2.120
    elif df == 18:
        tcrit = 2.101
    elif df < 2 or df > 18 or df % 2 != 0:
        print "You have entered an invalid value or values for sample size."
        return

   #this section calculates the means of x and y
    mx = x / nx
    my = y / ny

   #this section calculates the sum of squares for x and y
    ssx = x2 - ((x ** 2) / nx)
    ssy = y2 - ((y ** 2) / ny)

   #this section calculates the standard error of the difference between x and y
    sxy = math.sqrt(((ssx + ssy) / ((nx - 1) + (ny - 1))) * ((1 / nx) + (1 / ny)))

   #this section calculates the t-value
    tcalc = (mx - my - nullhyp) / sxy

   #this section calculates the s pooled value for Cohen's d
    spooled = math.sqrt((ssx + ssy) / (nx - 1) + (ny - 1))

   #this section calculates Cohen's d
    d = (mx - my) / spooled

   #this section compares the calculated t-value to the critical t-value and prints the result
    if abs(tcalc) > tcrit:
        print "There is a significant difference in the performance of the two groups (t", \
            int(df), "=", ("%.2f" % tcalc), ", p > 0.05, d =", ("%.2f" % d), ")."
    else:
        print "There is not a significant difference in the performance of the two groups (t", \
               int(df), "=", ("%.2f" % tcalc), ", p > 0.05, d =", ("%.2f" % d), ")."

   #this section evaluates Cohen's d and prints the result
    if abs(d) <= 0.2:
        print '''This is a small effect size, meaning it is not important. \
The difference between the group means is''', ("%.2f" % d), 'standard deviations.'
    elif 0.2 < abs(d) < 0.8:
        print '''This is a moderate effect size, meaning it is somewhat important. \
The difference between the group means is''', ("%.2f" % d),'standard deviations.'
    elif abs(d) >= 0.8:
        print '''This is a large effect size, meaning it is important. \
The difference between the group means is''', ("%.2f" % d), 'standard deviations.'

ind_t_test_2tail(27.0, 147.0, 5.0, 13.0, 45.0, 5.0)