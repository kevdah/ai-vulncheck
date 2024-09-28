from pydriller import Repository
import json

def process_changed_methods():
    # Get the two most recent commits in the repository
    repo = Repository('.', only_modifications_with_file_types=['.py']).traverse_commits()
    
    # Retrieve commits in reverse order (so the latest commit is first)
    commits = list(repo)[-2:]
    if len(commits) < 2:
        print("Not enough commits to compare.")
        return

    latest_commit = commits[0]
    second_latest_commit = commits[1]
    method_changes = {}

    #print(f"Analyzing changes between latest commit ({latest_commit.hash}) and previous commit ({second_latest_commit.hash})")

    for modification in latest_commit.modified_files:
        # Only process Python files
        if modification.filename.endswith('.py'):
            #print(f"Processing file: {modification.filename}")

            # Parsing the old and new methods using the diff
            for method in modification.changed_methods:
                #print(f"Modified Method: {method.name}")
                # Get JSON structure
                method_json = process_method(method, modification)
                method_changes['functions'] = [method_json] if not 'functions' in method_changes else method_changes['functions'].append(method_json)
    output_json = json.dumps(method_changes)
    print(output_json)
    return output_json


def process_method(method, filechange):
    method_name = method.name
    method_code = '\n'.join(filechange.source_code.splitlines()[method.start_line-1:method.end_line+1]) if filechange.source_code else "Source code not available"
    
    # Return JSON structure for the method
    return {method_name: method_code}

if __name__ == "__main__":
    process_changed_methods()
