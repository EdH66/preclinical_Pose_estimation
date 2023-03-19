import deeplabcut
import os

config_path = "/rds/user/ech66/hpc-work/data/TestProject-Ed-2022-06-09/config.yaml"

#"/rds/user/ech66/hpc-work/data/TestProject-Ed-2022-06-09/config.yaml"

# Add new videos
# deeplabcut.add_new_videos('/rds/user/ech66/hpc-work/deeplabcut*', ['full path of video 4', 'full path of video 5'], copy_videos=True/False)

#Train new videos

#VideoDir = os.path.join(os.path.split(config)[0], "videos")
VideoDir = "/rds/user/ech66/hpc-work/Workshop_DLC_20220916/LMB_Pupil_test-ECH-2022-09-16/Videos"

print("Analyze Videos")
deeplabcut.analyze_videos(config_path,[VideoDir], videotype='.avi', save_as_csv=True, gputouse=os.environ.get("CUDA_VISIBLE_DEVICES"))
print("Video analysed")

#create labeled video
print("Creating labeled videos")
deeplabcut.create_labeled_video(config_path, [VideoDir], save_frames=False, draw_skeleton=False)
print("Labeled videos created")




