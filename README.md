# Household Battery Storage Capacity Calculator

## Introduction

Household Battery Storage is becoming increasingly important in the modern energy landscape, providing numerous advantages such as:

- **Energy Independence:** Allows households to generate and store their own electricity.
- **Self-Sufficiency:** Enhances self-sufficiency by reducing dependence on external energy sources.
- **Cost Savings:** Reduces reliance on grid electricity during peak hours, saving money.
- **Environmental Impact:** Promotes the use of renewable energy sources and lowers carbon footprint.
- **Grid Support:** Can contribute excess energy back to the grid, supporting overall grid stability.

Determining the optimal capacity for battery storage is crucial for maximizing these benefits. This tool aims to assist users in calculating the optimal storage capacity based on various parameters.

## About the Tool
<p align="justify"> The Household Battery Storage Capacity Calculator is a Python application based on an **OEMOF Storage_Investment optimization model**, meticulously crafted to assist homeowners and installers in estimating the capacity of battery storage systems within households. This tool serves as a valuable asset, simplifying decision-making processes by providing comprehensive insights into energy distribution, financial analysis, and determining the optimal storage capacity. Whether you are planning to enhance energy independence, reduce costs, or contribute to environmental sustainability, this calculator empowers users to make informed choices by customizing parameters to suit their unique needs and preferences. </p>

![BESS_GUI_Tool](Input_Files/GUI_Tool_image.png)

## Environment and Dependencies

To set up the environment for running the tool, follow these steps:

1. **Create New Environment**

2. **Install Dependencies:**
   
    ```bash
    pip install oemof.solph
    pip install PyQt5
    pip install pandas
    pip install plotly
    ```
<p align="justify">For running an oemof-solph optimisation model, you need to install a solver. Following you will find guidelines for the detailed installation process for different operating systems. https://oemof-solph.readthedocs.io/en/stable/readme.html#contents</p>

3. **Clone the Repository:**
    ```bash
    git clone https://github.com/Jayasurya-Vardhan/Storage_optimization_Tool.git
    ```

4. **Run the Application:**


## Contributions

Any kind of contributions to the project are welcome! If you would like to contribute, please follow these guidelines:

- Fork the repository and create a new branch for your feature or bug fix.
- Make your changes and submit a pull request.
- Provide a clear and detailed description of your changes.

Thank you for considering contributing to the Household Battery Storage Capacity Calculator!

## Citation

If you find this tool helpful in your work, please consider citing the following:

```
@software{GUI: Optimal Home Storage Calculator,
  author={Jayasurya Vardhan, Pujari},
  url={https://github.com/Jayasurya-Vardhan/Storage_optimization_Tool},
  year={2024},
  note={Accessed: Date},
  version={1.0},
}
```