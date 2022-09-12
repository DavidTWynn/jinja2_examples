import jinja2


def main():
    env = jinja2.Environment(loader=jinja2.PackageLoader("jinja2_basics"))
    env.trim_blocks = True
    template = env.get_template("basic_template.j2")
    oss = ["Linux", "macOS", "OS/2"]
    year = 2022

    print(template.render(oss=oss, year=year), end="")


if __name__ == "__main__":
    main()
