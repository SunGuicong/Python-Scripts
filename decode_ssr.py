#! /bin/env python
import base64
ssr = 'ssr://MTA0LjIzNi4yMzEuNjQ6NTI1MjphdXRoX3NoYTFfdjQ6cmM0LW1kNTpodHRwX3NpbXBsZTpOVEp6YzNJdVpuVnUvPw'
split_ssr = ssr.split("/",2)[-1]
missing_padding = 4 - len(split_ssr) % 4
if missing_padding:
    split_ssr = bytes(split_ssr,encoding = "utf-8")
    split_ssr += b'='* missing_padding
    print (base64.b64decode(split_ssr))
    print(type(split_ssr))
