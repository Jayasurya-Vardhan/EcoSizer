"""
EnergyModelApp Module

This module defines the EnergyModelApp class, which represents the main application window
for the Household Battery Storage Capacity Calculator. The application includes sections for
configuring parameters, displaying optimal storage capacity, visualizing energy distribution,
and performing financial analysis.

The module contains the following components:
- EnergyModelApp class: The main application window with various sections.
- Functions for handling simulation, updating costs, and saving financial analysis reports.

Usage:
1. Import the EnergyModelApp class from this module.
2. Create an instance of EnergyModelApp to run the application.

"""


import sys
import logging
import pprint as pp
import pandas as pd
from PyQt5.QtWidgets import (QApplication, QGroupBox, QListWidget, QVBoxLayout, QTableWidget,
                             QLabel, QWidget, QHBoxLayout, QPushButton, QLineEdit, QFileDialog,
                             QSlider, QGridLayout, QSplitter, QTableWidgetItem)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5 import QtCore, QtPrintSupport
from oemof.tools import logger
from oemof.tools import economics
from oemof import solph
import plotly.graph_objects as go
from plotly.subplots import make_subplots



class EnergyModelApp(QWidget): 
    """
    Main application window for the Household Battery Storage Capacity Calculator.

    This class defines the user interface with various sections for configuring 
    parameters, displaying optimal storage capacity, visualizing energy distribution, 
    and performing financial analysis.

    """
    def init_ui(self):
        self.setWindowTitle('EcoSizer: Optimal Home Solar + Battery Sizing Tool')
        self.setGeometry(100, 100, 1600, 920)

        # Create a splitter to divide the main window into three sections
        splitter = QSplitter(QtCore.Qt.Horizontal)

        # Create three child widgets(left, center, right) within the main window 
        self.left_widget = QWidget()
        self.center_widget = QWidget()
        self.right_widget = QWidget()
        
        
        ######################################################################################
        # COnfigure Parameters Section
        ######################################################################################
        
        # Create Groupbox widget for parameters section with title
        #========================================================#
        self.parameters = QGroupBox('Configure Parameters',self)
        self.parameters.setStyleSheet("QGroupBox {color: white; font-size: 16px}")
        configure_parameters_layout = QVBoxLayout(self.parameters) # vertical layout to set items in this section
        
        
        # Create buttons Widget
        #=====================#
        self.btn_run_simulation = QPushButton('Run Simulation',self, styleSheet="background-color:sandybrown ;color:black")
        self.btn_run_simulation.setFixedSize(160, 30)
        self.btn_run_simulation.setCheckable(True)
        self.btn_run_simulation.clicked.connect(self.toggle)
        
        
        # Create Sliders with Labels and Input Fields
        #============================================#
        self.label_PV_Capex = QLabel('PV CAPEX (500-2500 €/kWp):')
        self.input_PV_Capex = QSlider(QtCore.Qt.Horizontal, self)
        self.input_PV_Capex.setRange(5, 25)
        self.input_PV_Capex.setTickPosition(QSlider.TicksBelow)
        self.input_PV_Capex.setTickInterval(2)
        self.label_PVCapex_value = QLabel('500')  # Display current value
        self.input_PV_Capex.sliderMoved.connect(lambda value: self.label_PVCapex_value.setText(str(value*100)))
        
        self.label_BESS_Capex = QLabel('BESS CAPEX (300-1500 €/kWh):')
        self.input_BESS_Capex = QSlider(QtCore.Qt.Horizontal, self)
        self.input_BESS_Capex.setRange(3, 15)
        self.input_BESS_Capex.setTickPosition(QSlider.TicksBelow)
        self.input_BESS_Capex.setTickInterval(2)
        self.label_BESSCapex_value = QLabel('300')  # Display current value
        self.input_BESS_Capex.sliderMoved.connect(lambda value: self.label_BESSCapex_value.setText(str(value*100)))
        
        self.label_electricity_price = QLabel('Electricity Price (1-100 €-cents/kWh):')
        self.input_electricity_price = QSlider(QtCore.Qt.Horizontal, self)
        self.input_electricity_price.setRange(0, 100)
        self.input_electricity_price.setTickPosition(QSlider.TicksBelow)
        self.input_electricity_price.setTickInterval(10)
        self.label_electricity_value = QLabel('0')  # Display current value
        self.input_electricity_price.valueChanged.connect(lambda value: self.label_electricity_value.setText(str(value)))

        self.label_feedin_price = QLabel('Feed-in Tariff (1-20 €-cents/kWh):')
        self.input_feedin_price = QSlider(QtCore.Qt.Horizontal, self)
        self.input_feedin_price.setRange(0, 20)
        self.input_feedin_price.setTickPosition(QSlider.TicksBelow)
        self.input_feedin_price.setTickInterval(2)
        self.label_feedin_value = QLabel('0')  # Display current value
        self.input_feedin_price.valueChanged.connect(lambda value: self.label_feedin_value.setText(str(value)))

        self.label_pv_existing_capacity = QLabel('PV System Capacity (1-30 kWp):')
        self.input_pv_existing_capacity = QSlider(QtCore.Qt.Horizontal, self)
        self.input_pv_existing_capacity.setRange(0, 30)
        self.input_pv_existing_capacity.setTickPosition(QSlider.TicksBelow)
        self.input_pv_existing_capacity.setTickInterval(2)
        self.label_pv_existing_value = QLabel('0')  # Display current value
        self.input_pv_existing_capacity.valueChanged.connect(lambda value: self.label_pv_existing_value.setText(str(value)))

        self.label_demand = QLabel('Demand (1000-20000 kWh/Yr):')
        self.input_demand = QSlider(QtCore.Qt.Horizontal, self)
        self.input_demand.setRange(0, 20)
        self.input_demand.setTickPosition(QSlider.TicksBelow)
        self.input_demand.setTickInterval(2)
        self.label_demand_value = QLabel('0')  # Display current value
        self.input_demand.valueChanged.connect(lambda value: self.label_demand_value.setText(str(value*1000)))
        
  
        # Create a Listwidget to set sliders with a vertical layout
        #=========================================================#
        self.sliders_widget = QListWidget(self, styleSheet="background-color:LemonChiffon") 
        sliders_layout = QVBoxLayout(self.sliders_widget)
        
        # Add created sliders, labels and button to the layout
        sliders_layout.addWidget(self.label_PV_Capex)
        sliders_layout.addWidget(self.input_PV_Capex)
        sliders_layout.addWidget(self.label_PVCapex_value)
        sliders_layout.addWidget(self.label_BESS_Capex)
        sliders_layout.addWidget(self.input_BESS_Capex)
        sliders_layout.addWidget(self.label_BESSCapex_value)
        sliders_layout.addWidget(self.label_electricity_price)
        sliders_layout.addWidget(self.input_electricity_price)
        sliders_layout.addWidget(self.label_electricity_value)
        sliders_layout.addWidget(self.label_feedin_price)
        sliders_layout.addWidget(self.input_feedin_price)
        sliders_layout.addWidget(self.label_feedin_value)  # Add label for displaying current value
        sliders_layout.addWidget(self.label_pv_existing_capacity)
        sliders_layout.addWidget(self.input_pv_existing_capacity)
        sliders_layout.addWidget(self.label_pv_existing_value)  # Add label for displaying current value
        sliders_layout.addWidget(self.label_demand)
        sliders_layout.addWidget(self.input_demand)
        sliders_layout.addWidget(self.label_demand_value)  # Add label for displaying current value
        sliders_layout.addWidget(self.btn_run_simulation, alignment=QtCore.Qt.AlignCenter)
        
        
        # Now add sliders layout to the configure_parameters layout
        configure_parameters_layout.addWidget(self.sliders_widget)
        
        
        ######################################################################################
        # Optimal Capacity Section
        ######################################################################################
        
        # Create Groupbox Widget for Optimal_values  
        #=========================================#
        self.output_terms = QGroupBox('Optimal Storage Capacity',self)
        self.output_terms.setStyleSheet("QGroupBox {color: white; font-size: 16px}")
        self.output_terms.setFixedHeight(250)
        output_terms_layout = QVBoxLayout(self.output_terms)
        
        # Create a plain Widget to display image and output 
        #=================================================#
        self.outputitems_widget = QWidget(styleSheet="background-color:LemonChiffon")
        outputitems_widget_layout = QGridLayout(self.outputitems_widget)
       
        # Set Icon for Storage
        self.image_Storage = QPixmap("Input_Files/BESS_icon.jpg")
        self.label_Storage = QLabel('Image2')
        self.label_Storage.setPixmap(self.image_Storage)
        
        # create Lineedit widget to display output value
        self.Storage_output = QLineEdit(self)
        self.Storage_output.setFixedSize(200, 100)
        self.Storage_output.setAlignment(QtCore.Qt.AlignCenter)
        self.Storage_output.setStyleSheet("font-weight: bold; font-size: 35px;")
        
        # Add image and output value to outputitems_widget_layout
        outputitems_widget_layout.addWidget(self.label_Storage, 0, 0)
        outputitems_widget_layout.addWidget(self.Storage_output, 0, 1)
        
        # At last add the outputitems_widget to the groupbox layout
        output_terms_layout.addWidget(self.outputitems_widget)
        
        
        ######################################################################################
        # Energy Distribution Section
        ######################################################################################
        
        # Create Groupbox Widget for graphs section 
        #=========================================#
        self.graphs_section = QGroupBox('Energy Distribution Overview', self)
        self.graphs_section.setStyleSheet("QGroupBox {color: white; font-size: 16px}")
        graphs_layout = QVBoxLayout(self.graphs_section)
        
        # Now create a WebEngineView widget to display plotly graphs
        self.grahics_view = QWebEngineView(self)
    
        # Add WebEngineView widget to groupbox layout of graphs section
        graphs_layout.addWidget(self.grahics_view)
        
            
        # Add plotly Figure axes
        self.fig = make_subplots(rows=3, cols=1,   
        specs=[[{"type": "indicator"}],
           [{"type": "indicator"}],
           [{"type": "indicator"}]],
            vertical_spacing = 0.21)
      
    
        ######################################################################################
        # Financial Analysis Section
        ######################################################################################
        
        # Create Groupbox Widget for FinanceAnalysis Section  
        #==================================================#
        self.FinanceAnalysis_section = QGroupBox('Financial Analysis',self)
        self.FinanceAnalysis_section.setStyleSheet("QGroupBox {color: white; font-size: 16px}")
        FinanceAnalysis_layout = QVBoxLayout(self.FinanceAnalysis_section)
        FinanceAnalysis_layout.setSpacing(0)
        
        # Create TableWidget to display Finacial calculations
        #===================================================#
        self.table_widget = QTableWidget(styleSheet="background-color:LemonChiffon ")
        self.table_widget.verticalHeader().setVisible(False)
        
        # Create buttons Widget
        #=====================#
        self.btn_update_costs = QPushButton('Update Report', self, styleSheet="background-color:sandybrown ;color:black")
        self.btn_update_costs.setFixedSize(140, 30)
        self.btn_update_costs.clicked.connect(self.update_costs)
        
        self.btn_export_csv = QPushButton('Save as PDF', self, styleSheet="background-color:sandybrown ;color:black")
        self.btn_export_csv.setFixedSize(140, 30)
        self.btn_export_csv.clicked.connect(self.save_to_pdf)
        
        # Create plainwidget to display and arrange buttons 
        #=================================================#
        self.report_btns_widget = QWidget(self)
        self.report_btns_layout = QHBoxLayout(self.report_btns_widget)
        
        # Add buttons to the widget
        self.report_btns_layout.addWidget(self.btn_update_costs)
        self.report_btns_layout.addWidget(self.btn_export_csv)
        
        # Create Line edit for Disclaimer Text
        #====================================#
        self.Disclaimer_text = QLineEdit(self, styleSheet="background-color:LemonChiffon ;color:black")
        self.Disclaimer_text.setFixedHeight(27)
        # self.Disclaimer_text.setAlignment(QtCore.Qt.AlignCenter)
        
        
        # Add Table and buttons to the groupbox Widget of FinanceAnalysis_section 
        #=======================================================================#
        FinanceAnalysis_layout.addWidget(self.table_widget)
        FinanceAnalysis_layout.addWidget(self.Disclaimer_text)
        FinanceAnalysis_layout.addWidget(self.report_btns_widget)
        

        
        ######################################################################################
        # Child Widgets Layout Section
        ######################################################################################
        
        # Create layouts for each child widget add corresponding widgets to the layout  
        #============================================================================#
        
        # Add widgets to left layout
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.parameters, stretch=2)
        left_layout.addWidget(self.output_terms)
        
        # Add widgets to ccenter layout
        center_layout = QVBoxLayout()
        center_layout.addWidget(self.graphs_section)
        
        # Add widgets to center layout
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.FinanceAnalysis_section)
        
        
        # Now set these Created layouts to the each child widget  
        #======================================================#
        self.left_widget.setLayout(left_layout)
        self.center_widget.setLayout(center_layout)
        self.right_widget.setLayout(right_layout)
    

        ######################################################################################
        # Main Window Layout Section
        ######################################################################################
        
        # Add left, center and right widgets to the splitter
        #==================================================#
        splitter.addWidget(self.left_widget)
        splitter.addWidget(self.center_widget)
        splitter.addWidget(self.right_widget)
        splitter.setSizes([400,500,500]) 

        # Main layout for the entire mainwindow
        main_layout = QHBoxLayout()
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)
        
        # Set stylesheet
        self.setStyleSheet("""
                background-color:Cadetblue ; 
                font-family:Segoe UI;
                font-size: 13px;
                font-weight: Bold;
            """)
        
        # Open Central/Mainwidget to fullscreen
        self.showMaximized() 
        
    #***************************************************End of GUI Tool****************************************#
    
    
    
    #***************************************************Simulation Part****************************************#
    
    # Actions to Perform when the Simulation button clicked
    #======================================================#
    def toggle(self):
        """
        Toggle function for the "Run Simulation" button.

        If the button is checked (pressed), it attempts to execute the 
        `run_simulation` method, updating the simulation results. If an 
        exception occurs during the simulation,it logs the error, updates 
        the button status, and displays an error message.

        If the button is unchecked, it does nothing.

        Returns:
        -------
            None
        """
        if self.btn_run_simulation.isChecked():
            try:
                self.run_simulation()
            except Exception as e:
                logging.error(f"Error during simulation: {e}")
                self.btn_run_simulation.setFixedSize(250, 30)
                self.btn_run_simulation.setText("Simulation Failure due to an error....")
        else:
            pass
    
    # Oemof Simulation Code with plots
    #================================#
    def run_simulation(self):
        """
        Execute the Oemof Simulation Code with plots.

        This method performs the Oemof simulation, optimizing the energy system based 
        on input parameters and simulation results. It includes the following steps:
        1. Initialize the energy system with input parameters.
        2. Create components such as buses, sources, sinks, and storage based on Oemof 
        library.
        3. Optimize the energy system using the Oemof Model.
        4. Extract and print the main simulation results, such as electricity consumption 
        and optimal storage capacity.
        5. Calculate and print special parameters like self-consumption, self-sufficiency, 
        and feed-in percentage.
        6. Generate and display gauge plots representing PV production fed into the grid, 
        self-consumption, and self-sufficiency.

        Note: The method also updates the GUI widgets with the simulation results.

        Returns:
        -------
            None
        """
        
        # Simulation Part
        #================#
        logger.define_logging()
        logging.info('Simulation Started')
        self.btn_run_simulation.setText('Simulating.....') # change status when simulation is running
        QApplication.processEvents()
        
        # read input values from sliders
        self.electricity_price = int(self.input_electricity_price.value())
        self.feedin_price = int(self.input_feedin_price.value())
        self.pv_existing_capacity = int(self.input_pv_existing_capacity.value())
        self.annual_demand = int(self.input_demand.value())
     
        # create datetime index and read input files
        logging.info("Initialize the energy system")
        date_time_index = pd.date_range("1/1/2012", periods=8760, freq="h")
        load_demand = pd.read_csv("Input_Files/Scaled_LP_H0.csv", usecols=['h0'])
        PV_feed = pd.read_csv("Input_Files/Scaled_PV_Feed_in.csv", usecols=['DC_Power','AC_Power'] )

        # Set Epc_Costs
        epc_storage = economics.annuity(capex=int(self.input_BESS_Capex.value()*100), n=10, wacc=0.03)
        energysystem = solph.EnergySystem(timeindex=date_time_index, infer_last_interval= False)

        bel = solph.buses.Bus(label="electricity")

        # create fixed source object representing pv system
        pv = solph.components.Source(
            label="pv",
            outputs={
                bel: solph.Flow(
                    fix=PV_feed['AC_Power'],  
                    nominal_value = self.pv_existing_capacity
                )
            },
        )

        # create simple sink object representing the electrical demand
        demand = solph.components.Sink(
            label="demand",
            inputs={bel: solph.Flow(
                fix=load_demand['h0'],
                nominal_value=self.annual_demand,
            )}
        )

        grid_supply = solph.components.Source(
            label="grid_supply",
            outputs={bel: solph.Flow(variable_costs=self.electricity_price / 100)}
        )

        grid_feed_in = solph.components.Sink(
            label="grid_feed_in",
            inputs={bel: solph.Flow(variable_costs=-self.feedin_price / 100)}
        )

        # create storage object representing a battery
        storage = solph.components.GenericStorage(
            label="storage",
            inputs={bel: solph.Flow()},
            outputs={bel: solph.Flow()},
            balanced=True,
            loss_rate= 0.005,
            invest_relation_input_capacity=1/6,
            invest_relation_output_capacity=1/6,
            inflow_conversion_factor=1,
            outflow_conversion_factor=1,
            investment=solph.Investment(ep_costs=epc_storage),
        )

        energysystem.add(bel, pv, demand, grid_supply, grid_feed_in, storage)

        # Optimise the energy system
        logging.info("Optimise the energy system")
        om = solph.Model(energysystem)

        # if tee_switch is true solver messages will be displayed
        logging.info("Solve the optimization problem")
        om.solve(solver="cbc", solve_kwargs={"tee": False})
        
        # check if the new result object is working for custom components
        results = solph.processing.results(om)
        electricity_bus = solph.views.node(results, "electricity")
        
        # Extract Optimal Capacity
        my_results = electricity_bus["scalars"]
        my_results["storage_invest_KWh"] = (results[(storage, None)]["scalars"]["invest"] )
       
        # Print Results
        print("********* Main results *********")
        print(electricity_bus["sequences"].sum(axis=0))
        pp.pprint(my_results)

        # Rename sequences names 
        nodes = electricity_bus["sequences"]
        nodes.columns = ['demand','grid_feed_in', 'storage_in','grid_supply','Pv_feed_in','storage_out' ]
        
        # Calculate Special Parameters
        self_consumption = (nodes['Pv_feed_in'].sum() - nodes['grid_feed_in'].sum())/ nodes['Pv_feed_in'].sum()
        self_sufficiency = (nodes['demand'].sum() - nodes['grid_supply'].sum())/ nodes['demand'].sum()
        self.storage_capacity =  my_results["storage_invest_KWh"]
        Total_self_consumption = round(self_consumption * 100, 2)
        Total_self_sufficiency = round(self_sufficiency * 100, 2)
        self.Total_Pv_production = nodes['Pv_feed_in'].sum()
        self.Grid_feed_in = nodes['grid_feed_in'].sum()
        self.Grid_Import = nodes['grid_supply'].sum()
        self.feed_in_percentage = (self.Grid_feed_in/ self.Total_Pv_production) * 100
        self.Total_Demand = self.annual_demand*1000
        self.optimal_Storage = f'{round(self.storage_capacity,2)} KWh'
            
        
        # Plots Section
        #=============#
        
        # To clear plots and entire layout in order to display updated/new graphs for every new simulation
        self.fig.data = []
        self.fig.layout = {}
        
         # 1. PV Production Fed into grid Gauge
        self.fig.add_trace(go.Indicator(
        value=self.feed_in_percentage,
        mode="gauge+number",
        title={'text': "<b>PV Production Fed into Grid (%)</b>"},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 30], 'color': "red"},
                {'range': [30, 70], 'color': "yellow",},
                {'range': [70, 100], 'color': "limegreen"}],
            'bar': {'color': "silver"},
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': self.feed_in_percentage}}),
        row=1, col=1)
        
        # 2. Self Consumption Gauge
        self.fig.add_trace(go.Indicator(
        value=Total_self_consumption,
        mode="gauge+number",
        title={'text': "<b>Self Consumption (%)</b>"},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, Total_self_consumption], 'color': "orange"},
                {'range': [Total_self_consumption, 100], 'color': "white"}],
            'bar': {'color': "orange"}}),
        row=2, col=1)

        # 3. Self Sufficiency Gauge
        self.fig.add_trace(go.Indicator(
            value=Total_self_sufficiency,
            mode="gauge+number",
            title={'text': "<b>Self Sufficiency (%)</b>"},
            gauge={
                'axis': {'range': [0, 100]},
                'steps': [
                    {'range': [0, Total_self_sufficiency], 'color': "yellowgreen"},
                    {'range': [Total_self_sufficiency, 100], 'color': "white"}],
                'bar': {'color': "yellowgreen"}}),
            row=3, col=1)

        # Assign outputs to the Widgets
        self.grahics_view.setHtml(self.fig.to_html(include_plotlyjs='cdn'))
        self.Storage_output.setText(self.optimal_Storage)
        self.grahics_view.show()
        self.btn_run_simulation.setText("Run Simulation")
        self.btn_run_simulation.setCheckable(False)
        self.btn_run_simulation.setCheckable(True)


    # Financial Analysis calculation 
    #==============================#
    def update_costs(self):
        """
        Performs financial calculations based on simulation results and input 
        parameters,updating the results_display table with the calculated values.

        Retrieves input parameters and simulation results such as electricity 
        price, feed-in tariff,PV system capacity, and demand. Additionally, 
        retrieves relevant data like PV and BESS capital expenditures from the 
        simulation model if available.

        Calculates various financial metrics, including yearly energy costs without 
        and with PV+BESS,total PV generation, income from feed-in, energy bill for 
        grid import, investment costs for PV and BESS, total investments, cost savings, 
        and payback period.

        Populates the results_display table with the calculated values for better 
        visualization.

        Returns:
        -------
            None
        """
        

        # Retrieve data from simulation results or input parameters
        electricity_price = int(self.input_electricity_price.value())
        feedin_price = int(self.input_feedin_price.value())
        pv_capacity = int(self.input_pv_existing_capacity.value())
        demand = int(self.Total_Demand)

        # Retrieve other necessary data from the simulation results (if available)
        pv_capex = int(self.input_PV_Capex.value()*100) # Example value, retrieve from model if available
        bess_capex = int(self.input_BESS_Capex.value()*100)  # Example value, retrieve from model if available
        bess_optimal_value = self.storage_capacity

        # Perform financial calculations
        yearly_energy_costs_conventional = demand * electricity_price/100
        total_pv_generated = self.Total_Pv_production  # Assuming 9411 kWh/kWp as in your previous calculation
        fed_into_grid = self.Grid_feed_in  # Assuming all excess goes to grid
        income_from_fit = fed_into_grid  * feedin_price/100
        energy_bill_grid_import = self.Grid_Import * electricity_price/100
        pv_investment = pv_capacity * pv_capex
        bess_investment = bess_optimal_value * bess_capex
        total_investments = pv_investment + bess_investment

        # Calculate cost savings and payback period
        cost_savings = yearly_energy_costs_conventional - energy_bill_grid_import + income_from_fit
        payback_period = total_investments / cost_savings
        Disclaimer_text = "Disclaimer:  Results and analysis are estimations and may vary in real-world scenarios"
        
        data = [
        ("Electricity Price", f"{electricity_price} €-cents/kWh"),
        ("Feed-in Tariff (FiT)", f"{feedin_price} €-cents/kWh"),
        ("PV System Capacity", f"{pv_capacity} kWp"),
        ("Energy Demand", f"{demand} kWh/Yr"),
        ("Yearly Energy Costs (Without PV+BESS)", ""),  # Separator for better organization
        ("Energy bill for Grid Import", f"{yearly_energy_costs_conventional:.2f} €/Yr"),
        ("Yearly Energy Costs (With PV+BESS)", ""),  # Separator
        ("Total PV Generated", f"{total_pv_generated:.2f} kWh"),
        ("Fed-into-Grid", f"{fed_into_grid:.2f} kWh"),
        ("Income from FiT", f"{income_from_fit:.2f} €"),
        ("Grid Import", f"{self.Grid_Import:.2f} kWh"),
        ("Energy bill for Grid Import", f"{energy_bill_grid_import:.2f} €/Yr"),
        ("Investment Costs", ""),  # Separator
        ("PV-CAPEX", f"{pv_capex} €/kWp"),
        ("BESS-CAPEX", f"{bess_capex} €/kWh"),
        ("PV Investment", f"{pv_investment:.2f} €"),
        ("BESS Investment", f"{bess_investment:.2f} €"),
        ("Total Investments", f"{total_investments:.2f} €"),
        ("Savings and Payback Period", ""),  # Separator
        ("Energy bill Savings (with PV+BESS)", f"{cost_savings:.2f} €/Yr"),
        ("Payback Period", f"{payback_period:.2f} Yr")]
        
        self.table_widget.setRowCount(0)  # Clear existing rows
        self.table_widget.setColumnCount(2) 
        self.table_widget.setColumnWidth(0,324)
        self.table_widget.setColumnWidth(1,300)

        # Populate the table with data
        for row, (property_name, value) in enumerate(data):
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QTableWidgetItem(property_name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(value))

        # Set table headers
        self.table_widget.setHorizontalHeaderLabels(["Description", "Value"])
        self.Disclaimer_text.setText(Disclaimer_text)
        
 
    # Save Financial Analysis report as PDF 
    #=====================================#
    def save_to_pdf(self):
        """
        Save the Financial Analysis report as a PDF file.
        Opens a file dialog to get the desired file name and location for saving 
        the PDF. Utilizes QtPrintSupport.QPrinter to create a PDF file with high 
        resolution.Renders the content of the table widget onto the PDF using
        QPainter.

        Parameters:
        -----------
            None
    
        Returns:
        --------
            None
        """
        file_name, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")

        if file_name:
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setOutputFileName(file_name)

            painter = QPainter(printer)
            scale_factor = 16
            painter.scale(scale_factor, scale_factor)
            self.table_widget.render(painter)
            painter.end()



def main():
    app = QApplication(sys.argv)
    main_window = EnergyModelApp()
    main_window.init_ui()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
