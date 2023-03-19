import deeplabcut
import os

#config_path = "/rds/user/ech66/hpc-work/data/TestProject-Ed-2022-06-09/config.yaml/"
config_path = "/home/ech66/rds/hpc-work/data/TestProject-Ed-2022-06-09/config.yaml/" 

#VideoDir = os.path.join(os.path.split(config_path)[0], "videos")
VideoDir = r"/rds/user/ech66/hpc-work/data/TestProject-Ed-2022-06-09/videos"
#videofile_path = os.path.join(os.getcwd(),'/rds/user/ech66/hpc-work/data/TestProject-Ed-2022-06-09/videos/010522_GA_RML_M00708505_NM_CD_18wk.avi')

print("Analyze Videos")
#deeplabcut.analyze_videos(config_path,[VideoDir], videotype='.avi', save_as_csv=True, gputouse=os.environ.get("CUDA_VISIBLE_DEVICES"))
deeplabcut.analyze_videos(config_path,[VideoDir])
print("Video analysed")

#create labeled video
print("Creating labeled videos")
#deeplabcut.create_labeled_video(config_path, [VideoDir], save_frames=False, draw_skeleton=False)
deeplabcut.create_labeled_video(config_path,[VideoDir])
print("Labeled videos created")




