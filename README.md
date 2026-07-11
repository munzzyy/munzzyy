<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Cole Munz" src="assets/banner-light.svg" width="100%">
</picture>

I'm Cole. I build open-source tools and contribute upstream where correctness matters — security, RF/SDR, accessibility, health tech.

Everything below is free for noncommercial use and runs with zero dependencies. Most come with a live demo you can try in your browser right now — no install, no account. Pick whichever fits; each repo has the full story.

## Tools

| Project | What it does |
|---------|--------------|
| [noslop](https://github.com/munzzyy/noslop) | Catches the AI tells in your writing — buzzwords, filler, flat rhythm — and points you at what to fix before you hit send. Reads sixteen languages, each with its own researched tell lists. Runs in your [browser](https://munzzyy.github.io/noslop/) (UI in 32 languages), your terminal, CI, or as an agent skill. |
| [hopandhaul](https://github.com/munzzyy/hopandhaul) | Finds when flying into a cheaper hub and taking the train the rest of the way beats flying direct. Click-the-map planner that runs in your [browser](https://munzzyy.github.io/hopandhaul/) with no install, 4,175 airports, UI in 46 languages. |
| [liftmath](https://github.com/munzzyy/liftmath) | Strength-training math with receipts — consensus 1RM, load charts, volume landmarks, macros, plate loading, program templates. A [web app](https://munzzyy.github.io/liftmath/) plus a CLI, 32 languages. |
| [translint](https://github.com/munzzyy/translint) | A linter for your translation files — catches missing keys, placeholder mismatches, and untranslated values before they ship. CLI, CI gate, pre-commit, or agent skill. Its [site](https://munzzyy.github.io/translint/) practices what it lints: 32 languages, RTL included. |
| [skillxray](https://github.com/munzzyy/skillxray) | Reads an AI agent skill before you install it and flags what's hiding — prompt injection, invisible Unicode, curl-pipe-sh and reverse shells, credential theft, leaked keys — then grades it A–F. SARIF for the GitHub Security tab, exit codes for CI. Python, zero dependencies. |
| [actbreak](https://github.com/munzzyy/actbreak) | A breakpoint debugger for GitHub Actions. Wraps `act` to pause a workflow mid-step, drop you into a live shell inside the job container, and resume when you're done. Python, zero dependencies. |
| [webmcp-devtools](https://github.com/munzzyy/webmcp-devtools) | A Chrome DevTools panel that inspects and security-lints the WebMCP tools a web page hands to AI agents — a live tool table, a call-history timeline, and per-tool tool-poisoning checks. Plain JavaScript, no build step. |

They're all open to contributors, several with issues tagged **good first issue** if you want a place to start.

## Upstream

Thirty-seven landed upstream now, with another thirty-odd open across sixteen more repos: correctness, security, RF/SDR, accessibility, and translation. A few that were fun to track down: a heap out-of-bounds read parsing short iCLASS dumps, byte-order corruption in RFID dump files, authenticode digest buffers that were never null-terminated in YARA, an OAuth open-redirect in a medical-records system, a flipped GPS hemisphere in a photo-evidence app, and a fixed-size HTTP header buffer that overflowed on emit.

### Merged

| Repo | Change |
|------|--------|
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2221) | Null-terminate authenticode digest/thumbprint hex buffers |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2220) | Fix a string leak in CLI `args_free` |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2219) | Honor `-w`/`--no-warnings` for the file-too-large skip message |
| [YARAHQ/yara-forge](https://github.com/YARAHQ/yara-forge/pull/88) | Align indexed and patterned hash meta fields |
| [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma/pull/6114) | Add a vmmemWSL exception to the non-existing-file rule |
| [splunk/security_content](https://github.com/splunk/security_content/pull/4146) | Add a PreAuthType filter to the PetitPotam Kerberos detection |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8986) | Scan XDG-base-directory Firefox profiles |
| [osquery/osquery](https://github.com/osquery/osquery/pull/8987) | Add the Windsurf `.devin` path to `vscode_extensions` |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3412) | Fix a heap out-of-bounds read in `hf iclass view` on short dumps |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3411) | Stop the IR56 wiegand decode leaking the header sentinel bit into the facility code |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3409) | Fix byte-swapped, corrupted EM 4x05 dump files |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3597) | Fix a `uint8_t` offset wraparound in the m-bus payload parser |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3572) | Restore a missing `bitbuffer_clear` in `pulse_slicer_dmc` |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3574) | Fix swapped order/inversion nibbles in the secplus_v2 docs |
| [f4exb/sdrangel](https://github.com/f4exb/sdrangel/pull/2795) | Bump bundled faad2 to 2.10.1 to fix a heap overflow |
| [f4exb/sdrangel](https://github.com/f4exb/sdrangel/pull/2797) | Fix a crash adding a LocalSink channel with no Local Input device |
| [UberGuidoZ/Flipper](https://github.com/UberGuidoZ/Flipper/pull/684) | Fix dead links in the Sub-GHz docs |
| [PentHertz/urh-ng](https://github.com/PentHertz/urh-ng/commit/7306cca71ec0) | Decode int8 samples as `signed char` so magnitudes stay correct on ARM |
| [jcsteh/osara](https://github.com/jcsteh/osara/pull/1416) | Make paste/duplicate screen-reader messages translatable |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1748) | Request `ACCESS_LOCAL_NETWORK` before opening the proxy on all interfaces |
| [ooni/probe-cli](https://github.com/ooni/probe-cli/pull/1786) | Remove a stray debug print in the feature-flag cache |
| [symfony/symfony](https://github.com/symfony/symfony/pull/64796) | Fix the Finnish BIC/IBAN mismatch translation |
| [symfony/symfony](https://github.com/symfony/symfony/pull/64815) | Drop an always-true `method_exists` check |
| [symfony/symfony](https://github.com/symfony/symfony/pull/64811) | Fix broken placeholder translations across [Armenian](https://github.com/symfony/symfony/pull/64811), [Arabic](https://github.com/symfony/symfony/pull/64810), [Basque](https://github.com/symfony/symfony/pull/64809), [Turkish](https://github.com/symfony/symfony/pull/64808), [Galician](https://github.com/symfony/symfony/pull/64807), [Azerbaijani](https://github.com/symfony/symfony/pull/64806), [Traditional Chinese](https://github.com/symfony/symfony/pull/64805), [Finnish](https://github.com/symfony/symfony/pull/64804), and [Welsh](https://github.com/symfony/symfony/pull/64803) |
| [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio/pull/7261) | Improve the French localization |
| [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio/pull/7260) | Improve the Dutch localization |
| [mdn/translated-content](https://github.com/mdn/translated-content/pull/36835) | Correct the Japanese `Reflect.deleteProperty()` docs |
| [openfoodfacts/open-prices](https://github.com/openfoodfacts/open-prices/pull/1376) | Remove an unreachable branch in the barcode short-code fixups |
| [openfoodfacts/robotoff](https://github.com/openfoodfacts/robotoff/pull/1909) | Replace obsolete facet URLs with the `/facets/` prefix |

<details>
<summary><b>Open / in review</b> — 30+ PRs across ~16 more repos</summary>

**Security and detection**
- [elastic/detection-rules #6383](https://github.com/elastic/detection-rules/pull/6383): KQL wildcard lexer fails on escaped specials with spaces
- [splunk/security_content #4147](https://github.com/splunk/security_content/pull/4147): computer-account filter in the service-ticket detection
- [openemr/openemr #12768](https://github.com/openemr/openemr/pull/12768): validate `post_logout_redirect_uri` before redirecting (open-redirect)
- [chimera-nas/libevpl #114](https://github.com/chimera-nas/libevpl/pull/114): fixed-size HTTP header buffer overflow on emit
- [VirusTotal/yara #2224](https://github.com/VirusTotal/yara/pull/2224): bound the tilde-stream row count in `dotnet_parse_tilde_2`
- [VirusTotal/yara #2223](https://github.com/VirusTotal/yara/pull/2223): document the `YR_RE_SCAN_LIMIT` regex scan limit
- [YARAHQ/yara-forge #89](https://github.com/YARAHQ/yara-forge/pull/89): match author/reference/description meta keys case-insensitively
- [semgrep/semgrep-rules #3999](https://github.com/semgrep/semgrep-rules/pull/3999): stop flagging Renovate `packageRules` already covered by `minimumReleaseAge`
- [semgrep/semgrep-rules #3998](https://github.com/semgrep/semgrep-rules/pull/3998): remove the obsolete `no-replaceall` rule
- [osquery/osquery #8990](https://github.com/osquery/osquery/pull/8990): fix a one-past-end iterator deref in `vscode_extensions`
- [osquery/osquery #8989](https://github.com/osquery/osquery/pull/8989): fix the wrong `key_strength` for Windows certificates
- [osquery/osquery #8991](https://github.com/osquery/osquery/pull/8991): add Edge and Flatpak paths to `chrome_extensions` on Linux

**RF / SDR**
- [PentHertz/urh-ng #4](https://github.com/PentHertz/urh-ng/pull/4): fix CRC data-range detection for reflected (`ref_out`) CRCs

**Accessibility**
- [patternfly/patternfly #8481](https://github.com/patternfly/patternfly/pull/8481): document listbox/option/aria-selected for select menus

**Privacy / anti-censorship**
- [guardianproject/proofmode-android #136](https://github.com/guardianproject/proofmode-android/pull/136): correct the QR bitmap stride
- [guardianproject/proofmode-android #135](https://github.com/guardianproject/proofmode-android/pull/135): correct the C2PA GPS hemisphere

**Systems / web**
- [ClickHouse/click-ui #1141](https://github.com/ClickHouse/click-ui/pull/1141): default Button `htmlType` to button
- [ClickHouse/click-ui #1140](https://github.com/ClickHouse/click-ui/pull/1140): respect a consumer-supplied `aria-label`
- [openclimatefix/graph_weather #231](https://github.com/openclimatefix/graph_weather/pull/231): division-by-zero on single-axis grids
- [openclimatefix/graph_weather #230](https://github.com/openclimatefix/graph_weather/pull/230): guard optional data-module imports
- [hotosm/tasking-manager #7287](https://github.com/hotosm/tasking-manager/pull/7287): replace Nominatim reverse geocoding with pg-nearest-city

**Health / food**
- [davidhealey/waistline #961](https://github.com/davidhealey/waistline/pull/961): guard `Meals.init` against overlapping calls
- [davidhealey/waistline #960](https://github.com/davidhealey/waistline/pull/960): distinguish rate-limit/network errors from bad USDA keys
- [simonoppowa/OpenNutriTracker #513](https://github.com/simonoppowa/OpenNutriTracker/pull/513): catch silent 0-byte exports

**Localization**
- [TheIllusiveC4/Curios #622](https://github.com/TheIllusiveC4/Curios/pull/622) and [#621](https://github.com/TheIllusiveC4/Curios/pull/621): Turkish placeholder and locale-casing bugs
- [chubin/wttr.in #1279](https://github.com/chubin/wttr.in/pull/1279) and [#1278](https://github.com/chubin/wttr.in/pull/1278): RTL mark and corrupted Persian/Hebrew/Arabic captions
- [ghostfolio/ghostfolio #7297](https://github.com/ghostfolio/ghostfolio/pull/7297): fix corrupted state attributes in the ca and tr locales
- [ghostfolio/ghostfolio #7296](https://github.com/ghostfolio/ghostfolio/pull/7296): improve the Dutch localization
- [tolgee/tolgee-platform #3789](https://github.com/tolgee/tolgee-platform/pull/3789): keep the zero plural form in Apple XLIFF export
- [jsverse/transloco #940](https://github.com/jsverse/transloco/pull/940): respect currency in `numberFormatOptions`
- [simonoppowa/OpenNutriTracker #515](https://github.com/simonoppowa/OpenNutriTracker/pull/515) and [#514](https://github.com/simonoppowa/OpenNutriTracker/pull/514): Slovak and English i18n keys

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/route-dark.svg">
  <img alt="" src="assets/route-light.svg" width="100%">
</picture>

<p align="center"><sub>Munzzyy5@proton.me</sub></p>
