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
| 7316588d-d303-3565-a4b5-431a152c9b52 | -9.4435 | -60.5307 | 2025-08-30 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 545fbe1f-4d3f-3fd8-9852-70fdcfa29f5f | -13.3623 | -47.018 | 2025-08-30 03:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 06e0cf6f-9a66-3115-8ad5-3ba08ee65476 | -9.0614 | -65.4355 | 2025-08-30 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 05674fda-a545-3fae-a5b0-6fa38bfeab2a | -6.1853 | -43.3257 | 2025-08-30 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 75357fe3-bf48-3cca-9fbf-d20ef9acce3e | -9.462 | -60.549 | 2025-08-30 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| cbb292dd-a7d2-3e85-a3e5-207b3e0a3418 | -13.3821 | -46.9924 | 2025-08-30 03:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| e8abdba6-ce88-35b0-87b7-79d5a28a7be6 | -9.4432 | -60.5692 | 2025-08-30 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 4932015f-e104-3c9f-b46f-2d3348f041d5 | -13.9918 | -44.5884 | 2025-08-30 03:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| b4a3c4d2-34ae-3a29-b815-12e7c7a61179 | -11.8764 | -46.378 | 2025-08-30 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| a1e95c10-ce0b-3522-8379-6b33be60cc7b | -9.0799 | -65.4349 | 2025-08-30 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 62a56029-10b1-3a10-8e10-db7e57d4782a | -13.3817 | -47.015 | 2025-08-30 03:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 46ba21c4-f31f-36dc-abe9-03535eb460dd | -8.8843 | -60.7315 | 2025-08-30 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 3651e4ba-5729-34c1-bdff-ad40fa851bcd | -11.8369 | -46.4514 | 2025-08-30 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 6a10a307-80b2-3d55-923b-a8c3714a2a77 | -11.8572 | -46.3807 | 2025-08-30 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| d866fbbd-73ea-3078-ba78-48651adb34a8 | -6.185 | -43.3491 | 2025-08-30 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b5cfee98-4ba3-39f2-9c04-dd5065711330 | -8.9126 | -62.1058 | 2025-08-30 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 5fefd417-2a41-3d6a-a844-81b38add6d6a | -9.4433 | -60.5499 | 2025-08-30 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 178.8 |
| cf8887d9-3cc5-3967-85de-ba921aff4060 | -9.4247 | -60.5509 | 2025-08-30 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| f0a1b7ad-6b3e-3456-859f-2f9ca26f8950 | -11.8373 | -46.4287 | 2025-08-30 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 85e144f2-dcd0-3bdd-bc33-db9a9e4821c4 | -6.27663 | -44.4668 | 2025-08-30 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 72d14ab3-4d2e-3609-abeb-17e77cc59a6e | -6.17769 | -43.32455 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| d82a4de5-203a-30c4-898e-27c90eaf5c45 | -4.64888 | -43.63029 | 2025-08-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 001746e7-4bf2-3961-921e-4041de19146b | -6.5601 | -43.68454 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5911f9f1-dd92-336f-a93f-826be06e3a62 | -6.18296 | -43.33028 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d97a2b7a-9d13-3620-b411-036523bdaee6 | -6.61851 | -43.73971 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1246f51e-fa54-3445-9c3d-41f0df0cf550 | -3.08998 | -40.10437 | 2025-08-30 03:28:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 156292a6-42a9-3f8e-a540-10686ac07edf | -6.70406 | -43.09899 | 2025-08-30 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3d49af8-c94f-363c-b14c-9458318f9669 | -6.23625 | -42.40871 | 2025-08-30 03:28:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ebe91d10-4836-3a17-9da3-50ffc19f6d8c | -6.49715 | -43.54606 | 2025-08-30 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 63b96b57-ce58-3267-8342-2f0de9d613a7 | -6.81003 | -43.72627 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca9997a7-aad2-3ef6-984d-5f0ec8ebd6fd | -7.54399 | -36.73964 | 2025-08-30 03:28:00 | NOAA-20 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 19f06cf9-d01e-36c5-96c4-62ecc483d576 | -6.59796 | -43.6526 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| badd6cd1-1230-3333-a001-dee654711bcc | -6.18058 | -44.00094 | 2025-08-30 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbea8067-f82b-3535-b23f-8c718b650ecd | -6.17517 | -43.33834 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 292abea9-b719-3e9c-98a5-7302a97489d5 | -6.1735 | -44.86314 | 2025-08-30 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27d20dd3-6472-3a9d-b871-199664e8d312 | -6.80455 | -43.75534 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b182910-6248-314b-b85f-e2bd7cfb8330 | -6.17969 | -44.0058 | 2025-08-30 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f392ff4-6e87-3217-90e9-86ebcf319109 | -6.17335 | -44.00452 | 2025-08-30 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d056fbd6-7e5e-3937-9b4d-d73376fa3b45 | -6.17648 | -44.79386 | 2025-08-30 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d502a72-988d-3419-a096-3b531e8906c7 | -5.72871 | -43.94266 | 2025-08-30 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe4b726d-1ba1-3eb0-9c27-5c25c355d6e1 | -4.98655 | -38.60183 | 2025-08-30 03:28:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 996b0670-f1c2-34ff-b1e7-469e7d9cc158 | -5.77708 | -42.60429 | 2025-08-30 03:28:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| efd42dd6-0d47-30c6-819b-a28f7076ae9c | -6.50337 | -43.54689 | 2025-08-30 03:28:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 25941b0e-c3d7-3f18-8359-f33b5804db79 | -5.04773 | -37.99385 | 2025-08-30 03:28:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| efe940ab-f81d-3a22-b973-7725f476c01b | -6.18022 | -44.86432 | 2025-08-30 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffdc1ee0-96f8-3cbd-a3d6-0237f62ff2aa | -6.80363 | -43.76021 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f62795bc-ed00-3a15-b31e-e18fad8bfb9a | -6.8006 | -43.7528 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00d2661e-b382-3394-99f2-ec75c6d3745c | -5.68988 | -45.96233 | 2025-08-30 03:28:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69229b5f-1640-3218-8921-d6f541626d63 | -6.53971 | -43.10558 | 2025-08-30 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d2e81c5-237d-38cc-b0a0-fcf4247ccd86 | -6.7979 | -43.037 | 2025-08-30 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 24a02a26-6824-35c7-b51f-5e6beffcfe1b | -5.99586 | -44.72663 | 2025-08-30 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 642ad90e-c61f-3a00-a9b1-30401d3a98bd | -6.80547 | -43.75046 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bfa73efa-0fec-38f0-91fe-49e8b4851b88 | -6.18213 | -43.33483 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b115c945-db49-37f1-853c-9bf31c6ef427 | -6.09584 | -43.32292 | 2025-08-30 03:28:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34fdd0f0-245b-36de-91d6-2d430a12cbbd | -6.17883 | -44.01049 | 2025-08-30 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| be9a9f18-f020-3709-8450-31e7bbbd7057 | -5.69704 | -45.96376 | 2025-08-30 03:28:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 91137e9a-e02b-376e-bcf6-fbc2d41c642c | -6.18461 | -43.32119 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aea8df02-a5ea-39ae-b72c-971bf218d793 | -6.8135 | -43.74192 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6ad8461-dd00-3b49-9c21-c747499634be | -6.79971 | -43.75768 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b3364b20-32ef-3b6e-a3ea-25cc37139f55 | -4.65525 | -43.63147 | 2025-08-30 03:28:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b02aadd7-2af3-399a-b6df-438a3d22909f | -6.19074 | -43.3222 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d626d774-1009-3744-a239-0450258b8c22 | -6.093 | -44.00312 | 2025-08-30 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf3caf6c-f7e0-3f40-bb2d-ac63bf58ebee | -6.27617 | -44.46218 | 2025-08-30 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c062f509-6d32-3911-87ee-324462425feb | -5.72335 | -43.94283 | 2025-08-30 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9cd8dd31-c3f1-3ddf-bf3c-824451e9e1e8 | -6.18431 | -44.78877 | 2025-08-30 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5d0f73ec-a5e0-3f9a-9d97-cad2c77b5824 | -5.61252 | -45.00613 | 2025-08-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 983c09ea-6452-3683-8d53-ffe5af7ac7a2 | -6.59271 | -43.64626 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a390bef3-1946-34d1-b4d8-288fad33426c | -6.02486 | -42.815 | 2025-08-30 03:28:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 60b6f3f6-ce69-3051-ba57-9efd965017ee | -5.61135 | -45.01238 | 2025-08-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 116989ca-6d7f-38bb-acc9-396e5cd4b53c | -6.19336 | -44.00304 | 2025-08-30 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| acbebfa2-84b0-31f7-a692-a3d73e50f928 | -6.80413 | -43.73336 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af786746-4561-351a-80a2-cb7df24d1401 | -6.79615 | -43.77729 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf5ffe7a-7f62-38f6-b5c5-50c014121376 | -5.91354 | -43.35582 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6dc3808-d58b-36af-be9b-640b279195db | -6.6878 | -43.08646 | 2025-08-30 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebc1d7f9-4b6a-3aa0-a86e-6aaeb33ec684 | -5.6046 | -40.8117 | 2025-08-30 03:28:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63e55750-61cc-37ee-b94b-0b2683c8d452 | -5.61182 | -45.00379 | 2025-08-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ab07733e-4b33-3e60-80b1-f5d13211678d | -6.70486 | -43.09449 | 2025-08-30 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b644379-813d-3930-8c63-ad7f25921e11 | -6.08747 | -43.99727 | 2025-08-30 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92baaf94-e3dc-384d-b07e-8422bf145bb1 | -5.25105 | -36.91188 | 2025-08-30 03:28:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 154a7289-510a-37f9-9bed-281a447c0519 | -6.02407 | -42.81936 | 2025-08-30 03:28:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b90bb7d1-bee4-3c2d-a9ae-ab34cd3c44c7 | -6.20852 | -42.76441 | 2025-08-30 03:28:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 607c7445-8a76-3c74-a66f-a562db5e1e10 | -6.62011 | -43.74343 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8b12117-2063-3b46-8a97-2364756a1e8b | -5.1418 | -37.36118 | 2025-08-30 03:28:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ae5f3aa-44f5-3e29-a1f9-7b0f3c3d0663 | -6.23038 | -42.40829 | 2025-08-30 03:28:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d78cef3b-ce50-337e-a861-80317ec36c1e | -5.72434 | -43.93748 | 2025-08-30 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| deef30ff-2996-323e-b35d-8e9de30bd2e1 | -6.21005 | -42.75582 | 2025-08-30 03:28:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4b85969a-ed95-36f6-8874-aaf38f9c867e | -6.17686 | -43.3291 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| b65b6b47-67f2-316c-ac18-f947e5c37c57 | -6.18606 | -44.00699 | 2025-08-30 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 421f7bee-91db-301f-8f63-8351eb3382e0 | -3.08944 | -40.10758 | 2025-08-30 03:28:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3fa3819e-7625-3c8a-bd21-532bb94a2ecf | -5.04265 | -37.99734 | 2025-08-30 03:28:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d33af1cc-da78-331c-bf1c-e98c795c80f6 | -3.72642 | -38.68018 | 2025-08-30 03:28:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0275ca9b-1d3a-396d-83f8-e02b972cd849 | -6.20929 | -42.76008 | 2025-08-30 03:28:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 97c983e6-6768-3dce-9ca0-4c8c0436310f | -5.91885 | -43.36169 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b60df27-5563-3eab-ae7a-bd7e80c4d8a8 | -6.18378 | -43.32576 | 2025-08-30 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bdbd50b2-f75a-344f-beab-c8b58e8c4fea | -6.805 | -43.72854 | 2025-08-30 03:28:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e19a5b4-2068-3f9e-ac1e-ccbd0d686562 | -6.56161 | -44.22235 | 2025-08-30 03:28:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd7085ee-3eaa-3abd-91ed-4cc742efe79d | -5.7015 | -45.96704 | 2025-08-30 03:28:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cbaab81-22a8-324e-baff-1e3d798743bc | -6.59192 | -43.65062 | 2025-08-30 03:28:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ff4e0800-98a4-3e51-a98d-357cea14849f | -5.53142 | -36.85387 | 2025-08-30 03:28:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d0e8e26f-cb78-3596-8484-5b40adf644a6 | -5.53601 | -36.85102 | 2025-08-30 03:28:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README11.md)
