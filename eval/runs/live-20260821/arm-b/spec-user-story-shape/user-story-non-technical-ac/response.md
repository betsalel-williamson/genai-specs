# User Story: Dark Mode on Settings Page

## User Persona

- **Name:** Night Shift Professional
- **Description:** Alex works evening hours and frequently adjusts app preferences in low-light environments. They want a comfortable viewing experience when managing settings without eye strain, and they expect appearance choices to persist across sessions so they do not have to reconfigure the app each time they open it.

## User Story

- **As a** Night Shift Professional
- **I want to** enable dark mode from the settings page
- **so that** I can view and change my preferences comfortably in low-light conditions without unnecessary eye strain

## Acceptance Criteria

- WHEN I open the settings page THEN I SHALL see a clear option to switch between light and dark appearance
- WHEN I select dark mode THEN I SHALL see the settings page and surrounding interface change to a darker color scheme immediately
- WHEN I select light mode THEN I SHALL see the settings page return to a lighter color scheme immediately
- WHEN I leave the settings page and return later THEN I SHALL see the appearance mode I last selected still applied
- IF I have not changed appearance settings before THEN I SHALL see a sensible default appearance that matches my device's system preference when available
- WHILE dark mode is active THE USER SHALL be able to read all labels, controls, and status messages on the settings page without difficulty

## Success Metrics

- **Primary Metric:** A tester can toggle dark mode on from the settings page and confirm the interface switches to a darker appearance (pass/fail)
- **Secondary Metrics:**
  - A tester can toggle back to light mode and confirm the interface returns to a lighter appearance (pass/fail)
  - A tester can leave and reopen the settings page and confirm the selected appearance is still applied (pass/fail)
  - A tester can read all visible settings labels and controls in both light and dark modes without reported legibility issues (pass/fail)
