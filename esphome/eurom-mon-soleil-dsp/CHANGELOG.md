# Changelog

## Unreleased - TYWE1S documentation contribution 2026-10-29

- Added Paul-contributed `TYWE1S_flashing.txt` and the approved carrier-board `images/pinout.png`, with development credit linking to @ph-wheels.
- Corrected spelling and clarified board pin numbering, crossed UART connections, the carrier's separate 5 V supply and 3.3 V TTL signaling, manual bootloader entry, browser serial installation and reconnection.
- Added a documentation-sourced full-flash backup procedure with two reads and comparison; it was absent from the original notes and remains untested on the heater. Restoration remains open.
- Updated the README, agent instructions, datapoint provenance, test notes and TODOs without changing heater-control YAML or claiming new model compatibility.

## Unreleased - public starter prepared 2026-10-29

- Added the experimental Eurom Mon Soleil DSP project, attributed datapoint observations and the two maintainer-supplied photographs.
- Preserved the original board, UART, DP mappings, entity names and encrypted OTA configuration. No heater-control logic change was intentionally introduced.
- Replaced the literal fallback AP password with a `!secret` reference. Wi-Fi and API credentials remain secret references; example values contain no working credentials.
- Removed the private `wifi.use_address`, placeholder area and unrelated Home Assistant helper text sensor. No heater behavior depended on that helper in the supplied YAML.
- Added an ESPHome minimum version of 2026.9.0 for encrypted OTA syntax and a 2026.10.1 validation baseline.
- Added setup notes, raw DP12 limitations, M/P distinctions, DP101 write-path caveat, testing checklist and evidence requirements.
- Left manufacturer backup/restoration, initial flashing, module identification and connector pinout as explicit TODOs. The manual is excluded from the public project.
