from github import get_diff
from ai import review_code

# filter diff
def clean_diff(diff_text):
    lines = diff_text.split("\n")

    filtered = []
    skip = False

    for line in lines:
        # skip.pyc
        if line.startswith("diff --git") and ".pyc" in line:
            skip = True
            continue

        # if file not .pyc → re-read
        if line.startswith("diff --git") and ".pyc" not in line:
            skip = False

        if not skip:
            filtered.append(line)

    return "\n".join(filtered)


# main function of reviewer
def process_pr(pr):
    diff_url = pr.get("diff_url")

    # 1. pull diff from GitHub
    diff = get_diff(diff_url)

    if not diff:
        return None

    # 2. clean diff
    diff = clean_diff(diff)

    # 3. limit prevent error
    diff = diff[:3000]

    print("===== CLEAN DIFF =====")
    print(diff[:500])

    # 4. send to AI
    review = review_code(diff)

    return review