# Description: This file contains the functions to write the code objects to a CSV file.

import csv


def write_python_to_csv(code_objects, generator="unknown"):
    python_total_code = len(code_objects)
    count = 1

    with open(f'Output/python_{generator}_code_objects.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            ['Title', 'Model', 'Code Type', 'LOC', 'Errors', 'options remain unchanged', 'trailing-whitespace',
             'undefined-variable', 'redefined-builtin', 'wildcard-import',
             'return-outside-function', 'bad-continuation', 'used-before-assignment', 'too-many-locals',
             'missing-docstring', 'too-few-public-methods', 'invalid-name', 'pointless-statement',
             'blacklisted-name', 'trailing-comma-tuple', 'parse-error', 'unused-import', 'bare-except',
             'anomalous-backslash-in-string', 'unused-argument', 'trailing-newlines', 'no-self-use',
             'import-error', 'redefined-outer-name', 'relative-beyond-top-level', 'line-too-long',
             'syntax-error', 'too-many-arguments', 'bad-whitespace', 'Other Errors'])

        for code in code_objects:
            try:
                print(f"({count}/{python_total_code}) {code.title}")
                count += 1

                if code.errors is not None:
                    if 'astroid-error' not in code.errors.keys():
                        # Count other errors
                        known_errors = ['options remain unchanged', 'trailing-whitespace', 'undefined-variable',
                                        'redefined-builtin', 'wildcard-import', 'return-outside-function',
                                        'bad-continuation',
                                        'used-before-assignment', 'too-many-locals', 'missing-docstring',
                                        'too-few-public-methods',
                                        'invalid-name', 'pointless-statement', 'blacklisted-name',
                                        'trailing-comma-tuple',
                                        'parse-error', 'unused-import', 'bare-except', 'anomalous-backslash-in-string',
                                        'unused-argument', 'trailing-newlines', 'no-self-use', 'import-error',
                                        'redefined-outer-name',
                                        'relative-beyond-top-level', 'line-too-long', 'syntax-error',
                                        'too-many-arguments',
                                        'bad-whitespace']
                        other_errors = 0
                        for key in code.errors.keys():
                            if key not in known_errors:
                                other_errors += int(code.errors.get(key, 0))

                        # Write code row to CSV
                        writer.writerow([code.title, code.model_used, code.code_language, code.eol, code.errors,
                                         code.errors.get('options remain unchanged', 0),
                                         code.errors.get('trailing-whitespace', 0),
                                         code.errors.get('undefined-variable', 0),
                                         code.errors.get('redefined-builtin', 0),
                                         code.errors.get('wildcard-import', 0),
                                         code.errors.get('return-outside-function', 0),
                                         code.errors.get('bad-continuation', 0),
                                         code.errors.get('used-before-assignment', 0),
                                         code.errors.get('too-many-locals', 0), code.errors.get('missing-docstring', 0),
                                         code.errors.get('too-few-public-methods', 0),
                                         code.errors.get('invalid-name', 0),
                                         code.errors.get('pointless-statement', 0),
                                         code.errors.get('blacklisted-name', 0),
                                         code.errors.get('trailing-comma-tuple', 0), code.errors.get('parse-error', 0),
                                         code.errors.get('unused-import', 0), code.errors.get('bare-except', 0),
                                         code.errors.get('anomalous-backslash-in-string', 0),
                                         code.errors.get('unused-argument', 0), code.errors.get('trailing-newlines', 0),
                                         code.errors.get('no-self-use', 0), code.errors.get('import-error', 0),
                                         code.errors.get('redefined-outer-name', 0),
                                         code.errors.get('relative-beyond-top-level', 0),
                                         code.errors.get('line-too-long', 0), code.errors.get('syntax-error', 0),
                                         code.errors.get('too-many-arguments', 0), code.errors.get('bad-whitespace', 0),
                                         other_errors])

            except Exception as e:
                print(f"Error: {e} on {code.title}")


def write_java_to_csv(code_objects, generator="unknown"):
    java_total_code = len(code_objects)
    count = 1

    with open(f'Output/java_{generator}_code_objects.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Title', 'Model', 'Code Type', 'LOC', 'Errors', 'UnnecessaryLocalBeforeReturn', 'NoPackage',
                         'UseLocaleWithCaseConversions', 'LiteralsFirstInComparisons', 'UnusedPrivateMethod',
                         'UnusedLocalVariable', 'UnusedPrivateField', 'UncommentedEmptyConstructor',
                         'UnusedFormalParameter', 'EmptyControlStatement', 'LooseCoupling', 'UseUtilityClass',
                         'UnnecessaryImport', 'Other Errors'])

        for code in code_objects:
            try:
                print(f"({count}/{java_total_code}) {code.title}")
                count += 1

                if code.errors is not None:
                    # Count other errors
                    known_errors = ['UnnecessaryLocalBeforeReturn', 'NoPackage', 'UseLocaleWithCaseConversions',
                                    'LiteralsFirstInComparisons', 'UnusedPrivateMethod', 'UnusedLocalVariable',
                                    'UnusedPrivateField', 'UncommentedEmptyConstructor', 'UnusedFormalParameter',
                                    'EmptyControlStatement', 'LooseCoupling', 'UseUtilityClass', 'UnnecessaryImport']
                    other_errors = 0
                    for key in code.errors.keys():
                        if key not in known_errors:
                            other_errors += int(code.errors.get(key, 0))

                    # Write code row to CSV
                    writer.writerow([code.title, code.model_used, code.code_language, code.eol, code.errors,
                                     code.errors.get('UnnecessaryLocalBeforeReturn', 0),
                                     code.errors.get('NoPackage', 0),
                                     code.errors.get('UseLocaleWithCaseConversions', 0),
                                     code.errors.get('LiteralsFirstInComparisons', 0),
                                     code.errors.get('UnusedPrivateMethod', 0),
                                     code.errors.get('UnusedLocalVariable', 0),
                                     code.errors.get('UnusedPrivateField', 0),
                                     code.errors.get('UncommentedEmptyConstructor', 0),
                                     code.errors.get('UnusedFormalParameter', 0),
                                     code.errors.get('EmptyControlStatement', 0), code.errors.get('LooseCoupling', 0),
                                     code.errors.get('UseUtilityClass', 0), code.errors.get('UnnecessaryImport', 0),
                                     other_errors])
            except Exception as e:
                print(f"Error: {e} on {code.title}")


def write_javascript_to_csv(code_objects, generator="unknown"):
    javascript_total = len(code_objects)
    count = 1

    with open(f'Output/javascript_{generator}_code_objects.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Title', 'Model', 'Code Type', 'LOC', 'Errors', 'Missing Semicolon', 'Unexpected Comma',
                         'Unnecessary Semicolon',
                         'Unclosed Regular Expression', 'String Formatting', 'Confusing Syntax',
                         'Closing Pair not Used',
                         'Labelling Error', 'Missing Initializer for Constant', 'Redeclaring Variables',
                         'Overriding Constants',
                         'Used before Declared', 'Use Restricted Word', 'Incorrect Identifier', 'Module Code Error',
                         'General Import Error', 'Operator Error', 'Unlocal Variable Call in Function', 'Dot Notation',
                         'Class properties Outside Methods', 'Duplicate Class Methods', 'Other Error'])

        for code in code_objects:
            try:
                print(f"({count}/{javascript_total}) {code.title}")
                count += 1

                if code.errors is not None:
                    # Count other errors
                    known_errors = ['missing semicolon', 'unexpected comma', 'unnecessary semicolon',
                                    'unclosed regular expression',
                                    'string formatting', 'confusing syntax', 'closing pair not used', 'labelling error',
                                    'missing initializer for constant', 'redeclaring variables', 'overriding constants',
                                    'used before declared', 'use restricted word', 'incorrect identifier',
                                    'module code error',
                                    'general import error', 'operator error', 'unlocal variable call in function',
                                    'dot notation',
                                    'class properties outside methods', 'duplicate class methods']
                    other_errors = 0
                    for key in code.errors.keys():
                        if key not in known_errors:
                            other_errors += int(code.errors.get(key, 0))

                    # Write code row to CSV
                    if code.errors is not None:
                        writer.writerow([code.title, code.model_used, code.code_language, code.eol, code.errors,
                                         code.errors.get('missing semicolon', 0),
                                         code.errors.get('unexpected comma', 0),
                                         code.errors.get('unnecessary semicolon', 0),
                                         code.errors.get('unclosed regular expression', 0),
                                         code.errors.get('string formatting', 0),
                                         code.errors.get('confusing syntax', 0),
                                         code.errors.get('closing pair not used', 0),
                                         code.errors.get('labelling error', 0),
                                         code.errors.get('missing initializer for constant', 0),
                                         code.errors.get('redeclaring variables', 0),
                                         code.errors.get('overriding constants', 0),
                                         code.errors.get('used before declared', 0),
                                         code.errors.get('use restricted word', 0),
                                         code.errors.get('incorrect identifier', 0),
                                         code.errors.get('module code error', 0),
                                         code.errors.get('general import error', 0),
                                         code.errors.get('operator error', 0),
                                         code.errors.get('unlocal variable call in function', 0),
                                         code.errors.get('dot notation', 0),
                                         code.errors.get('class properties outside methods', 0),
                                         code.errors.get('duplicate class methods', 0), other_errors])
            except Exception as e:
                print(f"Error: {e} on {code.title}")
