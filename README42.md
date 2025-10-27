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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28131b97-d132-3b86-8694-604966734ffa | -7.80856 | -45.38873 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59b0aa67-ce06-38c4-9b8e-85c0d6eb2bb5 | -4.86581 | -48.72303 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb547210-20e4-3362-83eb-4f84f8461603 | -7.76278 | -46.51632 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68da0df7-ed8f-39e7-9579-6a859ce43b8a | -7.84861 | -46.41825 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5b844158-ead1-3600-baeb-e54da9300554 | -8.65298 | -47.24603 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b61299c9-3445-36c6-9c7a-5cc1636fd6b0 | -7.1982 | -46.73845 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7fa20119-289a-3fc6-af2e-4f7ae75c7afc | -6.16301 | -41.57283 | 2025-10-27 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 51921b27-896b-35af-a9cd-ecae0078847b | -7.79158 | -45.38205 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71b05c91-86ac-3857-a834-1656c694af4a | -7.91662 | -45.6879 | 2025-10-27 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 175d7576-a4ae-33a2-a0a7-c25f421a6709 | -4.20903 | -48.3578 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 858ebac5-50a8-3f11-a4a3-6aa66f035d9c | -6.642 | -44.62807 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 330ecd81-a6d2-3c53-8f1a-a323ecb6aa37 | -7.94046 | -44.83932 | 2025-10-27 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 235bf227-f48c-3972-86f1-7c17c740240b | -7.38076 | -46.5428 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cef028b-7e34-3374-b2dc-e75a4c1218db | -6.99725 | -39.10318 | 2025-10-27 04:32:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dbae9c28-eb3f-3139-b841-27949c15315b | -6.9012 | -46.14444 | 2025-10-27 04:32:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8da1d919-af4b-3b17-9a6d-a1539db46f50 | -4.31412 | -48.23093 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f4243ab-9808-3de6-8c62-b1382e7e7341 | -3.52243 | -52.20274 | 2025-10-27 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f30861e1-2ab8-311e-ba29-67ecc517d985 | -9.58386 | -46.91228 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc2f4cd2-4bd6-30e1-a773-7f5b47437835 | -4.95251 | -44.87239 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb30f5e3-3a44-3800-8892-afd49fe6aafb | -7.2391 | -44.98804 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27b9caa4-36f1-338f-876e-a0b3d29f7d98 | -7.683 | -42.18441 | 2025-10-27 04:32:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aa3163b9-0102-30a0-95aa-5125ef5b8ed2 | -6.49076 | -44.44377 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b16f309-d14c-3fb5-9931-d76a94dd9a8f | -4.10195 | -48.02241 | 2025-10-27 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 29aba3d3-662d-3b42-b208-cd5001f746bc | -5.12016 | -41.18996 | 2025-10-27 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 78edc9f6-25f6-37bd-9c1d-30f77cf85152 | -4.44986 | -43.41915 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 297bad9b-9060-3384-a1b9-4ad73045f897 | -5.12298 | -47.74152 | 2025-10-27 04:32:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21036f76-6364-3d0e-bbda-001324bcdaea | -9.13138 | -45.86363 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eba3e30e-76ec-3e8c-b0b5-0b4fdfd67e0c | -4.02729 | -44.40848 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0327ba49-bc7d-33ae-a328-85ed73c507c4 | -8.27013 | -46.88121 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd6575c9-d86e-3dd1-a51e-5a5766909720 | -7.85377 | -46.45244 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe7c9823-2299-36f7-8cb1-87a9937de1ea | -4.48801 | -43.42042 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d113a5f2-d280-313e-89a0-e0620701be5d | -9.22219 | -50.76042 | 2025-10-27 04:32:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53fc93df-0d40-3f95-a4ce-afaf639bd110 | -4.44919 | -43.42366 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0935dbc-c2f2-3a47-8967-1d84426a509c | -5.63936 | -47.63619 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| adf260d7-ab7f-385e-b685-f025a7926592 | -9.18671 | -44.57446 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eab8b548-7ace-3a88-83fc-d87125fde6cf | -6.0835 | -42.15445 | 2025-10-27 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b79e4444-7935-32b8-a3b1-8dffa7e5779d | -8.65019 | -47.24199 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eeea3246-d52e-3677-bc97-3ed77cd5598e | -4.54919 | -46.55727 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c93b8e38-00d2-3f4a-8800-7b8af47f0a08 | -6.16544 | -44.21532 | 2025-10-27 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8434adc-9f36-37e8-9772-bbdc431ed1d0 | -4.47596 | -45.32349 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7f53aea-3704-33ff-a10e-4950b3873d7b | -7.84196 | -46.46186 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e45afbe-e194-3e29-9b1b-2533ef67a9dc | -4.45842 | -45.46416 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9734d43d-d848-3c20-b352-b0400a608742 | -3.71874 | -47.64643 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36a04b7a-86d4-33f8-aedf-48efea8b9336 | -7.3052 | -42.47609 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ae53bf78-4ead-37f0-affb-71109b619801 | -9.97796 | -45.67022 | 2025-10-27 04:32:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48048fc5-37d9-3e38-bf3b-6b9cb8f2b009 | -7.88027 | -47.25203 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1953eb61-509d-3f5f-9d52-63ee935db08b | -7.53457 | -46.26945 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dc1f749-d3a2-3d82-9650-75e9324ec67e | -6.37165 | -44.26274 | 2025-10-27 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb7675ab-c00f-3003-aa7d-e726ab4b129d | -4.20181 | -48.36029 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11a3fb42-2873-30bd-8bb3-9f659e7c5383 | -7.13283 | -47.02795 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d5d4ddf-9215-36fb-8913-891f6a1ffc3d | -6.87442 | -45.17048 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78bf68c6-7c52-37bd-9038-cb146164ddd7 | -3.55505 | -49.90783 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d4b31a1-e0ca-3dc2-b32f-2a40b6919c9e | -5.25075 | -44.86759 | 2025-10-27 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1147987e-d0db-3f10-a989-21779178e54a | -3.23451 | -48.75114 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4299c649-da2b-390e-9a5b-92440682125c | -9.18365 | -44.56932 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5a04392-8788-3bac-a353-23c3d874ec8e | -4.72787 | -46.80844 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f254328a-20f6-37ed-b2bc-8c662a274ba7 | -3.14782 | -50.33088 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f47cf43d-c27e-3900-8140-cddf00d61b35 | -4.45669 | -43.42478 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c380af-16da-3b0d-bc43-72a324231d0c | -7.97077 | -45.46797 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 30fd456f-e750-342d-9ffe-d0585c4038ea | -9.31775 | -46.25735 | 2025-10-27 04:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 824f1f9e-fcc6-3f51-8f5d-69577c6e0dc5 | -6.09853 | -41.77932 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cad0e204-ff43-398f-8ef8-b81dce96285c | -3.26808 | -50.04706 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 506c58c0-252f-3207-bf56-78c3b498e658 | -9.42767 | -46.20308 | 2025-10-27 04:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5a552d9-6612-3ef3-b07d-910fc5f534e8 | -6.43831 | -42.03293 | 2025-10-27 04:32:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 058bde00-91f9-389f-b105-e483b85abdd5 | -4.87432 | -48.64785 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0206df9-8825-30b0-bd19-8e88ea11653f | -8.14623 | -43.41081 | 2025-10-27 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5afac5dc-3e72-3a52-9bc6-ca07fac127b9 | -3.04453 | -53.01957 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc7335f7-ef16-3861-8b2b-138fd3f4acc9 | -8.28482 | -45.68971 | 2025-10-27 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e4044ce9-9e9e-361a-baab-c65123d142f9 | -3.09706 | -54.62107 | 2025-10-27 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38e9260e-8afb-3108-88ef-b84f04e3b49e | -6.59596 | -42.66407 | 2025-10-27 04:32:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f0fc56ed-d2b5-391d-bdb0-437210375d39 | -9.456 | -47.72894 | 2025-10-27 04:32:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 193df98b-6be1-3e81-bb44-5e3a5123ca1c | -5.72093 | -49.31242 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 232e415d-84e0-3326-92ba-20afcba1f058 | -5.63438 | -47.62485 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a27e2bf-0574-3ed8-8fb0-8b02858a502a | -3.12634 | -49.1006 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78f3c3e8-725c-3977-91d0-36eb47ff4729 | -8.3269 | -46.824 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93e77181-3c50-34f9-8933-cb0271161e7b | -7.8368 | -46.42758 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e6ee4d5-a5ff-37a5-85a4-591e98813600 | -7.22524 | -46.86939 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f996a697-438c-3d04-918b-d90f64907f45 | -4.44787 | -45.45926 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5479c59-3d39-3a98-85b4-a275af8e7408 | -6.13917 | -41.82949 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 19363a52-8ca8-354b-a451-a3e2ccbc14a4 | -3.10527 | -50.17851 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ddd63625-dacc-3bff-adf1-6582f3f90bf8 | -3.72107 | -49.45092 | 2025-10-27 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 133d0686-ee8e-34cc-8c01-0f3ba70eb719 | -9.62822 | -40.34824 | 2025-10-27 04:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e23a65a5-b026-383c-a72c-5f658d8f3b42 | -7.6017 | -45.68523 | 2025-10-27 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a13d7dd0-83de-3e45-a462-a8b9090b2de4 | -9.46317 | -47.72647 | 2025-10-27 04:32:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc135a23-4710-3953-bab0-25a6a4187190 | -4.47303 | -43.41804 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea234887-5751-32b7-9823-5a35394be38a | -4.83229 | -45.33449 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dee2f17-95e8-3835-bce9-c5fb3ed47b30 | -4.44488 | -45.97989 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dba6d423-a3bf-366c-9edd-bb9f3ef047c6 | -8.32441 | -46.17192 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 941c6dcb-db26-3635-bfe7-73961d45de8d | -6.01662 | -48.12034 | 2025-10-27 04:32:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce7053a8-e561-3dc5-ac93-73ace4418cf0 | -9.34727 | -49.24767 | 2025-10-27 04:32:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 046e3ecf-02e8-3596-9085-7cfeea062830 | -5.82364 | -40.8297 | 2025-10-27 04:32:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b34e328b-66b7-3a73-b5d8-8bf507fbdda4 | -8.74178 | -47.02326 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04955e82-e93f-3ff5-9675-9335b4fbe283 | -4.37695 | -48.69677 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90e55e9a-07e9-3c4e-8614-1e4148f71353 | -4.48733 | -43.42495 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3de09f38-b275-3415-a13b-e15b1f9c6179 | -2.25376 | -51.8858 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0cf9a30-6214-3669-9dd0-e828d16f7d80 | -6.96736 | -46.51312 | 2025-10-27 04:32:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7822afd-6d02-372c-9e6d-ad4f6a6398da | -3.33998 | -42.88494 | 2025-10-27 04:32:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e321380f-4be9-3fc3-9450-7890487f0bb6 | -9.02721 | -47.46699 | 2025-10-27 04:32:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d43db22-8918-35a3-a9c6-7100a349b753 | -7.02714 | -48.20689 | 2025-10-27 04:32:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23547877-b25d-340e-89fb-09f4870e6c26 | -5.65999 | -46.45692 | 2025-10-27 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README43.md)
