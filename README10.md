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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7d04be8-9556-3494-8beb-aa5b0988a32c | -3.8853 | -42.55985 | 2024-11-15 03:27:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6adc8e6a-b428-3647-8952-97ce5b666355 | -7.16329 | -35.02045 | 2024-11-15 03:27:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 63d22653-8e74-311b-bf87-ffb7e1ebf428 | -7.65317 | -35.17032 | 2024-11-15 03:27:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 585fca62-74bd-363d-98ab-826abb579611 | -3.70835 | -41.69769 | 2024-11-15 03:27:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 341dc029-6e68-37df-8435-91117dd796c1 | -3.71967 | -41.69701 | 2024-11-15 03:27:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2da665ae-793b-3dd3-8f15-f0d3cad68c65 | -3.88655 | -42.55883 | 2024-11-15 03:27:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9ce24e83-9da7-3071-bf9b-fec4c78b61a4 | -7.26395 | -39.85822 | 2024-11-15 03:27:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1b8e6d97-2cb3-3f79-b52d-3ad2ae84ab0a | -7.26489 | -39.85296 | 2024-11-15 03:27:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 12c9fd70-3d80-3d9e-a6d9-4afecf5ab468 | -3.71325 | -41.70005 | 2024-11-15 03:27:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 59bb5903-0e28-3fca-aea1-05a4b17574b4 | -3.70816 | -41.69505 | 2024-11-15 03:27:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 1ba20278-63c8-3e29-ba42-978faef9f7ef | -6.35174 | -39.81884 | 2024-11-15 03:27:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 80bfc920-d424-3f40-a174-03a3e3ee7662 | -6.73635 | -39.69685 | 2024-11-15 03:27:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9b730798-9c64-329c-85b2-74b3bdfed5b5 | -6.97152 | -38.38207 | 2024-11-15 03:27:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2bf42895-da1e-3334-b856-edbb37ea5b82 | -6.97222 | -38.37783 | 2024-11-15 03:27:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8fd640a7-7670-337f-94a5-acb2002773be | -6.30093 | -39.76612 | 2024-11-15 03:27:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7b7a00b7-ba37-393a-a1f0-1a7314d92d36 | -7.2176 | -35.17366 | 2024-11-15 03:27:00 | NOAA-20 | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 18dff536-950d-3f3a-87b8-1dde65562e9f | -10.72415 | -40.52869 | 2024-11-15 03:27:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64f40b4f-2e19-3be6-b5f5-cf466d74287c | -6.29997 | -39.77156 | 2024-11-15 03:27:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2d9e25ae-ac24-3a75-93dd-482f723b2cf9 | -6.58572 | -42.24768 | 2024-11-15 03:27:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c4732536-4464-3aab-bc93-3fb46778fc13 | -3.71392 | -41.69598 | 2024-11-15 03:27:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| cdc94380-d76a-3b31-b377-d79f810245e2 | -6.91771 | -38.07112 | 2024-11-15 03:27:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e217501c-e8f0-3cdb-a240-be3d3115ffea | -3.8818 | -43.15871 | 2024-11-15 03:27:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2526d26d-4829-3054-af7c-9365ec492f37 | -7.12442 | -35.23642 | 2024-11-15 03:27:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 934dc962-2ef3-39a2-a7a7-70878f43e0e8 | -10.69419 | -37.04957 | 2024-11-15 03:27:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a341c28c-7c25-37df-8bc1-662386c330d9 | -5.30176 | -37.34264 | 2024-11-15 03:27:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 236aae08-419f-3df2-8043-cbb42a038426 | -6.16072 | -41.16209 | 2024-11-15 03:27:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 37f1f21f-af1b-3d4e-a3c3-586a10fa7471 | -3.88532 | -43.15786 | 2024-11-15 03:27:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ecf4448-609f-3263-9f76-3e70baafefa0 | -6.226 | -35.16318 | 2024-11-15 03:27:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b50b25de-1777-35c2-bdc6-20dfb364c0de | -6.16324 | -41.16084 | 2024-11-15 03:27:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 09e2534f-f2a3-3e55-b044-039e0594a2ac | -3.71412 | -41.69859 | 2024-11-15 03:27:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d0b0479a-049c-3c8a-832b-a01ac53e44e5 | -7.26484 | -39.8568 | 2024-11-15 03:27:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e9ef3b4a-e6c2-3dd4-bab6-e1081d7ed794 | -3.70748 | -41.69917 | 2024-11-15 03:27:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 70025b0f-2235-31f3-95d9-0a5d187ae1fc | -4.1963 | -40.68111 | 2024-11-15 03:27:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0e59555d-65c0-3fa8-bb33-6f305046cd2d | -3.88738 | -42.5541 | 2024-11-15 03:27:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d4500afa-269d-35f8-967e-a3ed4e8051ef | -7.21692 | -35.17781 | 2024-11-15 03:27:00 | NOAA-20 | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0b5617e8-d2d6-36af-968f-b85e36aadbef | -6.86204 | -39.25693 | 2024-11-15 03:27:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 51eb43ba-3c65-3b15-8bc1-fb0e12c1ea0e | -10.72468 | -40.53124 | 2024-11-15 03:27:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6654fce5-498e-38eb-8481-2f45fd9ac6df | -7.13294 | -35.22943 | 2024-11-15 03:27:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fc715b22-4db7-34ce-950c-a021c6e2ad02 | -6.50162 | -41.59946 | 2024-11-15 03:27:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c98cd676-2d82-3cfb-941e-c8b689e2f109 | -3.71482 | -41.69454 | 2024-11-15 03:27:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 737b759c-58ad-3d9f-9801-1b556d69bc19 | -7.12868 | -35.23293 | 2024-11-15 03:27:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f60fd1ab-c5fd-3396-bb62-706e30a9c478 | -6.91905 | -38.07262 | 2024-11-15 03:27:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b3677a2-de46-361a-8e01-f044d397b30b | -3.8861 | -42.55508 | 2024-11-15 03:27:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a883a0ac-4fbd-3b6f-b554-f5be63fbe32a | -9.41105 | -35.52415 | 2024-11-15 03:27:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 33bec59b-881e-348a-aa94-d09f4dcdf204 | -6.14662 | -38.32169 | 2024-11-15 03:27:00 | NOAA-20 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2bddb584-89c7-3608-a2ab-dee74129e718 | -5.30065 | -37.34328 | 2024-11-15 03:27:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3701b29f-b4cf-3f08-810b-f29cf585eb22 | -7.15974 | -35.01986 | 2024-11-15 03:27:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| a5c5a8c3-db59-3dfe-8185-1a3fdf9421d7 | -8.07249 | -34.97797 | 2024-11-15 03:27:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a31ffc12-d929-3e3f-9539-9acf5f10da2d | -7.1249 | -35.1436 | 2024-11-15 03:27:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 50c14068-91b7-3fd5-a10b-f88b7760b87c | -7.50304 | -34.84773 | 2024-11-15 03:27:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 50dbb415-e462-3d66-ad8a-153b2caedc73 | -7.12801 | -35.23704 | 2024-11-15 03:27:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 663f16cd-8b31-3b62-b581-99552b388ac0 | -6.97322 | -38.37694 | 2024-11-15 03:27:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 41740b51-fbfb-3508-9364-33bab3046c8e | -5.79486 | -38.32331 | 2024-11-15 03:27:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bdd3eede-b15a-3b5c-8327-cff4ed4d7bc0 | -11.86759 | -38.35654 | 2024-11-15 03:27:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5e7fd0a5-d2d3-3f66-b2e5-9d3ba5d0239b | -5.97937 | -38.32427 | 2024-11-15 03:27:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0cb3923e-14c2-3250-81e3-82792b350911 | -4.39287 | -43.70602 | 2024-11-15 03:27:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85a849ee-a69c-3f9d-a94a-93ee9d785417 | -4.1985 | -40.68061 | 2024-11-15 03:27:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d1c9cd2d-f6b6-3f8c-bd12-b13c50ad94f3 | -6.75458 | -38.64967 | 2024-11-15 03:27:00 | NOAA-20 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b3401865-76f2-3c22-afdd-2c82c84128f1 | -6.501 | -41.60304 | 2024-11-15 03:27:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba1e6b9e-4ff1-35f1-a72d-8d5f13d763a1 | -6.16266 | -41.16426 | 2024-11-15 03:27:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 890912b8-52a5-35f6-94b9-6a6e4a00b0ff | -12.77901 | -38.49868 | 2024-11-15 03:29:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0b5be7b9-e63f-3e6d-a9cf-1e1cb753ac95 | 1.3035 | -60.4074 | 2024-11-15 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 54ef6e2e-3f98-36bc-aac8-e81155d484d9 | -17.2543 | -57.4698 | 2024-11-15 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.8 |
| 4ae5f25c-9d54-38c3-bca2-592cf790980b | -17.235 | -57.4516 | 2024-11-15 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 4f0497eb-7420-3f3c-9c94-e4ee8512e9b9 | -17.2347 | -57.4721 | 2024-11-15 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 6f21e77d-20e9-3a41-8e78-0b7068b2423f | -17.2547 | -57.4493 | 2024-11-15 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 62cbad80-26ac-3ea9-b160-82f8c3bda00d | -17.5879 | -57.4917 | 2024-11-15 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 322452c1-d0b6-30c7-9a5a-827b5e2a0222 | -17.5882 | -57.4711 | 2024-11-15 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 623b0fb7-8dde-36e5-ab24-2b23e6aaeefd | -21.08068 | -47.47507 | 2024-11-15 03:32:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 229176bb-e03a-30f0-9361-81de8146c7f2 | -21.07945 | -47.48038 | 2024-11-15 03:32:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f996a6f-8eeb-3393-9ab7-c20f79973059 | -21.07824 | -47.48561 | 2024-11-15 03:32:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e3e4ad8-10e9-3cbf-b951-c8caa2392d00 | -17.2543 | -57.4698 | 2024-11-15 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.1 |
| e67cf657-82d6-344c-8d68-d4c996bae9dc | -17.5882 | -57.4711 | 2024-11-15 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| abbca7b4-35ad-3656-a267-b12c95bd8e3d | -17.2347 | -57.4721 | 2024-11-15 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 009cf202-e640-34ce-a7bf-8c40a4d1cddf | -17.235 | -57.4516 | 2024-11-15 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 55897cfa-7ade-3244-8ad4-a829b4833c5c | -2.6596 | -46.1843 | 2024-11-15 03:40:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 792dfc15-9877-36f2-9e58-c94bfc55e8da | 1.3035 | -60.4074 | 2024-11-15 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 879cab6d-0f08-3fc7-91c9-0ff5e221731a | -17.7052 | -57.5392 | 2024-11-15 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| e8de7cdb-13e2-38bd-9d18-55c2a1319e89 | -17.2547 | -57.4493 | 2024-11-15 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| d7e44647-3322-31e6-a8cd-090f3bf42722 | -17.235 | -57.4516 | 2024-11-15 03:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| f49cad44-04c7-3d24-ba16-f4014dcba154 | 1.3035 | -60.4074 | 2024-11-15 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 0eca19d9-d695-363d-8f7d-69ae69e3f476 | -17.2347 | -57.4721 | 2024-11-15 03:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 1ef14a08-67a4-3600-865f-460188a339fc | -17.5879 | -57.4917 | 2024-11-15 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| c33195fc-87c4-3f60-84de-a203106cb051 | -17.2543 | -57.4698 | 2024-11-15 03:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.8 |
| ffe17d98-97c7-321f-8f6d-da3efe12d998 | -17.5882 | -57.4711 | 2024-11-15 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.4 |
| 7b162f02-c048-382c-8351-dfaa2c011b00 | -17.7048 | -57.5597 | 2024-11-15 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 39f5b6fb-9221-3560-b322-766b34340b9d | -17.2547 | -57.4493 | 2024-11-15 03:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| ae07691c-9823-3abb-b845-ca87652389ab | 1.0765 | -51.1441 | 2024-11-15 03:50:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 654b9329-6fe6-3c64-9f7d-aa795986045d | -17.235 | -57.4516 | 2024-11-15 04:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| b94d4f85-e4cc-3c46-893e-afb9efd201ee | -17.5882 | -57.4711 | 2024-11-15 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 37f82f9e-f914-3a10-ba5f-6f5aefd49368 | -17.2543 | -57.4698 | 2024-11-15 04:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 132.0 |
| 245e35c0-db75-3964-bf44-032b0b563381 | 1.3035 | -60.4074 | 2024-11-15 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.9 |
| fe2c65d0-d85d-3f0e-93b4-22cfb12270f8 | -17.5879 | -57.4917 | 2024-11-15 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 49fcf4c0-345f-3e3d-a851-5eef537ab594 | 1.0765 | -51.1441 | 2024-11-15 04:00:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 46.8 |
| e165ee4b-d59f-3895-acdc-e5dc157048b8 | -17.2547 | -57.4493 | 2024-11-15 04:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| 7407afb5-5bcb-32b0-b8d1-c3f3c7b2bce2 | -17.7048 | -57.5597 | 2024-11-15 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| e8ddda15-5020-3d59-b5e7-52f3a160b457 | -17.2347 | -57.4721 | 2024-11-15 04:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| e4df1fdc-793e-399e-8b10-cbf6b9871e08 | -17.235 | -57.4516 | 2024-11-15 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| adfc451e-89ee-36ac-8afc-b0dc4272ee63 | -3.1283 | -45.1609 | 2024-11-15 04:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 16fe8673-a14a-35ba-ba67-f34c30a3d27b | -17.2547 | -57.4493 | 2024-11-15 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |


[Clique aqui para ver as próximas entradas](README11.md)
