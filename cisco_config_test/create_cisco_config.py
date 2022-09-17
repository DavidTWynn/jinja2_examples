import jinja2


def main():

    env = jinja2.Environment(
        loader=jinja2.PackageLoader("create_cisco_config")
    )
    # env.trim_blocks = True
    template = env.get_template("cisco/cisco_standard_config.j2")

    template_input = {
        "hostname": "r1_homelab",
        "domain_name": "wynn.local",
        "local_username": "cisco",
        "local_secret": "cisco",
    }

    print(template.render(template_input))


if __name__ == "__main__":
    main()
