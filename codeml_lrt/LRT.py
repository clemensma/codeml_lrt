from scipy.stats import chi2

def likelihood_ratio_test(ln_likelihood_null, ln_likelihood_alternate, df_null, df_alternate):
    """
    Perform a likelihood ratio test

    Args:
        ln_likelihood_null: natural log of the likelihood of the null model
        ln_likelihood_alternate: natural log of the likelihood of the alternate model
        df_null: degrees of freedom of the null model
        df_alternate: degrees of freedom of the alternate model

    Returns:
        p-value of the test
    """
    
    D = -2*(ln_likelihood_null - ln_likelihood_alternate)
    df = df_alternate - df_null
    
    p_value = chi2.sf(D, df) # sf is survival function, which is 1 - cdf
    return p_value



def main():
    # example usage
    ln_likelihood_null = -150
    ln_likelihood_alternate = -100
    df_null = 5
    df_alternate = 8

    p_value = likelihood_ratio_test(ln_likelihood_null, ln_likelihood_alternate, df_null, df_alternate)
    print('p-value:', p_value)
    return 0

if __name__ == '__main__':
    main()