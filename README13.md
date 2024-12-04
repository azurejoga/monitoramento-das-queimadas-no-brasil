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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cec7dde9-061c-30ab-874d-dd2ff2da7e03 | -1.99883 | -53.27993 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2a384e0c-562a-3ef2-9854-b0c945f287a7 | -3.47884 | -49.98489 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e83a8e40-eda2-3df1-8b2a-b4017019f97b | -1.68031 | -52.51778 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 314794d9-6c50-3d50-83f9-a1a2053ca6c0 | -3.48293 | -50.94226 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8e1192e5-0d37-3659-b26d-815a5193d420 | -1.86079 | -46.33659 | 2024-12-04 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f7b94f67-f433-315f-87aa-17667787f630 | -3.19059 | -50.29894 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 90f0b32d-6184-3869-a3a7-bd67999d4cc8 | -2.89036 | -51.80305 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 5179044d-aeda-3f0b-9372-4fcf75d60fe6 | -2.58281 | -53.68452 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f998e311-28b8-3e54-bf23-9b6ef0b01e88 | -3.33003 | -46.61121 | 2024-12-04 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9ed18f61-0632-35f6-a833-9ee50cff473e | -2.71905 | -45.5344 | 2024-12-04 00:54:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aa31dedb-e678-34e5-8d8a-7addcd5317ec | -3.66835 | -47.12224 | 2024-12-04 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 1e94caeb-1f06-3915-84ab-681eaee1ea25 | -3.2029 | -50.65489 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| c33dbaca-53c2-33d8-aa82-8bfbdcc8f8f2 | -2.99518 | -54.10639 | 2024-12-04 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 35e43b68-2293-353b-8102-5fe1c36c4a11 | -3.99269 | -47.92367 | 2024-12-04 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 49cc4307-86d1-3377-91a7-55baa86faa64 | -3.96669 | -52.20912 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d0c982a5-c2b4-371e-87c4-0eee04d7914f | -4.6807 | -45.67456 | 2024-12-04 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ec3c8933-1a98-3b3d-87b5-ab2976609b52 | -1.48485 | -53.81807 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 41828d32-ac1a-37bc-9294-e96675d77127 | -3.55395 | -51.52018 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f617cad2-d720-31ac-a905-ba8f21ad4c63 | -2.69335 | -45.65157 | 2024-12-04 00:54:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 276b022f-1dda-33d5-8c01-6e276f3755d2 | -3.11173 | -54.63094 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 2737697f-443c-392e-b8e8-6c2def344b92 | -3.29646 | -53.71416 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0b26f8cb-c67d-3132-9a46-3e3bd7a41662 | -2.67236 | -52.45618 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 76f3c641-1ce4-3723-8060-d484e5749e8b | -6.09172 | -48.04935 | 2024-12-04 00:54:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7e6a32db-caf8-307c-bf22-f5093cc6c7fb | -3.93585 | -46.92485 | 2024-12-04 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0f5d3a0f-b06a-372f-817f-ab6b200209c3 | -4.19898 | -45.3901 | 2024-12-04 00:54:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2bae4238-8154-3962-9d46-1df7c835a520 | -3.73478 | -51.24965 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8a5a0cfb-8ab4-3d39-9a96-4cbe23604799 | -2.39807 | -45.36658 | 2024-12-04 00:54:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1c591728-132e-32fe-ad31-30509e3a430a | -3.78806 | -50.96432 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c1922b02-66e6-3e64-af61-b9d1361350be | -3.25233 | -50.60985 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f3f84f4d-7c2c-382d-85a5-97a77e75c20e | -3.6605 | -50.70461 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4a01ad71-f1ea-3059-bc87-e1e73e91a8d8 | -2.92683 | -46.77868 | 2024-12-04 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0102de6a-2cb8-31f1-9c81-04d50fc13502 | -4.09607 | -48.86303 | 2024-12-04 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 61d2e306-ef74-3844-85dd-99ea512674ac | -1.25448 | -46.60389 | 2024-12-04 00:54:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c06735ba-5b41-3111-ad83-3c620bf98116 | -4.29561 | -45.12945 | 2024-12-04 00:54:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 08a5a7a6-6a6a-312e-b46b-fcf818e4b1d4 | -2.96402 | -45.20145 | 2024-12-04 00:54:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 0010614b-a145-3f21-ad3d-013cd9f63315 | -3.98478 | -50.51966 | 2024-12-04 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| addf6359-631c-323a-bc02-7f64abfdf92b | -3.34824 | -49.77225 | 2024-12-04 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| c2a866cd-52bc-3036-b979-99f607baad20 | -2.32673 | -45.43526 | 2024-12-04 00:54:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 4d5ae7bc-1915-3118-9c71-0567cdb2b2df | -3.49819 | -49.92719 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a6ae7dbd-0838-3f2b-abc7-86eb80abcb23 | -3.72249 | -51.08936 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2ff88a50-cfdc-32f8-83a0-a092b287232d | -4.6824 | -45.68608 | 2024-12-04 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 22ff8ae4-86d5-3474-bcec-4ea5973bcc9b | -5.25 | -45.86857 | 2024-12-04 00:54:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8c54d080-ca19-3f62-8254-c7d671f6901a | -3.79999 | -50.98247 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8f4afab0-c0b1-3c1f-b976-f51ddf63deb1 | -3.54226 | -50.17891 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 231bed42-8f95-3ec9-b995-2539c4445af7 | -2.61727 | -45.42072 | 2024-12-04 00:54:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0f71a3a9-5f64-3faf-b6b6-f426a457dcfd | -4.91425 | -47.8607 | 2024-12-04 00:54:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 39.4 |
| a01300b3-a2fc-3c41-a1e8-1ebcba07c220 | -3.26091 | -53.61883 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 18a879c5-500e-36ea-87d7-20de7d64b229 | -3.25372 | -53.64814 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ed090549-7e21-3a81-881d-f3ae190ce589 | -3.19234 | -51.17973 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 80e78f2a-20fa-3cff-b48e-64bf27866fa5 | -2.89178 | -51.81351 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d3ade3b6-1c4f-3714-9113-61b920b015c7 | -3.90054 | -46.67239 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dbe1c136-3149-365e-96f8-8c52ee118c5e | 1.47101 | -55.87683 | 2024-12-04 00:56:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 719cd7f2-0a58-32d5-814d-3f06e1fa2450 | -3.1969 | -50.6428 | 2024-12-04 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| a168944e-8ca1-38f2-b758-1c0c6df48deb | -4.1223 | -43.9299 | 2024-12-04 01:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 230.7 |
| aba72a13-47d4-305e-a099-86a48f717637 | -3.2153 | -50.6423 | 2024-12-04 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 486b96b4-dd04-38c0-9af2-1c1447940013 | -1.7545 | -52.6159 | 2024-12-04 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4d10a67b-3848-31ff-853d-09a66687e8cc | -2.8975 | -51.8133 | 2024-12-04 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 979a8acc-4638-309e-8b76-d2c8e36d205b | -2.6428 | -45.7394 | 2024-12-04 01:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 106.8 |
| d3c12e9e-cd6b-36fe-8d96-7661819df06a | -2.8791 | -51.7932 | 2024-12-04 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0540cfe4-ab26-3c4f-be3a-d59971a52482 | -2.8012 | -53.0633 | 2024-12-04 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 7ef66982-713e-3881-afd9-3652bef6546f | -4.0501 | -46.5947 | 2024-12-04 01:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8490be88-73fa-3729-972a-1b57e2f45557 | -4.1225 | -43.9068 | 2024-12-04 01:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 6261f825-8200-37b9-aa42-d19cba6bdb53 | -1.5087 | -46.7647 | 2024-12-04 01:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 377f1b1a-f466-36cc-901c-8d9a570ad2ed | -3.058 | -53.28 | 2024-12-04 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 4b168515-dff1-300c-991b-7ea4ff66dafa | -1.7361 | -52.6366 | 2024-12-04 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 686a74c9-1b43-31a7-96cc-b414e72a13f3 | -2.8196 | -53.0629 | 2024-12-04 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| e23e0a7f-98fe-3c39-8634-eb5225171c8e | -2.6429 | -45.717 | 2024-12-04 01:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ac99e6ca-6252-34d1-8fd4-b6186d2eb602 | -2.9719 | -46.9248 | 2024-12-04 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e36e00b2-f4d3-3bf4-9102-d85c3e82af47 | -1.4768 | -53.8148 | 2024-12-04 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 2ea27175-a4c1-396c-9517-2d6e4a5eda19 | -1.4768 | -53.7947 | 2024-12-04 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| a139ed45-7f2c-38fe-a162-818ed9f330e0 | -5.5882 | -45.1412 | 2024-12-04 01:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a313a662-53e4-380b-a00e-db7d3d798c6c | -3.6572 | -47.1183 | 2024-12-04 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| cbba7b7c-6315-340a-84f7-b86f9f0fd0c5 | -6.086 | -48.0557 | 2024-12-04 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| a7e728bd-8ac9-3872-97a3-2f6978ea6031 | -1.7544 | -52.6363 | 2024-12-04 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 3cd44ef7-3f60-3acd-ad56-6592403d99db | -5.5693 | -45.1651 | 2024-12-04 01:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| dbba8c92-77c0-3285-a28a-614a7d9b102e | -3.0764 | -53.2796 | 2024-12-04 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f2f157d2-bb24-3bd0-9268-7260deb42105 | -3.259 | -53.6388 | 2024-12-04 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 701abb22-6923-31e7-a97f-a6509832f86a | -4.1222 | -43.9529 | 2024-12-04 01:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 384526fc-c825-35b2-91e2-9606ff3ae3ac | -2.6242 | -45.7399 | 2024-12-04 01:00:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 98801f9c-6263-364c-aa89-a5562895478e | -4.1037 | -43.9309 | 2024-12-04 01:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 47fdfc21-e7e3-392e-be6d-f5eb53200a48 | -3.259 | -53.659 | 2024-12-04 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 3f8b09a3-6972-35be-a034-5c68fc244d18 | -2.8197 | -53.0425 | 2024-12-04 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 572bd972-bdb6-3623-9f2b-5a5fa7e61d4f | -3.5675 | -50.3164 | 2024-12-04 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 2649b14f-4c04-36ba-a1dc-61c3173585f9 | -2.0682 | -45.4871 | 2024-12-04 01:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 0b6f3c72-10dc-300e-8cc4-932e8b59b777 | -5.588 | -45.1638 | 2024-12-04 01:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 0a733ddf-6131-3527-bfb5-162287c76cb1 | -3.6758 | -47.1176 | 2024-12-04 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 27301af8-6169-3b9f-bf1d-f36654537707 | -2.879 | -51.8138 | 2024-12-04 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2020fa07-b198-3674-a9c6-9ad0f331fcfb | -1.6241 | -53.5308 | 2024-12-04 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| ca6e1af3-da0c-3927-831a-2d181f8ba0df | -2.6947 | -51.8597 | 2024-12-04 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 3fbc5435-d7a3-3dc0-8054-9ca224adcb8d | -2.756 | -45.2871 | 2024-12-04 01:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 941ce35e-e44e-3cc8-8c4a-be5ea1b84cc5 | -4.0499 | -46.6168 | 2024-12-04 01:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 237d60f8-47a5-3b97-9d26-fc5f0b98df74 | -1.7361 | -52.6162 | 2024-12-04 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7acef823-7553-342f-b38f-a606f95049f6 | -3.5676 | -50.2954 | 2024-12-04 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 28ea595d-6bcf-351a-82af-621d4971601a | -2.7561 | -45.2646 | 2024-12-04 01:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 2a37a2fe-900f-3fc4-a12f-e98381acaa5c | -3.12 | -54.55 | 2024-12-04 01:00:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6bf26f3-8a48-333c-a4c6-381b5023abe6 | -3.12 | -54.62 | 2024-12-04 01:00:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 260abd2a-75f3-318d-a936-f6390c5ece05 | -2.5517 | -45.2712 | 2024-12-04 01:10:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 241b9262-d7bb-377e-aad0-4a1a5c20c251 | -3.259 | -53.659 | 2024-12-04 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 47450d83-fc46-3bc1-9c58-a5798b086e39 | -3.2153 | -50.6423 | 2024-12-04 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f0dde8ab-47c6-3fc1-8ece-c6c6106b0f63 | -2.211 | -47.254 | 2024-12-04 01:10:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |


[Clique aqui para ver as próximas entradas](README14.md)
