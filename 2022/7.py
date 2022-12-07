import pathlib
import tempfile

import util


def build_tree(root: pathlib.Path):
    # "sometimes my genius is.. it's almost frightening" - jeremy clarkson.
    # why know important data structures when you can also just ✨pretend✨
    ptr = root
    for line in util.load_input(7):
        if line == "$ cd /":
            ptr = root
            continue
        if line == "$ cd ..":
            # this technically isn't even necessary since pathlib is smart enough to process ".." into "one up".
            # it'd feel wrong to leave it out though
            ptr = ptr.parent
            continue
        if line.startswith("$ cd "):
            ptr = (ptr / line[5:])
            ptr.mkdir(exist_ok=True)
            continue
        if line == "$ ls":
            continue
        if line.startswith("dir "):
            (ptr / line[4:]).mkdir(exist_ok=True)
            continue
        size, name = line.split(maxsplit=1)
        with open(ptr / name, "w", encoding="utf-8") as f:
            f.write(size)


def dir_size(path: pathlib.Path):
    size = 0
    for file in path.glob("**/*"):
        if file.is_file():
            with open(file, encoding="utf-8") as f:
                size += int(f.read().strip())
    return size


def all_dir_sizes(root: pathlib.Path):
    return {
        dir_.relative_to(root): dir_size(dir_)
        for dir_ in root.glob("**/*")
        if dir_.is_dir()
    } | {"/": dir_size(root)}


def main():
    with tempfile.TemporaryDirectory() as _tmp_dir:
        root = pathlib.Path(_tmp_dir)
        build_tree(root)
        all_sizes = all_dir_sizes(root)
        print("\n".join(f"{key}: {value}" for key, value in sorted(all_sizes.items(), key=lambda x: x[1])))
        # first attempt: 1163150 is too low
        print("p1:", sum(size for size in all_sizes.values() if size <= 100_000))
        min_freeup_size = all_sizes["/"] - 40_000_000
        print(min_freeup_size)
        print("p2:", [size for size in sorted(all_sizes.values()) if size >= min_freeup_size][0])


if __name__ == '__main__':
    main()
