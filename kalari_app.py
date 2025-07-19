
import streamlit as st
import cv2
import tempfile
try:
    import mediapipe as mp
except ModuleNotFoundError:
    mp = None

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
try:
    import mediapipe as mp
except ModuleNotFoundError:
    mp = None

if mp is not None:
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        st.info("Pose detection is enabled.")
        # For now, just pass or put your future logic here
        pass
else:
    st.warning("⚠️ Pose detection is currently disabled because MediaPipe is not installed.")

try:
    import mediapipe as mp
except ImportError:
    mp = None
if mp is None:
    st.warning("Pose detection is currently disabled because MediaPipe is not installed.")
else:
    with mp.solutions.pose.Pose(...) as pose:
        # your pose detection code here

try:
    import mediapipe as mp
except ImportError:
    mp = None

if mp is None:
    st.warning("⚠️ Pose detection is currently disabled because MediaPipe is not installed in this environment.")
else:
    # Setup Mediapipe pose detection
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    # You can wrap this in a function or place inside your video frame loop
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        # Example processing (replace with your actual loop)
        st.info("Pose detection is enabled.")
        # Normally you'd process frames from webcam or uploaded video here
        # Example:
        # results = pose.process(frame)
        # mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

