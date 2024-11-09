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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d5a94ac-b275-3527-b937-0c9fe0885571 | -4.03183 | -47.14184 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dadbd985-c3b2-3fa9-bc5f-fdbfd22807ad | -2.94012 | -49.4327 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b74ba92-6dce-355c-ba1c-33971eb135a8 | -5.55561 | -45.82922 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 226ae1de-1446-31d6-a020-198146bb539b | -3.18358 | -50.59027 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c8fde9a-f92f-3bf8-be17-0526498c5598 | -2.18647 | -53.6279 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a337418-df67-30e6-8efd-9abd5aa11635 | -4.11506 | -46.91108 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bb68aa3-07b2-3a45-a4db-9c1cdbfc6372 | -7.12798 | -49.28713 | 2024-11-09 04:33:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f5c61626-1ada-343f-87ee-38f12c8419f0 | -3.97106 | -46.98436 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1298638-4252-3e6f-bea8-8b74f84b554c | -3.17279 | -51.30981 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b686a2ae-adbb-3e09-b263-3fad1abd5935 | -3.04744 | -53.27847 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb51042a-b4ce-3caa-b540-366aaeb4af50 | -3.24741 | -50.44576 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12678574-65a9-339e-b4a7-e6630bbb8a06 | -2.69611 | -51.69339 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e51f75c-7008-3700-8801-1ea00658faad | -2.65137 | -49.88022 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 510beda1-eab0-3bae-9e46-5ec08dec0da9 | -11.08113 | -43.33781 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| b1cace4a-e298-385f-a552-3d0121712318 | -5.9332 | -43.65857 | 2024-11-09 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08225f14-f191-321d-a1bf-bbce44662774 | -4.4155 | -45.93951 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59db5ab5-e11e-30b9-9024-3cee65c1e511 | -6.18125 | -45.44785 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 14e8718d-5acb-3c9f-a546-d44b23dcf530 | -3.17767 | -50.58068 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3182ecda-2711-3d39-a54f-f39d4551089a | -2.69221 | -51.69277 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ff99a7d-8169-3ad8-a326-150ee8daeab7 | -5.13448 | -45.80829 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82a09fe1-163a-336e-9ee3-04ceb16e840c | -2.91518 | -51.0507 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c8cea91-9e58-390b-84b3-d1a278d69aff | -3.98073 | -48.14251 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb6549ee-c782-35f7-8d86-d454a6fd53c1 | -3.79766 | -49.94407 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d79329de-b5ee-3a10-b33b-8c502e295d83 | -5.84061 | -46.23671 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13b78cbc-e2fe-3e1c-b12f-71360323b99e | -3.53721 | -51.59919 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b596c65a-01ec-3d64-8637-04d4cc5ddbd3 | -3.34371 | -50.36223 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 606a08c9-f884-3f66-9785-a216c05832ff | -4.58804 | -37.80973 | 2024-11-09 04:33:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6131173a-121e-3a61-b5b4-d1cae9f6d57d | -4.21757 | -48.54109 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d160d85e-7a90-372d-b054-6206b5f031a4 | -8.84867 | -47.6771 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35d4984d-897e-3215-9cfc-f1ca665b458c | -4.11414 | -48.50692 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d65c71b3-dbab-349f-a47c-2fb8b7a569e9 | -3.87249 | -46.43546 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c5b9249a-1919-3ee2-ae35-af8ac5efae66 | -2.3602 | -54.74858 | 2024-11-09 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3ee82a7d-3c40-34f5-837d-d8622125288d | -5.72768 | -47.71807 | 2024-11-09 04:33:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3809f53b-a1f1-337a-a399-e57cf649c91a | -3.97721 | -48.40256 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 325550d8-b924-3608-990f-e38026dafa0b | -3.09888 | -53.31562 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 181deb8a-4faf-3a31-84d5-1cadb08425ce | -4.11729 | -46.91851 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f799ec50-f101-38c1-92f2-444e59011947 | -3.73968 | -50.44641 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d5143b3-cfb2-34bc-8aca-a6608d90957f | -2.61061 | -51.74891 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a087d45-8ddd-3b74-ac96-231c01dada80 | -2.8027 | -52.94643 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29b0a0bc-8fce-3b72-af8b-4606aab050d9 | -2.65655 | -49.89322 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ff5f1d5-13af-3ef7-8482-a823c8ffca55 | -3.25291 | -46.46098 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84bc7bf9-4ec5-3a1e-9639-1147cb18a7d4 | -3.24838 | -53.40231 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 894b836b-30bf-3e00-8cca-eee69d6a0cc0 | -3.03851 | -50.36811 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14de0384-4a5a-36f7-b2a5-17e3990bdb41 | -4.1119 | -48.49937 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 71147c62-861e-3a6a-b97c-939f8beeb887 | -2.92035 | -51.04231 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01faa029-6cd2-32d4-8be7-3d1085fd9546 | -4.86777 | -45.67052 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c8ca09b-69ba-39d2-bead-e31be9a9117a | -3.06388 | -48.06608 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4a4c075-3a04-3e69-8b87-8284ee6ba097 | -3.6369 | -50.75638 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dbeede4-7587-33b2-b1db-5c8fc257d644 | -4.3976 | -50.97267 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f07d2f52-9086-3ee1-a2bd-7a6e2ca9eeb8 | -3.59347 | -50.27478 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2b5508e-da71-3413-9def-856aa7b14bd0 | -4.89696 | -48.56882 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97284bfb-66ab-30eb-b047-f8fbd3678d8d | -2.18576 | -53.63232 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d257f4f-b4fa-3a38-8b56-1d34e3033fe0 | -3.03265 | -53.27304 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 062afce5-97cd-3ee5-a0b7-3206f93a05d3 | -2.92441 | -51.67409 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 05469c04-bd28-3df3-9b5a-d8ad1c7e3d93 | -3.84588 | -46.89369 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d671672-52ef-39ce-9013-86a9f0aa3bdb | -2.63058 | -54.66019 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8df3d7d1-0ccd-3d87-a301-52b537990048 | -3.65173 | -50.1359 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61c93a3c-a3b6-3218-8c89-245278da810c | -3.2028 | -46.52083 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f4ad3dd-4af1-3846-8718-f016082d154e | -2.15527 | -53.65049 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| abac2da9-0ed8-3270-9760-9efdc55101f4 | -2.95682 | -53.72156 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 399a859d-d4a4-3574-b32c-33b827604e4d | -2.36057 | -54.75066 | 2024-11-09 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8940b780-ede6-3d2e-b539-9fe2eb3ef3e6 | -2.87154 | -49.37932 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76bc4912-b519-34b6-87f9-2b8747b8bef5 | -3.76365 | -51.76215 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a3c10c05-f4b3-348d-be0b-050b4ff6b398 | -5.41733 | -47.57049 | 2024-11-09 04:33:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8164505a-a251-3fb3-893f-449a316d71f9 | -3.24464 | -46.47039 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfd0528e-73de-389a-adf6-7ea8e5d22734 | -3.22486 | -50.3787 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3a1847a-95ab-36bc-9283-5ee8c0623c24 | -3.1685 | -49.10086 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93a87402-d0ea-356a-a54e-3054ef8c7043 | -5.96 | -45.37957 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5227c459-050c-35a8-924d-8b8c61f55f9d | -3.14512 | -52.97548 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d7e433ba-7610-3d17-abcb-712d37b24535 | -6.27988 | -44.74141 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02d1a282-ec2c-302b-b252-5f07899ad4ba | -4.05675 | -46.93751 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dea2e168-2a87-3326-ab1e-87fdb21beee8 | -11.08527 | -43.34579 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 860bb938-cd05-3ade-9532-1f6e78b1193a | -4.24097 | -47.87215 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c34f99b1-2905-301d-a536-6455f14f6409 | -3.33372 | -50.17345 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7347fed6-7817-3637-8751-e7ade7ba2cd9 | -5.31717 | -50.5424 | 2024-11-09 04:33:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73c09be4-5c63-30e2-8c6b-ea5652dab9a4 | -3.26467 | -46.31995 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39e2c9c8-4759-3dde-844a-7a7afdb60a7f | -2.68329 | -51.8238 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a951c981-b334-3bcd-babd-af09844fa48c | -11.09008 | -43.33512 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 504ce43b-a189-34f7-938f-fb87283cbfbb | -2.64258 | -54.36621 | 2024-11-09 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b290244-22dd-30d4-8335-621a21664496 | -2.8459 | -49.2294 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a5132f5-01cd-3dcb-b13f-1db32b3c4287 | -4.20283 | -45.86315 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e490a518-81e6-3210-9666-a14ed53edfa1 | -4.05104 | -47.38766 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28955148-1152-3143-ac32-ccb0b1936ccf | -3.28627 | -51.5226 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb5804ab-05d6-35e5-a3a4-bbcaed3ccc60 | -6.53765 | -44.46683 | 2024-11-09 04:33:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3aec49f-4a93-3627-ad9c-24fa69f4fb07 | -3.98101 | -49.88868 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5f7dc7d-e6ff-3e78-841e-174ef8bf4c00 | -2.15977 | -53.65114 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 898ec253-0b30-34dd-9694-fbbc73529cc1 | -3.38874 | -51.46384 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1add32dc-ca9c-3ce3-b148-42321858a58c | -6.31266 | -42.7576 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3af2402f-7fd2-3d7e-89c6-9d368fbd1e07 | -10.04084 | -50.58266 | 2024-11-09 04:33:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cde784a-0a88-39e2-acba-611b57b795eb | -5.68783 | -46.43502 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d899b27-1b23-3c74-b093-35b33371c1a2 | -3.24314 | -50.44938 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f16479c-3744-36e6-9840-10c3e791ea35 | -4.3052 | -46.27457 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fbd624bb-69a2-3541-8390-3d1e96c4ac5d | -4.86625 | -48.11557 | 2024-11-09 04:33:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c4b5586-9230-3f1a-b684-2b86fbad4d68 | -4.23213 | -50.43242 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0203488d-33be-3190-b407-8ac20b7707a9 | -3.23954 | -50.44881 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abb783fb-aec6-36a6-a851-2091c89745da | -2.83708 | -49.4632 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a016d8e0-c2a1-305c-b5b1-d5b6787876e2 | -3.59702 | -47.35532 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| e3b1f35d-1eb8-30dc-b4f7-60c0eef44fd5 | -3.08575 | -51.22291 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa633776-a9e8-3db2-8d62-da63e63b3b21 | -3.07472 | -50.47549 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| adddf3a9-222c-390a-91d0-dbad640835c9 | -3.1557 | -51.12235 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README60.md)
