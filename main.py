def basicFunction(arg1):
    print(f"This is a basicFunction and it got {arg1} as an argument")

def funcFeatureA(arg1, arg2):
    print(f"This is a funcFeatureA and it got {arg1} and {arg2} as arguments")
    print(f"Also arguments have type {type(arg1)} and {type(arg2)}")
    print(f"This is also a feature that we want to backport to main branch")

def funcNewFeatureA(arg1, arg2):
    print(f"This is a funcFeatureA and it got {arg1} and {arg2} as arguments")
    print(f"Also arguments have type {type(arg1)} and {type(arg2)}")
    print(f"This is also a feature that we do not want to backport to main branch")

def funcAnotherNewFeatureA():
    print("FeatureA branch went even further in development since diverging")