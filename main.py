import os
# One-liner entry: the line below is the whole submission.
LINE = "Your data is safe. It lives in a backup nobody has tested since 2019, in a format nothing can read, on a server we cannot find."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
