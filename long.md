# VOXY: REBORN

```
WORKSPACE / VOXY REBORN
BUILD     / VERSION 1.0.0
MODULE    / XYLOS / NEOFORGE
```

**Far-distance terrain. Near-zero compromise.**

Voxy: Reborn is a NeoForge 1.21.1 Level-of-Detail (LoD) rendering mod. It extends your horizon far past vanilla chunk distance by drawing distant terrain at reduced detail — built for Sodium, tuned for immersion, and authored for the modern NeoForge stack.

**Author:** Xylos_Official  
**Version:** 1.0.0  
**Lineage:** unofficial NeoForge port based on [neo-voxy](https://github.com/JohnSnow14284/neo-voxy) · original Voxy by [MCRcortex](https://github.com/MCRcortex)

---

## Demo

<!-- INSERT DEMO SCREENSHOT: horizon / LoD vista -->
![Demo — distant LoD horizon](IMAGES/demo-horizon.png)

<!-- INSERT DEMO SCREENSHOT: close transition vanilla ↔ LoD -->
![Demo — vanilla to LoD transition](IMAGES/demo-transition.png)

<!-- INSERT DEMO SCREENSHOT: Sable sub-level / ship at distance -->
![Demo — Sable sub-level at range](IMAGES/demo-sable.png)

<!-- INSERT DEMO GIF OR VIDEO THUMB: flight / dogfight / exploration -->
![Demo — in motion](IMAGES/demo-motion.gif)

---

## What it does

| Capability | Detail |
|---|---|
| **Extended horizon** | LoD terrain beyond vanilla render distance |
| **Sodium pipeline** | Integrates with Sodium’s world renderer and options |
| **Smooth handover** | Circular LoD fade between vanilla chunks and distant LoD |
| **Sable “from afar”** | Sub-levels / contraptions stay visible out toward the LoD horizon |
| **Optional stack** | Iris shaders, Create distant content, seasonal snow (when present) |

---

## Requirements

| | |
|---|---|
| Minecraft | **1.21.1** |
| Loader | **NeoForge 21.1.x** |
| Java | **21** |
| Recommended | **Sodium 0.8.x (NeoForge)** |

**Optional:** Iris · Sable · Create · EclipticSeasons

> Hard requirement for meaningful client LoD: a NeoForge-compatible Sodium build. Fabric Sodium will not work.

---

## Highlights — 1.0.0

- Firm product release branding: **Voxy: Reborn** by **Xylos_Official**
- NeoForge-native LoD core (neo-voxy lineage)
- Sodium video-settings integration
- Sable sub-level render-distance extension + depth shim vs LoD terrain
- Create distant trains / tracks / contraption tooling (when Create is installed)
- Clean English-only localization · no community-fork locale baggage

---

## Install

1. Install Minecraft **1.21.1** + NeoForge **21.1.x**
2. Install **Sodium** (NeoForge build for 1.21.1)
3. Drop `voxy-reborn.jar` into `mods/`
4. Launch · open Sodium video settings → Voxy page · tune LoD distance

<!-- INSERT DEMO SCREENSHOT: Sodium / Voxy settings page -->
![Demo — settings](IMAGES/demo-settings.png)

---

## Sable notes

For sub-levels / vehicles past vanilla view distance:

- Enable Sable LoD rendering in Voxy options
- Tune **simulated contraption distance %** toward your LoD horizon
- On dedicated servers, raise Sable **`sub_level_tracking_range`** so distant plots stay discoverable

See also: [Sable wiki](https://github.com/ryanhcode/sable/wiki) · [Sodium wiki](https://github.com/CaffeineMC/sodium/wiki)

---

## Shader warning

If your shader pack already fades LoD / distant terrain (e.g. Photon), **disable Voxy’s circular LoD fade** to avoid double-fade noise and broken shadow edges.

---

## Credits

| | |
|---|---|
| Original Voxy | MCRcortex / Cortex |
| NeoForge lineage | JohnSnow14284/neo-voxy & community maintainers |
| Voxy: Reborn 1.0.0 | **Xylos_Official** |

Upstream Voxy is All Rights Reserved. This is an unofficial NeoForge development release — not affiliated with Mojang, Microsoft, NeoForge, Sodium, Iris, or the original author.

---

```
BUILD / VERSION 1.0.0
MODULE / XYLOS / NEOFORGE
```
