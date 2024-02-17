

def loading_process_part(index):
        animation_frames = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        index_frame = index % len(animation_frames)
        process_string = "{ info }" + " " + animation_frames[index_frame]
        return process_string
