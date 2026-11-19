from model.custom_sofa import CustomSofa

from service.custom_sofa_service import CustomSofa_service
from service.fabric_service import Fabric_service
from service.customer_service import customer_service
from service.sofa_type_service import SofaType_service
from service.sofa_design_service import SofaDesign_service
from service.color_service import Color_service
from service.back_design_service import BackDesign_service
from service.armrest_design_service import ArmrestDesign_service
from service.leg_design_service import LegDesign_service
from service.foam_type_service import FoamType_service

custom_sofa_service = CustomSofa_service()


# CUSTOM SOFA ID

custom_sofa_id = int(input("Enter custom sofa id: "))


# CUSTOMER SELECTION

customer_service = customer_service()

customers = customer_service.Display_customers()

print("\nAvailable Customers:")

for i in range(len(customers)):
    print(i + 1, customers[i].name)

choice = int(input("Choose customer: "))

selected_customer = customers[choice - 1]

print("You selected:", selected_customer.name)
print("Database ID:", selected_customer.customer_id)

customer_id = selected_customer.customer_id

# SOFA TYPE SELECTION

sofa_type_service = SofaType_service()

sofa_types = sofa_type_service.display_sofa_types()

print("\nAvailable Sofa Types:")

for i in range(len(sofa_types)):
    print(i + 1, sofa_types[i].type_name)

choice = int(input("Choose sofa type: "))

selected_sofa_type = sofa_types[choice - 1]

print("You selected:", selected_sofa_type.type_name)
print("Database ID:", selected_sofa_type.sofa_type_id)

sofa_type_id = selected_sofa_type.sofa_type_id

# SOFA DESIGN SELECTION

sofa_design_service = SofaDesign_service()

designs = sofa_design_service.display_sofa_designs()

print("\nAvailable Sofa Designs:")

for i in range(len(designs)):
    print(i + 1, designs[i].design_name)

choice = int(input("Choose sofa design: "))

selected_design = designs[choice - 1]

print("You selected:", selected_design.design_name)
print("Database ID:", selected_design.design_id)

design_id = selected_design.design_id

# FABRIC SELECTION

fabric_service = Fabric_service()

fabrics = fabric_service.display_fabrics()

print("\nAvailable Fabrics:")

for i in range(len(fabrics)):
    print(i + 1, fabrics[i].fabric_name)

choice = int(input("Choose fabric: "))

selected_fabric = fabrics[choice - 1]

print("You selected:", selected_fabric.fabric_name)
print("Database ID:", selected_fabric.fabric_id)

fabric_id = selected_fabric.fabric_id


# OTHER IDs - TEMPORARILY MANUAL

# COLOR SELECTION

color_service = Color_service()

colors = color_service.display_colors()

print("\nAvailable Colors:")

for i in range(len(colors)):
    print(i + 1, colors[i].color_name)

choice = int(input("Choose color: "))

selected_color = colors[choice - 1]

print("You selected:", selected_color.color_name)
print("Database ID:", selected_color.color_id)

color_id = selected_color.color_id
# BACK DESIGN SELECTION

back_design_service = BackDesign_service()

back_designs = back_design_service.display_back_designs()

print("\nAvailable Back Designs:")

for i in range(len(back_designs)):
    print(i + 1, back_designs[i].back_design_name)

choice = int(input("Choose back design: "))

selected_back_design = back_designs[choice - 1]

print("You selected:", selected_back_design.back_design_name)
print("Database ID:", selected_back_design.back_design_id)

back_design_id = selected_back_design.back_design_id

# ARMREST DESIGN SELECTION

armrest_design_service = ArmrestDesign_service()

armrest_designs = armrest_design_service.display_armrest_designs()

print("\nAvailable Armrest Designs:")

for i in range(len(armrest_designs)):
    print(i + 1, armrest_designs[i].armrest_design_name)

choice = int(input("Choose armrest design: "))

selected_armrest = armrest_designs[choice - 1]

print("You selected:", selected_armrest.armrest_design_name)
print("Database ID:", selected_armrest.armrest_design_id)

armrest_design_id = selected_armrest.armrest_design_id

# LEG DESIGN SELECTION

leg_design_service = LegDesign_service()

leg_designs = leg_design_service.display_leg_designs()

print("\nAvailable Leg Designs:")

for i in range(len(leg_designs)):
    print(i + 1, leg_designs[i].leg_design_name)

choice = int(input("Choose leg design: "))

selected_leg = leg_designs[choice - 1]

print("You selected:", selected_leg.leg_design_name)
print("Database ID:", selected_leg.leg_design_id)

leg_design_id = selected_leg.leg_design_id

# FOAM TYPE SELECTION

foam_type_service = FoamType_service()

foam_types = foam_type_service.display_foam_types()

print("\nAvailable Foam Types:")

for i in range(len(foam_types)):
    print(i + 1, foam_types[i].foam_type_name)

choice = int(input("Choose foam type: "))

selected_foam = foam_types[choice - 1]

print("You selected:", selected_foam.foam_type_name)
print("Database ID:", selected_foam.foam_type_id)

foam_type_id = selected_foam.foam_type_id

# SOFA DIMENSIONS

length = float(input("Enter length: "))

width = float(input("Enter width: "))

height = float(input("Enter height: "))

seat_depth = float(input("Enter seat depth: "))

number_of_seats = int(input("Enter number of seats: "))

custom_requirements = input("Enter custom requirements: ")


# CREATE CUSTOM SOFA OBJECT

custom_sofa = CustomSofa(
    custom_sofa_id,
    customer_id,
    sofa_type_id,
    design_id,
    fabric_id,
    color_id,
    back_design_id,
    armrest_design_id,
    leg_design_id,
    foam_type_id,
    length,
    width,
    height,
    seat_depth,
    number_of_seats,
    custom_requirements,
    None
)


# SAVE TO DATABASE

custom_sofa_service.add_custom_sofa(custom_sofa)

print("\nCustom sofa added successfully")

#-----------------------
print("\nAll Custom Sofas:")

custom_sofas = custom_sofa_service.display_custom_sofas()

for sofa in custom_sofas:
    print(
        sofa.custom_sofa_id,
        sofa.customer_id,
        sofa.sofa_type_id,
        sofa.design_id,
        sofa.fabric_id,
        sofa.color_id,
        sofa.back_design_id,
        sofa.armrest_design_id,
        sofa.leg_design_id,
        sofa.foam_type_id,
        sofa.length,
        sofa.width,
        sofa.height,
        sofa.seat_depth,
        sofa.number_of_seats,
        sofa.custom_requirements
    )