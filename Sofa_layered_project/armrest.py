from model.armrest_design import ArmrestDesign
from service.armrest_design_service import ArmrestDesign_service


armrest_service = ArmrestDesign_service()

armrest_designs = armrest_service.display_armrest_designs()

print("\nAvailable Armrest Designs:")

for i in range(len(armrest_designs)):

    print(
        i + 1,
        armrest_designs[i].armrest_design_name
    )


choice = int(input("Choose armrest design: "))

selected_armrest = armrest_designs[choice - 1]

print("You selected:", selected_armrest.armrest_design_name)
print("Database ID:", selected_armrest.armrest_design_id)