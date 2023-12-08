The following Snakemake CLI flags allow to avoid harmful IO patterns on shared network filesystems by instructing Snakemake
to copy any input to a fast local scatch disk and copying output files back to the network filesystem at the end of a job.

```bash
snakemake --default-storage-provider fs --shared-fs-usage persistence software-deployment sources source-cache --local-storage-prefix /local/work/$USER
```

with `/local/work/$USER` being the path to the local (non-shared) scratch dir.
Alternatively, these options can be persisted in a profile:

```yaml
default-storage-provider: fs
local-storage-prefix: /local/work/$USER
shared-fs-usage:
  - persistence
  - software-deployment
  - sources
  - source-cache
```