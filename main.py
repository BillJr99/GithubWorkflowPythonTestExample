# https://docs.pytest.org/en/7.2.x/
# https://github.com/BillJr99/GithubWorkflowPythonTestExample
# workflow from https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python


# content of test_sample.py
def inc(x):
  return x + 1


if __name__ == "__main__":
  print(inc(2))
