1. chart 
import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

fig = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization", fontsize=10)

data = io.BytesIO()
plt.savefig(data)
image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Sample Visualization"
display.display(display.Markdown(F"![{alt}]({image})"))
plt.close(fig)

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/2b032e96-9eaa-4adf-b56c-4b2c62c471ac" />

## Technologies Used
- Python 3.9
- Pandas & NumPy
- BioPython

## Usage
To run the analysis script:
```bash
python data_analysis.py --input data.csv


Contact
Roman Lupashin - [[LinkedIn Profile Link](https://www.linkedin.com/in/roman-lupashin-4885a9330/)]
