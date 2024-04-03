#!/bin/bash

# AtCoder Problems APIから問題データを取得
problems_json=$(curl -s "https://kenkoooo.com/atcoder/resources/problems.json")

# Difficulty Aの問題を抽出し、ランダムに1つ選択
selected_problem=$(echo $problems_json | jq '[.[] | select(.id | startswith("abc_a"))] | .[random(length)]')

# 選択された問題のタイトルとURLを整形して出力
title=$(echo $selected_problem | jq -r '.title')
id=$(echo $selected_problem | jq -r '.id')
contest_id=$(echo $selected_problem | jq -r '.contest_id')
url="https://atcoder.jp/contests/$contest_id/tasks/$id"

# Issue Body用にフォーマット
echo "## Daily AtCoder Challenge\n\n**Title:** $title\n\n**URL:** $url"
