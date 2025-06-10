# Interactive US Agent Map

This project is a browser-based interactive map of the United States designed to help users quickly identify licensed states, view agent availability, and navigate to dynamic agent listings. The map is built using HTML, CSS, and JavaScript with an embedded SVG interface for interactive functionality. It is self-contained and requires no external libraries or frameworks.

## Features

- **Interactive SVG Map**  
  Clickable map of the United States with built-in interactivity and dynamic styling.

- **State Licensing Visualization**  
  Licensed states appear active and clickable; unlicensed states are visually disabled and non-interactive.

- **Agent Count Display**  
  Displays the number of available agents per state via:
  - Tooltips on map hover
  - A scrollable list view beneath the map

- **Dynamic Redirection**  
  Clicking on a licensed state navigates to a custom URL with agent listings specific to that state.

- **Responsive Design**  
  Layout adjusts for desktop and mobile screen sizes.

- **List View**  
  Provides a text-based alternative for accessing agent listings, useful for accessibility and smaller screens.

## Technologies Used

- **HTML5** – Structural layout for the map, tooltip, and list view
- **CSS3** – Styling for map states, tooltips, and responsiveness
- **JavaScript** – Logic for hover effects, click handling, and dynamic rendering of state data
- **SVG** – Scalable Vector Graphics map for pixel-perfect interactions
- **jQuery** (optional/assumed) – Used for simplified DOM manipulation, if present

## File Structure

- **Map.HTML** – Single file containing:
  - SVG map markup
  - `stateData` object for per-state configuration
  - All inline CSS and JavaScript logic

## State Data Configuration

The `stateData` object contains information for each state, including:

```javascript
"FL": {
  "fullName": "Florida",
  "title": "Florida",
  "longDescription": "<div style=\"text-align: center;\">Available agents: 6</div>",
  "linkUrl": "https://placeholder.com/map/fl",
  "isDisabled": false,
  "overrideFill": "#000000",
  "overrideFillEnabled": false,
  "overrideHoverFill": "#000000",
  "overrideHoverFillEnabled": false
}
```

### Key Properties

- `fullName`: Full state name
- `title`: Display title on map hover
- `longDescription`: HTML snippet for tooltip or list view
- `linkUrl`: Destination URL when clicked
- `isDisabled`: Boolean to disable interactivity for unlicensed states
- `overrideFill` / `overrideHoverFill`: Optional custom fill colors

## Usage Instructions

### View the Map

1. Open `Map.HTML` in a modern web browser (Chrome, Firefox, Edge, Safari).
2. Hover over a state to see its name and agent count.
3. Click on a licensed (enabled) state to be redirected to its listing page.

### List View

Scroll below the map to view a full list of licensed states and available agent counts. Clicking a state name navigates to the corresponding agent listing.

## Hosting

- For production use, place `Map.HTML` on a web server (Apache, Nginx, or static host).
- For development/testing, it may be opened locally, but note that certain dynamic features (like remote data or CORS-restricted links) may not work outside a server context.

## Customization

To change licensing status, agent counts, or redirect behavior:

1. Edit the `stateData` object within the `<script>` block in `Map.HTML`.
2. To customize colors or tooltip styles, modify the `<style>` block.

## Styling Guidelines

- **Enabled States**: Fully interactive with hover effects
- **Disabled States**: Grayed out and non-clickable
- **Tooltips**: Show on hover, styled with a light background, border radius, and drop shadow
- **List View**: Centered and scrollable, with clickable links for each state

## Dependencies

None required. This map is fully self-contained and does not rely on external JavaScript or CSS files.

## Compatibility

Tested in modern browsers. For best performance and interactivity, use an up-to-date version of Chrome, Firefox, Safari, or Edge.
