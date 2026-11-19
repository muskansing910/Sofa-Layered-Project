from service.back_design_service import BackDesign_service
from service.armrest_design_service import ArmrestDesign_service
from service.leg_design_service import LegDesign_service


# Back Designs
back_service = BackDesign_service()
back_designs = back_service.display_active_back_designs()

print("\nBACK DESIGNS")

for design in back_designs:
    print(design.back_design_id, design.back_design_name)


# Armrest Designs
armrest_service = ArmrestDesign_service()
armrest_designs = armrest_service.display_active_armrest_designs()

print("\nARMREST DESIGNS")

for design in armrest_designs:
    print(design.armrest_design_id, design.armrest_design_name)


# Leg Designs
leg_service = LegDesign_service()
leg_designs = leg_service.display_active_leg_designs()

print("\nLEG DESIGNS")

for design in leg_designs:
    print(design.leg_design_id, design.leg_design_name)