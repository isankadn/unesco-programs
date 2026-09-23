# Graph Report - /home/dev/workbench/unesco/src/unesco-programs  (2026-05-30)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 32 nodes · 31 edges · 12 communities (6 shown, 6 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]

## God Nodes (most connected - your core abstractions)
1. `UnescoProgram` - 8 edges
2. `UnescoProgramForm` - 5 edges
3. `Meta` - 2 edges
4. `add_program()` - 2 edges
5. `edit_program()` - 2 edges
6. `UnescoProgramAdmin` - 2 edges
7. `Meta` - 1 edges
8. `Migration` - 1 edges
9. `Migration` - 1 edges
10. `Migration` - 1 edges

## Surprising Connections (you probably didn't know these)
- `UnescoProgramForm` --uses--> `UnescoProgram`  [INFERRED]
  unesco_programs/forms.py → unesco_programs/models.py
- `Meta` --uses--> `UnescoProgram`  [INFERRED]
  unesco_programs/forms.py → unesco_programs/models.py
- `UnescoProgramAdmin` --uses--> `UnescoProgram`  [INFERRED]
  unesco_programs/admin.py → unesco_programs/models.py
- `add_program()` --calls--> `UnescoProgramForm`  [EXTRACTED]
  unesco_programs/views.py → unesco_programs/forms.py
- `edit_program()` --calls--> `UnescoProgramForm`  [EXTRACTED]
  unesco_programs/views.py → unesco_programs/forms.py

## Communities (12 total, 6 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.39
Nodes (4): UnescoProgramAdmin, Meta, Meta, UnescoProgram

### Community 1 - "Community 1"
Cohesion: 0.47
Nodes (3): UnescoProgramForm, add_program(), edit_program()

## Knowledge Gaps
- **7 isolated node(s):** `Meta`, `Migration`, `Migration`, `Migration`, `Migration` (+2 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnescoProgram` connect `Community 0` to `Community 1`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Why does `UnescoProgramForm` connect `Community 1` to `Community 0`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `UnescoProgram` (e.g. with `UnescoProgramAdmin` and `Meta`) actually correct?**
  _`UnescoProgram` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Meta`, `Migration`, `Migration` to the rest of the system?**
  _7 weakly-connected nodes found - possible documentation gaps or missing edges._