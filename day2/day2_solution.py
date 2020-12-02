import pandas as pd
import operator

def read_input(path):
    df_input = pd.read_csv(
        path,
        sep = '-|\s+|:\s',
        engine = 'python',
        names = ['min_char', 'max_char', 'char', 'password']
    )
    return df_input

def is_policy_compliantA(pw_df):
    def is_compliant_dict(x):
        n = x["password"].count(x["char"])
        return n >= x["min_char"] and n <= x["max_char"]
    return pw_df.apply(is_compliant_dict, axis = 1)

def is_policy_compliantB(pw_df):
    def is_compliant_dict(x):
        letters = [x["password"][i - 1] \
            for i in (x["min_char"], x["max_char"])]
        return operator.xor(*(l == x["char"] for l in letters))
    return pw_df.apply(is_compliant_dict, axis = 1)

def print_solution(compliance, problem):
    print(
        f'Solution to problem {problem}:\n'
        f'----------------------\n'
        f'Number of compliant pw: {sum(compliance)}\n'
        f'Not compliant pw: {len(compliance) - sum(compliance)}\n'
        )

if __name__ == "__main__":
    input_df = read_input("input.txt")
    complianceA = is_policy_compliantA(input_df)
    print_solution(complianceA, "2A")

    print()
    complianceB = is_policy_compliantB(input_df)
    print_solution(complianceB, "2B")
