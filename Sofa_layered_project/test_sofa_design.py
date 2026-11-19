from service.sofa_design_service import SofaDesignService


service = SofaDesignService()

designs = service.display_active_designs()


for design in designs:

    print("--------------------------------")
    print("Design ID:", design.design_id)
    print("Design Name:", design.design_name)
    print("Description:", design.description)
    print("Starting Price:", design.starting_price)
    print("Image:", design.image)
    print("Status:", design.status)