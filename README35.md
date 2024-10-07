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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c7165f7-97bb-3614-b75c-a83383068af5 | -16.6136 | -57.1555 | 2024-10-07 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.2 |
| cd2a3e02-ef9d-3bc4-901f-8fcc117c84c1 | -16.6332 | -57.1533 | 2024-10-07 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.3 |
| 24d43a75-083f-3743-8183-bf8f6bdc86f1 | -16.992 | -56.721 | 2024-10-07 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 662b11e7-b749-37ef-985b-51377aa97094 | -17.0116 | -56.7186 | 2024-10-07 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 1ffb90e0-6b74-399b-854f-8b6bf27e75d8 | -17.012 | -56.698 | 2024-10-07 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.4 |
| b0a86e20-30e7-3ee3-85fb-66c0dd7d4763 | -17.0685 | -56.8352 | 2024-10-07 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| 4930455a-be95-3a87-a454-fb434bd82b19 | -17.0881 | -56.8328 | 2024-10-07 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.3 |
| 55c69bc4-dc1f-3c77-9bef-d0d77a193758 | -17.0982 | -57.4267 | 2024-10-07 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.7 |
| 29323b20-7b36-3a55-8621-1a03c130be93 | -17.0985 | -57.4062 | 2024-10-07 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.5 |
| f06195c7-c75a-31a3-a8ef-eb8e6fe1588c | -17.0989 | -57.3857 | 2024-10-07 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 6aea91ea-b971-3627-be3a-e2579cbf032f | -17.1074 | -56.851 | 2024-10-07 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.7 |
| d4ad2861-d1f9-34e8-ada5-6e94f750bb5e | -17.1078 | -56.8304 | 2024-10-07 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.5 |
| 5fdc51a2-606e-3c44-9dfc-68c1c4efaf82 | -17.1274 | -56.828 | 2024-10-07 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.1 |
| cafbe65b-2106-32ba-9b5a-0d3430e6d655 | -17.1278 | -56.8074 | 2024-10-07 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 45acca38-5d42-33b2-9387-a8902e0d5411 | -17.1375 | -57.4221 | 2024-10-07 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 053601a6-e411-3ec6-a405-a6cf584bac24 | -17.1571 | -57.4198 | 2024-10-07 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 4aa68470-8584-3361-9d1c-94336ab3a3ad | -17.1581 | -57.3582 | 2024-10-07 02:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 14e4ea4b-abca-35ba-ba23-43bbc866d64f | -17.1584 | -57.3377 | 2024-10-07 02:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 65df99f0-ef63-365d-9047-768c67c6b491 | -17.6279 | -53.1094 | 2024-10-07 02:26:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 9e8172fb-f358-3ee5-96d2-a7aa1fd12fe9 | -17.6283 | -53.088 | 2024-10-07 02:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| b5b90f04-9f34-3b2c-8f2e-c50f1ed4f073 | -17.6477 | -53.1064 | 2024-10-07 02:26:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 5467e781-d6f8-3a04-80db-ecddd825a6dd | -17.6481 | -53.0849 | 2024-10-07 02:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 711efbaa-abfa-34d5-a9a4-ddbf64a5632b | -17.6679 | -53.0819 | 2024-10-07 02:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 693f3d33-4f98-3536-9f9b-5787dc96fce2 | -18.4518 | -53.5165 | 2024-10-07 02:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 6b26d1d2-9a09-3248-8b53-39fbcdd86cfb | -18.4523 | -53.495 | 2024-10-07 02:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 2e44015c-021d-3633-8a1d-f4ee77681988 | -18.4718 | -53.5134 | 2024-10-07 02:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 2eb9684e-5aee-30fa-bca2-d88442de7395 | -18.4722 | -53.4919 | 2024-10-07 02:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 96a1ee9f-26a3-3936-8ea4-63f521170def | -18.6391 | -57.2578 | 2024-10-07 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| d89945f1-cf52-300b-a7d9-97fe0758737b | -18.659 | -57.2552 | 2024-10-07 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 78ad0403-da64-3093-9055-2cf818e41d68 | -18.718 | -57.289 | 2024-10-07 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 28a7c44e-cbb9-3698-9ae1-a5e6c029314f | -19.2962 | -42.5779 | 2024-10-07 02:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 802b4309-a923-3b26-aa25-2bb427449d7e | -20.1223 | -49.0748 | 2024-10-07 02:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 5fc8ff4e-54d5-37f7-9223-51a4a14f45ed | -20.1229 | -49.0518 | 2024-10-07 02:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 230.3 |
| e21bb376-96c1-3316-a3eb-fb0bb097685d | -20.4655 | -47.6827 | 2024-10-07 02:26:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 7e05e12b-6dc1-3fa8-893e-0e52c9165ff6 | -20.4661 | -47.6592 | 2024-10-07 02:26:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 310.8 |
| 87f56ced-f721-3168-af7d-8cef1dd7e9b0 | -20.4866 | -47.6544 | 2024-10-07 02:26:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 145.2 |
| b918d372-c5bd-39ca-ad4f-c15931d09669 | -20.4449 | -47.6875 | 2024-10-07 02:26:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 87.3 |
| fe2f6a39-43c1-3fdc-8da9-68d2c5fe0392 | -20.4456 | -47.664 | 2024-10-07 02:26:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 68dad8c8-229c-3bd7-b997-508f698b543a | -20.5848 | -48.5137 | 2024-10-07 02:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 191502e7-653f-361b-ab17-a5d7d0d05bb8 | -20.5855 | -48.4904 | 2024-10-07 02:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 330.7 |
| 609793af-b978-3e63-9b3a-6721ae55fb7f | -20.5861 | -48.4672 | 2024-10-07 02:27:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 8d421a7d-d59c-3ebb-9f5f-5fc7440af227 | -20.6053 | -48.509 | 2024-10-07 02:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 106.5 |
| bd719aac-94a5-38d9-bbcf-a21961465e6f | -20.606 | -48.4858 | 2024-10-07 02:27:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 258.2 |
| 3562d08e-4db4-3484-843c-808b2c661c36 | -21.3274 | -47.5939 | 2024-10-07 02:27:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 5c20d42e-7258-386f-90a6-1c006798ca91 | -21.5843 | -47.9536 | 2024-10-07 02:27:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 474527f2-1297-301d-8020-f074b0f25992 | -21.605 | -47.9485 | 2024-10-07 02:27:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 779cd299-7eda-3ede-a025-67bd6684de69 | -22.1974 | -48.1778 | 2024-10-07 02:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 24157aea-70bd-305a-8eea-e19ccf875bd6 | -22.1981 | -48.1541 | 2024-10-07 02:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 4087a586-b71f-31c3-b970-7f07ba417f28 | -22.2183 | -48.1726 | 2024-10-07 02:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 865a4392-228b-33cf-9c47-1442e276771a | -22.219 | -48.1489 | 2024-10-07 02:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 88.0 |
| f70955c9-b91f-3f0d-a5cb-318e1d2377ef | -23.8863 | -51.8173 | 2024-10-07 02:27:17 | GOES-16 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 124.2 |
| 2b0dad67-b859-3ab6-b80a-47699a32fe1d | -23.8869 | -51.7944 | 2024-10-07 02:27:17 | GOES-16 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 107.5 |
| 67e830b5-5020-3a77-ab95-a119c0b26a19 | -1.0182 | -53.739 | 2024-10-07 02:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f110a7b2-24bc-3891-9b17-cadfa2a239cc | -1.0365 | -53.7389 | 2024-10-07 02:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 5af1ced5-92ec-303b-99c5-ffc94e48d4aa | -2.2113 | -53.7029 | 2024-10-07 02:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 15b78556-b37a-31c9-b3c1-b1d9c439c7f6 | -2.8569 | -52.9197 | 2024-10-07 02:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 3c5c8e53-75d6-302d-a6c8-730e4458ea0e | -2.857 | -52.8993 | 2024-10-07 02:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 9423f98f-d298-35df-9c75-c590a8eb3cba | -2.8753 | -52.9192 | 2024-10-07 02:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 0dad93cf-126f-3576-9366-1a523ea4af61 | -2.8754 | -52.8989 | 2024-10-07 02:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 59bd7322-e652-3c83-b9d2-5644b87a5e04 | -3.5381 | -65.0229 | 2024-10-07 02:35:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7b84700e-573d-3176-b05b-8bcece4bbe8b | -3.5563 | -65.0227 | 2024-10-07 02:35:27 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 5e88a258-c1a7-34fa-a516-3f8ee8fbde7c | -4.2728 | -43.7601 | 2024-10-07 02:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 213703cc-77e6-3752-9272-733ff8aaca27 | -4.2729 | -43.737 | 2024-10-07 02:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 4d62911b-be28-3f5e-9b02-daea52fd0860 | -4.2916 | -43.736 | 2024-10-07 02:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 6edbd66c-5b36-33e3-8a8f-42bdda0bee59 | -10.8337 | -68.3636 | 2024-10-07 02:36:08 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 60.3 |
| da865dd8-c6ae-3c23-84b4-c63e6e6726e5 | -10.8338 | -68.345 | 2024-10-07 02:36:08 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 05540a09-4578-3273-a27c-945e051263e9 | -10.8754 | -63.9169 | 2024-10-07 02:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b34debca-b537-30f4-924f-2a469b1e1913 | -10.8755 | -63.8979 | 2024-10-07 02:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 1e995dbe-3442-3588-a992-fab06a95d0a6 | -11.2657 | -51.3898 | 2024-10-07 02:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| c942c7eb-6ef4-3a8c-9492-c461e9b7c1bb | -11.266 | -51.3686 | 2024-10-07 02:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| cd7ff631-509c-3910-bd26-9636478cd46c | -11.2847 | -51.3878 | 2024-10-07 02:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| a08578f8-a896-3e26-b965-9ed79801895c | -11.285 | -51.3666 | 2024-10-07 02:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 46d89764-9d9c-3a30-94ff-9bab4daa27f0 | -11.3037 | -51.3858 | 2024-10-07 02:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| fe02c5e4-baea-36e0-972f-f9eb68032430 | -13.7342 | -60.6471 | 2024-10-07 02:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e4922694-c5b7-3999-9564-60e99796508c | -16.4161 | -57.3211 | 2024-10-07 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 8e1ad7a0-7625-3ee3-a6dd-4e46b9036e39 | -16.4164 | -57.3006 | 2024-10-07 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 9d7411e5-234b-3c3f-83fd-8c9e663d5c40 | -16.4362 | -57.278 | 2024-10-07 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.1 |
| ae62368b-1cb6-3f7a-9c55-bed4a692d82f | -16.4365 | -57.2575 | 2024-10-07 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 37bd610e-87d3-3fb9-9e5a-8f1e2a931356 | -16.4948 | -57.2713 | 2024-10-07 02:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| cc9df820-616a-3ead-bc14-0002a77e148c | -16.5941 | -57.1578 | 2024-10-07 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 06099713-38e9-34fe-a292-e148c3348534 | -16.6136 | -57.1555 | 2024-10-07 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.3 |
| 58675f08-b842-3852-baf4-af6b6d66935a | -16.614 | -57.135 | 2024-10-07 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.8 |
| edfb940b-2ad2-3c72-a413-5a9ff1d81fe8 | -16.6332 | -57.1533 | 2024-10-07 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.7 |
| d172aeed-7f18-3794-bc1b-adb7854c030e | -16.6335 | -57.1328 | 2024-10-07 02:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.9 |
| ba6d9a1e-c074-3450-8a11-cd8a0f7ebd0a | -16.992 | -56.721 | 2024-10-07 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 2433d728-90c7-3e5f-9e3f-7faab3b43c9b | -17.012 | -56.698 | 2024-10-07 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 7bbea53a-8c37-3356-b33f-36a69906cd47 | -17.0685 | -56.8352 | 2024-10-07 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 9299cf21-d0d3-3736-b7af-bc278e27002d | -17.0881 | -56.8328 | 2024-10-07 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.6 |
| bd440e39-7a6b-3090-97dc-6048c47a326b | -17.0982 | -57.4267 | 2024-10-07 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| 16887fbb-2e5d-3ce1-a53b-4b7e06dd92f9 | -17.0985 | -57.4062 | 2024-10-07 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| d547d141-3b81-3a53-8416-9442b9ab82cb | -17.1074 | -56.851 | 2024-10-07 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 6e78dd76-3cb0-3598-8027-9d9e4b96e9cc | -17.1078 | -56.8304 | 2024-10-07 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.9 |
| 4bd79bbc-5f9b-31d4-876e-52e4af933454 | -17.1178 | -57.4244 | 2024-10-07 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| b37fe097-d206-33b1-991e-13af0002eff4 | -17.1274 | -56.828 | 2024-10-07 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.5 |
| 5e664bd8-b62c-3e15-9fd1-288a6a7c43e4 | -17.1278 | -56.8074 | 2024-10-07 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 930c336a-82bc-3f66-805f-087eec61892d | -17.1375 | -57.4221 | 2024-10-07 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| fddfe9b6-0020-3bb5-af99-a7224443e7f8 | -17.1571 | -57.4198 | 2024-10-07 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| 9f5eae2c-aa64-3314-bc26-6fd1efadb74e | -17.1581 | -57.3582 | 2024-10-07 02:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 3fa282ef-2989-3a5a-a1db-06a29e22f9ad | -17.1584 | -57.3377 | 2024-10-07 02:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| da7019a5-bc55-3d21-a262-7fc2d6b5fce0 | -17.6279 | -53.1094 | 2024-10-07 02:36:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |


[Clique aqui para ver as próximas entradas](README36.md)
