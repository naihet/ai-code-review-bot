from github import get_diff
from ai import review_code

# filter diff
def clean_diff(diff_text):
    lines = diff_text.split("\n")

    filtered = []
    skip = False

    for line in lines:
        # new files
        if line.startswith("diff --git"):
            # if not wanted files
            if "__pycache__" in line or ".pyc" in line:
                skip = True
            else:
                skip = False

        # if not skip -> save
        if not skip:
            filtered.append(line)

    return "\n".join(filtered)


# main function of reviewer
def process_pr(pr):
    diff_url = pr.get("diff_url")

    # 1. pull diff
    diff = get_diff(diff_url)

    if not diff:
        print("Failed to get diff")
        return None

    # 2. CLEAN
    diff = clean_diff(diff)

    # 3. limit size before send to AI
    trimmed_diff = diff[:3000]

    # 🔍 LOG: Diff
    print("\n===== CLEAN DIFF =====")
    print(trimmed_diff[:1000])  # preview
    print("===== END DIFF =====\n")

    # 4. send to AI
    review = review_code(trimmed_diff)

    # 🔍 LOG: AI Result
    print("===== AI REVIEW =====")
    print(review)
    print("===== END REVIEW =====\n")

    return review