FROM debian:11-slim as builder
RUN apt-get update && \
    apt-get install scons \
                    patchelf \
                    upx \
                    python3-minimal \
                    python3-pip \
                    python3-venv \
                    python3-dev \
                    gcc --no-install-recommends -y
ENV VIRTUAL_ENV=/usr/src/.venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /usr/src
COPY requirements.txt .
RUN pip install --no-cache-dir wheel && \
    pip install --no-cache-dir staticx==0.13.9 && \
    pip install --no-cache-dir -r requirements.txt
COPY cli.py .
COPY renderer/ renderer/
RUN pyinstaller -F cli.py
RUN staticx dist/cli dist/cli_static

FROM debian:11-slim
COPY --from=builder /usr/src/dist/cli /usr/local/bin/j2render
COPY --from=builder /usr/src/dist/cli_static /usr/local/bin/j2render_static
