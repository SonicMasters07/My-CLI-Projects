def main():
    Table_of = int(input("Enter the table you want: "))
    Range = int(input("Define a range at which table will end: "))
    for table in range(1, Range+1):
        answer = Table_of * (table)
        print(f"{Table_of} * {table} = {answer}")
main()