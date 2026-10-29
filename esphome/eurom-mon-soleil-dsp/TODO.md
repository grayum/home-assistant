# TODO

## Installation and recovery documentation

- [ ] Confirm the maintainer's exact article number, Wi-Fi module, flash size and PCB revisions.
- [ ] Document a verified way to back up the original manufacturer flash/configuration before modification, including integrity checks and private storage. Distinguish a full flash image from readable settings; do not upload either.
- [ ] Verify restoration/recovery using the owner's own backup and document the limitations.
- [ ] Document replacing stock firmware with ESPHome for a specifically identified module/revision, with safe isolation, power and programming requirements reviewed by a qualified person.
- [ ] Document the **internal four-pin connector**: clearly oriented photo, connector numbering, measured supply and logic levels, ground, signal directions, ESP pin mapping, revision and isolation evidence. Do not guess from wire color or the GPIO settings.

These installation items are intentionally placeholders. Contributors may submit evidence-backed PRs. This starter does not provide a wiring diagram or initial flashing commands.

## Behavior and compatibility

- [ ] Complete the supervised [test checklist](TESTING.md), with versions and observations.
- [ ] Verify climate Heat/Off writes to DP1/DP101 in both M and P modes, including transitions from ECO and idle.
- [ ] Decide whether the writable DP101 select should remain, be diagnostic by default or be replaced with read-only reporting, based on test evidence.
- [ ] Verify power-loss, ESP reboot, API loss, Wi-Fi loss and time recovery behavior; document whether heating and stored schedules persist.
- [ ] Determine stock local/app timer persistence and a verified way to inspect/clear schedules before migration.
- [ ] Investigate open-window detection and external probe behavior without inventing datapoints.
- [ ] Decode fault bits only when supported by reliable evidence; never induce hazardous faults.
- [ ] Record full firmware compilation and flash/OTA size on the actual 1 MB target.
- [ ] Add evidence-backed compatibility reports for 361919, 361933, 361902, 361926 and 361940, including hardware revisions.
- [ ] Consider an ESPHome device-directory submission after the hardware and behavior are documented.
