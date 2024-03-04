# EcoSizer: Optimal Home Solar + Battery Sizing Tool

## Introduction

Household PV and Battery Storage Systems are becoming increasingly important in the modern energy landscape, providing numerous advantages such as:

- **Self-Consumption:** Use more of the clean energy you generate directly, reducing your reliance on the grid.
- **Become Energy Independent:** Generate and store your own electricity, increasing self-sufficiency.
- **Save Money on Electricity Bills:** Reduce reliance on expensive grid power, especially during peak hours.
- **Reduce Your Environmental Impact:** Generate clean energy and lower your carbon footprint.
- **Support a Stable Grid:** Contribute excess energy back to the grid, benefiting everyone.

## Importance of Optimal Sizing

Determining the optimal capacities is crucial for maximizing these benefits. This tool aims to assist users in calculating the optimal PV+BESS and only storage capacity based on various parameters.

  - Maximizing Benefits: Optimal sizing ensures that PV, battery energy storage systems (BESS), and other components operate  efficiently, maximizing benefits such as energy independence and cost savings.

  - Avoiding Wastage: Inadequate sizing can lead to energy wastage and increased operational costs. Optimal sizing helps avoid unnecessary resource use and financial expenditures.

  - Reliable Energy Supply: A carefully sized system guarantees a reliable energy supply. An oversized system can meet demand, while an undersized one may lead to insufficient electricity supply. Achieving optimal benefits requires a balance in system sizing.

## About the Tool

<p align="justify"> The EcoSizer is a Python application offering two distinct tools tailored to meet specific needs. It is completely based on an OEMOF Investment Optimization model designed for homeowners and installers aiming to estimate the optimal battery storage capacity for an existing PV system. Secondly, for those planning a new setup, the tool also assists in determining the optimal capacities for both PV and BESS within households. This comprehensive solution simplifies decision-making by providing insights into energy distribution, financial analysis, and the most efficient capacities for solar and battery storage.</p>

<p align="justify"> Whether your goal is to enhance energy independence, reduce costs, or contribute to environmental sustainability, this calculator empowers users to make informed choices. It allows for customization of parameters to suit unique needs and preferences, ensuring a tailored solution for each user.</p>

**Key Features:**


*EcoSizer Storage*

- Determines optimal battery capacity for an existing PV system.
![BESS_GUI_Tool](Input_Files/BESS_GUI_tool.png)


*EcoSizer SunVault*

- Determines optimal capacities for both PV and BESS in new household setups.
![BESS_GUI_Tool](Input_Files/PV_BESS_GUI_tool.png)


**Limitations:**

- Maximum PV capacity considered is up to 30 kWp, catering to typical household scenarios.
- The PV feed-in profile is based on the location from the central part of Germany, impacting the tool's accuracy in regions with      significantly different solar profiles.
- For Energy demand a standard Household BDEW Profile is used. 
- In the PV+BESS model, the maximum PV capacity is dependent on the feed-in tariff (FiT). If FiT is 8 and above, the maximum capacity is 10 kWp; otherwise, it is capped at 30 kWp, following amendments to the EEG considering partial feed-in.
- The tool assumes a system lifetime of 25 years for PV and 10 years for Battery Storage.
- The battery efficiency is set at 95% in the calculations.
- The tool is set to use "GLPK" solver for optimization and the solver settings are currently compatible only with Windows. This restricts usage for users on macOS and Linux systems.


## Download Tool

If you don't have a programming background, no worries! We've prepared a user-friendly version of EcoSizer for you. Simply click the link below and download the file EcoSizer.zip:

[Click here to download EcoSizer](https://github.com/Jayasurya-Vardhan/EcoSizer/releases)

**Note:** 

- Before using the application, make sure to read the [EcoSizer_User_Guide](https://github.com/Jayasurya-Vardhan/EcoSizer/blob/main/EcoSizer_User_Guide.pdf) for clear instructions on how to operate the tools effectively.
- The application will be updated and released as a new version when a major new feature is introduced that enhances functionality or user experience.

## Environment and Dependencies

To set up the environment for running the tool, follow these steps:

1. **Create New Environment:**

    Creating a new environment is a good practice to manage dependencies and isolate your project. THe following link helps you with all the steps in order to create a new environment: https://realpython.com/python-virtual-environments-a-primer/

2. **Install Dependencies:**
   
    ```bash
    pip install oemof.solph = 0.5.2
    pip install PyQt5
    pip install plotly
    ```
    To make the oemof-solph optimization model work, you need to set up a solver. The steps for installing this solver vary depending on the system type you're using. Here's a guide to help you through the installation process on different operating systems. https://oemof-solph.readthedocs.io/en/stable/readme.html#contents or https://youtu.be/eFvoM36_szM?si=3pRmnGV7J129kBKo

3. **Clone the Repository:**
    ```bash
    git clone https://github.com/Jayasurya-Vardhan/EcoSizer.git
    ```

4. **Run the Application:**
     ```bash
    PV_BESS_GUI.py
    BESS_GUI.py
    ```

## Contributions

Any kind of contributions to the project are welcome! This can help in enhancing the tool and make it more user-friendly. If you would like to contribute, please follow these guidelines:

- Fork the repository and create a new branch for your feature or bug fix.
- Make your changes and submit a pull request.
- Provide a clear and detailed description of your changes.

Thank you for considering contributing to the EcoSizer!

## Citation

If you find this tool helpful in your work, please consider citing the following:

```
@software{EcoSizer: Optimal Home Solar + Battery Sizing Tool,
  author={Jayasurya Vardhan, Pujari},
  url={https://github.com/Jayasurya-Vardhan/EcoSizer.git},
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
