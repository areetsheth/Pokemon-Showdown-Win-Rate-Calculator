from backend import collect_data
# import json


def test_load_csv():
    # Ensure dataframe exists
    assert collect_data.load_csv() is not None


'''
Commenting out this test because the necessary .json file is not in the repo
This test can be used locally, but fails in the CI pipeline
'''
# def test_create_json():
#     # Cannot directly call api to test function because it is is costly
#     # Instead, we can ensure the .json file exists on one's local machine
#     with open('backend/data/pokeapi_data.json') as f:
#         data = json.load(f)
#     assert data is not None
