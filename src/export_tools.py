import pandas as pd
import os

def export_excel(data, path):
    df = pd.DataFrame(data)
    df.to_excel(path, index=False)


def export_report(text, path):
    with open(path, "w") as f:
        f.write(text)
