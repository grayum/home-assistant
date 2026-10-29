# TODO

## Installation and recovery documentation

- [x] Add Paul-contributed TYWE1S carrier-board connection/flashing notes and pinout, with edited spelling and clearer instructions.
- [x] Add a full-flash backup/readback comparison procedure based on Espressif's documentation, labelled as awaiting device testing.
- [ ] Confirm the maintainer's exact article number, module/PCB revisions and detected flash size against the contributed TYWE1S drawing and existing YAML profile.
- [ ] Run the backup procedure on the actual unit and record matching reads, detected capacity and tool version without publishing the dumps or credentials. Distinguish Wi-Fi-module flash from separate heater MCU settings.
- [ ] Verify restoration/recovery using the owner's own backup and document the limitations.
- [ ] Independently verify the contributed stock-to-ESPHome instructions on the identified board revision and record the result, including a qualified review of isolation, supply and logic levels.
- [ ] Supplement the supplied **four-pin connector** drawing (1=RX, 2=TX, 3=GND, 4=5V) with an oriented board photograph, measured supply/logic levels, confirmed signal directions, traced ESP GPIO mapping, PCB revision and isolation evidence. Do not infer these from the drawing or YAML alone.

The [connection/flashing notes](TYWE1S_flashing.txt) and [pinout](images/pinout.png) now provide contributor-supplied starting information. The backup section was added during documentation review; neither it nor restoration has been independently hardware-tested. Remaining checkboxes concern verification and missing evidence, not a claim that the contribution has already been measured or certified.

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
