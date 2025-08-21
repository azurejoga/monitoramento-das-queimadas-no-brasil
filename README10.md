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
| a4587eec-3326-3741-a0a7-0c4245d1e6d3 | -6.01608 | -42.82396 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3f1cb9f6-0597-31c3-87d9-617bf0bd6403 | -4.28677 | -48.27658 | 2025-08-21 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fbb9c94-7903-3df4-a34d-7d69c3838a24 | -2.25908 | -47.85043 | 2025-08-21 03:47:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d95b85e-2e29-31cf-9a22-b98315bb814b | -3.04428 | -49.42045 | 2025-08-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3694a337-b8a6-3d44-b65a-23433739ca91 | -6.19968 | -43.57029 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 50b02f43-b768-37c7-bcc2-fb220910722e | -2.55148 | -47.70851 | 2025-08-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c725e615-b8f3-34b1-afd9-7afcce75b3ae | -2.44522 | -47.32578 | 2025-08-21 03:47:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f8c36e34-9ea8-3359-91c6-08ce24b97b44 | -2.38433 | -47.65931 | 2025-08-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 61217d22-cfde-3789-a41a-2421cc0d8508 | -6.82029 | -39.89356 | 2025-08-21 03:47:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b1e2f8ff-2727-36ba-8e8f-d5bf74dd0d27 | -6.03027 | -44.36583 | 2025-08-21 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a915700-bf6b-38df-8b2f-5106179243e0 | -5.75713 | -45.30157 | 2025-08-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| babc1c22-d79c-3c31-9294-fdd38c919c8b | -5.79028 | -45.07841 | 2025-08-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8759ab3a-f77f-39dd-b0c7-d783cfad0d43 | -6.20046 | -43.56581 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5163800c-c222-384a-a3d6-9c0c5cf8689d | -4.87855 | -37.48361 | 2025-08-21 03:47:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ceafd87c-9fb5-31e9-a5b2-92b7101d1c81 | -5.12687 | -43.21308 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01c77043-2bb3-3da5-973b-3c94480bb6b7 | -2.90814 | -48.25297 | 2025-08-21 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3ef7942-a6b8-3e67-8dc9-cc17f9e72cd1 | -6.00225 | -42.81044 | 2025-08-21 03:47:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4f8284e3-a089-3ca0-822a-839c5f731c76 | -6.16538 | -42.71412 | 2025-08-21 03:47:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e27f3d4b-b5ec-37f1-b58e-11ac570d92ed | -4.71306 | -47.21716 | 2025-08-21 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 02281c10-b94f-30b0-bc4d-a50da9759b72 | -2.69441 | -48.2098 | 2025-08-21 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a84fb7c-3ca4-3f47-8d12-e8027d670ff3 | -4.86238 | -42.53888 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 11f78ed8-cef8-3e49-92f7-d4fb96f9c323 | -5.66556 | -43.51036 | 2025-08-21 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c20d595d-bfa0-38d4-92d3-e410d24ca4f8 | -2.44529 | -47.3257 | 2025-08-21 03:47:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ffbb76e-3cf5-3234-ab69-9b214d70f96b | -4.65018 | -41.40342 | 2025-08-21 03:47:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 61d79295-cdd7-3677-9ebd-d38311cbd8ab | -5.48404 | -42.1683 | 2025-08-21 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c3831540-d375-387d-907e-731f9f838399 | -6.2023 | -43.56811 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1641c6b-44a4-3637-80d2-b352b30c19c0 | -5.75074 | -42.75333 | 2025-08-21 03:47:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1013cdcb-51a0-39b4-ab3e-ce6526eaaaf6 | -5.9924 | -42.81683 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 622e06c2-2ed7-3a0d-9f73-c2d6f86dbc4b | -2.54356 | -47.71737 | 2025-08-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a6855586-eb15-3c6d-91a6-470fea971691 | -6.00836 | -42.85371 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| be040215-fd95-3a25-a78f-f67914ad3567 | -5.78172 | -45.0682 | 2025-08-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c579f692-f5c6-3635-8c56-7deee8c15a46 | -3.81668 | -41.56949 | 2025-08-21 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 45993e30-9ade-3e6b-bf7c-82fb8a6a5cb6 | -6.00589 | -42.81503 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 42c5b263-98f6-36dc-a46d-cca0809f37ae | -5.66725 | -43.50997 | 2025-08-21 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0a72d50-c91e-3026-9780-05f6226b1996 | -6.26663 | -43.72149 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 743848d3-fef9-3808-bda8-f54fbb649731 | -3.86953 | -40.45709 | 2025-08-21 03:47:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f656db6-f49c-3d38-a857-d4a1099a0c99 | -5.68115 | -43.86857 | 2025-08-21 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44f3d5a4-a92b-30a0-8803-fc9fc525aac3 | -5.78675 | -45.06893 | 2025-08-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3a78020-0e7f-3e7b-b73b-99046443e0d6 | -3.24119 | -39.53035 | 2025-08-21 03:47:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6ef3c826-5312-3ba6-bf5c-1ed2d1aa64b5 | -6.81963 | -39.89774 | 2025-08-21 03:47:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7924d45b-521b-3ad0-b454-f9e1b895d1cf | -5.48467 | -42.16457 | 2025-08-21 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f7c4b7b-e982-3747-9c11-efdcf591b11e | -6.21381 | -43.33438 | 2025-08-21 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f7635d0-2bae-3d6f-bee1-42c844e73688 | -6.01384 | -42.82018 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 30cad54b-8cdb-38a7-88c1-afad50b95fc3 | -4.91125 | -45.31841 | 2025-08-21 03:47:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f9df2fc-5c4d-3c80-b450-183162838f22 | -5.9912 | -42.85081 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2992232e-7108-3036-a1bc-4e5ebe5394db | -3.24186 | -39.52613 | 2025-08-21 03:47:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0de8c3c5-15cb-342e-bfa5-9814765c68f2 | -5.96148 | -44.13354 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3694804b-81e9-3e20-82d7-e719c5d3d3e1 | -6.01105 | -42.85334 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 063d7954-c24b-3695-b12b-083adadaa485 | -5.87821 | -42.40816 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 76202aaf-952c-3820-9498-6e26db7d2ca3 | -6.19888 | -43.57486 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09e8cf40-d417-3114-8cd7-71a5c1ceb2e3 | -6.06847 | -44.11263 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 737e4dd1-7b81-332d-a2d7-58fa71d616b8 | -5.96442 | -44.14461 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| faa6e46c-4457-3294-a0a8-0fbb7768f0b8 | -2.70087 | -48.21082 | 2025-08-21 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aaa5e38-1a69-3939-ac14-4726b780675c | -4.86899 | -42.54422 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 235c3394-63f5-3ab9-8078-c8c49f25b440 | -5.40602 | -42.37081 | 2025-08-21 03:47:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c835f934-9de3-3098-ac22-c8c795fd53ae | -5.67008 | -43.51103 | 2025-08-21 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8c5cdc1-9a8a-3033-bbc3-b5b0135ce8b0 | -5.4781 | -44.6992 | 2025-08-21 03:47:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bc980f9-640b-31be-9a00-68bd0b20fe53 | -4.63755 | -42.53414 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2f44bc10-2a47-39f4-b77a-7ffb51d3131f | -3.9813 | -43.24388 | 2025-08-21 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60963046-8e18-3d76-8617-ed9a2f1b3fb6 | -4.71444 | -47.21679 | 2025-08-21 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 91e7b6be-e2e1-3523-91f5-ece901b8c1eb | -5.37995 | -42.34616 | 2025-08-21 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 85f4b43e-a29a-3ae1-85a1-e0cc05734b64 | -5.87338 | -42.41132 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e9ec2163-9364-3e3b-a374-be44ee87f534 | -5.74218 | -42.75198 | 2025-08-21 03:47:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7f3af22b-8ee4-3128-9890-a6978bc04726 | -2.44442 | -47.33046 | 2025-08-21 03:47:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e23b28a4-fb12-3c43-ae44-7f627b602299 | -4.86172 | -42.54295 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4e893c29-70e9-3d47-a8ab-d50826bd4f75 | -4.17231 | -42.03138 | 2025-08-21 03:47:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a7c5889b-c57b-368d-9b7c-2ebc153e65bb | -4.31356 | -48.08441 | 2025-08-21 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2eec1cfc-6ff7-372a-9c13-6fa116f067f9 | -6.21454 | -43.33001 | 2025-08-21 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8cd7d77-6f65-39a9-9450-12d496a4cd18 | -5.64476 | -43.72136 | 2025-08-21 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 213f055b-9026-3275-b6e7-331e26f49fb2 | -2.38978 | -47.66536 | 2025-08-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 641c0e8c-8af9-3e19-ae50-f57637aef9fc | -3.36401 | -43.36283 | 2025-08-21 03:47:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8dabc94-6d51-3ced-8dba-3e8e6702c957 | -6.08449 | -44.42464 | 2025-08-21 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0621367-5e54-300c-ab1a-133e37a87f41 | -5.7993 | -42.30851 | 2025-08-21 03:47:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2a7090a3-b1c1-34be-a89a-c237cca247e9 | -6.00678 | -42.85249 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 58e6b2ec-933d-3047-860a-45d8441a6327 | -3.04353 | -49.42347 | 2025-08-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36b0af76-2fec-35ba-8888-2a420d46de78 | -5.04477 | -43.05585 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8134b311-21de-3277-9313-af220b0dfbf3 | -2.38194 | -47.65855 | 2025-08-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3831884-0a89-3eda-9c78-de86b6e719ed | -6.19777 | -43.56757 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c83a659c-53c6-36e2-ae6d-e9831f689879 | -5.98875 | -42.81231 | 2025-08-21 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5d60cdf7-819f-3d63-8e67-b0491ba5b59a | -3.04316 | -49.42679 | 2025-08-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e0480bb-acf5-3014-9307-bfb4bb276a52 | -2.25504 | -47.85141 | 2025-08-21 03:47:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec50cf8d-4248-3040-831c-b42d26b5c578 | -5.25583 | -40.71911 | 2025-08-21 03:47:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 3f098cc0-04eb-3a78-8bac-0de6e8ef5e6d | -2.91916 | -48.30402 | 2025-08-21 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 99428f47-55d7-3c4c-9556-45e16d7c8d28 | -4.9159 | -45.3224 | 2025-08-21 03:47:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dfe0187-e766-3487-b612-c71982face62 | -6.1934 | -35.792 | 2025-08-21 03:47:00 | NOAA-21 | TANGARÁ | RIO GRANDE DO NORTE | Brasil | 2414001 | 24 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 317e4c33-140b-36c4-aa8c-c113c2e9fb71 | -4.01641 | -49.50848 | 2025-08-21 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e60a54a1-6b50-3613-ae38-62cc1998365c | -4.8654 | -42.53945 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dfb05bf6-a5f4-3d9b-9451-13c3415bffde | -5.78122 | -45.07111 | 2025-08-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8208b48d-8fbd-323a-bff3-699a6f218c86 | -5.78609 | -43.61255 | 2025-08-21 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3be896db-c3a1-3e89-8e60-32985522e3ba | -2.38736 | -47.66451 | 2025-08-21 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8fb034db-f17d-3b32-a055-533a3e2a9566 | -3.99252 | -42.51307 | 2025-08-21 03:47:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 083df206-8099-32fd-a78d-643812c5247f | -4.63325 | -42.53345 | 2025-08-21 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| caf3805f-d0e6-3f1b-9bb6-8a3090cacbab | -4.6491 | -41.41001 | 2025-08-21 03:47:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 85cfaca0-9514-355c-bc80-e84f735deab0 | -6.07348 | -44.13978 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea71bb7e-444f-3299-b382-827ba827eca2 | -4.64623 | -41.40259 | 2025-08-21 03:47:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bff2ff53-4393-3f13-b9af-c170e93b56de | -3.04246 | -49.42985 | 2025-08-21 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f59bd8b8-78d7-3f4b-bb48-0efcdb06e9e2 | -5.97083 | -44.13522 | 2025-08-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd27fe29-3d1b-3c2b-82ad-631c919d201b | -5.16656 | -37.98131 | 2025-08-21 03:47:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9e64ffcf-610d-3869-b91b-c8f4eec9935d | -5.44084 | -45.10286 | 2025-08-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43f4963b-7dcc-3871-9779-3828c583fc7b | -4.6457 | -41.40584 | 2025-08-21 03:47:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README11.md)
