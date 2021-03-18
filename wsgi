[uwsgi]
http-socket = :80
main = true
die-on-term = true
module = app:app
memory-report = true