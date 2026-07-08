<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Cole Munz — small, sharp tools" src="assets/banner-light.svg" width="100%">
</picture>

I'm Cole. I build small, sharp tools under **Flight Unreached** and contribute to open source where correctness matters — security, RF/SDR, accessibility, health tech.

Everything below is free for noncommercial use and runs with zero dependencies. Each has a live demo you can try in your browser right now — no install, no account. Pick whichever fits; each repo has the full story.

## Tools

| Project | What it does |
|---------|--------------|
| [noslop](https://github.com/munzzyy/noslop) | Catches the AI tells in your writing — buzzwords, filler, flat rhythm — and points you at what to fix before you hit send. Reads sixteen languages, each with its own researched tell lists. Runs in your [browser](https://munzzyy.github.io/unslop/) (UI in 32 languages), your terminal, CI, or as an agent skill. |
| [hopandhaul](https://github.com/munzzyy/hopandhaul) | Finds when flying into a cheaper hub and taking the train the rest of the way beats flying direct. Click-the-map planner that runs in your [browser](https://munzzyy.github.io/hopandhaul/) with no install, 4,175 airports, UI in 46 languages. |
| [liftmath](https://github.com/munzzyy/liftmath) | Strength-training math with receipts — consensus 1RM, load charts, volume landmarks, macros, plate loading, program templates. A [web app](https://munzzyy.github.io/liftmath/) plus a CLI, 32 languages. |
| [translint](https://github.com/munzzyy/translint) | A linter for your translation files — catches missing keys, placeholder mismatches, and untranslated values before they ship. CLI, CI gate, pre-commit, or agent skill. Its [site](https://munzzyy.github.io/translint/) practices what it lints: 32 languages, RTL included. |

All four are open to contributors — each has issues tagged **good first issue** if you want a place to start.

## Upstream

Fifteen merged now, with another forty-odd open across roughly thirty more repos: correctness, security, accessibility, and translation. A few that were fun to track down: byte-order corruption in RFID dump files, authenticode digest buffers that were never null-terminated in YARA, an OAuth open-redirect in a medical-records system, a flipped GPS hemisphere in a photo-evidence app, and a fixed-size HTTP header buffer that overflowed on emit.

### Merged

| Repo | Change |
|------|--------|
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2221) | Null-terminate authenticode digest/thumbprint hex buffers |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2220) | Fix a string leak in CLI `args_free` |
| [VirusTotal/yara](https://github.com/VirusTotal/yara/pull/2219) | Honor `-w`/`--no-warnings` for the file-too-large skip message |
| [YARAHQ/yara-forge](https://github.com/YARAHQ/yara-forge/pull/88) | Align indexed and patterned hash meta fields |
| [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma/pull/6114) | Add a vmmemWSL exception to the non-existing-file rule |
| [splunk/security_content](https://github.com/splunk/security_content/pull/4146) | Add a PreAuthType filter to the PetitPotam Kerberos detection |
| [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3/pull/3409) | Fix byte-swapped, corrupted EM 4x05 dump files |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3572) | Restore a missing `bitbuffer_clear` in `pulse_slicer_dmc` |
| [merbanan/rtl_433](https://github.com/merbanan/rtl_433/pull/3574) | Fix swapped order/inversion nibbles in the secplus_v2 docs |
| [jcsteh/osara](https://github.com/jcsteh/osara/pull/1416) | Make paste/duplicate screen-reader messages translatable |
| [guardianproject/orbot-android](https://github.com/guardianproject/orbot-android/pull/1748) | Request `ACCESS_LOCAL_NETWORK` before opening the proxy on all interfaces |
| [symfony/symfony](https://github.com/symfony/symfony/pull/64796) | Fix the Finnish BIC/IBAN mismatch translation |
| [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio/pull/7261) | Improve the French localization |
| [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio/pull/7260) | Improve the Dutch localization |
| [openfoodfacts/robotoff](https://github.com/openfoodfacts/robotoff/pull/1909) | Replace obsolete facet URLs with the `/facets/` prefix |

<details>
<summary><b>Open / in review</b> — 40+ PRs across ~30 more repos</summary>

**Security and detection**
- [elastic/detection-rules #6383](https://github.com/elastic/detection-rules/pull/6383): KQL wildcard lexer fails on escaped specials with spaces
- [splunk/security_content #4147](https://github.com/splunk/security_content/pull/4147): computer-account filter in the service-ticket detection
- [openemr/openemr #12768](https://github.com/openemr/openemr/pull/12768): validate `post_logout_redirect_uri` before redirecting (open-redirect)
- [chimera-nas/libevpl #114](https://github.com/chimera-nas/libevpl/pull/114): fixed-size HTTP header buffer overflow on emit

**RF / SDR**
- [PentHertz/urh-ng #3](https://github.com/PentHertz/urh-ng/pull/3): wrong int8 magnitude/demod on ARM (signed `char`)

**Accessibility**
- [nvaccess/nvda #20444](https://github.com/nvaccess/nvda/pull/20444): clearer error for bare drive letters in Create Portable
- [patternfly/patternfly #8481](https://github.com/patternfly/patternfly/pull/8481): document listbox/option/aria-selected for select menus

**Privacy / anti-censorship**
- [guardianproject/proofmode-android #136](https://github.com/guardianproject/proofmode-android/pull/136): correct the QR bitmap stride
- [guardianproject/proofmode-android #135](https://github.com/guardianproject/proofmode-android/pull/135): correct the C2PA GPS hemisphere
- [ooni/probe-cli #1786](https://github.com/ooni/probe-cli/pull/1786): remove a stray debug print in the feature-flag cache

**Systems / web**
- [osquery/osquery #8986](https://github.com/osquery/osquery/pull/8986): scan XDG-base-directory Firefox profiles
- [osquery/osquery #8987](https://github.com/osquery/osquery/pull/8987): add the Windsurf `.devin` path to `vscode_extensions`
- [ClickHouse/click-ui #1141](https://github.com/ClickHouse/click-ui/pull/1141): default Button `htmlType` to button
- [ClickHouse/click-ui #1140](https://github.com/ClickHouse/click-ui/pull/1140): respect a consumer-supplied `aria-label`
- [openclimatefix/graph_weather #231](https://github.com/openclimatefix/graph_weather/pull/231): division-by-zero on single-axis grids
- [openclimatefix/graph_weather #230](https://github.com/openclimatefix/graph_weather/pull/230): guard optional data-module imports
- [hotosm/tasking-manager #7287](https://github.com/hotosm/tasking-manager/pull/7287): replace Nominatim reverse geocoding with pg-nearest-city
- [symfony/symfony #64815](https://github.com/symfony/symfony/pull/64815): drop an always-true `method_exists` check

**Health / food**
- [openfoodfacts/open-prices #1376](https://github.com/openfoodfacts/open-prices/pull/1376): remove an unreachable branch in the barcode fixups
- [davidhealey/waistline #961](https://github.com/davidhealey/waistline/pull/961): guard `Meals.init` against overlapping calls
- [davidhealey/waistline #960](https://github.com/davidhealey/waistline/pull/960): distinguish rate-limit/network errors from bad USDA keys
- [simonoppowa/OpenNutriTracker #513](https://github.com/simonoppowa/OpenNutriTracker/pull/513): catch silent 0-byte exports

**Localization** (Symfony validator placeholder fixes plus a wider i18n wave)
- [symfony/symfony](https://github.com/symfony/symfony/pull/64811): placeholder fixes across [Armenian](https://github.com/symfony/symfony/pull/64811), [Arabic](https://github.com/symfony/symfony/pull/64810), [Basque](https://github.com/symfony/symfony/pull/64809), [Turkish](https://github.com/symfony/symfony/pull/64808), [Galician](https://github.com/symfony/symfony/pull/64807), [Azerbaijani](https://github.com/symfony/symfony/pull/64806), [Traditional Chinese](https://github.com/symfony/symfony/pull/64805), [Finnish](https://github.com/symfony/symfony/pull/64804), and [Welsh](https://github.com/symfony/symfony/pull/64803)
- [mdn/translated-content #36835](https://github.com/mdn/translated-content/pull/36835): correct the Japanese `Reflect.deleteProperty()` docs
- [TheIllusiveC4/Curios #622](https://github.com/TheIllusiveC4/Curios/pull/622) and [#621](https://github.com/TheIllusiveC4/Curios/pull/621): Turkish placeholder and locale-casing bugs
- [chubin/wttr.in #1279](https://github.com/chubin/wttr.in/pull/1279) and [#1278](https://github.com/chubin/wttr.in/pull/1278): RTL mark and corrupted Persian/Hebrew/Arabic captions
- [tolgee/tolgee-platform #3789](https://github.com/tolgee/tolgee-platform/pull/3789): keep the zero plural form in Apple XLIFF export
- [jsverse/transloco #940](https://github.com/jsverse/transloco/pull/940): respect currency in `numberFormatOptions`
- [simonoppowa/OpenNutriTracker #515](https://github.com/simonoppowa/OpenNutriTracker/pull/515) and [#514](https://github.com/simonoppowa/OpenNutriTracker/pull/514): Slovak and English i18n keys

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/route-dark.svg">
  <img alt="" src="assets/route-light.svg" width="100%">
</picture>

<p align="center"><sub><a href="https://gitlab.com/flight-unreached">GitLab mirrors</a> · Munzzyy5@proton.me</sub></p>
