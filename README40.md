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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3ef5da7-6ab4-3222-9d92-8055aad6f44e | -4.07835 | -47.95646 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4ed077cf-65d3-37dc-b54d-207588d2267d | -4.0738 | -47.94552 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f81e5f56-cd94-3c82-a887-a2d1463e6a78 | -4.07292 | -47.95055 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 9c4ffd29-aa5d-3235-b4c1-e10740663b2d | -4.06958 | -47.94802 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b4bfb9cd-ec93-3d43-8e0f-3223bd639938 | -2.20648 | -48.84874 | 2024-10-05 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ffd9002a-97f5-336b-8e09-8638aee1d917 | -2.20502 | -48.84829 | 2024-10-05 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8867c395-aa06-3be2-8f0c-9b73679b7042 | -3.30714 | -49.46642 | 2024-10-05 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 5915e0ee-22a1-3c13-98fd-717e8eb5b2dd | -3.2475 | -49.40231 | 2024-10-05 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c502c63-35db-3fe8-ac95-fc6dd0727036 | -3.24687 | -49.40281 | 2024-10-05 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a84e295-f207-3a5b-8c63-aa1abc93b11f | -3.24635 | -49.40901 | 2024-10-05 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 407856a5-e9d1-3d22-90eb-1cc916f0983a | -3.24568 | -49.40948 | 2024-10-05 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7d73d0b-dc78-39db-8473-3ff7dcd79b74 | -4.66103 | -49.52948 | 2024-10-05 03:47:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a020b733-4e8c-3cd7-b694-0100179efcbc | -6.35583 | -35.1813 | 2024-10-05 03:47:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3ccc33a7-acb0-3c93-be51-4d11acde6855 | -5.90452 | -35.43431 | 2024-10-05 03:47:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d84eade1-9d47-3903-a2ce-4dc67a8d2fb7 | -5.54578 | -42.78852 | 2024-10-05 03:47:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4853d409-9814-3858-b8c9-e538794ef3bb | -5.54507 | -42.79279 | 2024-10-05 03:47:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e2fee839-0502-3208-acd4-501223c23435 | -5.82342 | -43.24078 | 2024-10-05 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b22ce43-7137-3872-8243-4b5c7320056f | -5.75131 | -43.15204 | 2024-10-05 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2121ea5b-4cf2-31f8-b128-2c177c09d13c | -5.68711 | -43.15992 | 2024-10-05 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 48ba0ec1-e6d5-38ee-9b10-c69191ca6a03 | -5.64974 | -43.24501 | 2024-10-05 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a350980a-9b82-329b-b7a0-294786fe3bf3 | -5.38245 | -36.81934 | 2024-10-05 03:47:00 | NOAA-21 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dae3d3f7-5e96-371a-9d20-f501387d8ede | -5.46687 | -39.12548 | 2024-10-05 03:47:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2565c3bc-67c4-3b2a-a485-d3068a044ae1 | -5.17708 | -41.29503 | 2024-10-05 03:47:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4c4d92dd-e1ed-3806-b70a-37e41b4c0b6a | -5.17636 | -41.29257 | 2024-10-05 03:47:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 57016b76-c751-32ed-902e-6bae94f63513 | -5.17549 | -41.29776 | 2024-10-05 03:47:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b75c8132-cdf0-3d95-8a8a-592ed4cbdf29 | -5.17311 | -41.29444 | 2024-10-05 03:47:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 178c4338-791d-37a4-8b65-8af91631bcee | -5.53272 | -42.78638 | 2024-10-05 03:47:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d433b916-9964-3fac-a3e1-cebbaba3f506 | -4.86461 | -38.4368 | 2024-10-05 03:47:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d3497a6e-5644-3a2e-99c2-e029940af2f4 | -5.11817 | -37.56522 | 2024-10-05 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c0a8b966-924e-3e8f-afac-ed57464b6aec | -5.11761 | -37.56875 | 2024-10-05 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 359d7d2f-8750-3b78-8d1a-64d9ad3353a1 | -4.89306 | -43.20152 | 2024-10-05 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a306cc18-f68b-3a12-ade4-7f1c56f42de9 | -4.94775 | -43.77452 | 2024-10-05 03:47:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 35fc1d07-1b90-3815-8443-88cc93826d01 | -4.9469 | -43.7796 | 2024-10-05 03:47:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 633bd7d2-ed0e-3334-aea1-dd3eb17d9197 | -4.9422 | -43.77878 | 2024-10-05 03:47:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 2b3fcd6b-fc8d-3f97-926c-d500412d9e5e | -4.85011 | -38.37347 | 2024-10-05 03:47:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e5ef578-d74a-3492-9b3c-c30ffad14112 | -4.46878 | -42.8807 | 2024-10-05 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb186719-e7ac-3397-98b9-f385abbe0d12 | -4.4636 | -42.88437 | 2024-10-05 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 175b99d4-de90-3669-aa8e-6e86d2d3ee53 | -4.73192 | -43.59732 | 2024-10-05 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e35a86c4-8208-33f7-a8cb-b6bfb10be45c | -4.69205 | -43.19043 | 2024-10-05 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 034e7ecd-f099-343a-864c-7b5825969f41 | -4.66408 | -43.76097 | 2024-10-05 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09c55f46-6b8b-31d2-8c81-0b4ea291377b | -4.66099 | -43.759 | 2024-10-05 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8fd36437-3a35-3a83-a2e5-66d40ddc2179 | -4.65935 | -43.76024 | 2024-10-05 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a4c08ec2-62f5-332d-b118-1a8987e034a8 | -4.51916 | -43.8686 | 2024-10-05 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 387f6163-8ecd-3d4a-8959-8729477dfecc | -3.78159 | -38.65956 | 2024-10-05 03:47:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5096ec8b-5522-3e5e-b470-164338a6bcfd | -3.78097 | -38.66345 | 2024-10-05 03:47:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 572bbc09-24a7-3a11-8d4e-e84570fbabf7 | -3.80021 | -41.59791 | 2024-10-05 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fcf66de8-d714-3f2c-9472-f140491819b7 | -3.79789 | -41.58603 | 2024-10-05 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f14f8f44-cf91-3647-bf87-d18b87436757 | -3.76409 | -40.42192 | 2024-10-05 03:47:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49773c7f-75a3-382d-abc4-8195b3f54e58 | -3.76333 | -40.42665 | 2024-10-05 03:47:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3b236c92-f4b6-3332-bbce-af7866cecabc | -3.219 | -42.69906 | 2024-10-05 03:47:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a63dfc16-2bea-35b9-87f3-c28238af3811 | -3.21825 | -42.70355 | 2024-10-05 03:47:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27bb9181-17fe-3375-b219-26acabba9174 | -3.21638 | -42.70073 | 2024-10-05 03:47:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf22195c-94c2-3b4c-9c37-8b465f66cbc0 | -3.47648 | -43.35952 | 2024-10-05 03:47:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5192aafb-b875-3720-b8a3-30c01ebf416b | -3.47179 | -43.35879 | 2024-10-05 03:47:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 247e2d85-c3a7-3655-8539-0333cb95f963 | -5.64525 | -43.24428 | 2024-10-05 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06153bdb-4d83-312b-8444-3af45742bafd | -5.62513 | -43.36227 | 2024-10-05 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1142a385-d964-3bff-a5d6-c7d48f1b7a80 | -5.89183 | -43.87368 | 2024-10-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38ee6952-4621-3161-a13d-78eb3a59b788 | -5.8859 | -43.71328 | 2024-10-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dce8a522-ab1a-3f0f-a93a-31e5116433f4 | -5.88505 | -43.71822 | 2024-10-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd86e86f-9e1c-312c-a5ca-2d5143390c2f | -5.72688 | -43.97772 | 2024-10-05 03:47:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe1fc9d3-5e7d-3122-a539-408dd28d7f0e | -5.5051 | -42.76451 | 2024-10-05 03:47:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c63bb216-2270-3e6f-8f19-1ab08cca21d3 | -5.50037 | -43.65268 | 2024-10-05 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9420dc70-1f57-3ef7-9ef6-e4a23a03a992 | -5.36858 | -43.34781 | 2024-10-05 03:47:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6aa32156-f2c2-3899-85b3-dd2ea0768a03 | -5.36735 | -43.34835 | 2024-10-05 03:47:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b098d498-b5fb-32cb-a30c-f2f5911d950e | -4.94135 | -43.78382 | 2024-10-05 03:47:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 086fe013-3cf9-3933-ad83-9d3d56155a5e | -4.93751 | -43.7779 | 2024-10-05 03:47:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| a52fb02c-5b92-366c-9103-a682d38067d8 | -4.93282 | -43.77701 | 2024-10-05 03:47:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec0c69df-5e8d-3ede-9634-758f98b9fe85 | -4.92813 | -43.77617 | 2024-10-05 03:47:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91e5963b-a3d0-3705-94cb-d7f0a072d908 | -3.79729 | -41.58974 | 2024-10-05 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| df2d57be-adf5-3b96-8a1a-3e1f50fe206a | -3.79669 | -41.59346 | 2024-10-05 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4eb5de59-ad60-3b13-8cdc-1b01d8473ad9 | -4.01736 | -43.25048 | 2024-10-05 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c4f7ccd8-0ebb-3a46-9f18-4c4a18cb6e40 | -4.01276 | -43.24973 | 2024-10-05 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| da39a0dc-42b0-3734-9dd5-fedfa81b8aca | -4.00815 | -43.24899 | 2024-10-05 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 81b18a57-0149-377b-8524-9f76688da4be | -4.00354 | -43.24825 | 2024-10-05 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b51a81f-bf4a-3ed4-a23a-ad246a747cb4 | -3.99893 | -43.24751 | 2024-10-05 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9002c90c-3483-3eeb-a26c-32e9a3efca88 | -3.99812 | -43.25228 | 2024-10-05 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79415287-f877-3aae-8cbf-f5da3dd81ad4 | -3.99731 | -43.25708 | 2024-10-05 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b90437d-3885-3d40-b124-e118ac9ce3a8 | -5.82445 | -44.12594 | 2024-10-05 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| a644012f-c53c-3797-9b44-c2b7d2255b5b | -5.82358 | -44.13103 | 2024-10-05 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 38d8944d-749f-330e-88a9-5e536fec3948 | -5.8227 | -44.13613 | 2024-10-05 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| da8d7334-55c1-3e33-a4fd-1e9c969972f3 | -5.8197 | -44.12517 | 2024-10-05 03:47:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| cd84b712-1874-3a8f-9fb1-af5d72c0785e | -5.81883 | -44.13023 | 2024-10-05 03:47:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 5a9f9b1a-56ac-3d2d-a99c-d3bbcb40567e | -5.81794 | -44.13536 | 2024-10-05 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 74c0fafa-848a-3858-ac25-83682ae0cbd1 | -5.71581 | -44.81368 | 2024-10-05 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 993b324c-8e08-318c-a41a-aedbebb676d1 | -5.71033 | -44.81572 | 2024-10-05 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f9a376a-f661-32de-b085-7d0200df8d35 | -5.63374 | -44.32085 | 2024-10-05 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bb54be2-fac5-3cda-9abb-0fc6fa5b9769 | -5.53678 | -44.31244 | 2024-10-05 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51c247ff-57d5-33fc-8b48-0f0f4195e070 | -5.53589 | -44.31779 | 2024-10-05 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dc112a2-7bcc-3f5a-90e6-094ca7ae1a25 | -5.53528 | -44.31528 | 2024-10-05 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fc828991-c02e-3a92-9255-a079183b0a21 | -5.53194 | -44.31166 | 2024-10-05 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d0ddd8d3-5aec-3b0c-b104-36592bcbf6d4 | -5.53138 | -44.30918 | 2024-10-05 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cc5f8b6d-2783-360c-a298-37613f0fd0db | -5.53105 | -44.31699 | 2024-10-05 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7a51f3eb-9f7f-379e-9e14-db0391e882b7 | -5.53045 | -44.3145 | 2024-10-05 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3fd92271-a0c8-3ea3-9980-361219f691fc | -5.53019 | -44.11686 | 2024-10-05 03:47:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30bc6454-be8f-33e4-9f13-2d40fe974bd9 | -5.51996 | -44.20628 | 2024-10-05 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7832aa6-10e5-31a0-850f-87815d0520a2 | -5.44906 | -44.04328 | 2024-10-05 03:47:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4c07362-872d-3993-a3d6-51eae16bf183 | -13.10962 | -46.37831 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8f59b17d-7391-3737-8e64-e73307282cf4 | -13.10904 | -46.35513 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7e74761c-c12d-3916-9fcb-48ce145fa95c | -13.10894 | -46.33967 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 87ce9813-aec7-350f-8628-d45b82234830 | -13.10796 | -46.36074 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 160.1 |


[Clique aqui para ver as próximas entradas](README41.md)
