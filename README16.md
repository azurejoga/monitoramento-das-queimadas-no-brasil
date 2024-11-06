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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8175a244-6966-329b-9124-4a2e3296050e | -3.2053 | -53.2356 | 2024-11-06 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 2ab5951b-83ff-3f18-bd0d-315ad189daa4 | -2.1746 | -53.6834 | 2024-11-06 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| f3b1ce24-302e-35cf-8de1-37e76b5dd8ea | -6.5012 | -47.5033 | 2024-11-06 01:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 155.0 |
| a108dbcc-1075-3943-8242-c2b2a488e0ac | -2.8607 | -51.7937 | 2024-11-06 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 0d170efe-85c6-3925-bd90-d5c9216fa658 | -3.6788 | -50.2284 | 2024-11-06 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2aa6687f-ed7a-3676-abe2-5d5cf9b611b7 | -6.5014 | -47.4813 | 2024-11-06 01:50:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 278.0 |
| 53001464-fd54-3500-a1f1-8a136f01a5cd | -3.6603 | -50.2291 | 2024-11-06 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f6dc7bfd-a5fd-329b-a9de-3451048884a2 | -3.0607 | -52.5066 | 2024-11-06 01:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c8d4dada-31cb-3797-99f6-9704a65ed9ea | -2.8423 | -51.7942 | 2024-11-06 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f63308b1-d947-3554-a29d-f5c668e12ad1 | -6.5096 | -44.6618 | 2024-11-06 01:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| ee5c5d27-2be1-3cb8-a30a-aef58235e127 | -3.2348 | -50.3904 | 2024-11-06 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 46042031-b1bc-3f4c-805f-07d1ab5c1e05 | -3.5446 | -47.3855 | 2024-11-06 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| eec7378b-1345-3421-adb5-153fc11fd5eb | -3.967 | -48.15 | 2024-11-06 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 514a7e34-56ca-3d24-9316-ee57f2f5be6b | -3.2349 | -50.3695 | 2024-11-06 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| f27d642f-125f-33a4-8a37-824f5fb00f41 | -3.5305 | -50.3387 | 2024-11-06 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 2d9c0899-65cc-3ab5-a02d-b616a1e20ef8 | -3.2164 | -50.3701 | 2024-11-06 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c644b8cd-066d-3dc3-a4ab-fcedf7897d6f | -6.1039 | -43.9824 | 2024-11-06 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 2caf34dd-97df-31f2-b28e-0b3f63d59398 | -3.2054 | -53.2153 | 2024-11-06 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 1831016d-7d8e-3c58-80a6-22b904ee56e2 | -3.0213 | -53.2607 | 2024-11-06 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d56db2dd-f461-3f2a-8f22-29e14e798c76 | -3.2415 | -53.3967 | 2024-11-06 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 18e7a09b-25b9-3d19-9178-4eae56a080b8 | -3.0396 | -53.2805 | 2024-11-06 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 44a52cc2-2753-3b03-be3c-9d6131f8c758 | -3.0397 | -53.2603 | 2024-11-06 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| a74312ad-9a70-346a-91a9-10113528b1fd | -2.7427 | -54.1548 | 2024-11-06 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 94ddf288-0b61-3215-bded-e3273d7450ff | -3.0207 | -53.4227 | 2024-11-06 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 12c612f3-cfe7-3e3f-b488-84352e24980d | -4.1246 | -43.5833 | 2024-11-06 01:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| af2c5f29-1289-3a02-b502-f59087e910db | -2.8608 | -51.7731 | 2024-11-06 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 202.0 |
| 37215774-a5a8-36e7-a6b8-408d9c4cb558 | -2.7243 | -54.1552 | 2024-11-06 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 66f762b5-9db3-3b0c-97fa-ce5facd025bd | 3.6184 | -51.3162 | 2024-11-06 01:50:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c3f97f89-4218-3e96-b849-c39e8786cf9d | -2.7428 | -54.1347 | 2024-11-06 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 47f75a4d-4441-3ae0-9890-4e92e03f7ee2 | -6.1229 | -43.9578 | 2024-11-06 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 44ccdbec-a9e1-337c-8fe5-ceeb61780902 | -3.1433 | -50.2044 | 2024-11-06 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 70361c6e-799e-3ed9-83d0-9fc031b59fc7 | -2.6764 | -51.8395 | 2024-11-06 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| f7202604-d143-31d7-8041-8ab90c84de7f | -3.526 | -47.3862 | 2024-11-06 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 87494a17-dc74-3aa1-9063-f4230b65a03d | -3.0207 | -53.443 | 2024-11-06 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| db74c7f5-f7af-3608-a0b8-60cf7a3ea24f | -6.1414 | -43.9794 | 2024-11-06 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 52dcc3c0-8771-36b3-a634-2b5bee8d3c8d | -3.2163 | -50.391 | 2024-11-06 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8c7c8c4a-2c25-3a72-a398-53f77589e023 | -3.9669 | -48.1716 | 2024-11-06 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a7d03ddf-6fd6-3989-b78d-9c97527e39dc | -11.76873 | -64.98592 | 2024-11-06 01:53:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.7 |
| e7b60e27-6d00-3902-a85d-3e202c1229f2 | -11.77274 | -64.99059 | 2024-11-06 01:53:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 24.6 |
| fc90f9e4-da12-393d-9ffe-759e318d6a3c | -11.77136 | -64.97979 | 2024-11-06 01:53:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 16.7 |
| e1ae7c9d-d750-36f0-a2b7-27c3f2317cb6 | -2.71204 | -54.14086 | 2024-11-06 01:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b482942d-6e00-3f9d-a2ca-21de1001a988 | -3.74034 | -58.53282 | 2024-11-06 01:56:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ac75210c-fb73-3baa-a296-f6af0687bd4c | -3.59699 | -58.59372 | 2024-11-06 01:56:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 09756123-1ea9-314f-93df-290edbd0f454 | -3.59086 | -58.60116 | 2024-11-06 01:56:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 10e12181-b6aa-3f37-9384-bc4c905278e5 | -3.59947 | -58.61024 | 2024-11-06 01:56:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0652ec86-424b-3a8b-9ad2-c4999ae7e102 | -4.40423 | -59.53379 | 2024-11-06 01:56:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| fcbef1c8-0632-3a43-9b19-0830a0d837b9 | -2.71792 | -54.17816 | 2024-11-06 01:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| e0904df0-6a47-393f-affa-5864505a62c5 | -0.7441 | -62.90913 | 2024-11-06 01:58:00 | TERRA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3c00f0dc-a0e7-3039-879a-a760d5dcb3d6 | 0.3848 | -62.67463 | 2024-11-06 01:58:00 | TERRA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a3c88a79-4dde-362e-83bc-c9ee9a1d3461 | -0.74276 | -62.8996 | 2024-11-06 01:58:00 | TERRA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6d407e5c-91ad-3c6a-b0c3-2c868e04525d | -2.72632 | -54.14605 | 2024-11-06 01:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 6bf43b49-5e2c-3f68-bc12-7da888e0ae1b | -1.49037 | -60.37987 | 2024-11-06 01:58:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 808fd81e-153e-3fb1-a09c-cc7fa2c31fdf | -2.9185 | -51.0678 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| c189c00d-bbc6-3459-9ff4-543c0d1c1ab5 | -3.9669 | -48.1716 | 2024-11-06 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c585ff70-e048-323a-9321-10489cfe8ed8 | -2.8424 | -51.7529 | 2024-11-06 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| a421bd3c-3ea4-3b05-a321-73eb6aed3beb | -6.4906 | -44.6862 | 2024-11-06 02:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b55b0b84-3526-31e6-ad7d-ec0b8d10263c | -2.9187 | -51.0262 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| b82bbb4d-8d72-37ce-a044-62a75831496a | -3.0213 | -53.2607 | 2024-11-06 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| bd5ddc55-e918-3032-a6a0-c859c876d8d2 | -3.5304 | -50.3597 | 2024-11-06 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| e8155907-8253-3b6c-bf6d-87f3f788013c | -6.4825 | -47.5046 | 2024-11-06 02:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 5db997be-4dc7-32f2-ae45-762ec0200986 | -2.8423 | -51.7735 | 2024-11-06 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 76634f2f-c148-365b-9215-4d7de76d6be5 | -2.7243 | -54.1552 | 2024-11-06 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| cebc72cd-0bc4-3554-ad0b-f07bfe411a35 | -3.0396 | -53.2805 | 2024-11-06 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 42cedcc5-57fd-3d26-9b4b-6e30232d6ac2 | -3.1393 | -51.2069 | 2024-11-06 02:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 9347fdd9-39ca-3f9d-8734-dc817c0944ab | -2.1746 | -53.6834 | 2024-11-06 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| f71a8c54-e495-3fac-82f4-30b7d6beb7ee | -3.1616 | -50.2248 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 733b4706-f9bb-335e-89b1-e9ac18d006c8 | -3.2164 | -50.3701 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 0f18aa4a-00b1-30c9-adaa-aa7f397f6818 | -6.5096 | -44.6618 | 2024-11-06 02:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 662488a7-6197-366e-9b82-ecd16e343144 | -2.8423 | -51.7942 | 2024-11-06 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| c72a6390-fe91-3927-abb1-76e4a344a241 | -2.937 | -51.0673 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 33eab26e-d10a-3fee-b3b7-e716ac2f3ce7 | -3.0397 | -53.2603 | 2024-11-06 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| b16139b4-3cf4-3376-ae1e-dad1e1826cad | -2.6764 | -51.8395 | 2024-11-06 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| a9c5f10b-0317-3ed2-8f86-47d67ccefb1a | -2.1948 | -46.5296 | 2024-11-06 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 3b1b10e8-85e9-38f9-a2bf-714b9ae7ae3b | -2.1746 | -53.7036 | 2024-11-06 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 5c0af57c-43e6-357d-8df8-927d1d6d975d | -2.082 | -47.0602 | 2024-11-06 02:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 4679ed14-7e30-32ce-89db-1f701e715907 | -6.5094 | -44.6847 | 2024-11-06 02:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 45248580-91e1-3368-a624-18362ddd8270 | -2.7244 | -54.1351 | 2024-11-06 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8c608f16-1205-309d-99a5-4c27015129bf | -4.1247 | -43.5601 | 2024-11-06 02:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e02192e6-6911-3b2c-8b55-09fabdc57811 | -2.706 | -54.1556 | 2024-11-06 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 770259d8-5ec1-3d0c-bff5-cbbdda34bedb | -3.0207 | -53.443 | 2024-11-06 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a9ec7381-4b40-305d-9d80-adb0305a8ead | -6.5014 | -47.4813 | 2024-11-06 02:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 61d1080c-a3a5-3d7d-a831-19d185699024 | -3.2348 | -50.3904 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 76b10536-1930-366b-bab0-3cda51faaa6b | -3.0023 | -53.4434 | 2024-11-06 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| bf64b41d-241f-3eec-a4ce-5128b827d8fb | -6.5012 | -47.5033 | 2024-11-06 02:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 135.2 |
| a11e363f-23cf-38b4-9913-7fcc33a39579 | -6.1041 | -43.9593 | 2024-11-06 02:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| c57f88e7-357f-3824-962b-61147cd4a09f | -3.2349 | -50.3695 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 3ceb48ee-b709-3103-b6d3-f8d2e5d0cb02 | -2.6764 | -51.8189 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bfc747c4-6385-3f5f-a992-f8915c47e11f | -3.2163 | -50.391 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 58ddc379-9bf0-3c34-95ea-c97fb3c1a25f | 3.6 | -51.3168 | 2024-11-06 02:00:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 92.1 |
| bfbc501c-9177-39e5-9a49-995fa696b18a | -3.1617 | -50.2038 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| f15b6105-0d21-32ca-9447-56535522b0d9 | -2.8608 | -51.7731 | 2024-11-06 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 258.0 |
| 0eee8108-8816-3218-aab3-91df010d0810 | -3.0023 | -53.4232 | 2024-11-06 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a6e6dd09-24ff-3823-a386-f1ff099ac7b7 | -6.1414 | -43.9794 | 2024-11-06 02:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| c403d980-0812-3e1a-a47b-8476d651703e | -4.5614 | -48.0141 | 2024-11-06 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| b6c8f9ff-8ec5-319a-9c4f-63301162d96a | -3.967 | -48.15 | 2024-11-06 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| e7dbad51-b2ae-36a3-a6b0-edce9eeb3736 | -3.0607 | -52.5066 | 2024-11-06 02:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 34f392ca-7659-394c-9ed7-87dcd969b449 | -2.9186 | -51.047 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 7abd162f-f57b-3f47-a03d-2a7bbe57b4e9 | -2.8608 | -51.7524 | 2024-11-06 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 26655ace-4dbc-3c52-8691-f9b63956f1df | -6.1229 | -43.9578 | 2024-11-06 02:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| cfd12a74-d15a-3688-ba98-eac2c0fd0c8d | -3.1213 | -51.1036 | 2024-11-06 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |


[Clique aqui para ver as próximas entradas](README17.md)
