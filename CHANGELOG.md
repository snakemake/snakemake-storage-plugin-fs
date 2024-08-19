# Changelog

## [1.0.6](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v1.0.5...v1.0.6) (2024-08-16)


### Bug Fixes

* clean up target path upon storage in order to avoid merges of directories ([#25](https://github.com/snakemake/snakemake-storage-plugin-fs/issues/25)) ([5a9bd27](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/5a9bd27a40377b0cadfc51fd576ae98c9ee06668))

## [1.0.5](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v1.0.4...v1.0.5) (2024-07-04)


### Bug Fixes

* fix touch and retrieval of mtime for directories ([#20](https://github.com/snakemake/snakemake-storage-plugin-fs/issues/20)) ([898d367](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/898d367ddff01282ab0808a66e7d5fe086272b2e))

## [1.0.4](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v1.0.3...v1.0.4) (2024-04-25)


### Bug Fixes

* inherit ownership and permissions from "remote"/destination dir ([289a739](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/289a73974b60cf5b6d02c1bc50894e7bc8521478))

## [1.0.3](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v1.0.2...v1.0.3) (2024-04-17)


### Bug Fixes

* fix query validation (used deprecated API) ([9bbeaaa](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/9bbeaaa302683fc08b15c27f1de5b4ab4492f2aa))

## [1.0.2](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v1.0.1...v1.0.2) (2024-04-16)


### Miscellaneous Chores

* release 1.0.2 ([173ce62](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/173ce62626d49f17fb99fc94519ec981339ffc1e))

## [1.0.1](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v1.0.0...v1.0.1) (2024-04-16)


### Bug Fixes

* do not consider URL-like queries as valid ([bb0cd39](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/bb0cd390ac288600f61ed4fb7236b8dc2bfdbc03))

## [1.0.0](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v0.2.0...v1.0.0) (2024-02-24)


### ⚠ BREAKING CHANGES

* remove latency wait support as this should rather be handled in main Snakemake (as it is already done). The reason is that the plugin cannot distinguish between cases where latency has to be taken into accound and where not, leading to overall much slower processing when latency wait is applied regardless of the context. This introduces a breaking change because this plugin now does not offer any settings anymore. ([#13](https://github.com/snakemake/snakemake-storage-plugin-fs/issues/13))

### Bug Fixes

* remove latency wait support as this should rather be handled in main Snakemake (as it is already done). The reason is that the plugin cannot distinguish between cases where latency has to be taken into accound and where not, leading to overall much slower processing when latency wait is applied regardless of the context. This introduces a breaking change because this plugin now does not offer any settings anymore. ([#13](https://github.com/snakemake/snakemake-storage-plugin-fs/issues/13)) ([1c78d88](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/1c78d880925ad1af08195d4035028a9117755551))
* respect permissions of the target dir, especially setgid ([#11](https://github.com/snakemake/snakemake-storage-plugin-fs/issues/11)) ([2132a5a](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/2132a5a845f865fd076235620f8e2a91a2300206))

## [0.2.0](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v0.1.5...v0.2.0) (2024-02-19)


### Features

* add touch support ([#9](https://github.com/snakemake/snakemake-storage-plugin-fs/issues/9)) ([7ed5a6a](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/7ed5a6a5a6d4208124f946ae9269e72ab0d9e509))
* provide setting for latency wait ([#8](https://github.com/snakemake/snakemake-storage-plugin-fs/issues/8)) ([9ac5c8d](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/9ac5c8ddc89d6a35c36dc991bdc24f1965f42a16))

## [0.1.5](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v0.1.4...v0.1.5) (2023-12-20)


### Documentation

* add license to metadata ([ac8cc98](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/ac8cc9893590f59d45d2f9b3bbd1660dd5f9fd55))
* update metadata ([9a66b33](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/9a66b3341fdbd58aa1211da2f8f0de0cd0057b4c))

## [0.1.4](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v0.1.3...v0.1.4) (2023-12-08)


### Documentation

* refactor docs ([aeeee93](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/aeeee9331ae1910e8c4d0a1d76d835043fbfb9f5))

## [0.1.3](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v0.1.2...v0.1.3) (2023-12-05)


### Bug Fixes

* adapt to interface change ([6b1bee0](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/6b1bee0174f8157a85751fe4ce405890168f474e))

## [0.1.2](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v0.1.1...v0.1.2) (2023-11-20)


### Bug Fixes

* create directory if not yet existing ([e8d959f](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/e8d959faeea27face12dcb785679cfc7fa45595d))
* fix inventory ([25e56ba](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/25e56ba4b4b5edf44c7838915b3b6ea6f2c95bb8))

## [0.1.1](https://github.com/snakemake/snakemake-storage-plugin-fs/compare/v0.1.0...v0.1.1) (2023-11-17)


### Bug Fixes

* fixed query validation ([04aba41](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/04aba41f4ec858cae4692de3eb8f36077a7ee4f7))

## 0.1.0 (2023-11-15)


### Bug Fixes

* adapt to interface changes, fix implementation ([7883f07](https://github.com/snakemake/snakemake-storage-plugin-fs/commit/7883f078edc4a441c317a14cf0cc63499e2af9b3))
