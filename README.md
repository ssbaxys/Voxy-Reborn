# Voxy: Reborn

**Unofficial NeoForge port of [Voxy](https://github.com/MCRcortex/voxy)** by MCRcortex.

**Author:** Xylos_Official  
**Version:** 1.0.0  
**License:** [MIT](LICENSE.md)  
**Target:** Minecraft 1.21.1 · NeoForge 21.1.x  
**Base lineage:** [JohnSnow14284/neo-voxy](https://github.com/JohnSnow14284/neo-voxy)

Far-distance terrain LoD with Sodium integration and Sable sub-level visibility beyond vanilla render distance.

## Requirements

| Dependency | Version |
|---|---|
| Minecraft | 1.21.1 |
| NeoForge | 21.1.x |
| Java | 21 |
| Sodium | 0.8.x (NeoForge) — recommended |

Optional: Iris, Sable, Create, EclipticSeasons.

## Build

```powershell
.\gradlew clean build
```

Distributable jar: `build/libs/voxy-reborn-1.0.0.jar` (via `slimJar`; name includes `mod_version`).

Product version is firm **1.0.0** (`gradle.properties` → `mod_version`). Bump that field for releases.

## Adding upstream source

You can drop extra / upstream Java into `src/` safely:

- Gradle `sourceSets` already excludes Fabric-only and missing-API classes
- `processResources` strips Fabric metadata and Chinese locale files if re-added
- `.gitignore` ignores orphan root dumps, reference clones (`_*/`), `zh_cn`/`zh_tw`, and maintainer leftover notes

## Compatibility notes

- [Sodium wiki](https://github.com/CaffeineMC/sodium/wiki) — rendering hooks / chunk pipeline
- [Sable wiki](https://github.com/ryanhcode/sable/wiki) — sub-levels; companion for plot-safe coords

## Credits & license

**Voxy: Reborn** is an unofficial NeoForge **port of Voxy**.

| | |
|---|---|
| Original Voxy | [MCRcortex](https://github.com/MCRcortex/voxy) |
| NeoForge lineage | [JohnSnow14284/neo-voxy](https://github.com/JohnSnow14284/neo-voxy) |
| Voxy: Reborn | **Xylos_Official** |
| License | **MIT** — see [LICENSE](LICENSE) / [LICENSE.md](LICENSE.md) |

Not affiliated with Mojang, Microsoft, NeoForge, Sodium, Iris, Sable, or the original Voxy author.
