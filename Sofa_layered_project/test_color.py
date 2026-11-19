from service.color_service import Color_service

service = Color_service()

colors = service.display_active_colors()

for color in colors:
    print(
        color.color_id,
        color.color_name,
        color.color_code,
        color.status
    )