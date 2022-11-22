def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

print(find_needle(["hay", "more hay", "junk", "needle", "horse"]))