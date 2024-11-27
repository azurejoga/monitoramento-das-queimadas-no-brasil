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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b779f0e9-b81d-37c9-841d-b351273c680b | -3.89941 | -50.60558 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a3e9356-58a2-3917-8099-53f8a2314c38 | -2.82605 | -46.81041 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c358b4a0-1828-3d5d-8ef4-0eee52834dea | -2.8213 | -51.79971 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da0a92d2-3dc5-3c34-bc3b-ce058fde975f | -4.3182 | -47.51908 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d4c6a12-53d2-334b-80b3-3c55ae22958c | -3.95722 | -49.34877 | 2024-11-27 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59d8c4fb-547d-32ff-8558-f32a0ba0fdc3 | -3.52656 | -52.15146 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 41bc5120-6eb7-34c2-a2cc-74888d92e681 | -3.3433 | -50.51088 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc0936c3-eba6-3173-a517-e6c419956075 | -2.81679 | -46.82198 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 703c9a9a-5085-3ef2-bebb-25741616e593 | -3.96799 | -48.06085 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61832bfc-042d-3ecf-ab7e-b4fbe904b240 | -3.1754 | -48.43354 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 0d89579b-dafa-3834-b92d-edb6b3cf4cdb | -3.38064 | -50.10123 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dabc2ce-d38e-3f02-ac61-e82a183663a2 | -4.50049 | -46.60208 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c83276e-6b9b-3952-ba5e-dc519603bd1f | -3.70508 | -50.43737 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da103df0-eb78-3c02-a386-bac1c0968ecd | -2.80595 | -53.02417 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a78182e0-1728-3167-ae13-87bd87a1352d | 0.99273 | -50.25795 | 2024-11-27 04:42:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87cdda75-0ec3-39e7-ab3d-cec2594b085e | -3.10094 | -53.26355 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dacb6377-0635-37ec-a2e6-5ae0365399ad | -3.65854 | -50.23634 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34194e3f-30cf-30e7-ad77-798984a5d531 | -3.97898 | -46.65177 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1951e4b-052d-3c7d-a50e-70029083f919 | -4.16527 | -48.71388 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90706a8a-8600-34a7-8c4f-1cf0a69f24c0 | -4.11755 | -48.52598 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 577b65c8-4709-3c18-a5c3-ed8fdc7eb1cb | -2.59841 | -54.20246 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0a07d55-19be-308a-a539-98c5b105a25e | -2.6046 | -51.7957 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ddc458c-4955-3743-90d8-8886fe22c1c3 | -2.05189 | -51.18477 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99adbf4a-bd33-3462-b256-487768cc11b3 | -3.26324 | -46.41903 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53eb73ef-60cc-3f3e-af61-27bb6e1ac98e | -1.19013 | -51.76302 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 522f0149-80eb-3781-bd04-4a472213145b | -2.75233 | -51.94981 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3803afa6-d281-3a19-a2e9-67f91fb7c86c | -4.03052 | -46.95358 | 2024-11-27 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45d4d4f7-71e7-3c31-9a96-eb426fa0231f | -3.09572 | -53.25018 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 79996e49-27cf-3530-8250-b5e592982219 | -1.65727 | -46.94567 | 2024-11-27 04:42:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a34004f5-b72b-382d-b5c5-89efe9a8471e | -4.23706 | -41.92527 | 2024-11-27 04:42:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 25be020d-9c23-3ddf-8d31-836b69418e30 | -2.30471 | -51.32233 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2ff5d80-0447-37b7-a423-dc2873dc8ce9 | -3.4467 | -49.5064 | 2024-11-27 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a28758cc-a064-3b46-ac7a-0e7dace0c9ad | -1.66917 | -52.45314 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1e9cc9f-b143-3dbb-82fb-bec907ead63b | -1.63235 | -52.70641 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3a6b949-90e2-38c2-b1f5-5c8c71df5434 | -3.23999 | -53.0275 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaf5832e-9b45-35fe-8a11-2b2d6eb0a9cd | -2.16384 | -47.95258 | 2024-11-27 04:42:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 572f7941-2ac0-3ebc-9f95-84bcf03f5eba | -1.53996 | -45.69193 | 2024-11-27 04:42:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a33be431-abd8-3775-aa1a-e959cb508cd7 | -2.8286 | -54.12133 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 1bec94b6-ab56-3464-b797-b097d0ff8654 | -2.92362 | -48.33928 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8fb1d24-68cc-3803-aae4-a1cdc758da15 | -2.55056 | -48.28299 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bd7f176-e279-3fe8-bb9d-5c2e383aa6df | -3.57301 | -50.56464 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2fd1610-7437-31ce-b5fb-1f594b26a94e | -1.31754 | -51.75511 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c66d7abf-bc38-3326-b313-82dfc3fd1fbc | -5.50362 | -47.16886 | 2024-11-27 04:42:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dd4051f-72f0-3efe-a3a2-f1018c0e1034 | -2.5868 | -54.0562 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 827db1a1-27f4-3522-8dfd-1c971761a989 | -2.59887 | -51.83218 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01da43ac-033f-310d-ab89-4afe0ea37c37 | -3.11039 | -53.27349 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 449b0afa-0882-3487-914a-9a50242e2e24 | -3.61024 | -49.894 | 2024-11-27 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63e1603c-4d6f-3ffc-b313-078225669fe0 | -4.05674 | -49.0779 | 2024-11-27 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c5dd70f-f777-3faa-970a-1131e73af71b | -2.74834 | -51.95294 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a01f5a4-cc91-32fc-b437-6fa40e3094f6 | -2.88664 | -51.38418 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27db1665-007c-3459-9f50-391ee99e2430 | -2.61617 | -52.53651 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aef2e8ad-6197-3711-90c3-7494e4c44129 | -1.5195 | -46.07307 | 2024-11-27 04:42:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cbcca67-a971-3430-ac81-4564234de8ca | -2.17141 | -54.63188 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99558cc9-e8d1-3b5f-b804-aeb7792c1ccd | -4.06147 | -54.6738 | 2024-11-27 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a6490be-3b63-336e-851c-a0737aa494b9 | -1.80725 | -55.48093 | 2024-11-27 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc39cdff-8f0f-3c96-8921-579c9e84b2d8 | -2.85186 | -46.83603 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42536f86-6f27-3033-8760-67fd08f01afc | -3.70946 | -51.80058 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4453660-9e7b-3526-aad1-26e42c0ab0d7 | -5.98304 | -45.37127 | 2024-11-27 04:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| f2f7ca14-591f-329f-be42-6eb6729a87db | -2.70484 | -51.87093 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9759a6a4-328b-356a-aef6-c81e0d96ca0c | -1.74123 | -52.79691 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c93b82d7-0d1e-37ac-a217-65da3cfd7404 | -3.27767 | -48.76506 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7089b54a-febe-3487-af3c-56199765f867 | -2.63724 | -51.90159 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89733b92-9713-399b-9044-35c5bdf8fba9 | -1.48944 | -52.44291 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e9f8acbf-d580-3f49-8671-559874a088d3 | -3.73314 | -49.9553 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02079de7-dab9-319d-9349-a213b2d89ab5 | -3.17086 | -48.44035 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7cc8f830-7609-37a9-b130-40a6590509b5 | -2.59605 | -51.82797 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97b4ced9-bfea-31ae-ba18-a1d7af3f6dae | -3.90765 | -50.59629 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f552fcc-95bb-3a50-a97f-cf37c29d2841 | -3.05618 | -53.2901 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad406583-006f-3164-8527-5d21a3bb0a51 | -1.56832 | -47.81776 | 2024-11-27 04:42:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a047f492-a7c7-35b1-89c6-304e58188c64 | -1.23175 | -53.36432 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef922178-1608-3886-b671-bb89662cd325 | -4.10641 | -51.05853 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d68967c-1d2b-3b45-904a-8cea374d3136 | -3.0431 | -53.72103 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54a68136-8b2b-36e6-992e-92ed8cb38f9b | -4.18183 | -48.63016 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4249d3e6-354a-323c-a3ac-df57884822ab | -3.28094 | -51.12173 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 993ff190-a3d6-39fc-aabc-f0b25fbb6d46 | -2.32371 | -53.86116 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a50fe9f1-1946-3a79-aad7-fcb2ac0885ce | -2.94034 | -51.29776 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 447df861-1f9a-3a29-a67a-64fc6c002bfc | -4.48112 | -45.91978 | 2024-11-27 04:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ed71a2e-4ec4-3028-b9a0-67913fa3082d | -1.13368 | -48.35693 | 2024-11-27 04:42:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 578d8fef-e517-3b71-bc92-5e7a36ee637b | -1.35164 | -54.6366 | 2024-11-27 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3747a500-a986-37fb-9bbf-3d57879cddda | -3.32816 | -53.7172 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f53b86d0-d7e8-3114-9c23-834af22227ed | -2.66631 | -49.86949 | 2024-11-27 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b443819f-24b0-3b82-8cf8-3288714d264b | -3.09314 | -51.04201 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8539fe87-a840-3b32-a0dc-73d6a5ff86c9 | -4.30778 | -48.08357 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39746ac3-0aaf-3f11-837c-34d2a6eed948 | -1.3147 | -51.75138 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5bc0412-9e56-358a-b530-e71685025665 | -3.96742 | -48.06466 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bc016b2-69ce-392d-a5f2-6375ed96f64f | -3.11273 | -51.26369 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c22c60e-3d79-32ba-9153-9cea8a084a02 | -1.63583 | -52.50401 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d10dd4c8-6b1e-32cf-945e-636d66cffaed | -3.32655 | -50.0576 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f623041-1a39-3282-84a3-9b3a174c49f1 | -2.83665 | -46.83801 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c1405fc7-deff-3875-8b7f-3b5f539bb78a | -2.61062 | -53.98324 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 912f1309-1947-35b0-afcb-658ba81bfee6 | -4.21915 | -48.6618 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| faabec64-22ce-3718-888d-6ce6dee2c395 | -2.5649 | -46.42267 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdb214a4-a3ae-3186-b4f4-65e4bdbb4cba | -1.86124 | -48.05138 | 2024-11-27 04:42:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c0830cc-1320-38ae-9421-62ec809bf0e8 | -5.02893 | -43.59631 | 2024-11-27 04:42:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb7b99ec-dddc-347e-b3cc-600df38fc19a | -4.26003 | -48.66812 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e7cefc9d-3a59-3cbd-b438-e7111c188888 | -2.45388 | -53.68021 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c8b0032-d97a-3d3e-86b7-caa725faf573 | -2.77069 | -52.9039 | 2024-11-27 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d6f3aef-7d25-3d99-9329-558a231a4bd3 | -5.19442 | -48.19602 | 2024-11-27 04:42:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1e17f26-4f04-3390-8196-df85d4e84010 | -2.81876 | -46.80928 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 540109c6-4ca1-3b73-8a81-590c66a27323 | -4.7256 | -46.57247 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README72.md)
