def calc_marks(maths, physics, chemistry):
    return maths + physics + chemistry
maths, physics, chemistry = map(int, input("Enter the marks for maths, physics, and chemistry separated by spaces: ").split())
print("Total marks:", calc_marks(maths, physics, chemistry))
