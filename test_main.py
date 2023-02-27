from main import inc

# https://docs.pytest.org/en/7.2.x/
# pip install pytest
# run with: pytest


# execute with pytest
def test_answer():
  assert inc(3) == 5  # deliberately fails


def test_answer2():
  assert inc(3) == 4


def test_answer3():
  assert inc(-1) == 0
