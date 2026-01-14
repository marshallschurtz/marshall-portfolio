# Dissertation Figures Status

**Last Updated:** 2026-01-13 (After refactoring integration)
**Status:** 25 Integrated / 27 Missing

---

## Technical Updates
- **Duplicates Removed**: Logic improved to prevent duplicate figure insertions.
- **Smaller Display**: Figures now display `max-w-xl` by default (was 3xl).
- **Interactive**: All figures are clickable to view full resolution.
- **Placeholders**: Missing figures show a clear placeholder box.

---

## Integrated Figures (25 Total)

### Chapter 2
- Figure 2.2: Muṣaṣir Relief (Sargon II's Palace)

### Chapter 4 (Excavations)
- Figure 4.1: Traditional Building at Mudjesir
- Figure 4.3: Gund-i Topzawa Building 1-W Phase B Full Plan
- Figure 4.4: Top-down View of Room 1
- Figure 4.5: Room 1 Pithos (Plate 44.2)
- Figure 4.6: Room 1 Pithos (Plate 44.1)
- Figure 4.7: Cross-section of Bin 1, Room 2
- Figure 4.8: Top-down View of Room 2
- Figure 4.9: Stratigraphy Comparison
- Figure 4.10: Room 2 South Facing Section
- Figure 4.11: Room 3 Objects
- Figure 4.17: Partially Pierced Disc
- Figure 4.20: Spearhead
- Figure 4.21: Gund-i Topzawa 1C-W Burial

### Chapter 5 (Survey)
- Figure 5.1: CORONA Image (1968)
- Figure 5.2: Maxar Satellite Image

### Chapter 6 (Landscape)
- Figure 6.1: Least Cost Paths (Pedestrian vs Horse)
- Figure 6.2: Vectorized Field of Rust
- Figure 6.3: Catchment of Agricultural Land
- Figure 6.4: Agricultural Land Estimate

### Chapter 7 (Conclusion)
- Figure 7.1: Eighth Campaign Reconstructions (Zimansky 1990)
- Figure 7.3: Muṣaṣir Relief (Left)
- Figure 7.6: Muṣaṣir Relief (Center)
- Figure 7.8: Muṣaṣir Relief (Right)
- Figure 7.10: Bronze Model City

---

## Missing Figures (27 Total)

### Chapter 1
- 1.1: Map of District of Soran
- 1.2: Map of RAP Project Area

### Chapter 2
- 2.1: Kelishin Stele
- 2.3: Geneology of Sorani Rulers

### Chapter 4
- 4.2: Full Gund-i Topzawa Section
- 4.12: Plan of Building 1-E
- 4.13: Interior of Building 1E
- 4.14: Building 1-E South Facing Section
- 4.15: Radiocarbon Dates
- 4.16: Tau Model
- 4.18: Room 2 Objects
- 4.19: Room 3 Objects
- 4.22: Burial Objects
- 4.23: Metal Burial Goods
- 4.24: Beads

### Chapter 5
- 5.3: Sidekan Area Survey Sites
- 5.4: Mudjesir Area Sites

### Chapter 7
- 7.2: Sargon II Route
- 7.4: Sennarcherib's Destruction of Ukku (Room I)
- 7.5: Sennarcherib's Destruction of Ukku (Room XLVIII)
- 7.7: Ground Plans of Urartian Susi Temples
- 7.9: Adilcevaz Relief
- 7.11: Altintepe Temple Reconstruction
- 7.12: Four Reconstructions of susi Temple
- 7.13: 3D Reconstruction of Susi Temple
- 7.14: Kleiss Reconstruction
- 7.15: Overlaid Susi Design

---

## How to Add Missing Figures
1. Locate the image file in `project_assets/images/dissertation/By_Chapter/`
2. Open `enhanced_figure_mapping.json`
3. Add an entry under the correct chapter number:
   ```json
   "4.18": {
     "source_file": "AnnotatedImages/filename.jpg",
     "caption": "Exact title if different from text"
   }
   ```
4. Run: `python3 final_figure_integration.py`
