
import streamlit as st
import cv2
import tempfile
import mediapipe as mp
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

st.title("🤺 Kalari Pose Feedback App")

uploaded_file = st.file_uploader("Upload your practice video (.mp4)", type=["mp4"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_path = tfile.name

    cap = cv2.VideoCapture(video_path)
    pose = mp.solutions.pose.Pose()
    student_pose = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        if results.pose_landmarks:
            keypoints = []
            for lm in results.pose_landmarks.landmark:
                keypoints.extend([lm.x, lm.y, lm.z])
            student_pose.append(keypoints)

    cap.release()
    df = pd.DataFrame(student_pose)
    st.success(f"✅ Pose data extracted! {len(df)} frames.")

    # Load master pose
    master_pose = pd.read_csv("ideal_pose.csv").mean().values.reshape(1, -1)
    student_avg = df.mean().values.reshape(1, -1)

    score = cosine_similarity(student_avg, master_pose)[0][0]
    st.subheader(f"🧠 Pose Similarity Score: {score*100:.2f}%")

    if score > 0.9:
        st.success("🎉 Great posture! You’ve nailed it!")
    elif score > 0.8:
        st.warning("🙂 Almost perfect — Slight correction needed.")
    else:
        st.error("⚠️ Needs improvement. Try checking your leg and spine alignment.")
