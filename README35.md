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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adba2821-d3c6-3e5a-a3a5-1f5243c1c44a | -7.29101 | -43.68325 | 2025-08-18 12:34:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e8824695-b8ee-3b4c-b828-bfb5c5fbe268 | -9.00681 | -46.03163 | 2025-08-18 12:34:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| b1af29a3-a24c-32c7-aa88-399fea8ab02b | -12.53262 | -48.49777 | 2025-08-18 12:34:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 002ec67b-1572-31b1-8573-da0669849229 | -8.86113 | -48.98917 | 2025-08-18 12:34:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b18cea44-d0f7-3dae-9b8c-d2ff6283a16a | -11.15148 | -46.89549 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8818b071-8a7a-3a96-8fb5-a0bc183cfb9a | -12.8459 | -46.01849 | 2025-08-18 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 891f7ead-928c-3c15-9141-f23a1d5b42a9 | -8.07145 | -47.70112 | 2025-08-18 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7251c9f6-bb82-3217-894c-e3a5c0e9edb1 | -7.98583 | -49.95614 | 2025-08-18 12:34:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 44aebb33-e7a2-3161-acc1-6eaccd62603e | -5.63737 | -43.14257 | 2025-08-18 12:34:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 37.4 |
| ce51e3d0-cb02-3354-bc41-5e16425c37c0 | -13.41454 | -51.72264 | 2025-08-18 12:34:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 29106df3-1490-36e9-99a0-03d6315732fc | -13.1998 | -50.77024 | 2025-08-18 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e906164a-8f9f-3b1f-b0c2-9d1e3b551da1 | -7.5701 | -45.44256 | 2025-08-18 12:34:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 380719da-e6e8-3d0d-9458-631b099c6c0f | -11.15517 | -46.9498 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 2aa18e4b-d0cf-322b-bf76-161d999d68ac | -7.19756 | -46.24341 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| be07a1d0-4c47-3802-8d4d-70bd537f9c3e | -12.63099 | -46.88937 | 2025-08-18 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| be1fd58f-5ecc-3814-920a-a8d882fa1938 | -5.67236 | -43.38138 | 2025-08-18 12:34:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| cf07f202-bdbf-3403-bd8b-ed122dd0ba45 | -13.15885 | -54.91869 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 5798c1c8-58d5-34cb-99b8-fa6e2150fab9 | -13.96079 | -43.33228 | 2025-08-18 12:34:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 814d23e6-67a0-3859-a895-a49faa8e60c6 | -11.84915 | -51.57963 | 2025-08-18 12:34:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 680905d7-90ae-32ba-b2cf-83782f6f5caf | -13.15808 | -54.92475 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 517db8e8-8e5c-36ad-8930-f3755f0c7070 | -13.29438 | -50.81783 | 2025-08-18 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c99e0313-c4bf-364f-8391-1bd0e91f758d | -13.15624 | -54.9367 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 04e1bb91-686e-36ad-b9fb-7ab369837d3b | -7.57214 | -45.42725 | 2025-08-18 12:34:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| ee565674-4b2f-37eb-b712-9384ef3d90cb | -13.22476 | -48.27386 | 2025-08-18 12:34:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0e8deafc-91df-30b3-890b-46f0a6cca608 | -13.17703 | -54.93378 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 2b42f8d2-d55e-35f2-9397-10a63c4942eb | -11.14083 | -46.89375 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 99a1e07d-3d5c-38b0-9003-c0ace7f008b5 | -12.8527 | -46.02591 | 2025-08-18 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 59b3b886-e193-3e7b-9fcd-22ed829e8940 | -13.58166 | -46.98991 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 29f9ca5e-8e41-3427-b3f2-056779879899 | -13.87501 | -45.52684 | 2025-08-18 12:34:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| f1b03439-2e50-302d-b93b-ac0559dab31c | -6.86136 | -42.80082 | 2025-08-18 12:34:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.8 |
| d37dfdf3-5534-3711-bca9-3d6d068e9048 | -10.20133 | -48.27773 | 2025-08-18 12:34:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 24af953c-d1b6-39da-ab44-5a2b6bbe693a | -13.23346 | -50.73433 | 2025-08-18 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c2fa42fb-cb33-3ae1-b2cf-9a2534198dbf | -8.33834 | -47.62265 | 2025-08-18 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6352146a-925a-3d3c-ad9c-e1edb82ac6bb | -12.64796 | -45.33678 | 2025-08-18 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 1e582a78-0000-3de0-9f7f-89de7513a0dd | -6.51224 | -45.46355 | 2025-08-18 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| db7e1ff3-094f-33ff-81df-5a748d0f2cd9 | -6.96541 | -43.57618 | 2025-08-18 12:34:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 252.3 |
| 22648240-9156-345d-9615-579e5def7c02 | -13.24228 | -50.80103 | 2025-08-18 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| a153241b-7c81-3585-a9ff-e76c613ff3e6 | -8.32857 | -47.62147 | 2025-08-18 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 23906e4d-a562-3696-b896-b8bcb1cfb8d0 | -14.62746 | -54.90648 | 2025-08-18 12:34:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 2d7b326a-9934-3eaa-806c-8dd8a9576874 | -6.55547 | -49.5117 | 2025-08-18 12:34:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 770efb91-9f5c-3825-92c0-3e4e439012b9 | -14.45793 | -53.03827 | 2025-08-18 12:34:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5a74b138-30ec-37fc-92f0-bb8361258365 | -6.5628 | -44.46779 | 2025-08-18 12:34:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1709a42a-f99e-340b-9572-9a5970dc38e9 | -13.59433 | -46.97818 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1255d703-8548-3cb2-bdda-520c4951ff5f | -5.5633 | -43.60436 | 2025-08-18 12:34:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8a64dc40-7d3c-3cf8-913e-a6b155882e8a | -6.51037 | -45.47772 | 2025-08-18 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 14705872-4fbd-3018-9e14-5a393f696814 | -8.19911 | -47.3651 | 2025-08-18 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6a8aeced-b460-389b-93a8-6790c13ad3d1 | -12.30268 | -50.00732 | 2025-08-18 12:34:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 51cdfcc4-c4e4-3bf3-bb96-7c51a987a3fb | -6.55071 | -44.46639 | 2025-08-18 12:34:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 81611b76-3ca4-31c3-9c37-536419975b24 | -14.17292 | -45.32475 | 2025-08-18 12:34:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3bf18b79-4e9b-36df-b9b3-cded20cf7bc5 | -11.13733 | -46.92054 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 487ccfa4-f789-3ebb-bfb7-79925477b344 | -6.37381 | -43.30915 | 2025-08-18 12:34:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 9b6ddde9-c62f-3a12-91b9-91ae94973729 | -15.49729 | -48.5238 | 2025-08-18 12:34:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6b0237fc-afb2-3099-9e87-a64f15bc5569 | -8.20368 | -47.33121 | 2025-08-18 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c36d08a2-b329-3c7d-9c00-205b8db13b94 | -14.45932 | -53.02888 | 2025-08-18 12:34:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e129ea91-7164-36f1-82af-6ea56f96446b | -6.86692 | -42.80839 | 2025-08-18 12:34:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| bb804a1c-8fa4-35f1-aeaf-a3d51d39cde8 | -11.14971 | -46.90894 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 212.1 |
| d1bb1f7e-3ef4-3c42-8f32-ccb37d016219 | -7.43516 | -44.89787 | 2025-08-18 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5f9cb0cd-c26c-36a3-965a-ac238a8aa254 | -11.14625 | -46.93526 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 308242f8-7ab8-3ec2-b99e-9b8da438ed2a | -11.85799 | -51.58092 | 2025-08-18 12:34:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 76ca79da-db1c-3c2e-8da5-8dc540f2fd1f | -11.15693 | -46.93656 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6b3a9afa-9d28-394c-8b2c-962f533174c2 | -8.99607 | -60.51968 | 2025-08-18 12:34:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| bc67c3a2-4783-3d93-9ce5-af6f403238d5 | -14.97518 | -50.11585 | 2025-08-18 12:34:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| c52665fc-f6ef-3620-9ac4-6f1afc2d57ab | -8.72897 | -47.99114 | 2025-08-18 12:34:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 991dfb98-e54f-3380-a179-1ed132030452 | -8.33982 | -47.61165 | 2025-08-18 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7304efa1-c575-3195-b91e-76ca27902d58 | -11.13906 | -46.90726 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 4a9b48dd-1d58-3dcb-9088-58d5305b7d57 | -9.49304 | -48.35627 | 2025-08-18 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b604033e-7759-31ab-9f37-14a664a9ccfc | -13.24357 | -50.79188 | 2025-08-18 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 8ceeadf2-ecbf-3d8a-80e1-d54113069a75 | -7.17043 | -43.50776 | 2025-08-18 12:34:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 21517dbb-acb5-38d0-a6e8-314dfe16a57d | -12.30137 | -50.01674 | 2025-08-18 12:34:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| c3da767e-2b2c-3c3c-ba24-f748eb79bec0 | -11.85668 | -51.58992 | 2025-08-18 12:34:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| fafdfdaa-8990-38bf-b651-b262d515f872 | -11.15867 | -46.92337 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 9c4facfe-6588-35b3-a02d-2d7dff219d11 | -6.54661 | -49.51045 | 2025-08-18 12:34:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ff8929a7-356a-39ae-825e-be52b8a5c008 | -6.35626 | -43.64269 | 2025-08-18 12:34:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a6d754d9-3b3b-38d0-a34c-ec2c704c859a | -8.38306 | -44.98531 | 2025-08-18 12:34:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a7817d19-f3af-301c-8868-2a111de037c0 | -14.18802 | -45.30622 | 2025-08-18 12:34:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 77be3311-5337-3917-8924-db2df0e5471b | -6.96275 | -43.5969 | 2025-08-18 12:34:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 215.7 |
| fbc0d661-a3d7-38d0-a936-b5aa949838e2 | -5.79302 | -45.0096 | 2025-08-18 12:34:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f93ee0db-3813-3045-85ee-e147ff8c6282 | -14.97386 | -50.12572 | 2025-08-18 12:34:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7781092a-5219-3443-8a5c-09786e45ad8a | -12.54238 | -48.49903 | 2025-08-18 12:34:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6255278b-7061-3c1d-8a2c-7eb6b0dca290 | -11.14259 | -46.88026 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b7e702f7-3d3c-3e79-943b-c77d5027f112 | -13.16508 | -54.94413 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 915aaf68-f38d-36fc-856e-7d5421afbb77 | -14.87534 | -52.58558 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 06a4da93-d0ac-3f7e-8739-9544fec6df56 | -5.5635 | -43.60991 | 2025-08-18 12:34:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 34e47cae-2f47-3785-821e-0c45a17324c9 | -15.14135 | -44.01417 | 2025-08-18 12:34:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 2c4a0036-1c3b-3f1d-83ad-c6b59052821d | -13.64775 | -53.69347 | 2025-08-18 12:34:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| aa8bb5c0-b00b-3ed8-8335-697a39146ec4 | -13.16889 | -54.92025 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| ef269cb2-caae-3db5-8160-a2cc0f1a6679 | -8.19072 | -47.35245 | 2025-08-18 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7cb8044d-4d65-3e05-969d-9a8923a4928a | -12.61831 | -46.90141 | 2025-08-18 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 18623515-4416-3809-94ac-f88fe9b9b7c7 | -13.15236 | -42.5555 | 2025-08-18 12:34:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 7cda6779-2a9b-3459-a9c5-3a79d2eb4f77 | -13.57999 | -47.00335 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 119a7596-9c3c-37e9-b9a7-18e7bcd03b7f | -13.15694 | -54.9306 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 18b9d391-03fd-32bb-b837-abdea6e421c7 | -8.78315 | -49.99627 | 2025-08-18 12:34:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| acffa6a8-e4b5-3d52-8622-aad48367c5a9 | -12.65012 | -45.31823 | 2025-08-18 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 0d4aada7-76bd-38d8-b0b2-80f5450e8b2a | -13.19592 | -50.79769 | 2025-08-18 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6f7a5c9a-329a-3df7-9a1b-6495092d09a4 | -10.57864 | -52.497 | 2025-08-18 12:34:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 57c930e4-3c64-3eae-993a-f080c968a0f9 | -13.58869 | -47.74616 | 2025-08-18 12:34:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2f455e7f-419f-379a-95f2-789d00313b74 | -5.67063 | -43.38776 | 2025-08-18 12:34:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 0515a954-229d-3d7e-bb8d-fbac6f08303f | -13.16699 | -54.93218 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 670.1 |
| 94d411ad-3fba-3c53-951d-da3aa97714e3 | -9.54423 | -47.23855 | 2025-08-18 12:34:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 27a31bb7-2c48-3150-ba18-763d7aaab0ad | -6.35901 | -44.5331 | 2025-08-18 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |


[Clique aqui para ver as próximas entradas](README36.md)
