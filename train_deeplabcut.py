import deeplabcut
import os

config_path = "/rds/user/ech66/hpc-work/data/DLC_TRN_191022_v2-ECH-2022-10-22/config.yaml"
 
#"/rds/user/ech66/hpc-work/data/TestProject-Ed-2022-06-09/config.yaml"

# Add new videos
# deeplabcut.add_new_videos('/rds/user/ech66/hpc-work/deeplabcut*', ['full path of video 4', 'full path of video 5'], copy_videos=True/False)

# Extract Frames
# deeplabcut.extract_frames(/rds/user/ech66/hpc-work/deeplabcut/config.yaml, mode='automatic/manual', algo='uniform/kmeans', userfeedback=False, crop=True/False)

# Manual add frames 
# deeplabcut.extract_frames(/rds/user/ech66/hpc-work/deeplabcut/config.yaml, 'manual')

# label frames
# deeplabcut.label_frames(/rds/user/ech66/hpc-work/deeplabcut/config.yaml)

# check labels
# deeplabcut.label_frames(/rds/user/ech66/hpc-work/deeplabcut/config.yaml)

# create training dataset
print("Creating Training Dataset")
deeplabcut.create_training_dataset(config_path, augmenter_type='imgaug')
print("Network Trained")

# ImageNet pre-trained networks (i.e. ResNet-50, ResNet-101 and ResNet-152, etc) should download now

# Start network training

deeplabcut.train_network(config_path, shuffle=1, displayiters=100, saveiters=1000, maxiters=400000)

# Train network non-default
# deeplabcut.train_network(/rds/user/ech66/hpc-work/deeplabcut/config.yaml, shuffle=1, trainingsetindex=0, gputouse=None, max_snapshots_to_keep=5, autotune=False, displayiters=100, saveiters=15000, maxiters=30000, allow_growth=True)

# Evaluate network

deeplabcut.evaluate_network(config_path, plotting=True)

# deeplabcut.evaluate_network(config_path,Shuffles=[1], plotting=True)

#Train new videos

#VideoDir = os.path.join(os.path.split(config)[0], "videos")
#VideoDir = /rds/user/ech66/hpc-work/data/TestProject-Ed-2022-06-09/videos

#print("Analyze Videos")
#deeplabcut.analyze_videos(config,[VideoDir], videotype='.avi', save_as_csv=True, gputouse=os.environ.get("CUDA_VISIBLE_DEVICES"))
#print("Video analysed")

#create labeled video
#print("Creating labeled videos")
#deeplabcut.create_labeled_video(config, [VideoDir], save_frames=False, draw_skeleton=False)
#print("Labeled videos created")
