from service.foam_type_service import FoamType_service

service = FoamType_service()

foam_types = service.display_active_foam_types()

for foam in foam_types:
    print(
        foam.foam_type_id,
        foam.foam_type_name,
        foam.density,
        foam.price_per_cubic_ft,
        foam.status
    )