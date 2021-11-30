# Novel PETase Discovery on Metagenomic Datasets

Pipeline imitates the workflow in a [scientific paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5881046/) (Danso et.al.) which downloads generates a Hidden Markov Model from known 9 PETases and searchs databases with this Hidden Markov Model to discover novel PETases.

In this snakemake pipeline we built a HMM with same 9 molecules and search only 1 metagenomic dataset(not in the repo check Dataset section).

This search results in 2 proteins under our threshold constraints(hmmsearch score > 150). Then we generate a phylogenetic tree with those 2 and 9 known PETases.

### Dependencies
- python (tested with 3.10.0)
- snakemake (tested with 6.12.1)
- conda 
- Other dependencies that will be automatically downloaded by snakemake:
  - tcoffee
  - hmmer
  - fasttree  

We suggest you to downlaod `snakemake` with `conda`
```conda install -n base -c conda-forge mamba```
