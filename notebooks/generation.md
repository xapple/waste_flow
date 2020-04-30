---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Generation

```python
import pandas
from waste_flow.generation import waste_gen
with pandas.option_context('display.min_rows', 10, 'display.max_rows', 10):
    display(waste_gen.df)
```

# Check waste categories avail

```python
from waste_flow.mappings   import wastes_selected
from waste_flow.generation import waste_gen

wastes_avail = waste_gen.df.waste.unique()
print(set(wastes_selected) - set(wastes_avail))
```

# Check nace categories

```python
from waste_flow.mappings   import nace_selected
from waste_flow.generation import waste_gen

nace_avail = waste_gen.df.nace_r2.unique()
print(len(nace_avail))
print(len(nace_selected))
print(set(nace_selected) - set(nace_avail))
```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```
