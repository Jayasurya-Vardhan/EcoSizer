# EcoSizer: Optimal Home Solar + Battery Sizing Tool

## Introduction

Household PV and Battery Storage Systems are becoming increasingly important in the modern energy landscape, providing numerous advantages such as:

- **Self-Consumption:** Maximizes direct use of energy produced by your own PV system.
- **Self-Sufficiency:** Enhances self-sufficiency by reducing dependence on external energy sources.
- **Energy Independence:** Allows households to generate and store their own electricity.
- **Cost Savings:** Reduces reliance on grid electricity during peak hours, saving money.
- **Environmental Impact:** Promotes the use of renewable energy sources and lowers carbon footprint.
- **Grid Support:** Can contribute excess energy back to the grid, supporting overall grid stability.

## Importance of Optimal Sizing

Determining the optimal capacities is crucial for maximizing these benefits. This tool aims to assist users in calculating the optimal PV+BESS and only storage capacity based on various parameters.

  - Maximizing Benefits: Optimal sizing ensures that PV, battery energy storage systems (BESS), and other components operate  efficiently, maximizing benefits such as energy independence and cost savings.

  - Avoiding Wastage: Inadequate sizing can lead to energy wastage and increased operational costs. Optimal sizing helps avoid unnecessary resource use and financial expenditures.

  - Reliable Energy Supply: A carefully sized system guarantees a reliable energy supply. An oversized system can meet demand, while an undersized one may lead to insufficient electricity supply. Achieving optimal benefits requires a balance in system sizing [[11]].

## About the Tool

<p align="justify"> The EcoSizer is a Python application offering two distinct tools tailored to meet specific needs. Firstly, it includes an OEMOF Storage_Investment optimization model designed for homeowners and installers aiming to estimate the optimal battery storage capacity for an existing PV system. Secondly, for those planning a new setup, the tool assists in determining the optimal capacities for both PV and BESS within households. This comprehensive solution simplifies decision-making by providing insights into energy distribution, financial analysis, and the most efficient capacities for solar and battery storage.</p>

<p align="justify"> Whether your goal is to enhance energy independence, reduce costs, or contribute to environmental sustainability, this calculator empowers users to make informed choices. It allows for customization of parameters to suit unique needs and preferences, ensuring a tailored solution for each user.</p>

Key Features:

- Estimate optimal battery capacity for an existing PV system.
![BESS_GUI_Tool](Input_Files/BESS_GUI_tool.png)

- Determine optimal capacities for both PV and BESS in new household setups.
![BESS_GUI_Tool](Input_Files/PV_BESS_GUI_tool.png)


Limitations:

- Maximum PV capacity considered is up to 30 kWp, catering to typical household scenarios.
- The PV feed-in profile is based on the location from the central part of Germany, impacting the tool's accuracy in regions with      significantly different solar profiles.


## Environment and Dependencies

To set up the environment for running the tool, follow these steps:

1. **Create New Environment**
    Creating a new environment is a good practice to manage dependencies and isolate your project. THe following link helps you with all the steps in order to create a new environment: https://realpython.com/python-virtual-environments-a-primer/

2. **Install Dependencies:**
   
    ```bash
    pip install oemof.solph
    pip install PyQt5
    pip install pandas
    pip install plotly
    ```
    To make the oemof-solph optimization model work, you need to set up a solver. The steps for installing this solver vary depending on the type of computer you're using. Here's a guide to help you through the installation process on different operating systems. https://oemof-solph.readthedocs.io/en/stable/readme.html#contents or https://youtu.be/eFvoM36_szM?si=3pRmnGV7J129kBKo

3. **Clone the Repository:**
    ```bash
    git clone https://github.com/Jayasurya-Vardhan/Storage_optimization_Tool.git
    ```

4. **Run the Application:**
     ```bash
    PV_BESS_GUI.py
    BESS_GUI.py
    ```

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

@software{oemof.solph—A model generator for linear and mixed-integer linear optimisation of energy systems,
  author={Uwe Krien, Patrik Schönfeldt, Jann Launer, Simon Hilpert, Cord Kaldemeyer, Guido Pleßmann},
  url={https://oemof-solph.readthedocs.io/en/latest/readme.html},
  year={2020}
}

```


<!-- ## Importance of Optimal Sizing

Determining the optimal capacities is crucial for maximizing these benefits. This tool aims to assist users in calculating the optimal PV+BESS and only storage capacity based on various parameters. -->




<!-- 
<p align="justify"> The EcoSizer is a Python application based on an OEMOF Storage_Investment optimization model, meticulously crafted to assist Homeowners and Installers in estimating the capacity of Solar and battery storage systems within households. This tool serves as a valuable asset, simplifying decision-making processes by providing comprehensive insights into energy distribution, financial analysis, and determining the optimal capacities. Whether you are planning to enhance energy independence, reduce costs, or contribute to environmental sustainability, this calculator empowers users to make informed choices by customizing parameters to suit their unique needs and preferences. </p>\n -->