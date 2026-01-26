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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc48b245-2e07-3658-a6bc-b6945a16d7e6 | -19.7246 | -56.8198 | 2026-01-26 05:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| d82c10bf-21e4-368c-ab56-8a6bfbd20f31 | -19.7242 | -56.8408 | 2026-01-26 05:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 138.6 |
| 9d10870a-01e9-3442-b13b-4b0e2eb2c56c | -19.7045 | -56.8226 | 2026-01-26 05:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 178f34ca-075c-3b7e-b04b-61171e14d3be | -14.33313 | -57.72084 | 2026-01-26 05:20:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59b5180b-83d3-3520-8960-baa32127936c | -14.33251 | -57.72511 | 2026-01-26 05:20:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d99fc881-1191-3ac2-8657-bad6f214be90 | -19.63656 | -57.28109 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| aafa6d5c-68ee-335a-86c2-57bc37c49660 | -19.71457 | -56.84484 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 587c94d6-b826-3d76-aee7-9a1e5d36cdbd | -19.63208 | -57.34513 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7a62e238-4c0a-3893-92d1-b63c04cbb7eb | -19.71503 | -56.84106 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 8ca75331-4ddb-3169-883d-1090816a439c | -19.61379 | -57.33173 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9d6928dd-d2e0-3cf9-bcbc-2c89f902b979 | -19.64709 | -57.34933 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b4faa8a7-e62a-3751-a3eb-c5b9eeeb3e6b | -19.66215 | -57.3569 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c8f06cef-1d1d-3194-8ba3-51baaf7e7f5d | -18.8267 | -57.72127 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b851916b-8555-3889-8f3d-f7c2617b6da2 | -19.65428 | -57.35575 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4ac0d52e-35df-3203-b56d-d15b4e14773a | -19.71194 | -56.86385 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3b07c4e5-74fb-3773-abbc-bcbefda4f3e9 | -19.7155 | -56.83729 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 58042fd5-6a4c-302c-bbdd-8295c083b848 | -19.65121 | -57.28518 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c7730776-14d0-3819-8e2d-c0b99ecf4ed5 | -19.61703 | -57.33759 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5361d74f-4410-31a7-9fc0-251c8c37eafd | -19.71223 | -56.86366 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 507bf7de-8615-37e6-acf2-e53108827a70 | -19.63855 | -57.35345 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a0f3d01c-16ca-3208-9303-114151b8bd6e | -19.63924 | -57.35154 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 869e09cf-a051-34c8-a6a3-a189b1248096 | -19.71597 | -56.83352 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6134b7fa-b878-356c-82b3-96a069daa9c2 | -19.67269 | -57.17913 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 39ebd0de-94d0-33ae-a083-ed1138b225e3 | -19.64841 | -57.28279 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 92d6874a-92c7-38ad-9ee9-8900bba2adc1 | -19.65276 | -57.31045 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| abe96cf1-9a9d-3f4c-a4a4-f4d002b6e78e | -19.60821 | -57.28239 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7fe2efa2-9552-34e8-b529-27ebeea6b78d | -19.66689 | -57.3199 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 79086ee4-4462-394e-9e32-8f5dfdf09991 | -19.7149 | -56.8413 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| dcb3cd8e-1cf1-30e4-b72b-fb98fc35e1df | -19.6666 | -57.17634 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 09538bbc-a70b-3492-9523-9ea681c50c8f | -19.61449 | -57.32645 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 92a07795-2d3d-360f-a2fb-5bd518d9e740 | -19.72316 | -56.84223 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 243a427d-2b2b-31a9-b967-38e1764b2481 | -19.71084 | -56.84072 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c774e7a8-4236-3606-bc9e-a77b7a042f8c | -19.64658 | -57.26627 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ab40f066-6adc-3c08-b39f-d46d1e97ea28 | -19.67455 | -57.17748 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 677c1212-29ca-3d93-8139-aac2d31ce146 | -19.64446 | -57.28223 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3f7faf71-f9fe-34b0-bba8-f81e70b85b85 | -19.65955 | -57.28982 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ae2a6d65-7113-3882-9525-dca282e5cdc5 | -19.61333 | -57.30475 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c30cbdb2-6099-3593-a645-bb7cd0e3c962 | -19.65822 | -57.35632 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 17742037-81b3-3124-b57d-76f1404bb171 | -19.64051 | -57.28166 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7e74dbae-e7bf-3577-be36-663efe152e81 | -19.66191 | -57.18115 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| cf1d5730-d76c-3eb6-9d61-c529cd094b8e | -18.84372 | -57.73874 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5402e4ee-8cab-3908-8878-4a167033bd3c | -19.66474 | -57.17797 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e7dc4aa8-49c9-3cd2-8e39-b7832f5dff56 | -20.31122 | -57.82124 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d29ac802-7c3f-3e4f-ac9c-050e2491d8c6 | -19.34528 | -54.17551 | 2026-01-26 05:22:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0eb2dd2d-7596-3d6a-b6ab-691eb89959e4 | -19.66553 | -57.3305 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d18a25c3-b575-3c0e-bbd4-d7aaeedad2e5 | -19.71628 | -56.86425 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 17c71037-4202-3a56-ba3a-94ed1513e258 | -20.30669 | -57.82574 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| bc149434-591c-3b21-a9a4-07bed3470d4b | -18.7761 | -57.66375 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d285cfe9-b926-3802-8344-d6e867f8c46c | -19.34589 | -54.17016 | 2026-01-26 05:22:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a674d34-0b58-3ad1-b572-2ec286c90936 | -19.69053 | -56.83784 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8f68517f-6150-34d9-9011-f53564e00dd0 | -19.65179 | -57.31231 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9fa5ab85-d093-3cd8-b326-957bcac7e8d1 | -18.84696 | -57.73627 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8b179245-0a25-3881-9d2f-eb65c119decd | -19.70727 | -56.83638 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 9d4afb8d-db00-31bf-bf4f-6f3243af8784 | -19.7069 | -56.87078 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2a2d4b86-52b1-32b8-b0d8-0e5acf3fed6c | -19.62814 | -57.34456 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b44fb295-5448-3645-ba83-881746665dac | -19.65361 | -57.36102 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a1a70a1d-6709-3aae-a788-18186bb2eed2 | -19.65671 | -57.31102 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 78aa92e9-acd0-331e-98b8-8f749ed0e767 | -19.64728 | -57.26094 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5fa17a19-7334-3757-abeb-53b46455740d | -19.63138 | -57.3504 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8daad646-c714-382e-b29a-c8d20a0bd81d | -19.61055 | -57.32589 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 29ae09be-1199-3b85-937c-a4d3ed7cd855 | -18.81974 | -57.71525 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9d179b2b-c8a2-37dc-98aa-2ca149113b5d | -19.71191 | -56.83294 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2fe9bb5a-a8e9-390a-8acb-849044391a85 | -19.65236 | -57.28337 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5f236fcd-bd4b-3f13-a845-31a53047d334 | -19.7154 | -56.83754 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 75c8537a-bd81-35b9-9b68-b9aaecfa499e | -19.71244 | -56.8601 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 75988365-3f29-38a5-a353-abb9fe49b48f | -19.71133 | -56.83696 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| e43d5fa8-a85e-301c-a8ab-5ac54d62780f | -19.69915 | -56.83523 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 4bb0e1ae-a5a6-3b2f-becb-35f589b19498 | -18.82736 | -57.71638 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bef45353-21c6-316b-b2fd-626b7fb972cf | -19.65105 | -57.35325 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| faccc0e5-c29d-3446-9335-8cad469090a6 | -19.65516 | -57.28575 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 39d656fc-77bd-39e7-8ec0-ab0b8ae1b29a | -18.77675 | -57.65883 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d4dc19e0-cb5e-3623-bf0f-5c9ec454bf30 | -19.71863 | -56.84542 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 28c42abd-f719-3e63-8b07-749efa3f0ea4 | -19.64318 | -57.35211 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3e035545-2462-3d7b-b60c-9d0a31bc2be7 | -19.71144 | -56.83671 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 14f13473-8eca-363e-a085-92ebece5dce3 | -20.31508 | -57.82181 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fca4063a-ac80-3a0b-8b30-dc95672f073b | -19.69508 | -56.83466 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| b1b5eb46-b939-3532-a3df-6183586e35f2 | -19.65035 | -57.35518 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ee2026a3-ff7f-368b-a4f3-88db288c9f51 | -19.65754 | -57.3616 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1f0f7310-f4aa-3d50-9398-642688d53afc | -19.65911 | -57.28632 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 60bfaa70-f3ef-3186-976b-c1ff8fe62136 | -19.65574 | -57.31287 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5b70cf91-f991-3f60-b948-f24d7704b202 | -18.84753 | -57.7393 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7b818ff9-8a31-328c-b692-abdc7fe1f129 | -19.67925 | -57.17265 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 20c8a2cc-3e44-3010-9624-fb819efced9b | -19.64315 | -57.34875 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 62dd25e3-003a-3d17-b321-7ac2f856d900 | -19.64726 | -57.2846 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d091be21-ae1d-3a7f-a8fc-a5a2eb85da0b | -19.70724 | -56.8706 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0263bf09-b291-3d7e-b517-d8238fd8878f | -19.72363 | -56.83846 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 8fd3225c-5538-3a29-8a04-d3674d722eb8 | -19.61263 | -57.31004 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cfc9f6e3-aff7-332f-9e3b-3f6875979e66 | -18.77741 | -57.65391 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| c44ec2cf-d88d-3cc8-bde9-e4b82c798f08 | -19.6556 | -57.28925 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f93b5e9b-ffa3-3f22-b408-b6feb708efcb | -20.31055 | -57.82631 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d021fc37-2e49-3241-9c8f-80f26d99a1ba | -19.60752 | -57.2877 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 77d3df94-ebc7-3468-b221-63fab0eba995 | -19.63531 | -57.35097 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 76137dc0-ccc6-327a-aef0-4b2470b51367 | -19.66065 | -57.31159 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ff43036c-846a-31dc-a598-9f0c4eb0fcfc | -19.66295 | -57.31933 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a35bc77e-0277-34f6-8a5f-2d0702a15e18 | -19.65994 | -57.31688 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4640ef5e-acf2-39a5-b463-a468b42b7676 | -19.62097 | -57.33815 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| aca8345a-9760-34df-a834-f989995c4124 | -19.71097 | -56.84048 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 6e822bce-5b99-3844-b75a-5af09763632c | -19.62491 | -57.33872 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bfbc7ad4-eb8e-301d-943c-e1df8f2b847a | -19.71182 | -56.8332 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| a2e71b04-699e-3467-a428-e2e667d267f7 | -20.91749 | -56.38159 | 2026-01-26 05:22:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README7.md)
