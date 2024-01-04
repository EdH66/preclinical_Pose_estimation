import deeplabcut
import os

# add perhaps config path as input function
config = "/beegfs3/dmalmazet/M5-DdM-2022-08-25/config.yaml"

# Create Training dataset
print("Creating Training Dataset")
deeplabcut.create_training_dataset(config,  net_type='resnet_50', augmenter_type='imgaug', windows2linux = True)
print("Training Dataset created")

# train
print("Training network")
deeplabcut.train_network(config, gputouse=os.environ.get("CUDA_VISIBLE_DEVICES"), maxiters=800000)
print("Network Trained")

# Evaluate
print("Evaluating network")
deeplabcut.evaluate_network(config, plotting=False, gputouse=os.environ.get("CUDA_VISIBLE_DEVICES"))
print("Network evaluated")

# get path movies
print("Analyzing videos")

VideoDir = os.path.join(os.path.split(config)[0], "videos")

# Train new videos (Check if previous training already has coordinates)
deeplabcut.analyze_videos(config,[VideoDir], videotype='.avi', save_as_csv=True, gputouse=os.environ.get("CUDA_VISIBLE_DEVICES"))
print("Video analyzed")

# create labeled data
print("Creating labeled videos")
deeplabcut.create_labeled_video(config, [VideoDir], save_frames=False, draw_skeleton=False)
print("Labeled videos created")
