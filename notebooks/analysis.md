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

```python
import waste_flow
```

# Check totals

```python
# Import #
from matplotlib import pyplot
import seaborn
import pandas
from waste_flow.treatment  import waste_trt
from waste_flow.generation import waste_gen

# Process #
gen = waste_gen.long_format
trt = waste_trt.long_format
gen = gen.groupby(['country', 'year', 'waste'])
trt = trt.groupby(['country', 'year', 'waste'])
gen = gen.aggregate({'tonnes': 'sum'})
trt = trt.aggregate({'tonnes': 'sum'})

# Join #
df = gen.left_join(trt, lsuffix='_gen', rsuffix='_trt')

# Remove zeros #
df = df.query('tonnes_gen != 0.0')
df = df.query('tonnes_trt != 0.0')

# Compute discrepency both directions #
df['discrep_trt'] = df['tonnes_gen'] / df['tonnes_trt']
df['discrep_gen'] = df['tonnes_trt'] / df['tonnes_gen']

# Keep each positive direction #
#df.loc[df['discrep_trt'] <= 1.0, 'discrep_trt'] = 0.0
#df.loc[df['discrep_gen'] <= 1.0, 'discrep_gen'] = 0.0
#df['discrep'] = df['discrep_trt'] + df['discrep_gen']

# Filter large values #
#df = df.query('discrep < 10')

# Print #
#print(max(df['discrep_trt']))
#print(min(df['discrep_trt']))

# Plot #
#display(pyplot.hist(df['discrep_trt']))

# Filter large values #
df = df.query('discrep_trt < 10')

# Plot #
seaborn.distplot(df['discrep_trt'])

# Display #
with pandas.option_context('display.min_rows', 20, 'display.max_rows', 20):
    display(df)

```

# Combine

```python
# Import #
import pandas
from waste_flow.treatment  import waste_trt
from waste_flow.generation import waste_gen

# Process #
gen = waste_gen.long_format
trt = waste_trt.normalized
df  = gen.left_join(trt, on = ['country', 'year', 'waste'])

# Display #
with pandas.option_context('display.min_rows', 10, 'display.max_rows', 10):
    display(df)
```

# Combine package version

```python
# Import #
import pandas
from waste_flow.analysis import waste_ana

# Process #
df = waste_ana.combined

# Display #
with pandas.option_context('display.min_rows', 20, 'display.max_rows', 20):
    display(df)
```

# In kilograms

```python
# Import #
import pandas
from waste_flow.analysis import waste_ana

# Process #
df = waste_ana.kilograms

# Display #
with pandas.option_context('display.min_rows', 20, 'display.max_rows', 20):
    display(df)
```

# Spread into new waste categories

```python
# Custom page width #
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

# Custom number printing #
import pandas
pandas.options.display.float_format = '{:.0f}'.format

# Import #
from waste_flow.analysis import waste_ana

# Process #
df = waste_ana.spread_waste

# Filter #
result = df.query('country == "EU28"')
result = result.query('year == "2010"')

# Display #
with pandas.option_context('display.min_rows', 100, 'display.max_rows', 100):
    display(result)
```

# Dry weight

```python
# Custom number printing #
import pandas
pandas.options.display.float_format = '{:.0f}'.format

# Import #
import pandas
from waste_flow.analysis import waste_ana

# Process #
df = waste_ana.dry_mass

# Filter #
result = df.query('country == "EU28"')
result = result.query('year == "2010"')

# Display #
with pandas.option_context('display.min_rows', 100, 'display.max_rows', 100):
    display(result)
```

# Dry Long Format

```python
# Custom number printing #
import pandas
pandas.options.display.float_format = '{:.0f}'.format

# Import #
import pandas
from waste_flow.analysis import waste_ana

# Process #
df = waste_ana.dry_long

# Filter #
result = df.query('country == "EU28"')
result = result.query('year == "2010"')

# Display #
with pandas.option_context('display.min_rows', 100, 'display.max_rows', 100):
    display(result)
```

# Collapse industrial

```python
# Custom number printing #
import pandas
pandas.options.display.float_format = '{:.0f}'.format

# Import #
import pandas
from waste_flow.analysis import waste_ana

# Process #
df = waste_ana.collapse_ind

# Filter #
result = df.query('country == "EU28"')
result = result.query('year == "2010"')

# Display #
with pandas.option_context('display.min_rows', 100, 'display.max_rows', 100):
    display(result)
```

# Collapse industrial wide

```python
# Custom number printing #
import pandas
pandas.options.display.float_format = '{:.0f}'.format

# Import #
import pandas
from waste_flow.analysis import waste_ana

# Process #
df = waste_ana.wide_format

# Filter #
result = df.query('country == "EU28"')
result = result.query('year == "2010"')

# Display #
with pandas.option_context('display.min_rows', 100, 'display.max_rows', 100):
    display(result)
```

# Test dropping levels

```python
# Import #
import pandas
from waste_flow.analysis import waste_ana

# Process #
df = waste_ana.wide_format.copy()

# Reorder #
df = df.sort_index(level=2, ascending=False)

# Filter #
result = df.query('country == "EU28"')
result = result.query('year == "2010"')

# Display #
with pandas.option_context('display.min_rows', 100, 'display.max_rows', 100):
    display(result)
```

```python

```
