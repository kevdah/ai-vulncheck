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

    old_commit = commits[0]
    this_commit = commits[1]
    print(f"comparing {this_commit.hash} against {old_commit.hash}")
    method_changes = {}
    supported_langs = ('.py', '.java')

    #print(f"Analyzing changes between latest commit ({latest_commit.hash}) and previous commit ({second_latest_commit.hash})")

    for modification in this_commit.modified_files:
        # Only process Python files
        if modification.filename.endswith(supported_langs):
            #print(f"Processing file: {modification.filename}")

            # Parsing the old and new methods using the diff
            for method in modification.changed_methods:
                #print(f"Modified Method: {method.name}")
                # Get JSON structure
                method_json = process_method(method, modification)
                
                # Check if 'functions' key exists, if not, initialize it as an empty list
                if 'functions' not in method_changes:
                    method_changes['functions'] = []
            
                # Append the method_json to the 'functions' list
                method_changes['functions'].append(method_json)
    output_json = json.dumps(method_changes)
    return output_json


def process_method(method, filechange):
    s_line = method.start_line
    e_line = method.end_line
    method_code = '\n'.join(filechange.source_code.split('\n')[s_line-1:e_line]) if filechange.source_code else "Source code not available"
    
    # Return JSON structure for the method
    return {method.name: method_code}

if __name__ == "__main__":
    method_changes = process_changed_methods()
    with open("function_changes.json", "w") as f:
        f.write(method_changes)
