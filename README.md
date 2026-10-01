<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Cole Munz" src="assets/banner-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://munzzyy.dev"><b>munzzyy.dev</b></a> ·
  <a href="https://log.munzzyy.dev/">build log</a> ·
  <a href="https://github.com/sponsors/munzzyy">sponsor</a> ·
  <a href="mailto:Munzzyy1@proton.me">Munzzyy1@proton.me</a>
</p>

I'm Cole. I work on embedded and firmware security: kernel drivers, device firmware, and the RF/SDR stack around them. I also build privacy apps, and I send fixes upstream wherever correctness matters. The interesting bugs get written up on my [build log](https://log.munzzyy.dev/).

**140+ patches merged upstream · 60+ open · 70+ projects**

## Android apps

No accounts and no tracking. Starling and Magpie are on F-Droid, and the rest are in review there. [Tern](https://github.com/munzzyy/tern) keeps all of them up to date straight from their releases.

| App | What it does |
|:----|:-------------|
| [Starling](https://github.com/munzzyy/starling) | Location sharing for family and friends. Positions are encrypted on your phone, so the relay only ever holds ciphertext, and it deletes that after 24 hours. On [F-Droid](https://f-droid.org/packages/app.starlingmap/). |
| [Tern](https://github.com/munzzyy/tern) | Installs and updates apps straight from GitHub, GitLab, Codeberg and F-Droid repos, and checks who signed every file before Android sees it. Works on Android TV too. |
| [Sepia](https://github.com/munzzyy/sepia) | Shows everything a photo says about you, blacks out what you choose, then re-opens its own output and checks it again. |
| [Magpie](https://github.com/munzzyy/magpie) | An incident journal that still proves something months later: encrypted, hash-chained, and checkable without the app. On [F-Droid](https://f-droid.org/packages/io.github.munzzyy.magpie/). |
| [Blot](https://github.com/munzzyy/blot) | A PDF redactor that can't leave the text behind, because it never keeps the text in the first place. |
| [Sweep](https://github.com/munzzyy/sweep) | A plain-language stalkerware checkup. It never says "you are safe", and a Leave fast button sits on every screen. |

## Tools and web apps

| Project | What it does |
|:--------|:-------------|
| [nucleus](https://github.com/munzzyy/nucleus) | A local security console: passive recon, an authorized pentest kit, opsec checks and file scrubbing. It binds to loopback and nothing else. |
| [tellcheck-github](https://github.com/munzzyy/tellcheck-github) | Flags pull requests that look AI-written and shows the signals behind every flag. A [Firefox add-on](https://addons.mozilla.org/en-US/firefox/addon/tellcheck-for-github/). |
| [hopandhaul](https://github.com/munzzyy/hopandhaul) | Finds when flying into a cheaper hub and taking the train beats flying direct. [Open it](https://hopandhaul.munzzyy.dev/). |
| [liftmath](https://github.com/munzzyy/liftmath) | Gym math you can check: 1RM from any set, plate loading, Wilks, DOTS and IPF scores. [Open it](https://liftmath.munzzyy.dev/). |
| [puzzlepress](https://github.com/munzzyy/puzzlepress) | Seven daily puzzle games with no accounts and no ads. [Play](https://puzzlepress.munzzyy.dev/). |
| [coacheck](https://github.com/munzzyy/coacheck) | Reads a research-peptide certificate of analysis and does the math. A calculator, not advice. |

All of it is GPL-3.0-or-later, and almost all of it runs with zero dependencies. Every repo has a CONTRIBUTING file and an open issue tracker, and [munzzyy.dev](https://munzzyy.dev) has the whole set on one page.

## Upstream

I'm one of the ten people with code in the Flipper One's MCU firmware before the device ships, with more fixes in its Linux kernel, U-Boot, debug probe, corelibs and docs. Mainline U-Boot carries three btrfs patches of mine, reviewed by a btrfs maintainer, and the Rockchip tree took a two-patch SPI series for devices with no wire in one direction. GNU cpio fixed a stack overread in its tar parser that I reported with a repro and a patch; a plain `cpio -itv` could hit it. The rest is memory-safety and correctness work in YARA, osquery, proxmark3, rtl_433, gpac, libevpl and Monero, and fixes in privacy tools like Orbot, ProofMode, mat2 and OONI Probe.

<details>
<summary><b>Everything merged</b></summary>

### BUSY Bar

The BUSY Bar shipped in July 2026, so the firmware is young and the bugs are still live. Three I found went upstream together in [busy-app/busybar-firmware #905](https://github.com/busy-app/busybar-firmware/pull/905), which the team wrote themselves from my reports and patches:

| Change | How it got there |
|:-------|:-----------------|
| A zero-size allocation in the JS runner, where `furi_check` turns `malloc(0)` into a reboot, so `console.log("")` restarts the device | reported and patched in [#903](https://github.com/busy-app/busybar-firmware/pull/903), reimplemented by the team |
| An error string in the HTTP display API leaked on the success path | reported and patched in [#904](https://github.com/busy-app/busybar-firmware/pull/904), reimplemented by the team |
| A missing union tag in the draw API | reported privately to their security address, fixed in the same PR |

Also traced why [`pip install busylib`](https://github.com/busy-app/busylib-py/issues/43) used to hand you a version that refused to talk to current firmware: 1.1.0 and 1.2.0 were tagged on GitHub but never published to PyPI, so pip could only reach 1.0.0. Fixed upstream since; current releases publish cleanly.

### Security, firmware and RF

| Repo | Change |
|:-----|:-------|
| [u-boot/custodians/u-boot-rockchip](https://source.denx.de/u-boot/custodians/u-boot-rockchip) | Support SPI devices with no wire in one direction: a two-patch series applied for the 2027.01 cycle, written for the Flipper One's display bus, where the missing MISO pin doubles as the end-of-frame GPIO |
| [GNU cpio](https://git.savannah.gnu.org/cgit/cpio.git/commit/?id=e5bb73f8c2f3) | Stack out-of-bounds read parsing unterminated tar uname/gname fields, reachable from `cpio -itv`; reported with a repro and patch, fixed upstream by the maintainer |
| [flipperdevices/flipper-linux-kernel](https://github.com/flipperdevices/flipper-linux-kernel/pull/18) | Add the missing cache hierarchy to the RK3576 CPU nodes, so Linux stops reporting the Flipper One with no caches |
| [flipperdevices/flipper-linux-kernel](https://github.com/flipperdevices/flipper-linux-kernel/pull/17) | Register the Flipper One's side-button interrupt in the MCU MFD driver |
| [flipperdevices/flipper-linux-kernel](https://github.com/flipperdevices/flipper-linux-kernel/pull/21) | Wire the Type-C up port's VBUS supply to the connector so the USB mux can actually switch it |
| [flipperdevices/flipper-linux-kernel](https://github.com/flipperdevices/flipper-linux-kernel/pull/22) | Stop dwc3 returning an error when a gadget dequeues a request that already completed; the same patch is on the linux-usb list for mainline |
| [u-boot/u-boot](https://github.com/u-boot/u-boot/commit/1cf825afd0d7ebb4857002833658574efbef6626) | Report file sizes from btrfs readdir, with a path-release fix and a shared size helper: three patches in mainline U-Boot, reviewed by a btrfs maintainer |
| [flipperdevices/u-boot](https://github.com/flipperdevices/u-boot/commit/b5b70eeb5a377cf72643255bcc26a5cd88d11199) | Fix btrfs zstd decompression of compressed inline extents, applied from my mainline U-Boot patch |
| [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware/pull/4429) | Initialize `timings_cnt` on infrared decoder alloc and fix its bounds check |
| [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware/pull/4428) | Check the NFC poller error before reading a FeliCa system-code response |
| [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware/pull/4427) | NUL-terminate the PAC/Stanley card id before parsing it |
| [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware/pull/4426) | Fix the trailing Wiegand parity bit on Pyramid LFRFID cards |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/232) | Stop the main GPIO expander's reset path using a freed handle when re-initialization fails |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/220) | Read `Status1`, not `Control0`, when the USB-C PD controller checks `rx_empty` |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/221) | Fail the haptic driver's auto-calibration when its status register says it failed |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/219) | Leave the I2C slave critical section on the early return |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/216) | Check for NULL before dereferencing in serial deinit |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/215) | Remove a double `pipe_free` in the CLI UART disable handler |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/212) | Fix a hard fault in the Flipper One CLI when USB disconnects mid-`screen` |
| [flipperdevices/flipperone-mcu-firmware](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/211) | Stop a wild pointer reaching the Flipper One's device-info callback |
| [flipperdevices/fbtng-corelibs](https://github.com/flipperdevices/fbtng-corelibs/pull/40) | Fix a use-after-free in the event loop when a run-once subscription fires |
| [flipperdevices/fbtng-corelibs](https://github.com/flipperdevices/fbtng-corelibs/pull/39) | Fix an out-of-bounds read in `bit_lib` when the requested bits fit one byte |
| [flipperdevices/flipperzero-good-faps](https://github.com/flipperdevices/flipperzero-good-faps/pull/307) | Add the missing terminator to the SPI-mem chip table |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2221) | Null-terminate authenticode digest/thumbprint hex buffers |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2220) | Fix a string leak in CLI `args_free` |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2219) | Honor `-w`/`--no-warnings` for the file-too-large skip message |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2237) | Reject hex jump and repeat lengths that overflow an int |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2223) | Document the `YR_RE_SCAN_LIMIT` regular-expression scan limit |
| [ffuf/ffuf](https://github.com/ffuf/ffuf/pull/905) | Stop terminal control characters leaking into redirected output |
| [gpac/gpac](https://github.com/gpac/gpac/pull/3877) | Fix four more `strchr` scan loops that read past the end of the buffer, two reachable from a crafted file, finishing a sweep upstream had started |
| [chimera-nas/libevpl](https://github.com/chimera-nas/libevpl/pull/117) | Stop the HTTP server freeing a client's in-flight request twice when the client disconnects mid-request |
| [chimera-nas/libevpl](https://github.com/chimera-nas/libevpl/pull/136) | Keep the iovec ring's waist in bounds when the ring grows |
| [YARAHQ/yara-forge](https://github.com/YARAHQ/yara-forge/pull/88) | Align indexed and patterned hash meta fields |
| [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma/pull/6114) | Add a vmmemWSL exception to the non-existing-file rule |
| [splunk/security_content](https://github.com/splunk/security_content/pull/4146) | Add a PreAuthType filter to the PetitPotam Kerberos detection |
| [splunk/security_content](https://github.com/splunk/security_content/pull/4196) | Fix a wildcard declared on a column that doesn't exist in the malware user-agent lookup |
| [openmls/openmls](https://github.com/openmls/openmls/pull/2143) | Sign the GroupInfo with the new key when a commit rotates the signature key, so joiners can verify it |
| [openmls/openmls](https://github.com/openmls/openmls/pull/2151) | Stop FrankenProposal's length counting the proposal type twice |
| [cake-tech/trezor-flutter](https://github.com/cake-tech/trezor-flutter/pull/2) | Decode a THP packet that exactly fills the packet size |
| [monero-project/monero](https://github.com/monero-project/monero/pull/11019) | Keep the additional-derivations list aligned when one derivation fails, so later outputs are still seen as yours |
| [monero-project/monero](https://github.com/monero-project/monero/pull/11020) | Make `sweep_account` expand `index=all` against the account being swept, not the current one |
| [monero-project/monero](https://github.com/monero-project/monero/pull/11018) | Clamp the `export_outputs` start to the transfer count so the reserve stops underflowing |
| [monero-project/monero](https://github.com/monero-project/monero/pull/11213) | Stop reserve proofs counting outputs already spent by a broadcast-but-unconfirmed send, which proved reserve the wallet no longer had |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8986) | Scan XDG-base-directory Firefox profiles |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8987) | Add the Windsurf `.devin` path to `vscode_extensions` |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8991) | Add the Microsoft Edge and Flatpak paths to `chrome_extensions` on Linux |
| [osquery/osquery](https://github.com/osquery/osquery/pull/9036) | Split the sudoers header on the first unescaped whitespace, so escaped spaces in a name stop leaking into the rule |
| [osquery/osquery](https://github.com/osquery/osquery/pull/9051) | Fix an off-by-one bounds check in the `platform_info` BIOS parser |
| [osquery/osquery](https://github.com/osquery/osquery/pull/9068) | Widen the `mounts` table's statfs block and inode counts to 64 bits, so a filesystem over 2^32 blocks stops wrapping |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3412) | Fix a heap out-of-bounds read in `hf iclass view` on short dumps |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3411) | Stop the IR56 wiegand decode leaking the header sentinel bit into the facility code |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3409) | Fix byte-swapped, corrupted EM 4x05 dump files |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3433) | More heap out-of-bounds reads on short iCLASS dump files |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3471) | Set the `stringop-overflow` guard before the bundled deps are added, so the flag actually reaches them |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3555) | Reject an undersized `hf xerox view` dump file instead of reading past the buffer |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3597) | Fix a `uint8_t` offset wraparound in the m-bus payload parser |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3572) | Restore a missing `bitbuffer_clear` in `pulse_slicer_dmc` |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3574) | Fix swapped order/inversion nibbles in the secplus_v2 docs |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3657) | Widen the m-bus payload offset so the AFL sub-header recursion can't wrap it |

### RF/SDR, privacy, accessibility, localization and health

| Repo | Change |
|:-----|:-------|
| [f4exb/sdrangel](https://github.com/f4exb/sdrangel/pull/2795) | Bump bundled faad2 to 2.10.1 to fix a heap overflow |
| [f4exb/sdrangel](https://github.com/f4exb/sdrangel/pull/2797) | Fix a crash adding a LocalSink channel with no Local Input device |
| [UberGuidoZ/Flipper](https://github.com/UberGuidoZ/Flipper/pull/684) | Fix dead links in the Sub-GHz docs |
| [PentHertz/urh-ng](https://github.com/PentHertz/urh-ng/commit/7306cca71ec0) | Decode int8 samples as `signed char` so magnitudes stay correct on ARM |
| [jcsteh/osara](https://github.com/jcsteh/osara/pull/1416) | Make paste/duplicate screen-reader messages translatable |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1748) | Request `ACCESS_LOCAL_NETWORK` before opening the proxy on all interfaces |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1780) | Fix the `Bridge.doh` getter reading the `dot` parameter, so `doh=` lines parse and stop growing duplicates |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1786) | Fix bridge parsing for transport lines with no fingerprint |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1789) | Unit tests for the bridge line parser, one case per transport the app ships |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1791) | Normalize unicode spaces in custom bridge input |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1792) | Add an IPv6 preference to `HTTPTunnelPort` |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1807) | Kindness mode stopped a proxy it had already stopped, died with the process, and left stale UPnP mappings behind; closed a two-year-old battery-drain issue |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1805) | Register the Kindness network callback according to the Wi-Fi-only preference, so cellular users aren't stranded |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1809) | Stop every log line being stored twice when two start requests land in the bind window |
| [guardianproject/proofmode-android](https://github.com/guardianproject/proofmode-android/pull/135) | Correct the C2PA GPS hemisphere on longitude and latitude |
| [guardianproject/proofmode-android](https://github.com/guardianproject/proofmode-android/pull/136) | Correct the bitmap stride in QR code generation |
| [guardianproject/proofmode-android](https://github.com/guardianproject/proofmode-android/pull/138) | Write the C2PA `dc:creator` as a JSON array instead of a bracketed string, so the signed CAWG metadata parses |
| [guardianproject/proofmode-android](https://github.com/guardianproject/proofmode-android/pull/143) | Stop the share screen crashing when a shared media URI's read grant has expired |
| [flipperdevices/flipperone-debug-probe](https://github.com/flipperdevices/flipperone-debug-probe/pull/12) | Keep the DAP ring-buffer backpressure working after the pointers wrap, plus NULL handle derefs and a CDC error read as a huge length ([#16](https://github.com/flipperdevices/flipperone-debug-probe/pull/16), [#15](https://github.com/flipperdevices/flipperone-debug-probe/pull/15), [#14](https://github.com/flipperdevices/flipperone-debug-probe/pull/14)) |
| [flipperdevices/flipperone-docs](https://github.com/flipperdevices/flipperone-docs/pull/423) | A docs validator for fragment anchors and broken image paths, plus microSD, charger and fuel-gauge part-number fixes ([#427](https://github.com/flipperdevices/flipperone-docs/pull/427), [#422](https://github.com/flipperdevices/flipperone-docs/pull/422), [#421](https://github.com/flipperdevices/flipperone-docs/pull/421)) |
| [hotosm/tasking-manager](https://github.com/hotosm/tasking-manager/pull/7287) | Replace Nominatim reverse geocoding with an in-database pg-nearest-city lookup |
| [ooni/probe-cli](https://github.com/ooni/probe-cli/pull/1786) | Remove a stray debug print in the feature-flag cache |
| [jvoisin/mat2](https://github.com/jvoisin/mat2/pull/49) | Strip APEv2 and ID3v1 tags that sit after the audio in mp3, ogg and flac |
| [jvoisin/mat2](https://github.com/jvoisin/mat2/pull/50) | Sort OOXML attributes themselves instead of reordering elements out of schema order |
| [jvoisin/mat2](https://github.com/jvoisin/mat2/pull/55) | Clean tracked moves out of docx files, which Word records as `moveFrom`/`moveTo`, not `del`/`ins` |
| [jvoisin/mat2](https://github.com/jvoisin/mat2/pull/58) | Stop a bare HTML5 void element like `<meta charset="utf-8">` making mat2 refuse to clean the file |
| [symfony/symfony](https://github.com/symfony/symfony/pull/64796) | Fix the Finnish BIC/IBAN mismatch translation |
| [symfony/symfony](https://github.com/symfony/symfony/pull/64815) | Drop an always-true `method_exists` check |
| [symfony/symfony](https://github.com/symfony/symfony/pull/65128) | Escape backslashes in Mime's `Address::getEncodedName()`, so a name ending in one can't break the header quoting |
| [symfony/symfony](https://github.com/symfony/symfony/pull/64811) | Fix broken placeholder translations across [Armenian](https://github.com/symfony/symfony/pull/64811), [Arabic](https://github.com/symfony/symfony/pull/64810), [Basque](https://github.com/symfony/symfony/pull/64809), [Turkish](https://github.com/symfony/symfony/pull/64808), [Galician](https://github.com/symfony/symfony/pull/64807), [Azerbaijani](https://github.com/symfony/symfony/pull/64806), [Traditional Chinese](https://github.com/symfony/symfony/pull/64805), [Finnish](https://github.com/symfony/symfony/pull/64804), and [Welsh](https://github.com/symfony/symfony/pull/64803) |
| [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio/pull/7261) | Improve the French localization |
| [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio/pull/7260) | Improve the Dutch localization, [again later](https://github.com/ghostfolio/ghostfolio/pull/7296) |
| [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio/pull/7297) | Fix corrupted state attributes in the Catalan and Turkish locales |
| [jsverse/transloco](https://github.com/jsverse/transloco/pull/940) | Respect currency in `numberFormatOptions` |
| [simonoppowa/OpenNutriTracker](https://github.com/simonoppowa/OpenNutriTracker/pull/513) | Catch silent zero-byte export writes |
| [simonoppowa/OpenNutriTracker](https://github.com/simonoppowa/OpenNutriTracker/pull/615) | Stop stone body weights showing a full stone worth of pounds |
| [davidhealey/waistline](https://github.com/davidhealey/waistline/pull/961) | Guard `Meals.init` against overlapping calls |
| [davidhealey/waistline](https://github.com/davidhealey/waistline/pull/960) | Distinguish rate-limit and network errors from bad USDA keys |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8990) | Fix a one-past-end iterator deref in `vscode_extensions` |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8989) | Fix the wrong `key_strength` reported for Windows certificates |
| [osquery/osquery](https://github.com/osquery/osquery/pull/9010) | Key the recursive-glob visited set on (device, inode) so symlinked trees stop being rescanned |
| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates/pull/16672) | Stop `nfs-v3-exposed` counting a `PROG_UNAVAIL` reply as a hit |
| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates/pull/16739) | Fix the nh-c2 DSL matcher that can never match |
| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates/pull/16912) | Stop two WordPress VR XSS templates firing on any HTML page that escapes the payload |
| [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates/pull/17032) | Stop the HP printer default-login template matching any 200 response as a hit |
| [monero-project/monero-gui](https://github.com/monero-project/monero-gui/pull/4652) | Fix a stale subaddress selection on the Receive page after switching accounts |
| [monero-project/monero-gui](https://github.com/monero-project/monero-gui/pull/4672) | Read a restore date typed without hyphens as a date, not a block height |
| [mdn/translated-content](https://github.com/mdn/translated-content/pull/36835) | Correct the Japanese `Reflect.deleteProperty()` docs |
| [openfoodfacts/open-prices](https://github.com/openfoodfacts/open-prices/pull/1376) | Remove an unreachable branch in the barcode short-code fixups |
| [openfoodfacts/open-prices](https://github.com/openfoodfacts/open-prices/pull/1414) | Point the `prediction_count__lte` filter at prediction count instead of price count |
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
| [splunk/security_content](https://github.com/splunk/security_content/pull/4245) | Point two LOLBin detections at a CIM field that exists, so a renamed whoami or arp stops slipping past them |
| [ClickHouse/click-ui](https://github.com/ClickHouse/click-ui/pull/1140) | Respect a consumer-supplied `aria-label` instead of overwriting it with the icon name |
| [FoggedLens/deflock](https://github.com/FoggedLens/deflock/pull/133) | Tell people they need an OpenStreetMap account before they pick a way to report a camera |
| [mdn/translated-content](https://github.com/mdn/translated-content/pull/37508) | Use a real minus sign in the BigInt operator example across the Korean, Portuguese and Russian docs |

</details>

<details>
<summary><b>Open and in review</b>: 66 across 45 projects</summary>

**Security and detection**
- [assimp/assimp #6800](https://github.com/assimp/assimp/pull/6800): out-of-bounds access on short uv source and mapping mode properties
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
- [YARAHQ/yara-forge #91](https://github.com/YARAHQ/yara-forge/pull/91): a missing comma in the tag_names list glues two tags into one
- [jsverse/transloco #982](https://github.com/jsverse/transloco/pull/982): block prototype pollution in the keys-manager's `mergeDeep`
- [semgrep/semgrep-rules #4051](https://github.com/semgrep/semgrep-rules/pull/4051): two Python security-hooks rules treat `realpath()`/`abspath()` as complete path sanitization, hiding real findings
- [libtiff/libtiff !945](https://gitlab.com/libtiff/libtiff/-/merge_requests/945): `LZWDecodeCompat` returns a failure without zeroing the output buffer, unlike `LZWDecode`, so a truncated strip leaks whatever was in memory

**OSINT**
- [mxrch/GHunt #601](https://github.com/mxrch/GHunt/pull/601): read `isDefault` from the API for profile photos instead of hashing the image
- [mxrch/GHunt #602](https://github.com/mxrch/GHunt/pull/602): key profile photos by their own container, not the outer loop's

**RF / SDR**
- [PentHertz/urh-ng #4](https://github.com/PentHertz/urh-ng/pull/4): fix CRC data-range detection for reflected (`ref_out`) CRCs
- [UberGuidoZ/Flipper #687](https://github.com/UberGuidoZ/Flipper/pull/687): flippercheck, a validator for `.sub` / `.ir` / RTTTL / playlist files

**Flipper One** (9 open): the device isn't out yet, so this is bootloader, MCU firmware, build system and docs
- [flipperdevices/fbtng-corelibs #43](https://github.com/flipperdevices/fbtng-corelibs/pull/43): a record-destroy race where a late opener can hang forever
- [flipperdevices/fbtng-corelibs #44](https://github.com/flipperdevices/fbtng-corelibs/pull/44): an int overflow in the datetime timestamp calculation
- [flipperdevices/flipperone-debug-probe #17](https://github.com/flipperdevices/flipperone-debug-probe/pull/17): the CLI accepts `clock_out 14`, which reads past the clock source table
- [flipperdevices/flipperone-mcu-firmware #218](https://github.com/flipperdevices/flipperone-mcu-firmware/pull/218): the touch controller uses I2C registers before they're initialized
- [flipperdevices/flipperone-testing #8](https://github.com/flipperdevices/flipperone-testing/pull/8), [#7](https://github.com/flipperdevices/flipperone-testing/pull/7) and [#6](https://github.com/flipperdevices/flipperone-testing/pull/6): the test suite passed a failed CPU/GPU stress run, cut the stress test short, and reported a PipeWire restart that never happened
- [flipperdevices/flipperos-installer #2](https://github.com/flipperdevices/flipperos-installer/pull/2) and [#1](https://github.com/flipperdevices/flipperos-installer/pull/1): profile names that collide with reserved subvolumes, and an unreadable `/proc` source treated as a free disk

**FreeWili 2** (1 open): the RP2350B handheld, before it ships
- [freewili/wilibsp #28](https://github.com/freewili/wilibsp/pull/28): a USB `wMaxPacketSize` copied unbounded into a 64-byte DPRAM window, four IR decoders accepting over-long frames, a UF2 check that ignored the family ID, and signed CIC accumulators; each fix with a test that fails without it, plus the repo's first CI

**Flipper Zero** (6 open): firmware, apps, host tooling, and the RPC libraries
- [flipperdevices/flipperzero-firmware #4452](https://github.com/flipperdevices/flipperzero-firmware/pull/4452): passing the same RX callback to both UARTs trips a `furi_check` and kills the firmware
- [flipperdevices/qFlipper #255](https://github.com/flipperdevices/qFlipper/pull/255): crash when a log message arrives with no category
- [flipperdevices/flipperzero-good-faps #308](https://github.com/flipperdevices/flipperzero-good-faps/pull/308): mfkey redoes recovery for nonces it already solved
- [flipperdevices/video-game-module #16](https://github.com/flipperdevices/video-game-module/pull/16): check the screen frame size before copying it
- [flipperdevices/video-game-module #17](https://github.com/flipperdevices/video-game-module/pull/17): reject data frames larger than the receive buffer
- [flipperdevices/flipperzero-ufbt #68](https://github.com/flipperdevices/flipperzero-ufbt/pull/68): a build killed by a signal is reported as a success

**TentacleOS** (4 open): firmware for the ESP32-P4 High Boy handheld
- [HighCodeh/TentacleOS #159](https://github.com/HighCodeh/TentacleOS/pull/159): the firmware didn't build from a clean checkout (an lvgl 9.6 break and a missing mbedtls DES option)
- [HighCodeh/TentacleOS #160](https://github.com/HighCodeh/TentacleOS/pull/160): the host emulator's tests stopped building after the SPI frame CRC change
- [HighCodeh/TentacleOS #161](https://github.com/HighCodeh/TentacleOS/pull/161): bring the interactive SDL simulator back to life on current dev
- [HighCodeh/TentacleOS #162](https://github.com/HighCodeh/TentacleOS/pull/162): bounds-check the ELF sections of a sideloaded app before the loader copies them

**GrapheneOS** (2 open): fixes in their allocator and Info app, every one reproduced before it was written
- [GrapheneOS/hardened_malloc #374](https://github.com/GrapheneOS/hardened_malloc/pull/374): get `make tidy` back to green by restructuring the two remaining analyzer complaints instead of suppressing them
- [GrapheneOS/Info #132](https://github.com/GrapheneOS/Info/pull/132): show a translated offline message with a Retry action instead of a raw `UnknownHostException` toast

**F-Droid**
- [fdroid/fdroidserver !1863](https://gitlab.com/fdroid/fdroidserver/-/merge_requests/1863): list every certificate in a rotated app's signing lineage, so a client can match a copy signed with the old key

**Accessibility**
- [jcsteh/osara #1434](https://github.com/jcsteh/osara/pull/1434): on the Mac, messages that carry a menu access key never find their translations, so localized menus read out in English

**Privacy / anti-surveillance**
- [FoggedLens/deflock #137](https://github.com/FoggedLens/deflock/pull/137): the geocode cache key ignores the geojson variant, so two different lookups share one cache slot
- [ooni/probe-cli #1811](https://github.com/ooni/probe-cli/pull/1811): make tlsmiddlebox's ClientId settable and validate its value
- [guardianproject/ripple #45](https://github.com/guardianproject/ripple/pull/45): integer division collapses the panic-swipe ripple to zero on odd screen heights
- [guardianproject/tor-android #197](https://github.com/guardianproject/tor-android/pull/197): NullPointerException in `getPortFromGetInfo` when `getInfo()` fails
- [guardianproject/tor-android #198](https://github.com/guardianproject/tor-android/pull/198): pin jar timestamps so builds of the same commit come out byte-identical
- [guardianproject/wind/fdroid-metadata !27](https://gitlab.com/guardianproject/wind/fdroid-metadata/-/merge_requests/27): a browse link beside the repo mirrors a browser can't list
- [guardianproject/info !114](https://gitlab.com/guardianproject/info/-/merge_requests/114): remove the tutorials archive page

**Cryptography and wallets**
- [cake-tech/cupcake #62](https://github.com/cake-tech/cupcake/pull/62): the seed-check quiz can offer the correct word twice among the choices
- [monero-project/monero-gui #4685](https://github.com/monero-project/monero-gui/pull/4685): a self-shadowing `const` throws before the amount field can strip a leading zero, on four wallet pages

**Systems / web**
- [ClickHouse/click-ui #1141](https://github.com/ClickHouse/click-ui/pull/1141): default Button `htmlType` to button
- [openclimatefix/graph_weather #231](https://github.com/openclimatefix/graph_weather/pull/231): division-by-zero on single-axis grids
- [openclimatefix/graph_weather #230](https://github.com/openclimatefix/graph_weather/pull/230): guard optional data-module imports
- [omacom/omarchy #8076](https://github.com/omacom/omarchy/pull/8076): stop the hybrid GPU test failing on a machine without Omarchy installed

**Health / food**
- [openfoodfacts/robotoff #1919](https://github.com/openfoodfacts/robotoff/pull/1919): anchor nutrient-mention regex alternatives on word boundaries

**Localization**
- [TheIllusiveC4/Curios #622](https://github.com/TheIllusiveC4/Curios/pull/622) and [#621](https://github.com/TheIllusiveC4/Curios/pull/621): Turkish placeholder and locale-casing bugs
- [drewnoakes/metadata-extractor #741](https://github.com/drewnoakes/metadata-extractor/pull/741): lowercase hardcoded description strings with `Locale.ROOT` so the Turkish locale doesn't corrupt them
- [chubin/wttr.in #1279](https://github.com/chubin/wttr.in/pull/1279) and [#1278](https://github.com/chubin/wttr.in/pull/1278): RTL mark and corrupted Persian/Hebrew/Arabic captions
- [tolgee/tolgee-platform #3789](https://github.com/tolgee/tolgee-platform/pull/3789): keep the zero plural form in Apple XLIFF export

**Directory listings** (not fixes, just getting the tools indexed)
- [yigitkonur/awesome-webmcp #10](https://github.com/yigitkonur/awesome-webmcp/pull/10) and [#9](https://github.com/yigitkonur/awesome-webmcp/pull/9): add webmcp-devtools and webmcp-lint

</details>

## Support

If one of these saves you an afternoon, [sponsoring](https://github.com/sponsors/munzzyy) is what keeps them free, and every sponsor gets a line in [SUPPORTERS.md](SUPPORTERS.md). Monero works too:

```
8BApLkfsBS39oNXz4L1qCmZ7f5zKVRr1qLJgrHddRZb4JRcnjDkcKdk7wW7uThCeV9CuLn8o7gAn8d6vFeWNiyeXSmrRUSq
```

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/route-dark.svg">
  <img alt="" src="assets/route-light.svg" width="100%">
</picture>
