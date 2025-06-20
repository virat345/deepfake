
import os
from roop import face_swapper, face_enhancer, video_helper

def run():
    print("✅ Starting face swap pipeline...")

    # Define paths
    source_path = "source.jpg"
    target_path = "target.mp4"
    output_path = "face_changed_video.mp4"
    temp_dir = "temp_frames"

    # Step 1: Extract frames from target video
    print("📽️ Extracting frames from target video...")
    frames = video_helper.extract_video_frames(target_path, temp_dir)

    # Step 2: Swap faces
    print("🔄 Swapping faces in frames...")
    swapped_frames = []
    for i, frame in enumerate(frames):
        swapped = face_swapper.swap_face(frame, source_path)
        enhanced = face_enhancer.enhance_face(swapped)
        swapped_frames.append(enhanced)
        if i % 10 == 0:
            print(f"Processed frame {i+1}/{len(frames)}")

    # Step 3: Reconstruct video
    print("🎞️ Rebuilding video from frames...")
    video_helper.create_video_from_frames(swapped_frames, output_path, target_path)

    print(f"✅ Done! Output saved to: {output_path}")
