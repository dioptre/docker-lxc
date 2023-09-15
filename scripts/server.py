#docker privileged
# docker run --privileged -it debian bash
# apt update && apt install -y systemd libpam-cgfs wget xz-utils lxc iproute2 screen bash-completion curl wget apt-transport-https lxcfs vim overlayroot libkmod2 libkmod-dev cgroup-tools cgroupfs-mount
# echo "$(id -un) veth lxcbr0 10" | sudo tee -a /etc/lxc/lxc-usernet
# mkdir -p ~/.config/lxc
# cp /etc/lxc/default.conf ~/.config/lxc/default.conf
# MS_UID="$(grep "$(id -un)" /etc/subuid  | cut -d : -f 2)"
# ME_UID="$(grep "$(id -un)" /etc/subuid  | cut -d : -f 3)"
# MS_GID="$(grep "$(id -un)" /etc/subgid  | cut -d : -f 2)"
# ME_GID="$(grep "$(id -un)" /etc/subgid  | cut -d : -f 3)"
# echo "lxc.idmap = u 0 $MS_UID $ME_UID" >> ~/.config/lxc/default.conf
# echo "lxc.idmap = g 0 $MS_GID $ME_GID" >> ~/.config/lxc/default.conf
# echo "lxc.aa_allow_incomplete = 1" >> ~/.config/lxc/default.conf
# lxc-create -t download -n n1 -- --dist debian --release buster --arch arm64
# amd64 for x86
# lxc-ls --fancy
# lxc-start --name ubuntu-test --daemon
# lxc-attach --name ubuntu-test -- echo "hi world"
# https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#container_definition_security
# https://infoheap.com/lxc-linux-containers-quick-start-tutorial-ubuntu/
# lxc config set machine boot.autostart true
# https://stgraber.org/2014/01/17/lxc-1-0-unprivileged-containers/
# cp test_runner /var/lib/lxc/<container_name>/rootfs/tmp/
# Rootfs is the raw filesystem for the container. You would then execute your script by doing something like:
# lxc-attach -n container -- /tmp/testprogram


# import lxc
# from bottle import run, request, get, post
# @post('/build')
# def build():
#      name = request.headers.get('X-LXC-Name')
#      memory = request.headers.get('X-LXC-Memory')
#      template = str(request.headers.get('X-LXC-Template'))

#      container = lxc.Container(name)
#      container.create(template)

#      return "Building container {0} using the {1} template\n".format(
#     name, template)

# @post('/container/<name>/start')
# def container_start(name):
#      container = lxc.Container(name)
#      container.start(useinit=False, daemonize=True)

#      return "Starting container {0}\n".format(name)

# @post('/container/<name>/stop')
# def container_start(name):
#      container = lxc.Container(name)
#      container.stop()

#      return "Stopping container {0}\n".format(name)

# @post('/container/<name>/destroy')
# def container_start(name):
#      container = lxc.Container(name)
#      container.destroy()

#      return "Destroying container {0}\n".format(name)

# @post('/container/<name>/freeze')
# def container_start(name):
#      container = lxc.Container(name)
#      container.freeze()

#      return "Freezing container {0}\n".format(name)

# @post('/container/<name>/unfreeze')
# def container_start(name):
#      container = lxc.Container(name)
#      container.unfreeze()

#      return "Unfreezing container {0}\n".format(name)

# @get('/container/<name>/state')
# def container_status(name):
#      container = lxc.Container(name)
#      state = container.state

# return "The state of container {0} is {1}\n".format(name, state)

# @get('/container/<name>/ips')
# def container_status(name):
#      container = lxc.Container(name)
#      ip_list = container.get_ips()

# return "Container {0} has the following IP's {1}\n".format(
#     name, ip_list)

#  @get('/list')
# def list():
#      container_list = lxc.list_containers()

#      return "List of containers: {0}\n".format(container_list)

# run(host='localhost', port=8080, debug=True)