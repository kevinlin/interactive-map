# CLAUDE.md - AI Assistant Guide

> **Last Updated**: 2025-11-23
> **Project**: Rainforest Wild Asia Interactive Map
> **Tech Stack**: Python, Streamlit, PIL (Pillow)

## 📋 Project Overview

This is a **single-page interactive web application** built with Streamlit that provides an interactive map interface for exploring the Rainforest Wild Asia park itinerary. Users can click on highlighted points on a park map to view detailed information about different locations and attractions.

### Purpose
- Display an interactive park map with clickable points of interest
- Provide time-based itinerary information for park visitors
- Offer an intuitive interface for exploring park attractions

### Key Features
- Interactive image coordinates with clickable hotspots
- Real-time highlighting of selected points
- Sidebar with expandable itinerary details
- Visual overlays on map image

## 🏗️ Repository Structure

```
interactive-map/
├── app.py                      # Main Streamlit application (single file)
├── requirements.txt            # Python dependencies
├── README.md                   # User-facing documentation
├── .gitignore                  # Git ignore patterns
├── .streamlit/
│   └── config.toml            # Streamlit configuration
└── assets/
    └── rfw-asia-en-map.png    # Park map image
```

### File Descriptions

#### `app.py` (Main Application)
- **Lines 1-3**: Import dependencies (streamlit, streamlit-image-coordinates, PIL)
- **Lines 5-7**: Page configuration and title setup
- **Lines 10-11**: Image loading using PIL
- **Lines 14-27**: Dictionary of POI coordinates (x, y pixel positions)
- **Lines 30-43**: Dictionary of itinerary details with timestamps and descriptions
- **Lines 46**: Sidebar selectbox for POI selection
- **Lines 49-57**: Function to generate highlighted overlay on map image
- **Lines 60-69**: Interactive image display and click detection logic
- **Lines 72-74**: Sidebar expandable sections for each POI

#### `.streamlit/config.toml`
- **runOnSave**: Automatically reruns app when files change
- **showErrorDetails**: Shows full error stack traces
- **gatherUsageStats**: Disabled for privacy

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.x**: Primary programming language
- **Streamlit 1.43.2**: Web framework for interactive apps
- **PIL/Pillow 11.1.0**: Image processing library
- **streamlit-image-coordinates 0.2.0**: Custom component for clickable images

### Key Dependencies
```
streamlit==1.43.2              # Main web framework
streamlit-image-coordinates==0.2.0  # Interactive image component
pillow==11.1.0                 # Image manipulation
numpy==2.2.3                   # Array operations (indirect dependency)
pandas==2.2.3                  # Data structures (indirect dependency)
```

See `requirements.txt` for complete dependency list.

## 🔧 Development Workflow

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
streamlit run app.py
```

### Development Server
- **URL**: http://localhost:8501
- **Auto-reload**: Enabled (configured in .streamlit/config.toml)
- **Error display**: Full stack traces shown

### Testing Changes
1. Make code changes to `app.py`
2. Streamlit auto-reloads (runOnSave=true)
3. Refresh browser to see changes
4. Check browser console for JavaScript errors
5. Check terminal for Python errors

## 📝 Code Conventions

### Python Style
- **Indentation**: 4 spaces
- **String quotes**: Single quotes for dict keys, double quotes acceptable
- **Line length**: Reasonable (no strict limit observed)
- **Comments**: Inline comments for section headers

### Data Structure Patterns

#### POI Coordinates
```python
# Format: "Location Name": (x_pixel, y_pixel)
itinerary_points = {
    "Point Name": (588, 804),
    # ...
}
```

#### Itinerary Details
```python
# Format: "Location Name": "Time and description"
itinerary_details = {
    "Point Name": "9.00am: Description of the location...",
    # ...
}
```

### Streamlit Conventions
- Use `st.set_page_config()` as first Streamlit command
- Use `st.sidebar` for controls and information panels
- Use expanders for collapsible content sections
- Use emojis in UI strings (🌳, 📍, etc.)

## 🎨 Image Handling

### Map Image Requirements
- **Format**: PNG with alpha channel (RGBA)
- **Location**: `assets/rfw-asia-en-map.png`
- **Processing**: Converted to RGBA mode on load
- **Overlay**: Semi-transparent yellow circles (60 alpha) for POI markers

### Coordinate System
- **Origin**: Top-left corner (0, 0)
- **X-axis**: Increases left to right
- **Y-axis**: Increases top to bottom
- **Units**: Pixels
- **Click radius**: 25 pixels (5² in detection, 15 in drawing)

### Highlighting Logic
```python
# Detection radius: 25px
if (clicked_x - x) ** 2 + (clicked_y - y) ** 2 <= 25 ** 2:
    # POI clicked

# Visual radius: 15px
draw.ellipse((x - radius, y - radius, x + radius, y + radius), ...)
```

## 🔍 Key Implementation Details

### Interactive Click Detection
The app uses a custom Streamlit component `streamlit_image_coordinates` that:
1. Displays an image with PIL-generated overlays
2. Returns click coordinates as `{'x': int, 'y': int}`
3. Compares clicks against POI coordinates using distance formula
4. Updates UI state when POI is clicked

### State Management
- **No explicit session state**: Uses Streamlit's native component state
- **Component key**: `"interactive_map"` for image coordinates
- **Selection sync**: Sidebar selectbox and map clicks are independent

### UI Layout
- **Main area**: Interactive map image with overlays
- **Sidebar**: POI selector dropdown + expandable detail panels
- **Wide layout**: Configured via `layout="wide"`

## 🚀 Common Tasks for AI Assistants

### Adding a New Point of Interest
1. Add coordinate tuple to `itinerary_points` dict (line 14-27)
2. Add description to `itinerary_details` dict (line 30-43)
3. Ensure keys match exactly between both dicts

### Modifying Existing POI Coordinates
1. Update the tuple in `itinerary_points`
2. Test by running app and clicking the area
3. Adjust coordinates until click detection works properly

### Changing Visual Styling
- **Highlight color**: Modify `color` variable in `generate_highlighted_image()` (line 54)
- **Circle size**: Modify `radius` variable (line 52)
- **Transparency**: Modify alpha value in `fill=(255, 255, 0, 60)` (line 56)
- **Border width**: Modify `width=3` parameter (line 55)

### Updating Map Image
1. Replace `assets/rfw-asia-en-map.png` with new image
2. Update all coordinates in `itinerary_points` to match new image
3. Test all POI clicks to ensure accuracy

### Debugging Tips
1. **Click not registering**: Check if coordinates are within image bounds
2. **Wrong POI selected**: Verify coordinate accuracy and click radius
3. **Image not loading**: Check file path and image format (must support RGBA)
4. **Overlay not visible**: Verify PIL overlay composition and alpha values

## ⚙️ Configuration

### Streamlit Config (.streamlit/config.toml)
```toml
[server]
runOnSave = true               # Auto-reload on file changes

[client]
showErrorDetails = "full"      # Show full error traces

[browser]
gatherUsageStats = false       # Disable telemetry
```

### Page Config (app.py)
```python
st.set_page_config(
    "Interactive Rainforest Wild Asia Map",  # Page title
    layout="wide"                             # Wide layout mode
)
```

## 🐛 Known Limitations

1. **No database**: All data hardcoded in dictionaries
2. **No user authentication**: Public access only
3. **Single page**: No routing or navigation
4. **Static content**: Content updates require code changes
5. **No mobile optimization**: May have usability issues on small screens
6. **No accessibility features**: No ARIA labels or keyboard navigation

## 📦 Dependencies Security

Recent security updates (from git history):
- `urllib3` updated from 2.3.0 to 2.5.0
- `protobuf` updated from 5.29.3 to 5.29.5
- `requests` updated to 2.32.4

Always run `pip install -r requirements.txt` to get latest secure versions.

## 🔄 Git Workflow

### Branch Naming
- Feature branches: `claude/claude-md-*` or descriptive names
- Main branch: (not specified in current context)

### Commit Guidelines
- Use clear, descriptive commit messages
- Reference PR numbers when merging
- Security updates should mention CVE or vulnerability details

### Development Process
1. Create feature branch from main
2. Make changes and test locally
3. Commit with descriptive messages
4. Push to remote with `git push -u origin <branch-name>`
5. Create pull request
6. Merge after review

## 💡 Best Practices for AI Assistants

### When Modifying Code
1. **Read before editing**: Always read `app.py` before making changes
2. **Preserve structure**: Maintain the existing single-file structure
3. **Test coordinates**: Verify POI coordinates are within image bounds
4. **Keep data in sync**: Ensure `itinerary_points` and `itinerary_details` keys match
5. **Respect conventions**: Follow existing code style and patterns

### When Adding Features
1. **Keep it simple**: This is intentionally a simple single-file app
2. **Avoid over-engineering**: Don't add unnecessary abstractions
3. **Preserve user experience**: Maintain the current interaction model
4. **Consider performance**: Large images or many POIs may impact load time

### When Debugging
1. **Check Streamlit logs**: Terminal output shows Python errors
2. **Check browser console**: JavaScript/component errors appear here
3. **Verify image paths**: Ensure `assets/rfw-asia-en-map.png` exists
4. **Test click detection**: Use print/st.write to debug coordinates

## 📚 Helpful Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [streamlit-image-coordinates](https://github.com/blackary/streamlit-image-coordinates)

## 🎯 Quick Reference

### Run Application
```bash
streamlit run app.py
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Update Single Dependency
```bash
pip install <package>==<version>
pip freeze > requirements.txt
```

### Check Streamlit Version
```bash
streamlit version
```

---

**Note**: This is a straightforward, single-file Streamlit application. When working with this codebase, prefer simplicity and clarity over complex abstractions. The entire application logic fits in ~75 lines of code, and it should stay that way unless additional complexity is explicitly required.
