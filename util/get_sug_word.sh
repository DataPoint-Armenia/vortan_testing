curl -X POST -H "Content-Type: application/json;" -s http://127.0.0.1:5000/suggest -d '{"word": "'$1'"}' | \
    python3 -c "import sys, json; print(json.load(sys.stdin)['suggestions'][0])"
