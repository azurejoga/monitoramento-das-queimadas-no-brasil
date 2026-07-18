# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 162cc16d-6d46-3db3-a7c9-349e13cf6f5b | -4.10006 | -49.35725 | 2026-07-18 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 171e8111-df85-3a2b-8702-95a5ad489d6e | -2.76808 | -49.46601 | 2026-07-18 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a9034af3-d065-3802-be39-fb323fe2b507 | -2.77095 | -49.47038 | 2026-07-18 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 10ba982c-1286-31ff-844b-59d06dd61e22 | -2.77155 | -49.46656 | 2026-07-18 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 765c7d04-da14-3747-b0f9-23ba86e9f3f2 | -2.78927 | -49.5234 | 2026-07-18 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4d0ae9f-bea8-32dc-8e70-22ee2968b381 | -5.12079 | -43.23392 | 2026-07-18 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3c3fcb7a-5771-33fd-8a8c-094d80da0662 | -2.32732 | -49.08202 | 2026-07-18 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0980bb7b-620c-3795-a46c-bb7a2dcb56d6 | -4.15851 | -48.94505 | 2026-07-18 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 231a4a46-77bc-3acf-8bb4-933b3b477f80 | -4.83289 | -44.0653 | 2026-07-18 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9e58549-29ba-3f6b-8a6f-1610e45d4735 | -2.47909 | -47.08343 | 2026-07-18 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afb24e32-ed6f-3981-8896-00149d3b1d30 | -3.14589 | -48.15104 | 2026-07-18 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4cd5381-7c4e-3246-b7a3-89b7d3bc87c3 | -2.79621 | -49.52451 | 2026-07-18 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 839b071b-e145-3020-9882-23f09a6f6af1 | -2.046 | -48.0352 | 2026-07-18 04:36:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0fc46725-8010-3c73-8565-38104863c759 | -1.58853 | -50.43658 | 2026-07-18 04:36:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bd739038-0d2b-3bb1-835e-3304f9dd9dff | -2.47854 | -47.08686 | 2026-07-18 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a52ab3b-bea0-3fc0-a1cd-79c39115eb9f | -5.12005 | -43.23878 | 2026-07-18 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b6f9a54-e7f9-3522-913a-dd01aa8460f6 | -2.7932 | -48.57599 | 2026-07-18 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 211761a7-0fd9-3920-9f6f-5311dfd8384c | -3.42616 | -49.22931 | 2026-07-18 04:36:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8609704f-f9aa-3c22-a88b-b25e6e7a15c4 | -3.98615 | -47.93134 | 2026-07-18 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85455318-eefa-3d78-b826-7898c403c24c | -4.86453 | -47.40754 | 2026-07-18 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bac5e61a-fd86-332b-9857-f8a0d4ef7cf1 | -3.71465 | -48.82755 | 2026-07-18 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5907108-5b58-38b4-8fab-aebed8599be8 | -4.82985 | -44.06038 | 2026-07-18 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 62fb3fba-e733-3778-8f0d-574aa045c83d | -4.09723 | -49.35302 | 2026-07-18 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a51fc81-b7b7-389e-8cdb-69a498fd971f | -4.10028 | -49.35683 | 2026-07-18 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aed62bdd-a3c7-3c7c-87d3-c41845d0941c | -4.10064 | -49.35356 | 2026-07-18 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ede8f511-aa72-30dc-ae3c-972dfa50d5b4 | -9.82937 | -57.85172 | 2026-07-18 04:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80360974-3649-3ea3-b3cd-31284bf9b67c | -9.16015 | -50.88948 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d31fe57f-119e-39d8-9dd3-c35220bbdadd | -9.07129 | -50.59491 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3d17643-186d-3edf-88a2-5d6ec0e3ec16 | -9.07936 | -50.58856 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7fed0b9-2a5c-38c9-a9b8-482d5a6ad29a | -9.70245 | -47.70006 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 68e4c4d3-5ff4-3951-abae-b38b08d0e821 | -9.08536 | -50.61651 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52ba0242-12cd-3f4d-b4d4-28a17eb74c87 | -9.6105 | -48.31328 | 2026-07-18 04:38:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2518ff5-a994-3892-abeb-e24fd397e6dd | -11.4058 | -47.52702 | 2026-07-18 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a3d30b4-4ba0-393e-ac1f-e7aba0ee7f69 | -7.2903 | -46.25322 | 2026-07-18 04:38:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fa873f1-2db5-3053-919f-eae55fdff3af | -5.71106 | -45.66076 | 2026-07-18 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8f8ab50-f7a8-3153-9804-d5a361e91689 | -10.95314 | -49.80799 | 2026-07-18 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c02e884c-d931-3641-8022-d200abba92c8 | -9.0894 | -50.61333 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d43b6df7-37cd-3873-9508-4ad48dd743f4 | -11.47498 | -47.34773 | 2026-07-18 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3f80295-4d3b-35eb-91c2-68c96276f3ed | -6.10967 | -46.18515 | 2026-07-18 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7981c64-821f-3376-838b-7ceab3ab39ef | -9.8896 | -53.38538 | 2026-07-18 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1621d60c-44f1-36a4-b22d-013474a034fc | -9.30278 | -51.91779 | 2026-07-18 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44e821f6-5de5-3c75-b30e-2854ae95e4ef | -10.64973 | -47.22979 | 2026-07-18 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f43ac93-079e-3490-847e-cfd9e48c7dee | -10.95371 | -49.80445 | 2026-07-18 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18b951e3-061b-3bfe-97ee-54fa56e64aed | -11.9378 | -49.30147 | 2026-07-18 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3faa0d86-d232-3812-a791-080c50f0c49c | -8.47553 | -50.22405 | 2026-07-18 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 976278e3-5641-3ea2-b460-daeae27ae573 | -5.67229 | -43.57121 | 2026-07-18 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6607502-382b-39f2-9403-f0ac38f5ce63 | -9.52748 | -47.12292 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a3654ed-7c9b-3631-971f-2a2e3c87db6e | -12.94675 | -44.7318 | 2026-07-18 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fab28526-10f2-380b-9af6-4d9305700e76 | -5.92891 | -43.64391 | 2026-07-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 48e1e462-a3a3-3a4a-87fa-383eaa9ea278 | -7.72921 | -47.24642 | 2026-07-18 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa0f2198-861c-3c0a-b69d-c29481e85667 | -12.00427 | -50.58025 | 2026-07-18 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a56dafbb-fee6-385d-b772-ed9f9c643061 | -5.43826 | -46.28725 | 2026-07-18 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00369a04-3ff8-31a0-860e-873b482a7f16 | -9.28224 | -49.07796 | 2026-07-18 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6dbcbe94-be5b-3f90-80a2-e61b906dd2a3 | -10.90889 | -56.36734 | 2026-07-18 04:38:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47c24d91-4be0-3098-82ff-e69280cc52bc | -5.93441 | -43.65931 | 2026-07-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ad5cb2b-c790-3406-a870-8f015b1587c1 | -11.16411 | -54.11414 | 2026-07-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feb28dcc-4950-3a96-ab9d-ac33ef4c3f77 | -8.94025 | -47.60604 | 2026-07-18 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e360f69b-8f74-309c-bc6d-44327500f93d | -5.60071 | -45.33894 | 2026-07-18 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43331709-a214-34db-a516-03beee3aec3e | -8.47213 | -50.2235 | 2026-07-18 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ce36248-2789-3e93-85fe-1deba78962fa | -5.92819 | -43.64866 | 2026-07-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 38197d2d-cf9a-3877-bd93-63afbcbe7a52 | -13.29379 | -42.11718 | 2026-07-18 04:38:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.1 |
| 3d6cd7ef-bdd5-3a06-91d4-c7bc94c6ca50 | -7.84868 | -48.3914 | 2026-07-18 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e994c99-bfc8-31c6-b222-625c21392975 | -12.30159 | -50.08798 | 2026-07-18 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12efe73f-9f4e-3f74-914f-fd9fcd23554b | -9.47958 | -57.32238 | 2026-07-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 546e1232-f61a-33e7-bdea-185e09530382 | -12.12498 | -51.17144 | 2026-07-18 04:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bb2667f-4ebb-3383-b9a4-c49aab80b3a6 | -5.92507 | -43.64334 | 2026-07-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a11e72b-e849-3418-990f-abf0a2872998 | -10.80119 | -46.55312 | 2026-07-18 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f160ab27-b4d1-3aa5-be0a-f081d533fc2c | -6.83729 | -45.51123 | 2026-07-18 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 179cbf35-4fa6-3d54-834b-4303f0cee6be | -12.50603 | -48.25238 | 2026-07-18 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94ce7316-340c-3311-8e58-971aedc6d4d5 | -10.47603 | -42.48028 | 2026-07-18 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f50657bf-72e5-318e-b879-70dd7bd4b701 | -8.94303 | -47.6101 | 2026-07-18 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c56930d-a6ee-3f4e-a3f8-d77edf3fe756 | -7.2863 | -46.25642 | 2026-07-18 04:38:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eeb2b079-e19b-32b2-bde7-f424c34f9014 | -12.2243 | -44.00181 | 2026-07-18 04:38:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7d21d66-894b-3c7a-9f80-5264fcba891d | -9.47643 | -57.32434 | 2026-07-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3b416a7-e69b-311c-9959-7230370a7320 | -9.4426 | -51.81917 | 2026-07-18 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85942bee-2411-3e6f-ad6c-9a40ad2cb0b1 | -9.68599 | -56.10392 | 2026-07-18 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a750150-3eb6-39b2-9dbd-282a391c9441 | -7.47889 | -46.66899 | 2026-07-18 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 487f5b4d-a7aa-32a9-b4ed-21c7e9168df6 | -9.07533 | -50.59173 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06546bf8-4c8e-321e-aab9-f9d2cabbd307 | -11.59794 | -48.52562 | 2026-07-18 04:38:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90e3dc09-1ad4-3a21-9b75-b02b5307f195 | -6.60276 | -41.62567 | 2026-07-18 04:38:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0f59eaa-96c6-3cee-bb2f-c522f761f1d3 | -9.07472 | -50.59548 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d8d2f23-5409-376e-9aab-eef086ea94d7 | -13.29919 | -42.11261 | 2026-07-18 04:38:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.1 |
| e135675e-0079-393e-bcea-6841d6a883b4 | -7.91245 | -48.2453 | 2026-07-18 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21f2110c-d2e9-3b30-b39c-9b0b5a5a94c8 | -12.01217 | -50.57413 | 2026-07-18 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 871b06bf-5b2e-35ed-a48f-3f0b779503ce | -5.92961 | -43.63923 | 2026-07-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e4b1c948-d3d8-3874-baf8-2430ebca8c0d | -9.88172 | -53.33828 | 2026-07-18 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 167e6547-93d4-3b5a-a0ec-d466f8528548 | -12.05392 | -50.52907 | 2026-07-18 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cf6887c-c6b7-3ed4-8c07-0477b7667de4 | -5.63316 | -47.09963 | 2026-07-18 04:38:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb5013c7-d0b1-322d-ae0a-77ad75ae4f1b | -7.72976 | -47.24288 | 2026-07-18 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd31f247-b99e-3a5d-ae7c-656091277dde | -8.47273 | -50.21981 | 2026-07-18 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce727435-e644-3f22-8262-cfd20e59e76f | -9.47698 | -57.32127 | 2026-07-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be5e934f-7bcf-363d-9cea-144a81484ea9 | -9.07875 | -50.5923 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0815520f-c99f-3fb0-8c5f-c7a1a675aa9c | -9.48979 | -46.66209 | 2026-07-18 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 399f33e2-0112-39a2-ace3-efeab02ee84d | -7.84813 | -48.39487 | 2026-07-18 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b42819e-38d3-367c-95e1-4a5a849f0068 | -7.85089 | -48.39886 | 2026-07-18 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69f6309f-0ea7-315b-86ac-b177a2ea2d58 | -7.48227 | -46.66952 | 2026-07-18 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b80bd1f9-4d07-3034-b62a-6ec4a11d1217 | -7.83892 | -47.10727 | 2026-07-18 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51ea66a1-eed1-3aba-95cb-aa004c3eaf10 | -5.35554 | -49.16681 | 2026-07-18 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b35a4d6-e0e2-3e06-808b-399ead0f30a2 | -7.48283 | -46.66589 | 2026-07-18 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb49e76b-eb98-310c-b008-f0f98eb2c40f | -5.80566 | -45.11554 | 2026-07-18 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README11.md)
