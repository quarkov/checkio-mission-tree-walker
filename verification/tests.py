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
            "input": [{"one": [1, 2], "two": [{1: "one", 2: "two"}, [1, 2], "1", "one"]}, [1, 2]],
            "answer": 2
        },
        {
            "input": [5, 5],
            "answer": 1
        },
        {
            "input": [[5, 6, 2, "1"], 1],
            "answer": 0
        },
        {
            "input": [[[dict()], [[[3], [3, 5]]], [], []], 3],
            "answer": 2
        },
        {
            "input": [[{1: "one"}, {2: "two"}, "two", ["two", {"two": "one"}]], "two"],
            "answer": 3
        },
    ],
    "Extra": [
        {
            "input": [[], []],
            "answer": 1
        },
        {
            "input": [
                [{
                    "one": [["checkio"], "checkio", {"checkio": 4, "py": 5}],
                    "two": ["aaa", "bbb", "check", {"six": 6, "seven": 7}],
                    "three": ["checkio", {"checkio": "checkio", 1: "checkio"}, {"8": "checkio", "9": 9}]
                }], "checkio"],
            "answer": 6
        },
        {
            "input": [
                [[{
                    "one": [["checkio"], "checkio", {"checkio": 4, "py": 5}],
                    "two": ["aaa", "bbb", "check", {"six": 6, "seven": 7}],
                    "three": ["checkio", {"checkio": "checkio", 1: "checkio"}, {"8": "checkio", "9": 9}]
                }]], "checkio"],
            "answer": 6
        },
        {
            "input": [
                [[[[[[[[[[{
                    "one": [["checkio"], "checkio", {"checkio": 4, "py": 5}],
                    "two": ["aaa", "bbb", "check", {"six": 6, "seven": 7}],
                    "three": ["checkio", {"checkio": "checkio", 1: "checkio"}, {"8": "checkio", "9": 9}]
                }]]]]]]]]]], "checkio"],
            "answer": 6
        },
        {
            "input": [dict(), {}],
            "answer": 1
        },
        {
            "input": [[1, [2, [3, [4, [5, [6, [7, [8, [9, [1]]]]]]]]]], 1],
            "answer": 2
        },
        {
            "input": [[1, [2, [3, [4, [5, [6, [7, [8, [9, [1]]]]]]]]]], [9, [1]]],
            "answer": 1
        },
        {
            "input": [[1, [2, [3, [4, [5, [6, [7, [8, [9, [1]]]]]]]]]], [1, [2]]],
            "answer": 0
        },
        {
            "input": [[1, [2, [3, [4]]]], [1, [1, [1, [1]]]]],
            "answer": 0
        },
        {
            "input": [[1, [1, [1, [1]]]], [1, [1, [1, [1]]]]],
            "answer": 1
        },
        {
            "input": [{1: {2: {3: {5: {6: {7: {8: {9: 10}}}}}}}}, 10],
            "answer": 1
        },
        {
            "input": [{1: {2: {3: {5: {6: {7: {8: {9: 10}}}}}}}}, 1],
            "answer": 0
        },
        {
            "input": [dict(dict(dict(dict(dict(dict(dict())))))), dict()],
            "answer": 1
        }
    ]
}
