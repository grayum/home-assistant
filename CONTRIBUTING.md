# Contributing

Small, focused pull requests are welcome, including documentation and compatibility reports.

1. Read the project's README and TODO. Open an issue first for a substantial behavior or hardware change.
2. Work on a branch. Keep private device YAML, credentials, firmware and backups outside tracked files.
3. Describe the problem, resulting behavior and evidence. For a new model, include the article number, module/PCB revision if known and a redacted datapoint report. A similar enclosure or wattage is insufficient evidence.
4. Install `requirements-dev.txt` in a virtual environment and run `python3 scripts/validate-esphome.py --generate`.
5. For behavior changes, record relevant supervised device tests using the project test checklist. State clearly when hardware testing was not possible.
6. Review `git diff --cached` and `git diff --cached --name-only` before committing. Do not attach the manufacturer manual or raw device logs.

Never intentionally obstruct, tip, overheat or fault a heater to test this project. Follow the manufacturer's operating instructions. Hardware work belongs with a competent, qualified person; no verified internal wiring guide is currently provided here.

## AI-assisted contributions

AI assistance is allowed. Contributors remain responsible for correctness, permission to contribute material, privacy and safety. Briefly disclose the tools used and what was checked in the PR. Follow [AGENTS.md](AGENTS.md); do not substitute plausible AI-generated mappings or pinouts for measurements.

## License

By contributing original material, you agree to provide it under the repository's MIT License. Only submit photographs and other material you have permission to redistribute. Do not upload manufacturer firmware or manuals.
