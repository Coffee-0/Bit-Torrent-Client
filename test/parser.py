from bencode import decode


with open("test/data/ubuntu-16.04-desktop-amd64.iso.torrent", "rb") as f:
    meta_info = f.read()
    torrent = decode(meta_info)

print(torrent)
