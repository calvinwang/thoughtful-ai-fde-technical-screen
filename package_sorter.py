from enum import Enum

class PackageCategory(str, Enum):
    """
    Enumeration for package categories.

    Attributes:
        STANDARD: Represents a standard package.
        SPECIAL: Represents a bulky or heavy package.
        REJECTED: Represents a package that is rejected because it is heavy and bulky.
    """
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def sort(width: int, height: int, length: int, mass: int):
    """
    Classifies packages based on their dimensions and mass.

    Parameters:
        width (int): The width of the object in centimeters.
        height (int): The height of the object in centimeters.
        length (int): The length of the object in centimeters.
        mass (int): The mass of the object in kilograms.

    Returns:
        str: A string enum representing the category that the package should be dispatched as.

    Raises:
        ValueError: If any dimension or the mass is negative.

    Classification:
        - REJECTED: If the package is both heavy (mass >= 20kg) and bulky
                    (any dimension >= 150cm or volume >= 10**6 cm³).
        - SPECIAL:  If the package is exclusively either heavy or bulky.
        - STANDARD: If the package is neither heavy nor bulky.
    """
    if any(dimension <= 0 for dimension in (width, height, length)) or mass <= 0:
        raise ValueError("Zero or negative dimensions and/or mass. Cannot sort package!")

    is_heavy: bool = mass >= 20
    is_bulky: bool = max(width, height, length) >= 150 or width * height * length >= 10**6

    if is_heavy and is_bulky:
        return PackageCategory.REJECTED
    elif is_heavy or is_bulky:
        return PackageCategory.SPECIAL
    else:
        return PackageCategory.STANDARD
