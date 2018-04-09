#!/bin/bash
#SBATCH --partition=hort503-01-s18        ### Partition (like a queue in PBS)
#SBATCH –account=hort503-01-s18
#SBATCH --job-name=Assignment12      ### Job Name
#SBATCH --output=A12.out         ### File in which to store job output
#SBATCH --error=A12.err          ### File in which to store job error messages
#SBATCH --time=0-00:01:00       ### Wall clock time limit in Days-HH:MM:SS
#SBATCH --nodes=1               ### Node count required for the job
#SBATCH --ntasks-per-node=1     ### Number of tasks to be launched per Node
TAIR10_functional_descriptions.txt

results = re.sub('.*?(^AT\dG\d+\.\d+|IPR\d+|$).*?’r'\1,',text, 0, re.M)
results_io = StringIO(results)
df = pd.read_csv(results_io, sep=",", header=None)
df.columns = ['Transcript ID','IPR1', 'IPR2’, 'IPR3', 'IPR4', 'IPR5', 'IPR6', 'IPR7’]

annots = df.melt(id_vars = 'Transcript ID’, value_name='IPR Term')
annots = annots.drop('variable', axis=1)
annots = annots.dropna()
