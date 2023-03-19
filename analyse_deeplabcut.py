import deeplabcut
import os

config_path = "/rds/user/ech66/hpc-work/data/DLC_TRN_191022_v2-ECH-2022-10-22/config.yaml"
 
#deeplabcut.extract_save_all_maps(config_path, shuffles=shuffles, Indices=[0, 5]) # error on shuffles

VideoDir = os.path.join(os.path.split(config_path)[0], "videos")
#VideoDir = "/rds/user/ech66/hpc-work/data/TestProject-Ed-2022-06-09/config.yaml"

print("Analyze Videos")
deeplabcut.analyze_videos(config_path,[VideoDir], videotype='.avi', save_as_csv=True, dynamic=(True,.5,10), gputouse=os.environ.get("CUDA_VISIBLE_DEVICES"))
print("Video analysed")

print("Creating labeled videos")
deeplabcut.create_labeled_video(config_path, [VideoDir], save_frames=False, draw_skeleton=True)
print("Labeled videos created")

print("Extracting skeleton distances, filter and plot filtered output")
deeplabcut.analyzeskeleton(config_path, [VideoDir], save_as_csv=True)
deeplabcut.filterpredictions(config_path,[VideoDir])

#print("Plotting trajectories")
#deeplabcut.plot_trajectories(config_path, [VideoDir])
#print("Plotting trajectories complete")

