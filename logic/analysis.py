def get_basic_stats(df):
    stats = []
    stats.append(f"Total Rows: {len(df)}")
    stats.append(f"Total Columns: {len(df.columns)}")
    stats.append(f"Columns: {', '.join(df.columns)}")
    stats.append("\nSummary Statistics:\n")
    stats.append(str(df.describe(include='all')))
    return '\n'.join(stats)
