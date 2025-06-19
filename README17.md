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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc226cab-45f3-3ec8-b306-05919cbb0ac7 | -10.64262 | -49.45578 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8a0a81e9-5388-3532-9fe1-f29fdccc076a | -9.41647 | -48.42575 | 2025-06-19 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 756afb0f-07e1-364f-bb34-4ca2a2c5bb0a | -10.45968 | -58.68559 | 2025-06-19 04:19:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d044d3c6-76e5-3dc9-9bd3-d4e9b1de1a24 | -12.20376 | -49.62731 | 2025-06-19 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64039483-b597-36d5-a173-3d3a8f747771 | -14.44166 | -48.913 | 2025-06-19 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efd509a0-befd-347b-9e5d-f76ed96b8269 | -3.07942 | -40.07755 | 2025-06-19 04:19:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aab860be-3060-31fc-9e1e-49edfc43b924 | -3.40455 | -43.10295 | 2025-06-19 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f2c048cd-035c-39bf-974c-cb145e74f228 | -11.95168 | -58.74185 | 2025-06-19 04:19:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 54267e3c-ea93-343b-8305-55216b378dbd | -8.75069 | -46.94249 | 2025-06-19 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39ebd261-f0d9-3152-9ce6-da41e9fc1daa | -7.80117 | -46.04609 | 2025-06-19 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7b7431b-5693-3178-8d79-456cd1a50c8b | -11.28665 | -48.68958 | 2025-06-19 04:19:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e621eeb4-ad69-35c7-bfd9-0249e7288ff1 | -12.02468 | -57.08916 | 2025-06-19 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 573189bb-a0a7-3d6a-9c79-a86084767a99 | -10.64635 | -49.45643 | 2025-06-19 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9caccd97-419c-3188-9e4e-9c8921159257 | -11.08249 | -55.05397 | 2025-06-19 04:19:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 773c0d46-c6d1-336b-8063-c9e3229d2d9a | -14.44363 | -48.90123 | 2025-06-19 04:19:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 052ccb6e-e780-370d-be41-ab16096a9e57 | -12.06893 | -48.46153 | 2025-06-19 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76d39ee7-f52c-39fd-9ca4-3c28e253c449 | -8.1243 | -46.08651 | 2025-06-19 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13321da2-d26e-38a6-8780-fa0a05759c27 | -12.29073 | -48.80269 | 2025-06-19 04:19:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48fd6f0e-1468-3814-a063-8fa695f59e2d | -12.26832 | -44.60494 | 2025-06-19 04:19:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8db721af-d1e7-38b4-888d-38ab2470c8cc | -9.38023 | -47.63838 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 134a914d-2775-3c95-9e79-b1060b3945b9 | -14.2159 | -45.51517 | 2025-06-19 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c94b4ec7-2a72-3cae-af60-1c1fa365496b | -12.08086 | -45.77669 | 2025-06-19 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f995530f-538d-33b4-9cda-bcdb21e1f80c | -13.31013 | -48.75682 | 2025-06-19 04:19:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 838cc867-7663-367e-ad8b-09561c10299f | -9.3774 | -47.63397 | 2025-06-19 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a253bc5c-b8f2-3467-bdd0-a9df28091ede | -9.49064 | -56.09193 | 2025-06-19 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 87452868-b5fa-372b-bec2-17fd13d5f03f | -9.7914 | -47.1785 | 2025-06-19 04:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 942e1b39-a688-3105-ab34-1b861d7920a0 | -11.9709 | -58.7362 | 2025-06-19 04:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| adf1b4b1-7fe0-3a42-9808-605ec4985b21 | -11.9707 | -58.756 | 2025-06-19 04:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 99e6be28-cba4-376f-9cf7-b66829d871c6 | -7.2405 | -43.0899 | 2025-06-19 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.2 |
| e568f3e5-5062-3e0e-8f0b-c9ed8ff70479 | -8.0703 | -43.0981 | 2025-06-19 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 774ef77d-5b0d-3498-949b-a3da1b3c3c66 | -16.3047 | -58.2676 | 2025-06-19 04:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| f67b2284-1ef0-3501-9d0b-64234141b4ad | -11.952 | -58.7376 | 2025-06-19 04:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 55eadda8-c43c-3424-bb7e-ee8fbd0aebb6 | -11.9518 | -58.7574 | 2025-06-19 04:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 6c6dd0e3-409a-385d-bdef-18e8df16e1ed | -8.07 | -43.1216 | 2025-06-19 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 9fc4067e-b4e7-34c1-8b0d-64442c36f80f | -21.43355 | -45.08128 | 2025-06-19 04:21:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 54dddfa9-2308-34b4-a93b-e65988667d3a | -16.28621 | -52.92902 | 2025-06-19 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f737400-7ce4-38b4-8e15-441b0177dbe9 | -16.30754 | -58.2574 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 461f3431-2cd5-3250-bf64-a1f9613cec79 | -15.29112 | -48.66248 | 2025-06-19 04:21:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9d1d15eb-5333-3af4-8743-47c34d8cda6d | -13.5773 | -59.20295 | 2025-06-19 04:21:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca44d7f9-db98-382b-8cf6-66e00af7bf74 | -16.30165 | -58.25603 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 2ec622ac-243a-3986-a0a3-eacc1da8afa2 | -20.94138 | -47.4285 | 2025-06-19 04:21:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d242633f-da70-3ec6-b1fe-640296260897 | -21.10327 | -47.78672 | 2025-06-19 04:21:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 446c1446-2d2c-3020-9a48-e8c410528291 | -16.67962 | -43.88475 | 2025-06-19 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 796308d9-0e48-3ff9-b30c-488a4fae3f5c | -20.93806 | -47.42791 | 2025-06-19 04:21:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 259b06d8-b826-391a-b587-b3352deed7a6 | -16.29977 | -58.265 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 81892dff-7426-31c4-bee8-315ce7641e39 | -16.28544 | -52.93443 | 2025-06-19 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de129ece-1c03-364d-b349-9443033375d2 | -21.0906 | -48.68322 | 2025-06-19 04:21:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 62ee65d1-e052-3d80-b13e-519b8c8b65e6 | -18.66264 | -55.75489 | 2025-06-19 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 7b464306-484c-37ea-a426-5b32e7c6efd0 | -16.30339 | -58.26327 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 52e211e5-d21c-38ab-888a-24b38cf26acb | -19.45492 | -45.30592 | 2025-06-19 04:21:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59405698-0636-3bc4-9dfd-62471361461a | -19.12668 | -52.70121 | 2025-06-19 04:21:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5252c6e8-aee1-3b8b-83b0-ed34f65a40ee | -18.30186 | -54.25894 | 2025-06-19 04:21:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89187bb1-407a-37ef-a90f-d446e4f93a0f | -19.96965 | -44.21569 | 2025-06-19 04:21:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1298d585-2554-3c8c-967d-9a08b6e49379 | -17.09435 | -43.8041 | 2025-06-19 04:21:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7971ea8-6824-3ea9-91e8-9e52b83ec999 | -16.64007 | -48.49063 | 2025-06-19 04:21:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cca586b8-fc6f-3595-b9d3-f7c5391dc808 | -20.44987 | -50.0074 | 2025-06-19 04:21:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1e29ec8-84ce-3588-9765-6dcb2d765784 | -14.02956 | -55.11969 | 2025-06-19 04:21:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88f23267-69d3-3ed3-8953-ac36af793427 | -14.02839 | -55.12563 | 2025-06-19 04:21:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 725cd54c-9bca-3cae-b773-adba3cb47905 | -16.13384 | -52.24541 | 2025-06-19 04:21:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed96f8bf-631f-3411-a881-f875ac8cbb53 | -14.02391 | -55.12167 | 2025-06-19 04:21:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01714af4-4dd9-3189-8814-8d846908f6f3 | -21.70919 | -54.12147 | 2025-06-19 04:21:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d81f3c5-6cc7-376d-bd63-8fb95947efc5 | -19.96194 | -47.20296 | 2025-06-19 04:21:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e76a604-dff2-323a-a48c-d5ac647f11e8 | -21.78384 | -52.75998 | 2025-06-19 04:21:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff4c4275-a464-31d3-bca9-ef644920a682 | -19.58623 | -49.10522 | 2025-06-19 04:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dea60cc7-ac33-3c3a-8017-583cc08c26a6 | -16.30071 | -58.26052 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| b39ceacb-622d-3bf6-9f39-f89c8f927bd0 | -16.2847 | -52.93851 | 2025-06-19 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4363cc09-13cc-327c-b43b-2985f6ceca38 | -16.64798 | -49.36707 | 2025-06-19 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92182f90-4f9c-3af4-a360-143cc68faad6 | -21.19363 | -44.93513 | 2025-06-19 04:21:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7fbcb26d-33f4-3e70-86f9-9ca1388e8b25 | -19.96251 | -47.19928 | 2025-06-19 04:21:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 251efce9-c6e7-354c-9263-9fb863171c39 | -16.2985 | -58.25734 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 6057bd20-875d-3b34-b041-43ff8f284bc0 | -21.13137 | -47.80306 | 2025-06-19 04:21:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc43b3eb-930e-3b8f-9e85-122eaf5e9aca | -22.53798 | -48.81323 | 2025-06-19 04:21:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c21bae67-8934-3118-87ba-476173cfd0be | -18.65413 | -55.74707 | 2025-06-19 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5ff36b4f-8c5d-3df8-80f2-c5f575233844 | -16.31126 | -58.25549 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| f632e922-7266-3e86-b779-fd5bf9ef1bd6 | -18.65782 | -55.75378 | 2025-06-19 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| b5d09a88-316e-3da1-8f7c-26fadd0f6de4 | -16.30536 | -58.25424 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 5cfa28ed-6bbc-3597-86a1-67d4f6210ab9 | -16.32191 | -53.79158 | 2025-06-19 04:21:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2cda192-56d7-3c51-9528-c689da42a2c4 | -18.72631 | -46.87648 | 2025-06-19 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2dddaae-d701-3a71-972f-181dae1d7c4b | -18.99422 | -52.0805 | 2025-06-19 04:21:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 21dfe18c-e8b0-32e6-8c63-35b1e59c2e51 | -16.31661 | -53.79525 | 2025-06-19 04:21:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca2cb364-b994-35e4-b33e-5ae25701a891 | -19.0834 | -45.43294 | 2025-06-19 04:21:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf98e9cb-2ad6-3bb4-9797-d000084732c4 | -19.12372 | -52.69499 | 2025-06-19 04:21:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dc235b3-d37c-3560-b3d1-96838c63b88b | -20.76369 | -46.76996 | 2025-06-19 04:21:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fbde8501-1af0-30b5-bb65-8f67a9327fa2 | -16.30437 | -58.25876 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 2ce7e79b-0fec-388b-a847-e0357cddb07c | -20.99518 | -51.79053 | 2025-06-19 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c66b1549-2777-3ec5-8135-5e9fd9fd2fc9 | -17.75567 | -52.42724 | 2025-06-19 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 132aeeff-11d8-3a30-a816-ae440c653af6 | -19.71838 | -40.3556 | 2025-06-19 04:21:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7d4c7673-d40c-34bb-9a65-456c7ce67d72 | -18.99804 | -52.08126 | 2025-06-19 04:21:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c019970-2d77-3585-a1e0-56731dda4904 | -21.01231 | -44.20994 | 2025-06-19 04:21:00 | NOAA-20 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f0e91de7-736f-312e-b297-6c0816fd9408 | -20.47604 | -53.6746 | 2025-06-19 04:21:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddd0b488-6a83-36db-b90d-615b796787d4 | -18.05962 | -44.4939 | 2025-06-19 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dfcadcd-aaa6-3dd7-b411-22e79aff22f9 | -19.58475 | -53.50152 | 2025-06-19 04:21:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48f2d672-330f-3cef-9392-bb16604a996a | -16.29948 | -58.25285 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 0ad69716-8033-3955-8cd6-0520ae9be2be | -16.30634 | -58.24969 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2b0cc956-3165-3226-8da9-5a130f0db25f | -22.22812 | -46.75606 | 2025-06-19 04:21:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 04580345-64b5-3e22-aa9c-78b7411ee7f2 | -14.0278 | -55.12861 | 2025-06-19 04:21:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 201cc1bf-581b-3ead-a798-9e0a802bf3c5 | -20.94527 | -47.42538 | 2025-06-19 04:21:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94aba34b-7167-3fb8-9475-0c18cff4c496 | -19.71721 | -40.35194 | 2025-06-19 04:21:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4ab4a04f-30a9-3f03-b3b6-e5fac74a4f85 | -22.55143 | -42.20417 | 2025-06-19 04:21:00 | NOAA-20 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 843ca50c-d69a-3920-a227-699cbd588c88 | -17.31654 | -44.89707 | 2025-06-19 04:21:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |


[Clique aqui para ver as próximas entradas](README18.md)
