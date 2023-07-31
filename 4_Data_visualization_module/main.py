import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os


def main():
    # To remove large margins
    st.set_page_config(layout="wide")

    # Siderbar selection (will redirect to each "web" page)
    st.sidebar.title("Menu")
    app_mode = st.sidebar.selectbox("", ["Introduction", "Charts", "Video analysis"])
    if app_mode == "Introduction":
        page0()
    elif app_mode == "Charts":
        page_charts()
    elif app_mode == "Video analysis":
        page_video_analysis()


def page_charts():
    data = pd.read_csv("inference_results.csv")
    counts = data["category"].value_counts()

    # Create a bar plot
    fig, ax = plt.subplots(figsize=(4, 3))
    counts.plot(kind="bar", ax=ax)

    # Set plot labels and title
    ax.set_xlabel("Categories")
    ax.set_ylabel("Count")
    ax.set_title("Bar Plot")

    # Display the plot in Streamlit
    st.pyplot(fig)


def page_video_analysis():
    for root, _, files in os.walk("./videos"):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if ".mp4" in file_path:
                with open(file_path, "rb") as video_file:
                    video_bytes = video_file.read()
                    st.write(file_path)
                    st.video(video_bytes, format="video/mp4")


def page0():  # Introduction
    # Display the logos of SystemX
    st.image("figures/system-x-logo.jpeg", width=200)

    # Write some text on the page
    st.write(read_local_file("page_0.txt"))


def read_local_file(path, extention="txt"):
    with open(path, encoding="utf-8") as file:
        if extention == "txt":
            content = file.read()
        elif extention == "csv":
            content = pd.read_csv(path)
    return content


if __name__ == "__main__":
    main()
