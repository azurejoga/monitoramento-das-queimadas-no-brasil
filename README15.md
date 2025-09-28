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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6cd4991-8266-34d2-bf58-b51665445d83 | -5.74201 | -42.83335 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f4a848e9-71e1-369a-b445-48566cd6e1d8 | -5.73916 | -42.83256 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a2ca735d-4202-3b17-85a6-b1abd301f217 | -5.73359 | -42.84962 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8271ced3-341c-3afb-9653-734d50410d31 | -6.71115 | -42.76591 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5e578e51-12f1-3bf6-8755-941418216165 | -6.78758 | -44.08251 | 2025-09-28 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| dff6f276-7447-3aa0-9229-2f30c09f5772 | -7.30611 | -42.94769 | 2025-09-28 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 015d7267-763e-339e-9ae4-e9a1a3f8ec1a | -7.42649 | -40.07976 | 2025-09-28 03:36:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f80f51f0-5552-344c-a00a-beb8dfa1ef22 | -8.67274 | -43.9877 | 2025-09-28 03:36:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94fedef5-b57e-37db-931b-10431a9c1d01 | -7.31904 | -45.99004 | 2025-09-28 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81667766-a0c2-3687-bddb-05fd4e885382 | -6.26243 | -44.07479 | 2025-09-28 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b47a534-0476-3dd8-99d9-d68a3e463523 | -6.11245 | -41.81062 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d2965473-e5a3-32f1-8dcc-7d2e87e31549 | -6.11744 | -41.81567 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3f381c84-f4f5-339f-bd97-f40999166b43 | -5.82645 | -44.44175 | 2025-09-28 03:36:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4e40e231-7b91-36ce-93cb-19bd64550419 | -5.75804 | -42.83648 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 438e70aa-4c56-3577-8b25-4bbe9ad1da10 | -8.28905 | -45.45031 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1715d5f0-383f-3664-91db-94874323a4db | -8.28567 | -45.46437 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6f7dcf89-4cef-36cf-a27a-dadaf3ace2d2 | -8.28026 | -45.4634 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d4e46651-c4c0-3441-8785-d25afcb5006f | -8.28655 | -45.45956 | 2025-09-28 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| afeb6cbb-368f-31d6-ad38-b4e15c0a19ea | -6.48206 | -44.25319 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be2eaaf0-45b1-3a5a-a9b9-449d5c6a8783 | -6.11793 | -41.81286 | 2025-09-28 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f1f9c8cb-133f-358b-b081-d6d1461fd7d9 | -6.53913 | -43.82449 | 2025-09-28 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4086eb2f-b8da-38c7-aea4-4773364808f6 | -7.03405 | -44.77128 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f8103911-5b27-35ba-91ca-6b2cc05b5596 | -6.14579 | -43.47449 | 2025-09-28 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 94d34c96-889d-38ef-bbe4-86838630c6c9 | -7.79421 | -46.99976 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6fac48fb-6db2-3699-a374-ccd110c68cb1 | -7.30139 | -42.94368 | 2025-09-28 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e97812d6-c5d1-3175-9eb4-bc190555b9dc | -6.89829 | -44.75718 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b2057356-0b76-3572-9dc9-9527bab5c985 | -7.77607 | -47.02236 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8298ab73-7897-3d7a-ab56-631cc4271f5b | -5.81948 | -42.80042 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ad67df16-d35e-3a1f-9550-0a5647f1e969 | -6.78156 | -41.75304 | 2025-09-28 03:36:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bc7f81a0-fd99-30ac-ac11-d410e9e34069 | -6.48447 | -44.23988 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35125866-6c00-3833-a22a-e61fe56b7600 | -7.02898 | -44.76544 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f43c712-259a-3f43-b11c-f27f2f7053c3 | -5.82725 | -44.43727 | 2025-09-28 03:36:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 38168b45-f0f5-32f4-870d-8b8982ab6234 | -7.74246 | -47.01572 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 66cac5bf-d066-3998-94c8-f43dd663067b | -5.73208 | -42.84173 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5a65ca72-3bc3-361c-bd1c-55a5c40a58c0 | -4.68357 | -41.9522 | 2025-09-28 03:36:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c9e2f708-255e-370a-8e0d-97d98b6c30fd | -7.70841 | -41.28609 | 2025-09-28 03:36:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 78fba294-9529-3ce9-9cbb-ae01c1eb499a | -5.14532 | -45.70418 | 2025-09-28 03:36:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f828a886-7d8f-3754-8ab0-4f39aa751606 | -6.18235 | -42.944 | 2025-09-28 03:36:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| dd44b270-c9ae-3fc2-87fc-b1db4cf68cb8 | -6.31089 | -43.46904 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b96aea58-a303-3825-a72f-cad2eacdff76 | -5.6318 | -44.93193 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07b3e666-fb37-3aee-ae9d-17acdc2d0dca | -5.05276 | -45.31747 | 2025-09-28 03:36:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e95b0f8b-7d52-3c6c-b826-adc3605aca2e | -5.76589 | -42.82324 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| efcd100b-98f0-33eb-a0a9-f8fe57002965 | -7.30553 | -42.95101 | 2025-09-28 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1484c3ae-53d4-3344-b607-54a971140e16 | -7.1029 | -44.22818 | 2025-09-28 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a443341-1bdc-3b55-8bab-7f6e98a759dd | -7.30494 | -42.95435 | 2025-09-28 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3711e31a-082e-39e9-9f50-99303faba398 | -7.54626 | -46.09966 | 2025-09-28 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 222daed8-4f8c-39a6-b75a-43f1ab035cb2 | -6.98735 | -43.78121 | 2025-09-28 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39650432-a5e5-3e2f-8a87-179c2c9aee5c | -5.35467 | -45.03946 | 2025-09-28 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ce0f8a7a-45b8-317b-b23d-254cc6b3d913 | -7.44919 | -43.17468 | 2025-09-28 03:36:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6134c652-7a28-3f01-8327-655e164cb889 | -6.16782 | -43.38029 | 2025-09-28 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2eba30f-c4ef-3f5b-bf93-1022d467dcb5 | -7.80582 | -46.98975 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5d6d0aec-4b88-36cb-9978-c5a7ba8a9450 | -6.68813 | -42.74265 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2f7e2eed-3952-3fbb-921e-46e0aa171383 | -5.7574 | -42.84011 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 28e5c51a-c97a-3adf-a7a7-9246a8efc3a7 | -7.79189 | -47.01221 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2dcc7bce-fa50-3473-abe0-409ef1ecd438 | -7.79429 | -47.01345 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 630662a2-6db9-3dfe-be40-2778b80b0f67 | -5.74143 | -42.83664 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e5471b2d-08b4-3ba2-aae6-e2beacf22005 | -5.74551 | -42.84481 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5685612e-053f-37b3-8518-3d6042585ed5 | -5.26944 | -44.73252 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 79a7c9c3-c11c-3e2f-8bdf-4cf5be558bc2 | -5.63973 | -44.92302 | 2025-09-28 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ec1b76d-19e9-32aa-93b7-0908bf7339d7 | -7.24495 | -44.76284 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6164bd4-9c24-31a3-983c-9363a44b914b | -5.80754 | -42.80574 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 861b17f1-3e04-30d0-952c-4e72a77d19d3 | -7.62681 | -43.79771 | 2025-09-28 03:36:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 93c377f2-5ffa-36ca-8acf-ba28b63989e7 | -4.15495 | -39.99878 | 2025-09-28 03:36:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a37b7d6a-5838-3cb6-b3b5-0510c6386ea1 | -7.50262 | -44.304 | 2025-09-28 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bd7689ea-2da0-3f89-a99b-20933201e814 | -6.70865 | -44.58385 | 2025-09-28 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0208bb25-f8dc-3a4b-83eb-8736bf864ede | -8.36493 | -41.40909 | 2025-09-28 03:36:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1965a3af-511c-3a93-8559-7f7ecb681850 | -6.05097 | -43.91774 | 2025-09-28 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7489c8e1-62fc-3e2f-898d-fa62d62dc124 | -7.50432 | -44.3016 | 2025-09-28 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f73803ee-6f51-3e9c-9c11-818ebaa1eda2 | -6.06973 | -42.44591 | 2025-09-28 03:36:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2ed7e828-0f8f-39b3-8491-ecbc00de3e9f | -7.58532 | -42.32315 | 2025-09-28 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 93fcf466-55ed-3e9d-bba9-58f5266862e6 | -6.90426 | -44.75818 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4354e6b5-265f-3cf7-adb4-644005480382 | -8.64346 | -43.99334 | 2025-09-28 03:36:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2511356a-342d-3570-8c11-a4a78af65d4a | -6.0857 | -42.6346 | 2025-09-28 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2bf4bac4-3cbf-3e5c-819e-3c5a3afe93b3 | -6.28796 | -39.82706 | 2025-09-28 03:36:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a26e4e65-14e9-355b-9007-f60b5c7120b4 | -5.90904 | -42.93871 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 297537f4-e5ed-3410-b85d-6cd0de2bf7be | -7.79981 | -47.021 | 2025-09-28 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| aece14ef-4359-3a44-894d-175eead2f860 | -5.88167 | -43.19964 | 2025-09-28 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b2b0f58c-5d47-32c0-abb5-ea0149e5e7a8 | -5.41219 | -42.28116 | 2025-09-28 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d9f5b590-a935-3097-8c6d-1d3551cd91ee | -8.4932 | -44.72073 | 2025-09-28 03:36:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dceafbbe-fd06-3ab8-9020-40dfdda83655 | -6.31966 | -43.45182 | 2025-09-28 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1506000a-24b1-3e7c-a6f5-10c02a03e46a | -5.80872 | -42.83088 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 56ed75cf-6612-30ce-b106-6d87d0508d9f | -5.73804 | -42.83918 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a45ae3f6-ecc1-37d3-956e-7205fca4c36d | -8.48078 | -47.81422 | 2025-09-28 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 10da13a5-ca06-3f6e-8431-8c1ee56d2f8b | -5.76627 | -42.8842 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 9754f06b-ba20-3506-af79-e66338d5907b | -3.80544 | -41.56564 | 2025-09-28 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 818cab36-939e-39e9-bb30-ef3fd38ecc11 | -5.70883 | -42.65717 | 2025-09-28 03:36:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ed0a9ffc-5e2f-39ee-851b-39643abf13fd | -6.71004 | -42.77013 | 2025-09-28 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2d5ca3a6-2313-37e9-96d0-5e05fff11c43 | -6.70876 | -44.5951 | 2025-09-28 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3c57008a-5c31-3fb1-9a8a-1ec6314a6e61 | -6.70114 | -44.60363 | 2025-09-28 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d91c13ff-c56d-30fc-a14d-b8f245f9b94f | -7.87378 | -44.57048 | 2025-09-28 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| beb2a53f-41dd-31ce-9282-5c5e4452abcf | -6.25572 | -42.46635 | 2025-09-28 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2f147d6f-7e8b-30fa-bc70-bcbea8238e99 | -6.11992 | -43.45864 | 2025-09-28 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b9b93127-5539-39ef-9568-5c3d509f3c72 | -5.776 | -42.82855 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e904d258-a48c-377d-878f-d9d4dc6b58ce | -5.79855 | -42.82585 | 2025-09-28 03:36:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5686be83-f6ba-3557-8757-1967cd5d69c6 | -5.84884 | -43.67479 | 2025-09-28 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c00b8ad-93d2-3e25-86a1-0033210ddf2a | -5.70514 | -35.2845 | 2025-09-28 03:36:00 | NOAA-21 | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c559ad18-d8d1-3e63-b57b-0bbfd2df56f7 | -6.29228 | -39.82781 | 2025-09-28 03:36:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6986a9ff-05a0-346e-b2a0-7de7bae7bb93 | -6.90007 | -44.76384 | 2025-09-28 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d6ea76d9-73e9-3e7b-942c-391cb9e1c626 | -7.76142 | -45.73336 | 2025-09-28 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba15192c-2afd-365e-bec9-29ac20271c70 | -5.69746 | -42.62838 | 2025-09-28 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README16.md)
