↖️ Table of Contents

<h1 align="center"><code>j2render</code></h1>

<div align="center">
  <a href="https://github.com/gcavalcante8808/j2render/actions/workflows/ci.yaml">
    <img src="https://github.com/gcavalcante8808/j2render/actions/workflows/ci.yaml/badge.svg">
  </a>
  <a href="https://github.com/gcavalcante8808/j2render/actions">
    <img src="https://raw.githubusercontent.com/gcavalcante8808/j2render/main/badges/coverage.svg?token=GHSAT0AAAAAACCF2E37QVT26VHYFWALDLVAZGI4TOQ" alt="coverage">
  </a>
  <a href="https://www.buymeacoffee.com/gcavalcante8808">
    <img src="https://img.shields.io/badge/-buy_me_a%C2%A0coffee-gray?logo=buy-me-a-coffee" alt="buy me a coffee">
  </a>
</div>
<br>

`j2render` is a linux cli tool that interpolates jinja2 templates and variables in a declarative way.

For each file/template that you want to render, you need to define a `config.yaml` file with the following syntax:

```yaml
resources:
  - name: yamlResource1
    template: some.template
    output_file: /tmp/rendered1.config
    variables:
      key1: value1
      key2: value2
      key3: value3
```

In the example above, j2render will read a template file called `some.template` and will try to interpolate the `key1`, `key2`, `key3` variables, creating an output file on `/tmp/rendered1.config`.

The template should use two curly braces to be able to receive the value as it will be rendered using jinja2.render:

```
items:
  - key1: "{{ key1 }}"
  - key2: "{{ key2 }}"
  - key3: "{{ key3 }}"
```

If you need help with j2render please feel free to open an issue. Feature requests and bug reports are always welcome!

## Installation

### Prerequisites

`j2render` should run on any *Linux* amd64 or arm64 system.

### Prebuilt Binaries

Pre-built binaries for Linux can be found on [the releases page](https://github.com/gcavalcante8808/j2render/releases).

### Download from a docker image

You can also copy the binary in your docker image by using the following statement in your Dockerfile:

```dockerfile
COPY --from=gcavalcante8808/j2render:latest /usr/local/bin/j2render_static /usr/local/bin/j2render
```

### Author

Author: Gabriel Cavalcante (gabriel.cavalcante88 at gmail.com)
