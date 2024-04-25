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

If the shared scratch is e.g. specific for each job (e.g. controlled by a ``$JOBID``), one can define a job-specific local storage prefix like this

```yaml
default-storage-provider: fs
local-storage-prefix: /local/work/$USER
remote-job-local-storage-prefix: /local/work/$USER/$JOBID
shared-fs-usage:
  - persistence
  - software-deployment
  - sources
  - source-cache
```

Note that the non-remote job local storage prefix is still always needed, because Snakemake can also decide to run certain jobs without submission to the cluster or cloud.
This can happen either on dev request because a certain rule is very lightweight, or by Snakemake's own decision, e.g. in case of rules that just format a template (see `docs <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#template-rendering-integration>`_).