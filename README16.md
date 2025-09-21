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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab5efbe7-0438-35fe-bc3a-163aeaef5f90 | -11.64843 | -52.86221 | 2025-09-21 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e6e1c39d-41d0-30a7-a277-5922f9dfeaff | -14.62174 | -48.27452 | 2025-09-21 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e5da886-7be6-308f-bf70-c394e7d6f8d9 | -14.97315 | -44.43304 | 2025-09-21 04:10:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e137f8e3-e9e8-379c-9e60-6dd80a7ab4b9 | -13.25803 | -47.2813 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0aa54c9f-bf5a-3f1b-8966-7bd33caee97d | -16.59917 | -45.09782 | 2025-09-21 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdc35ff6-afbf-3418-98e5-8d58f8dafe34 | -12.42472 | -45.12558 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1325858-3ba5-3a5c-a5e2-be1ecfe61ddc | -18.04533 | -43.84895 | 2025-09-21 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 26f0c4b1-3326-3119-9530-6ae80328eda2 | -14.21414 | -41.66883 | 2025-09-21 04:10:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a5d62448-3b65-3162-ad21-83ffd9c95263 | -14.17081 | -49.10255 | 2025-09-21 04:10:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b30af407-cd86-3b1c-9e02-491e083522b3 | -11.62622 | -50.60337 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 07b31c51-a880-3a06-a663-ca9b72d97564 | -12.08469 | -44.79754 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd6713f2-0b31-30c6-9c33-b1124811417d | -12.09613 | -44.79166 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6195bc04-715b-3c69-aee4-6ba3d933a981 | -12.05822 | -48.75674 | 2025-09-21 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48465a9a-defc-3c14-b261-ec6a2e66bbae | -13.20256 | -47.26279 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76675a4f-c70c-3bbd-8569-65a3e148f506 | -14.47473 | -46.51077 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7a01db4-7527-3cf5-b532-45d8757f9b25 | -12.08407 | -44.80133 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a3af720-b69c-382f-8b65-d7774d0aa767 | -14.20897 | -44.65647 | 2025-09-21 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b47828b9-1972-3e65-8a7e-c187cf12c06a | -14.87156 | -48.41506 | 2025-09-21 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d94af3c9-5045-3c18-92ce-1d8d5c7c7a55 | -14.31827 | -47.79177 | 2025-09-21 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9fb8671b-87fa-3f13-a9d5-291058cac8cf | -14.80247 | -51.38083 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8090654d-c9d1-3c19-bfa7-54570e3cd523 | -12.71369 | -46.8674 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe8d78df-def4-335d-b646-ccb75c951c66 | -12.4172 | -45.12835 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b829b58f-2837-3ffa-bb21-96a95c01b0f1 | -12.07883 | -44.81208 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e87feb5-cdf5-3e22-b3a4-6a3f945a3256 | -18.97264 | -41.09072 | 2025-09-21 04:10:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d7594b7-ac46-3157-abc3-b428902ce1e0 | -12.71221 | -46.85371 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23b8be99-6099-36ba-8b30-d219347f61c4 | -14.52865 | -43.91097 | 2025-09-21 04:10:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f21743f6-2e0d-3613-9cfd-06b97a0e3912 | -17.63963 | -44.18401 | 2025-09-21 04:10:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2712e5f9-f8ec-3d5d-8736-8e225be3fd54 | -16.21079 | -46.69457 | 2025-09-21 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 643c3218-4e9c-393c-bc57-950176b4d7b5 | -13.78748 | -44.33284 | 2025-09-21 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c008177a-9691-36b5-8d87-0a02bc0b0cd6 | -14.79771 | -51.37989 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1919df4f-a9c3-3073-bad2-038c82c63fad | -13.31105 | -47.28868 | 2025-09-21 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cb52686-5820-3b31-a939-a3968771ec5a | -14.0247 | -43.73962 | 2025-09-21 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4988f772-561d-36f0-a4e7-c8084ed5788f | -12.72484 | -46.84671 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2079eea1-68d8-3933-9337-efbddb61ef46 | -17.43744 | -44.79717 | 2025-09-21 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a8c8a23-0c61-3252-9c06-67e06e243eac | -14.97373 | -44.42945 | 2025-09-21 04:10:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5910ba3c-e206-3375-97b2-629a742ff45f | -11.29317 | -47.40942 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0ff6c95-3238-3a1c-a4bd-b8b66c7840d2 | -14.46766 | -46.5093 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ab9eae8-98b6-3b6b-a596-2e6b8e965844 | -14.4378 | -46.51742 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c7caabb5-82c9-35eb-828b-6ddd7740adb7 | -14.52128 | -44.86708 | 2025-09-21 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c942e043-47bd-338a-9e47-8cdf32e4e1d1 | -11.60609 | -50.6051 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0070e3ae-a085-3b23-b356-dcb3be2d942f | -14.97602 | -44.41509 | 2025-09-21 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07efbff6-1a75-31d4-9823-c3fdf92a7832 | -12.49376 | -46.72248 | 2025-09-21 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 142e8c5a-a1a5-3d92-b831-e7de2ec295b8 | -14.4491 | -46.51566 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bc8eb66-815c-3123-8da4-90e40d20b128 | -11.30495 | -47.50478 | 2025-09-21 04:10:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ab0b81e-143c-3c4e-bb56-99c13e1111a6 | -11.64218 | -52.8648 | 2025-09-21 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98dd4734-d5d1-365d-ad67-da3bd1dc8354 | -15.70442 | -46.99465 | 2025-09-21 04:10:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32daf0f8-d042-30ac-b063-51d09229e600 | -14.45275 | -46.51074 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af31491a-de5a-345a-be85-4064ca587cd9 | -14.60466 | -49.76256 | 2025-09-21 04:10:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00a9087d-d455-3374-9d5e-9d1dee40d3b7 | -14.81198 | -51.38273 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3870557-5de5-3cb7-9207-606462ba73e9 | -12.71147 | -46.85807 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33e22b2a-059b-3ef0-94f1-43ffbbf0d13e | -19.22415 | -43.76424 | 2025-09-21 04:10:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d06b36f-f8a9-3666-b04c-92a4ee888540 | -16.03579 | -43.36514 | 2025-09-21 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5165317c-1b3f-31c5-bb14-c8665c3f6aa0 | -12.24879 | -49.17188 | 2025-09-21 04:10:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 972ed83b-a5c2-3834-8a1f-edc03d24a964 | -14.74719 | -49.18956 | 2025-09-21 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa1c1784-c313-3199-ae34-98756555d02c | -14.97647 | -44.43361 | 2025-09-21 04:10:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7b3ed28-cb5a-3936-9b21-b8a65a9e7616 | -17.24776 | -43.44222 | 2025-09-21 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6b25529-2468-30d7-93d9-6f74b3e6a310 | -12.71519 | -46.8586 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a527eaf3-14ff-362f-afb4-198e4836b96a | -13.65093 | -44.44019 | 2025-09-21 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cbc0e0d-b838-3fca-a539-785c136fa2ce | -11.27367 | -47.40594 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cbbdce8-90e6-3e75-8c2d-efd51f1bc35d | -12.24638 | -49.17252 | 2025-09-21 04:10:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b2ac937-818b-37de-93e4-53d6d5929015 | -14.64812 | -46.83607 | 2025-09-21 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b53e6777-7220-3cf5-b82e-5cd2d8ab7215 | -14.60899 | -49.76317 | 2025-09-21 04:10:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d8d19dad-6655-351b-bcc3-c675455c59b0 | -13.5353 | -43.00045 | 2025-09-21 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 50456971-6b22-3b1d-8433-014ca40c4e46 | -12.11602 | -44.84501 | 2025-09-21 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3494a26f-4103-332d-81cc-783283f271d8 | -16.31379 | -43.03828 | 2025-09-21 04:10:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f836b5c-2f9a-3e93-976c-47c7b558ee38 | -14.6098 | -49.75874 | 2025-09-21 04:10:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aecbd4ef-2e26-32d2-a225-893b1194ca0e | -15.46964 | -49.96935 | 2025-09-21 04:10:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 458cdded-b2de-3d5e-aa7e-604812256db2 | -17.64237 | -44.18816 | 2025-09-21 04:10:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17bdbfdd-d71b-34bd-b57a-c0c3648fe4ea | -14.45201 | -46.515 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af466aec-24ec-3437-aa9a-56aff978696b | -12.0897 | -44.8528 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c396a38a-9c0a-3444-8317-ec37217f9171 | -18.93971 | -47.20202 | 2025-09-21 04:10:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bac9fd1d-6abb-3c37-971a-085d78e702a5 | -14.25039 | -44.71255 | 2025-09-21 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c91ae731-4f92-3a82-8fa5-31c27bcff3c1 | -12.35052 | -43.76016 | 2025-09-21 04:10:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d1e2255-b559-3bce-abe1-1842e97b2b7a | -18.41992 | -44.95519 | 2025-09-21 04:10:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 508fcb04-870c-338d-83af-2c3bd3dc2912 | -12.71966 | -46.85477 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33e57019-80b1-3fb5-88f6-f219c1f836ee | -17.07536 | -43.32514 | 2025-09-21 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 964cfa50-189c-3218-947b-df9df9746965 | -12.0717 | -44.83432 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| befc6009-ce05-32a2-a59a-4cb3b237b7eb | -13.33606 | -43.70529 | 2025-09-21 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42cf05a8-cb55-3dbd-958e-c913de05722c | -14.25577 | -44.38572 | 2025-09-21 04:10:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e564cb5a-f902-3868-95f2-e9202824ecc1 | -14.028 | -43.74017 | 2025-09-21 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bdf731d-03d7-30d9-979a-7569774efeb3 | -11.9366 | -48.70704 | 2025-09-21 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5036fce6-f19a-3b87-96d8-cd339c682401 | -12.49252 | -46.68546 | 2025-09-21 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7a52e1b4-d2a6-3acd-bf38-14e97b55c5ff | -12.47995 | -46.69242 | 2025-09-21 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8dd8a4b7-d5f7-3c7e-8f53-b7dd54baf4df | -15.49097 | -41.91874 | 2025-09-21 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c1c86d3a-fc2a-31ff-9e4c-7d44e0f76d15 | -13.36678 | -44.28147 | 2025-09-21 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8a0631d-63a4-34a7-b70d-512c1649a48e | -13.68247 | -43.81696 | 2025-09-21 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1de6680a-aa8a-301c-91ad-ec7c8be2a409 | -12.07669 | -44.84663 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80c2e39f-4bc7-3ac4-bb3b-44de6bf5ef14 | -12.35439 | -43.75721 | 2025-09-21 04:10:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d26a912-d5e5-363b-8215-51a2cf428d12 | -14.46909 | -46.50094 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 938a616c-609d-3ec7-b00e-931dee79c319 | -12.96488 | -46.95314 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 032176cd-2223-3412-9e5b-20a41e35536f | -14.63056 | -48.27034 | 2025-09-21 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2b12e0f-5e55-3f98-a46c-a0ca98f6fafe | -17.05344 | -44.89866 | 2025-09-21 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bd6bfed-9603-38b3-a63f-6cd48270c521 | -14.97271 | -44.41453 | 2025-09-21 04:10:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71ec4c35-2338-379b-a067-8e391bc8d1ab | -12.71369 | -46.84504 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45287153-4360-3772-867c-8010b5510b8b | -14.81465 | -42.19484 | 2025-09-21 04:10:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 797ddb79-f5b9-387e-800f-3953238e7980 | -19.03111 | -46.93939 | 2025-09-21 04:10:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef1e91f8-b3ec-3339-9c2b-cd265d0b1576 | -12.07138 | -44.81483 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4db3de3f-dbb6-3d21-ac5d-bb2bcbaba7a8 | -13.62318 | -47.42002 | 2025-09-21 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62905df2-6b0c-3607-9e98-1c366dad1dc7 | -14.97488 | -44.42227 | 2025-09-21 04:10:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbcc65b9-4e65-319e-9345-ef6c8e8db5cb | -17.43802 | -44.79355 | 2025-09-21 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README17.md)
