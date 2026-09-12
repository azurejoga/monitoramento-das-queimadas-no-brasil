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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62344e28-6d0f-3eea-bd66-714c43b015a4 | -5.76344 | -45.09034 | 2026-09-12 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 6019d0bc-587b-3e39-a430-8965ad10de05 | -2.93656 | -50.47137 | 2026-09-12 11:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ce6ce64f-6e83-3bd7-82c7-7553c6947d54 | -3.76588 | -44.08944 | 2026-09-12 11:47:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d574a074-f841-35be-a5c2-52a0b5317ccc | -7.18384 | -45.9266 | 2026-09-12 11:47:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 398a2d7c-e511-36f0-b088-7f803c7725df | -7.20465 | -44.11271 | 2026-09-12 11:47:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e9f583e3-2485-39a1-b237-7431aa5cf0e3 | -6.96453 | -44.54046 | 2026-09-12 11:47:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2e8debda-7493-3ce4-8763-253ad2dd17c3 | -4.37666 | -43.35681 | 2026-09-12 11:47:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 720a0819-eda3-345f-9d5d-5e455c42375b | -7.46793 | -42.12323 | 2026-09-12 11:47:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| ead7963d-c49f-31b1-a0c7-f5eebd990c54 | -7.59813 | -46.12393 | 2026-09-12 11:47:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 50611179-75da-39fe-862b-845a5fe0d057 | -6.758 | -45.00802 | 2026-09-12 11:47:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 87cf429a-4901-32b8-98fd-624c242db82d | -6.51404 | -47.60472 | 2026-09-12 11:47:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 24dcce26-a112-3e31-95cd-ab0924839f50 | -8.02469 | -44.15921 | 2026-09-12 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 60bd76ba-6d2b-3c3f-8390-5d7247516843 | -5.30984 | -43.64767 | 2026-09-12 11:47:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 558ce52d-c475-3ff3-80f5-d98cface58b4 | -7.56514 | -45.16083 | 2026-09-12 11:47:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 460344f4-1518-3616-b3ed-1bbbf09f50c9 | -6.71855 | -45.43589 | 2026-09-12 11:47:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b1d31517-199d-3218-8c72-8488f5822560 | -6.50648 | -47.59466 | 2026-09-12 11:47:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d8e69a7e-971a-3c06-882f-d0a1a517f21b | -2.94665 | -50.47282 | 2026-09-12 11:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 69f8dae7-a7cb-3b9d-97bc-8b6314e83caa | -6.7595 | -44.9971 | 2026-09-12 11:47:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 98a71292-86aa-3051-9ee7-fd0d3649bf8f | -7.99508 | -44.01503 | 2026-09-12 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 41.8 |
| cb59227e-069a-3b6e-b2ae-283bb7624e5e | -7.18 | -45.88572 | 2026-09-12 11:47:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| c762e29b-fedb-3638-b91c-d569989b8e0c | -7.18934 | -45.88685 | 2026-09-12 11:47:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ff60b80e-2d5e-3b45-961b-8d9c418159cc | -4.32433 | -43.82053 | 2026-09-12 11:47:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ce6e5069-88c6-30f3-9f4e-5f30db8d6038 | -7.96311 | -44.01074 | 2026-09-12 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2cbbb3df-f654-3a07-9f11-3bf5fe2a2aaa | -2.95676 | -50.40292 | 2026-09-12 11:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 58c6a57b-bd18-3efd-8d11-a6dc1bc52cae | -6.96296 | -44.55228 | 2026-09-12 11:47:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a40cfa4d-cb6c-33a5-9819-a1f18accaff4 | -6.88107 | -47.42802 | 2026-09-12 11:47:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bd6edbea-f53e-374f-afb9-3b03fcbb3ff7 | -8.04019 | -43.75796 | 2026-09-12 11:47:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 70610487-62c6-36dc-aec8-b4644b81b4eb | -6.20563 | -55.26751 | 2026-09-12 11:47:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| ce1d13b3-ef3f-3b2d-a747-8cd642416301 | -6.5153 | -47.5959 | 2026-09-12 11:47:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 777a6102-c46f-3c4a-b7e1-cdf78e676dc0 | -7.02231 | -44.64366 | 2026-09-12 11:47:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 520a3500-1eba-386c-8d10-7efda0dd1626 | -8.01981 | -44.15202 | 2026-09-12 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f7544fc9-a428-36ca-97b4-6802e89e169a | -7.60739 | -46.12515 | 2026-09-12 11:47:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2005534b-b9dd-3d2d-8e00-de7db921646d | -2.95843 | -50.39138 | 2026-09-12 11:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 7bf5d823-c800-301d-b285-636aeee4b35f | -4.37843 | -43.34367 | 2026-09-12 11:47:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f5486dc6-9838-3c74-a6d8-cd1fbfbfe1a2 | -2.29699 | -48.13116 | 2026-09-12 11:47:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7dd4caaa-11be-3f8d-8e7d-269a20b7cb03 | -2.94671 | -50.40153 | 2026-09-12 11:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 6c1bd3d8-384c-318c-9d6a-ba433aa1a6ba | -6.87981 | -47.43689 | 2026-09-12 11:47:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 9831c657-192d-3c23-a66e-d1fa80aa090a | -7.53733 | -44.91188 | 2026-09-12 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2222bae6-e127-3700-b41d-b9d39f7c9187 | -5.77638 | -45.098 | 2026-09-12 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b1c7f2bb-134f-30d0-83bd-4d99d4b3e04e | -6.89947 | -44.64518 | 2026-09-12 11:47:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 998f0b7b-d880-39e2-afa2-96b172a929a6 | -5.61271 | -44.85163 | 2026-09-12 11:47:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| c3e73b97-cf62-3708-92b6-80bb8e577195 | -7.19706 | -44.11877 | 2026-09-12 11:47:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 3e1156d5-33cb-38a1-9ccb-1bb2136b953c | -7.01387 | -44.63067 | 2026-09-12 11:47:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 91308c1f-7bbe-301d-bd0c-fddb260b84c2 | -6.81898 | -43.19487 | 2026-09-12 11:47:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 47d9cdf8-8c75-3772-b9d3-58b80a5e717b | -1.50055 | -47.24792 | 2026-09-12 11:47:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c4158fa3-6f73-3184-b159-1caae78bf49e | -6.86212 | -47.43448 | 2026-09-12 11:47:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 022864f2-ea05-3c19-8216-cdd0517b976d | -7.41881 | -46.15679 | 2026-09-12 11:47:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 464b4461-d6b1-35bd-a7d1-42908ac7b6a7 | -7.02391 | -44.63205 | 2026-09-12 11:47:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 4a073a65-1683-3962-ac4f-de4dfc7e9951 | -7.01546 | -44.61907 | 2026-09-12 11:47:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| f89b11ea-b3b4-36b7-a9bd-6d7b8b6b3672 | -7.96481 | -43.99765 | 2026-09-12 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| c9253ef4-c691-3e5b-95bb-31d12e6b77a2 | -2.9601 | -50.37984 | 2026-09-12 11:47:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c3c864e2-fb70-3ba5-a521-2457320b4a03 | -5.7778 | -45.08755 | 2026-09-12 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b47d1eed-573a-32e6-8e38-1e745ae7f838 | -7.17863 | -45.89565 | 2026-09-12 11:47:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9af938e1-5ab9-3820-a3a3-d5fd86151f92 | -6.23821 | -51.68396 | 2026-09-12 11:47:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cc5ae552-e338-323d-9777-e6a3b8931285 | -7.27334 | -46.80343 | 2026-09-12 11:47:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 451a3878-7a58-3eac-ae56-934020110645 | -7.20979 | -43.70617 | 2026-09-12 11:47:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 7ccfa9a1-14a4-3d83-8563-e47dd8544778 | -6.74825 | -45.00665 | 2026-09-12 11:47:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e7b712ba-ac09-31cd-9241-ae62fe52c1d4 | -6.89791 | -44.65662 | 2026-09-12 11:47:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a437c5d7-b398-3d7e-be84-a387679a6424 | -7.0123 | -44.64215 | 2026-09-12 11:47:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 83e54e63-4be6-35cd-a646-880d4a41a547 | -5.77302 | -45.0917 | 2026-09-12 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| b2c2b93e-20f3-31f7-bd4d-4b1a88d54807 | -13.62433 | -47.90319 | 2026-09-12 11:49:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6a5f8ecc-688b-3e28-a1a5-bb8f900578c0 | -9.91174 | -45.88336 | 2026-09-12 11:49:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 203c2f8e-5a8b-3d9d-bb2b-d4aeb5ce8862 | -10.54914 | -45.22403 | 2026-09-12 11:49:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 671dbcf0-e51f-3a79-9847-1f41362e8d46 | -12.64725 | -51.40929 | 2026-09-12 11:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 37047f1b-5659-35d7-b440-21bd7e488fd2 | -11.3711 | -46.8063 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 3378a4c6-5cdd-3568-ab16-4b99345d539f | -8.39355 | -46.29763 | 2026-09-12 11:49:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1eb275f3-2807-3bdc-9809-280c7517b377 | -16.3185 | -49.53284 | 2026-09-12 11:49:00 | TERRA_M-M | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| b75602e3-88ee-39cd-892e-36bcdfd609ad | -8.82761 | -46.02488 | 2026-09-12 11:49:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f22390df-5e3c-3259-a1c6-74dd902886f8 | -14.58844 | -52.65625 | 2026-09-12 11:49:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 12e07b58-fb32-3653-a0f3-792e493979a5 | -18.38631 | -45.14693 | 2026-09-12 11:49:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d27b0bd3-2a5d-39af-bfe9-bd067697e2db | -16.49454 | -49.38639 | 2026-09-12 11:49:00 | TERRA_M-M | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 056bd1a7-48d4-32d8-b45c-ec6fb8d97777 | -8.81553 | -46.91286 | 2026-09-12 11:49:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 52734c28-1190-3ce0-816c-85399656160e | -10.33708 | -48.01909 | 2026-09-12 11:49:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 50140410-cefd-38bf-90ea-66639b0c934b | -10.32504 | -46.44662 | 2026-09-12 11:49:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 399e8c11-0bfa-37ba-abba-23dd3f29b944 | -11.08255 | -50.83105 | 2026-09-12 11:49:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2213349c-f9de-3c43-a421-474f97309dac | -18.66231 | -41.98732 | 2026-09-12 11:49:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 76b7804a-52f0-3b6d-b75f-750c91886aa3 | -14.83949 | -48.17148 | 2026-09-12 11:49:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 00957711-fb0f-3099-811a-62d15587b58a | -12.72427 | -43.16015 | 2026-09-12 11:49:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 1bc0cc2a-00d6-3ba3-a39f-78613b623c23 | -13.30658 | -51.63993 | 2026-09-12 11:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ac0dc08f-9f05-35a9-96c1-942358ca673f | -9.67765 | -46.00654 | 2026-09-12 11:49:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1e3a712d-37db-321a-b992-8afc882aa43b | -10.31431 | -46.45548 | 2026-09-12 11:49:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7515ffb4-cded-3648-9979-c5c691b9b75f | -15.05676 | -48.5328 | 2026-09-12 11:49:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 98428cdb-ce46-323a-91bc-c174b09e472d | -9.52988 | -45.44595 | 2026-09-12 11:49:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 1a600edf-d9e1-3631-98a1-9210b2accf7c | -11.41927 | -47.73358 | 2026-09-12 11:49:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6d52fabf-910f-3fc6-8905-24182ced3d80 | -9.67908 | -45.99608 | 2026-09-12 11:49:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a6e79260-965f-32fe-95e1-79a336aebf00 | -11.36178 | -46.8051 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1225c29f-8d35-31ff-88fa-8200f5e6d88a | -13.05545 | -42.32325 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 28.8 |
| a4601b5c-615e-3e60-bda8-9f3bb66deb69 | -11.38429 | -46.84869 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| dd9978a0-b391-3e6c-b617-12283aa9dc8c | -11.37905 | -46.81752 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 305.1 |
| 814ef255-862c-3fd5-b563-156dcd9db946 | -10.9583 | -48.33039 | 2026-09-12 11:49:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| b57f99e3-cee9-35b9-8462-4611e5008ff9 | -11.35256 | -45.78926 | 2026-09-12 11:49:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 128da85d-0b18-3a2c-ab61-ccee1f5f27d3 | -16.14721 | -43.6228 | 2026-09-12 11:49:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2866058f-0824-364e-85e3-b1f9fe4e1376 | -10.47145 | -48.63995 | 2026-09-12 11:49:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 0cb75af1-0d87-3a38-b6d2-4ef5a09f16d0 | -13.26452 | -43.64151 | 2026-09-12 11:49:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| bb98efff-790f-3e55-a591-d4f9194759d6 | -8.8998 | -45.42033 | 2026-09-12 11:49:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 289f80ec-c395-3194-8d4d-80b8356f67b2 | -10.90756 | -47.83142 | 2026-09-12 11:49:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bef58561-755e-3da7-a7d5-033face2323f | -15.49537 | -44.39066 | 2026-09-12 11:49:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 92107cd2-9bf6-3c5a-9dd9-df4f2f771af2 | -11.38294 | -46.85863 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| ffbc00b9-5df8-3e4a-bd04-f24834687857 | -9.31998 | -45.64114 | 2026-09-12 11:49:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4156bc08-7a00-323c-8aed-463487c8e43e | -17.24706 | -48.11679 | 2026-09-12 11:49:00 | TERRA_M-M | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README57.md)
