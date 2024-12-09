import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


def analyze():
    df = pd.read_csv("companies_analysis.csv")

    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x="Procon Atendidas %",
        y="Reclame Aqui Taxa Resolução %",
        data=df,
        hue="Company",
        palette="Set1",
        s=100,
    )
    plt.title("Procon Atendidas % vs Reclame Aqui Taxa Resolução %")
    plt.xlabel("Procon Atendidas %")
    plt.ylabel("Reclame Aqui Taxa Resolução %")
    plt.legend(title="Company", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True)
    plt.show()

    ######
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x="Reclame Aqui Reclamações",
        y="Reclame Aqui Taxa Resolução %",
        data=df,
        hue="Company",
        palette="Set2",
        s=100,
    )
    plt.title("Reclame Aqui Reclamações vs Reclame Aqui Taxa Resolução %")
    plt.xlabel("Reclame Aqui Reclamações")
    plt.ylabel("Reclame Aqui Taxa Resolução %")
    plt.legend(title="Company", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True)
    plt.show()

    df["Total Complaints"] = df["Procon Total"] + df["Reclame Aqui Reclamações"]

    ######
    # plt.figure(figsize=(12, 6))
    # sns.barplot(
    #     x="Company",
    #     y="Reclame Aqui Reclamações",
    #     data=df,
    #     color="blue",
    #     label="Complaints",
    #     ci=None,
    # )
    # sns.barplot(
    #     x="Company",
    #     y="Reclame Aqui Tempo Resposta (days)",
    #     data=df,
    #     color="orange",
    #     label="Response Time (Days)",
    #     ci=None,
    # )
    # plt.title("Complaints vs Time to Response by Company")
    # plt.xlabel("Company")
    # plt.ylabel("Count / Time (Days)")
    # plt.xticks(rotation=90)
    # plt.legend(title="Metrics", bbox_to_anchor=(1.05, 1), loc="upper left")
    # plt.grid(True)
    # plt.show()

    ######
    # Scatter Plot: Procon Complaints vs Reclame Aqui Complaints by Company
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x="Procon Total",
        y="Reclame Aqui Reclamações",
        data=df,
        hue="Company",
        palette="Set1",
        s=100,
    )
    plt.title("Procon Complaints vs Reclame Aqui Complaints")
    plt.xlabel("Procon Total Complaints")
    plt.ylabel("Reclame Aqui Complaints")
    plt.legend(title="Company", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True)
    plt.show()

    #####
    # RANKS

    # Ranking Companies based on Procon Attended %
    df["Procon Attended % Rank"] = df["Procon Atendidas %"].rank(ascending=False)

    # Ranking Companies based on Reclame Aqui Resolution Rate %
    df["Reclame Aqui Taxa Resolução % Rank"] = df["Reclame Aqui Taxa Resolução %"].rank(
        ascending=False
    )

    # Ranking Companies based on Reclame Aqui Response Rate %
    df["Reclame Aqui Taxa Resposta % Rank"] = df["Reclame Aqui Taxa Resposta %"].rank(
        ascending=False
    )

    # Ranking Companies based on Procon Total Complaints
    df["Procon Total Complaints Rank"] = df["Procon Total"].rank(ascending=False)

    # Ranking Companies based on Reclame Aqui Complaints
    df["Reclame Aqui Complaints Rank"] = df["Reclame Aqui Reclamações"].rank(
        ascending=False
    )

    # Show the rankings for the first few companies
    df[
        [
            "Company",
            "Procon Attended % Rank",
            "Reclame Aqui Taxa Resolução % Rank",
            "Reclame Aqui Taxa Resposta % Rank",
            "Procon Total Complaints Rank",
            "Reclame Aqui Complaints Rank",
        ]
    ]

    # Plotting Procon Attended % Rank
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Procon Attended % Rank", y="Company", data=df, palette="Blues_d")
    plt.title("Companies Ranked by Procon Attended %")
    plt.xlabel("Procon Attended % Rank")
    plt.ylabel("Company")
    plt.show()

    # Plotting Reclame Aqui Resolution Rate Rank
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x="Reclame Aqui Taxa Resolução % Rank", y="Company", data=df, palette="Greens_d"
    )
    plt.title("Companies Ranked by Reclame Aqui Resolution Rate")
    plt.xlabel("Reclame Aqui Resolution Rate Rank")
    plt.ylabel("Company")
    plt.show()
