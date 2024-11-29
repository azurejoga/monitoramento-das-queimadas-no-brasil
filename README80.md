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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b1d6dfa-f649-37dd-921e-e0ae6487a16c | -0.92302 | -51.63153 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 195f908c-9bf9-3458-add1-a48da92eec71 | -3.16696 | -51.09475 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf759425-a914-3f4a-9dc6-cb92e3610716 | -4.1781 | -53.72654 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 834bb51c-9ae5-377d-b329-b43017732385 | -4.17955 | -48.61375 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21150f67-ce93-3989-adf2-d850fd3f3a31 | -1.09426 | -53.39059 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 584cdc04-410b-3a53-9ab0-2f08ca5fbc81 | -1.06487 | -53.2106 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66f83f4d-9cab-3d91-8e72-503c31518564 | -4.64383 | -42.40223 | 2024-11-29 04:57:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 45ba0f6b-f113-3a40-adcd-bda84f1d26f0 | -3.10463 | -53.25858 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f3cc889-33a5-3450-a8c1-df5617184147 | -3.24204 | -53.92806 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1270e672-0c3a-3859-b7f0-e5c12b47f8e8 | -2.72414 | -51.7398 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec2c53b9-c926-3a02-a88e-12185d41c1c8 | -2.97234 | -53.73784 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c213a68f-07e7-310b-a9cf-ffd10f00cdf9 | -3.5851 | -51.31976 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35ae286b-755c-311c-b9ba-5dfa3e625a12 | -4.04336 | -48.3311 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cf8d95f-f3fc-3235-af1b-e9780679639e | -4.03039 | -48.8898 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3fde9db-c8bd-3d39-b225-34980c7af2cb | -1.21773 | -54.19085 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71197a60-72a5-32e0-a509-dff67e923c2d | -2.86936 | -45.53941 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48db9f84-d6fa-3f5c-a376-138536bb577d | -2.7557 | -54.12341 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fd59f9f-1b04-3783-a75f-83a4f382e468 | -2.44065 | -53.9604 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a91f55b-75a5-3ce1-829c-ac79b2104a2c | -3.28688 | -50.62333 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43390317-03e3-33f5-9fa8-694b86cf285e | -3.22212 | -53.61884 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bd7e287-ad16-3d4e-8972-427bf24953e1 | -2.25642 | -53.46412 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 864e085e-3906-37f9-af8d-b764c943192e | -3.11411 | -53.98552 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f1fb817-cc19-3932-a2ec-f95098536550 | -2.92579 | -48.58712 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e76c5bc-bf05-358f-b9a2-87f864fedf69 | -5.30159 | -49.97428 | 2024-11-29 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47284cee-9d4f-37b4-a615-f57ccec17b1a | -2.83767 | -48.09048 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42cfbc2e-d3b1-3069-8983-cb6c6c60afe0 | -3.08879 | -53.29496 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e81b1ae-f261-3e8f-9eea-d5b4b5b0939e | -3.07664 | -53.28602 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77d7f2c0-cf5e-3c7e-b063-bb38b39b26ce | -2.6916 | -54.14105 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eeb0f92e-7432-30d1-a35e-51f88b70c7e8 | -3.52853 | -50.19702 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3f035ae8-671c-3262-888c-87d819eb6bc1 | -2.61729 | -53.98479 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c263fd1b-040d-32b5-b683-74226d515eee | -2.76112 | -54.08892 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3db25af5-f234-3bef-9f8f-784ec4726be0 | -3.06655 | -53.9178 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 569abb33-e82b-30cb-be20-f8b1e725c19f | -2.82814 | -54.02871 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ebde097-dbc7-35e8-aee3-2017e97b6d99 | -3.0403 | -50.97576 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31172dec-d08d-30ef-9036-e48a8c7e988b | -2.80981 | -54.14589 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c9c8bb4-6c96-3bb8-baad-2563c0ad9dea | -1.17958 | -53.41085 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4a9b42d-57b0-3c43-8030-619d935b0f8c | -3.1622 | -53.23928 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ad84e8c-8b8e-36d5-ac76-c0bdfa887037 | -2.41273 | -54.00903 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02db8f4f-2cff-3075-a204-ff69872edfcd | -3.24617 | -50.76796 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0166483-6da6-38eb-898f-1398cc041f1d | 0.0383 | -51.11264 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 369136fc-57ea-34b7-b8cd-79f2aa8e17de | -3.36611 | -50.40327 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b334166-9e5d-3324-8d8f-e8760ffc9285 | -3.96274 | -48.08902 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 60c9f3e4-6a62-3a8b-9d0f-80cd50567a08 | 1.45662 | -55.9062 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 951d6636-3d31-35e5-9751-24bb050b1858 | -2.87319 | -54.00042 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f9e8bfc-14f8-3c09-b8c4-d363cb18af05 | -2.59818 | -51.82973 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a01a0aa2-cf65-3200-8df2-f8bb4014f3db | -1.27208 | -53.29939 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1533b933-872f-38a2-abf1-cdbdf576382d | -3.91578 | -50.10329 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbc9d688-7ee4-3944-8da6-1ff2aa9682e2 | -2.26526 | -53.47251 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85f2191d-d6d0-308c-aaca-358aa957c4f0 | -1.94855 | -52.97208 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8d35d7b-330a-31fa-b818-ecadf9608f58 | -1.79017 | -52.74614 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dfa5163-47e9-331b-9f95-53089e3d938e | -3.96945 | -48.98457 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3999f0c0-a9b3-3424-9179-cd9238880ced | -1.1995 | -53.87211 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 54cd51e8-abaa-3536-bec5-ee321cb94862 | -3.37452 | -50.12184 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c5de1a1-5d7c-3e9c-af3d-1ac05372edc1 | -2.86873 | -53.98563 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 674e12af-decc-389e-8b74-658a43fd4c8a | -1.14065 | -53.70358 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 034bf886-7b00-3f4e-bd00-1b8d0ef24eb9 | -2.89196 | -54.01392 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4484e12e-6850-3b0e-b860-222156135218 | -2.98196 | -51.33694 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63fa11cc-f54b-3592-961c-c0fc2d8d0e6b | -1.42789 | -54.30265 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d192393-fdd2-3fa1-9630-57a12f59d117 | -2.16663 | -53.27736 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a0dec26-06cb-35b0-8113-8cac76114adc | -3.11472 | -54.00323 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7e9c177-4052-3af5-8103-d9f2d533fabc | -1.39238 | -54.94492 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6914af8-b80e-3481-98db-9064b8621cd6 | -3.08495 | -53.29789 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11b11165-81ff-349c-913f-27bbe7f0dc8f | -1.13976 | -48.3486 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb577d85-4e96-3f3f-b0fa-09ba6735071e | -3.7317 | -51.09588 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aba7af0d-97d9-3ffc-bd57-1263b5b04c2b | -3.05625 | -48.52363 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fbdfcf4-df1d-3792-9604-668f68f3da5d | -2.46819 | -53.6972 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42e1d85c-6d54-3110-bffa-6a175e56ca34 | -5.75952 | -46.26624 | 2024-11-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d93b39de-2f1c-3938-b230-3ba92605a2c8 | -2.79849 | -48.68336 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56c94a1e-3b73-3fbe-a9e6-35b87e137dc5 | -2.84769 | -54.09874 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18e65056-7ab6-3ef1-9fa6-3cf6370d2e6f | -2.05987 | -56.08032 | 2024-11-29 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a6a535ba-53b4-3e17-b4dc-31ea36b46c59 | -4.15524 | -54.80828 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5da3e423-51a9-384f-8876-48dc2de72bbc | -2.83784 | -54.1184 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66b474fe-efaa-33a5-82a0-f911d9cdd928 | -4.06333 | -46.6858 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a21bb03-1db1-3f12-a451-28f7a4bad01c | -2.84538 | -54.07014 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f25fb41-a1e5-338f-9b88-4352c6c52ac4 | -2.2384 | -53.62294 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46056e48-92d4-320f-9af7-a643d06308a5 | -1.50942 | -52.56049 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 650c3fb7-90c7-347c-aa32-59171d18d58c | -2.01847 | -51.19477 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ae07b562-ea10-3fcf-a486-578625929205 | -1.53583 | -51.62072 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ceaf2f32-fee5-3b5f-a925-03ca78048b82 | -2.89289 | -53.96476 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cb4393b-6389-3fa8-bfe6-b01d52ec0f42 | 1.23241 | -55.93334 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 161ad919-0097-316a-86d5-f8e03c89b131 | -1.2421 | -53.36147 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2a0b5eb-db33-3d53-bcd1-17807f8a0928 | -1.40561 | -53.40083 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b5b93e3-80cd-39c3-ad82-7b518e4bf551 | -2.75535 | -54.08018 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2476c299-d1b1-32ad-ab5c-8c376c22a98b | -2.26026 | -53.4612 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 746c0e2c-d2f0-3bce-bb9d-c7e141ca14cf | -1.20324 | -53.67516 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bb57b73-6788-3082-933a-b26e08bea9ba | -1.09095 | -53.39008 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 808f8313-1c99-33d5-8e3a-6f6129fb31e7 | -3.61162 | -50.18977 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c5f8c144-2e21-3909-a80d-93b6dee2aee9 | -4.51532 | -48.06836 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad694786-6a7a-3862-8a30-fe6419c51a8f | -2.52564 | -47.07341 | 2024-11-29 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd12421f-df71-335d-a827-b83f8cbe8f11 | -3.87404 | -47.07794 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bef61789-e89f-3670-9879-48a211986236 | -2.69559 | -51.99303 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 51f7735b-26d7-3266-9cae-137fe16e7e61 | -1.09363 | -53.37295 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eda2fb9b-1e2d-3da2-a65b-5cd9d1bbaf03 | -2.88697 | -54.00258 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18d9c1ea-0828-3347-b467-ccbc79360e6e | -3.3386 | -53.22115 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9c5d082-0fd4-34c1-bd3f-3e9af5655f35 | -1.63262 | -53.88688 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e8f957a-dd14-3393-a0c0-598d3d879299 | -3.28994 | -53.66463 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7cc29440-4dc4-3c9d-bbd8-97bba90156d5 | -1.56448 | -52.11705 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce8ef4e6-7bd1-3089-befb-74f372125b18 | -3.16615 | -46.56377 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00593eb2-6f5a-396a-88dc-6988d85afbf0 | -1.11377 | -53.59396 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a05feae4-78ce-32b7-a8b0-5d1cad4c916d | -2.60327 | -54.07441 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README81.md)
