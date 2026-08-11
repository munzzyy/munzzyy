<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Cole Munz" src="assets/banner-light.svg" width="100%">
</picture>

[![Sponsor](https://img.shields.io/badge/GitHub%20Sponsors-support%20this%20work-db61a2?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/munzzyy)

I'm Cole. I work on embedded and firmware security: kernel drivers, device firmware, and the RF/SDR stack around them. I also build open-source tools and contribute upstream wherever correctness matters, from accessibility to health tech. I write up the interesting bugs on my [build log](https://munzzyy.github.io/).

Most of these are MIT; the big apps are free for noncommercial use. Almost everything runs with zero dependencies, and most come with a live demo you can try in your browser right now, no install and no account. Pick whichever fits; each repo has the full story.

## Which one do I need?

- Vetting an AI agent skill before you install it → [skillxray](https://github.com/munzzyy/skillxray)
- Writing an MCP server → [toolsmell](https://github.com/munzzyy/toolsmell) for the tool descriptions, [webmcp-lint](https://github.com/munzzyy/webmcp-lint) if it's WebMCP in a page
- Seeing what your agent actually touched on a run → [sessionxray](https://github.com/munzzyy/sessionxray)
- Screenshots feeding a vision agent → [framewall](https://github.com/munzzyy/framewall) to scan them, [injection-fixtures](https://github.com/munzzyy/injection-fixtures) to test your defense
- Shipping a translated app → [translint](https://github.com/munzzyy/translint)
- GitHub Actions → [wouldrun](https://github.com/munzzyy/wouldrun) for what fires, [actbreak](https://github.com/munzzyy/actbreak) to break into a step, [ci-safety-gate](https://github.com/munzzyy/ci-safety-gate) to gate the repo
- Checking a research-peptide COA → [coacheck](https://github.com/munzzyy/coacheck)
- Cheapest way to travel → [hopandhaul](https://github.com/munzzyy/hopandhaul)
- Strength-training math → [liftmath](https://github.com/munzzyy/liftmath)
- A daily puzzle habit → [puzzlepress](https://github.com/munzzyy/puzzlepress)

## Tools

| Project | What it does |
|---------|--------------|
| [hopandhaul](https://github.com/munzzyy/hopandhaul) | Finds when flying into a cheaper hub and taking the train the rest of the way beats flying direct. Click-the-map planner that runs in your [browser](https://munzzyy.github.io/hopandhaul/) with no install, 4,175 airports, UI in 46 languages. |
| [liftmath](https://github.com/munzzyy/liftmath) | Gym math with receipts: a 1RM estimate from any set you just did, plate loading with a barbell that loads itself as you type, and Wilks/DOTS/IPF strength scores, plus a searchable record book for powerlifting, strongman, grip sport, and track and field. A [web app](https://munzzyy.github.io/liftmath/) plus a CLI. |
| [puzzlepress](https://github.com/munzzyy/puzzlepress) | Seven daily puzzle games in your [browser](https://munzzyy.github.io/puzzlepress/): a word guesser, group sorting, a pangram hunt, a mini crossword with hand-written clues, a themed word search, letter chains, and sudoku. Installable as an app. No accounts, no ads, no tracking, zero dependencies, and every puzzle bank ships in the repo. |
| [translint](https://github.com/munzzyy/translint) | A linter for your translation files. Catches missing keys, placeholder mismatches, and untranslated values before they ship. CLI, CI gate, pre-commit, or agent skill. Its [site](https://munzzyy.github.io/translint/) practices what it lints: 32 languages, RTL included. |
| [skillxray](https://github.com/munzzyy/skillxray) | Reads an AI agent skill before you install it and flags what's hiding: prompt injection, invisible Unicode, curl-pipe-sh and reverse shells, credential theft, leaked keys. Then grades it A to F. SARIF for the GitHub Security tab, exit codes for CI. Python, zero dependencies. |
| [actbreak](https://github.com/munzzyy/actbreak) | A breakpoint debugger for GitHub Actions. Wraps `act` to pause a workflow mid-step, drop you into a live shell inside the job container, and resume when you're done. Python, zero dependencies. |
| [webmcp-devtools](https://github.com/munzzyy/webmcp-devtools) | A Chrome DevTools panel that inspects and security-lints the WebMCP tools a web page hands to AI agents: a live tool table, a call-history timeline, and per-tool tool-poisoning checks. Plain JavaScript, no build step. |
| [webmcp-lint](https://github.com/munzzyy/webmcp-lint) | The same idea as a CI gate: lints a WebMCP tool manifest against Chrome's own security guidance before you ship it. Read-only hints, untrusted-content flags, injection in tool descriptions, unconstrained parameters. Human, JSON, or SARIF out. Python, zero dependencies. |
| [framewall](https://github.com/munzzyy/framewall) | Scans a screenshot for prompt injection a person would miss but a vision model reads: hidden low-contrast text, fake system-message overlays, instructions buried in image metadata, all before your agent acts on it. Reads the text with OCR when tesseract is around and falls back to image heuristics when it isn't. Python, Pillow only. |
| [injection-fixtures](https://github.com/munzzyy/injection-fixtures) | Known visual prompt-injection payloads packaged as pytest fixtures, so anyone building a screenshot or computer-use agent can test their defenses against poisoned images right in CI. Installs straight from the repo with `pip install git+https://github.com/munzzyy/injection-fixtures`, Pillow only. |
| [sessionxray](https://github.com/munzzyy/sessionxray) | Audits a Claude Code session transcript after the fact and tells you what the agent actually touched: files outside the project, unexpected outbound hosts, secret reads, destructive commands. A security lens on your own agent's run, all local. Python, zero dependencies. |
| [toolsmell](https://github.com/munzzyy/toolsmell) | Finds the smells in an MCP server's tool descriptions and schemas: the vague verbs, undocumented parameters, and missing return docs that quietly make agents worse at using your tools. For authors, before you publish. Python, zero dependencies. |
| [wouldrun](https://github.com/munzzyy/wouldrun) | Answers which GitHub Actions workflows would fire for a given diff or event, statically, without pushing or running `act`. Resolves triggers, branch and path filters, and reusable-workflow calls, and says why each one runs or doesn't. Python, zero dependencies. |
| [ci-safety-gate](https://github.com/munzzyy/ci-safety-gate) | One GitHub Action that runs the checks an AI-era repo wants: zizmor for workflow security, skillxray for agent skills, and a secrets scan, all as a single pass-or-fail gate with one combined report. |
| [coacheck](https://github.com/munzzyy/coacheck) | Reads a research-peptide Certificate of Analysis and does the math: real deliverable purity from the labeled amount, a red-flag checklist for thin or faked COAs, and reconstitution down to syringe units. A calculator, not advice. Python, zero dependencies. |

They're all open to contributors. Each one ships a CONTRIBUTING file with the setup and the house rules, and the issue trackers are open, so if something is broken or missing, file it and I'll pick it up. Stars genuinely help other people find them.

## Upstream

Ninety-six have landed upstream and another sixty-six are open, seventy-two projects in all: correctness, security, RF/SDR, firmware, hardware docs, accessibility, and translation. That includes the Flipper One's MCU firmware, where I'm one of the ten people with code in the tree before the device ships, its Linux kernel, where a device-tree fix of mine is merged and now sitting on the mainline list, and its U-Boot, which applied my btrfs zstd fix from the mainline U-Boot list. Mainline U-Boot itself now carries three more btrfs patches of mine, reviewed by a btrfs maintainer and applied by the project's lead. A few that were fun to track down: a heap out-of-bounds read parsing short iCLASS dumps, byte-order corruption in RFID dump files, authenticode digest buffers that were never null-terminated in YARA, a flipped GPS hemisphere in a photo-evidence app, a use-after-free that fired the moment a run-once event subscription cleaned itself up, and a hard fault you could trigger by unplugging USB mid-command.

### BUSY Bar

The BUSY Bar shipped in July 2026, so the firmware is young and the bugs are still live. Three I found went upstream together in [busy-app/busybar-firmware #905](https://github.com/busy-app/busybar-firmware/pull/905), which the team wrote themselves from my reports and patches:

| Change | How it got there |
|--------|------------------|
| A zero-size allocation in the JS runner, where `furi_check` turns `malloc(0)` into a reboot, so `console.log("")` restarts the device | reported and patched in [#903](https://github.com/busy-app/busybar-firmware/pull/903), reimplemented by the team |
| An error string in the HTTP display API leaked on the success path | reported and patched in [#904](https://github.com/busy-app/busybar-firmware/pull/904), reimplemented by the team |
| A missing union tag in the draw API | reported privately to their security address, fixed in the same PR |

Also traced why [`pip install busylib`](https://github.com/busy-app/busylib-py/issues/43) hands you a version that refuses to talk to current firmware: 1.1.0 and 1.2.0 are tagged on GitHub but were never published to PyPI, so pip can only ever reach 1.0.0.

### Merged

| Repo | Change |
|------|--------|
| [flipperdevices/flipper-linux-kernel](https://github.com/flipperdevices/flipper-linux-kernel/pull/18) | Add the missing cache hierarchy to the RK3576 CPU nodes, so Linux stops reporting the Flipper One with no caches |
| [flipperdevices/flipper-linux-kernel](https://github.com/flipperdevices/flipper-linux-kernel/pull/17) | Register the Flipper One's side-button interrupt in the MCU MFD driver |
| [u-boot/u-boot](https://github.com/u-boot/u-boot/commit/1cf825afd0d7ebb4857002833658574efbef6626) | Report file sizes from btrfs readdir, with a path-release fix and a shared size helper: three patches in mainline U-Boot, reviewed by a btrfs maintainer |
| [flipperdevices/u-boot](https://github.com/flipperdevices/u-boot/commit/b5b70eeb5a377cf72643255bcc26a5cd88d11199) | Fix btrfs zstd decompression of compressed inline extents, applied from my mainline U-Boot patch |
| [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware/pull/4429) | Initialize `timings_cnt` on infrared decoder alloc and fix its bounds check |
| [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware/pull/4428) | Check the NFC poller error before reading a FeliCa system-code response |
| [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware/pull/4427) | NUL-terminate the PAC/Stanley card id before parsing it |
| [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware/pull/4426) | Fix the trailing Wiegand parity bit on Pyramid LFRFID cards |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/221) | Fail the haptic driver's auto-calibration when its status register says it failed |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/219) | Leave the I2C slave critical section on the early return |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/216) | Check for NULL before dereferencing in serial deinit |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/215) | Remove a double `pipe_free` in the CLI UART disable handler |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/212) | Fix a hard fault in the Flipper One CLI when USB disconnects mid-`screen` |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/211) | Stop a wild pointer reaching the Flipper One's device-info callback |
| [flipperdevices/fbtng-corelibs](https://github.com/flipperdevices/fbtng-corelibs/pull/40) | Fix a use-after-free in the event loop when a run-once subscription fires |
| [flipperdevices/fbtng-corelibs](https://github.com/flipperdevices/fbtng-corelibs/pull/39) | Fix an out-of-bounds read in `bit_lib` when the requested bits fit one byte |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2221) | Null-terminate authenticode digest/thumbprint hex buffers |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2220) | Fix a string leak in CLI `args_free` |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2219) | Honor `-w`/`--no-warnings` for the file-too-large skip message |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2223) | Document the `YR_RE_SCAN_LIMIT` regular-expression scan limit |
| [ffuf/ffuf](https://github.com/ffuf/ffuf/pull/905) | Stop terminal control characters leaking into redirected output |
| [YARAHQ/yara-forge](https://github.com/YARAHQ/yara-forge/pull/88) | Align indexed and patterned hash meta fields |
| [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma/pull/6114) | Add a vmmemWSL exception to the non-existing-file rule |
| [splunk/security_content](https://github.com/splunk/security_content/pull/4146) | Add a PreAuthType filter to the PetitPotam Kerberos detection |
| [splunk/security_content](https://github.com/splunk/security_content/pull/4196) | Fix a wildcard declared on a column that doesn't exist in the malware user-agent lookup |
| [openmls/openmls](https://github.com/openmls/openmls/pull/2143) | Sign the GroupInfo with the new key when a commit rotates the signature key, so joiners can verify it |
| [monero-project/monero](https://github.com/monero-project/monero/pull/11019) | Keep the additional-derivations list aligned when one derivation fails, so later outputs are still seen as yours |
| [monero-project/monero](https://github.com/monero-project/monero/pull/11020) | Make `sweep_account` expand `index=all` against the account being swept, not the current one |
| [monero-project/monero](https://github.com/monero-project/monero/pull/11018) | Clamp the `export_outputs` start to the transfer count so the reserve stops underflowing |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8986) | Scan XDG-base-directory Firefox profiles |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8987) | Add the Windsurf `.devin` path to `vscode_extensions` |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8991) | Add the Microsoft Edge and Flatpak paths to `chrome_extensions` on Linux |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3412) | Fix a heap out-of-bounds read in `hf iclass view` on short dumps |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3411) | Stop the IR56 wiegand decode leaking the header sentinel bit into the facility code |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3409) | Fix byte-swapped, corrupted EM 4x05 dump files |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3597) | Fix a `uint8_t` offset wraparound in the m-bus payload parser |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3572) | Restore a missing `bitbuffer_clear` in `pulse_slicer_dmc` |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3574) | Fix swapped order/inversion nibbles in the secplus_v2 docs |

<details>
<summary><b>The rest of the merged list</b>: RF/SDR, privacy, accessibility, localization, health</summary>

| Repo | Change |
|------|--------|
| [f4exb/sdrangel](https://github.com/f4exb/sdrangel/pull/2795) | Bump bundled faad2 to 2.10.1 to fix a heap overflow |
| [f4exb/sdrangel](https://github.com/f4exb/sdrangel/pull/2797) | Fix a crash adding a LocalSink channel with no Local Input device |
| [UberGuidoZ/Flipper](https://github.com/UberGuidoZ/Flipper/pull/684) | Fix dead links in the Sub-GHz docs |
| [PentHertz/urh-ng](https://github.com/PentHertz/urh-ng/commit/7306cca71ec0) | Decode int8 samples as `signed char` so magnitudes stay correct on ARM |
| [jcsteh/osara](https://github.com/jcsteh/osara/pull/1416) | Make paste/duplicate screen-reader messages translatable |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1748) | Request `ACCESS_LOCAL_NETWORK` before opening the proxy on all interfaces |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1780) | Fix the `Bridge.doh` getter reading the `dot` parameter, so `doh=` lines parse and stop growing duplicates |
| [guardianproject/proofmode-android](https://github.com/guardianproject/proofmode-android/pull/135) | Correct the C2PA GPS hemisphere on longitude and latitude |
| [guardianproject/proofmode-android](https://github.com/guardianproject/proofmode-android/pull/136) | Correct the bitmap stride in QR code generation |
| [guardianproject/proofmode-android](https://github.com/guardianproject/proofmode-android/pull/138) | Write the C2PA `dc:creator` as a JSON array instead of a bracketed string, so the signed CAWG metadata parses |
| [flipperdevices/flipperone-debug-probe](https://github.com/flipperdevices/flipperone-debug-probe/pull/12) | Keep the DAP ring-buffer backpressure working after the pointers wrap, plus NULL handle derefs and a CDC error read as a huge length ([#16](https://github.com/flipperdevices/flipperone-debug-probe/pull/16), [#15](https://github.com/flipperdevices/flipperone-debug-probe/pull/15), [#14](https://github.com/flipperdevices/flipperone-debug-probe/pull/14)) |
| [flipperdevices/flipperone-docs](https://github.com/flipperdevices/flipperone-docs/pull/423) | A docs validator for fragment anchors and broken image paths, plus microSD, charger and fuel-gauge part-number fixes ([#427](https://github.com/flipperdevices/flipperone-docs/pull/427), [#422](https://github.com/flipperdevices/flipperone-docs/pull/422), [#421](https://github.com/flipperdevices/flipperone-docs/pull/421)) |
| [hotosm/tasking-manager](https://github.com/hotosm/tasking-manager/pull/7287) | Replace Nominatim reverse geocoding with an in-database pg-nearest-city lookup |
| [ooni/probe-cli](https://github.com/ooni/probe-cli/pull/1786) | Remove a stray debug print in the feature-flag cache |
| [jvoisin/mat2](https://github.com/jvoisin/mat2/pull/49) | Strip APEv2 and ID3v1 tags that sit after the audio in mp3, ogg and flac |
| [jvoisin/mat2](https://github.com/jvoisin/mat2/pull/50) | Sort OOXML attributes themselves instead of reordering elements out of schema order |
| [symfony/symfony](https://github.com/symfony/symfony/pull/64796) | Fix the Finnish BIC/IBAN mismatch translation |
| [symfony/symfony](https://github.com/symfony/symfony/pull/64815) | Drop an always-true `method_exists` check |
| [symfony/symfony](https://github.com/symfony/symfony/pull/64811) | Fix broken placeholder translations across [Armenian](https://github.com/symfony/symfony/pull/64811), [Arabic](https://github.com/symfony/symfony/pull/64810), [Basque](https://github.com/symfony/symfony/pull/64809), [Turkish](https://github.com/symfony/symfony/pull/64808), [Galician](https://github.com/symfony/symfony/pull/64807), [Azerbaijani](https://github.com/symfony/symfony/pull/64806), [Traditional Chinese](https://github.com/symfony/symfony/pull/64805), [Finnish](https://github.com/symfony/symfony/pull/64804), and [Welsh](https://github.com/symfony/symfony/pull/64803) |
| [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio/pull/7261) | Improve the French localization |
| [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio/pull/7260) | Improve the Dutch localization, [again later](https://github.com/ghostfolio/ghostfolio/pull/7296) |
| [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio/pull/7297) | Fix corrupted state attributes in the Catalan and Turkish locales |
| [jsverse/transloco](https://github.com/jsverse/transloco/pull/940) | Respect currency in `numberFormatOptions` |
| [simonoppowa/OpenNutriTracker](https://github.com/simonoppowa/OpenNutriTracker/pull/513) | Catch silent zero-byte export writes |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8990) | Fix a one-past-end iterator deref in `vscode_extensions` |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8989) | Fix the wrong `key_strength` reported for Windows certificates |
| [osquery/osquery](https://github.com/osquery/osquery/pull/9010) | Key the recursive-glob visited set on (device, inode) so symlinked trees stop being rescanned |
| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates/pull/16672) | Stop `nfs-v3-exposed` counting a `PROG_UNAVAIL` reply as a hit |
| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates/pull/16739) | Fix the nh-c2 DSL matcher that can never match |
| [monero-project/monero-gui](https://github.com/monero-project/monero-gui/pull/4652) | Fix a stale subaddress selection on the Receive page after switching accounts |
| [monero-project/monero-gui](https://github.com/monero-project/monero-gui/pull/4672) | Read a restore date typed without hyphens as a date, not a block height |
| [mdn/translated-content](https://github.com/mdn/translated-content/pull/36835) | Correct the Japanese `Reflect.deleteProperty()` docs |
| [openfoodfacts/open-prices](https://github.com/openfoodfacts/open-prices/pull/1376) | Remove an unreachable branch in the barcode short-code fixups |
| [openfoodfacts/robotoff](https://github.com/openfoodfacts/robotoff/pull/1909) | Replace obsolete facet URLs with the `/facets/` prefix |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2224) | Bound the tilde-stream row count in `dotnet_parse_tilde_2` |
| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates/pull/16579) | Detect exposed ZooKeeper even when the 4lw commands are blocked |
| [splunk/security_content](https://github.com/splunk/security_content/pull/4147) | Add a computer-account filter to the service-ticket detection |
| [flipperdevices/flipperone-docs](https://github.com/flipperdevices/flipperone-docs/pull/419) | Fix broken section anchors and an image path, add a missing eSIM mention |
| [flipperdevices/flipperone-docs](https://github.com/flipperdevices/flipperone-docs/pull/417) | Fix a mismatched M.2 thickness spec on the M.2 port page |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3632) | Reject out-of-range temperature and humidity in the GT-WT03 decoder |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3635) | Reject implausible temperature and humidity in the WT450 decoder |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3645) | Reject an all-zero Truck TPMS payload that passes the XOR check |
| [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware/pull/4425) | Reject a zero or negative timer interval in `js_event_loop` |
| [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware/pull/4424) | Don't read past the buffer in `bit_lib` when the requested bits fit one byte |
| [flipperdevices/flipper-application-catalog](https://github.com/flipperdevices/flipper-application-catalog/pull/1154) | Log the folder being skipped, not a leftover filename |

</details>

<details>
<summary><b>Open / in review</b>: 66 PRs across 44 repos</summary>

**Security and detection**
- [elastic/detection-rules #6383](https://github.com/elastic/detection-rules/pull/6383): KQL wildcard lexer fails on escaped specials with spaces
- [chimera-nas/libevpl #114](https://github.com/chimera-nas/libevpl/pull/114): fixed-size HTTP header buffer overflow on emit
- [ffuf/ffuf #924](https://github.com/ffuf/ffuf/pull/924): keyword and value columns scrambled in CSV/HTML/Markdown output when more than one wordlist is used
- [YARAHQ/yara-forge #89](https://github.com/YARAHQ/yara-forge/pull/89): match author/reference/description meta keys case-insensitively
- [semgrep/semgrep-rules #3999](https://github.com/semgrep/semgrep-rules/pull/3999): stop flagging Renovate `packageRules` already covered by `minimumReleaseAge`
- [semgrep/semgrep-rules #3998](https://github.com/semgrep/semgrep-rules/pull/3998): remove the obsolete `no-replaceall` rule
- [evilsocket/opensnitch #1634](https://github.com/evilsocket/opensnitch/pull/1634): fix a duplicated `a-z` class in auto-generated rule names
- [evilsocket/opensnitch #1641](https://github.com/evilsocket/opensnitch/pull/1641): an empty `list` operator matches every connection, so one rule with no sub-operators swallows the whole ruleset
- [elastic/detection-rules #6501](https://github.com/elastic/detection-rules/pull/6501): KQL-to-EQL conversion treats an escaped or quoted asterisk as a wildcard
- [elastic/detection-rules #6502](https://github.com/elastic/detection-rules/pull/6502): validate the field against the schema in KQL range expressions
- [SigmaHQ/sigma #6180](https://github.com/SigmaHQ/sigma/pull/6180): the macOS network-service-scanning filter matches any `l`, not netcat's listen flag
- [semgrep/semgrep-rules #4020](https://github.com/semgrep/semgrep-rules/pull/4020): `run-shell-injection` flags the truthiness-check shape on bare inputs
- [ffuf/ffuf #925](https://github.com/ffuf/ffuf/pull/925): strip wordlist comments before the `%ext%` branch, not only after it
- [chimera-nas/libevpl #117](https://github.com/chimera-nas/libevpl/pull/117): the HTTP server frees a client's in-flight request twice when the client disconnects mid-request
- [osquery/osquery #9036](https://github.com/osquery/osquery/pull/9036): split the sudoers header on the first unescaped whitespace, so escaped spaces in a name stop leaking into the rule
- [VirusTotal/yara #2237](https://github.com/VirusTotal/yara/pull/2237): reject hex jump and repeat lengths that overflow an int
- [YARAHQ/yara-forge #91](https://github.com/YARAHQ/yara-forge/pull/91): a missing comma in the tag_names list glues two tags into one
- [jsverse/transloco #982](https://github.com/jsverse/transloco/pull/982): block prototype pollution in the keys-manager's `mergeDeep`

**OSINT**
- [mxrch/GHunt #601](https://github.com/mxrch/GHunt/pull/601): read `isDefault` from the API for profile photos instead of hashing the image
- [mxrch/GHunt #602](https://github.com/mxrch/GHunt/pull/602): key profile photos by their own container, not the outer loop's

**RF / SDR**
- [PentHertz/urh-ng #4](https://github.com/PentHertz/urh-ng/pull/4): fix CRC data-range detection for reflected (`ref_out`) CRCs
- [UberGuidoZ/Flipper #687](https://github.com/UberGuidoZ/Flipper/pull/687): flippercheck, a validator for `.sub` / `.ir` / RTTTL / playlist files
- [RfidResearchGroup/proxmark3 #3433](https://github.com/RfidResearchGroup/proxmark3/pull/3433): more heap out-of-bounds reads on short iCLASS dump files

**Flipper One**: the device isn't out yet, so this is kernel, bootloader, MCU firmware, build system and docs
- [flipperdevices/flipper-linux-kernel #21](https://github.com/flipperdevices/flipper-linux-kernel/pull/21): wire the Type-C up port's VBUS supply to the connector so the mux can actually switch it
- [flipperdevices/flipper-linux-kernel #22](https://github.com/flipperdevices/flipper-linux-kernel/pull/22): dwc3 returns an error when a gadget dequeues a request that already completed, reshaped so it can go to linux-usb as-is
- [flipperdevices/fbtng-corelibs #43](https://github.com/flipperdevices/fbtng-corelibs/pull/43): a record-destroy race where a late opener can hang forever
- [flipperdevices/flipperone-mcu-firmware #220](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/220): the USB-C PD controller checks `rx_empty` against the wrong register
- [flipperdevices/flipperone-mcu-firmware #218](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/218): the touch controller uses I2C registers before they're initialized
- [flipperdevices/flipperone-testing #8](https://github.com/flipperdevices/flipperone-testing/pull/8), [#7](https://github.com/flipperdevices/flipperone-testing/pull/7) and [#6](https://github.com/flipperdevices/flipperone-testing/pull/6): the test suite passed a failed CPU/GPU stress run, cut the stress test short, and reported a PipeWire restart that never happened
- [flipperdevices/flipperos-installer #2](https://github.com/flipperdevices/flipperos-installer/pull/2) and [#1](https://github.com/flipperdevices/flipperos-installer/pull/1): profile names that collide with reserved subvolumes, and an unreadable `/proc` source treated as a free disk

**Flipper Zero**: apps, host tooling, and the RPC libraries
- [flipperdevices/qFlipper #255](https://github.com/flipperdevices/qFlipper/pull/255): crash when a log message arrives with no category
- [flipperdevices/flipperzero-good-faps #308](https://github.com/flipperdevices/flipperzero-good-faps/pull/308): mfkey redoes recovery for nonces it already solved
- [flipperdevices/flipperzero-good-faps #307](https://github.com/flipperdevices/flipperzero-good-faps/pull/307): a missing terminator in the SPI-mem chip table
- [flipperdevices/video-game-module #16](https://github.com/flipperdevices/video-game-module/pull/16): check the screen frame size before copying it
- [flipperdevices/video-game-module #17](https://github.com/flipperdevices/video-game-module/pull/17): reject data frames larger than the receive buffer
- [flipperdevices/flipperzero-ufbt #68](https://github.com/flipperdevices/flipperzero-ufbt/pull/68): a build killed by a signal is reported as a success

**Accessibility**
- [ClickHouse/click-ui #1140](https://github.com/ClickHouse/click-ui/pull/1140): respect a consumer-supplied `aria-label` instead of overwriting it with the icon name
- [jcsteh/osara #1434](https://github.com/jcsteh/osara/pull/1434): on the Mac, messages that carry a menu access key never find their translations, so localized menus read out in English

**Privacy / anti-surveillance**
- [FoggedLens/deflock #133](https://github.com/FoggedLens/deflock/pull/133): tell people they need an OpenStreetMap account before they pick a way to report a camera
- [FoggedLens/deflock #137](https://github.com/FoggedLens/deflock/pull/137): the geocode cache key ignores the geojson variant, so two different lookups share one cache slot
- [ooni/probe-cli #1811](https://github.com/ooni/probe-cli/pull/1811): make tlsmiddlebox's ClientId settable and validate its value

**Cryptography and wallets**
- [openmls/openmls #2151](https://github.com/openmls/openmls/pull/2151): FrankenProposal's length counts the proposal type twice
- [cake-tech/cupcake #62](https://github.com/cake-tech/cupcake/pull/62): the seed-check quiz can offer the correct word twice among the choices
- [cake-tech/trezor-flutter #2](https://github.com/cake-tech/trezor-flutter/pull/2): a THP packet that exactly fills the packet size fails to decode

**Systems / web**
- [ClickHouse/click-ui #1141](https://github.com/ClickHouse/click-ui/pull/1141): default Button `htmlType` to button
- [openclimatefix/graph_weather #231](https://github.com/openclimatefix/graph_weather/pull/231): division-by-zero on single-axis grids
- [openclimatefix/graph_weather #230](https://github.com/openclimatefix/graph_weather/pull/230): guard optional data-module imports
- [symfony/symfony #65128](https://github.com/symfony/symfony/pull/65128): Mime's `Address::getEncodedName()` escapes quotes but not backslashes, so a name ending in one breaks the header quoting

**Health / food**
- [davidhealey/waistline #961](https://github.com/davidhealey/waistline/pull/961): guard `Meals.init` against overlapping calls
- [davidhealey/waistline #960](https://github.com/davidhealey/waistline/pull/960): distinguish rate-limit/network errors from bad USDA keys
- [simonoppowa/OpenNutriTracker #615](https://github.com/simonoppowa/OpenNutriTracker/pull/615): stone body weights can display a full stone worth of pounds
- [openfoodfacts/open-prices #1414](https://github.com/openfoodfacts/open-prices/pull/1414): the `prediction_count__lte` filter was filtering on `price_count`
- [openfoodfacts/robotoff #1919](https://github.com/openfoodfacts/robotoff/pull/1919): anchor nutrient-mention regex alternatives on word boundaries

**Localization**
- [TheIllusiveC4/Curios #622](https://github.com/TheIllusiveC4/Curios/pull/622) and [#621](https://github.com/TheIllusiveC4/Curios/pull/621): Turkish placeholder and locale-casing bugs
- [drewnoakes/metadata-extractor #741](https://github.com/drewnoakes/metadata-extractor/pull/741): lowercase hardcoded description strings with `Locale.ROOT` so the Turkish locale doesn't corrupt them
- [chubin/wttr.in #1279](https://github.com/chubin/wttr.in/pull/1279) and [#1278](https://github.com/chubin/wttr.in/pull/1278): RTL mark and corrupted Persian/Hebrew/Arabic captions
- [tolgee/tolgee-platform #3789](https://github.com/tolgee/tolgee-platform/pull/3789): keep the zero plural form in Apple XLIFF export
- [mdn/translated-content #37508](https://github.com/mdn/translated-content/pull/37508): use a real minus sign in the BigInt operator example across the Korean, Portuguese and Russian docs

**Directory listings** (not fixes, just getting the tools indexed)
- [yigitkonur/awesome-webmcp #10](https://github.com/yigitkonur/awesome-webmcp/pull/10) and [#9](https://github.com/yigitkonur/awesome-webmcp/pull/9): add webmcp-devtools and webmcp-lint

</details>

## Support

All of this is free and maintained on my own time. If one of these tools saves you a trip, a bad batch, or an afternoon of debugging, [sponsoring](https://github.com/sponsors/munzzyy) is what keeps it that way. Every sponsor gets a permanent line in [SUPPORTERS.md](SUPPORTERS.md).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/route-dark.svg">
  <img alt="" src="assets/route-light.svg" width="100%">
</picture>

<p align="center"><sub>Munzzyy1@proton.me</sub></p>
