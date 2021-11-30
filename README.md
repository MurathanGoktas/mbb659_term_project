# Novel PETase Discovery on Metagenomic Datasets

Pipeline imitates the workflow in a [scientific paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5881046/) (Danso et.al.) which generates a Hidden Markov Model from known 9 PETases and searchs databases with this Hidden Markov Model to discover novel PETases.

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

### Dataset
There are two types of data in this pipeline. 
- Known PETases
- Metagenomic datasets

Known PETases are automatically downloaded by pipeline by their Uniprot entry keys identified in `config/config.json`.
Metagenomic datasets in this study cannot be downloaded by APIs. Thus users are excepted to download those metagenomic datasets manually and move to `data/metagenomic_datasets/` folder and fill the necessary parts in `config/config.json`. The metagenomic dataset used in this study is [here](https://img.jgi.doe.gov/cgi-bin/m/main.cgi?section=TaxonDetail&page=taxonDetail&taxon_oid=2140918008). Moving `2140918008.a.faa` file into `data/metagenomic_datasets/` and filling `config/config.json` would be sufficient to reproduce results.


