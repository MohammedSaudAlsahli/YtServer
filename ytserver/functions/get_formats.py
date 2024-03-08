from ytserver.models.format import Format
from ytserver.models.formats import Formats


def get_formats(formats: list[dict]) -> Formats:
    """
    Generates the formats dictionary based on the input formats list, and returns the Formats object.
    Parameters:
    - formats: a list of dictionaries representing different formats
    Returns:
    - Formats: the Formats object generated from the formats dictionary
    """
    formats_dict: dict[str, list] = {
        "audio": [],
        "video": [],
    }

    formats_list: list = []
    for item in formats:
        if (
            item.get("ext") == "mhtml"
            or item.get("protocol") == "m3u8_native"
            or item.get("acodec") == "none"
        ):
            pass
        else:
            formats_list.append(item)

    for item in formats_list:
        if item.get("vcodec") == "none":
            formats_dict["audio"].append(Format(**item))

        if (item.get("vcodec") or item.get("acodec")) != "none":
            formats_dict["video"].append(Format(**item))

    return Formats(**formats_dict)
