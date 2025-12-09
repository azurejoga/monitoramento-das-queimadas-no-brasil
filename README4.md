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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb14041a-dae6-3c98-9662-14500a91dfb6 | -7.86267 | -38.73061 | 2025-12-09 03:17:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5e6f317b-848b-3b6a-abec-4511e32ea663 | -3.4449 | -41.6653 | 2025-12-09 03:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 44c3bcdd-d1be-35c7-8380-c983c001b854 | -3.0909 | -45.2074 | 2025-12-09 03:20:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| cb3f215a-9a26-3de1-a6ce-e942c7d71641 | -3.4262 | -41.6662 | 2025-12-09 03:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 40.9 |
| ed920669-2aa7-33f3-bc28-d7fb0ab15d63 | -4.2958 | -45.9385 | 2025-12-09 03:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| be0eb79d-618b-3fef-9676-7696f1f4e452 | -3.4449 | -41.6653 | 2025-12-09 03:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 6458c11e-2cef-3ec4-924d-99634ff00dcb | -3.4262 | -41.6662 | 2025-12-09 03:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 62dc14ce-017a-3131-a3bd-dfc7342cbdb0 | -3.4451 | -41.6413 | 2025-12-09 03:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 6974bbc2-39fe-304f-89d2-cb8010ff421c | -3.4264 | -41.6423 | 2025-12-09 03:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| 3d91fb34-ec9c-31c4-aaa6-fdce8923795b | -3.0909 | -45.2074 | 2025-12-09 03:30:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 46c1284d-6768-301d-aa50-aa5e716e1409 | -3.42276 | -41.66078 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5e5eb9ff-87ad-3846-98cc-76fa5340c6cf | -5.71209 | -42.06221 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a19f7f72-58db-3e2c-9652-d1789e3f61bb | -5.70179 | -42.07538 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa0559eb-3467-350f-bfae-7b3f99c8bb9f | -4.17899 | -43.82775 | 2025-12-09 03:36:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 469eaf06-a530-3681-85db-a7cce1148ae1 | -7.70311 | -36.76191 | 2025-12-09 03:36:00 | NOAA-20 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8e71a964-128f-33bb-8a17-f13131f57b8b | -5.70333 | -42.06627 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fbe0feaf-d762-35e5-8772-06cd0c7208d3 | -7.04283 | -35.26372 | 2025-12-09 03:36:00 | NOAA-20 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4498bd6d-b462-3c3a-be1b-d319e83392d2 | -5.70896 | -42.06409 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c21d89b3-3943-3dc4-bc80-5eac72ee04b4 | -3.43306 | -41.66254 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 35e207e0-1275-3482-adfd-3c024aa0ba8c | -3.2593 | -45.48469 | 2025-12-09 03:36:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b83d280-5088-3ce3-8af3-5c27f491eb10 | -5.08662 | -37.54676 | 2025-12-09 03:36:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 9.9 |
| e26b44dd-19a5-3c96-8997-ba7980b729a7 | -7.8614 | -38.73008 | 2025-12-09 03:36:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a1b08726-2d66-3818-8eaf-a78f8886baf9 | -5.0008 | -41.30343 | 2025-12-09 03:36:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8d5feb80-e754-3771-9be8-72136e4485c6 | -5.82297 | -39.2086 | 2025-12-09 03:36:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4108b49c-5836-3da6-a8aa-2950479c79b4 | -6.81682 | -38.58015 | 2025-12-09 03:36:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 07119de9-3554-31a4-9f8d-580801484b55 | -5.54407 | -35.4455 | 2025-12-09 03:36:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 610a34a9-8ec7-3a68-8791-6e3fe6c8274a | -6.60035 | -39.53779 | 2025-12-09 03:36:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b574383c-b04f-30f0-bdd4-63e90b7135c0 | -5.71102 | -42.06829 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d03ce06c-21c1-3242-81f8-e5b0414a9ca9 | -6.60172 | -39.52982 | 2025-12-09 03:36:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a4eccf80-fe15-3b59-93fd-a13b86eb7ea7 | -2.37455 | -45.7198 | 2025-12-09 03:36:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db16ba37-bc97-30cc-ac94-369af3b88ad9 | -6.76513 | -35.40109 | 2025-12-09 03:36:00 | NOAA-20 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a804702e-46fe-3575-b6f6-16586acac283 | -5.26139 | -37.71808 | 2025-12-09 03:36:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2c5d0877-bdcd-3a4f-b695-df89a4f7f4d3 | -5.885 | -37.67086 | 2025-12-09 03:36:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 914d695e-9231-3d59-8f99-a87ece19efeb | -3.43358 | -41.65947 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 44bddae5-faf1-30e7-8992-b19b09ee68c2 | -5.70994 | -42.07438 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 94667f6e-5dd1-3f12-a477-9a663e6e9f74 | -2.05155 | -46.51112 | 2025-12-09 03:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 236d7305-330c-327a-a2ee-4cfcc7d32bcf | -3.43925 | -41.65726 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 68592289-1df2-323f-a8b4-f837cb142da0 | -8.36769 | -36.69117 | 2025-12-09 03:36:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4532b750-26e3-3965-8c2c-bc473bdacd7c | -6.31777 | -37.70432 | 2025-12-09 03:36:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4c1894b1-ad1d-366e-aec1-e65e85d6a112 | -7.12869 | -35.12652 | 2025-12-09 03:36:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 240fecbf-6ae8-34f7-8f36-7c4f98278818 | -3.95623 | -41.52121 | 2025-12-09 03:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e8942f81-951f-3851-abfc-16c42ec5f8a7 | -3.42739 | -41.66474 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6c7504da-03df-30c8-a91d-8c183e105939 | -4.18485 | -43.82888 | 2025-12-09 03:36:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9da029cf-a571-38d7-aa4e-65ac0034b7cd | -3.95573 | -41.52422 | 2025-12-09 03:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5b9aa6aa-6236-362c-b9e6-f5889b08ce65 | -2.37352 | -45.72594 | 2025-12-09 03:36:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 859816e4-9dee-3529-8855-fb5c6b766d5c | -5.70844 | -42.06713 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 60c7a6ad-a5ce-3dd9-a167-bd864c3ab7f8 | -3.42843 | -41.65858 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d9c5e3a-1611-356f-b754-4926c86b84ee | -4.82192 | -42.98445 | 2025-12-09 03:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 020681b7-20ae-3fae-a312-2faf7d521f7b | -5.70792 | -42.07018 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 09ad3b64-3cc4-3187-aa21-1bfbfb01f2b7 | -5.03561 | -43.60411 | 2025-12-09 03:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3f9def9-63eb-3333-9bbd-909e0fde4b2b | -4.15643 | -38.13905 | 2025-12-09 03:36:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5a629b57-9b65-3392-83b7-aeee95918762 | -6.60104 | -39.53379 | 2025-12-09 03:36:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4ad4f75b-aefc-32c9-9c40-d06998422c80 | -2.05268 | -46.50435 | 2025-12-09 03:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6ee61bd9-9ea9-3661-ad23-b25dd3f502fe | -2.05868 | -46.51232 | 2025-12-09 03:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 634572b0-fd48-370a-a802-9f914b98590a | -6.59966 | -39.54182 | 2025-12-09 03:36:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f976813-b122-3801-9537-e35be8c0a6f4 | -5.22181 | -39.25245 | 2025-12-09 03:36:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1bd2a2cb-046f-39e7-8f93-fd07598d4b39 | -6.87 | -39.13308 | 2025-12-09 03:36:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 20a4de77-f4af-3817-bff5-3839ba593fcb | -2.05535 | -46.50972 | 2025-12-09 03:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 80dc529b-c2af-3090-8c00-0be8151d9282 | -5.70741 | -42.07322 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd578d48-8367-3c05-99ce-276a80621f13 | -6.4024 | -39.5028 | 2025-12-09 03:36:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a4fa71d-008d-318f-96ce-c34f1e916f2e | -5.7094 | -42.07742 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6eb8451d-bd8f-314d-b81e-a6894764abbf | -2.05982 | -46.50544 | 2025-12-09 03:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cf094434-0141-36c8-8a28-06499b15b307 | -3.09402 | -45.2037 | 2025-12-09 03:36:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 36.2 |
| ca1f0db6-9086-3449-b11f-27555937122a | -5.25923 | -37.72033 | 2025-12-09 03:36:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a31efe1e-3b16-388b-8f7e-678937f86de0 | -4.99984 | -41.30899 | 2025-12-09 03:36:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5faea16c-74c9-36cc-baf6-d57feb032adf | -5.36748 | -35.38794 | 2025-12-09 03:36:00 | NOAA-20 | RIO DO FOGO | RIO GRANDE DO NORTE | Brasil | 2408953 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 43a34d3e-9bd3-32b4-b80a-ff858060fc5d | -5.7023 | -42.07235 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 41ef9607-eade-3230-ace6-91395cb716d5 | -6.7427 | -39.44192 | 2025-12-09 03:36:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d3ec232-9253-3e41-ba2d-8779327eb8ab | -6.45697 | -39.59361 | 2025-12-09 03:36:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8e0770fe-2454-3bcf-8caf-c504adb4907d | -5.00177 | -41.2978 | 2025-12-09 03:36:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cc834707-bced-3774-b3eb-96db75d8f117 | -3.43253 | -41.66563 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 71d1a9a0-052d-3e66-bc73-1e9349518749 | -9.01438 | -35.57293 | 2025-12-09 03:36:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 833b1802-e68c-38ce-a467-a740172642bb | -3.43515 | -41.65019 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 65c9d8db-fa4a-324d-a843-c50890957d8d | -3.4341 | -41.65638 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 51b2576b-57ee-3795-a2e5-20537a262c2d | -5.70435 | -36.24131 | 2025-12-09 03:36:00 | NOAA-20 | LAJES | RIO GRANDE DO NORTE | Brasil | 2406700 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0cd9c5df-20f1-3f20-891f-80f435fc63c2 | -6.46923 | -39.23576 | 2025-12-09 03:36:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 500ed0c2-cfbc-3287-abaf-e067bd6fb8ba | -7.23906 | -35.0743 | 2025-12-09 03:36:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4705612f-bb16-3ab8-86db-538561af3091 | -5.70689 | -42.07626 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d41cb08f-8e7c-368e-bf3d-61b3f73d4a53 | -3.42791 | -41.66166 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 76a8e0f4-4860-364d-a862-329b7bb5f154 | -3.43768 | -41.66653 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 944f0f37-c911-3025-a689-e3184e9bff58 | -6.0534 | -39.43684 | 2025-12-09 03:36:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 116b8384-1bbf-3513-b030-2162aad50b7a | -6.45638 | -39.59193 | 2025-12-09 03:36:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6718fede-ef90-3a76-906d-b24e15cb8917 | -5.7043 | -42.07654 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f4b54a9f-8eaf-3f40-858f-2727f74e2b35 | -3.42947 | -41.65244 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 344f0928-8e96-3152-bce4-4e29c22989bf | -2.93872 | -40.13367 | 2025-12-09 03:36:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 76032935-c376-3ab6-af5f-5caff6d9fa42 | -3.4403 | -41.65105 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c77dfff3-89c5-3d7d-ad0d-dfc5a7daec47 | -6.05373 | -39.43739 | 2025-12-09 03:36:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c0c4203-8c73-3d51-93f5-f1b3e7f06251 | -3.25832 | -45.49044 | 2025-12-09 03:36:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cc618cf-1982-38ed-8701-f7b67da575f3 | -5.2207 | -39.25583 | 2025-12-09 03:36:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9b8f557-7358-3985-acf5-97df256a2a4f | -5.52564 | -36.91024 | 2025-12-09 03:36:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e9b7b91-a582-3556-884d-66bc1fde0175 | -3.43873 | -41.66036 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8edad2d7-27bd-3cd9-a556-d8b65d4e468b | -3.4382 | -41.66345 | 2025-12-09 03:36:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 80fd6147-8eae-3b50-9ba3-7db68f35c421 | -3.62499 | -42.36988 | 2025-12-09 03:36:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6006f5a8-31c9-3134-b647-742a3a631da2 | -5.70591 | -42.06745 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3d2db42f-3089-3cd6-8fd8-c4f5c380b273 | -5.70638 | -42.0793 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e27d22d-a55d-3bb4-92e9-1448f331a04f | -5.70282 | -42.06931 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38672ca7-5a21-394a-8eb0-c0bd5258d37c | -5.70645 | -42.06441 | 2025-12-09 03:36:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 26dce2f7-40b6-3b7e-9e15-8a9729a54d09 | -5.3643 | -36.84291 | 2025-12-09 03:36:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8633e2be-1125-3b8d-bb3c-b5a0d3d9a51a | -3.09309 | -45.20919 | 2025-12-09 03:36:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 2a474be5-c359-36ca-8e17-5935c8b263c3 | -6.72181 | -39.96241 | 2025-12-09 03:36:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README5.md)
