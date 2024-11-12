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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7612ef0-9ca1-337e-b3e3-822340f40e02 | -15.89208 | -43.4595 | 2024-11-12 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 83a281ca-e26b-3384-bba2-5702adeeaa61 | -2.37186 | -48.51899 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6172f41c-2eb5-310b-992f-a0baa45c00b4 | -2.12626 | -50.68005 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff18b31c-793b-30e2-b0e2-d490597ee492 | -2.77676 | -50.31165 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d07152ad-5dac-35d2-9a9b-094267eb5806 | -2.78292 | -50.29854 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e1856c7-9568-3b63-a00d-131880bb9365 | -2.81869 | -46.6498 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 513175c7-59f6-3331-9a80-a5c528bb0159 | -2.78183 | -50.3054 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9b2b303-ff38-38be-af75-3b4fe47099dd | -2.76878 | -49.33678 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b42fda3f-840d-325b-96c9-71e1fb4f07e4 | -2.13331 | -50.68879 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| fd79331b-30eb-3907-8d31-c1b4db805839 | -3.17015 | -50.43575 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9e3fbf1-f170-30ff-8586-643bf2a6a7f2 | -15.89437 | -43.45829 | 2024-11-12 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 12b9e5e1-af77-307e-9cf6-fb51a4e7191e | -2.64935 | -46.81583 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 834eae83-1aa7-353d-b8af-06733915145d | -2.90198 | -48.30517 | 2024-11-12 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a5d7dba-ab81-33ec-90ef-5ae72fb7215f | -2.9429 | -49.36529 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24fe6ee4-49a6-31c5-b3ab-0f0642c78c40 | -2.15423 | -50.91172 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a1b3fd6-9713-37fd-b996-1159aa3b23d3 | -2.61955 | -46.25198 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edab0463-aeed-3152-9364-62bf96d12c8a | -3.29609 | -43.54372 | 2024-11-12 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 465fc320-3745-38dd-bb28-e7c475938eac | -2.12978 | -50.68442 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27fbdacd-4397-351d-88dc-a3d695491603 | -2.84445 | -46.63204 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e596c949-1fed-356e-a6df-9a4b459c355e | -2.12034 | -50.69047 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| f82b6e53-f6fd-32ae-ac16-65e932be2ea2 | -2.7295 | -51.83041 | 2024-11-12 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 03415ae6-8a66-344d-b33e-be77bf8f68ca | -2.60617 | -46.16446 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5b455c4-32cc-377b-b91e-4bcd5611b4cf | -2.65214 | -46.81993 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e42c59db-7a2b-3110-923d-89a8c7841306 | -3.1377 | -50.43369 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cc66233-f699-3ecb-8f25-b3d19df9d9a8 | -3.13602 | -50.44404 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f2a0f86-8805-3fe2-aa2f-fc8cf877118b | -2.25521 | -48.85367 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b16815cb-5046-376e-9f32-e0dbbb83153d | -3.07383 | -49.36945 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61dff8e0-385d-3376-bb45-771025efc369 | -2.77331 | -50.30759 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 24643a5a-db4b-398d-942e-c8f8541a94bc | -3.19922 | -50.27974 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a88b7fb5-58f8-30a0-aca7-0d2683caefeb | -3.02588 | -47.98187 | 2024-11-12 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 092f6ffd-e211-3db0-9cbb-0754ba59ede9 | -2.74908 | -46.07674 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 030348b7-b569-3137-b5cd-629abd9d9cc7 | -2.13446 | -50.708 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0720b9b-0951-32ff-8118-0f408081979c | -2.37252 | -48.51485 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c76535e-75e1-3d27-a8cd-3df76b6ccec5 | -2.77386 | -50.30415 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c1b9aba6-9ce8-3b0e-a10b-c21ba0d34ae9 | -2.47042 | -50.40821 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f8276a9-d445-399f-9dc1-14c160b03bf6 | -2.13152 | -50.69991 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 6070de52-48e6-3f18-9423-6c3a66db3be4 | -3.21483 | -50.38611 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82cfaef5-f47b-30c8-99ce-e60f004a35dd | -3.12333 | -48.12025 | 2024-11-12 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1decf809-786d-3590-8042-1832bb2bf892 | -2.11562 | -50.69354 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4089f50f-4b65-3df7-95b1-e2721d3917bc | -3.00719 | -49.11144 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85b0c89a-60ac-3f45-9d5f-3c6c60784201 | -2.86581 | -45.09814 | 2024-11-12 04:25:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 904cffa1-95ac-3c89-98f6-2c3bb4dcf9e5 | -2.51355 | -46.38535 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8174cdb-787a-31d9-ab8b-bcf234abb21c | -3.42982 | -43.03704 | 2024-11-12 04:25:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4f784ca-c829-3130-8936-8f253b5caa75 | -2.64993 | -46.79036 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72cd39d7-0238-3f5d-abe2-059e99de7885 | -3.34027 | -39.90596 | 2024-11-12 04:25:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 445a2410-3939-3900-a32d-8722b493d5a9 | -5.12715 | -37.85703 | 2024-11-12 04:25:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4bc7709f-7d32-3e11-a2b4-6e7e2a70b405 | -2.45723 | -48.59552 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0d45b6b-313b-34c4-842a-d914c0e7f917 | -3.29324 | -43.53948 | 2024-11-12 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 05828424-aac8-31fe-b2d3-49c0762787e8 | -2.00121 | -48.20937 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66df2f05-2cc5-37bc-9e8a-1d3494d66fa6 | -2.63272 | -46.16861 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cbafc6f-68dc-345e-a80c-85b1f418b161 | -2.40763 | -50.30499 | 2024-11-12 04:25:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e488ae18-6c61-3a3d-a89d-2b00ae1d462b | -2.11209 | -50.68919 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 235a288d-7766-33ab-a89d-a5f274578eb4 | -4.06245 | -43.95657 | 2024-11-12 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 28b39ffa-1830-3f26-b7fd-ccf925764755 | -2.956 | -47.36034 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47e91438-2d81-3984-9837-572ebce9cbd7 | -3.15822 | -49.73551 | 2024-11-12 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1be93e1b-780e-34ee-9f71-0638a172c6bd | -2.78074 | -50.31228 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d495030-30d6-3521-9ab5-fa0bf1c35bf2 | -2.65049 | -46.7868 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c914efb6-db4b-3ec6-90ff-46a673e146b1 | -2.6583 | -46.82457 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15daba37-6d32-3044-af3b-419ce602879b | -2.59788 | -46.17383 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a27a4171-e8b6-3f01-98b5-e1cc5e4affaf | -2.89513 | -48.30481 | 2024-11-12 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2106152e-d1ce-3b90-b82b-a05112e8fb21 | -3.13202 | -50.4434 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f8db325-83e3-3f7a-bacc-c6971c9bc245 | -2.78693 | -51.75482 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9b3dcf46-8a35-3393-a302-66468cff8497 | -2.62974 | -46.8091 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e328b970-67d4-3a78-a6bc-abc975c80259 | -2.12918 | -50.68813 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 7d70fd4a-1feb-31fe-a18e-156e17171c1e | -1.8212 | -46.29211 | 2024-11-12 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c75105b-b60a-3548-bde3-9ded4f13c7d0 | -2.53321 | -45.39831 | 2024-11-12 04:25:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 998a9fc1-32a5-3694-94cf-795d3b85a882 | -2.12799 | -50.69553 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| fae84962-90e4-3dd7-aade-7286bde58c58 | -2.1339 | -50.68509 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f021a897-c23d-34b4-86f5-dc377ee988e3 | -2.78418 | -50.31638 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddadbb7a-b0d0-3575-84a2-d9c4864fba91 | -3.19364 | -50.28925 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 852791af-d9a0-3ea0-bfd3-1f755e93b75d | -2.12859 | -50.69183 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 072a187e-00ab-317c-b845-09cdba4d49bc | -2.46869 | -50.39354 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b032176-bc56-332e-a409-8f9398e17780 | -2.69754 | -46.81603 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0906815-3754-305c-be91-4c6add26badd | -2.64178 | -45.98215 | 2024-11-12 04:25:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9715624a-2d9f-3009-a915-5b01d3403ce6 | -2.89423 | -48.30807 | 2024-11-12 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af934467-0f07-3ee1-b614-c387301166c0 | -2.13625 | -50.69685 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8839ed50-a4b2-3cd4-a9a2-27fdc5ac50a6 | -2.21567 | -48.31959 | 2024-11-12 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 428b5c0d-29ac-39e8-8cdd-80187e4eee66 | -2.89804 | -48.30938 | 2024-11-12 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0969a9c-667b-3c65-bfe1-3710b78f85b1 | -2.77365 | -51.61128 | 2024-11-12 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 324e13e1-26ad-31cc-821e-012019ba2e91 | -3.81248 | -45.73238 | 2024-11-12 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56dba88a-e4c8-3681-8398-e0d4381e8c50 | -3.2594 | -48.75893 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 603a723f-e8f3-3bb8-8baa-97f6d210c8ad | -3.48102 | -48.24181 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fcff3e7-4bc6-303e-a5f9-698272945ade | -4.45016 | -37.80009 | 2024-11-12 04:25:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a67b663e-cc0b-376d-8c17-9b6f151415d0 | -2.78635 | -50.30262 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5ce53768-80f5-3419-adc1-a1b4c20a84aa | -2.1946 | -48.38328 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b12f48ab-390a-3237-a865-44abb9bd8fc4 | -3.25799 | -48.75976 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32cc05eb-7b8d-3987-8e9c-8088ed334876 | -2.78622 | -51.75908 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| df141d68-4da8-34fe-8204-ca601171e0f8 | -2.6869 | -46.81798 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 535e24cf-7b8c-3058-9196-dd68691f8afb | -3.2551 | -48.76254 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dbcc168-af84-38d9-a458-354a81207af1 | -2.35857 | -48.95147 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28308693-5e49-3bb6-b66b-aa0496505092 | -2.1274 | -50.69925 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 50206d53-5df4-3a0d-ba00-3bb0da4207ef | -1.67982 | -48.46897 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07242ed7-590e-3fbe-8293-7a93c388db84 | -2.81814 | -46.65334 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6a93f6a-d2f3-3656-a747-3daea4e8eaed | -2.78346 | -50.2951 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 579adcb1-29ac-39ca-82a2-0e5665ccb38d | -2.10163 | -48.94684 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de6497e1-46c9-3e09-8bb0-74ddbeb69c42 | -3.26436 | -48.75117 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28649dc9-6131-3182-9981-0f7f2cf1568c | -2.13505 | -50.70429 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aac0c37-6d95-30f0-ae28-dd1f04d9c045 | -2.17081 | -48.32496 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 085c7876-1875-3888-95cf-30385ada5d1e | -3.02422 | -47.96974 | 2024-11-12 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67043f54-c4d6-3ebc-bcf4-288d5448ea57 | -3.56258 | -45.22475 | 2024-11-12 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README16.md)
