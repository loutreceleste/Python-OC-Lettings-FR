function deploy_docker {

  cd $(git rev-parse --show-toplevel) && COMMIT_HASH=$(git rev-parse --short HEAD)
  docker build -t python-oc-lettings-fr:$COMMIT_HASH -f Dockerfile .

  echo "$DOCKERHUB_PASSWORD" | docker login -u loutreceleste --password-stdin
  docker tag python-oc-lettings-fr:$COMMIT_HASH loutreceleste/python-oc-lettings-fr:$COMMIT_HASH
  docker push loutreceleste/python-oc-lettings-fr:$COMMIT_HASH
  docker pull loutreceleste/python-oc-lettings-fr:$COMMIT_HASH
}
