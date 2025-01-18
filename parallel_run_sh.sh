SCRIPT_PATH=$1
PROCESSOR_NUM=$2
GPU_ID=$3

for i in $(seq 1 ${PROCESSOR_NUM}); do
  ${SCRIPT_PATH} ${GPU_ID} &
  sleep 1
  echo "started Process No."$i
done

wait

echo "all Process finished!"
