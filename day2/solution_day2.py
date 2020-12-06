import pandas as pd

def read_input(path):
    """
        Reads multiline input of format "1-4 a: abcd" into a pandas.DataFrame
    """
    df_input = pd.read_csv(
        path,
        sep = '-|\s+|:\s',
        engine = 'python',
        names = ['min_char', 'max_char', 'char', 'password']
    )
    return df_input

def is_policy_compliantA(password_df):
    """
        Checks for each line of the password_df DataFrame if the password is
        compliant according to rule A
    """
    def is_compliant_dict(x):
        n = x["password"].count(x["char"])
        return x["min_char"] <= n <= x["max_char"]
    return password_df.apply(is_compliant_dict, axis = 1)

def is_policy_compliantB(password_df):
    """
        Checks for each line of the password_df DataFrame if the password is
        compliant according to rule B
    """
    def is_compliant_dict(x):
        isEq1, isEq2 = (
            x["password"][i - 1] == x["char"]
            for i in (x["min_char"], x["max_char"])
            )
        return isEq1 ^ isEq2
    return password_df.apply(is_compliant_dict, axis = 1)

def print_solution(compliance, problem):
    print(
        f'Solution to problem {problem}:\n'
        f'----------------------\n'
        f'Number of compliant pw: {sum(compliance)}\n'
        f'Not compliant pw: {len(compliance) - sum(compliance)}\n'
        )

if __name__ == "__main__":
    input_df = read_input("./day2/input.txt")
    complianceA = is_policy_compliantA(input_df)
    print_solution(complianceA, "2A")

    print()
    complianceB = is_policy_compliantB(input_df)
    print_solution(complianceB, "2B")
