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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ee5508f-0a4c-3a0f-a312-6f677c3c6eb9 | 0.19284 | -60.6138 | 2024-11-27 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76f91bc2-b1e9-3093-b5e8-fb3dd420bbce | -1.78778 | -52.74445 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f130030a-a810-3739-9101-ed5a5715c0bb | -3.51353 | -50.30716 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f8e1d014-ef8b-32e3-a8bd-634fd84cf192 | -2.24876 | -53.63062 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04211e89-da3c-3d0a-9460-7a55a6d2bfbb | -3.11339 | -51.2581 | 2024-11-27 05:35:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1bdad481-99ad-3e4c-924f-973c8c9c187c | -1.99304 | -53.29661 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d6c1ff0-cee5-302f-9008-b2937cc78665 | -3.75084 | -51.59424 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e172598-6b07-3273-9aad-3475fa4908fe | -3.59237 | -50.36116 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1393683e-6eb5-3ff2-a226-37a885567aac | -1.76248 | -53.62735 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 871e2af8-a06a-3f5a-b772-45c42be97990 | -2.6101 | -54.24646 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32520cdc-7b1b-35a6-bca3-5ec0f367150c | -2.82666 | -60.11247 | 2024-11-27 05:35:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8752ace1-ae2c-3385-b04f-c9c6c1f7637d | -3.09197 | -53.2592 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| e08f471a-fe3c-31bf-a3bb-c303c283b336 | -2.2529 | -53.62768 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9395f5a1-e93e-3b1c-b3c3-709cb99f4801 | -2.80942 | -54.13448 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eed78e79-f625-3239-ba00-008a6fd4cf90 | -3.24172 | -50.14285 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bc33807e-d1ca-3a1d-8f63-7fb807cf0bae | -3.27139 | -50.62494 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58e1a4bf-68cb-3b00-8dbe-aac1c5ebdaad | -3.09114 | -50.35548 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07db213e-5d3a-3f0e-a2dc-cdfb5d0a8707 | -3.71704 | -51.80373 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34e8d887-5beb-3da8-a427-2601565c6dc3 | -1.98808 | -53.2921 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74d57be2-b801-320a-9fdd-eb42a1e92a55 | -2.59871 | -54.21273 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9bf2dd9d-ee1e-3d59-8500-1eb3c822b41e | -3.24562 | -53.63839 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da022e28-702e-307e-a205-bcb124e8e98b | -2.60266 | -53.97225 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e544608-ca67-3ec0-8714-8b3749ebde7e | -1.99254 | -53.29701 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79a529f1-42c9-3820-bae5-8703abcb44a5 | -3.67273 | -53.68683 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d5b0134-75a1-3262-b5a1-b41620cbc5fe | -2.10967 | -52.77847 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e75064b8-002a-3fdb-9a01-c6bbcb38ae07 | -3.72274 | -50.18356 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ef54cf82-3556-3745-8793-0e3189bb536d | -2.59907 | -54.21168 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 315b4f46-43ec-3c5a-80e6-a9b5018e4ab2 | -3.11956 | -53.109 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df13be72-1573-3632-967b-e5dbdd193d83 | -2.82345 | -54.10699 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e29ea55d-dc94-3045-8754-eb2eebb7f729 | -1.04042 | -51.73949 | 2024-11-27 05:35:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 295082f5-ddf0-3ada-88f1-93138e2c5b56 | -2.96199 | -53.72422 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80436495-2da5-3e4f-81b9-f70d2edb1080 | -1.76197 | -53.63079 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c39da64-1075-358d-b640-9176dbc1ceec | -2.24282 | -53.63327 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9922f74d-fc81-3d77-ba21-7fb4b74267cb | -2.18094 | -53.77421 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1353f166-348e-36cf-b724-732b7d6c21c7 | -4.22035 | -50.85542 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd8e4595-4bc1-3047-9078-4810745d5fb1 | -2.73391 | -54.1328 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2889c22-b5e8-3dc5-92b5-d5be78dd769b | -1.69332 | -52.62021 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36eb502e-b642-3822-92f6-639ed1d322be | -3.09651 | -53.26762 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb3852dd-e73a-38ef-9fc8-11ff0738fa0d | -3.75717 | -51.59515 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7bf5500a-aa45-398d-8ca3-c1ececc1bbd5 | -1.04645 | -51.74051 | 2024-11-27 05:35:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe779c05-b732-3479-abbc-3d17a9b9c3af | -2.93972 | -54.79123 | 2024-11-27 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6aaa74da-77eb-33ca-bc78-306ba3837869 | -3.2882 | -51.1566 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e56e0dc-1426-3bd5-b184-9181a9494572 | -2.24205 | -53.6259 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b571c05a-6ece-31a8-8ce4-f1bc6dd0d84e | -3.28617 | -50.75742 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a20511a-a58d-338f-9f95-a2c88f97848c | -1.62941 | -53.8704 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2fa20a4-331a-362c-a95b-9de3b0c21acf | -3.59337 | -50.38859 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1cf414e-5165-3158-9ad9-9d64ff20e431 | -3.38011 | -50.11107 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 322b221e-1d27-368c-9c6e-724dfd8920d4 | -3.32967 | -53.72157 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a4b36dc-b73a-3ba3-ab14-acec9dd17853 | -3.50786 | -62.75657 | 2024-11-27 05:35:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4062172b-2432-313b-a46c-2ad91b671ad4 | -2.8331 | -54.11524 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e71d176b-cada-37fb-8687-38bd0c3ab8bd | -2.89519 | -54.17174 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daae7aca-4d8e-3d8c-b6be-ef859f29b5f8 | -3.31364 | -53.75529 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 247eb562-5d97-35e7-a0cd-af23330f311e | -3.25142 | -50.62163 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd3469f8-47c9-3527-b8b0-fc23c23c71da | -3.5979 | -50.35778 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 205a4914-02d7-37f5-bf42-e4fb01c6704d | -1.79409 | -52.7414 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc1a97f8-c7ab-358d-90f9-96934fb86096 | -1.17614 | -54.12696 | 2024-11-27 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ceb7e73-1238-3ac1-a85c-999006e4e419 | -3.4589 | -50.84394 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 593cdd9d-3f14-3736-87a8-aa1ee4acc260 | -1.34989 | -54.63075 | 2024-11-27 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 546ae1b2-1d75-3aed-a34d-a4ea4f10cc2e | -1.66638 | -52.72198 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1d2a0ea8-2db0-3e4f-b897-8ea3a244a3b3 | -2.15784 | -54.47083 | 2024-11-27 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f4ae67d-00a0-31f8-8317-444fda6f8879 | -2.80423 | -52.91029 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8090538e-97d4-3a80-afe0-3d68dfabdd55 | -3.53296 | -52.1561 | 2024-11-27 05:35:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 31620af3-4d0d-3e86-8c27-445203fb7af8 | -3.10377 | -50.36372 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e3b4aaa7-2c2d-3424-ab0b-b97fbab7882b | -3.69574 | -50.22334 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 81ad327c-0916-37fc-a9c7-1380f8ae4a10 | -3.67517 | -53.55059 | 2024-11-27 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 019dfc08-4b77-331b-a156-c09435f94fe7 | -3.51874 | -50.2247 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38df48d6-6bb8-34bb-ad11-3e6b2a7c3af9 | -2.89998 | -54.17585 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4478d57-2df4-3147-9d56-8ff1af17b902 | -3.10379 | -53.25715 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 104040c2-6a34-3d2b-9ca6-0dcea3c826c6 | -4.22626 | -50.86168 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1361518-f339-3d35-aa05-7500c56c394b | -3.91065 | -50.60184 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80faab34-eb1f-3b40-9b6f-1afb9a0514f8 | -2.88836 | -51.38422 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77e2a539-792a-31df-8c7c-889c33fbc063 | 1.43951 | -55.91177 | 2024-11-27 05:35:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7451eed8-6ad5-3e65-b044-c7e047fd0a1b | -3.25522 | -50.61683 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a53c8b5d-c045-37f8-9893-4fb6b0e00bac | -1.71939 | -53.60427 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11acd7e5-f5aa-399f-90b8-47604349ef73 | -3.90311 | -50.60657 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c1328ebc-17d2-3150-9164-3c9fe0cf38ed | -3.59109 | -50.35678 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| aee2fa3b-7e61-3c1e-be85-16e08dfe6699 | -1.66184 | -52.71316 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c19902e-e0e7-30f3-a4f2-c09d6778b866 | -1.3549 | -54.63148 | 2024-11-27 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6fdd55a-6213-3be5-91eb-05f13955e25b | -3.09253 | -53.25533 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 2ce7906b-ddb9-38ab-a833-551245bb848b | -3.45969 | -50.83838 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c836235-df1a-383b-9aaf-0dd96577c444 | -2.18683 | -53.77162 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dfc98b22-f6d9-3ce2-b814-677da45c820d | -3.69477 | -50.23003 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ba5db105-bea1-35da-b98b-ff2e59f79b3e | -1.7929 | -52.74929 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05dfd6bc-c11c-326a-86d1-ed5b627ca047 | -2.59858 | -54.21507 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 07dbf7a2-355b-349a-91a7-b31f0c39f14b | -1.79981 | -52.74231 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6bf03ecd-0cb8-3caa-8aad-86d58267b1b6 | -1.725 | -52.48801 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5756750b-459e-3888-aa84-902aa79413be | -2.74022 | -54.16356 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10c5c18c-e2ed-357c-9127-6c9ef5f6d4f5 | -2.59624 | -51.82955 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5154ce24-8540-317b-9730-3376d71f4b38 | -2.34259 | -54.3768 | 2024-11-27 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbcfaffd-fb8e-3192-8681-6d660d5b7b6b | -2.24748 | -53.62673 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 669ef198-67e7-3c54-acd0-f216d3ca90d4 | -2.60316 | -53.96889 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47adde74-e40e-3108-b1e0-0d1e029d6072 | -3.24856 | -50.14399 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb00e1bb-76fe-366f-8cf9-a9b2f3e8d5be | -2.7943 | -53.01937 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 150c2922-ac57-3378-b1dc-9f857b6549da | -1.76892 | -53.62129 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d398d427-01a0-312f-b694-2c14f65fabfc | -2.25344 | -53.62416 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a4fa5ed9-f383-3286-89f9-c840d2dcc350 | -1.62355 | -53.87329 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4226c74-297e-3f12-8931-381fbb80bdbd | -3.37229 | -50.1165 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0217b320-df02-343c-ba22-91707be3fcc0 | -3.51261 | -50.31339 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8dc9b5a4-4505-3cfd-81e2-2df143f3fda4 | -3.22232 | -50.91992 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e25f9116-0963-379d-b294-f16775c9da47 | -2.82538 | -54.02873 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README79.md)
