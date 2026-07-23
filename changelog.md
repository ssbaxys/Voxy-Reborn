# Changelog — Voxy: Reborn

```
WORKSPACE / VOXY REBORN
BUILD     / VERSION 1.0.0
MODULE    / XYLOS / NEOFORGE
```

---

## 1.0.0 — Initial release

**First firm product build of Voxy: Reborn.**

### Identity

- Rebranded as **Voxy: Reborn** by **Xylos_Official**
- Firm semver **1.0.0** (no commit-suffix version noise)
- New HUD-style icon / branding
- English-only localization

### Platform

- Minecraft **1.21.1**
- NeoForge **21.1.x**
- Java **21**
- Sodium **0.8.x** (NeoForge) integration

### Core

- Far-distance LoD terrain rendering
- Sodium world-renderer / options integration
- Circular LoD boundary fade (vanilla ↔ LoD)
- Water / lighting / storage pipeline from neo-voxy lineage

### Compatibility

- **Sable:** sub-level / contraption visibility toward LoD horizon (render-distance extension + depth shim + tracking hooks)
- **Create:** distant trains / tracks / contraption tooling (optional)
- **Iris:** shader path support (pack-dependent)
- **EclipticSeasons:** seasonal snow LoD (optional)

### Packaging

- Distributable artifact: `voxy-reborn.jar`
- Gradle excludes for Fabric leftovers & locale dumps when merging upstream sources

---

### Demo gallery (insert your shots)

<!-- INSERT: before/after vanilla vs LoD -->
![1.0.0 — horizon](IMAGES/changelog-1.0.0-horizon.png)

<!-- INSERT: Sable vehicle / sub-level at distance -->
![1.0.0 — Sable](IMAGES/changelog-1.0.0-sable.png)

<!-- INSERT: settings / branding splash -->
![1.0.0 — branding](IMAGES/changelog-1.0.0-brand.png)

---

### Known notes

- Shader packs with their own LoD fade: disable Voxy circular fade
- Dedicated servers: raise Sable `sub_level_tracking_range` for long-range sub-levels
- Always use NeoForge Sodium — Fabric builds are incompatible

---

```
END OF CHANGELOG / 1.0.0
```
