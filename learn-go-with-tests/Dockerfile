FROM golang:1.19.0-bullseye
# Visual Studio Code Remote Development 拡張機能がデフォルトで開くディレクトリーであるため
WORKDIR /workspace
# 2021-06-10 時点で Visual Studio Code でコードのフォーマットや Lint などの支援を受けるのに必要なモジュール
# モジュール未インストール時に Visual Studio Code を開き、次のコマンドで一覧表示されたものです:
# Ctrl + Shift + P -> Go: Install/Update Tools
RUN go install github.com/uudashr/gopkgs/v2/cmd/gopkgs@latest
RUN go install github.com/ramya-rao-a/go-outline@latest
RUN go install github.com/cweill/gotests/...
RUN go install github.com/fatih/gomodifytags@latest
RUN go install github.com/josharian/impl@latest
RUN go install github.com/haya14busa/goplay/cmd/goplay@latest
RUN go install github.com/go-delve/delve/cmd/dlv@latest
# div-dap のインストール方法は次のドキュメントを参考にしました:
# https://github.com/golang/vscode-go/blob/v0.26.0/docs/dlv-dap.md#updating-dlv-dap
RUN GOBIN=/tmp/ go install github.com/go-delve/delve/cmd/dlv@master \
 && mv /tmp/dlv $GOPATH/bin/dlv-dap
RUN go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
RUN go install golang.org/x/tools/gopls@latest