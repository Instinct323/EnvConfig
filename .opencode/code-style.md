# Code Style Report: ModelsAPI

## Overview
This document describes the coding style used in the ModelsAPI project (`/media/tongzj/Data/Workbench/ModelsAPI`). Use this as a reference when contributing or extending the codebase.

---

## 1. Variable Naming

### Conventions
- **Short names** for common objects: `pcd` (point cloud), `pc` (point cloud), `cfg` (config), `req` (request), `fp` (footprint), `T` (transform), `R` (rotation), `vec` (vector)
- **Descriptive names** for domain concepts: `Tcw` (camera to world), `Teb` (end effector to base), `len_finger`, `radius_mesh`
- **Underscore separated**: `axis_aligned_bounding_box`, `pointcloud`, `grasp_direction`

### Examples
```python
# Short names
pcd = o3d.geometry.PointCloud()
cfg = yaml.safe_load(f)
req = PlacementRequest()

# Transforms
Tcw = np.eye(4)  # camera to world
Teb = np.eye(4)  # end effector to base

# Descriptive
len_finger = 0.05
radius_mesh = 0.002
```

---

## 2. Comments

### Style
- **English only**
- **Minimal and functional**
- **One-line** for simple explanations
- **No obvious comments** (e.g., `# increment i` is unnecessary)

### Examples
```python
# Good
def solve_v2v(vec1, vec2):
    """ Solve the transformation matrix from vec2 to vec1 """

# Good - explains non-obvious behavior
Sxx, Sxy, Sxz, Syx, Syy, Syz, Szx, Szy, Szz = (pcd1.T @ pcd2).flatten()

# Avoid
i += 1  # increment i
```

---

## 3. Function/Class Organization

### Principles
- **Small functions**: Each function does one thing
- **Clear inputs/outputs**: Type hints on parameters and returns
- **No deep nesting**: Max 2-3 levels

### Structure
```python
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    """ Short one-line description. """
    # Core logic
    return result
```

---

## 4. Type Hints

### Usage
- Use but **not verbose**
- Common types: `List`, `Tuple`, `Optional`, `np.ndarray`, `o3d.geometry.PointCloud`

### Examples
```python
# Good
def create_arrow(start: np.ndarray, end: np.ndarray, radius: float = 0.002) -> o3d.geometry.TriangleMesh:

# Good - simple types
def ball_query(pcd: np.ndarray, center: np.ndarray, r: float) -> np.ndarray:

# Avoid over-specifying
# Bad: Dict[str, List[Tuple[int, Optional[float]]]]
```

---

## 5. Import Patterns

### Organization
```python
from __future__ import annotations

# Standard library
import itertools
from dataclasses import dataclass
from pathlib import Path

# Third party
import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d
import sklearn
import trimesh
import yaml

# Local
from . import o3d_extension as o3de
from .pose_tf import solve_v2v
```

### Aliases
- `o3d` for open3d
- `np` for numpy
- `o3de` for o3d_extension (when needed)

---

## 6. Error Handling

### Patterns
- Use `assert` for internal checks
- Raise `NotImplementedError` for unsupported features
- Simple error messages

### Examples
```python
# Assertion for internal checks
assert pcd1.shape[-1] == 3 and pcd1.size == pcd2.size

# Not implemented
raise NotImplementedError(f"Method {method} is not implemented.")

# Simple error
if method not in ("sim3", "se3"):
    raise ValueError(f"Invalid method: {method}")
```

---

## 7. Dataclass Usage

### When to Use
- Simple data containers with no logic
- Grouping related parameters

### Examples
```python
from dataclasses import dataclass

@dataclass
class TwoFingerGripper:
    len_finger: float
    len_handle: float
    radius_mesh: float
    
    def __post_init__(self):
        # Initialize derived values
        self._connection = np.array([...])
```

---

## 8. Code Layout

### File Structure
```python
# 1. Future imports
from __future__ import annotations

# 2. Standard library
import ...

# 3. Third party
import ...

# 4. Local
from . import ...

# 5. Constants (if any)
CONSTANT = 100

# 6. Functions and classes
def function1():
    ...

def function2():
    ...

class Class1:
    ...
```

### Line Spacing
- 2 blank lines between top-level definitions
- 1 blank line between methods in class

---

## 9. Naming Conventions Summary

| Type | Convention | Example |
|------|------------|---------|
| Variables | snake_case, short | `pcd`, `cfg`, `Tcw` |
| Functions | snake_case | `solve_v2v`, `ball_query` |
| Classes | PascalCase | `TwoFingerGripper`, `ShelfManager` |
| Constants | UPPER_SNAKE | `MAX_RESULTS = 10` |
| Private | _leading_underscore | `_compute_pos` |

---

## 10. Anti-Patterns to Avoid

1. **Chinese comments** - Use English only
2. **Verbose names** - `point_cloud_data` → `pcd`
3. **Redundant comments** - `# iterate over items` → just write `for item in items:`
4. **Deep nesting** - If >3 levels, extract to function
5. **Magic numbers** - Use named constants
6. **Long parameter lists** - Use dataclass or configuration object

---

## Reference Files

- `/media/tongzj/Data/Workbench/ModelsAPI/api/utils/o3d_extension.py` - Open3D utilities
- `/media/tongzj/Data/Workbench/ModelsAPI/api/utils/pose_tf.py` - Pose transformations
- `/media/tongzj/Data/Workbench/ModelsAPI/api/utils/grasp_pose.py` - Grasp definitions