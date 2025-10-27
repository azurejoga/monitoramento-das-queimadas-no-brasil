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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 206b449e-e4c8-3a48-bb1b-137abf5ee693 | -3.14623 | -53.14498 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 944ba9cb-e244-30cf-989c-a72f312184d2 | -3.13205 | -53.00085 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fbac488-bd5c-3491-846b-32e019b97fda | -4.19898 | -48.36428 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71929060-f72e-35ba-8174-60e32dca28ca | 1.67954 | -55.66128 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0624b9fb-4380-3569-92a5-8ab2a01bbc94 | -3.52346 | -52.20744 | 2025-10-27 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 909b0cbd-2a24-30ac-b86b-c75d6a7ee422 | -2.48014 | -58.04181 | 2025-10-27 04:59:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 999fd99a-9bd9-380d-adac-52f06ce51f99 | -3.23912 | -50.65071 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d95a852-0d49-301f-8d85-e379513e9dd9 | 1.62412 | -55.71301 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d11a3bd-abdc-32fe-86d4-8ce264cdc79f | -3.09821 | -49.44408 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e16f05c0-801b-3b73-a8a0-742c9ffa3573 | -3.56859 | -44.53169 | 2025-10-27 04:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cfc99d3-7cac-3291-98cb-137b8fc0532f | -4.39167 | -43.31461 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 476389c3-6709-3018-be5a-6eb66a581ff9 | -3.33783 | -42.88517 | 2025-10-27 04:59:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbc53ed3-f5af-3c8c-aac4-e282fb6fd28e | -3.14351 | -50.45285 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 129db2a7-5759-3889-9877-a8504132d252 | -1.40096 | -53.09797 | 2025-10-27 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e32bad3-e042-3365-a322-864fe991e73a | -3.42325 | -52.62836 | 2025-10-27 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78093a08-7c45-3e98-90c1-5ddd0c7df0a8 | -3.24332 | -50.64723 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 08d3e138-558a-3627-88d5-aeee9294d127 | -4.47597 | -43.42594 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5e77ed8d-4260-3efa-8645-0a3dbbc871b9 | -2.94374 | -51.7628 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b28e30d0-0e3d-3cf0-9756-96c417a7821b | -3.89067 | -52.13385 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9682873-0c8a-387a-8862-6f2687c8d159 | -1.75173 | -46.53766 | 2025-10-27 04:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcdc4005-6c55-3ad9-9d8e-a4c2752333b7 | -3.57393 | -44.53253 | 2025-10-27 04:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 578dab7d-dfba-30f1-ad6e-e92dbe20b2db | -3.40845 | -52.72306 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a6a144d-7862-3c7b-8e58-e23254820425 | -2.7944 | -48.89479 | 2025-10-27 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4435a503-9b3a-3a4a-bf5c-e50dd1934847 | -3.85616 | -52.17668 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 560249b6-c242-394f-8d61-631476280e76 | -3.11891 | -51.26277 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec0b482e-b12c-349c-92cf-2735876b615a | -3.47064 | -49.97783 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ab93357-eb8d-3723-bcb0-2bbec3d07063 | -2.69386 | -48.45786 | 2025-10-27 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1623f0b-4f04-39b3-889e-f74f247124f4 | -3.10583 | -49.4453 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 716e7d24-cbf6-3620-bcb3-967b56e88a87 | -4.45093 | -45.4601 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be936e69-71fb-3d18-9c25-b453c15c46c7 | -4.89397 | -43.22718 | 2025-10-27 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16fcb81e-32e7-39e9-a27f-8ba3d90d2b9e | -4.483 | -43.41869 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a2116f8-32e5-33ad-b585-ca5f012b49de | -3.14712 | -50.4534 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b150bebd-d2bc-3d42-9bac-7338e9eed5e7 | -4.47015 | -43.42496 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1a746f2-e800-3b37-82af-5d895475bd6c | 1.61942 | -55.73109 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a556a48-64f8-3d3d-af18-881ac929afad | -3.98688 | -51.03664 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ed039ac-bf55-3e32-96a6-abbedf4ec020 | -3.75493 | -51.75361 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ac6fe5f-dc25-38e1-8783-3ef233cd7c19 | -2.25746 | -51.88841 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f00e2aff-5d3d-3b81-af61-a3a9c822ca25 | -4.25271 | -48.64448 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf5b4c41-3b1e-3a3d-9621-8e211b32e844 | -3.36557 | -53.10518 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3df4ef78-3e00-3b2f-8685-4a80442a9250 | -2.35493 | -48.29095 | 2025-10-27 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1563066e-a80d-36a3-aec3-d6c97297d646 | -3.9875 | -51.03268 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02b7c838-99c2-3921-9895-f73e92c55d6f | -4.83241 | -45.34212 | 2025-10-27 04:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1aeb5a22-e773-380a-804a-481ec780426a | -2.44643 | -49.02794 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 040d034a-d377-38f5-8e2d-1f8737e95c6a | -3.05446 | -53.01717 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8244f13e-8322-3e7c-963b-910ce07428b9 | -3.52007 | -52.20693 | 2025-10-27 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d77dd11-59e5-343e-9e91-efe8e496079d | -5.59551 | -41.31792 | 2025-10-27 04:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a7b0061-8271-3cb5-8e46-868dbcea26d8 | -3.04781 | -53.01614 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec270a04-c78c-3d03-9fa2-fca89c3f9f7a | 1.60244 | -55.74066 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2b0e55a-80e1-3902-9ce7-945ebde7df94 | -2.78647 | -54.41742 | 2025-10-27 04:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7684bdf5-b74c-36c5-99b5-a7e14378acc4 | -4.09964 | -48.02237 | 2025-10-27 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 251bdcbf-5c1d-3cc5-88e1-5141c4c25e59 | -3.41769 | -51.85728 | 2025-10-27 04:59:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dea1d429-d13b-33cb-9793-7b7e4ee98534 | 1.62477 | -55.71724 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e28f4a0f-1a2f-3a71-a0fb-07e43eac5610 | 1.60012 | -55.74968 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e62cc187-0e19-3810-bbfa-2147e60dc89a | -3.1267 | -50.15151 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5896c6ea-34c6-308b-8614-d9f1ce6dd99e | -3.24564 | -50.65586 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2a19a70-46af-333c-8d9c-8a600d6ee27b | -4.32666 | -48.08723 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 352c6ba8-1b57-383c-97ed-80e2b122670b | -4.45406 | -43.65514 | 2025-10-27 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4da2a939-7f1c-31c9-90dd-314112c344bb | -1.18936 | -53.38928 | 2025-10-27 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20970c96-adc1-3e5b-b56e-e7a4e1c63e78 | 0.43624 | -50.79142 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 51205f3e-9b81-3d24-a215-c3fc8ae6fd2f | -4.63779 | -49.54213 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a37c29e-bb71-399e-97c7-5ff16ed06a91 | -4.21668 | -48.35947 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 599fac1d-2372-3f45-89b8-be1c1c16f819 | -2.86954 | -54.20757 | 2025-10-27 04:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c95fcb36-49e5-3885-93b3-0b0e3e33b3d0 | -3.13593 | -52.9979 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6500ae06-8771-3ee9-898c-553f6e6760cc | -4.48239 | -43.42279 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 99169ccd-2f13-318d-87c2-fb5fe80225b5 | -4.45601 | -45.46095 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07578f9c-55f7-32e4-be2a-b39c78f63f25 | -2.32495 | -50.53242 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9131e9f2-db02-3bb9-82d9-d4e770d35fa4 | 1.6031 | -55.74488 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64b15483-bb87-3e43-a187-569b05b9d823 | -3.8636 | -49.80577 | 2025-10-27 04:59:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3233184d-118c-3afc-a28d-e0ec85e537d0 | -4.47959 | -43.43266 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f1ba96bf-e4fb-3f62-a831-517f69a0a57d | -3.82666 | -51.69561 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f512c3a-9eb6-323c-bbc2-de96e7ea08ed | -4.46796 | -43.43072 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d67a66ec-402e-3c72-85bb-c365496028d7 | -2.79288 | -54.86255 | 2025-10-27 04:59:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6b547ba-5062-3da4-9841-6c06813adb6a | -2.69629 | -48.46896 | 2025-10-27 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e75675d9-cd1c-3953-b831-0e10dbdf313d | -4.48057 | -48.6718 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69de047b-4773-3d10-957e-0c85c4e7d692 | -3.04548 | -51.22428 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27cb39ed-c676-353f-a380-22f960d9c067 | -3.51813 | -49.23574 | 2025-10-27 04:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad7b6e97-552c-367f-ab37-baef75fa3fad | -3.93493 | -54.84708 | 2025-10-27 04:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d801ecdd-683d-3d73-a46c-5e530867df36 | -3.6109 | -43.55956 | 2025-10-27 04:59:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 618db0f7-b83d-3381-93b6-bf379ccefb11 | -4.46493 | -43.41996 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d58ef5c2-9a31-3250-a38e-c8f4dcd9e56c | -4.26962 | -50.51789 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48e559dd-138d-35cd-9401-a059cd001127 | -3.71407 | -47.64227 | 2025-10-27 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58c87c0c-1564-37e1-ad9f-723686576140 | -4.09965 | -51.04839 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bfc91962-d898-39e8-8b7b-5ac98d5a7654 | -4.45849 | -43.42322 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 861cb63d-5935-3cbb-8e49-e3a252d0f8e4 | -5.58733 | -41.31631 | 2025-10-27 04:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 19d0017a-af7d-34e1-a364-cc0c2859d742 | -4.15624 | -51.08125 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9004a952-4c6a-30bc-893b-8cbb1bcf65de | -2.81421 | -49.13241 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0a7477a-b968-3bcf-8bb1-2e09440cd025 | -2.94432 | -51.75914 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57842c9c-7c42-32cc-8a14-a0b04108a739 | -4.48191 | -43.4162 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08dae56c-ba6c-3576-9ffb-6550698c38c7 | -4.43672 | -45.97887 | 2025-10-27 04:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93725587-f570-30c9-a7e9-614d933266b6 | -3.93057 | -50.02473 | 2025-10-27 04:59:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb044416-1ac2-3a4e-a7bc-47842e8a6ff2 | -4.28185 | -49.66834 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22cd6fbd-a8ae-3865-8f40-5f5d5d4a30a2 | -3.15846 | -50.33181 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e03b30fa-6488-3a5f-bd91-abc2f9d22401 | -3.83418 | -50.20002 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d10512a-89a0-32c9-95f6-c5c0588d91d5 | -3.23974 | -50.64668 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81cfade7-f055-3cd4-b8e7-44b532f4135a | -5.5947 | -41.32399 | 2025-10-27 04:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fca6d0d9-e7c3-3e56-837a-bc08e5f25b8c | -3.75873 | -47.61119 | 2025-10-27 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b01958d-f5e4-3f70-b7f0-40a82565f868 | -3.34664 | -53.0738 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2403a81f-8159-3b68-9288-1e24fda898d2 | -4.86719 | -48.52574 | 2025-10-27 04:59:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98f477a4-7948-39c4-aa3f-b64574ecc299 | -3.46456 | -49.96795 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 755f8673-a826-37fb-a68c-efe58b0ceebc | -3.11964 | -51.21201 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README56.md)
