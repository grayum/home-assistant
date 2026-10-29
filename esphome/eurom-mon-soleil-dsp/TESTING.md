# Testing and validation

## Starting evidence

The source YAML attributes DP1/2/3/4/101/102 observations to the maintainer's log/button testing on 2026-10-28. Detailed logs, the exact installed ESPHome version and a full test record were not supplied. The maintainer is still testing. These notes do not certify heater safety or other variants.

## Public example software validation

Run from the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate-esphome.py --generate
```

The script copies the public configuration into a temporary directory and supplies generated dummy secrets. It never reads your local `secrets.yaml`, connects to a device or flashes firmware. The included GitHub workflow runs the same checks on pushes and PRs. Review the Actions result; no successful GitHub run is claimed before publication.

The validation baseline is ESPHome 2026.10.1. Configuration validation and C++ generation are checked separately from a full toolchain build. See the dated record at the end of this file for the actual preparation results.

## Supervised hardware checklist

Use the heater in its normal manufacturer-approved position. Do not intentionally tip, cover, overheat, obstruct or fault it. Stop if physical behavior is unexpected. Network-loss checks require a person present who can operate the heater directly; software disconnects are not a heat cut-off.

Record each result as pass, fail or not run, with actual observations. A checkbox is only completed after a real test.

| Check | Expected observation / question | Status |
| --- | --- | --- |
| Identity | Article number, module/PCB revision, installed ESPHome version and config commit recorded | Not run for this public example |
| State after startup | Observe DP1/4/101/102, display and heat state before sending commands; identify retained state | Not run |
| HA power Off | Heater/display and HA agree; observe DP1 and DP101 | Not run |
| HA Heat in M and P | Capture writes to DP1/DP101 and verify physical response; confirm DP4 is unchanged | Not run |
| P mode setpoint | Above/below ambient: compare setpoint, sun indicator, HA action and actual normal heat cycling | Not run |
| Manual mode | Confirm manual element control and that a setpoint does not imply thermostatic regulation | Not run |
| Element select in P | Determine whether writes are ignored, override temporarily or alter regulation; record results | Not run |
| Panel / remote feedback | Power, MODE, +/− and bars changes reach HA; preserve control behavior | Not run |
| ECO transitions | Enable/disable ECO from different modes; check 16 °C, EC display, restored setpoint and mode | Not run |
| Time sync | Check day/time after cold start and after HA reconnect; do not assume sync succeeded | Not run |
| Existing timers | Identify retained schedules and interactions without assuming the ESPHome YAML removed them | Not run |
| API/Wi-Fi loss | Under direct supervision, observe heater state and ESP reboot/reconnect behavior | Not run |
| Normal power cycle | Record heat, setpoint, mode, ECO and schedule state after restart | Not run |
| Temperature / probe | Compare DP3/display and, if already fitted, external-probe behavior | Not run |
| Fault DP | Record naturally occurring/previously known fault values only; do not manufacture faults | Not run |
| Open-window button | Repeat normal button interaction and record any DP changes; do not simulate dangerous conditions | Not run |

## Hardware report template

```text
Date:
Model and article number:
Module / PCB revision (or unknown):
ESPHome version:
Home Assistant version:
Configuration commit:
Initial M/P, power, ECO and timer state:
Action / expected result:
Observed panel, HA and redacted DP changes:
Result (pass / fail / not run):
Remaining uncertainties:
```

## Preparation record - 2026-10-29

| Check | Result |
| --- | --- |
| ESPHome 2026.10.1 configuration validation with temporary dummy secrets | Passed |
| ESPHome 2026.10.1 C++ source generation (`compile --only-generate`) | Passed |
| Compare control configuration against supplied YAML | Board, UART, logger, API, OTA, time, Tuya, climate, selects, switches and sensors preserved |
| Publication review | Original literal fallback password and private address absent; helper removed; photos unchanged and no EXIF entries found; no manufacturer PDF included |
| Full firmware/toolchain compilation and binary/OTA size | Not run |
| Flashing or hardware tests of this public example | Not run; requires maintainer testing |
| GitHub Actions | Workflow supplied; not run on GitHub before publication |

Time zone is normally inferred from the build environment when it is not set in YAML. Check the resulting local day/time on the heater; set `time.homeassistant.timezone` explicitly in your private configuration if needed. Time-source availability and timer behavior remain hardware test items.

## TYWE1S documentation contribution - 2026-10-29

Paul (@ph-wheels) supplied connection/initial-flashing notes and a numbered carrier-board drawing through the maintainer. Editing corrects typos (including TYME1S → TYWE1S), clarifies 3.3 V UART logic versus the carrier's 5 V input, and adds a full-flash backup/readback comparison procedure based on Espressif's documentation. Backup commands were absent from the source contribution; they are not presented as a completed device test.

The pin table was checked against the supplied drawing and the original connection notes. No voltage, isolation, connector-to-GPIO, flash-read, flash-write or restoration test was performed during this documentation edit. No heater-control YAML or validation-tooling behavior was changed. Record those hardware results before closing the remaining installation/recovery TODOs.

The maintainer subsequently supplied the original legacy `read_flash` command with a 2 MiB length and an erase example. The guide preserves the backup example, supplies modern syntax, flags the unresolved 2 MiB read versus 1 MiB board-profile distinction, and corrects the erase target from ESP32 to ESP8266. A full erase is optional and follows verified backup; no erase was performed. YAML comments and credits now attribute Paul's development work alongside Claude AI (Anthropic); no functional YAML setting changed.
