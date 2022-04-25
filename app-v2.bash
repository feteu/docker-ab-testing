docker run \
    --detach \
    --name "app-v2" \
    --network "docker-ab-testing" \
    --volume "$(pwd)/app-v2/:/usr/src/:ro" \
    python:latest \
    /bin/bash -c "python -m pip install flask && python /usr/src/app.py"