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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c758ee99-3908-373f-8270-f5b4cda17eb0 | -1.5289 | -60.328602 | 2024-11-19 01:25:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf9ae3e-c72c-3a96-a4f5-a66aa874e667 | -2.2806 | -53.642502 | 2024-11-19 01:25:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b47bc021-8161-3409-8fd6-467ff60f144f | -1.345 | -55.743999 | 2024-11-19 01:25:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52d2b422-27ee-358b-a270-33506ce7c345 | -4.1113 | -51.060902 | 2024-11-19 01:25:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1c198dc-dc12-300d-ae3d-40d3fee2e0b1 | -13.1669 | -53.276001 | 2024-11-19 01:25:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aeca506a-28ab-31fe-a78a-c92124c4c794 | -3.355 | -54.099499 | 2024-11-19 01:25:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51e218d7-c4f4-3325-b4c9-3870a9b9fabb | -2.76 | -52.594299 | 2024-11-19 01:25:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48800ebd-3576-3800-b524-08fd8ff1ef96 | -13.1695 | -53.286499 | 2024-11-19 01:25:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c024ff59-8b6b-3d1d-af45-b86584abada5 | -3.508 | -50.225899 | 2024-11-19 01:25:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1322da8d-2410-38b1-8fa3-f78225620a92 | -3.5138 | -50.249699 | 2024-11-19 01:25:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1c0bf2d-3a1a-34b7-af91-bad38bd0de5a | -2.5816 | -51.720901 | 2024-11-19 01:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95f9d086-ff6d-3b89-81a1-c87356fce29e | -3.3279 | -50.492699 | 2024-11-19 01:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 287c1411-db2a-3b17-a42a-ccebb4d0990b | -2.2772 | -53.627998 | 2024-11-19 01:25:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd0b0eb1-b6ff-31fe-9bec-0c1e97fff038 | -4.1063 | -51.040501 | 2024-11-19 01:25:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1a11134-b95f-304b-a908-9e079cc8f432 | -2.4917 | -49.028801 | 2024-11-19 01:25:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa9cf56d-623b-3430-b2a5-330bcb3558b1 | -9.2543 | -45.0074 | 2024-11-19 01:30:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ad23bff0-bfd9-3f74-87fb-c5b08706cd14 | -2.8431 | -46.6651 | 2024-11-19 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| d810df01-1acf-37fd-9150-253feef6b4aa | -2.5012 | -49.0162 | 2024-11-19 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e8844798-03c1-3138-b388-4a3b2b1f96e2 | -1.3962 | -47.445 | 2024-11-19 01:30:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 95e837e7-4c88-3a71-98f8-14e8919b106b | -5.9788 | -45.3621 | 2024-11-19 01:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 7332a4d9-37d2-3f07-8169-1ade9a78615c | -3.5125 | -50.2343 | 2024-11-19 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| dd95b3e2-95fc-3f87-baf5-541392608753 | -4.1246 | -43.5833 | 2024-11-19 01:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 402fae0a-d19d-3946-840a-6184d9c8800b | -13.2643 | -56.7947 | 2024-11-19 01:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| cb7998de-93fb-34cb-a231-7f045cc92733 | -13.245 | -56.8167 | 2024-11-19 01:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 0253daca-8281-30d1-8987-3782baf25ad5 | -23.9706 | -54.1372 | 2024-11-19 01:30:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 95.0 |
| 117975e1-aec4-331f-a419-1b5b08add47b | -2.7659 | -52.6163 | 2024-11-19 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 62bd6e21-b3ce-30bc-9d06-8b3ba9280851 | -13.264 | -56.8149 | 2024-11-19 01:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 190.7 |
| 3e2b320e-e174-37db-a3af-4710b224e176 | -23.9711 | -54.1148 | 2024-11-19 01:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| cc1a78ee-d05d-3617-a1a5-e93ff26d4303 | -23.95 | -54.1191 | 2024-11-19 01:30:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 68.8 |
| 3b1cfbe8-c440-3347-a225-0deceb976281 | -13.2452 | -56.7965 | 2024-11-19 01:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 83e60b05-9a68-3714-ae4e-ef2953bbad0e | -4.1244 | -43.6064 | 2024-11-19 01:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 4a0e6345-1692-311d-a472-febb5ad3648f | -9.2546 | -44.9845 | 2024-11-19 01:30:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 15a18690-7cc7-3f54-b87d-fd0436c31c73 | -13.2831 | -56.8131 | 2024-11-19 01:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 736d933a-f9db-3922-8064-ad5ecc021913 | -2.766 | -52.5959 | 2024-11-19 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 183.7 |
| 4a1d6d02-e67d-3f7d-9851-877c4128bff9 | -8.2659 | -44.0348 | 2024-11-19 01:30:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 4b98f5e0-365f-3454-8898-78a7ca2a6863 | -4.1182 | -51.0486 | 2024-11-19 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 074829f9-fd4e-39db-bd04-27afa50cd035 | -8.2662 | -44.0115 | 2024-11-19 01:30:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 7f8a07ac-6e78-383e-8077-709bf3a6f90a | -3.5126 | -50.2133 | 2024-11-19 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| d288a4ab-0dba-3071-af84-19a3bb4c22ef | -13.264 | -56.8149 | 2024-11-19 01:40:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 187.3 |
| 4a565956-60cf-38ae-9872-dd0a47abd814 | -9.2543 | -45.0074 | 2024-11-19 01:40:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 403621e3-e32d-3928-9b5b-e095ee77ac94 | -23.95 | -54.1191 | 2024-11-19 01:40:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| c4f620ca-590c-39f2-9d3f-b1d066a5bdfa | -8.2659 | -44.0348 | 2024-11-19 01:40:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 44b3b8ee-f1cb-3a52-9ba6-6b59be2cb30e | -4.1246 | -43.5833 | 2024-11-19 01:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| f545acdb-5cc8-329f-b062-4318888f4e89 | -5.9788 | -45.3621 | 2024-11-19 01:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| d5a9583c-b245-317e-b601-8868f7dfad2d | -13.2452 | -56.7965 | 2024-11-19 01:40:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3199aba5-9144-3630-bba8-38d564c18e26 | -3.5125 | -50.2343 | 2024-11-19 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 8ae8e029-0e59-3cc7-b110-5c06f27bcf76 | -4.1059 | -43.5843 | 2024-11-19 01:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 47df743a-9e79-3caf-8cf1-45c858a45009 | -1.3962 | -47.445 | 2024-11-19 01:40:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 582af1fa-fe43-3498-bd49-74e6cc9eb36f | -9.2546 | -44.9845 | 2024-11-19 01:40:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| de5640ef-bc36-3f6f-8860-da5ea24b3f0f | -4.3958 | -47.7835 | 2024-11-19 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 392e01d6-b1fd-320a-b4d4-cd7de47fad66 | -2.8431 | -46.6651 | 2024-11-19 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| af0c39db-04a1-34a9-8ec6-3a654469331c | -13.2643 | -56.7947 | 2024-11-19 01:40:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| a20e299e-0be2-3cad-9dc2-3daa8b13de46 | -2.6131 | -54.5381 | 2024-11-19 01:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6f25b6f2-597b-376c-a5e8-67318092a15b | -4.1244 | -43.6064 | 2024-11-19 01:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 6f91201b-5e7c-3d83-9c22-01dabb23f8ab | -4.3959 | -47.7618 | 2024-11-19 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 902f571c-6d7a-3fdb-8baf-631fd3322110 | -2.7844 | -52.5954 | 2024-11-19 01:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| c701d0b1-76ea-3ec8-9347-dcd48cc49d34 | -2.766 | -52.5959 | 2024-11-19 01:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 4b89c022-39fa-3f35-aaea-758788214a06 | -13.245 | -56.8167 | 2024-11-19 01:40:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 42177a07-2ad0-39e1-9c34-cfc8c497017a | -5.9975 | -45.3607 | 2024-11-19 01:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| b3c253aa-b324-32e9-8905-0771008fdb8f | -2.7659 | -52.6163 | 2024-11-19 01:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b9b7b64d-a250-3fbe-acf1-ff0f6e9121c5 | -23.9711 | -54.1148 | 2024-11-19 01:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| c89009fe-a245-39c6-b179-8e5ea671c1c0 | -4.1182 | -51.0486 | 2024-11-19 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 4f93c6a0-65e8-3188-9d5e-07b7f61be809 | -2.4293 | -54.6216 | 2024-11-19 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| b824ac20-c1c1-3157-a99f-cd3c11d37bb0 | -13.245 | -56.8167 | 2024-11-19 01:50:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 001e63ca-aec8-3f85-8368-ff0533d88b9f | -4.3959 | -47.7618 | 2024-11-19 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 1cefbf87-4831-38b4-8a4a-4b87617fd878 | -3.5126 | -50.2133 | 2024-11-19 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 9721ff50-30d0-3dc8-8371-aa6595f60227 | -23.95 | -54.1191 | 2024-11-19 01:50:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 73.2 |
| 73d6a2ee-e39c-398d-9f88-9d396cf6fc3d | -13.264 | -56.8149 | 2024-11-19 01:50:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 6089a63c-c548-35e1-b6b8-6c6fa5a6e1ee | -13.2452 | -56.7965 | 2024-11-19 01:50:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 32ed56df-c268-3089-bd58-91bde245720f | -3.5125 | -50.2343 | 2024-11-19 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 33c349b9-a072-3299-93d9-c271f4109807 | -5.9788 | -45.3621 | 2024-11-19 01:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| c37aaa0c-d5e0-33b0-b7d3-289ea457d62d | -4.3958 | -47.7835 | 2024-11-19 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6538688d-cdf4-3e69-86e1-5eac23e02097 | -2.766 | -52.5959 | 2024-11-19 01:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 49bbe1d5-7637-3929-b08b-c4ace42857d8 | -4.1244 | -43.6064 | 2024-11-19 01:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| cdf21aa4-0175-3c64-ad21-8253b75c7457 | -1.3962 | -47.445 | 2024-11-19 01:50:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 4dda4c0b-d3eb-36cb-a40c-62606c57991b | -9.2543 | -45.0074 | 2024-11-19 01:50:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 8f6a7452-5f0d-3abd-9564-0c7b9cfa071f | -2.7659 | -52.6163 | 2024-11-19 01:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 6341af77-293d-3975-84a3-d2edd1c49e17 | -13.2831 | -56.8131 | 2024-11-19 01:50:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 39e64043-68e3-3232-b19b-9257deb33456 | -13.2643 | -56.7947 | 2024-11-19 01:50:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 4bd95fb6-c3f5-3326-9f78-d86054601085 | -5.979 | -45.3395 | 2024-11-19 01:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 9788c992-3608-39b3-8e51-d9ac5f0d6ac8 | -4.1059 | -43.5843 | 2024-11-19 01:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 3adbf869-20b5-3245-8706-92df768b895b | -4.1246 | -43.5833 | 2024-11-19 01:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f51b2366-49a2-3b74-a18a-826df878b500 | -3.5125 | -50.2343 | 2024-11-19 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 3ae4d89a-4ba1-37fe-bde9-4498191214f3 | -4.3958 | -47.7835 | 2024-11-19 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 1f5ebe7e-9957-323d-a674-e25ff03d5925 | -13.264 | -56.8149 | 2024-11-19 02:00:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 126d60e0-6744-3af4-8caf-ecffb7e99db2 | -13.2643 | -56.7947 | 2024-11-19 02:00:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a8428db6-8e7d-389b-af23-132fd3efadea | -1.3962 | -47.445 | 2024-11-19 02:00:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 38f56df1-9bd2-3c06-a6c9-b505c313a474 | -8.2659 | -44.0348 | 2024-11-19 02:00:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 477dba18-57cd-3397-ac64-423845026a9d | -13.2452 | -56.7965 | 2024-11-19 02:00:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d0f429b7-d73a-307c-be4d-323e38ae3d08 | -4.3959 | -47.7618 | 2024-11-19 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 622ab7c6-cf1a-34c9-b970-d1ea14264885 | -13.245 | -56.8167 | 2024-11-19 02:00:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 65d776ed-3075-3777-af62-c208c802ee9f | -2.766 | -52.5959 | 2024-11-19 02:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 905cc1e5-5b58-3852-9116-342e353ac699 | -4.1246 | -43.5833 | 2024-11-19 02:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 3570d273-3433-355b-b384-4896c3143936 | -5.9788 | -45.3621 | 2024-11-19 02:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 157.6 |
| f48d69ba-621e-307b-814d-69943926fa07 | -3.5126 | -50.2133 | 2024-11-19 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a73e278c-ad1a-3d63-bcd2-8e3d9e8edc8c | -2.4293 | -54.6216 | 2024-11-19 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| aab169e0-d3c0-36e4-8210-39a6c2a46a6c | -4.1059 | -43.5843 | 2024-11-19 02:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| c7675c5d-2366-30cb-a476-cc8dcb17af04 | -2.7659 | -52.6163 | 2024-11-19 02:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 053a1671-fbd6-3459-986e-5234a975ab2b | -4.1244 | -43.6064 | 2024-11-19 02:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| af049a0b-3efc-3e9c-aa20-af8063b5f0d4 | -13.264 | -56.8149 | 2024-11-19 02:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 135.6 |


[Clique aqui para ver as próximas entradas](README12.md)
