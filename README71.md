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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 436ac3c1-b759-3782-8257-bf8210ab64fe | -19.87546 | -46.06601 | 2024-11-28 04:27:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddbbd6cd-9313-35b3-9c9d-60f64a9335df | -23.47517 | -45.34956 | 2024-11-28 04:27:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7cbeff7c-55e4-3ca8-9753-3e200e3ef7fe | -21.13294 | -49.98779 | 2024-11-28 04:27:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 13da2d79-bad9-3a06-a35f-f24cea7723f5 | -20.90042 | -43.82082 | 2024-11-28 04:27:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8feeb033-ffa6-3652-b330-f61c99ecf4df | -22.58789 | -48.05044 | 2024-11-28 04:27:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e46bf04-0a1b-3965-9da3-9b1031869365 | -21.12088 | -48.64662 | 2024-11-28 04:27:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f4c5becc-6d6e-3f03-9c53-e0659c2e7d61 | -18.7796 | -55.83801 | 2024-11-28 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 811633d2-928b-3ebf-a98f-c56c4a7f9963 | -17.63059 | -57.57797 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cdc47abf-a053-3510-9e4d-29ba93c1ad45 | -20.71799 | -54.43376 | 2024-11-28 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 34aba886-9f3c-35b2-bd74-f19d9712acc1 | -19.97178 | -55.09367 | 2024-11-28 04:27:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 058f95ea-e6e9-3475-8d10-2d740e0ca5cd | -20.67428 | -49.12406 | 2024-11-28 04:27:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27d99cfa-93de-32a8-b543-9d5de0731cd0 | -20.13033 | -53.32438 | 2024-11-28 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0e1889b-457c-33a2-b291-845c181be0cc | -22.11666 | -49.60464 | 2024-11-28 04:27:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6ca01e1b-b1a4-3aef-a570-645ffa247778 | -23.40411 | -46.55843 | 2024-11-28 04:27:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 584a859c-b562-3233-90e7-35b30d9f4055 | -23.33767 | -46.77431 | 2024-11-28 04:27:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 51129eee-bceb-39be-ae4d-8668cd38ea02 | -20.4256 | -48.77875 | 2024-11-28 04:27:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 327c99ca-1ff8-301a-a576-fa9db4fe6757 | -17.56267 | -57.47858 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f5f3250b-6641-33de-bcef-d7a8e5d6cb85 | -21.03964 | -49.34937 | 2024-11-28 04:27:00 | NOAA-20 | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ae1f248b-f96d-330c-b7f4-e0db0d60883c | -20.12662 | -53.32367 | 2024-11-28 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 427ae0a4-0ea1-3dfe-9bf2-c663c5eff422 | -17.17122 | -44.87791 | 2024-11-28 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f887754-c055-378a-8c79-c07e37157471 | -20.63073 | -56.58985 | 2024-11-28 04:27:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08b9d0bc-7331-3f93-92e0-4f37f317ff0e | -22.45812 | -47.68344 | 2024-11-28 04:27:00 | NOAA-20 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 97877c01-d820-3916-891c-68747af40242 | -23.32477 | -47.63977 | 2024-11-28 04:27:00 | NOAA-20 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6d700375-88d1-3336-b42e-5bbd6b7e9b7a | -17.62469 | -42.61119 | 2024-11-28 04:27:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2f0769d9-bc5a-3159-a621-3526e534c79e | -16.0797 | -60.11056 | 2024-11-28 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96aa76c5-2bc6-3603-ac93-d86af45fda19 | -22.11608 | -49.60836 | 2024-11-28 04:27:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8502506a-0de9-3804-8c13-81d2a251c64b | -18.10881 | -51.16662 | 2024-11-28 04:27:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9524fefe-a338-3237-9b6e-37304a7eb03f | -18.77347 | -55.84612 | 2024-11-28 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 472205e6-914d-3a59-b971-9096a47b6fb9 | -16.07367 | -60.1092 | 2024-11-28 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56327afa-83d2-3619-8e72-d226cd94d403 | -18.77082 | -55.83609 | 2024-11-28 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 70f3818b-59e3-3f17-9b09-30f8762b0728 | -18.76908 | -55.84517 | 2024-11-28 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b3536463-655a-346c-8d66-05b22dcba322 | -23.71609 | -50.55426 | 2024-11-28 04:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| b4794656-fc9f-345e-ac11-00f9069d3c1c | -19.54005 | -47.33855 | 2024-11-28 04:27:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 403b27d4-4e74-3256-8211-12da05932be9 | -19.88229 | -54.81265 | 2024-11-28 04:27:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 074534af-2d7a-32c7-a25e-7021a3b32b21 | -20.35446 | -47.45551 | 2024-11-28 04:27:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94988333-6812-3542-990e-be14cb3dfd0c | -17.57793 | -57.60442 | 2024-11-28 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9f584b33-f5b5-3895-bb49-77a6b23d2d8c | -17.28979 | -44.35208 | 2024-11-28 04:27:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69a1166c-67d2-3d2e-8420-94a61cb3ac8f | -19.2066 | -45.37911 | 2024-11-28 04:27:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16a60ea6-9953-3716-a6a1-41002ddf95ee | -17.67597 | -42.74541 | 2024-11-28 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e45c6e0-e3db-3ce7-bc63-e6308549567c | -23.70887 | -50.55679 | 2024-11-28 04:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5d9ce0b9-9473-3070-8c9a-48061ea9eee9 | -18.77786 | -55.84709 | 2024-11-28 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1e64fe81-cec3-3497-a365-e89eb68ec500 | -21.62679 | -46.38003 | 2024-11-28 04:27:00 | NOAA-20 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4cb223e4-33f5-34ae-99a9-824b2effa060 | -23.33343 | -47.66096 | 2024-11-28 04:27:00 | NOAA-20 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a985193e-2194-3dec-8b8a-45748c693f5b | -20.90475 | -55.32967 | 2024-11-28 04:27:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edc94642-bfb5-321d-8f7d-e859df4e05e3 | -18.70872 | -47.47963 | 2024-11-28 04:27:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f855cdf8-5021-39c2-9a55-ad4f30ed8731 | -17.22948 | -54.4431 | 2024-11-28 04:27:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 951ca2fe-0cce-3252-8fbb-fcf4f5829812 | -18.77521 | -55.83705 | 2024-11-28 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ac3143fa-f71b-3bf3-8783-90a1fb28291b | -20.32463 | -48.81882 | 2024-11-28 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43339b81-c907-3acb-a431-4b73a24d71f2 | -16.07955 | -60.1087 | 2024-11-28 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 006edd0f-d004-39fd-b8e6-7e20101603de | -20.45677 | -46.14226 | 2024-11-28 04:27:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffda0046-3baf-31c9-84a2-1fe73da2bf92 | -21.80651 | -50.84568 | 2024-11-28 04:27:00 | NOAA-20 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 651a3eb2-9e6c-3e1e-8171-df57a1ad783e | -18.25574 | -51.2701 | 2024-11-28 04:27:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03e22191-a35d-30d6-9a10-e440ab662037 | -17.63561 | -57.57909 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ee23297d-ab01-35ce-af53-b2839a2dc121 | -22.58847 | -48.04643 | 2024-11-28 04:27:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5f6a3ca-20c0-3b98-be40-e72fea45a3d1 | -22.11998 | -49.60523 | 2024-11-28 04:27:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f35e20ae-599c-3d60-8248-a997f7706609 | -16.07252 | -60.11205 | 2024-11-28 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a120c8b-0811-3d28-a72c-4264966d6049 | -21.2405 | -49.49817 | 2024-11-28 04:27:00 | NOAA-20 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 4352650a-e331-39ae-b316-858db8468e3d | -20.35103 | -47.45493 | 2024-11-28 04:27:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78b3cc0f-3c5b-357a-9702-aab11dd4bf76 | -16.88223 | -57.51258 | 2024-11-28 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a9ee1f95-71ee-360e-8e02-b0bcbb060939 | -21.95979 | -47.40722 | 2024-11-28 04:27:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1a0f2d07-cc56-33fe-b549-43d588e6039e | -23.3697 | -47.06047 | 2024-11-28 04:27:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| aa2a16de-ea1e-3d54-ba7a-2ad0d8571ed2 | -19.2083 | -45.38203 | 2024-11-28 04:27:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d800364-53da-3aaa-bb56-3e1fe4d9fc34 | -17.95053 | -47.07259 | 2024-11-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57100044-e545-3e5e-919d-d9f9f956b39b | -21.19599 | -44.93703 | 2024-11-28 04:27:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f17c5fdb-254a-381a-963d-333734c7b637 | -20.57726 | -44.57397 | 2024-11-28 04:27:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b5ae39d8-53b8-3a84-a85c-5f7f0e59db2c | -19.33197 | -45.6271 | 2024-11-28 04:27:00 | NOAA-20 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9119e4b-341f-3162-8f19-b86e7e43a75b | -21.12365 | -48.65095 | 2024-11-28 04:27:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 96d15b00-9a3a-3bc5-abca-2935436f1812 | -21.29185 | -50.58232 | 2024-11-28 04:27:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 21a20856-55fb-3e95-b76b-6c46037a277d | -21.89692 | -46.50457 | 2024-11-28 04:27:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b81edda1-f663-386b-9615-5ff9fcc66ba3 | -21.29579 | -50.57921 | 2024-11-28 04:27:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| de6f67f0-118b-33f9-88bb-3fb0459d456f | -23.98092 | -48.91768 | 2024-11-28 04:27:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a77078b3-a4b4-3899-a37a-f2c03f3f6d06 | -23.70556 | -50.55619 | 2024-11-28 04:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 90ccd4ce-80b2-365b-a432-68c1a8744d8c | -20.7992 | -49.17199 | 2024-11-28 04:27:00 | NOAA-20 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 16fadbf4-2918-31af-80b8-fe09f7ebdc3a | -22.82526 | -46.32654 | 2024-11-28 04:27:00 | NOAA-20 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4f604e57-b2c9-3fdb-a139-1cd59bcba3bf | -19.5264 | -47.33624 | 2024-11-28 04:27:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d4c7dd0-70de-3c46-826e-a02c481ee031 | -17.34812 | -50.52565 | 2024-11-28 04:27:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e62d1e8-63a0-352b-8b69-f9be1e0464b9 | -22.45954 | -47.68492 | 2024-11-28 04:27:00 | NOAA-20 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 486c67e4-d0bd-3cf2-ba32-6d35cd39a0dc | -21.6052 | -57.50061 | 2024-11-28 04:27:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25589ed3-f633-38a8-8371-912b056b36a0 | -20.67485 | -49.12037 | 2024-11-28 04:27:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3597026e-18ab-300e-993a-470335a60581 | -21.82532 | -44.19113 | 2024-11-28 04:27:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c889159c-4543-3c6a-8584-317b6cf40808 | -20.32406 | -48.82252 | 2024-11-28 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89060d09-014d-353c-85ec-32184b56a555 | -22.05878 | -49.73565 | 2024-11-28 04:27:00 | NOAA-20 | ÁLVARO DE CARVALHO | SÃO PAULO | Brasil | 3501400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 619f75d9-604a-3ab2-84c3-93a0df7f0a51 | -20.84201 | -45.42911 | 2024-11-28 04:27:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75cc9283-3858-3c0e-a157-08f0128e2b53 | -23.71941 | -50.55487 | 2024-11-28 04:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| a459b61d-6ed4-3857-aadd-5c080c104bb5 | -22.78305 | -43.75866 | 2024-11-28 04:27:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| de6c7163-661d-3281-aef8-61c4e2d38439 | -17.63499 | -57.58215 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 10b5341b-ec07-3045-ab8a-90532befc3a2 | -16.07867 | -60.1153 | 2024-11-28 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad9f28dd-6bb8-321d-af50-e856af8ac81d | -17.54879 | -57.44403 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d7e45e49-857e-34c3-be93-ecbafb7742dc | -17.57398 | -57.60521 | 2024-11-28 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 007c49ee-45ec-3fcf-a5a0-74d2eca054b3 | -19.89383 | -54.06082 | 2024-11-28 04:27:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1655a1ba-16b0-32cb-a51c-10b6dd81f962 | -17.62998 | -57.58102 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 045bf591-2f41-342d-a62a-c7b28883d14a | -17.5494 | -57.44103 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 14a99e69-8fcf-3b35-8df9-3ee379c2b757 | -20.32795 | -48.8194 | 2024-11-28 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b33aaf15-820a-38b4-8cb2-7a4fcfc4f602 | -21.29125 | -50.58606 | 2024-11-28 04:27:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| c3dd0f0b-afa7-3083-9e90-05f3cdef6e5b | -17.63622 | -57.57605 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 31869c6a-93fb-3632-b06b-5fa2494dfafd | -23.3386 | -46.77264 | 2024-11-28 04:27:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 33a529b1-e13d-3830-a9cb-c8027f80cf2b | -23.70616 | -50.55242 | 2024-11-28 04:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 63b72618-8ffe-3507-8d39-26fd2563d28b | -22.05489 | -49.73877 | 2024-11-28 04:27:00 | NOAA-20 | ÁLVARO DE CARVALHO | SÃO PAULO | Brasil | 3501400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5a67ac22-dbec-32a4-bebb-0f3b0c53d44f | -21.49661 | -45.10957 | 2024-11-28 04:27:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 30823988-62b8-377b-b0c9-f2f40aa40d4e | -16.07352 | -60.1073 | 2024-11-28 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README72.md)
