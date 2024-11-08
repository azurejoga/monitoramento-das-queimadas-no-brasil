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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a99cfc3d-cfeb-3b52-9f38-6ecaea9e537c | -2.76982 | -54.04904 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ec24aa1-89bd-3cfc-8388-03acf120f2dd | -2.617 | -51.2969 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78533bd2-52da-3b4a-8d99-de19a0466414 | -1.23007 | -55.80811 | 2024-11-08 04:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7bbfd843-0644-3fa9-b175-1443090554ad | -2.68761 | -51.82887 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b4411c9-69b3-369a-9409-350d4757e775 | -4.21673 | -45.74038 | 2024-11-08 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35ebe3cd-7856-3097-b6ce-3e2e0bb03341 | -1.63274 | -53.44294 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46acfcec-d226-3163-beec-06771274671d | -1.22847 | -51.75853 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e349bbb-78b5-37df-983a-84f93bad9f45 | -2.30105 | -48.5837 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3770368-8318-3942-8f42-c92da3f09a44 | -3.00923 | -53.44411 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fe72b82-7f04-339e-a554-761c6f79c090 | -3.29145 | -50.02988 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1014c84d-5344-36d4-974e-bd7f01f1fe7d | -0.40239 | -51.49204 | 2024-11-08 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e61b0f96-441e-3e5f-8e72-5719faa99a97 | -2.55102 | -54.01155 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a42c913-8d0e-3cd1-a06e-fd87d89f5d6d | -3.79015 | -44.01798 | 2024-11-08 04:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5fc0198c-2da0-383d-9e4e-90a837bc7557 | -2.3102 | -46.48105 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58333340-b66b-3edf-bdde-5db60d631919 | -4.26731 | -55.14341 | 2024-11-08 04:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94c6a4dc-1fad-31eb-8f42-f3dd9f93d2e2 | -2.83195 | -48.46367 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5f6b490-20ad-3e16-a6ec-07283aec58a2 | 0.03433 | -49.43243 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 63c243e9-4323-353f-8144-c843a8636bd6 | -2.23611 | -53.67068 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b0b45db-4c1e-37fc-8944-d55245309720 | -3.37415 | -52.35543 | 2024-11-08 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 900eb0a6-2ffe-33ec-8b90-ebdceabf4acb | -1.25841 | -53.34782 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87397ecd-8607-3572-a2ac-ad7baa7b9e50 | -1.61597 | -47.34937 | 2024-11-08 04:53:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d535b9ce-8df5-3ede-aaa0-17d306632f79 | -4.68225 | -46.41127 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 96f126b6-b814-3264-bc10-340b3005a934 | -4.23988 | -48.02502 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf951ae4-53be-3465-a62f-f9f8e0e92e12 | -2.10494 | -51.08966 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af845c4b-f30e-37eb-876b-53bfa57506b6 | -2.77221 | -54.03403 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c64022a-253f-3863-a38f-e3a90272cad0 | -1.65768 | -47.91068 | 2024-11-08 04:53:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| df74af47-7d84-3356-9d85-2a528f7926d8 | -1.34524 | -51.42583 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6d7f5f0-60fb-327c-bd11-904d1619bb66 | -1.87481 | -48.77108 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1938b0e-e9f6-3183-9548-c21bff73328f | -1.50582 | -52.16097 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e76a9c94-476f-329e-ae2d-9974453b19ef | -3.93873 | -48.35305 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56cd9ea2-7d7a-3dc0-8a03-04bb179098d6 | -3.07248 | -45.74532 | 2024-11-08 04:53:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57cf53a3-4d62-3842-a73d-4d47493ad9bc | -4.48719 | -48.49057 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eedfbfd9-d136-3efd-8208-c4b5e110388f | -3.18386 | -53.85048 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3249a7c7-6114-3282-a181-097b41277293 | -2.84068 | -53.97948 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 173abbb4-8e6b-3063-8718-350f2557495b | -4.6165 | -45.7108 | 2024-11-08 04:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aadcf331-dbc7-3e5b-ab86-6e89f8a17d64 | -1.45455 | -54.31028 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cef6580b-8479-3be3-bff5-2716d3fe3b09 | -3.36441 | -51.85052 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3abb3817-3759-31d1-9e40-8602c60fff9d | -1.16448 | -53.72364 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64ec2ae6-1edd-3bda-96c7-a53d9fa81acb | -2.73174 | -51.74083 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d9effa7-36b0-3574-8f41-073f41ebf0e7 | -1.71086 | -55.15779 | 2024-11-08 04:53:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8719693-29f7-3762-a3bd-0397b8192a11 | -2.18046 | -50.97692 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 270bc176-725a-32e2-a56a-236473e1fdd3 | -2.81241 | -52.94495 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3126698b-5637-37e6-a45b-6e0cd810a7ec | -2.80962 | -52.94094 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9ba092ae-74ae-348d-b45c-3e3c5e29e41b | -2.29621 | -48.55836 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f671ece-f6ca-3b76-b4e7-d1bb6910f03e | -4.28605 | -45.69405 | 2024-11-08 04:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb9f711d-7035-3a35-a6e4-eb8a9027bfd1 | -2.62254 | -46.15507 | 2024-11-08 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eb4a16d-95c1-3b75-9c46-3792230d90b4 | -2.18389 | -46.46161 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 538e9ba8-6183-30fe-b9aa-9f001498033c | -2.61396 | -51.75426 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 549b125c-beb4-3339-b13f-8cc789fe01d4 | -0.16523 | -51.48645 | 2024-11-08 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1fa1d06-fade-3984-b68c-01727963e4d4 | -1.41316 | -54.50369 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 752f222f-e524-3b87-907e-b0f092e189f2 | -5.65989 | -45.2038 | 2024-11-08 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9378894-4ff2-3b49-9462-a8e19b10d1d9 | -3.71794 | -53.39725 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 746574ef-1818-3d95-bb38-4ad31b858fcb | -3.02242 | -48.08093 | 2024-11-08 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e93f8fb4-7d17-32eb-ba44-371ced5056a8 | -3.22016 | -50.38306 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31c50948-b76e-306b-b592-eff1be921bb9 | -0.43854 | -51.82791 | 2024-11-08 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72660201-3e4e-3c19-8229-038405de911a | -3.53995 | -47.35851 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44fafd3e-18da-36d2-9ab6-956d760151dd | -2.15256 | -53.66515 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 007c43e6-bebe-33a8-b513-b540a74fb1d5 | -4.21793 | -48.55777 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9321a1b-c0d2-381b-8ec0-3afe744b9aad | -2.25537 | -53.72653 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95e9d783-c7f5-3ebc-bed5-9bc149bc3971 | -1.33549 | -54.60812 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d2cb23c-3b44-35d0-81fb-8c1ed6aa02de | -3.01207 | -53.42612 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7db7c46e-401b-31f5-94b8-5ccc2ccfe308 | -3.03396 | -53.26516 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c747956-e2c8-3563-b087-f058a8f1f6eb | -2.80853 | -52.94794 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c9369ba0-b07c-3038-b718-8169877f1221 | -3.09281 | -53.32134 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9a019d54-c377-3dde-a0ca-c579636e7f45 | -2.61978 | -51.30086 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b9ced19-7512-3c20-8976-d5d7c59be82a | -3.33471 | -51.62417 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7709dd18-2e63-3fc2-b698-7e17ba28b7c8 | -4.86892 | -42.95284 | 2024-11-08 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 925d06f1-76ba-3600-aa02-8da511b08dda | -1.42936 | -54.53967 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e8244ce-b6bc-3240-988c-9674d8cd1168 | -1.38136 | -52.26129 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46e6df97-3765-3b3d-acf5-05828d292e2c | -5.74352 | -42.00134 | 2024-11-08 04:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 13e3b088-4e3c-3328-aa29-c45d071ad15d | 0.03093 | -49.43296 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b513763-0805-35cf-8df8-7001be3051d3 | -3.03005 | -53.26818 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c4d099d-329a-37bf-b7d7-4e576ce3d4bb | -4.60981 | -49.57561 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13a5f2a5-fcd8-3bce-a89e-1aeff59d305a | -2.1044 | -51.09312 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c94f3d8-8dfb-3f9d-b68f-a8883939563f | -4.07195 | -48.31675 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b844d8bc-bc72-3c21-a708-15c05631fd05 | -4.99146 | -49.89954 | 2024-11-08 04:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 181d2e8a-8da5-3834-a2af-6845a651d259 | -2.95516 | -53.72102 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34876c10-f476-3c24-bdb5-4f15db648fd5 | -3.34389 | -45.36631 | 2024-11-08 04:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cae5e79a-cb5d-3c61-a9af-7350fb0dfa5d | -2.84137 | -52.90998 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88d43f40-08e8-395a-b8a2-850e2741332e | -2.83914 | -52.9025 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f16df7a-1621-35d5-9516-c98136cf0e07 | -3.93181 | -52.24904 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa5117f7-04b9-3dd1-b614-5c5d071ae9d1 | -1.38719 | -52.20207 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4e2cfe8-0281-3c37-9468-a28de967f74c | -1.1475 | -53.65144 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c7a873cc-a0fc-3ad6-b137-3dc10f9b9d57 | -3.13833 | -51.20387 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13bea55f-6a86-38b3-87dc-fd633f3d05d3 | -1.46184 | -53.41637 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 578bb871-3c31-3f40-a389-b9e79ca5279e | -1.82167 | -48.57641 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c857029-0104-3d11-bb8a-2d4068fc3b43 | -3.35044 | -51.67945 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f351f54a-467e-339e-af6f-4d4acb6bb1c6 | -4.52152 | -45.68573 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 775ca1b8-33b0-3e4c-a8c5-8d8727e4caee | -2.15205 | -48.82682 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a95787a0-edac-3607-90f0-f40dceb6fe3a | -4.52218 | -45.68125 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1b27c2ca-3594-35a1-92cb-a6afed4d1680 | -2.66482 | -52.45159 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ed14756-b1b8-34e3-a329-8c35b164a729 | -3.79929 | -44.02505 | 2024-11-08 04:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7de3727a-2649-32df-b51a-c6303586cb44 | -2.6079 | -51.74981 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60e3a70a-506b-391a-b531-642504112d66 | -1.14808 | -53.6477 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e386bcfd-dba9-31aa-b936-afc027c90819 | -3.33112 | -53.19187 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca818625-4934-36f9-846b-41dfa2bade4e | -3.8064 | -43.60014 | 2024-11-08 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 036f2388-e38a-3d7c-9b31-a31e3fdfa7c9 | -2.27725 | -51.14157 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9062008-8fe0-30b2-bf32-b350bb863e2f | 0.02066 | -49.412 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ed203f66-f711-3772-9d07-0c0cdc6f52fb | -3.11311 | -53.71895 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e88b834-ef56-3d1f-9eb5-ef793919450c | -2.80676 | -51.80583 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README33.md)
