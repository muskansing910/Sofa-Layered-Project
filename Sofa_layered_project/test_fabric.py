from service.fabric_service import Fabric_service

service = Fabric_service()

fabrics = service.display_active_fabrics()

for fabric in fabrics:
    print(
        fabric.fabric_id,
        fabric.fabric_name,
        fabric.price_per_meter,
        fabric.status
    )