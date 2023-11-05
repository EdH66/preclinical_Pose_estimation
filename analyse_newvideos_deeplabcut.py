import deeplabcut
import os
import glob


# Path to the config file
config_path = "/rds/user/ech66/hpc-work/data/DLC_TRN_MOTOR_021022-ECH-2022-11-02/config.yaml"

# Directory containing the videos to be added
VideoDir = "/rds/user/ech66/hpc-work/data/DLC_TRN_MOTOR_021022-ECH-2022-11-02/videos/"

# Fetching all .avi videos from the video directory
video_paths = glob.glob(os.path.join(VideoDir, '*.avi'))

# Add new videos
deeplabcut.add_new_videos(config_path, video_paths, copy_videos=False)

print("Analyze Videos")
deeplabcut.analyze_videos(config_path, [VideoDir], videotype='.avi', save_as_csv=True, gputouse=os.environ.get("CUDA_VISIBLE_DEVICES"))
print("Video analysed")

#create labeled video
#print("Creating labeled videos")
#deeplabcut.create_labeled_video(config, [VideoDir], save_frames=False, draw_skeleton=False)
#print("Labeled videos created")
