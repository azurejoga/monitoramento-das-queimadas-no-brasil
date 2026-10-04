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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ebadfc2-0022-371c-9d81-fb50e2588aa2 | -3.08047 | -51.27555 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40c19031-32ff-3a7f-b479-e76dc4e13886 | 0.0939 | -51.04073 | 2026-10-04 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64d9f042-b88f-3743-8fc1-ee7a10776297 | 1.76181 | -55.63988 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5078865-8d36-31b6-853d-0cdb73f5902a | -3.11885 | -53.75497 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 83cbb3ab-446b-3659-8c5f-b3d8fffdbe4f | 2.35245 | -50.75432 | 2026-10-04 04:55:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb65e03a-bf11-32a5-a5bc-698e0bd3cb0c | -3.56864 | -51.98138 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba8596f9-3d20-35c9-9369-ba91861f3db2 | -3.00585 | -53.88335 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6169f0df-4fa3-3ca5-80e6-2445c5ec6e96 | -3.18777 | -57.92028 | 2026-10-04 04:55:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b70d5c82-798b-3b4d-88f9-c232240d7781 | -3.56806 | -51.98503 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9861e9a9-b6e4-32e3-81b0-e816679c8608 | -3.71294 | -50.65952 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea15eec9-e0cf-309b-b161-b44e17e5e903 | 1.9236 | -55.72244 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e12be201-cc7b-3444-babc-daae58a8d69d | -3.32235 | -54.17187 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a813ef3-fdf4-3639-b4fc-132a921fdbde | -3.46835 | -50.0889 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e5b5e369-bcd5-38c0-a2a2-36bafb83072f | -3.51022 | -49.93233 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0a090e8-0481-3408-bd5f-b92e8a28a151 | -3.29058 | -53.84233 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0de53a83-1ac4-33db-b764-e5f2a30f5698 | -3.06033 | -54.16656 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 67c9dedc-13d7-3617-af84-b5f2554893f4 | -4.31984 | -48.6289 | 2026-10-04 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01e8c0fe-6013-38d5-83c5-ec50a6595a82 | -3.07674 | -49.54745 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d9900b5-3ac5-3acf-9725-ed24b075dab5 | -4.27176 | -49.97405 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91409188-6a47-337a-92e5-334bebecae4a | -3.17692 | -50.53918 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f63e7521-7a24-3370-9d02-aa0ddd302c60 | -1.28054 | -55.41267 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ffe0515-14a3-3d31-88e8-e1e5d1cf4e17 | -3.17235 | -48.69501 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1687ab6-b49f-36a8-93fd-064fbe5deaf8 | -3.08087 | -54.39988 | 2026-10-04 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63e84f0c-9378-3dda-9092-e10e28b0d516 | 2.00035 | -50.93249 | 2026-10-04 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ad7e20e-cd4d-3898-a6d6-ee7b2bfad7bb | 1.76629 | -55.63916 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ae57870-efef-3045-9060-162895120c00 | -3.07784 | -49.54047 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5d813e87-106a-3300-afff-9385e42dc7bf | -4.45715 | -50.97585 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a50cfad1-d88d-3c07-ba10-12b527cad5a7 | -2.82438 | -50.50126 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28e665b6-ee4c-32a7-9ac7-252d17c5b38f | 2.8773 | -60.54359 | 2026-10-04 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b800708-e4b4-3daa-bac7-d6facb89a009 | -3.36052 | -43.38412 | 2026-10-04 04:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 553e5d3f-4a59-3d25-8006-e325a7ad4eab | -2.15456 | -59.22801 | 2026-10-04 04:55:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ae078e1-304a-3904-aa4c-2b4d24c5425b | -5.34354 | -44.82819 | 2026-10-04 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f754885d-b455-320f-8834-06191060c890 | -2.80692 | -54.13675 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74090086-9845-394c-9a64-ab832ca07480 | -3.02028 | -53.89264 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f475a3f-1367-3892-852b-5a68588978cf | -2.21988 | -53.70788 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 85bfb1fd-7d3e-3711-a306-1fa01feaed9f | -3.12463 | -53.74251 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e92c9496-e7cb-35ce-a9b1-1043519955c4 | -3.07374 | -51.27449 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd0db1b2-be9a-3343-868a-60261696b09a | -4.05846 | -51.12388 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| deed5a4c-2714-3f67-8aff-452de31088bb | -1.56173 | -46.86139 | 2026-10-04 04:55:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbd2765f-721a-318d-a498-922e851e0639 | -3.69907 | -50.66088 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99ee72e9-23ad-3b24-a5bf-03cabf281cec | -3.04428 | -54.19845 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 167d547a-dffa-3db3-b306-2291dc56faba | -1.76669 | -55.0251 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0209b101-bff5-3f47-8637-ffd68c18f705 | -3.0098 | -53.8864 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f0ff412-c2b3-3b8f-ac57-3c75a380d030 | -2.90045 | -54.08349 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b6fcd67-796e-3d1e-bdff-2bddd4fdd9a0 | -2.57922 | -49.99836 | 2026-10-04 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c64ccdb6-2269-3db1-bff6-333691a831f9 | -3.28014 | -53.83619 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11f23780-9ce7-39c3-ac57-b95738135863 | -4.28504 | -50.2709 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 15db3d02-a452-3577-b091-9122a7aad437 | -3.18358 | -50.54023 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 50854e47-2035-3f26-981a-549cc3e694f0 | -3.17045 | -54.08607 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1fa8cd3d-ae6e-3d5b-818c-ac17fcb4d916 | 1.80166 | -55.55905 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2a0c1fd-d256-3ef5-92c9-f4a48f458230 | -3.18025 | -50.5397 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c9f60ef6-c4b1-3c98-af85-dd2c0ccf205b | -3.09728 | -51.10483 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a018af08-4049-3aa6-9a39-908d323315c1 | -3.17869 | -54.0829 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13058139-a5f2-3214-b26e-7277bd8a4612 | -2.5938 | -51.85608 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ac652ba6-a80c-349b-a7b5-f3b92e73b44d | -3.13642 | -53.73996 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4191a015-7096-38b0-8896-27e3f7eb16d2 | -3.17565 | -54.07774 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8b95a80-3ca7-3b0e-b857-3d0dcbc7568f | -2.36483 | -50.60289 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab36e33c-6d2d-3d28-8cab-fc8e4eb7f10b | -3.07953 | -49.55146 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d10838d3-c7ac-31a3-b753-11340d5cc512 | -3.13487 | -53.73875 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34b4dafa-a02c-3e2e-a201-e1be3aeea3d1 | -3.12532 | -53.73814 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d48acf39-6a66-3101-b78a-09cc0971f16c | -3.08397 | -49.54501 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a196418f-198a-30da-8a16-c81f37a35ef5 | -3.47281 | -50.10378 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90dd7b11-ad83-35b8-a3ac-8ef4d40aa2f9 | -2.82508 | -54.12077 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdd40f45-451e-3079-bcd0-0e0f5e403bbd | -2.82128 | -54.12015 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2dc5feb0-27e6-302d-825e-1e181ef89a98 | -2.57939 | -51.88013 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1a68ef9-1276-31a1-a237-1e17ea206e50 | -3.1246 | -53.75494 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cc9f0ee-bcdb-3838-b66d-0f61383c6b15 | 0.98933 | -50.01544 | 2026-10-04 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffe383af-31a8-37e1-a71d-5693bb4f7373 | -3.18622 | -54.08422 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 100b7c83-c7cc-3c66-9896-bf98882bd3cf | 1.76009 | -55.65845 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4908da81-d0c6-30ad-8719-5cf9be146a8f | -3.0444 | -54.22214 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 444258b1-660c-35d9-92f2-76723b07a288 | -3.298 | -53.84352 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca215f61-9e93-3008-a984-76503ddf67c7 | -3.51762 | -54.61697 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69f654d2-03ab-32e4-9282-0100effbb9b4 | -3.11286 | -50.2842 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7c4c2f7-9fe6-3a3e-b969-220ddafc60fc | -3.0068 | -53.88138 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f91bad54-33dc-3a12-be7b-904e59de2370 | -3.00783 | -50.47315 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 130dd605-ad23-3f8c-9752-91bbb8c2275b | -3.01281 | -53.89143 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8145978-f33d-31c3-8def-e719d99e555a | -1.87548 | -50.61836 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ef6889c-df6d-3249-8c4d-070cf91b30c4 | -3.77671 | -51.40313 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34f9121f-244c-358b-a776-d20f06e5353b | -3.19075 | -54.10114 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ed16c43-7847-3ea9-a95f-53de35b597f5 | -2.57879 | -51.88382 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08b42fdc-b8d6-338b-811b-a6b10459dda8 | -4.28668 | -50.26052 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72f27948-eebd-3c43-a28c-62ce046d053c | -2.21568 | -51.95325 | 2026-10-04 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f4823f3-1ff2-3f1b-a827-97580078b275 | -3.70738 | -50.65155 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffc90471-d6b0-3ba8-800f-4b0e52f9d796 | -2.25531 | -51.93964 | 2026-10-04 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d9d2022-a9b1-32d5-b7b0-e8f3f2ff5e8d | -4.29932 | -50.54268 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d745b9e-9928-37c4-8024-070b11bda6e1 | -3.0608 | -54.16806 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f6046664-8cc6-345a-b9fa-a374bd81e4f1 | -2.25366 | -51.92796 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e162afb5-1ae8-3b21-a876-e1bece9fed6e | -3.07002 | -49.52496 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20834e2f-a108-30d6-bc1d-22fa7fbede67 | -3.07505 | -49.53646 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e56b4a0-bb87-3d33-8e95-e52b732e3e48 | -3.46948 | -50.10326 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7245c948-ff4a-3e9c-bcff-f9ffb50f257e | -3.51065 | -54.61086 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c62c225-8829-3a79-a925-09c3349f31da | -3.13573 | -53.7443 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ffff68c-9987-3d17-ba09-608328ef8d3e | -3.71311 | -53.39631 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b70ea44-0548-3ec7-8b9a-e62ea81463ec | -3.12891 | -53.72886 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b73330fb-cf70-3add-b17a-ef2a48d4effa | -4.26355 | -50.78894 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb74bbe4-4446-38be-9400-5ed51d7e8ea3 | 1.94081 | -50.91149 | 2026-10-04 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2a95605-a7ba-3c1a-9a16-5dc2183bfb0f | -3.11931 | -53.72825 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 04088297-2aa3-3090-9590-cdfd281c2a29 | -3.1283 | -53.75554 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc5e6c78-872c-3eba-96dd-24ce945da658 | -2.81055 | -54.09015 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94f59d25-a47c-32a2-a0a5-abd2f06bb7b2 | -2.97649 | -54.08872 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README38.md)
