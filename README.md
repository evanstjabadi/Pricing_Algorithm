# Pricing_Algorithm

This repo was created to host the numeric simulation codes developed in python during my final year research project.

The folder "Numeric Simulations" has subfolders according to the different development:

1. "Partial" folder:
Partial effect of arrival rate (demand) and remaining resources (supply) were analysed individually and the relevent python files.

2. "Full 2D and 3D Price Update Function" folder..
...contains the numeric simulation for the 3D ("full3dpricefunction.py") and 2D ("full2dpricefunction.py") price map to arrival rate and to remaining resource. Random calls were generated in "random.py" and the revenue from the calls was calculated in the "revenue.py"


3. "Effect_Comparison" folder:
The "effect.py" analyses the effect of capacity. 
"linear.py" compares this function with linear schemes
"compare_price.py" compares this price update function to literature paper.
"exponentail.py" compares this price update function to exponential method.


4. "Sensitivity" folder:
User price sensitivity was used with price to form a feedback loop congestion control
"sensitivity.py" shows analyses how typical data is modified to adhere to effect of acceptance to pricing.

