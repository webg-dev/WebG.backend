window.buildGraph = function buildGraph() {
    const nodes = [];
    const edges = [];

    let allElements = document.querySelectorAll('*');
    for (const [id, element] of allElements.entries()) {
        element.setAttribute("webg_id", id.toString());

        let label = element.tagName;
        let coordinates = element.getBoundingClientRect();
        let centerX = coordinates.left + (coordinates.width / 2);
        let centerY = coordinates.top + (coordinates.height / 2);
        // note elementFromPoint will return null for points outside of the
        // current viewport. This will be fixed later by using a large viewport
        // in headless mode.
        let elementAtCentroid = document.elementFromPoint(centerX, centerY);
        let visible = element === elementAtCentroid;

        const attributesArray = [...element.attributes];
        const attributes = attributesArray.reduce((map, obj) => (map[obj.name] = obj.value, map), {});

        nodes.push(
            {
                id,
                label,
                attributes,
                coordinates,
                visible,
            }
        )

    }

    console.log(`Finished building graph with ${allElements.length} nodes`);

    return {nodes}
}

window.graph = buildGraph();
