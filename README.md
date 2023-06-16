# Codeml Likelihood Ratio Test (LRT) Tool

This command-line tool performs a likelihood ratio test (LRT) for results from PAML's `codeml` program, assisting in model selection. 

## Requirements

- Python 3.6 or above
- Biopython

To install the Python dependencies, you can use pip:

```shell
pip install biopython
```

## Usage

```shell
python LRT_for_codeml.py --H0_dir /path/to/null_model_results --H1_dir /path/to/alternative_model_results
```

This will perform a likelihood ratio test comparing the results in the `H0_dir` directory (representing the null model) and the `H1_dir` directory (representing the alternative model). The tool will print a summary of the test, including the p-value and whether the null model can be rejected at the 0.05 significance level.

## Directory Structure

For the tool to work correctly, results from `codeml` should be organized in directories as follows:

- Each directory should contain one `codeml.ctl` control file and one results file.
- The directory name should match the name of the results file, without the `_out.paml` extension. For example, if your results file is named `model1_out.paml`, the containing directory should be named `model1`.

For example, a valid directory could look like this:

```
model1/
    codeml.ctl
    model1_out.paml
```

## Troubleshooting

If you encounter any issues with this tool, please open an issue on this GitHub repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
