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

# Treatment

```python
import pandas
from waste_flow.treatment import waste_trt
with pandas.option_context('display.min_rows', 10, 'display.max_rows', 10):
    display(waste_trt.df)
```

# Check waste categories avail

```python
from waste_flow.mappings  import wastes_selected
from waste_flow.treatment import waste_trt

wastes_avail = waste_trt.df.waste.unique()
print(set(wastes_selected) - set(wastes_avail))
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

```python

```

```python

```
