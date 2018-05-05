#!/usr/bin/env nextflow
//Total sequences = 66338 (Based on ###grep -c ">" filename###).
//Divide each file into 6634 sequences
//module use /data/ficklin/modulefiles
//module add java nextflow

divnum = params.divideby
params.inf = '/data/hort503_01_s18/example-data/all.pep' 
params.db = '/data/hort503_01_s18/example-data/swissprot'
params.publish = '/data/hort503_01_s18/zara.york/BlastOut/'

SplitFiles = Channel
  .fromPath(params.inf)
  .splitFasta(by: divnum, file: true)

process BLAST {
  module 'blast'
  cpus 8
  queue 'hort503-01-s18'
  executor 'slurm'
  publishDir params.publish, mode: 'copy'
  input:
  file SplitFP from SplitFiles

  output:
  file '*.blastp.out' into blastFiles
  """
  outfile=`echo -n $SplitFP | perl -p -e 's/^.*\\/(.*)\$/\\1/'`
  blastp -num_threads 8 -query $SplitFP -db $params.db -out \${outfile}.blastp.out -outfmt 6
  """
}

