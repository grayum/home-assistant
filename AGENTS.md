# Instructions for coding assistants

## Scope

This repository contains public Home Assistant and ESPHome examples. Read the relevant project README, datapoint notes, test record and TODO before changing a device configuration. Keep changes small and reviewable. Explain behavior changes and preserve existing entity names and secret names unless a migration is documented.

## Privacy and publication

- Never commit actual credentials, API keys, private addresses, household details, private logs, firmware images or flash backups. Use `!secret` and explicit example values.
- The supplied public configuration, two approved device photographs, Paul-contributed TYWE1S flashing notes and approved pinout image may be published. Do not add the manufacturer PDF or extracted manual pages. Link to the manufacturer instead.
- Never assume `.gitignore` removes already tracked secrets. Inspect the staged diff and filenames before a commit.
- Do not embed a remote GitHub package dependency, telemetry or a cloud service into a working local configuration without an explicit request.

## Hardware evidence and heater behavior

- Distinguish maintainer observations, manufacturer descriptions and new contributor measurements. Never fabricate logs or mark untested variants as supported.
- Preserve the existing datapoint IDs, enum values, board and UART pins unless a proposed change includes evidence for that hardware revision.
- Do not invent connector pinouts, electrical isolation, voltage levels, module identities or flashing/backup procedures. GPIO assignments in YAML do not establish connector order.
- M mode is manual heat control; setting a target temperature does not make M mode thermostatic. Do not describe it otherwise.
- DP101 is shared by the climate component and a writable select. Account for the climate component writing it on Heat commands. Document and test changes to this interaction.
- Do not add automatic heating on boot, reconnect or time synchronization. Do not bypass safety mechanisms or create artificial fault conditions to test protections.
- TYWE1S_flashing.txt and images/pinout.png contain contributor-supplied carrier-board information. Keep the supplied board numbering separate from bare-module pins and the GPIO assignments in YAML. Distinguish supplied steps from documentation-added backup guidance; do not claim either was independently hardware-tested. Restoration, PCB-revision measurements and connector-to-GPIO tracing remain TODO until evidence is provided.

## Validation and reporting

- Use the pinned ESPHome version in `requirements-dev.txt`. Run `python3 scripts/validate-esphome.py --generate` after configuration changes; use dummy credentials only.
- Validation and C++ generation are not firmware compilation, hardware verification or a safety assessment. Report exactly which checks ran.
- Hardware test records must state model/article number, module/PCB revision if known, ESPHome version, steps, expected result, observed result and date. Explicitly identify tests that were not run.
- Keep experimental status until the maintainer has evidence to change it. Update README, test notes and changelog when behavior changes.
- Describe AI assistance in the PR and preserve human authorship. Never claim the assistant physically tested a heater.
