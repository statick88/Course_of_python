# Independent ABP practices for M0–M10
Objective: extend the existing guided-practice dynamic across both course repositories. Branch: `feat/abp-modulos-00-10` in each isolated worktree.
Delivery: `auto-chain`, `chain_strategy=feature-branch-chain` (user selected). Forecast 1,350–2,200 authored lines; review/commit slices by module on feature branches, no publication yet. Runners: stdlib `unittest`, private isolated reference/mutant checks, existing ebook pytest and Quarto HTML checks.

## Specs

- S1. User: «pensando en esta misma dinamica vamos a realizar practica para todos los modulos».
- S2. User selection: «Independientes por módulo — recomendado».
- S3. Established dynamic, user: «verifica que tanto el ebook como el repositorio de ejemplo estan listos, agregar un directorio de practicas con comentarios para poder realizar practicas y aplica uinitest en esas practicas, de esa forma fomentamos el abp y el estudiante debe seguir las instrucciones de los comentarios para dicho avance».
- S4. File organization, user: «separa cada practica en archivo diferente».
- S5. Curriculum coherence, user: «documenta estas practicas en el ebook para tener coherencia de lo que se explica, lo que se revisa y lo que se practica».

### Operational decisions derived from the selected dynamic

These are implementation contracts, not additional user requests. Course-facing artifacts remain Spanish. Each module has its own editable artifact, teacher-owned flat `test_mNN_*.py`, and short guide under `practicas/guias/`. Existing snacks scaffolds, tests, examples, and learning-history checkboxes remain intact. A newly available exercise does not prove it was taught or mastered. No student solution is delivered. M0 is a planning artifact with limited structural checks and required human assessment. M9's student deliverable is a test suite; supplied teacher functions are its subject, not a solved student exercise. Other student Python bodies remain incomplete with numbered comments and bare `return` placeholders. M10 imports none of the earlier unfinished practices.

Locations:
- Ebook worktree: `.deployment-verification/practicas-todos-modulos/ebook`, base `0a1b182b353aa283de19144b6fed34ec26d2416e`.
- Examples worktree: `.deployment-verification/practicas-todos-modulos/ejemplos`, base `c3326395f0487763adc5f070bfb9425655cfbc5f`.
- Authoritative curriculum reference: `.deployment-verification/ebook-abp-publication/content/modulo-00` through `modulo-10`.
- Feature locator: `odd/tasks/practicas-abp-modulos-00-10.md` in the ebook worktree. Workers read through this document until `## Log` and report covered S#/T#.

### Module contracts

| ID | Student artifact and independent mini-project | Public behavior and assessment boundary |
|---|---|---|
| C0 | `practicas/m00_planificador.md`: plan a school outing | Sections `Problema`, `Entradas`, `Salidas`, `Subproblemas`, `Pseudocódigo`, `Alternativas`, `Justificación`; at least four meaningful listed subproblems and two approaches. Editable placeholders must be filled. Structural tests must not enforce one exact algorithm or pretend to assess reasoning. Instructor reviews feasibility, decomposition, and justification. No Python prerequisite. |
| C1 | `practicas/m01_tarjeta_presentacion.py` | Supplied `presentarse()` shell requests exactly `Nombre: ` and `Ciudad: ` and prints `Hola, soy Ana y vivo en Quito.\n` for Ana/Quito. Valid nonempty text is preserved. Test prompts, input order, exact stdout, empty stderr and return value `None`. No retries/while, validation or invented function-design prerequisite. |
| C2 | `practicas/m02_presupuesto_viaje.py` | `calcular_costo(distancia_texto, tarifa_texto)` converts valid finite nonnegative numeric strings and returns a two-decimal numeric total: `('12','0.35') -> 4.2`. `normalizar_destino(' loja ') -> 'Loja'`. `formatear_presupuesto(' loja ',4.2) -> 'Viaje a Loja: $4.20'`. Zero is valid; preserve arguments. No printing, input or invalid-input handling yet. |
| C3 | `practicas/m03_reporte_paridad.py` | `reporte_paridad(inicio, fin)` returns inclusive lines, e.g. `(2,3) -> '2: par\n3: impar\n'`. `contar_pares(inicio, fin)` counts even integers in the same inclusive interval, guided with `while`. Integers may be negative or zero, `inicio <= fin`; include singleton and both boundary cases. No output side effects. This is focused practice, not coverage of every control-flow feature. |
| C4 | `practicas/m04_recibo_envio.py` | `calcular_envio(peso, tarifa=3)` returns a two-decimal numeric fee; `(2.5) -> 7.5`. `crear_recibo(destino,peso,tarifa=3)` returns `Envío a Loja: $7.50` for Loja/2.5/default. Valid finite nonnegative numbers and nonempty destination; test default, positional and keyword arguments, zero and composition. No printing or mutation. |
| C5 | `practicas/m05_maleta.py` | `peso_total(pesos)` returns numeric sum; `seleccionar_livianos(pesos,limite)` returns a NEW list of weights `<= limite`, in original order; `invertir_itinerario(paradas)` accepts a tuple of names and returns reversed list. Empty collections are valid. Inputs stay unchanged and results must not alias input lists. |
| C6 | `practicas/m06_votacion_club.py` | `contar_votos(votos)` returns counts; `candidatos_unicos(votos)` returns a set; `ganador(conteo)` returns the unique highest candidate or `None` for an empty mapping/tie. Valid names are nonempty strings and supplied counts positive integers. Test duplicates, order-independent dict/set equality, empties, ties and no input mutation. |
| C7 | `practicas/m07_exportar_inventario.py` | `exportar_inventario(origen_csv,destino_json)` reads UTF-8 CSV `nombre,cantidad` (nonempty name, integer quantity >=0), writes a NEW JSON list of dictionaries preserving order, returns row count. Header-only input writes `[]`. Missing input raises `FileNotFoundError`, malformed CSV raises `ValueError`, existing destination raises `FileExistsError` and remains byte-identical. Rejected input creates no output; input CSV remains unchanged. Every test/reference uses `TemporaryDirectory`; no real data paths. Explain these file-error contracts as a focused reading prerequisite, not proof M9 was taught. |
| C8 | Teacher package `practicas/m08_saludos/`; only student file `formato.py` | Teacher `__init__.py` exports `construir_saludo`, and `catalogo.py` supplies greetings. Public API: `construir_saludo('Ana','manana') -> 'Buenos días, Ana.'`; `tarde -> 'Buenas tardes, Ana.'`, `noche -> 'Buenas noches, Ana.'`. Valid nonempty name and one of those keys. Tests import package PUBLIC export; no pip/network or unfinished earlier modules. |
| C9 | `practicas/m09_pruebas_impuesto.py`: student-written unittest assertions | Teacher `soporte_m09_impuestos.py` supplies `calcular_subtotal(precio,cantidad)` and `aplicar_iva(monto,tasa=0.15)` with rounded numeric returns and `ValueError` on negative numeric arguments; otherwise valid finite numbers and integer quantities. Student supplies at least four meaningful tests for normal, zero, rounding and exception cases. Teacher grader proves that student tests pass correct APIs, contain no skips/expected failures, and reject quantity/tax/rounding/error mutants. No solved student assertions shipped. Ebook explicitly introduces stdlib `unittest` alongside, not replacing, its existing pytest lesson. |
| C10 | `practicas/m10_biblioteca.py`: independent reading-log project | `cargar_lecturas(path)` reads valid JSON list of `{titulo,estado}` records (`pendiente`/`leido`), preserves order and rejects malformed input. `resumir_por_estado(items)` returns both count keys, initialized to zero. `guardar_reporte(path,resumen)` creates a NEW JSON report, returns `None`, refuses existing output with `FileExistsError`. No mutation or overwrite on rejection; all file examples/tests use temporary fixtures and synthetic data. Integrate read/summarize/save within M10 only; no imports of other student TODOs. |

### Verification and delivery invariants

- Teacher tests cover each documented example/boundary, actual public results, stdout/stderr, exit status, and nonmutation/preservation when named. No committed test reads git history or a fixed commit.
- Starter `unittest` runs intentionally fail assertions, without syntax/import errors or skips. Teacher quality verification must turn GREEN with private reference implementations only in isolated memory/temp state, and reject meaningful mutants. References and solved student tests are NOT delivered.
- Naming: new test classes use `TestMNN...`, never `TestEtapa...`. Preserve the legacy three-practice suite as 12 tests via `-k TestEtapa` and its three original per-file commands; update legacy guide/global index so a global `test_*.py` run is not falsely described as only 12 tests after expansion.
- Global discovery remains `python3 -m unittest discover -s practicas -p 'test_*.py' -v`. Per-module commands select their own `test_mNN_*.py`; no module imports another unfinished module.
- Preserve all 14 original example scripts byte-for-byte. Run exact baseline/candidate public checks under the same Python interpreter; distinguish its volatile timing/environment details from behavioral differences. Do not suppress lint rules or skip failing material checks.
- Publishing, PR creation, merge and dependency installation are NOT authorized by the new request alone. Large-ODD work-unit commits on feature branches are authorized; keep code/tests/module guide together. Forecast exceeds ~400 lines, so resolve delivery shape once before commits; this is not publication consent.
- Risk assessment before writes: student scaffolds have no real filesystem effects; teacher file fixtures are temporary and protected; packages require no dependency changes. Any newly discovered high-risk item must be named and handled by the parent, not silently widened.

## Tasks

- T0 | S1–S5 | Freeze module contracts and delivery slices | route: parent + read-only explorer | done: user chose feature-branch-chain | commit: tracking only
- T1 | S1–S4, C0–C10 | Build and verify all independent module units | route: three disjoint writers; parent readback, references and mutants | done: 46 teacher methods GREEN with private references; starters intentionally RED without errors/skips | commit: recorded by T14
- T2 | S1–S4, C1 | Accept/check and commit M1 interactive card unit | route: parent using writer A evidence | dropped: acceptance bookkeeping consolidated into T14; module unit retained | commit: T14
- T3 | S1–S4, C2 | Accept/check and commit M2 travel-budget unit | route: parent using writer A evidence | dropped: acceptance bookkeeping consolidated into T14; module unit retained | commit: T14
- T4 | S1–S4, C3 | Accept/check and commit M3 parity/iteration unit | route: parent using writer A evidence | dropped: acceptance bookkeeping consolidated into T14; module unit retained | commit: T14
- T5 | S1–S4, C4 | Accept/check and commit M4 shipping-functions unit | route: parent using writer B evidence | dropped: acceptance bookkeeping consolidated into T14; module unit retained | commit: T14
- T6 | S1–S4, C5 | Accept/check and commit M5 collections unit | route: parent using writer B evidence | dropped: acceptance bookkeeping consolidated into T14; module unit retained | commit: T14
- T7 | S1–S4, C6 | Accept/check and commit M6 voting unit | route: parent using writer B evidence | dropped: acceptance bookkeeping consolidated into T14; module unit retained | commit: T14
- T8 | S1–S4, C7 | Accept/check and commit M7 CSV/JSON unit | route: parent using writer C evidence | dropped: acceptance bookkeeping consolidated into T14; module unit retained | commit: T14
- T9 | S1–S4, C8 | Accept/check and commit M8 package unit | route: parent using writer C evidence | dropped: acceptance bookkeeping consolidated into T14; module unit retained | commit: T14
- T10 | S1–S4, C9 | Accept/check and commit M9 student-testing unit | route: parent using writer C evidence | dropped: acceptance bookkeeping consolidated into T14; module unit retained | commit: T14
- T11 | S1–S4, C10 | Accept/check and commit M10 independent project unit | route: parent using writer C evidence | dropped: acceptance bookkeeping consolidated into T14; module unit retained | commit: T14
- T14 | S1–S4, C0–C10 | Record verified units as eleven separate module commits | route: parent, explicit path staging and module commit ledger | done: eleven isolated module commits, ledger L13.M00–L13.M10 | commit: 4714ea4 through a6daf4d
- T12 | S1–S5 | Link global practice catalog, module indexes and unittest explanation in ebook | route: bounded ebook writer; parent examples-catalog integration | in_progress | commit: —
- T13 | S1–S5 | Verify every module, legacy behavior, instructions and ebook navigation | route: parent functional checks; independent verifier only on named high risk | pending | commit: —

## Log

- L1. Original request: «pensando en esta misma dinamica vamos a realizar practica para todos los modulos».
- L2. User selection: «Independientes por módulo — recomendado».
- L3. Prior accepted dynamics are quoted in S3–S5. Source examples main is c332639; ebook main is 0a1b182. Both new worktrees are clean isolated branches; dirty original ebook tree remains untouched.
- L4. Exploration returned a module-by-module map with actual curriculum paths. M0 needs human reasoning assessment; M9's current lesson teaches pytest, requiring a bounded unittest-alternative explanation for coherence.
- L5. The expanded route is large because eleven distinct learner contracts, two repositories, private verification evidence, curriculum links and per-module commit boundaries cannot be safely resumed from the user request and one diff alone. Forecast 1,350–2,200 authored lines; no artificial compression to fit a single slice.
- L6. Before the delivery decision, no writer had been launched and no student/teacher source file had been changed. Earlier M2 public-page TLS check remains a separately reported exhausted-proof follow-up, not a prerequisite for authoring these new practices.
- L7. User selected: «Cadena sobre una rama de trabajo — recomendado» (`feature-branch-chain`). This sets review shape only; no push, merge or PR creation is authorized.
- L8. T1 is the active parent coordination/build task for three parallel writers on disjoint module files. T2–T11 are subsequent parent acceptance/commit gates, not source-writing tasks left falsely pending while children build. This preserves one active visible task while each independent unit retains its own evidence and commit boundary. About 400 lines is a review heuristic, not a reason to compress comments, tests or contracts.
- L9. All three initial writers completed. Parent reproduced and closed nine readiness/input/boundary/alias/type gaps in M0–M6; 32 teacher methods now pass private references and reject those nine incorrect plans/implementations.
- L10. Parent verified 14 teacher methods in M7–M10, including file byte preservation, silent APIs and M9 grading. A further M9 false GREEN was reproduced: arithmetic mutants omitted unrelated validation, so negative tests could mask missing rounding assertions. Mutants now preserve every unrelated contract through captured correct public functions; the missing-rounding suite is rejected and a complete private suite is accepted. References/solved student suites remain outside delivered repositories.
- L11. Structural checks, isolated Ruff check/format for all 24 new Python files, lesson-source links in all eleven guides and starter discovery passed their intended checks. Starter discovery runs 46 methods and intentionally exits 1 with assertions only, empty stdout and no errors/skips. All 20 preserved Python files are byte-identical; 14 original scripts have identical stdout/stderr/exit. Legacy 12-test differential matches after worktree-path/timing normalization.
- L12. Plan reconciliation after authoring: T1 now records verified construction of all modules. Redundant subsequent acceptance bookkeeping T2–T11 is consolidated into T14, not marked done; every module still requires its own explicit-path commit and ledger entry. No learner deliverable is dropped. T12/T13 remain open. No push, merge, PR or dependency installation is authorized. Native assessment was previously unavailable (`package-local-binary-missing`); no native approval is claimed.

- L13.M00. Verified module unit committed as `4714ea482b9e07d9308d270227bcd68de74b76ae` (165 authored lines; code/tests/guide together).
- L13.M01. Verified module unit committed as `2d66fbadec16d3ccb777bccc15342de48444941d` (103 authored lines; code/tests/guide together).
- L13.M02. Verified module unit committed as `735b2f8b3de82266a642c455183075875a78d173` (145 authored lines; code/tests/guide together).
- L13.M03. Verified module unit committed as `6f795ae40dc3aba385f22adccb75203e6e1ae3e4` (122 authored lines; code/tests/guide together).
- L13.M04. Verified module unit committed as `479f7851dd9e1209146cd9fed9bfd4975ffb4c5a` (161 authored lines; code/tests/guide together).
- L13.M05. Verified module unit committed as `4c588de08d0d1e99c42a4382fdf9bd9a3722922c` (196 authored lines; code/tests/guide together).
- L13.M06. Verified module unit committed as `e1d650e63bc889fb0920d4379f65a9a8c05d23b9` (180 authored lines; code/tests/guide together).
- L13.M07. Verified module unit committed as `9720fdf2adaf51507953ab20d3d9c947367bfcd3` (175 authored lines; code/tests/guide together).
- L13.M08. Verified module unit committed as `64381dd2a2c57915c0ecd5bcb198686eae35e624` (83 authored lines; code/tests/guide together).
- L13.M09. Verified module unit committed as `638d3d6e9ce76a2faee21c509f40a9e244ed332c` (192 authored lines; code/tests/guide together).
- L13.M10. Verified module unit committed as `a6daf4d588cd367ce50cc9b7da7ee6b3369b1c5f` (200 authored lines; code/tests/guide together).
- L14. Examples catalog/README compatibility committed as `d4e9db05f5f4ddca145359c234e8d6e9c9cf1efd`. Global command verified: 58 teacher methods, starter assertion RED; same public command with isolated private references GREEN (58/58, no errors/skips). All original curriculum checkbox lines preserved. T12 ebook integration still running.
