#!/usr/bin/env python3
"""Testa as vias por API do kit contra um servidor FALSO local (nenhuma API real é chamada)."""
import importlib.util, json, os, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

RESP = {
    '/v1/messages': {'content': [{'type': 'text', 'text': 'oi anthropic'}], 'usage': {'input_tokens': 11, 'output_tokens': 3}},
    '/v1/chat/completions': {'choices': [{'message': {'content': 'oi chat'}}], 'usage': {'prompt_tokens': 12, 'completion_tokens': 4}},
    '/v1beta/models/m:generateContent': {'candidates': [{'content': {'parts': [{'text': 'oi google'}]}}],
                                         'usageMetadata': {'promptTokenCount': 13, 'candidatesTokenCount': 5, 'thoughtsTokenCount': 2}},
}
VISTO = []


class H(BaseHTTPRequestHandler):
    def do_POST(self):
        corpo = json.loads(self.rfile.read(int(self.headers['content-length'])))
        VISTO.append((self.path, {k.lower(): v for k, v in self.headers.items()}, corpo))
        b = json.dumps(RESP[self.path]).encode()
        self.send_response(200); self.send_header('content-type', 'application/json'); self.end_headers(); self.wfile.write(b)

    def log_message(self, *a):
        pass


srv = HTTPServer(('127.0.0.1', 0), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{srv.server_port}'
for k in ('ANTHROPIC', 'OPENAI', 'GEMINI', 'OPENROUTER'):
    os.environ[f'{k}_BASE_URL'] = base
    os.environ[f'{k}_API_KEY'] = 'chave-falsa'
spec = importlib.util.spec_from_file_location('t', Path(__file__).with_name('testar.py'))
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)

casos = [('api-anthropic', ('oi anthropic', 11, 3)), ('api-openai', ('oi chat', 12, 4)),
         ('openrouter', ('oi chat', 12, 4)), ('api-google', ('oi google', 13, 7))]
for via, esperado in casos:
    txt, e, s, _ = t.VIAS[via]('m', 'pedido', '.')
    assert (txt, e, s) == esperado, (via, txt, e, s)
    print(f'ok {via}')
assert VISTO[0][1].get('x-api-key') == 'chave-falsa' and VISTO[0][2]['model'] == 'm'
assert VISTO[1][1].get('authorization') == 'Bearer chave-falsa'
assert VISTO[3][1].get('x-goog-api-key') == 'chave-falsa'
print('todas as vias por API ok (servidor falso)')
