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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d20aa2b-67a7-3a23-85f5-c843815e2c0d | -8.59579 | -54.74924 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b14d5dc-fb55-307e-9cd9-bee3f27d2ac3 | -6.76948 | -59.4465 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dccb2aca-2f40-3578-a2df-c0fcb0e75a98 | -6.73993 | -58.57846 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d64dd50-0945-3973-b3a5-16bba623b898 | -6.64385 | -56.34327 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ce32765-8e0d-3950-8883-66018556cadc | -6.78591 | -58.63212 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2d107f9-0def-3360-88d6-efe31c7ff807 | -12.06411 | -56.29199 | 2026-08-22 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80be1d96-cc76-3b7a-ad06-954f2d53bf47 | -6.81368 | -59.65948 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51c3d8bc-9d95-31ae-9315-b68d175dead8 | -14.55343 | -53.00858 | 2026-08-22 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 493b4551-c9e8-3a73-b6b3-c40a11157382 | -6.26552 | -62.5282 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5434623d-1156-36b1-a517-7bfebf6cb5df | -6.00388 | -57.85885 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58190164-f6d5-3641-a8d7-d1e6c2b17107 | -6.75998 | -58.66728 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e95969f3-2379-31e1-a30c-e138e47d1326 | -6.82473 | -59.67548 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 50888045-ed56-3bb0-9006-2010e5a75f55 | -14.39556 | -51.80437 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 269802d6-a993-375d-8a81-70580d6a817d | -6.09235 | -57.7005 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dcf0004-0680-3f9c-aef6-bbc056b0b5b4 | -13.38372 | -54.36549 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2ff4370-01b5-3f6e-9781-7b55cf0386a6 | -6.85496 | -59.46363 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e3603830-f347-3662-8c70-d10b075e5812 | -6.81632 | -59.40782 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7a5ab4d-c6e9-3c4b-9a91-ed46f25ae926 | -6.41293 | -52.7317 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50785c34-da12-3d8d-9887-9fd76bf6cb63 | -5.99936 | -57.79984 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dfef147-79a0-320c-a2c5-e415f150bf6a | -6.08988 | -59.95829 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 251edcde-613f-391c-9aa7-4ba91f7a81ee | -3.15087 | -51.10071 | 2026-08-22 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c14db3ff-2c7e-3282-bfd3-ae8a612fbfdb | -6.79877 | -59.58247 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bec41b41-27df-3dcb-8478-4965df592cc6 | -14.13972 | -48.06272 | 2026-08-22 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 525e50f2-f445-33ac-8406-7e0dbf3fbabb | -6.76826 | -58.65786 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 871f0760-f4d3-3abc-bb1e-fa558f3352bc | -8.57775 | -54.78988 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4f4f0f3-f514-3966-a943-fe97eeab8217 | -4.46936 | -55.39921 | 2026-08-22 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7712a2c3-82bb-3314-82db-375c37c015e0 | -6.11546 | -59.9264 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efe9ddb0-3acb-3751-9ed1-07449eb3028c | -6.93542 | -59.32039 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 090fa4c1-918d-3187-a6de-7ad37c89dcc9 | -6.37748 | -54.94788 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f95fb3c2-962a-3a74-9f92-fca73a645091 | -6.53933 | -58.51518 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d05738f5-c86d-3b06-9eb9-3ef769d01d44 | -6.26535 | -62.52943 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9fd811f-28d4-322b-9fa4-c487a416b4bd | -5.91379 | -61.29485 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa9841c1-4695-388c-9e2d-2485e9169c79 | -13.92205 | -58.25875 | 2026-08-22 05:23:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1610869d-2356-3b88-8dab-ef4d35777347 | -6.76452 | -59.77626 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 236ce5fc-a23c-39a4-9420-fa87ffaf7872 | -6.78987 | -59.4249 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 595b8e4d-6e7a-393f-8e00-22ffb9422083 | -13.83513 | -54.00428 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a28c425-7d29-3f1e-809a-1988e27bcae3 | -8.51642 | -55.32631 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d63f8d43-f353-3075-9ed9-df1f15dac65d | -3.26792 | -49.52539 | 2026-08-22 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a740b375-1aa1-374e-9c91-d36686c0c9b6 | -6.61289 | -58.39058 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bba07d30-8fe7-3d6d-8fde-dcaa503921e0 | -13.9955 | -53.71207 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ade220c3-319b-3dd9-a356-d0b1eb1af4eb | -6.80255 | -59.43047 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 353adb11-bd5d-3a4e-85f2-eaf74ef793d0 | -7.36248 | -55.68656 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2467497c-7c32-322c-90d7-384c69419102 | -6.58093 | -59.00531 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60cceb96-30ef-3dea-87f9-ddc128372f9e | -5.79656 | -57.55186 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fb63315-4fda-3432-84ce-199c5f3495b8 | -6.17492 | -55.44495 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a833ff6-de78-3197-84f4-8258f0f01bba | -6.89667 | -55.38325 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e47e7db5-faa8-3216-8ea8-6a3475dd2f6d | -6.136 | -59.90455 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3ea73dd-b603-31cc-ae45-d993d0fdfc06 | -6.82197 | -59.67148 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 4ef5b7ac-8c1f-3416-96bf-9191794cf0f5 | -13.69571 | -51.95058 | 2026-08-22 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c04dc08-c0c2-3ed7-a9f0-25ec8be52174 | -13.99487 | -53.66952 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e939967d-8268-38d4-aed6-f6b7cd3218b4 | -8.09694 | -50.0378 | 2026-08-22 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02962be6-7f32-3358-afbe-1810535f7a15 | -10.73882 | -58.90669 | 2026-08-22 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 954512bc-7961-3cf0-8f29-980d1fa542fc | -6.85163 | -59.44181 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35a02810-bf9c-3372-8a09-370ebcb7763b | -6.78435 | -59.41693 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 15fee97b-0fc5-3718-bd55-3e915378833b | -8.1608 | -54.9906 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 484af9b3-c9de-362c-9328-4106968aa1ac | -6.27575 | -62.53429 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 341f0968-46a8-309f-b64c-ce0a64fdb1d8 | -6.1719 | -53.50304 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 294a3e03-b454-3189-a5c7-7f40d5a9c137 | -6.21709 | -55.48093 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e01a6564-ec38-3c7d-be68-955da4cc4f79 | -6.81866 | -59.67095 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| e45a83ea-681e-339e-aa0b-144fed8abbaf | -6.7838 | -59.42039 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| be6e54e6-0900-318b-bd7a-575ffa424a04 | -6.80696 | -59.42406 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ccb473d-55f4-34d7-91f1-db33eb34c683 | -14.38537 | -51.79969 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| af1426b7-8213-399a-85eb-6252595fc48e | -6.00495 | -57.80802 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4cd77ed-6026-31bd-8443-39a0bd5aed49 | -7.33894 | -55.70257 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e1e9846-8a6d-3a95-9b53-90cbbc542ade | -6.48676 | -51.59995 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3129d971-7729-38a7-b8c7-5cc2312ad775 | -8.19014 | -54.98134 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e32034b0-037a-3eb9-98ee-6c25342c4d9c | -14.40086 | -51.80505 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b9a8b21-9e06-30a4-aa44-e32015fcde6c | -6.22565 | -55.42369 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bd2b215-f99b-3a55-b0da-69ad42e6870a | -6.87693 | -56.64148 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2bc6f66-f7ce-3ccc-9181-62f1c4b82f78 | -6.12939 | -57.68416 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8eb321a3-b978-3b64-9231-83b9b8ed2750 | -6.82528 | -59.67201 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 4e5b505a-acd4-3c8d-90bc-15dd8eb1a0a0 | -8.63082 | -54.73295 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22392d2e-bc92-37ee-870d-0372e6d60d60 | -8.58236 | -54.78616 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6519904e-5017-32d4-a28b-66a98befe680 | -6.86658 | -59.02573 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d52cb9c-284a-3d02-93b0-21e82c7a69d5 | -6.78043 | -58.66692 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad884027-9d7e-3842-b618-3f6c40470d88 | -6.4332 | -52.71675 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43c71c62-149b-309f-8b4d-d2a3c49c0a64 | -6.26901 | -62.53004 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65e2cb9f-edcc-3397-b9ea-2fea5c00c652 | -6.75611 | -58.67024 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cfd2db34-3e82-3127-a2ac-ec7a0d1d37ff | -8.57279 | -54.67025 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed98e1c4-9b29-3aaf-8f98-456b4d295014 | -3.03587 | -48.41604 | 2026-08-22 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ede62c85-cbdf-37a4-b199-117a5d99a1c2 | -6.7705 | -58.68676 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7219ac3f-d9f5-319d-81db-1474508a0ee2 | -8.80774 | -48.54826 | 2026-08-22 05:23:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4a3b6d86-23fc-3202-ab56-0aa3b9b2513c | -6.75949 | -58.71352 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5932e999-0742-32c5-9fc9-b8c182841938 | -6.84995 | -59.40961 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eba8df2e-5498-3433-8ae2-e48f94655737 | -6.11769 | -59.9124 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d361af27-245a-37a5-840e-44af33c073b2 | -7.20713 | -59.40584 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b815968-bdc8-329e-8ed4-538e0c6c20b6 | -6.81576 | -59.39 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 88601512-bbee-3f76-a0d3-cbd5e672ea4f | -12.76547 | -48.39629 | 2026-08-22 05:23:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5739d280-37a7-3682-bbf8-63af1d122a48 | -7.58556 | -57.69359 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5ee4dd2-acee-3a47-b542-1b68108f7cfd | -6.69637 | -58.9417 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf90b806-af95-3b85-a1a1-79bad126d270 | -6.78411 | -58.6639 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ceaafec-572e-3076-990d-61dce7060330 | -6.76996 | -58.69024 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 951a0ea1-b4f5-3af6-b4cb-248e58e4895e | -7.01794 | -59.55029 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ead127b9-87f4-350e-9c89-4c948632fa82 | -8.52796 | -55.32806 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6d648ba-82a4-312f-b218-40412754332c | -13.69535 | -51.95359 | 2026-08-22 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5285a02d-0a90-3c8e-9898-5b0995f1c95c | -7.59989 | -60.94893 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31037739-98c7-3c45-83a1-0f64f3d4fe62 | -3.42574 | -49.47871 | 2026-08-22 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 284ea774-d9cf-3c0d-8b9f-824e34d7aabd | -6.87644 | -59.4351 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 438aa19f-8c54-3bbb-b682-e68f97bc6a7e | -6.22693 | -55.61581 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 82b4cc69-3440-35ac-9bf0-5027660d97df | -6.76831 | -58.70067 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README62.md)
