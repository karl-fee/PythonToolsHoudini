# Global variable for bone count
bone_count = 0

# Recursively finds bone nodes starting from the specified node
def bone_finder(level, node):

    global bone_count

    if node.type().name() == "bone":
        print(f"{' ' * level}{node.name()}")
        bone_count += 1

    for child in node.outputs():
        bone_finder(level + 1, child)

    return bone_count

# Validate node selection
def validate_node(node):

    if node is None:
        raise ValueError("Please select a node.")

    if not node.path().startswith("/obj"):
        raise ValueError("The selected node must be in the /obj context.")

    return True

# Main function
def main():

    try:
        selected_node_path = hou.ui.selectNode(
            title="Please select a starting node:"
        )
        if not selected_node_path:
            print("No node selected. Exiting tool.")
            return

        selected_node = hou.node(selected_node_path)
        validate_node(selected_node)

        # Reset bone count
        global bone_count
        bone_count = 0

        # Run bone_finder function
        print(f"Starting bone search from: {selected_node.path()}")
        total_bones = bone_finder(0, selected_node)
        print(f"Bone count is: {total_bones}")

    except ValueError as ve:
        print(f"Validation error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

main()