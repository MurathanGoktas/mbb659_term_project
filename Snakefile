configfile: "config/config.json"

rule download_known_PETases:
    input:
        "config/config.json"
    output:
        "data/known_PETases.fa"
    shell:
        "./helper_scripts/download_known_PETases.py {input} {output}"

rule msa_known_PETases:
    input:
        "data/known_PETases.fa"
    output:
        "data/known_PETases.aln"
    conda:
        "envs/t_coffee.yaml"
    shell:
        "t_coffee {input} -outfile={output}"

rule build_HMM_from_known_PETases:
    input:
        "data/converted_known_PETases.aln"
    output:
        "data/known_PETases.hmm"
    conda:
        "envs/hmmer.yaml"
    shell:
        "hmmbuild {output} {input}"

rule convert_clustal_format:
    input:
        "data/known_PETases.aln"
    output:
        "data/converted_known_PETases.aln"
    shell:
        "sed -i.bak '1 s/.*/CLUSTAL 2.1 multiple sequence alignment/' {input} && mv {input} {output}"

rule run_HMM_search_from_known_PETases:
    input:
        "data/known_PETases.hmm", 
        "data/metagenomic_datasets/{metagenomic_dataset}"
    output:
        "data/{metagenomic_dataset}_hmmersearch.out.fa"
    conda:
        "envs/hmmer.yaml"
    shell:
        "./helper_scripts/run_hmm_search_iteratively.py ./config/config.json"

rule merge_all_PETases:
    input:
        expand("data/{metagenomic_dataset}_hmmersearch.out.fa", metagenomic_dataset=config["metagenomic_datasetss"]), 
        "data/known_PETases.fa"
    output:
        "data/merged_PETases.fa"
    shell:
        "cat {input} >> {output}"

rule msa_merged_PETases:
    input:
        "data/merged_PETases.fa"
    output:
        "data/merged_PETases.aln"
    conda:
        "envs/t_coffee.yaml"
    shell:
        "t_coffee {input} -outfile={output}"
	" && sed -i.bak '1 s/.*/CLUSTAL 2.1 multiple sequence alignment/' {output}"

rule convert_msa_merged_PETases:
    input:
        "data/merged_PETases.aln"
    output:
        "data/merged_PETases.aln.fa"
    conda:
	"envs/biopython.yaml"
    shell:
        "helper_scripts/clustal_to_fasta.py {output}"

rule generate_phylogenetic_tree:
    input:
        "data/merged_PETases.aln.fa"
    output:
        "data/pyhylogenetic_tree_PETases.tree"
    conda:
        "envs/fasttree.yaml"
    shell:
        "fasttree {input} > {output}"