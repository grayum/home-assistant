Adds an experimental ESPHome configuration for local Home Assistant control of a Eurom Mon Soleil DSP 400 WiFi heater through its Tuya MCU. The maintainer is still testing; the 650/770 W and Swiss-plug variants are explicitly unverified candidates.

Includes the sanitized configuration, two approved device photographs, setup and datapoint documentation, a hardware test checklist, contribution/AI instructions and dummy-secret validation CI. Public preparation removes the literal fallback AP password, private device address, placeholder area and unrelated Home Assistant helper while preserving the original heater mappings.

Factory backup/restoration, initial flashing and the internal four-pin connector pinout remain TODO. The manufacturer manual and private original configuration are not included. The README documents M/P behavior, unknown timer persistence and the DP101 write interaction in the climate component.

Validation: ESPHome 2026.10.1 configuration validation and C++ generation results are recorded in TESTING.md. Full firmware/toolchain compilation and hardware testing of this public example are not claimed; see that record for any environment limitation. The workflow has not run on GitHub before publication.

Created with assistance from ChatGPT & Codex (OpenAI). Maintainer review and supervised hardware verification remain necessary.
