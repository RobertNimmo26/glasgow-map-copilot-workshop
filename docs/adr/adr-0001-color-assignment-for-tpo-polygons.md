---
title: "ADR-0001: Color Assignment Strategy for Tree Preservation Order Polygons"
status: "Proposed"
date: "2025-11-11"
authors: "Development Team"
tags: ["architecture", "decision", "visualization", "mapping"]
supersedes: ""
superseded_by: ""
---

## Status

**Proposed**

## Context

The Glasgow Map application displays Tree Preservation Order (TPO) polygons using Folium map visualization. The GeoJSON data contains multiple TPO areas, each identified by properties such as `AREANAME` or `EVNUMBER`. Currently, all TPO polygons are rendered in a single color (green), which makes it difficult for users to distinguish between different preservation areas when they overlap or are adjacent to each other.

**Key Constraints:**
- Users need to quickly identify and distinguish between different TPO areas on the map
- The application uses Folium for map rendering, which supports polygon styling
- GeoJSON data contains area identifiers that can be used for differentiation
- Accessibility requirements mandate that colors must be visually distinct and not rely solely on color for information (complementary tooltips/legends needed)
- The solution should scale to an arbitrary number of TPO areas without manual configuration

**Business Requirements:**
- Improve map clarity and user experience
- Enable quick visual identification of different preservation areas
- Support users with various visual capabilities (accessibility)
- Maintain consistent colors across sessions for the same areas

## Decision

We will implement a **deterministic hash-based color generation algorithm** that assigns unique, visually distinct colors to each TPO polygon based on its area identifier (prioritizing `EVNUMBER` if available, falling back to `AREANAME`).

**Implementation Approach:**
- Generate colors using a hash function applied to the area identifier
- Map hash values to HSL color space with controlled saturation and lightness for visual accessibility
- Provide a color legend showing all TPO areas and their assigned colors
- Add tooltips to polygons displaying the area name/number and other relevant metadata
- Cache color assignments to ensure consistency across map interactions

**Rationale:**
- Deterministic approach ensures the same area always receives the same color
- Hash-based generation eliminates the need for manual color configuration
- HSL color space allows better control over color distinctiveness and accessibility
- Scales automatically to any number of areas
- No additional configuration files or databases required

## Consequences

### Positive

- **POS-001**: Users can immediately distinguish between different TPO areas through visual color coding, improving map comprehension and usability
- **POS-002**: Deterministic color assignment ensures consistency across page loads and user sessions, providing a stable user experience
- **POS-003**: Automatic color generation scales to any number of TPO areas without manual configuration or maintenance overhead
- **POS-004**: HSL-based color generation allows control over saturation and lightness, ensuring colors are visually distinct and accessible to users with color vision deficiencies
- **POS-005**: Combined color coding with tooltips and legends provides multiple ways to identify areas, improving accessibility and meeting WCAG guidelines
- **POS-006**: No external dependencies or databases required for color assignment, keeping the implementation simple and maintainable

### Negative

- **NEG-001**: Hash-based color generation may occasionally produce colors that are not optimally distinct from each other, especially when many areas exist in close proximity
- **NEG-002**: Users cannot customize colors to their preferences without modifying the code
- **NEG-003**: Color assignments are not semantically meaningful (e.g., older areas don't automatically get different colors than newer ones)
- **NEG-004**: Implementation adds complexity to the rendering logic, requiring hash function and color space conversion code
- **NEG-005**: Testing color distinctiveness across all possible area combinations is challenging and may require manual verification
- **NEG-006**: Color blind users may still have difficulty distinguishing some adjacent areas even with HSL optimization, requiring reliance on tooltips and legends

## Alternatives Considered

### Alternative 1: Maintain Single Color for All Polygons

- **ALT-001**: **Description**: Continue using a single color (green) for all TPO polygons as currently implemented
- **ALT-002**: **Rejection Reason**: Fails to meet the core requirement of distinguishing between different TPO areas, resulting in poor user experience when areas overlap or are adjacent

### Alternative 2: Random Color Assignment

- **ALT-003**: **Description**: Assign random colors to each polygon on page load
- **ALT-004**: **Rejection Reason**: Colors would change between sessions, creating confusion for users and making it impossible to reference specific areas consistently

### Alternative 3: Manual Color Configuration File

- **ALT-005**: **Description**: Create a JSON or YAML configuration file mapping area identifiers to specific hex color codes
- **ALT-006**: **Rejection Reason**: Requires manual maintenance when new TPO areas are added, does not scale well, and increases operational overhead

### Alternative 4: Sequential Color Palette

- **ALT-007**: **Description**: Use a predefined color palette (e.g., ColorBrewer) and assign colors sequentially to areas in alphabetical order
- **ALT-008**: **Rejection Reason**: Limited to the number of colors in the palette, may not provide sufficient distinct colors for all areas, and requires maintaining palette data

### Alternative 5: Color by Temporal Properties

- **ALT-009**: **Description**: Assign colors based on date properties in the GeoJSON data, using a gradient from older to newer preservation orders
- **ALT-010**: **Rejection Reason**: Not all areas may have comparable date properties, and temporal meaning may not be the most useful distinction for users

### Alternative 6: Category-Based Color Coding

- **ALT-011**: **Description**: Group TPO areas by type or category and assign colors based on these categories
- **ALT-012**: **Rejection Reason**: Requires categorical metadata that may not exist in the current GeoJSON data, and does not distinguish between individual areas within the same category

## Implementation Notes

- **IMP-001**: Implement a Python function to generate colors from area identifiers using hashlib (SHA-256) for consistent hashing across sessions
- **IMP-002**: Convert hash values to HSL color space with saturation between 60-80% and lightness between 45-65% to ensure accessibility and visual distinctiveness
- **IMP-003**: Create a Folium legend control displaying all area identifiers with their assigned colors, positioned in the top-right corner of the map
- **IMP-004**: Add Folium tooltips and popups to each polygon displaying the area name, EVNUMBER, and any other relevant metadata from the GeoJSON properties
- **IMP-005**: Test color distinctiveness with a variety of color vision simulation tools (e.g., Coblis, Color Oracle) to verify accessibility
- **IMP-006**: Document the color generation algorithm in code comments and include examples in the repository documentation
- **IMP-007**: Monitor user feedback after deployment to identify any issues with color distinctiveness or accessibility

## References

- **REF-001**: [Folium Documentation - GeoJSON Styling](https://python-visualization.github.io/folium/modules.html#folium.features.GeoJson)
- **REF-002**: [WCAG 2.1 Guidelines - Use of Color](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html)
- **REF-003**: [ColorBrewer - Color Advice for Maps](https://colorbrewer2.org/)
- **REF-004**: [Python hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
- **REF-005**: [HSL Color Space Accessibility](https://accessibility.blog.gov.uk/2019/02/11/using-the-gov-uk-colour-palette/)
