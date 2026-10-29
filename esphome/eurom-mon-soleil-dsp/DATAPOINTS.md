# Datapoints and evidence

## Provenance

The maintainer's supplied YAML says the following observations were confirmed with logs and button tests on **2026-10-28** on a 400 W unit. Raw logs were not included with the public starter, so these are attributed maintainer observations, not independently repeated measurements. The Tuya product ID in the source is `wv9d5ocs76u6maqj`; it is a product identifier, not a per-device credential or compatibility guarantee.

| DP | Reported type | Meaning/value | Evidence and limits |
| --- | --- | --- | --- |
| 1 | Boolean | Power / standby | Maintainer reports confirmed on/off |
| 2 | Integer | Target 0-37 °C; ECO selects 16 °C | Maintainer reports confirmed; thermostat requires P mode |
| 3 | Integer | Room temperature, °C | Maintainer reports confirmed; ambient accuracy and external probe unverified |
| 4 | Enum | 0 = Manual (M), 1 = Thermostat/program (P) | Maintainer reports confirmed with MODE button |
| 101 | Enum | 0 = heating/sun, 3 = off | Maintainer reports confirmed; bars button in M, thermostat in P; writable through both select and climate Heat path |
| 102 | Boolean | ECO fixed 16 °C / EC display | Maintainer reports confirmed; transition behavior still needs a test record |
| 12 | Bitmask | Raw fault indication; 0 observed/described as no fault | Listed in source; nonzero values and individual bit meanings not verified |

No changed datapoint was observed when testing the remote's open-window control. Do not assign a guessed DP to it or invent a corresponding entity.

## UART assumptions

| Setting | Value in supplied YAML |
| --- | --- |
| ESPHome platform | ESP8266 |
| Board profile | `esp01_1m` |
| ESP RX | GPIO13 |
| ESP TX | GPIO15 |
| Baud rate | 9600 |
| Serial logger | Disabled (`baud_rate: 0`) |

These values describe firmware settings for the test installation. They do not identify the exact module, confirm flash size, specify connector pin order or prove safe voltage levels/isolation. GPIO15 is an ESP8266 boot strap pin; the existing hardware must maintain correct boot conditions. Do not rewire based only on this table.

## Evidence needed for changes

For a mapping change or new device, provide model/article number, revision, ESPHome version and a redacted sequence showing initial state, one physical/HA action, changed DP value/type and resulting display/heat indication. Include conflicting observations and unknown enum values. Keep private identifiers out of logs, and never intentionally trigger dangerous physical fault conditions.
