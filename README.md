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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ea57472-c4b0-3b53-8ad9-2a827d9b0b8e | -5.9369 | -44.463299 | 2025-04-17 00:05:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 046b04fd-9baa-3e84-be3d-7a5c985ce2f1 | -6.3442 | -43.657398 | 2025-04-17 00:05:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 801a01a0-fc3a-3336-b83b-6a8068239005 | -10.6885 | -40.343399 | 2025-04-17 00:05:00 | METOP-C | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 79901fbe-217d-31db-886a-a57d50cfd693 | -9.9674 | -37.261799 | 2025-04-17 00:05:00 | METOP-C | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| c8761b7b-9b37-37ac-aa4a-255f4853af94 | -5.6391 | -43.713799 | 2025-04-17 00:05:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4927fd93-f41d-330b-950d-88c51973c0cc | -5.6369 | -43.7038 | 2025-04-17 00:05:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| faf2232d-d5f4-3473-a3a1-4a2ab087c0d7 | -9.7934 | -36.9538 | 2025-04-17 00:05:00 | METOP-C | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 0c377f16-4c82-3f1d-913e-44de35304ac5 | -10.4741 | -42.440701 | 2025-04-17 00:05:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ebf3c255-7c45-3a09-a088-9c34375ad32e | -9.6497 | -36.155399 | 2025-04-17 00:05:00 | METOP-C | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 44648f94-1a61-3d4d-a4bf-04bf09cef275 | -3.0195 | -40.027302 | 2025-04-17 00:05:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 80ab1512-9070-3052-abb3-aa9915c4e18e | -3.0179 | -40.020401 | 2025-04-17 00:05:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 26452e23-9d04-3add-8a13-759f27e7ad3b | -9.969 | -37.268799 | 2025-04-17 00:05:00 | METOP-C | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| 872ac549-73b4-3483-b9eb-f652fabb0026 | -5.9272 | -44.465401 | 2025-04-17 00:05:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2829934-d63f-312a-80e5-c86a83675de3 | -9.648 | -36.1479 | 2025-04-17 00:05:00 | METOP-C | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3794a500-4a9c-3849-9bf5-e586f0f6fd12 | -9.7918 | -36.946701 | 2025-04-17 00:05:00 | METOP-C | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 28e153a8-41cf-3650-88d8-9d9f83270ad4 | -10.472 | -42.430801 | 2025-04-17 00:05:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 20b3a69b-3466-34eb-8de4-5afb5f527d22 | -10.4699 | -42.421001 | 2025-04-17 00:05:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| db7e94a6-7a6a-3eb4-9331-34f44fb6c1c0 | -21.2166 | -48.604099 | 2025-04-17 00:50:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1dbbb14c-57f1-375d-842c-31959646d9ab | -21.22119 | -48.62159 | 2025-04-17 01:05:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 7cd64ef0-1086-3f87-bfb3-e32b3af04224 | -21.21939 | -48.61023 | 2025-04-17 01:05:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| de3af525-0c0d-395e-8957-e85515536540 | -6.57176 | -51.11567 | 2025-04-17 01:09:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5e3036e1-4ebf-3e3d-868b-d7cece72e68a | -8.39235 | -35.02514 | 2025-04-17 03:10:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 247eca0f-1a3d-3d3e-b523-62a76fcc9ce0 | -9.79922 | -36.95153 | 2025-04-17 03:10:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 15c5dd69-17da-3133-994d-e4145dd5aaec | -9.79866 | -36.95461 | 2025-04-17 03:10:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5249d3f-9efb-342e-b081-611fcd357ccd | -11.67765 | -37.64864 | 2025-04-17 03:13:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 424a14d7-4b32-320f-b02d-ad284b0d7d91 | -11.67899 | -37.6482 | 2025-04-17 03:13:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a01e0921-abdb-3dca-963b-bd9a814b8562 | -3.95951 | -41.48594 | 2025-04-17 03:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9fc2481-78d7-3d40-a64d-7f83767b204f | -3.96003 | -41.48289 | 2025-04-17 03:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3636eb40-bb50-33ae-b821-0e1c228db7de | -5.64317 | -43.70914 | 2025-04-17 03:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4538eab2-89af-3d4f-9fdc-613a89627331 | -5.4314 | -43.19966 | 2025-04-17 03:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c06ad071-7c7f-3f79-8b5c-206f3613ece9 | -6.34364 | -43.65418 | 2025-04-17 03:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6477113-2a7c-308e-bb65-168abb65dae6 | -5.90399 | -35.31761 | 2025-04-17 03:36:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f72dcdc5-dc84-3a25-94c4-4fbcee02751b | -8.39004 | -35.02526 | 2025-04-17 03:36:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5c97b2b5-9b59-3d45-9106-481ed7eab6df | -5.64246 | -43.71317 | 2025-04-17 03:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47e98d78-74f3-36db-a82d-1aa5eed753b7 | -5.48351 | -43.33086 | 2025-04-17 03:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34788451-5818-350e-96c3-4242b0b13864 | -5.64896 | -43.71005 | 2025-04-17 03:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f888036-e42f-3e98-a073-76163ac26f86 | -5.42779 | -43.20018 | 2025-04-17 03:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c910840f-7acd-3541-87ff-8f7ebfaebd35 | -6.34867 | -43.65878 | 2025-04-17 03:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 116fbb09-2299-3712-b48d-f4319fc3524a | -5.94246 | -44.47271 | 2025-04-17 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 541a753b-a68c-37e0-bfc7-20b1b334901e | -5.58527 | -37.28947 | 2025-04-17 03:36:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f0f0c8a3-c5f1-3298-867c-fbcd08f54501 | -5.90463 | -35.31797 | 2025-04-17 03:36:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0f98c407-47a6-303b-a7a6-b01a9887d160 | -5.48284 | -43.33467 | 2025-04-17 03:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be182d79-9327-3851-82ac-c9d97c3a9f15 | -5.94323 | -44.46838 | 2025-04-17 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 182b69a3-2264-38a1-9e36-10ab31ad22f9 | -5.93721 | -44.46724 | 2025-04-17 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbc0fefe-aaf0-324b-b32b-d7d2fc9cff31 | -8.07271 | -34.9775 | 2025-04-17 03:36:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9d472cf9-203f-3a5d-81c2-1d1e6ecc5f06 | -5.43074 | -43.20334 | 2025-04-17 03:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac1eb7a6-3b5f-383e-8dc8-1fb8d7cf2bda | -6.34935 | -43.65504 | 2025-04-17 03:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a780d777-e261-335e-8ea5-708a3404585b | -5.43335 | -43.20141 | 2025-04-17 03:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cf1c4a9-f174-377a-bab5-2a104a213adc | -10.98233 | -44.44381 | 2025-04-17 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c90ab458-8dbe-3dc8-974a-2541470a6f81 | -11.68081 | -37.64703 | 2025-04-17 03:38:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0223b27a-8a8b-3d3a-b003-7ef30a4a9a84 | -11.41334 | -42.29077 | 2025-04-17 03:38:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7b230b7b-2733-3696-8544-2a74672575eb | -10.69632 | -37.0492 | 2025-04-17 03:38:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1794f7b9-7ef6-3a2a-9030-f96303b5eaf2 | -10.98302 | -44.44016 | 2025-04-17 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07367c44-0b14-3a6d-a47b-ed73245431ba | -12.53681 | -39.10363 | 2025-04-17 03:38:00 | NPP-375D | CABACEIRAS DO PARAGUAÇU | BAHIA | Brasil | 2904852 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7f330fbd-dd3b-3bdc-ae49-b2a82f368b47 | -10.47978 | -42.42922 | 2025-04-17 03:38:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 72cee920-038b-3c6d-93b9-6197d09092da | -10.47878 | -42.43467 | 2025-04-17 03:38:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e39f2346-5c6c-3be0-a1d1-345b37508e26 | -9.1518 | -36.47059 | 2025-04-17 03:38:00 | NPP-375D | LAGOA DO OURO | PERNAMBUCO | Brasil | 2608602 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ade44b5-dc51-332e-99eb-d5707c1dfb96 | -9.6511 | -36.15078 | 2025-04-17 03:38:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a9aa74a6-612d-3241-9752-50aa4aaae05c | -10.98372 | -44.43649 | 2025-04-17 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4a4bd2a-8109-3fca-be99-7789367dd2b3 | -11.67724 | -37.64642 | 2025-04-17 03:38:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0498bbe6-52fc-3d35-8332-e793bb03939e | -12.35649 | -39.09649 | 2025-04-17 03:38:00 | NPP-375D | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b31e8d25-f4bb-32a2-b125-646045b69aec | -9.79911 | -36.94937 | 2025-04-17 03:38:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4fb0eef3-a6cc-3e15-8d0a-062a8e86ff4e | -10.48367 | -42.43555 | 2025-04-17 03:38:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 635728a9-d5dc-3c70-9c76-a89fdd47caa8 | -13.11646 | -43.48296 | 2025-04-17 03:38:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b7e0e2a-a9ca-32e2-8282-37460801facd | -10.98922 | -44.43768 | 2025-04-17 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40fc40b0-2ce2-3878-8799-82a1bd921b55 | -10.2547 | -37.42125 | 2025-04-17 03:38:00 | NPP-375D | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8566b2ef-4f41-3d74-87a3-47c5ec650796 | -10.48466 | -42.43011 | 2025-04-17 03:38:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9018187a-310f-31bf-ba33-f013376852a5 | -12.36031 | -39.09715 | 2025-04-17 03:38:00 | NPP-375D | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 851e112d-9e52-3912-af4d-b78639e34e32 | -9.79846 | -36.95329 | 2025-04-17 03:38:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 88f427c6-4dd1-31d6-bec2-0e2c0814e836 | -11.41297 | -42.2923 | 2025-04-17 03:38:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d5c1f75c-ae2e-3ae8-b9a4-1e2b907b13dd | -22.69949 | -43.34671 | 2025-04-17 03:40:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a54b7e3d-235f-35e7-b8b3-bb579371e7a7 | -21.21739 | -48.61505 | 2025-04-17 03:40:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 74e24d20-2365-3f1b-b8db-079a2aef0b63 | -21.22432 | -48.61187 | 2025-04-17 03:40:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7931e415-d2e0-3379-8f03-01cbc81d1f69 | -21.22324 | -48.61657 | 2025-04-17 03:40:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1313bdd6-e225-3d29-a933-f85f783b0332 | -5.64455 | -43.70472 | 2025-04-17 03:57:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 648690e3-4def-3ff5-9ce6-165ef5266cb2 | -3.12793 | -40.98913 | 2025-04-17 03:57:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b3c706cd-19d7-3105-aead-985350fef854 | -2.90927 | -40.20768 | 2025-04-17 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b767daf-72ec-304c-8231-8f68b9e09f18 | -6.35786 | -43.6575 | 2025-04-17 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74fc90fb-d844-3c46-bb6e-742aedc6d33b | -5.90493 | -35.31495 | 2025-04-17 03:57:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 96bf61f9-972b-3b74-920e-c4453b377d63 | -6.34711 | -43.65736 | 2025-04-17 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a833cde-eed3-3d73-b9b7-de4c47d4e776 | -6.34786 | -43.65293 | 2025-04-17 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27f4af64-1ca7-3268-ae04-a15c13f0594d | -5.58478 | -37.28771 | 2025-04-17 03:57:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f59d5880-3d40-3b05-b91f-8054342ffcbb | -3.42098 | -43.1665 | 2025-04-17 03:57:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11e868d3-fefa-3bbd-8e98-fe3019dbe3f8 | -7.95114 | -37.17889 | 2025-04-17 03:57:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b92e7df0-fe0b-3422-8669-ec33ea1ab382 | -3.02074 | -40.02304 | 2025-04-17 03:57:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 37d5d208-3652-3774-844d-171ac1c32579 | -6.34286 | -43.65507 | 2025-04-17 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fdfec670-3dea-3049-9a34-f8e300e94ec6 | -8.07262 | -34.97709 | 2025-04-17 03:57:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7fd57c7a-0b61-39e4-abfc-c185ddf62c49 | -3.96042 | -41.48668 | 2025-04-17 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7651faef-2384-3e0b-b158-396184111e60 | -6.3591 | -43.65472 | 2025-04-17 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bb6dbf6-33f3-316a-8c22-48475c77b744 | -6.18916 | -48.04131 | 2025-04-17 03:57:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c3d501c-4555-3860-bf7a-3755d0e7ab13 | -5.58825 | -37.28824 | 2025-04-17 03:57:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6ce2d974-810e-35a9-bdb9-2de4221db452 | -6.71677 | -47.61092 | 2025-04-17 03:57:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f938550d-c359-3d2c-91ec-4f3906806692 | -6.34964 | -43.66074 | 2025-04-17 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f08babd-3d6a-3e08-b25a-1cd966a3c3e0 | -6.35835 | -43.6592 | 2025-04-17 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f490e74-6c4d-34e2-8e21-0b7cf98492d4 | -5.63923 | -43.71341 | 2025-04-17 03:57:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db92a1fe-ad88-3e0c-acb2-a1d01c823a81 | -5.64303 | -43.71399 | 2025-04-17 03:57:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cda05148-3d9c-3e69-bced-4f6eaefecb3e | -5.94016 | -44.47202 | 2025-04-17 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6733ba1f-883b-3178-9d8c-e5da762da0e8 | -5.4957 | -43.94955 | 2025-04-17 03:57:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17598c4e-71a7-31f9-8715-2628d3e677d9 | -5.48077 | -43.33145 | 2025-04-17 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1b28fcfa-9d26-310a-beee-a22588bf6790 | -5.941 | -44.46699 | 2025-04-17 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README2.md)
