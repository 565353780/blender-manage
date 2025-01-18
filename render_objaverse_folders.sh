GPU_ID=$1

while true; do
  python render_objaverse_folders.py --gpu_id ${GPU_ID}
  sleep 1
done
