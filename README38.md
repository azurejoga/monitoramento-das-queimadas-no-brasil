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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3b76d84-8220-30c0-b219-d951d0535b17 | -3.81674 | -51.99648 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9dda8778-e542-3b87-9521-fdc2069cdbc4 | -1.10175 | -53.61967 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a942b728-f364-3cc4-9429-fc88d435cff9 | -1.28739 | -51.73427 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 999551f5-8873-3eee-8625-af9c76583e6e | -2.82281 | -54.0997 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ee2d0d3-17e0-32d9-b24b-862571cc2c73 | -3.58954 | -44.92503 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1acd879-3b93-3c67-8113-e11ea80a6588 | -3.5841 | -52.2322 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa1336cb-c469-3034-ab1b-91c49bb0c02c | -4.36527 | -48.57093 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3756f90e-17f7-3cfb-b880-9063e35810ec | -2.77413 | -54.02422 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4a1c51b-26c1-3dfb-bc8a-52574f0cb128 | -5.91153 | -45.57362 | 2024-11-25 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 818cafc8-894a-377a-8dfc-34b442db19ca | -2.86041 | -53.96986 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f353f116-8f57-33a3-bcaf-79df44b5044e | -2.35593 | -53.71304 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0263df31-a3dc-36c3-b567-edcb44a110c5 | -1.24144 | -51.74167 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98d827ba-f968-3dc0-9480-56ba930196df | -4.24586 | -48.67134 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5cdf8a18-fe10-3679-998f-d9eb614d7469 | -2.1434 | -51.04437 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db24a589-9c0d-3665-96d0-5c4145a8a854 | -3.11351 | -54.14182 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25346630-ba92-33a6-acc0-67620c3ba363 | -3.2229 | -53.83836 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c40775aa-26cf-36cf-839a-9e7eb185f3b1 | -1.14499 | -51.68694 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 492dd498-a31b-39ae-bce2-0e9fed81745b | -3.51287 | -53.82376 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 470535ca-2e7d-38b1-a1fd-b6a54b0187dd | -0.92596 | -52.65231 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09850fa8-e5d1-3563-8254-fa88547f7ff9 | -2.80994 | -54.02976 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 350c3a03-1534-3e8b-bd3b-e3ffa67ef733 | -1.6117 | -52.35894 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0cfbe0b-67d5-3957-9a42-68b9fb39b355 | 1.71008 | -55.82138 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f73eff6-6047-3883-95ff-bdbf78c9ef32 | -1.62206 | -52.43851 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1da9e6cd-e3b2-3778-b74b-b6159bcf458d | -2.24969 | -53.61501 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 776e1235-5f03-3c03-b8fe-068a532798c8 | -1.65942 | -53.81433 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 066e2365-7334-388e-b54b-ca5927be86d1 | -3.10002 | -53.99705 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9e2b42f-7d2b-3d9c-84e8-a0bf49c0884e | -1.60484 | -52.27239 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0c75a38-ddd9-3ec1-97cc-b9fefbb2a645 | -2.62001 | -54.25155 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d6dcc74-4272-3508-a153-d144a54578ab | -2.60966 | -53.97013 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f20d276-4c80-3536-a086-886e75a8e560 | -3.06349 | -53.21605 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d13c414e-6d73-3c48-b78b-d636a55a5c2c | -3.34696 | -50.51479 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a6b93549-0a65-3add-a981-f4bb78cd962c | -2.59695 | -54.05043 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f587ccf4-1223-333a-9012-58b0371651f4 | -4.52143 | -50.57983 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0002162-a2ca-3019-a71e-4f384e2f83a9 | -0.93035 | -51.71947 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e8fb5d7-dee4-3eac-ac9a-777216afdd14 | -1.61264 | -55.12908 | 2024-11-25 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1407722-565e-3949-b72f-793b33234d89 | -3.32248 | -51.62736 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd565385-f93c-3f9d-b80d-050f34a91095 | -2.31248 | -53.59989 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 222849f7-1f12-3896-9f2d-a4469a730e79 | -1.13233 | -53.81066 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22f63c7b-ba1a-381a-b530-985ae71b94c9 | -3.51837 | -53.81044 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f4742e7-3260-3215-bc6d-5dd629668931 | -3.11166 | -53.75017 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdfaae60-4651-312b-b157-44d33e31eb52 | -3.45513 | -54.10267 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71d7083b-4e26-3134-a398-88815a2bc994 | -4.24456 | -48.59908 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ccde512-1749-331a-8b36-8c425513edf4 | -0.92913 | -57.59755 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 458a52e1-9c59-369f-ac88-cb735d8217ec | -1.60037 | -52.57695 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 43c9a989-e17f-32ba-8572-27248ec227b0 | -3.00351 | -53.23452 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f42c5ddd-68c8-3e7c-9958-04c412e0f03f | -2.0788 | -51.1187 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df977130-45fd-3450-8e33-aeebaa7c8b8e | -2.63391 | -51.74615 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b5abc16-319c-3f1d-b6cc-807b63c0c4f8 | -1.3412 | -52.24598 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5ba1666-25d5-39be-8ec7-0c5b8c65be7c | -1.28627 | -51.74135 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8433377f-699a-3fb3-8eda-73362a9833c6 | -2.81167 | -54.08365 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e1f246f-a1de-3f08-9f96-5423fff5fb60 | -1.1282 | -52.09845 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e7b2f14-c4a4-3648-97be-14f8476080a9 | -3.28447 | -53.83371 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74183914-7731-34f4-b04e-d06d8889e4f8 | -1.24298 | -51.62181 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10b823e2-1eab-3079-b329-3bd69441b0f8 | -3.77378 | -52.40321 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16b0126e-3df0-3cd6-9e38-592aebec2388 | -1.14949 | -51.70216 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d272a6d5-2053-34dd-bf04-c5f7369b23e9 | -3.62052 | -55.30246 | 2024-11-25 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b0fac24-9a6f-3b65-acd3-a45eea6c9690 | -3.05631 | -53.21846 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2840d571-32fb-3a05-ac78-39801e4b40ce | -1.44432 | -52.58124 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d446d1fc-11cb-3931-b92b-65f6cf3666d4 | -2.80169 | -54.12506 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b147c0fb-208a-3ed9-8feb-9e44960f90e6 | -1.15061 | -51.69508 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 735b7e6d-b54a-3e37-a499-e3c313aa07cd | -3.05084 | -51.44711 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a868805-5bb3-39dd-b67c-c111b88368aa | -0.95461 | -53.19978 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e96de9e-1791-3a63-bf76-0d8de87e2cab | -1.26105 | -51.74834 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96cbc3f7-70e6-3b5b-8cef-5042c886cc2b | -1.12894 | -53.78881 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e27f325-eb56-3307-8948-13261edf6d35 | -2.68702 | -46.27744 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad14b895-f106-35dc-9b99-544a486a688a | -2.56467 | -54.05972 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f25d1cd-5039-324e-ad95-0dbc58ac359c | -3.00275 | -51.55296 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b41391a5-6ffd-3eb1-a069-dea6a281f5e5 | -3.47172 | -50.25625 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f41740d1-780c-3646-96a2-6e6851b90fff | -1.07292 | -53.17577 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9a99e3b-d499-30ba-b3ca-29d1f62acf18 | -3.28006 | -53.84011 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5be3ae9d-089a-38d5-a0cc-83e9dfe4aaf7 | -1.23959 | -53.38969 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8a10ba5-b02b-3cc4-8128-dc5d467230fd | -3.47099 | -47.68164 | 2024-11-25 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1eb9069d-b062-3a73-8009-001e32ee46a0 | -2.7993 | -53.005 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f42dc83-5496-30d9-b668-a84f87815c93 | -3.10723 | -53.99461 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ee28a00-b2d8-34ca-8bed-5650582e61bb | -1.77467 | -52.72137 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cd5abd1-13d8-3a45-ac2b-8afdb5a72e73 | -3.0091 | -51.44447 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b730fa7a-51bf-3989-8f02-f2013a65d17b | -2.64747 | -51.7704 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c7ca97f-70e5-3b7e-80e9-f1794605c199 | -0.03081 | -49.63861 | 2024-11-25 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37513b8c-c07c-3808-80a8-9bc15300563e | -2.78272 | -54.05052 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4402d88e-4852-34d7-b0c8-393f45d21cb3 | -3.36917 | -53.05842 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12949d63-9603-311f-827d-ce951212df4a | -3.10778 | -53.99113 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10746990-33e2-38c0-8f01-bb787eb9c16b | -2.96018 | -53.93599 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecf997a2-96bc-3dda-b174-14af958a7fd9 | -3.03844 | -54.01949 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d5657f0-cdac-32d5-8f4f-bafff33d0085 | -3.29345 | -45.7374 | 2024-11-25 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fadc318a-608e-3881-9dd2-e5ef7234e2c7 | -3.4745 | -50.43348 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 957095d0-bfba-3c53-ab31-f2e0098984a2 | -3.55196 | -53.53276 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9f8c9da-6ce6-3919-a34d-ddac216f5bec | -4.66236 | -46.92414 | 2024-11-25 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 24756085-98bd-30ba-9226-39b93181d023 | -1.61366 | -52.57902 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 223be57e-281e-3aec-92eb-3029288b3de2 | 0.69483 | -51.44287 | 2024-11-25 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 558aadec-bb53-3649-9466-79be0ae7d098 | -3.28194 | -53.00949 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d68f1f8-e003-3430-8b29-301a0ddc81ae | -0.14185 | -51.58682 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 889e616a-252e-3aea-9c81-b292426fa1a9 | -3.53922 | -50.44341 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad02d865-c666-3088-bb68-6ad20910ac87 | -4.13809 | -54.33816 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc7a81bc-be27-3c9a-9b81-144e75718d57 | -3.50308 | -50.46296 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4d69ce0-665e-32da-aa96-96ea256aaaf4 | -3.27558 | -48.74862 | 2024-11-25 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4544ad6a-9a79-3589-a2bc-306a01d4798a | -2.24914 | -53.61847 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3f02bd7-f5e8-3949-b0f9-eda95c3ee1fa | -2.62189 | -53.97919 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1253e87-012d-3c4d-9468-bb36d81b3a77 | -2.81834 | -54.08469 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb9f01fc-dec6-330e-b73e-0e3537db5e4d | 0.64181 | -50.5689 | 2024-11-25 04:55:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbfe99ea-c292-3bc3-bac6-f5687db03e3b | -1.22975 | -51.79421 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README39.md)
