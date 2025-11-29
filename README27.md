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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9faf888d-f048-3761-b863-901be148abb6 | -3.47871 | -51.36472 | 2025-11-29 05:03:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3c495aa-32bc-31d7-a18c-3007bea4106f | -3.57196 | -50.41042 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ccab7598-e6e7-3db7-93a6-c0b6efc1cc37 | -4.01049 | -49.11443 | 2025-11-29 05:03:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 212e101f-eb2d-333b-8eb5-b65dee7289e3 | -1.44271 | -55.52386 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bda373e8-aeb3-33b8-a7d9-a01611ed0365 | -3.32553 | -53.3249 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a55202c5-e7bd-3b86-9248-98b443f4397d | -4.63224 | -43.99013 | 2025-11-29 05:03:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbc0ac6c-9b01-3033-945b-5c05a7c850a5 | -2.78941 | -47.41328 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4cc2dcc5-7484-35f1-976b-b7691f802939 | -8.16407 | -43.19098 | 2025-11-29 05:03:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9b7b7b52-6cdd-354c-bbf0-e92e43b37d04 | -2.77282 | -49.6418 | 2025-11-29 05:03:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c7e1bfd-6e0b-3021-a747-a33d777855ab | -1.04361 | -57.48368 | 2025-11-29 05:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4c2ceda-1d57-36d5-9c9d-ad89935f6861 | -1.54458 | -55.35178 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2e06f29d-5bd6-3eda-9645-7bb222772814 | -8.16932 | -43.20438 | 2025-11-29 05:03:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| cd2337fb-8631-356a-8419-196156a4abfe | -2.96291 | -50.99314 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af3c0ead-4ac4-3b9c-9dc7-4f501cd8b3c2 | -1.95558 | -54.40551 | 2025-11-29 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc15fa17-4052-36ee-b897-8b16a2ad8124 | -3.31657 | -50.27675 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44fbe615-20ad-3c17-abbd-e99d6c7e7bf1 | -2.77897 | -47.4171 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6242551f-01bb-3c1f-86be-8aafd52202c7 | -2.77817 | -47.42236 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20233c17-686b-3f50-b93c-f489f14a2c47 | -2.30417 | -47.73654 | 2025-11-29 05:03:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 535d03f2-4871-399f-8d9c-53b6f6a1c709 | -1.74211 | -53.4095 | 2025-11-29 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33192911-f437-3fec-b190-35dd93a48aa0 | -2.2541 | -51.93642 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 332a0d43-45a9-3c6c-8589-048c5796b1f3 | -2.91347 | -53.06999 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a4a91c4-3965-39c2-b3e1-c9de6fd956ad | -2.74668 | -49.86603 | 2025-11-29 05:03:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbe4a099-3d26-3f93-b0e4-ededaa1663d6 | -3.16694 | -45.24157 | 2025-11-29 05:03:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e866d23-40d0-3539-ad42-74833455e5a5 | -2.9077 | -50.4081 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7caa894b-8ccf-3948-ae56-fddc7559c041 | -1.68585 | -53.65863 | 2025-11-29 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6875106a-3953-343d-8934-78fe03fa693a | -8.16169 | -43.20975 | 2025-11-29 05:03:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 3f392ae6-06e4-30e1-b1f6-190b2ecb5023 | -3.07679 | -50.34936 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c940a4cf-ea2d-356e-af95-557e4cf3b28d | -1.47459 | -55.53596 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f866053a-0e36-3af9-b60c-369a239cabac | -3.35921 | -50.80883 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d6690cc-7222-3aa8-84c4-08646a4d4a62 | -2.90377 | -50.40749 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27d633ed-9db8-3146-8179-1736bdab3d02 | -8.16852 | -43.21063 | 2025-11-29 05:03:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 9f21b131-f99c-3423-bf33-fcea8e64c8a9 | -3.68074 | -54.56233 | 2025-11-29 05:03:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a922b4c-c607-3939-a208-7fc2bee8d682 | -3.87401 | -54.23859 | 2025-11-29 05:03:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a79547c0-584d-3c2a-a682-2b67bbafda82 | -3.32611 | -53.32124 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08f0c8b2-3dda-3c7b-a28f-b9b039b6fb81 | -2.92807 | -53.26846 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccf0c3a2-db55-3aa2-8773-9e7f489c63e3 | -1.75856 | -53.99593 | 2025-11-29 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2065a7b-c1d0-31b4-8ff2-0b60f22dd0f5 | -2.91632 | -53.07423 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39f76a8e-daf1-3c00-8d43-fe8a1ea34e5f | -3.31552 | -50.28363 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf49f7a2-4cba-37b1-aa00-f13c3de62938 | -2.93772 | -53.27373 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21c68c92-faa5-32ac-b5f5-94c543871534 | -2.69765 | -51.79443 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3b23fb9-b29f-3d45-85e4-8a5af5c71a37 | -3.57432 | -50.30135 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c2f0378-2eec-3904-b8f2-ae1ef694e393 | -3.98319 | -49.02567 | 2025-11-29 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 323501dc-827a-3e79-9dd9-e1da22b669d4 | -3.17116 | -51.25063 | 2025-11-29 05:03:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6ee5dce-973f-366b-8635-792acfdbaea4 | -2.92377 | -53.0715 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 862ac6ad-1ad3-31d9-861b-5aca36278cca | -2.75049 | -49.33502 | 2025-11-29 05:03:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42fc9fe0-8223-3f26-82ed-af59dada8af7 | -2.82504 | -52.36413 | 2025-11-29 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b52ad6e4-12f8-372a-a393-765e94f5fa59 | -3.84167 | -44.129 | 2025-11-29 05:03:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf062810-4ed6-3c24-9427-0b7bba0ee80a | -3.32888 | -42.50202 | 2025-11-29 05:03:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87760121-9bc0-3bad-9a06-2758a9cbddec | -6.60054 | -43.68779 | 2025-11-29 05:03:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16e4b82f-1ff4-331b-bdf3-2d8700eecad7 | -3.03498 | -50.98037 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18e6b968-0d97-386e-bcd1-9556c962ac36 | -3.33013 | -50.26826 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 34b1b135-b5c1-323f-a0a9-2724ad7a6c24 | -2.93204 | -53.26536 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46eb6bde-ac1f-3216-8401-2ae1f3f7b4a5 | -5.00086 | -50.72239 | 2025-11-29 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a816766-670f-384a-827c-7728e42a3a33 | -2.39592 | -48.51682 | 2025-11-29 05:03:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de522140-d355-3fd4-832f-6e5bbdb3a5e7 | -3.63907 | -53.98554 | 2025-11-29 05:03:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4285c5e7-c52e-3db3-aaa3-75d06c4ff26d | -2.24734 | -48.31693 | 2025-11-29 05:03:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb41ab13-7a59-38f6-a0fd-31d39c436145 | -3.79867 | -51.14501 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c10d0eee-51cf-3c15-a34f-d09664351183 | -3.84054 | -44.13385 | 2025-11-29 05:03:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9d0ecff-b9b1-364f-869f-00fc8c5a51bd | -1.2911 | -55.42869 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5eef207-b865-3913-b92a-1360a6a90355 | -2.92318 | -53.07523 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca7da989-fe55-3be0-b75a-f262a1634659 | -3.40501 | -53.26509 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc52d95a-5264-3e8d-b425-b393d110c74b | -2.92603 | -53.07946 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afd173e3-a43b-3c73-8445-d9094d3b4bbb | -3.33239 | -42.50032 | 2025-11-29 05:03:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92924e7b-0a7a-30c5-849f-82c0dc1e56b8 | -8.66626 | -44.22765 | 2025-11-29 05:03:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b0cc416-bf86-3e37-9305-19312fd314d1 | -1.35983 | -53.09734 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb1c73f1-f765-365a-ae9d-32d7cff35f8b | -2.78458 | -47.41256 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efae0afe-be12-3308-959d-4709b7587839 | -1.52387 | -55.54717 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56184909-2a40-3934-8f4b-32413a160dc8 | -3.98693 | -49.03056 | 2025-11-29 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20cba832-09b6-313b-92a9-08faf9e186c0 | -3.52309 | -53.06921 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff6454f2-b31f-3acd-9b94-5c87f70727b8 | -2.8913 | -49.46197 | 2025-11-29 05:03:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82c53992-3160-33bf-9dab-67a13769ef45 | -3.33067 | -50.2648 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0734e8e3-a182-3c67-982f-064c71d11ab0 | -2.96043 | -53.2846 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f84ecc6-4e2b-3ac0-a01b-1d2d254af1e1 | -3.20241 | -51.14816 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e355d5d4-c345-33ad-916d-3abce9080633 | -2.42427 | -47.23377 | 2025-11-29 05:03:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0932e082-c129-31a9-b91f-f4898e881f9d | -2.83833 | -53.01273 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2eb56dfa-64d3-3ec0-a75a-1f52869ef447 | -3.98759 | -49.02626 | 2025-11-29 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9c18835-49ed-3ec4-aa22-092641765640 | -1.28779 | -55.42817 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7e250a1-dfed-3768-b52d-aeceb389e852 | -2.97018 | -45.50885 | 2025-11-29 05:03:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ebd6391-4c49-3ab4-8d3c-d9b2e6af2f66 | -3.22724 | -50.31215 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cf64f6b-74f1-3dcf-8d5c-d177ea01af95 | -2.78703 | -47.42892 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7391a168-cb98-342f-ab4e-bfa1539ce40e | -2.78219 | -47.42836 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 56189ce4-df4a-3310-aac3-40df85f24125 | -2.77825 | -53.26056 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec6a1842-1f7f-31f3-9c6d-8731cf74f9ef | -3.40551 | -53.30673 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14b3e579-5a6d-3e0c-b6ba-2b7b5ff7ad64 | -1.76021 | -54.78317 | 2025-11-29 05:03:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1d2c7f6-1770-32c1-a3b9-929a1c6ee2e8 | -2.77976 | -47.41187 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89b6f7bc-702d-3a21-bff3-875987c3fd79 | -3.86313 | -54.35193 | 2025-11-29 05:03:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82856bc8-46bc-3aea-a7bd-b1650dd6832b | -2.59943 | -47.34352 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c4589c8-809c-38b8-9f38-13664f36f9d2 | -2.92864 | -53.26483 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62c1ba44-bb43-30d9-9ae1-30db0bb2c774 | -4.73677 | -44.43351 | 2025-11-29 05:03:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faf2b69d-3b99-3796-bf04-d3e388ffae41 | -3.40892 | -53.30728 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6b2351e-331a-3ff3-bd0d-26acd43b5588 | -2.64537 | -48.02285 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35aa8771-9d33-3bf5-904e-8f8ae12d148f | -1.84524 | -55.34252 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 252d175d-2dfe-3370-a6c8-e6abbb37d52c | -8.16249 | -43.20346 | 2025-11-29 05:03:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| b60998c1-0b25-3d6c-b12e-7040107b0061 | -2.78861 | -47.41853 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c39295b7-17cb-3db3-b56f-d9dddd5db1e0 | -3.34106 | -50.27703 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af699312-e151-3420-ac3e-86231abc1532 | -3.57542 | -50.29429 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad6871d6-0bf1-36ce-8f48-47191925104a | -2.94332 | -54.28357 | 2025-11-29 05:03:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aeb33bdb-0898-3dc9-a6bb-8263407d781a | -2.41943 | -47.23294 | 2025-11-29 05:03:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6e2c733-0268-3cbb-a31d-4c225662b3b6 | -4.86106 | -50.82328 | 2025-11-29 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d959d51e-7416-3703-bbd3-e5bb6cf45fd3 | -8.66691 | -44.22246 | 2025-11-29 05:03:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README28.md)
