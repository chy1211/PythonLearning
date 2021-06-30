#!/usr/bin/env python3
import subprocess

stid = ["iC1101563{:02d}".format(i) for i in range(1, 56)]


for i in stid:
    proc = subprocess.Popen(
        ["adduser", "--gid", "1001", "{}".format(i)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate(b"ic109193244\nic109193244\n\n\n\n\n\nY\n")
    proc.wait()
    print(out)
