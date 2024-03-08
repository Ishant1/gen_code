

def get_prompt_for_learning(code_text):
    return f"{code_text} Read this code, firstly give a summary of what is repo/code is about?if this code contains read me contents, read from there to give summary of the project. sub title: what are the languages used mainly , give percentage if possible. Based on the percentage and the code itslef, suggest learning materials of the language which is available on internet, like documentations. Search the learning materials related to language and the code provided it self on youtube and give me links. Another sub title , give up-skilling learning materials, can be from hackerrank and kaggle. sub content, explain the library used in the code base, give documentation on huggingface, related tutorials on w3school search the library used on huggingface and give links. All the link must be valid and up to date."


def get_prompt_for_testing(code_text):
    return f"""{code_text}\n\n As an expert code writing chat assistant that writes unit tests

Write comprehensive and concise unit tests in pytest for the code provided. The test script should cover all aspects of the module's functionality, including:

    Functionality: Test the core functionality of the module with both valid and invalid inputs.
    Edge Cases: Explore boundary conditions and scenarios that may cause unexpected behavior.
    Corner Cases: Test the module's behavior in unusual or extreme circumstances.
    Input Types: Verify that the module handles different input types as expected.
    Output Verification: Check that the module produces the correct output or behavior for each test case.
    Error Handling: Test how the module responds to invalid inputs or exceptional conditions.

Additional Considerations:

    Follow established unit testing guidelines and standards.
    Aim for 100% code coverage.
    Use test fixtures and test parameters where appropriate to reduce code duplication and improve maintainability.
    Consider using a test coverage tool to ensure that all of the code in the module is being tested.
    Write meaningful error messages in your tests to help with debugging.
    Organize your test cases into modules, classes, and methods in a logical way.
    Name your test methods and classes descriptively.

Expected Outcome:

A robust and thorough unit test script that validates all aspects of the module's functionality and behavior.

Notes:

    Please use the pytest framework for writing the test script."""