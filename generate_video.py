
import cv2
import os
import glob

def generate_video(input_dir, output_file, fps=30, loops=2):
    # Get sorted list of images
    images = sorted(glob.glob(os.path.join(input_dir, "*.jpg")))
    if not images:
        print("No images found!")
        return

    # User requested 1920x1080
    width, height = 1920, 1080
    
    # Define the codec and create VideoWriter object
    # On Windows, 'mp4v' is generally reliable
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    print(f"Generating video: {output_file} ({width}x{height} @ {fps}fps)")
    print(f"Found {len(images)} frames. Looping {loops} times.")

    for i in range(loops):
        print(f"Processing loop {i+1}...")
        for image_path in images:
            frame = cv2.imread(image_path)
            if frame is None:
                continue
            # Resize frame to target resolution
            resized_frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_LANCZOS4)
            out.write(resized_frame)

    # Release everything if job is finished
    out.release()
    print("Video generation complete!")

if __name__ == "__main__":
    input_directory = r"c:\Users\itsam\OneDrive\Desktop\HTF-Timer\frames"
    output_filename = r"c:\Users\itsam\OneDrive\Desktop\HTF-Timer\background.mp4"
    generate_video(input_directory, output_filename)
