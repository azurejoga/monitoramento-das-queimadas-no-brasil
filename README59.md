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
| d3549dec-bff6-358b-92e3-65426a3fb948 | -5.83981 | -47.43171 | 2024-10-11 04:23:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33b91a81-ff64-31cb-85f5-bdcf1284fc15 | -5.83924 | -47.4353 | 2024-10-11 04:23:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a69ef4be-680f-33b0-838c-43a71b873678 | -5.83645 | -47.43117 | 2024-10-11 04:23:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 174293e2-aa5f-3449-a65e-1a1eb2addcf0 | -5.66692 | -46.5337 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aff61f54-d760-3d15-973a-7826ff83d42b | -5.64803 | -47.92601 | 2024-10-11 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d40d91d-c623-3da4-a8b3-fe2724c8f689 | -5.64461 | -47.92547 | 2024-10-11 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61a11305-cd37-3656-85e6-d54e8de1b311 | -5.55326 | -46.69301 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ec81929-8c00-39e6-91ce-d3f260f8cc70 | -5.55271 | -46.69649 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27d1ed78-a91e-3add-9d9b-738db169c9e9 | -5.55247 | -47.75288 | 2024-10-11 04:23:00 | NOAA-20 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfc8be73-9901-3156-b50e-3ba008f40696 | -5.55216 | -46.69996 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c391d5d-2008-39d7-ba63-78282af82849 | -5.55189 | -47.75655 | 2024-10-11 04:23:00 | NOAA-20 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1470c065-d460-3431-b350-dc22004eac64 | -5.5505 | -46.68901 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c284552a-2429-3d89-8178-462bcf38cc69 | -5.54995 | -46.69249 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a61e609-808f-383a-aa93-a4627bfb5623 | -5.54773 | -46.68501 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a7a6ab7-134b-386a-aa08-c7b534f94451 | -5.54387 | -46.68796 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89d0492a-1514-3117-891b-50e7887f2c9a | -5.53447 | -46.68291 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3197feb-d713-39ee-8307-eb291d979ad3 | -5.53392 | -46.68638 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f59b67c-ec67-3d74-8e64-b159e3d5e8a8 | -5.53337 | -46.68985 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c02c45ff-6b42-3925-acbb-d3eac3e6a267 | -5.52615 | -47.10112 | 2024-10-11 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 525c23df-3a54-3c25-937d-9a119ddeb50d | -6.84431 | -46.93029 | 2024-10-11 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 516b8fd0-62c5-3b11-8e44-60ec8339c1e0 | -6.70142 | -47.52764 | 2024-10-11 04:23:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 52df8abb-01c8-3863-9c3c-f55a74a0deaf | -6.62013 | -47.12345 | 2024-10-11 04:23:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4bcd6b1-f180-367e-9564-8ac214c55e13 | -6.61832 | -46.72671 | 2024-10-11 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ad6dc41-c7cb-37da-b99b-2e8efdb9c76e | -2.03659 | -48.02613 | 2024-10-11 04:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09fdad86-e93a-3a27-80d9-258c63442bc9 | -2.03656 | -48.02435 | 2024-10-11 04:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9df378a-698c-3588-b731-89d80db72444 | -1.91023 | -47.88497 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18eb6b3c-2564-39ef-8eba-a46c13b964c6 | -1.9067 | -47.88444 | 2024-10-11 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d297d13-8742-385c-bc26-062f9eff741b | -1.79956 | -48.06034 | 2024-10-11 04:23:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09b9503b-5354-3a52-9fb9-6444e5f325cc | -1.33592 | -48.34871 | 2024-10-11 04:23:00 | NOAA-20 | ANANINDEUA | PARÁ | Brasil | 1500800 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8b6493f-d7ff-33bd-8397-cf914bc91224 | -1.33565 | -48.3459 | 2024-10-11 04:23:00 | NOAA-20 | ANANINDEUA | PARÁ | Brasil | 1500800 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d318abea-09f3-3333-9064-6bb2dbe09ef7 | -3.70185 | -47.61626 | 2024-10-11 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 799ef4f1-1a6d-35ee-86c8-46bad7180de6 | -3.45949 | -47.66287 | 2024-10-11 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87eca248-cfe2-3a73-988d-04e99ea938dd | -3.42929 | -48.81969 | 2024-10-11 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f81d2c59-1fab-331d-a158-2523a462a8e2 | -3.42835 | -48.82103 | 2024-10-11 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb29c62b-42a3-3505-ad73-780c64c25d0e | -2.9713 | -47.99972 | 2024-10-11 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 340a9d6d-8b19-3771-9194-b6e09299edbb | -2.97069 | -48.00359 | 2024-10-11 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4a9e071e-a1c5-3fab-affa-2d896f9a626e | -2.9678 | -47.99916 | 2024-10-11 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0422614c-b179-3b22-8444-189f7b22713f | -2.87533 | -48.91036 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30e71e11-9f7f-35bc-942e-910698f1e5b2 | -2.87515 | -48.909 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 313b98c0-4874-3090-a95d-5d9adae62c5e | -2.876 | -48.90605 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66236a9c-0e94-3539-b182-edd06cb66bf6 | -3.05686 | -47.48268 | 2024-10-11 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fdb2d3d-5601-3f18-91d9-525ff247a15e | -2.96718 | -48.00304 | 2024-10-11 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b77c5ebd-106b-3e28-ac84-0b1f86c40c09 | -2.93548 | -47.84337 | 2024-10-11 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c699365-22f7-3fca-868c-0174b695ed9f | -2.80665 | -48.70734 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 11e7fc1d-db91-3299-ae6b-7d6b86a5e0e8 | -2.80439 | -48.69835 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8082c97-8eae-3708-a683-0eeeb5ee6352 | -2.80371 | -48.70255 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7a80674-7183-3db1-b173-4f61862ac8c8 | -2.80302 | -48.70676 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c3e00718-f437-3e56-869a-e57354ed5e08 | -2.80076 | -48.69778 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f9e4fb7-db7b-37fa-84ea-3f63370109a3 | -2.80008 | -48.70198 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29eace2a-2e33-3f1e-8857-36a55039dc6a | -2.79994 | -48.6992 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9d30d7a-b165-32cc-927c-5c390e782216 | -2.75208 | -48.6959 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 998b1918-41fb-3092-9806-74ec37a11c58 | -2.75046 | -48.68268 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f27b6ad5-aa43-304a-aeeb-11cc5b0d2808 | -2.74683 | -48.68209 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad894ab2-b406-3673-9a51-237c4b324552 | -2.72784 | -48.73098 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b0222c4-9584-3b42-b4f6-ae9d3556524b | -2.71853 | -48.7425 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f089e495-452a-3a68-8ce0-9c8a4e4b9b1d | -2.69559 | -48.63097 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 281ec3bc-5854-391b-823f-401e681c6f9f | -2.69443 | -48.6319 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dcca627-f4b9-35eb-b11c-65f972a0d125 | -2.69377 | -48.63608 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65186162-f33c-3fb1-b44b-2053643c3def | -2.69081 | -48.63132 | 2024-10-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2cf487d-02bd-3b69-b886-d3a85f16a44d | -2.48098 | -48.05457 | 2024-10-11 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25ebc1b8-e6c1-3c0a-ab50-94edc4f17130 | -2.47137 | -48.06933 | 2024-10-11 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23ec84e7-5b20-3150-bbb2-c6b4156eb3e6 | -2.46086 | -47.81576 | 2024-10-11 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31849c85-64e3-3774-a68d-ae43b72cdbca | -2.46008 | -47.84332 | 2024-10-11 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22a377fc-be80-3dad-b57c-d46b91a0b1ab | -2.42085 | -48.4509 | 2024-10-11 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 192d96e0-d68e-344e-bd40-ab489b7a0979 | -2.42018 | -48.45503 | 2024-10-11 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb3e57f6-604f-3f0f-b478-511a62bc6f06 | -2.41658 | -48.45446 | 2024-10-11 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 219fdc90-fa20-3cfc-8140-bd5536e41c7b | -2.40187 | -48.87292 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8cae8e2-0b01-323d-bd9c-4e51cbdb0422 | -2.33738 | -48.40945 | 2024-10-11 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a346c79-57dd-33e3-a135-377e2a107c44 | -2.32679 | -48.4756 | 2024-10-11 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30abab97-3adf-3133-81b8-7551e66b7d80 | -2.30955 | -48.42193 | 2024-10-11 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9acca70-ab4c-318d-8ddd-7d89d6343df4 | -2.2393 | -48.78686 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d0247a9-8025-3a16-bb84-645b9380be4f | -2.23619 | -48.02264 | 2024-10-11 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3f7cdd86-a8f1-3fc5-80bb-d97924701984 | -2.23266 | -48.02207 | 2024-10-11 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f87dd63-f1bd-399b-bad7-de41fd7a4f17 | -2.19084 | -48.2417 | 2024-10-11 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7de676cb-5483-3b61-923a-3bf053369b3f | -2.18727 | -48.24111 | 2024-10-11 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71448384-59f9-36a0-aa47-9d1ee742d859 | -5.07199 | -48.08072 | 2024-10-11 04:23:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8b8a50a-2eb5-3a7b-93ec-4fdead381ae4 | -4.97438 | -47.92715 | 2024-10-11 04:23:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 684bb62b-0ed0-3b7d-875b-c282464c8f0f | -4.97378 | -47.93091 | 2024-10-11 04:23:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 561784a5-a662-3d0b-95fe-d06fd3d6f008 | -4.97035 | -47.93036 | 2024-10-11 04:23:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29f18d0a-82bf-3aaa-85f4-041599e8fe9b | -4.77754 | -48.08176 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1ecb627-1589-32a5-8b30-8095b65332be | -4.57834 | -48.01224 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 360199bc-afad-32eb-b5b9-7c9fc07f3f43 | -4.48571 | -48.11083 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 693d6efe-bd8d-3ac8-9585-637ec860b8ec | -4.48225 | -48.11029 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5c848588-b8ec-3e60-a26c-9d5951b6884c | -4.20406 | -48.13376 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b7fce9d-b0a6-3560-b41d-bac9d72039ae | -4.20344 | -48.13761 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b67982a-af2e-33a5-8f32-e1e445cbc6e9 | -4.20058 | -48.13322 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 65b83744-326b-3d79-979f-0acc783ea77a | -4.18108 | -48.02161 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3da054d9-2807-38f1-bdf1-75d6957a9e1c | -4.18003 | -48.00585 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 311f22af-d59d-3588-b60e-41514e463805 | -4.17657 | -48.0053 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 366183f7-0336-3db1-9890-819d97a16090 | -4.16884 | -47.87618 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42e4a82d-9a7b-33a4-8bbe-9bce7b5a9370 | -4.14473 | -47.87228 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45a505a4-c4d3-3d92-8954-50d42a422f24 | -4.05302 | -47.92007 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90d79e5b-9719-39d1-a30d-01a894fb8e97 | -4.05241 | -47.92387 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9940594-15a0-34a4-bf2c-cf47826615bf | -4.04896 | -47.92331 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac188457-eee1-3aef-8ed1-68042db7db91 | -4.04835 | -47.92709 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f7b0e0a-55cb-3403-9ce8-c76f9a2176fe | -4.96601 | -49.06852 | 2024-10-11 04:23:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4bbab726-4ab0-3640-80e0-bca1e52d56e1 | -4.835 | -48.93405 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d99cff7-a4ab-3efc-9186-cc266624f1c1 | -4.78146 | -48.88835 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 026de027-7cad-3f47-bac1-8bf4921c1942 | -4.74409 | -48.86962 | 2024-10-11 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 955e1d21-2cc8-3351-bae7-494ac35be465 | -3.89554 | -48.36021 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README60.md)
