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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d38e961a-7a2b-3eb5-9ce7-f377e1c32210 | -13.68513 | -43.00471 | 2025-11-14 03:55:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6ece6064-150d-3157-aec9-f4764aa9ff3c | -15.95804 | -44.21785 | 2025-11-14 03:55:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f8c610e-69b1-3e52-b6b4-af98f2eaa572 | -2.24254 | -46.07867 | 2025-11-14 03:55:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acd3d1f3-c781-3aa5-9cf6-eca361f341a6 | -3.41659 | -41.18122 | 2025-11-14 03:55:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 75a0ca13-95b5-3921-964c-f8d3f2e48dc1 | -12.43446 | -43.17619 | 2025-11-14 03:55:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb1f0cda-7328-3813-bb85-89f82ee16f4e | -12.06814 | -48.20648 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7b9eb23-a1d8-319d-a6c7-7f94f51e0c99 | -3.01032 | -49.43994 | 2025-11-14 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 969c1776-b021-352d-a7fd-21f107e504ce | -10.74954 | -45.06698 | 2025-11-14 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31de781c-d77b-3c15-b4ee-ae68399a88fd | -9.93479 | -45.09673 | 2025-11-14 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bc583b1-b7fa-3803-b5ec-50973e0b1e31 | -2.52436 | -47.80771 | 2025-11-14 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e0ed3afb-79fe-39e0-9b54-5c8aafe3818f | -9.68009 | -47.89416 | 2025-11-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8dde1cc-d3ff-303a-af8b-d086f64a7a02 | -12.71007 | -45.42873 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 279d9d54-2336-3f89-be0a-e5db9b1e8129 | -10.80498 | -44.85476 | 2025-11-14 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b530374b-3370-386c-ae2b-7ec3638e9a2e | -4.30447 | -46.26948 | 2025-11-14 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4264fbf4-f9a1-3576-9927-5d63c027417b | -11.84823 | -49.22821 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6ad2475a-2843-39a9-962b-33200eeb43db | -10.33536 | -48.0694 | 2025-11-14 03:55:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85ebd420-141e-37f8-878e-9268d0af8164 | -2.96411 | -41.58221 | 2025-11-14 03:55:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fddd8d41-5bd6-36fe-8c71-526e655f691e | -5.0277 | -41.10434 | 2025-11-14 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 40ed0ee4-b701-385a-b273-4e80cd3fc926 | -3.91469 | -44.32452 | 2025-11-14 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f19849fb-4ca7-3fb6-bfde-3f74dbae44a2 | -12.71564 | -45.42169 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 277de139-3f35-31bc-931d-32c9a088e96a | -4.4103 | -41.48117 | 2025-11-14 03:55:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d28727f-5538-3781-98be-1ccdaa1abcb1 | -4.26703 | -42.29638 | 2025-11-14 03:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0ac8f249-3e94-3f87-b261-cf112e04f45d | -2.90066 | -48.05999 | 2025-11-14 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de45d876-0f9b-357a-8652-d564ab7c2c51 | -3.95253 | -47.4996 | 2025-11-14 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23c2a251-b4d9-30a8-ac30-efc9dd3c9154 | -12.71077 | -45.42482 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9c292475-12c8-39c5-bf28-19ebb2dd9bb3 | -14.98133 | -47.86639 | 2025-11-14 03:55:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3849507-4289-3dfe-9080-191294ccab9b | -14.66837 | -46.56459 | 2025-11-14 03:55:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11645489-a5e9-330c-87bd-784c84e2427e | -2.96005 | -45.75851 | 2025-11-14 03:55:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ef6d5b5-94ae-30b4-b204-c6a3c648d6ee | -10.76196 | -45.02028 | 2025-11-14 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ca2f2a6-ee78-3536-8f89-6e8b28b7e6d8 | -7.79068 | -49.61821 | 2025-11-14 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1d7c80f-c296-3d0a-8c14-be5397276e25 | -5.39614 | -37.86456 | 2025-11-14 03:55:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 01d75fcf-f04d-3bc5-bc09-2c56661ba6ee | -4.29016 | -41.80952 | 2025-11-14 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 45f6a4d7-78c6-30cd-91d2-5a2fd84aa283 | -3.95318 | -47.50204 | 2025-11-14 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49df7786-b3c7-3b02-bc33-4e2cc0b0273c | -13.76661 | -43.16679 | 2025-11-14 03:55:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c279fc43-e2f2-3f2f-a541-35fd9c4f8887 | -11.82626 | -47.79095 | 2025-11-14 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c148be7-7371-36d2-9c0e-73a533eeb420 | -9.85464 | -44.16449 | 2025-11-14 03:55:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e7758f0-221a-352b-98a8-ae21b55ea9c9 | -3.69951 | -39.89391 | 2025-11-14 03:55:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6be287a8-0eba-36ba-81ee-6a3a3d865877 | -11.85582 | -49.21835 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 477fd3d2-cd23-3c01-a41c-adc8e1d2ba1b | -17.03204 | -46.75659 | 2025-11-14 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6548abb4-4130-394e-8ef0-6f94f454ebec | -18.58969 | -46.55758 | 2025-11-14 03:57:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 377db266-66b0-33a8-8084-6157499705ad | -20.8559 | -43.95387 | 2025-11-14 03:57:00 | NOAA-21 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3a7b00da-f029-3877-80cd-8f5924ced06a | -20.10465 | -41.6771 | 2025-11-14 03:57:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4960003e-e15d-399b-b42a-8e1095415b3a | -17.36997 | -41.71119 | 2025-11-14 03:57:00 | NOAA-21 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5cc968d4-f3cd-3c25-8181-3fca6bb2fac6 | -17.969 | -47.25433 | 2025-11-14 03:57:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db4842cc-127b-35fc-8475-f74ef83cb6e1 | -17.42459 | -41.69075 | 2025-11-14 03:57:00 | NOAA-21 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 22efcc12-9fa2-321c-a5f3-6c409de1872f | -18.05503 | -42.48386 | 2025-11-14 03:57:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 72c8fd8d-be78-3b7e-8c09-97a4bbed6e5a | -16.6799 | -47.70382 | 2025-11-14 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c175ee4-b423-3ae7-921a-b97ee4586e9b | -16.54509 | -49.35835 | 2025-11-14 03:57:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 188ec224-9fcf-3060-83a6-e423071fd04e | -17.79459 | -44.9824 | 2025-11-14 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fb65a81d-5ddf-3dc3-b2da-73acdb87a2be | -21.11598 | -48.61003 | 2025-11-14 03:57:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0e2034ee-8759-33f1-8fee-3bad950bc67c | -17.98857 | -42.99175 | 2025-11-14 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8ae65de7-5566-3818-86c8-fa06ae3ad41b | -19.47482 | -46.92041 | 2025-11-14 03:57:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac49aeb2-cb8d-3ffc-9fbb-7a7e40851002 | -19.07771 | -44.86222 | 2025-11-14 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55d5816d-3a4c-3de2-a4b5-093450110b02 | -22.81339 | -47.20306 | 2025-11-14 03:57:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cff0db5d-5016-3230-8a09-8215821b6ca6 | -20.3494 | -41.7426 | 2025-11-14 03:57:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3d80bc53-18e1-3545-a9ff-571df77661ef | -20.53587 | -41.98281 | 2025-11-14 03:57:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7e45ff2c-3e1f-39d0-8c54-5a54d56ee533 | -16.54628 | -49.35239 | 2025-11-14 03:57:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cfa2cf1a-4a9e-3942-b340-8bc45607d80e | -22.2352 | -42.63486 | 2025-11-14 03:57:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1d2c4d21-b852-3247-bdbf-50c13b48630d | -17.16462 | -43.08186 | 2025-11-14 03:57:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ad5d4cf-5886-31f2-b167-35a0087083e5 | -20.10407 | -41.68075 | 2025-11-14 03:57:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 924927b7-e11e-3d16-a86f-b485a8441a9c | -21.11156 | -48.60913 | 2025-11-14 03:57:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 64f591a4-5e31-39d3-85fc-761dfeedc089 | -18.83848 | -39.85386 | 2025-11-14 03:57:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6f713a0e-e690-3eb8-8dee-5ee64eadd5d4 | -18.32309 | -46.6546 | 2025-11-14 03:57:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf30c07a-e334-398c-a2af-cdd65e4c5eef | -18.76594 | -45.28439 | 2025-11-14 03:57:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 475fea47-df62-3f25-ad18-baa2054898d7 | -17.62636 | -39.92261 | 2025-11-14 03:57:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0e8982ec-2a5b-3ba5-9ae0-c7e18f0a8fb9 | -18.22768 | -44.19653 | 2025-11-14 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 273d557b-15d6-3e56-ba25-2623f44190c2 | -17.54684 | -43.93154 | 2025-11-14 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c744a9a4-fa89-3345-be23-97e6467bfc19 | -19.47408 | -46.92424 | 2025-11-14 03:57:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5508c26-b190-3c43-b6f7-3ea784953454 | -18.32058 | -46.65344 | 2025-11-14 03:57:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fa51447-6826-35f0-a04e-2a0e3862a728 | -17.96983 | -47.24995 | 2025-11-14 03:57:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df3dbb06-5629-3c04-a506-bea136d1c22f | -21.65379 | -48.63083 | 2025-11-14 03:57:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67024c99-797e-3f86-90c2-c6cdbcf581d2 | -18.69857 | -39.99481 | 2025-11-14 03:57:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 92765f45-b1ae-3d71-8513-85b1a0dd0684 | -16.35795 | -46.00583 | 2025-11-14 03:57:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5680a434-3914-379f-ae4e-9415756c082b | -19.63335 | -40.25796 | 2025-11-14 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6d117f76-0152-352b-887f-2bcdacc417e4 | -16.30714 | -45.0979 | 2025-11-14 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9bbe96a-124f-3fed-8b62-3f81b33364c9 | -19.07851 | -44.85766 | 2025-11-14 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e74d131-315b-3777-854b-ce75e0897ee4 | -19.47494 | -46.92501 | 2025-11-14 03:57:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5eb0bf3-9d3b-3318-88fe-ae345ddd1bbb | -15.85094 | -47.45314 | 2025-11-14 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8371547e-0cdd-3cbe-9c93-e1a99ffd9d08 | -20.5386 | -41.98711 | 2025-11-14 03:57:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 01a1d8e6-a617-3178-b009-0481d27624aa | -18.19246 | -42.55087 | 2025-11-14 03:57:00 | NOAA-21 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b56831ba-36a5-3bba-9456-0602011c04dd | -16.30546 | -45.09972 | 2025-11-14 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f69af411-4857-3fc8-8a2a-7a44dfeffc46 | -16.51905 | -43.54381 | 2025-11-14 03:57:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19fbb329-540b-38e7-bf14-a2b2a41f652b | -17.79835 | -44.98306 | 2025-11-14 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c4899031-9b28-36ac-8889-24b17971f869 | -21.08652 | -43.90121 | 2025-11-14 03:57:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a500026b-7b1c-3b87-8fd9-f5a8cd6db513 | -19.94945 | -44.71918 | 2025-11-14 03:57:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0fd6596-00af-3e2d-bcd9-a6803263f3ab | -22.8654 | -42.39648 | 2025-11-14 03:57:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9a2543fc-4a97-367e-b2d4-8396c172b0c9 | -17.5438 | -44.7033 | 2025-11-14 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fef2b82-0ffa-33c8-99ce-90fc61d0e08b | -17.98479 | -42.93096 | 2025-11-14 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4da869ed-75de-3157-b9bd-0e05dacb5f0a | -22.81216 | -47.20462 | 2025-11-14 03:57:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ccc87e72-d674-3e3a-82eb-b0266562712d | -20.10076 | -41.68016 | 2025-11-14 03:57:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 41951d83-2800-3525-9b77-aa9de7b2afbe | -18.71045 | -43.00857 | 2025-11-14 03:57:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 77ffab70-9740-3b12-9428-6567c8ead0b2 | -17.37329 | -41.7118 | 2025-11-14 03:57:00 | NOAA-21 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15398b01-a023-3acb-a7f3-5e2ceeae4906 | -17.36938 | -41.71482 | 2025-11-14 03:57:00 | NOAA-21 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 99023c8c-7147-3939-b2a4-9c6b9a598ae5 | -21.11471 | -48.61232 | 2025-11-14 03:57:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| cb051988-52a2-30ac-9711-c81bf47481f0 | -17.62969 | -39.92316 | 2025-11-14 03:57:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c4303c53-c1b9-3b5b-85c6-0aaa802ce6a6 | -16.54569 | -49.35532 | 2025-11-14 03:57:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24e3ee31-b955-3ffa-8218-4be706f92cc4 | -19.47565 | -46.92117 | 2025-11-14 03:57:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4aa3087b-c695-350a-bbc7-ea574eaeae7b | -17.63054 | -46.70623 | 2025-11-14 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 476eaaec-7418-3130-8e4d-21739b1003f3 | -17.09988 | -42.24311 | 2025-11-14 03:57:00 | NOAA-21 | JENIPAPO DE MINAS | MINAS GERAIS | Brasil | 3135456 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fa1685ec-5fb2-3cf5-992c-7b1dd2cac8b2 | -20.53529 | -41.98651 | 2025-11-14 03:57:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README24.md)
