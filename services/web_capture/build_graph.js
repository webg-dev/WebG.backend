function buildGraph() {
    /* Returns Graph object containing nodes and edges of HTML DOM tree. */

    const nodes = [];
    const edges = [];

    const  allElements = document.querySelectorAll('*');

    for (const [id, element] of allElements.entries()) {

        element.setAttribute("webg_id", id.toString());
        let label = `${element.tagName} - ${id}`;
        let coordinates = element.getBoundingClientRect();
        let isVisible = isElementVisible(element, coordinates);
        let attributes = getAttributesMap(element);

        nodes.push(
            {
                id,
                label,
                attributes,
                coordinates,
                isVisible,
            }
        )

        if (element.parentElement !== null) {
            edges.push(
                {
                    from: parseInt(element.parentElement.getAttribute("webg_id")),
                    to: id
                }
            )
        }

    }

    console.log(`Finished building graph with ${allElements.length} nodes`);

    return { nodes, edges }
}

function isElementVisible(element, elementCoordinates){
    /* Returns true if element is visible to user else false.

    Note that elements outside the current viewport will be marked as not visible.
    This should be resolved by having a long viewport.
    * */
    const centerX = elementCoordinates.left + (elementCoordinates.width / 2);
    const centerY = elementCoordinates.top + (elementCoordinates.height / 2);
    const elementAtCentroid = document.elementFromPoint(centerX, centerY);
    const elementTopLeft = document.elementFromPoint(elementCoordinates.left + 1, elementCoordinates.top + 1);
    const elementTopRight = document.elementFromPoint(elementCoordinates.right - 1, elementCoordinates.top + 1);
    const elementBotLeft = document.elementFromPoint(elementCoordinates.left + 1, elementCoordinates.bottom - 1);
    const elementBotRight = document.elementFromPoint(elementCoordinates.right - 1, elementCoordinates.top + 1);

    const matchesElement = (elementAtPoint) =>  elementAtPoint === element;


    return [elementAtCentroid, elementTopLeft, elementTopRight, elementBotLeft, elementBotRight].some(matchesElement);
}

function getAttributesMap(element) {
    /* Returns Map containing name-value attribute pairs of element.*/
    const attributesArray = [...element.attributes];
    return attributesArray.reduce((map, obj) => (map[obj.name] = obj.value, map), {});
}


window.graph = buildGraph();
