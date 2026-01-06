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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce15d4e9-c9a9-3026-a1c4-88756fc80099 | -20.5279 | -58.0039 | 2026-01-06 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| c94f351f-6632-339c-9ad4-3b403760174d | -20.5077 | -58.0066 | 2026-01-06 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 2ac284a6-1776-3be7-9f12-fba9977a6134 | -2.5238 | -47.8332 | 2026-01-06 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 17c1c290-0c4f-37b7-b5fc-140b8e7f43ba | -4.3491 | -46.3364 | 2026-01-06 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 69b65713-6138-3d36-a600-42debe872862 | -2.2846 | -53.7822 | 2026-01-06 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 55b171c4-2643-3c6c-b648-f71da0dc04ba | -4.3492 | -46.3142 | 2026-01-06 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 151adbe5-26d1-394a-a65b-3d827860099d | -9.9513 | -36.2024 | 2026-01-06 01:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 181.3 |
| 16509977-06a5-3880-b1be-fe0f0fc3cfa3 | -3.6962 | -43.4432 | 2026-01-06 01:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 89ab4f9a-5a3e-311b-bd87-2353ba134fa6 | -2.5423 | -47.8327 | 2026-01-06 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| be3a3cac-8880-350b-93cb-121acc9ec175 | 2.5442 | -60.3563 | 2026-01-06 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 41.2 |
| a85aa83b-5647-3154-943f-bada5197c70e | -20.5149 | -57.979698 | 2026-01-06 01:42:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2269dca0-5c16-3a83-a94d-3c69c671c4de | -20.521601 | -58.002899 | 2026-01-06 01:42:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 176e2858-f2eb-366d-9a2e-2a90ddc970c1 | -20.524401 | -57.976501 | 2026-01-06 01:42:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 24f93ef5-4a7a-3eb3-b26a-fa2aa5109daa | -20.5054 | -57.9828 | 2026-01-06 01:42:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0b79058f-2d8d-3f0d-8f55-9aa5c4e73cd2 | -20.511999 | -58.006001 | 2026-01-06 01:42:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ab6149e0-589a-3d9d-b27f-dc72f70987e3 | -4.3492 | -46.3142 | 2026-01-06 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 62148716-75d8-37e1-b317-642b2f0d6305 | -2.5238 | -47.8332 | 2026-01-06 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a8c63b98-199d-307d-b7e3-e6d87a90cede | -4.3491 | -46.3364 | 2026-01-06 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8546a99b-cf4d-3b16-a8f8-72cda757814c | -20.5279 | -58.0039 | 2026-01-06 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 12713b4a-2dfb-32e0-b7a7-a18678774623 | -4.3491 | -46.3364 | 2026-01-06 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| fb0b9127-bcd3-392f-843f-fccc75e1da5e | -2.5238 | -47.8332 | 2026-01-06 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6125bf83-9d76-32da-aba4-1a77101bf8fe | -2.5238 | -47.8332 | 2026-01-06 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e896930f-adbf-3ed1-a80e-0d43c9a45af1 | -2.5238 | -47.8332 | 2026-01-06 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| eadb0d6c-ee1f-3d56-9b5c-d84c2e83423f | -2.5423 | -47.8327 | 2026-01-06 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7b8d5bc1-edd5-3628-b688-cde281683869 | -3.6962 | -43.4432 | 2026-01-06 02:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 46ab232a-f141-30c1-9e0c-ad11020ea9cb | -9.9706 | -36.199 | 2026-01-06 02:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 90.6 |
| b2d527a4-b5d0-318e-9938-f6535f2f2c79 | -9.9513 | -36.2024 | 2026-01-06 02:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 158.7 |
| 2de2df65-3caf-3313-b12a-885e300060cc | -2.5238 | -47.8332 | 2026-01-06 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 8e081d71-3ed8-3023-8a11-2eb0d9650211 | -2.5238 | -47.8332 | 2026-01-06 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| bd0df57b-1cee-3f03-8ba9-1179812c20cc | -2.0832 | -53.5237 | 2026-01-06 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e5fbe6b8-f190-3f66-8d39-66a60eaef569 | -2.1016 | -53.5233 | 2026-01-06 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 98a5e57c-3478-3b8d-a4d2-31c847d3e872 | -9.4777 | -35.7975 | 2026-01-06 02:50:00 | GOES-19 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| df6ea3cb-331b-32da-b0a4-749c33ade391 | -2.2846 | -53.7822 | 2026-01-06 02:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| a3fc7367-5469-3db9-bf4e-15cd0bcd6a6b | -9.497 | -35.7942 | 2026-01-06 02:50:00 | GOES-19 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.1 |
| 0f4eb39e-f023-3331-be53-2d3aee24ac40 | -8.04287 | -35.14799 | 2026-01-06 02:51:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 5c945137-0f80-3fec-a6c6-fba7baa36c5b | -9.51165 | -36.06712 | 2026-01-06 02:51:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 710f43d1-0521-3faa-9a23-c57d3d803c64 | -7.87754 | -35.24364 | 2026-01-06 02:51:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f5203d7d-a562-3de3-97d5-5502482be3b2 | -9.942 | -36.04657 | 2026-01-06 02:51:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c5035093-ec53-3da4-867e-d87347348670 | -7.87051 | -35.24192 | 2026-01-06 02:51:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 996d123f-bb2c-31d0-8b27-f79c61910647 | -9.51048 | -36.06691 | 2026-01-06 02:51:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 96c09116-b702-36b9-83f8-2ec449bf139c | -9.50904 | -36.07402 | 2026-01-06 02:51:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3eefe2b7-4c6f-3efe-92b5-24d14225b4a4 | -9.94076 | -36.04263 | 2026-01-06 02:51:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4d4d9ea2-2c27-3b4f-880a-fe196b256610 | -9.9435 | -36.03942 | 2026-01-06 02:51:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9f37c93f-c17a-3877-bca8-ec25f2bbe9e7 | -8.03991 | -35.14742 | 2026-01-06 02:51:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 9ce11a5f-1de1-3ae6-9f98-b8ce2a909361 | -9.51017 | -36.0742 | 2026-01-06 02:51:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7a0d86d3-dded-30de-8e2b-441e02ba2939 | -9.503 | -36.07241 | 2026-01-06 02:51:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 39f45b33-c4bb-393d-954c-7555225c5e0d | -6.63864 | -38.72624 | 2026-01-06 03:12:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8fb8e615-ab20-33e8-afd8-b31cb9456220 | -9.5124 | -36.07027 | 2026-01-06 03:12:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f8b52f1b-2740-37af-aee1-e8bf5810fe37 | -6.58619 | -38.45869 | 2026-01-06 03:12:00 | NOAA-20 | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 17cef5c9-c956-3e23-a488-4febd29823d0 | -9.38338 | -35.85352 | 2026-01-06 03:12:00 | NOAA-20 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 80b92176-ffb5-36f4-9374-a82c09438106 | -9.94106 | -36.04021 | 2026-01-06 03:12:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| fbb38182-0621-323e-b8f3-298d4e90749a | -9.50754 | -36.06926 | 2026-01-06 03:12:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d53b4718-6915-3309-8222-b07ce764e0a6 | -6.49265 | -39.04216 | 2026-01-06 03:12:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 76d29c82-87c1-3261-ad65-1b4807f4fe1a | -9.02519 | -35.76858 | 2026-01-06 03:12:00 | NOAA-20 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d673c2aa-25b2-3aeb-9d2e-fb718ec471e5 | -7.86922 | -35.2411 | 2026-01-06 03:12:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c302dd7e-742f-3d32-bae9-55331b04b5fa | -8.43307 | -35.58564 | 2026-01-06 03:12:00 | NOAA-20 | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e94b0866-09e4-3f68-8fe3-f2391522e3ab | -8.43398 | -35.58046 | 2026-01-06 03:12:00 | NOAA-20 | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a1fed3b7-f774-320b-9758-e8394142888e | -9.94589 | -36.04113 | 2026-01-06 03:12:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5da8ca19-6d80-35b3-8a5f-58f851594ce1 | -7.87394 | -35.24206 | 2026-01-06 03:12:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7da379cb-b5b6-3057-80ba-cf55486a3382 | -9.38437 | -35.84816 | 2026-01-06 03:12:00 | NOAA-20 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1da71b46-ba14-3bca-ba4a-2d4e69d362bc | -7.31688 | -34.93827 | 2026-01-06 03:12:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5fc451f0-fe2b-3c5b-bda7-b69cabf0a94a | -8.43787 | -35.58658 | 2026-01-06 03:12:00 | NOAA-20 | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b9361b11-5ce4-33e7-a4ed-d7aa4d91ebb4 | -9.05881 | -35.58049 | 2026-01-06 03:12:00 | NOAA-20 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fa5f1fe1-9bce-344d-aee7-2c2aaf192789 | -7.8735 | -35.24082 | 2026-01-06 03:12:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| e12966c0-a137-3935-a482-d9b4ae4f6844 | -7.86877 | -35.23985 | 2026-01-06 03:12:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2e92e339-7f3f-37ac-8cd8-db67e6c61f31 | -5.23605 | -38.13834 | 2026-01-06 03:12:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 58bb5758-9267-38e6-955f-c78593d38d3a | -6.49353 | -39.03733 | 2026-01-06 03:12:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9b0d6bc9-861a-3a3b-9a9b-a781075f60a7 | -6.43405 | -37.13437 | 2026-01-06 03:12:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 8.3 |
| acc04faa-02cd-309d-8e3e-bacb508e8607 | -6.43341 | -37.13803 | 2026-01-06 03:12:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ca88a0b6-a93b-3bfd-bcf3-bc494507c2e6 | -6.587 | -38.45422 | 2026-01-06 03:12:00 | NOAA-20 | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dbaedecc-21bc-3584-b20f-9c5acf37d51a | -10.92782 | -38.81934 | 2026-01-06 03:14:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f6c8d17e-8bcc-30b3-a5e9-95d4a382d000 | -3.6962 | -43.4432 | 2026-01-06 03:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e5058996-d023-3302-a0b3-d6f6a8b1ee7f | -0.36462 | -48.44281 | 2026-01-06 03:59:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1933610-0275-3265-9dd2-f6697f7446c7 | -3.12261 | -39.75895 | 2026-01-06 03:59:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 60814e0f-82f4-33e8-90b1-a27e03efba08 | -1.14286 | -48.10441 | 2026-01-06 03:59:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 46f223cd-07f4-3790-8171-7414ea365d6c | -1.14341 | -48.10099 | 2026-01-06 03:59:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 60c781d3-4e18-39cf-8ea7-d101e7794b72 | -2.91282 | -40.46475 | 2026-01-06 03:59:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 924b4140-4199-3bad-aa5a-ad0b9e8b272b | -2.92609 | -41.71207 | 2026-01-06 03:59:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 67b7c863-1ba9-3258-8d89-e4c0a4cd22b8 | -1.36048 | -49.41661 | 2026-01-06 03:59:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7874296-aae1-39f7-994d-49e29008474e | -2.9226 | -41.71154 | 2026-01-06 03:59:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 89b17e5c-1029-3fb3-ab25-bdc60425a4f2 | -0.36405 | -48.4465 | 2026-01-06 03:59:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b1cb690-89b8-36fc-aa6c-89018d530beb | -1.04195 | -47.22854 | 2026-01-06 03:59:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d052e3e-0a14-3d15-b998-a517acacd166 | -0.37076 | -48.43997 | 2026-01-06 03:59:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94f06cd7-1329-34ea-9a3f-4e724e99b4f0 | -1.78437 | -45.26134 | 2026-01-06 03:59:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a473a2eb-b524-3917-ae65-ffb67fb9ecd5 | -6.58762 | -38.45105 | 2026-01-06 04:01:00 | NOAA-21 | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 379e821a-899d-30c5-a878-98ec09dd8411 | -4.12311 | -43.89041 | 2026-01-06 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d5e1864-e3ae-31c2-8d38-086b89e85a8a | -6.50345 | -39.54763 | 2026-01-06 04:01:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f5933244-d07f-3500-b2b8-e59619e4fae8 | -10.21166 | -36.4206 | 2026-01-06 04:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 63abbd64-f1ea-3709-b7c8-3b7381e2fb70 | -7.08405 | -39.11551 | 2026-01-06 04:01:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b72fbd6-3ff8-3699-a3a3-3811d375f8bf | -10.82357 | -37.15082 | 2026-01-06 04:01:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ddf4b869-fb29-378b-b79b-55983bb248ab | -3.69537 | -43.43654 | 2026-01-06 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 943d1ddb-8b76-3950-a3db-6a4229e22594 | -2.53884 | -47.82971 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efcd3e8e-5343-369a-9a1a-66d4b47cabf4 | -2.53097 | -47.82611 | 2026-01-06 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c276b20-4ca1-33c0-b8c6-9e470dc1db03 | -10.21005 | -36.42388 | 2026-01-06 04:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 627f9ef9-aa75-3deb-9c22-a5a92f85c7bd | -3.7213 | -47.2112 | 2026-01-06 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41cb04d8-57b1-3cef-abbc-34f5f1d7c866 | -10.9284 | -38.81567 | 2026-01-06 04:01:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a77dc83e-801e-33be-a431-c7405fecadfd | -3.69914 | -43.43714 | 2026-01-06 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 75cd465b-4179-3f8e-b2ac-65ee2b1f28ed | -3.48993 | -41.70013 | 2026-01-06 04:01:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 57bcb509-a9cb-3777-8cf1-bb76436b5514 | -4.39896 | -43.57498 | 2026-01-06 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af40bbe8-606a-3e8c-9156-b8a9d8346d61 | -10.53879 | -36.97916 | 2026-01-06 04:01:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README5.md)
