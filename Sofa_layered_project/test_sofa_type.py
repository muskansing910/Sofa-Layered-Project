from service.sofa_type_service import SofaType_service


service = SofaType_service()

sofa_types = service.display_active_sofa_types()


for sofa_type in sofa_types:

    print("--------------------------------")
    print("Sofa Type ID:", sofa_type.sofa_type_id)
    print("Type Name:", sofa_type.type_name)
    print("Description:", sofa_type.description)
    print("Status:", sofa_type.status)