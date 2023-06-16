import argparse
import os
from Bio.Phylo.PAML import codeml
from .LRT import likelihood_ratio_test

# Mapping the number of site classes to their degrees of freedom
DF_PER_NSITES = {0: 1, 1: 2, 2: 4, 7: 2, 8: 4}

# Mapping the number of site classes to their model names
NSITES_TO_MODELS = {0: 'M0', 1: 'M1a', 2: 'M2a', 7: 'M7', 8: 'M8'}

def read_control_file(directory):
    """
    Function to read the results file of a codeml run and extract the model name, degrees of freedom and log-likelihood.

    Args:
        directory: The directory containing the codeml control file and the output file.

    Returns:
        model: Name of the model.
        df: Degrees of freedom of the model.
        lnL: Log-likelihood of the model.
    """
    # Initialize Codeml object
    cml = codeml.Codeml()

    # Read control file
    cml.read_ctl_file(os.path.join(directory, 'codeml.ctl'))

    # Get the model and degrees of freedom based on the NSsites parameter
    df = DF_PER_NSITES[cml.get_option('NSsites')[0]]
    model = NSITES_TO_MODELS[cml.get_option('NSsites')[0]]

    # Read the output file and get the log-likelihood
    results = codeml.read(directory + '/' + os.path.basename(directory) + '_out.paml')
    lnL = results['NSsites'][list(results['NSsites'].keys())[0]]['lnL']

    return model, df, lnL

def parse_arguments():
    """
    Function to parse command line arguments.

    Returns:
        args: A namespace containing the arguments provided.
    """
    parser = argparse.ArgumentParser(description='Perform a likelihood ratio test')
    parser.add_argument('-0', '--H0_dir', type=str, help='Directory containing H0 model results', required=True)
    parser.add_argument('-1', '--H1_dir', type=str, help='Directory containing H1 model results', required=True)
    return parser.parse_args()

def LRT_for_codeml(H0_dir, H1_dir):
    """
    Function to perform the likelihood ratio test for two directories containing codeml output.

    Args:
        H0_dir: The directory containing the null model results.
        H1_dir: The directory containing the alternate model results.

    Returns:
        p_value: The p-value of the likelihood ratio test.
    """
    # Read null model data
    _, df_null, lnL_null = read_control_file(H0_dir)
    
    # Read alternate model data
    _, df_alternate, lnL_alternate = read_control_file(H1_dir)
    
    # Perform likelihood ratio test
    p_value = likelihood_ratio_test(lnL_null, lnL_alternate, df_null, df_alternate)
    
    return p_value

def main():
    """
    Main function to execute the LRT test and print the results.

    Args:
        args: A namespace containing the directories for H0 and H1 models.
    """

    args = parse_arguments()

    # Read null model data
    model_H0, df_H0, lnL_H0 = read_control_file(args.H0_dir)

    # Read alternate model data
    model_H1, df_H1, lnL_H1 = read_control_file(args.H1_dir)

    # Perform likelihood ratio test
    p_value = likelihood_ratio_test(lnL_H0, lnL_H1, df_H0, df_H1)

    print("Model comparison summary:")
    print(f"Null model (H0): {model_H0}")
    print(f"Degrees of freedom: {df_H0}")
    print(f"log-likelihood: {lnL_H0}")
    print()
    print(f"Alternate model (H1): {model_H1}")
    print(f"Degrees of freedom: {df_H1}")
    print(f"log-likelihood: {lnL_H1}")
    print()
    print(f"p-value of the chi-squared survival-function test: {p_value}")
    print()
    # Interpretation of the p-value
    if p_value < 0.05:
        print("The null model can be rejected at the 0.05 significance level.")
    else:
        print("The null model cannot be rejected at the 0.05 significance level.")


if __name__ == '__main__':
    """
    Entry point of the script.
    Calls the main function.
    """
    main()
