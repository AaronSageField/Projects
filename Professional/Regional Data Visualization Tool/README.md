This project is an interactive US map designed to visualize the states where a company is licensed, display the number of available agents in each state, and redirect users to dynamic agent listings upon clicking a state. The map is built using HTML, CSS, and JavaScript, with an SVG-based map interface for interactivity.
Features

Interactive Map: Displays a clickable SVG map of the United States.
State Licensing Visualization: States are styled to indicate licensing status (enabled or disabled).
Agent Count Display: Shows the number of available agents in each state via hover tooltips and a list view.
Dynamic Redirection: Clicking a licensed state redirects users to a dynamic listing of agents for that state.
Responsive Design: Adapts to various screen sizes for optimal viewing on desktop and mobile devices.
List View: Provides an alternative list-based interface for users to access state-specific agent listings.

Technologies Used

HTML5: Structures the map and list view components.
CSS3: Styles the map, tooltips, and list view for a polished user experience.
JavaScript: Handles interactivity, including hover effects, click events, and dynamic state data rendering.
SVG: Utilizes Scalable Vector Graphics for the US map, ensuring crisp visuals and precise click detection.
jQuery: Simplifies DOM manipulation and event handling (assumed from common practices in similar projects).

File Structure

Map.HTML: The main file containing the HTML structure, CSS styles, SVG map, and JavaScript logic for the interactive map.
stateData: A JavaScript object within Map.HTML that defines state-specific data, including:
fullName: Full name of the state.
title: Display title for the state.
longDescription: HTML content showing the number of available agents.
linkUrl: URL for redirecting to the state's agent listing.
isDisabled: Boolean indicating if the state is unlicensed (disables interactivity).
overrideFill and overrideHoverFill: Optional custom fill colors for states.
Other properties for styling and interactivity.

Host the File:
Place Map.HTML in a web server directory (e.g., Apache, Nginx, or a local development server like http-server).
Alternatively, open Map.HTML directly in a browser for testing (note: some features may require a server due to CORS or dynamic content).

Dependencies:
No external dependencies are required, as the map is self-contained within Map.HTML.
Ensure a modern browser (Chrome, Firefox, Safari, Edge) for full compatibility.

Usage

Viewing the Map:
Open Map.HTML in a web browser to display the interactive US map.
Hover over a state to view a tooltip with the state name and number of available agents.
Click a licensed state (non-grayed) to navigate to the corresponding agent listing page.

List View:
Scroll below the map to see a list of states with available agents.
Click a state name to access the agent listing for that state.

Customization:
Update the stateData object in the JavaScript section of Map.HTML to modify:
Licensing status (isDisabled).
Agent counts (longDescription).
Redirect URLs (linkUrl).

Adjust CSS styles in the <style> section to customize appearance (e.g., colors, tooltip design).

Example State Data
"FL": {
    "fullName": "Florida",
    "title": "Florida",
    "description": null,
    "longDescription": "<div style=\"text-align: center;\">\n  Available agents: 6\n</div>",
    "linkUrl": "https://placeholder.com/map/fl",
    "isDisabled": false,
    "isHovering": false,
    "cssClass": null,
    "overrideFill": "#000000",
    "overrideFillEnabled": false,
    "overrideHoverFill": "#000000",
    "overrideHoverFillEnabled": false,
    "overridePopLink": null
}

Styling

Enabled States: Fully interactive with a default fill color and hover effects.
Disabled States: Grayed out (via CSS or overrideFill) and non-clickable.
Tooltips: Display state name and agent count on hover, styled with a white background, shadow, and rounded corners.
List View: Centered, with clickable links for licensed states and visual indicators for agent availability.
