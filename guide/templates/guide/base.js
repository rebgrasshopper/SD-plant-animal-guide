function becomeWhole() {
    document.getElementById("detail_image").src="{{ plant.image_whole.url }}"
}

function becomeLeaf() {
    document.getElementById("detail_image").src="{{ plant.image_leaf.url }}"
}