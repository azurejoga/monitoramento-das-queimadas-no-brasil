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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21208bbb-a1ea-3257-ace7-07e447d6942f | -9.5615 | -55.37973 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 39f71a53-9957-35fd-8564-6204fd4fbdf7 | -9.01814 | -65.69688 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fd19c0f-d6f7-3ef6-96a5-6f52fe1133e8 | -9.64855 | -64.99 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56c39114-d2eb-37a7-938d-f1a1cbdb7dd1 | -9.043 | -65.73047 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ecbffe1-4462-30ab-af44-1be816cf6788 | -11.30578 | -55.10797 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47d03a9c-7bd4-318c-ad14-8f3b01d8a818 | -9.16212 | -60.77134 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11043ec4-f0d0-320c-b031-6269aa8b4a27 | -9.81022 | -64.24512 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d25899f-6631-3748-b35b-4507aee0a080 | -6.82261 | -58.96885 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e72d882d-8736-344d-8b97-16d986832952 | -10.79276 | -60.78607 | 2025-08-27 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4959295-1f8e-3b53-8efa-306645b4b46c | -8.46178 | -64.05018 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25f7b540-c738-304c-8c2e-5d5481d03d98 | -8.90465 | -60.76241 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc7435e3-59a2-3bee-ae7e-b5deb9ef4229 | -9.80185 | -64.2609 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8ed24244-167f-3c13-a333-a113bb4b9526 | -9.20493 | -59.43896 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55938d3b-d6e8-3a3d-912f-b90ad8bf15fb | -13.38754 | -46.91541 | 2025-08-27 05:18:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 32.1 |
| e6020466-2568-3c43-91c6-f10bf0b9abad | -8.11034 | -62.87777 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c79140d-2dae-3dc0-9f1e-8f351a8c085a | -7.48049 | -61.36226 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc550477-3d14-3214-abad-f4537617d43c | -9.59072 | -55.36906 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb08713e-829d-3079-974d-d27f43ff60e5 | -8.34751 | -62.94096 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4330ed24-c67b-3a0f-a75a-1cde748b74fe | -8.55416 | -63.93859 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e65d8a9-eb81-3674-b09a-2ecd071b950a | -8.96199 | -65.98197 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c0b0762-1eda-3714-b495-195458602f1c | -7.73564 | -50.28234 | 2025-08-27 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 981d91c3-a655-3148-91fa-cbe910a50f17 | -6.83469 | -58.95657 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46617927-aad8-31fe-b469-c5e11610b792 | -9.80352 | -64.25125 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 623debc6-f473-3b7f-a458-21e8e3723fda | -9.92264 | -54.71754 | 2025-08-27 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57380bf6-af6d-33cb-9696-b0b5244ee0c7 | -9.3953 | -60.52329 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a164d55-01d7-3522-90cc-67f40dd76c4d | -8.65694 | -67.26926 | 2025-08-27 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cbb50f8a-97f0-3fe0-afa3-5d287f29cae2 | -9.40914 | -60.5219 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0886125-f552-3e70-868a-92781df6dee2 | -9.79467 | -64.2673 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55add74e-e9a1-3716-8493-e84e4079f928 | -9.23531 | -60.82316 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4a4998c-4d06-38e3-ac43-146f90ba86d2 | -7.54349 | -63.85324 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92d09e37-ddda-330d-b8cf-a5daa3c6ce4d | -8.57001 | -63.89207 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38a3232b-6a15-3280-b033-92c303c6c5f4 | -9.18362 | -60.8039 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fd07546-9729-39c2-a67d-8ace75fce5fc | -8.295 | -46.32601 | 2025-08-27 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28dcf496-a254-3641-bdc9-1fc3407526e9 | -9.21755 | -60.80574 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b61b363-fdab-36f2-ae8a-25fe16f6c48d | -9.41411 | -60.53351 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a6f4f6c-ce6a-3272-9751-cc3f755b8a5b | -9.15489 | -59.56234 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd39c811-2279-3853-bd8d-89f444a14ee2 | -11.52409 | -52.12997 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 85e2c177-98be-3825-83d7-fa1012019bfd | -8.95207 | -64.13519 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f557163d-5104-3255-8c93-c0d3447f2609 | -8.91144 | -60.71981 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f73bc41-5f1c-3d92-9d74-b64b13964a68 | -7.36202 | -70.14368 | 2025-08-27 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8845c4b-3862-3328-b913-b9545fe2ccde | -5.61729 | -60.6515 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1de4f91-dbe0-3ecf-abef-a08de350a136 | -9.0231 | -65.69363 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4e13c35-69e5-3c42-8c9f-daad8a3c2ef6 | -9.17908 | -59.45273 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c6dc125-8186-3849-a5d6-2b9171a1c670 | -6.33848 | -58.18803 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6485fe51-df97-37db-8dda-dcbb148485fe | -9.07056 | -66.06068 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e622050-4d74-3d6a-a9fc-b48626dc6cd3 | -9.16992 | -60.76532 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c705c42-008a-3035-ad99-713487bd8273 | -6.82038 | -58.96142 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 90278afd-cde8-39ac-b3e8-c358ec6e4b5b | -6.63023 | -58.54484 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ca744c2-bfc9-30c0-909a-596506571f78 | -10.10414 | -62.89838 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9e7fda5-9ebb-3aa2-ac20-f5a1ad13855c | -9.17096 | -59.50495 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 499e769d-772e-39c5-972d-1cbb6e32df28 | -8.89464 | -60.7608 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c78293d-844c-3c2c-a322-9f2363fe8303 | -8.86803 | -47.16658 | 2025-08-27 05:18:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c61b5fa-dcbd-3fda-85e9-bcd0ba8d5d3d | -8.13002 | -55.36826 | 2025-08-27 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76bc1fb4-dc75-38d0-91f9-dacb2559f112 | -9.41079 | -60.53297 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fcad32c3-0f54-3e0a-be67-649c04e34b77 | -9.11579 | -67.70422 | 2025-08-27 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e5fbeab-bea3-317a-9211-39a788e81db0 | -7.35207 | -57.63245 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8112a566-04bc-3208-afab-3c11d61ad183 | -7.43684 | -57.63037 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4d45029-7261-3bc3-8448-8c65745918ad | -9.03444 | -65.72907 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c7bc32c-6f32-3c09-baf6-8d5524b9c0a9 | -11.3093 | -55.11222 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c7f22b4-2fba-322c-972d-2057ecec07a2 | -8.9976 | -65.41706 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2c95ae87-2f2d-3a82-a310-207f909da817 | -9.52356 | -60.50787 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cee50d35-5e73-3de1-991e-de0d2a111828 | -9.27513 | -56.91189 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ac6c1b0-c321-3f6e-aac5-2a650749fe25 | -9.18731 | -59.44333 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bb7ce10-9521-3d19-a1b4-b1d9a346b30b | -8.92504 | -65.93661 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45079187-ba15-3f79-9310-2abcb4f3a65e | -5.3198 | -60.1975 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d5c4104-7c16-3c59-b5fa-ac612dff6199 | -9.17962 | -59.44925 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4feffe17-af27-3c20-aac7-6853fa03f382 | -9.63891 | -59.64342 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6a7d2d1-a158-3430-a4c4-38cfebc3e956 | -6.81769 | -58.97871 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c805f9cb-19c6-3de9-b007-0a2a39da6abe | -6.71103 | -58.57165 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c914462-c844-3305-b70c-28124097ffd5 | -7.05707 | -59.81854 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13891441-e89e-3718-a440-3791f6e200ae | -6.24199 | -60.02478 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a68b9f2-e267-3751-95e1-8de3793c36a6 | -10.27465 | -64.50748 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73036821-281f-3a81-a48c-ce153e758a55 | -9.18846 | -59.45778 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f64b1663-1834-30af-a952-7976aa9be316 | -8.84627 | -62.44595 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db8ec8cf-4c3b-32fc-9d1d-a0465e4f7c5b | -12.74183 | -48.19447 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4f64c19d-3033-39e9-9a32-98bdba26c0a1 | -8.25474 | -61.46214 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9687b66-cdec-3af4-9294-2b8ca6a9acc3 | -9.16934 | -59.51539 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2db2e654-e45d-35e8-b4ef-022e9eefe50a | -8.90129 | -60.54789 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 709e4df4-d31d-3b9e-9752-094830ee669b | -10.41183 | -57.70606 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1086492f-9359-336b-b8ef-e7f9397d3d29 | -9.17541 | -59.51991 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 869323a3-60e2-39a7-a4da-9dfd00518f10 | -9.27157 | -56.91135 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35e1a862-99f7-3a09-bddc-b1fa4f832c76 | -9.44822 | -65.42597 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce3771f4-26a8-3269-8130-fb8ab02ec178 | -8.94458 | -65.9529 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 8a0569ee-3936-319c-af57-05dcc3006cde | -8.90572 | -60.77717 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6be681be-9b87-35cb-8ecd-ff6cf951c966 | -9.40968 | -60.54 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f744a457-5d64-365e-a4e9-8867f2ce30bc | -8.63979 | -62.62152 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b97353e-3c99-31e8-b0c3-16b1d5dfe64c | -7.42408 | -60.61617 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f71b684-b504-3b8c-9cfe-19d893b4036e | -8.94893 | -65.95364 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 53bd30fb-6567-3fd1-895f-a12dd14f1cea | -6.76693 | -59.6727 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7bdd30b1-94af-3eef-91b1-8c896268e66a | -9.16284 | -59.55708 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c55356d-d92a-377c-94f0-9f56b8463f46 | -7.71289 | -61.12174 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fb0fdc9-8aa8-39a0-bca8-964cde37784f | -7.47164 | -61.33022 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e148863c-93e0-3e02-b447-59eab4972034 | -11.13523 | -46.33676 | 2025-08-27 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f2afa4f4-ed92-3aba-8edf-2a888ee8e407 | -7.75048 | -61.0828 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40b5aec3-2041-3f75-bfd3-96d8b04a4493 | -9.17595 | -59.51643 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84d03f77-813b-3dfa-bb89-e74741a4fd05 | -9.15791 | -59.56699 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70dee655-52a6-30f5-9ee4-2e40003cc0ce | -7.54268 | -63.85814 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ac09c54-1f3b-36ca-ad82-587f2f6bdfac | -9.49756 | -60.52169 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4831cd40-974d-3c34-b72b-adc4a4e97d14 | -11.30981 | -55.10859 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f369c23b-aa0e-3f91-9527-ccc40b11b10f | -9.40803 | -60.52893 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README57.md)
