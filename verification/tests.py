"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, "2", 3, [[3], 1, {1: "one"}]], 1],
            "answer": 2
        },
        {
            "input": [{"one": 1, "two": [{1: "one", 2: "two"}, 1, "1", "one"]}, 1],
            "answer": 2
        },
        {
            "input": [{"one": [1, 2], "two": [{1: "one", 2: "two"}, (1, 2), "1", "one"]}, [1, 2]],
            "answer": 2
        },
        {
            "input": [5, 5],
            "answer": 1
        },
        {
            "input": [(5, 6, 2, "1"), 1],
            "answer": 0
        },
        {
            "input": [[[dict()], [[[3], (3, 5)]], (), []], 3],
            "answer": 2
        },
        {
            "input": [{1: "one"}, {2: "two"}, "two", ["two", {"two": "one"}], "two"],
            "answer": 3
        },
    ],
    "Extra": [
        {
            "input": [[], ()],
            "answer": 0
        },
    ]
}
