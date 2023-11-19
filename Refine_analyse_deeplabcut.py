import deeplabcut
import os
import glob

config_path = "/rds/user/ech66/hpc-work/data/DLC_TRN_MOTOR_021022-ECH-2022-11-02/config.yaml"
 
deeplabcut.merge_datasets(config_path)

print("Creating Training Dataset")
deeplabcut.create_training_dataset(config_path, augmenter_type='imgaug')
print("Network Trained")

# ImageNet pre-trained networks (i.e. ResNet-50, ResNet-101 and ResNet-152, etc) should download now

# Start network training

deeplabcut.train_network(config_path, shuffle=1, displayiters=100, saveiters=1000, maxiters=200000)

# Train network non-default
# deeplabcut.train_network(/rds/user/ech66/hpc-work/deeplabcut/config.yaml, shuffle=1, trainingsetindex=0, gputouse=None, max_snapshots_to_keep=5, autotune=False, displayiters=100, saveiters=15000, maxiters=30000, allow_growth=True)

# Evaluate network

deeplabcut.evaluate_network(config_path, plotting=True)

# deeplabcut.evaluate_network(config_path,Shuffles=[1], plotting=True)

# Directory containing the videos to be added
VideoDir = "/rds/user/ech66/hpc-work/data/DLC_TRN_MOTOR_021022-ECH-2022-11-02/videos/"

# Fetching all .avi videos from the video directory
video_paths = glob.glob(os.path.join(VideoDir, '*.avi'))

# Add new videos
deeplabcut.add_new_videos(config_path, video_paths, copy_videos=False)

print("Analyze Videos")
deeplabcut.analyze_videos(config_path, [VideoDir], videotype='.avi', save_as_csv=True, gputouse=os.environ.get("CUDA_VISIBLE_DEVICES"))
print("Video analysed")

create labeled video
print("Creating labeled videos")
deeplabcut.create_labeled_video(config, [VideoDir], save_frames=False, draw_skeleton=False)
print("Labeled videos created")
