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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c03d342a-abd6-33db-b2bd-12561b3297ec | -3.59119 | -44.9284 | 2024-11-25 04:33:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47f4983f-d674-3b19-a85b-73e35738b6f5 | -3.2537 | -54.22751 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 465fba2f-1640-3a96-9bc8-abd2ba509cb1 | -3.24605 | -51.05895 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e8b7c34-73c0-369d-a947-c0f502ff1c48 | -3.53356 | -54.07981 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c843029d-43ae-3742-8572-cd2cc0ae2cc7 | -2.67775 | -46.25788 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f46dd53c-c783-33ee-9117-52548d10ff90 | -2.18964 | -52.12485 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06195509-96fc-3c5b-a2d1-68084d2d0cb5 | -4.29449 | -46.90522 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 204e0c22-7a70-3815-943e-43e204db9c62 | -4.24134 | -48.70408 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20e6cbdd-a88e-33f4-ba28-9db4a44400ee | -3.27286 | -50.55935 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 811b21c8-5ddb-3e45-bec0-94c5586603da | -3.26065 | -46.42323 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 846401fb-fe89-3785-bc33-f73247594186 | -3.50088 | -53.81555 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db8ca5e1-24d9-3a47-b90f-ed8414b5688f | -1.77187 | -52.70995 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33a8a077-7691-33d0-bf5a-4a6778dbd37d | -4.84274 | -50.80874 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ea5edd0-abc3-3d22-84bd-4b43b70ec98f | -2.73545 | -46.10163 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36f6e8f9-1ec1-30ff-b5cf-cb1300a43138 | -2.5854 | -54.22826 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0814b914-1bee-3d0b-ab83-d67c29cc18d6 | -3.8921 | -46.67135 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73140dc7-5bfc-3c2c-a975-510b78d024a2 | -2.98158 | -54.0834 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0d2ba02-0f6a-36aa-abce-a173bca15746 | -5.7567 | -45.90548 | 2024-11-25 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6c4d77f-ac87-3efc-b445-ae88c84e1e4d | -4.24748 | -47.99223 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55c3a60d-a9c9-3e50-8388-7d26b1e407fd | -2.56966 | -54.06095 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb679034-8fc8-3e7f-8b9b-99f1f10f46e5 | -4.16528 | -46.8172 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fd6f2d6-4aaf-389a-be3b-2482f436a489 | -3.23092 | -54.22396 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cf0ab7d-f03e-309b-b673-e06bee60a0b3 | -1.80407 | -50.90527 | 2024-11-25 04:33:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54e88295-948c-300c-9cc7-801167102950 | -2.51966 | -46.22306 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 267ab1fd-dd84-33fb-9d29-95d06fed3906 | -2.33748 | -53.86798 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7ac4c0b6-6482-31b0-883a-ceb3a2f1242e | -1.77364 | -52.72607 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa7dd939-50af-3364-9bd8-6845d98164d4 | -3.36762 | -46.6544 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77b8cf3b-a230-3fc4-810d-530de737c194 | -3.47755 | -50.43378 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e57238f-f8b2-3936-bb3f-494a8f075035 | -1.73727 | -52.79213 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08f6c3bb-3e41-3db7-aa99-93f852b1349f | -3.17312 | -46.54926 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26f94cab-86b5-3b05-b956-51c03ad9dae4 | -2.81995 | -51.30143 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ecebd852-c67a-366d-b2c8-2dc40ebd5259 | -1.49398 | -52.51843 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 377926cf-5030-3e20-a1f4-e5d991a1469f | -2.57515 | -53.96699 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bbdc135-15e1-3721-a201-a98076803012 | -2.79554 | -53.00892 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfe27a78-3ad0-3ddc-999d-29f3ed82c57c | -2.81589 | -54.11302 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9a0375e-051c-334d-9be4-70607c0ed6d4 | -2.5375 | -46.39378 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8a39d90-f60d-308e-b238-7cb77651abe4 | -1.77425 | -52.72219 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a1da0f8-9fee-3706-a0dc-1838a600f90a | -2.71677 | -46.28947 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a0ad10c-ab05-3ea6-95e8-fe596a79b3ef | -3.09817 | -53.73781 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cf2ccb1-ac7e-33ff-8303-5325dfc5f2d2 | -3.55346 | -54.57816 | 2024-11-25 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38f47c8e-57e9-336f-8a0e-252b6e7c0002 | -3.94018 | -48.15259 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 777cd13b-62ce-3752-b3f2-a65da9b27548 | -2.9033 | -45.37019 | 2024-11-25 04:33:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e67e3737-1c28-31db-9d10-7836f772faf8 | -3.94879 | -46.89778 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8425d24c-8c5d-3607-af23-312373600ca8 | -4.22795 | -48.65877 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a618159b-b771-38fb-aa02-0f5f4766b597 | -5.55604 | -46.18881 | 2024-11-25 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba2397ee-75d0-3142-91e1-b291f62fd228 | -4.37062 | -48.57372 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13dc4f4e-ff34-368b-b3a0-e2709a56cce5 | -4.36897 | -48.08521 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83198991-6093-3a11-9bfe-90e08eecc53b | -5.91196 | -45.57477 | 2024-11-25 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 663fbae3-59dd-3f65-b618-3bf1079c0794 | -3.27518 | -48.74902 | 2024-11-25 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aad5c008-75ec-37b6-980b-49fd247f9529 | -3.93988 | -46.7144 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14fd7a3b-8cf8-3fbe-851e-dc561f6c92f9 | -4.95596 | -49.99867 | 2024-11-25 04:33:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a38fa044-fd97-3839-b902-bcfbc2ffbb52 | -4.58572 | -46.09116 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 84087fbb-2757-3e5f-8b28-ab9d88669d68 | -2.82083 | -54.71666 | 2024-11-25 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af180115-39d0-3cd6-acc2-a7c21e24b1ed | -2.43262 | -46.67559 | 2024-11-25 04:33:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1588a86-0ed0-328d-b04e-5041e9bd07dc | -2.69224 | -46.27445 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39de9931-58a3-3334-8864-1fed2a1d1756 | -4.19763 | -50.6914 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 777714e2-882a-3779-ae6f-1345a8a2efa4 | -3.52915 | -53.11449 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb13dcac-07be-31bd-9016-d06bf28f4416 | -3.23188 | -45.92613 | 2024-11-25 04:33:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b7b6595-1737-3984-9e01-9c27c4443997 | -2.7949 | -51.67872 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6aabde2-17b5-35d6-8ac7-d75a7cb2da40 | -3.24534 | -54.22144 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6559928-dda5-3af4-b0ca-d5a7f8f91c62 | -4.22739 | -48.66228 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 957ccefb-5d70-305d-8208-6b6092e4191e | -3.78247 | -46.93877 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4116bcf-8b4c-38c3-be93-c3ca9be02bec | -4.16193 | -54.57602 | 2024-11-25 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b6746cf2-75a5-3d47-a187-99d965ffb142 | -3.8496 | -52.15265 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9c4c3759-2256-3506-9eb1-347243991837 | -4.7779 | -47.84311 | 2024-11-25 04:33:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07d21ac6-2f26-3be6-8f7e-f0d0d7783faf | -2.99442 | -46.91157 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0dbacf2-ffb2-3db8-8a49-d9cf15d50ff4 | -1.45093 | -53.40176 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea5e9c3c-54f7-3347-b846-04a87051fe7d | -1.62493 | -55.17394 | 2024-11-25 04:33:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 83d0631a-a3b5-39ab-8ece-61a404e38939 | -2.68228 | -46.09664 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 201c31b9-4dff-3372-b700-6a0e19d43862 | -3.50455 | -53.82072 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2b72b7f-752f-3968-b6bb-a9eab1786a05 | -3.54334 | -44.92941 | 2024-11-25 04:33:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adcf3ae6-d716-3edc-9a9a-c6d171f73e30 | -3.2159 | -51.42254 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4328ac5-1710-3aa3-9b42-70138ee18461 | -2.6812 | -46.8908 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48ccf3bf-0931-37b0-b358-e786d7783c0c | -2.67163 | -46.25336 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ad2ba2f-e8c1-3549-a9d9-5dd3f783625a | -5.28932 | -46.16407 | 2024-11-25 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8281b7f-f34c-3984-ab44-aa6402c9a87c | -2.55656 | -46.55655 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ab3e9ab-5e50-33cb-b7de-a569268dda97 | -3.94987 | -46.89085 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d02ac169-af18-3a77-9a79-e6b3cb268a6f | -7.57301 | -49.40587 | 2024-11-25 04:33:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ffcd9d9-6f68-363f-8835-f5d0af4c119c | -3.80495 | -46.59719 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d38080a-c40a-37f7-a048-a40e458f04c1 | -1.35103 | -54.6311 | 2024-11-25 04:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8ecf3b7e-715b-386c-9bd1-dbb4e793640d | -3.84342 | -49.95805 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23c33fb6-a020-3914-a02c-7f492f36d431 | -3.31884 | -54.09489 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afee53e7-64dd-3560-9ec3-028db6f1d671 | -3.52339 | -53.78844 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc2578e1-142d-3b46-9c9a-7af666b51fab | -9.48599 | -47.71379 | 2024-11-25 04:33:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bf995d1-ffe0-3846-8b24-4a0b4f0b587a | -3.25222 | -54.23664 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8696ee57-4b5e-3c49-92c3-87220c5c33b4 | -3.15172 | -46.59937 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3de7295d-1c3d-3756-9c77-ecfbb45bed2c | -3.16023 | -45.48018 | 2024-11-25 04:33:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7aeb1ca5-c51f-357e-b056-6cb7356957f9 | -3.38763 | -50.7312 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba155a63-d6b8-344a-a470-2ee2fcd1a0a6 | -2.52217 | -46.29507 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c21f9929-dc9a-32e0-9e39-89e5aedb5e10 | -6.72929 | -43.56312 | 2024-11-25 04:33:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a247533-2512-3878-8271-b31bb4faacbd | -4.65203 | -45.35559 | 2024-11-25 04:33:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dccc1e89-b058-3435-9411-e54c6a93b1a5 | -3.72747 | -51.18607 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e9f2f10-e97e-3253-ade4-038a300ac2c3 | -3.94592 | -46.69748 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df8deeee-adbb-3c6b-b911-b7f94b835bbe | -2.90273 | -45.37388 | 2024-11-25 04:33:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7cf2a93-2714-38e4-9737-41fc5af5cf16 | -3.29234 | -45.73599 | 2024-11-25 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 10c25f5b-2c48-371f-8adf-a982122a5a98 | -1.77724 | -52.73059 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a888a2e0-2219-3e6a-b251-b4b60b10515e | -3.97711 | -49.96976 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a9d32ae-7f22-305c-8533-a35a4c4626cd | -2.82954 | -54.11518 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c13fafc1-d631-31b7-b29d-9f5dff7e750c | -4.26022 | -48.67096 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e0d14991-11a7-3794-ba19-ee76c37f8feb | -3.67947 | -54.5868 | 2024-11-25 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README19.md)
