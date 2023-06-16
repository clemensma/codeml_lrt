from setuptools import setup, find_packages

setup(
    name='codeml_lrt',
    version='0.1.0',
    description='Perform likelihood ratio tests (LRT) on codeml output files for model selection.',
    author='Clemens Mauksch',
    author_email='clemens.mauksch@stud.uni-goettingen.de',
    url='https://github.com/yourusername/codeml_lrt',
    packages=find_packages(),
    install_requires=[
        'biopython'
    ],
    entry_points={
        'console_scripts': [
            'codeml-lrt=codeml_lrt.main:main',
        ],
    },
)
