import deeplabcut

# Create a project


project_name = "cutemice"
experimenter = "teamdlc"
video_path = "path_to_a_video_file"
config_path = deeplabcut.create_new_project(
    project_name,
    experimenter,
    [video_paths],
    multianimal=True,
    copy_videos=True,
)

# Dont forget to edit the config.ymal

# Extract video frames to annotate

deeplabcut.extract_frames(
    config_path,
    mode="automatic",
    algo="kmeans",
    userfeedback=False,
)

# Annotate Frames

deeplabcut.label_frames(config_path)

# Visually check annotated frames

# Create the training dataset

deeplabcut.check_labels(
    config_path,
    draw_skeleton=False,
)

# Train the network

deeplabcut.create_multianimaltraining_dataset(
    config_path,
    num_shuffles=1,
    net_type="dlcrnet_ms5",
)

deeplabcut.evaluate_network(
    config_path,
    plotting=True,
)