# lab_management/views.py
import json
from django.http import JsonResponse
def store_lab_data(request):
    # Sample JSON data
    json_data = '''
    {
      "LabData": [
    {
      "id": "1",
      "component": "Development Board",
      "manufacturer_year": "2020",
      "bought_year": "2021",
      "working_condition": "Good"
    },
    {
      "id": "2",
      "component": "Integrated Development Environment (IDE)",
      "manufacturer_year": "N/A",
      "bought_year": "2022",
      "working_condition": "Excellent"
    },
    {
      "id": "3",
      "component": "Programming Tools",
      "manufacturer_year": "N/A",
      "bought_year": "2023",
      "working_condition": "Good"
    },
    {
      "id": "4",
      "component": "Sensors and Actuators",
      "manufacturer_year": "N/A",
      "bought_year": "2021",
      "working_condition": "Fair"
    },
    {
      "id": "5",
      "component": "Logic Analyzers",
      "manufacturer_year": "2020",
      "bought_year": "2021",
      "working_condition": "Excellent"
    },
    {
      "id": "6",
      "component": "Power Supplies",
      "manufacturer_year": "2019",
      "bought_year": "2020",
      "working_condition": "Good"
    },
    {
      "id": "7",
      "component": "Breadboards and Jumper Wires",
      "manufacturer_year": "N/A",
      "bought_year": "2022",
      "working_condition": "Excellent"
    },
    {
      "id": "8",
      "component": "Oscilloscopes",
      "manufacturer_year": "2018",
      "bought_year": "2019",
      "working_condition": "Fair"
    },
    {
      "id": "9",
      "component": "Function Generators",
      "manufacturer_year": "2019",
      "bought_year": "2020",
      "working_condition": "Good"
    },
    {
      "id": "10",
      "component": "Hardware Description Language (HDL) Tools",
      "manufacturer_year": "N/A",
      "bought_year": "2021",
      "working_condition": "Excellent"
    },
    {
      "id": "11",
      "component": "Embedded Software Libraries",
      "manufacturer_year": "N/A",
      "bought_year": "2023",
      "working_condition": "Good"
    },
    {
      "id": "12",
      "component": "Printed Circuit Boards (PCBs)",
      "manufacturer_year": "N/A",
      "bought_year": "2022",
      "working_condition": "Good"
    },
    {
      "id": "13",
      "component": "Soldering Stations",
      "manufacturer_year": "2019",
      "bought_year": "2020",
      "working_condition": "Fair"
    },
    {
      "id": "14",
      "component": "Safety Equipment",
      "manufacturer_year": "N/A",
      "bought_year": "2021",
      "working_condition": "Good"
    },
    {
      "id": "15",
      "component": "FPGA Boards",
      "manufacturer_year": "2021",
      "bought_year": "2022",
      "working_condition": "Good"
    },
    {
      "id": "16",
      "component": "ASIC Design Tools",
      "manufacturer_year": "N/A",
      "bought_year": "2021",
      "working_condition": "Excellent"
    },
    {
      "id": "17",
      "component": "Digital Design Kits",
      "manufacturer_year": "N/A",
      "bought_year": "2022",
      "working_condition": "Good"
    },
    {
      "id": "18",
      "component": "Analog Design Kits",
      "manufacturer_year": "N/A",
      "bought_year": "2023",
      "working_condition": "Fair"
    },
    {
      "id": "19",
      "component": "PCB Fabrication Equipment",
      "manufacturer_year": "2020",
      "bought_year": "2021",
      "working_condition": "Good"
    },
    {
      "id": "20",
      "component": "Semiconductor Parameter Analyzers",
      "manufacturer_year": "2019",
      "bought_year": "2020",
      "working_condition": "Good"
    },
    {
      "id": "21",
      "component": "IC Testers",
      "manufacturer_year": "2018",
      "bought_year": "2019",
      "working_condition": "Fair"
    },
    {
      "id": "22",
      "component": "3D Printers",
      "manufacturer_year": "2022",
      "bought_year": "2023",
      "working_condition": "Excellent"
    },
    {
      "id": "23",
      "component": "Environmental Chambers",
      "manufacturer_year": "N/A",
      "bought_year": "2022",
      "working_condition": "Good"
    },
    {
      "id": "24",
      "component": "Workstations/Computers",
      "manufacturer_year": "2020",
      "bought_year": "2021",
      "working_condition": "Good"
    },
    {
      "id": "25",
      "component": "EDA Software",
      "manufacturer_year": "N/A",
      "bought_year": "2022",
      "working_condition": "Excellent"
    },
    {
      "id": "26",
      "component": "CAD Workstations",
      "manufacturer_year": "2019",
      "bought_year": "2020",
      "working_condition": "Good"
    },
    {
      "id": "27",
      "component": "Simulation Servers",
      "manufacturer_year": "2018",
      "bought_year": "2019",
      "working_condition": "Fair"
    },
    {
      "id": "28",
      "component": "Programming Devices",
      "manufacturer_year": "N/A",
      "bought_year": "2023",
      "working_condition": "Good"
    },
    {
      "id": "29",
      "component": "CAD Workstations",
      "manufacturer_year": "2019",
      "bought_year": "2020",
      "working_condition": "Good"
    },
    {
      "id": "30",
      "component": "Simulation Servers",
      "manufacturer_year": "2018",
      "bought_year": "2019",
      "working_condition": "Fair"
    }
  ]
    }
    '''

    data = json.loads(json_data)

    return JsonResponse(data)