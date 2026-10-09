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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddcd5101-c0cd-3835-8a09-1d205e00eba4 | -3.35087 | -50.41226 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 301446bc-5f1b-3a84-bbff-9cc4a76113fb | -1.73742 | -52.24536 | 2026-10-09 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8275ba72-44fa-3958-9c47-59b6839451d5 | -1.05231 | -53.59471 | 2026-10-09 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51fea20d-ba55-31d9-99f3-6f5766d2b3e0 | -2.47096 | -56.08492 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 324a4627-cc09-3dce-b903-04f146f68c83 | -3.35166 | -50.40731 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 38406265-7ecc-3f32-aca5-9920420ece3e | -2.74946 | -54.09833 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c87a819d-a22c-3040-9e11-b6dfb69c9f4a | -5.14294 | -48.8682 | 2026-10-09 04:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d959469-e23c-398e-9f84-363f33c30505 | -3.75868 | -40.75296 | 2026-10-09 04:25:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fa8f2f3e-08b3-322f-8ebd-6bd81b8e42a3 | -7.13251 | -41.80697 | 2026-10-09 04:25:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 49b15b95-9ea7-3458-996b-7af7b866864a | -4.82428 | -45.8343 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 378818a7-e8aa-3906-be91-f23fa09e87ff | -4.6718 | -48.95594 | 2026-10-09 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2561b18c-b05f-395d-8932-9b86feeaf7f3 | -3.07405 | -53.96862 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7fbb552-be1b-3a86-9167-4be23df5a980 | -5.23975 | -43.98033 | 2026-10-09 04:25:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dd65e9a-a78b-3462-9f6d-02a57e7bd5a4 | -2.84193 | -49.87788 | 2026-10-09 04:25:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a28f55e1-6299-331d-8769-e7be672c1a7c | -3.09882 | -53.94301 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbcec26c-3834-307f-90c7-14815058af76 | -3.02072 | -54.04077 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 560cb716-5491-398c-bca0-21a61a7afbdb | -5.26188 | -50.14265 | 2026-10-09 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04670b73-04b0-3b46-9b5f-466ca974d402 | -3.15583 | -57.68134 | 2026-10-09 04:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aee31dd6-b5de-3240-bc47-d33e67963076 | -2.93585 | -54.05751 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb839872-0ec0-38e0-b48c-0e8c37ee2a66 | -3.02044 | -54.0469 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 012e0e9a-2981-34f1-95f6-b8d6d5b13cef | -6.88951 | -45.03324 | 2026-10-09 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcab0fd4-53a2-3ae7-be0d-feac21910328 | -3.08255 | -54.28414 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f4d2f29-a553-3a99-84ce-20c444526856 | -3.55271 | -54.69447 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fd298ec2-188e-34df-94f2-f322dd497043 | -1.19778 | -46.15254 | 2026-10-09 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29facdd0-6634-37ec-9376-41adea2a2123 | -7.19254 | -44.27726 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1dc7b60-1c9f-3e12-8222-78c90fb76c4d | -3.29612 | -54.05744 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e210ba7f-db46-376b-bc43-1d6e2eab24d7 | -3.00762 | -51.0147 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7ef5ed5-a61b-3276-8455-d4b7351abb8a | -3.18975 | -50.58681 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 337068d3-b283-3f42-a9d7-9df17d36ffa2 | -3.86833 | -55.99028 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2271079c-90f1-34d2-bcf4-d3a659a74903 | -2.99461 | -57.75627 | 2026-10-09 04:25:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e428db8a-bc28-3410-8a63-c4ef93f9d541 | -6.70894 | -44.1168 | 2026-10-09 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 220b2ef0-756a-307b-bf30-591acef1ea06 | -3.08429 | -53.93781 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e06f28ff-59e5-366e-a4f0-70fdbf9986c9 | -6.04769 | -44.03673 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47f9b005-9111-3dc5-b70c-ece0582add4f | -3.29921 | -54.00747 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2249347-c80e-36f0-940a-415f7b7e70cb | -3.34383 | -50.40609 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 458185d7-fc70-371c-af82-e54460f48e0b | -4.64198 | -50.9624 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15191ed8-fe0d-374f-98dd-6c3e7ad0741c | -3.20964 | -53.86472 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9ee7f7c8-7f43-3b3c-8387-ed9e0bc8f3f9 | -1.537 | -54.55323 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fa1b44f-5727-332b-b971-6924a9e2cd26 | -3.3049 | -49.1283 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a22db31-90cc-3ad9-b7d9-ca8d30decb4c | -2.41293 | -56.53473 | 2026-10-09 04:25:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| faa7bb6a-ce2d-3ef2-8493-9bb357d4d6eb | -3.56826 | -54.69432 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 65e14f0e-35e0-30fb-a389-4eb534b58c26 | -3.00419 | -54.08351 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25f3e16e-79b8-3f62-a8f6-87beda3c1f2b | -1.21231 | -55.646 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e6fc41f-2932-3ada-b276-a4049e444ff0 | -3.08283 | -53.94659 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1718fa32-7e33-3402-b8cd-b802be54b9f9 | -2.95606 | -49.17362 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f073b502-4749-3667-880c-ded23180b8b3 | -4.50542 | -43.61863 | 2026-10-09 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 29429afc-6399-37fa-bed1-745e10441d9d | -4.52282 | -54.86449 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ccbe01b7-f6a2-3425-afb6-44c8983b42f0 | -5.71051 | -53.49223 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2961112e-1ce1-3760-9019-1e6d2a20a96b | -7.0201 | -45.29558 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a7f8acb-07d3-3469-ba1e-7dee4ea43d0f | -3.85229 | -51.11298 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e3cf07d-1c4c-3d6a-838a-630e231e536b | -3.89703 | -55.89208 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 77a55289-e2b9-3576-8fab-4cacf04efb38 | -3.59978 | -54.66976 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3771ce8-b97d-305e-85fd-1d9a676537e2 | -4.80865 | -54.67376 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14e4c281-2655-31e8-a72a-88bef79ac93b | -3.113 | -54.16598 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a689ffbe-71c4-35cb-8545-25ae78143e08 | -3.01144 | -54.10294 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cb6503a8-8030-319a-a230-8b565e782151 | -3.74084 | -51.20659 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5598e1d0-ccf5-3068-b99c-7e47019cac13 | -2.39103 | -57.89175 | 2026-10-09 04:25:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0c62db36-2ff5-3113-9b4f-4425fcae2427 | -4.57737 | -54.95357 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2e5eee2-7fc1-3df8-a2ce-08f3a725b304 | -3.25784 | -54.03961 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19f78aad-f28f-36c1-ab49-deadc7eec43d | -3.01776 | -54.05832 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f33f94a3-fbe2-332c-b77b-e7cc71b63762 | -6.96483 | -45.14021 | 2026-10-09 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfeb73cf-766a-3b39-bb2b-0dd2068d668c | -5.70352 | -53.46955 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 635c9890-932c-3e5f-b3dd-41899863f57a | -5.75612 | -41.67718 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0dd31039-0aae-3c78-8fd3-2b08c6625901 | -3.0866 | -54.30559 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52320871-1f83-3000-80d4-b8322374d500 | -4.9278 | -47.54038 | 2026-10-09 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d06ccd43-26b9-3f2a-9961-9dd8dd3424c6 | -3.53541 | -54.66591 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 31736329-c90c-3824-aad6-95541e3105e8 | -3.16395 | -50.44948 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a66d17e6-3c0f-3db7-a9d1-b83d736e5ba2 | -2.99659 | -53.846 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45fb4199-b7cf-3045-8d77-5ffe9f3e9d65 | -5.72229 | -41.76718 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 059c2182-2b01-34fa-ae69-bcc59ce313b1 | -5.69806 | -53.48106 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 844d0d31-c658-3753-8dea-f7916cf8a56f | -3.49087 | -50.49305 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d7fa453a-9ca6-3d4f-b9fe-de2f4199bc3b | -4.63915 | -50.95481 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 19975fda-ac45-3ea7-bb11-8cfb1d3cfbf6 | -5.87986 | -43.41672 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8055f0cf-d63c-3f0f-b2e8-a84310a690d7 | -4.61922 | -49.21542 | 2026-10-09 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 740e0968-cf7d-340b-94c0-dd5b16b3e0b8 | -3.30305 | -53.70959 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 76b3a777-7c88-3a66-8019-1babea962665 | -7.10366 | -42.5228 | 2026-10-09 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 2592b0a8-7001-3340-b799-cb6893d519c8 | -3.25527 | -54.02424 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f2108c5-74df-3c22-a8d3-d4dc09e0948d | -2.56946 | -56.17627 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9a385dd-5a99-3b48-8706-af9760ea0164 | -1.26399 | -54.68646 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 418635e2-f14c-35d2-bd2a-8fd2ee56e3f2 | -5.10716 | -46.22361 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 05c59930-0d49-376c-84b3-36dfe98115bc | -1.48345 | -54.52292 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 842af23e-97bc-3e15-b231-7f67ad86aa19 | -2.78428 | -54.07636 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ac952c2-3603-35b4-9dc1-e95a57fbe5ea | -2.75717 | -54.115 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f0deca38-a784-3d2c-9b70-9981e2e90789 | -6.00102 | -40.96389 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 96a20157-3559-3307-88ff-c3b6d3e31289 | -6.25673 | -45.32769 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cf05185-93ec-36de-ac6c-c17a6bb2f0b6 | -6.32794 | -43.83164 | 2026-10-09 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12b651d7-8137-34c7-b150-92b91057c7dd | -3.73583 | -59.44805 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8f20c5cf-9aac-36db-a78e-86e1dee20179 | -3.30194 | -53.7017 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 707f0005-9e4a-3311-be6e-60296045d57b | -3.56275 | -54.66712 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 432b2269-3ce0-3a5c-958f-d0a2a44f7526 | -5.30098 | -45.72166 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2761bf6-4913-3a5f-9aa4-084c97b9be1a | -3.35871 | -50.41351 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8407d6c2-35d1-357d-8c48-1c5b9a602f95 | -6.00461 | -40.9682 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ec2efb50-ee00-3da5-88c4-46717545caaa | -2.8479 | -54.12454 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66afb946-5f4a-38cd-b299-eb785ec18e93 | -5.70891 | -53.47309 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1bf7849f-5871-3976-8264-ad6818e0fb37 | -2.34014 | -48.86847 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a32c1168-1eed-3b15-8f14-ad2be12a10f6 | -1.32369 | -55.4386 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63fce002-0874-3663-9df7-b3d207ea4592 | -3.08492 | -54.28342 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f4ffde5-3b27-3517-8169-7235c86afdeb | -3.72122 | -54.22457 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7af9bef1-2d67-3a02-a507-241ad9ceee05 | -3.70088 | -47.68216 | 2026-10-09 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 275d21fc-36d1-34a2-9c62-4548b1610b32 | -3.28145 | -53.82959 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README74.md)
