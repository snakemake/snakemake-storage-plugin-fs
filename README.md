# snakemake-storage-plugin-fs

A Snakemake storage plugin that reads and writes from a locally mounted filesystem using rsync.
This is particularly useful when running Snakemake on an NFS.
Complex parallel IO patterns can slow down NFS quite substantially.
The following Snakemake CLI flags allow to avoid such patterns by instructing Snakemake
to copy any input to a fast local scatch disk and copying output files back to NFS at the end of a job.

```bash
snakemake --default-storage-provider fs --no-shared-fs --local-storage-prefix /local/work/$USER
```

with `/local/work/$USER` being the path to the local (non NFS) scratch dir.
Alternatively, these options can be persisted in a profile:

```yaml
default-storage-provider: fs
no-shared-fs: true
local-storage-prefix: /local/work/$USER
```