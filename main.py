import scipy.stats as stats

def expected_value_single_ticket(mean, std_dev):

    # Probabilities
    p_below_1 = stats.norm.cdf(1, mean, std_dev)
    p_between_1_100 = stats.norm.cdf(100, mean, std_dev) - p_below_1
    p_above_100 = 1 - stats.norm.cdf(100, mean, std_dev)
    # Expected values for each segment
    ev_below_1 = p_below_1 * 1
    ev_between_1_100 = p_between_1_100 * stats.norm.expect(lambda x: x, 
                                                           loc=mean, scale=std_dev, 
                                                           lb=1, ub=100)

    ev_above_100 = p_above_100 * (mean + 20 + std_dev)
    
    return ev_below_1 + ev_between_1_100 + ev_above_100

def expected_value_two_tickets(mean, std_dev):
    # Probabilities
    p_below_1 = stats.norm.cdf(1, mean, std_dev)
    p_between_1_100 = stats.norm.cdf(100, mean, std_dev) - p_below_1
    p_above_100 = 1 - stats.norm.cdf(100, mean, std_dev)
    
    # Expected value for the range $1 to $100
    ev_between_1_100 = stats.norm.expect(lambda x: x, loc=mean, scale=std_dev, lb=1, ub=100)

    # Expected value for above $100
    ev_above_100 = stats.norm.expect(lambda x: x + 20, loc=mean, scale=std_dev, lb=100)

    # Expected values for each combination
    ev_both_below_1 = p_below_1**2 * 1
    ev_one_below_1 = 2 * p_below_1 * p_between_1_100 * ev_between_1_100
    ev_one_below_one_above = 2 * p_below_1 * p_above_100 * ev_above_100
    ev_both_between = p_between_1_100**2 * ev_between_1_100
    ev_one_between_one_above = 2 * p_between_1_100 * p_above_100 * ev_above_100
    ev_both_above = p_above_100**2 * ev_above_100
    
    return (ev_both_below_1 + ev_one_below_1 + ev_one_below_one_above + 
            ev_both_between + ev_one_between_one_above + ev_both_above)
    
    return (ev_both_below_1 + ev_one_below_1 + ev_one_above_100 + 
            ev_both_between + ev_one_between_one_above + ev_both_above)

#50 for mean and 50 for std_dev
ev_single = expected_value_single_ticket(50, 50)
ev_double = expected_value_two_tickets(50, 50)

print(f"Expected Value of a Single Ticket: ${ev_single:.2f}")
print(f"Expected Value of Two Tickets: ${ev_double:.2f}")
