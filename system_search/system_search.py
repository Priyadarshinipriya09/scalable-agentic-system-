import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if project_root not in sys.path:
    sys.path.append(project_root)

from app.tool_registry import tools


def search_system(query):

    query = query.lower()

    stop_words = {
        "i", "want", "a", "an", "the", "for",
        "is", "there", "from", "to", "please",
        "can", "you", "me", "my", "give", "show"
    }

    words = query.replace("?", "").replace("$", "").split()


    words = [word for word in words if not word.isdigit()]

    meaningful_words = []

    for word in words:
        if word not in stop_words:
            meaningful_words.append(word)

    results = []

    # First, look for exact category matches
    for tool in tools:
        if tool["category"] in meaningful_words:
            if tool not in results:
                results.append(tool)

    # Then look for exact tool-name matches
    for tool in tools:
        tool_words = tool["name"].replace("_", " ").split()

        for word in meaningful_words:
            if word in tool_words:
                if tool not in results:
                    results.append(tool)

    # Return only the most relevant matches
    return results[:5]