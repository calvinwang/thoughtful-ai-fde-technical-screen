from dataclasses import asdict, dataclass

import pytest

from package_sorter import sort, PackageCategory

@dataclass
class Package:
  """
  Represents a package with width, height, and length in centimeters, and mass.

  Heavy packages weigh 20kg or more.
  Bulky packages have volumes equal to or exceeding 10**6 cubic centimeters OR have any dimension greater than 150cm.
  """
  width: int
  height: int
  length: int
  mass: int

# Test Fixtures

@pytest.fixture
def standard_package():
  """
  A standard package that is neither heavy nor bulky.
  """
  return Package(width=80, height=80, length=80, mass=10)

@pytest.fixture
def heavy_package():
  """
  A heavy package that isn't bulky.
  """
  return Package(width=80, height=80, length=80, mass=20)

@pytest.fixture
def voluminous_bulky_package():
  """
  A bulky package that isn't heavy and has a volume greater than or equal to 10**6 cm^3
  """
  return Package(width=100, height=100, length=100, mass=10)

@pytest.fixture
def dimensional_bulky_package():
  """
  This package is bulky because one of its dimensions equals or exceeds 150cm!
  It's also not voluminous and not heavy.
  """
  return Package(width=150, height=10, length=10, mass=10)

@pytest.fixture
def rejected_package():
  """
  This package is a tiny bit too heavy and a tiny bit too voluminous. We should reject it.
  """
  return Package(width=100, height=100, length=100, mass=20)

@pytest.fixture
def negative_length_package():
  """
  This package defies the laws of physics or someone entered the numbers wrong.
  """
  return Package(width=80, height=80, length=-100, mass=15)

@pytest.fixture
def weightless_package():
  """
  This package is levitating in the warehouse and freaking people out.
  """
  return Package(width=80, height=80, length=80, mass=0)

# Test functions
def test_standard(standard_package):
    result = sort(**asdict(standard_package))
    assert result == PackageCategory.STANDARD

def test_heavy(heavy_package):
    result = sort(**asdict(heavy_package))
    assert result == PackageCategory.SPECIAL

def test_voluminous_bulky_package(voluminous_bulky_package):
    result = sort(**asdict(voluminous_bulky_package))
    assert result == PackageCategory.SPECIAL

def test_dimensional_bulky_package(dimensional_bulky_package):
    result = sort(**asdict(dimensional_bulky_package))
    assert result == PackageCategory.SPECIAL

def test_rejected_package(rejected_package):
    result = sort(**asdict(rejected_package))
    assert result == PackageCategory.REJECTED

def test_negative_length_package(negative_length_package):
    with pytest.raises(ValueError):
        sort(**asdict(negative_length_package))

def test_weightless_package(weightless_package):
    with pytest.raises(ValueError):
       sort(**asdict(weightless_package))
