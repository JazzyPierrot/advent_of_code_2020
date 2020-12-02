import pandas as pd

def read_input(path):
    df_input = pd.read_csv(
        path,
        sep = '-|\s+|:\s',
        engine = 'python',
        names = ['min_char', 'max_char', 'char', 'password']
    )
    return df_input

def is_policy_compliant(pw_dict):
    n = pw_dict["password"].count(pw_dict["char"])
    return n >= pw_dict["min_char"] and n <= pw_dict["max_char"]

def print_solution(compliance, problem):
    print(
        f'Solution to problem {problem}:\n'
        f'----------------------\n'
        f'Number of compliant pw: {sum(compliance)}\n'
        f'Not compliant pw: {len(compliance) - sum(compliance)}\n'
        )

if __name__ == "__main__":
    input_df = read_input("input.txt")
    compliance = input_df.apply(is_policy_compliant, axis = 1)
    print_solution(compliance, "2A")




