A Snakemake storage plugin that reads and writes from a locally mounted filesystem using rsync.
This is particularly useful when running Snakemake on an NFS as complex parallel IO patterns can slow down NFS quite substantially.
See "Further information" for an example configuration in such a scenario.
