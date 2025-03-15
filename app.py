import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image, ImageDraw

st.set_page_config("Interactive Rainforest Wild Asia Map", layout="centered")

st.title("🌳 Rainforest Wild Asia Interactive Map")

# Load latest cropped map image
img_path = 'assets/rfw-asia-en-map.png'
original_img = Image.open(img_path).convert("RGBA")

# Updated coordinates based on the new cropped map
itinerary_points = {
    "Entrance Gorge": (588, 804),
    "Log Crossing Trek": (503, 760),
    "Karst Loop Trek": (352, 788),
    "The Karsts (Ranger Talk)": (244, 815),
    "Forest Floor Trek": (421, 569),
    "Rock Cascade": (585, 446),
    "The Canopy": (853, 255),
    "Langur Walking Nets": (1017, 191),
    "Canopy Jump": (729, 428),
    "Upper Stream Trek": (740, 588),
    "Lower Stream Trek": (780, 699),
    "The Cavern": (960, 774)
}

# Full itinerary details
itinerary_details = {
    "Entrance Gorge": "9.00am: Enter the Entrance Gorge as you are welcomed by the waterfall. Enjoy the serene habitat of the Asian arowana and Southern river terrapin at the Entrance Pond.",
    "Log Crossing Trek": "9.15am: Venture off the beaten path by heading onto the Log Crossing Trek, where you can cross rocks and fallen logs that lie over a flowing stream.",
    "Karst Loop Trek": "9.30am: Continue to the Karst Loop Trek where you may spot Francois' langurs on their karst island and harnessed adventurers on the Wild Apex Adventure. Catch the Ranger Talk happening daily at 9.45am at The Karsts to learn more about the Francois' langurs from our keepers!",
    "The Karsts (Ranger Talk)": "9.45am: Ranger Talk about Francois' langurs at The Karsts.",
    "Forest Floor Trek": "10.15am: Get closer to the animals by heading on the Forest Floor Trek, where you may even encounter a prowling Malayan tiger!",
    "Rock Cascade": "10.45am: Spot the Babirusas and Red dholes at the Rock Cascade from the elevated walkway. \nHead to the Tiger Waterfall for the Ranger Talk happening daily at 11.00am.",
    "The Canopy": "11.15am: Explore The Canopy, where langurs and deer thrive in this habitat.",
    "Langur Walking Nets": "11.15am: Step onto the Langur Walking Nets as you try to spot the Philippine spotted deer below.",
    "Canopy Jump": "1.00pm: Continue your adventure by stepping off a towering 13m or 20m platform at Canopy Jump! \nAdditional charges apply for Canopy Jump",
    "Upper Stream Trek": "1.30pm: Venture down the Upper Stream Trek to the Malayan sun bear habitat.",
    "Lower Stream Trek": "1.30pm: Cross the various bridges and under fallen logs on the Lower Stream Trek and visit the Watering Hole Cafe for a quick respite as you enjoy the view of the Tapir pool.",
    "The Cavern": "2.00pm: Explore The Cavern, inspired by the Mulu caves in Sarawak, Malaysia, where you can find Cave racer snakes and Asian forest scorpions! End your cave exploration with a stunning photo at The Oculus!"
}

# Draw clickable area highlights
overlay = Image.new("RGBA", original_img.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(overlay)
radius = 15
for x, y in itinerary_points.values():
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline='yellow', width=3, fill=(255, 255, 0, 60))

img_with_highlights = Image.alpha_composite(original_img, overlay)

# Display interactive image
details_placeholder = st.empty()
coords = streamlit_image_coordinates(img_with_highlights, key="interactive_map")

if coords:
    clicked_x, clicked_y = coords['x'], coords['y']
    selected = None
    for name, (x, y) in itinerary_points.items():
        if (clicked_x - x) ** 2 + (clicked_y - y) ** 2 <= radius ** 2:
            selected = name
            break

    if selected:
        with details_placeholder.expander(f"📍 {selected}", expanded=True):
            st.write(itinerary_details[selected])
    else:
        details_placeholder.warning("Tap directly within a highlighted circle.")
else:
    details_placeholder.info("Tap any highlighted area on the map above to see details.")
