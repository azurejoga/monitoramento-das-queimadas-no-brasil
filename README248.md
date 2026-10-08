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

## Dados Diários - Página 248

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb051283-79d1-37e7-b135-898d264838db | -5.75308 | -42.07405 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c7dd795a-baba-34a4-8182-e4643b384f6a | -9.13585 | -45.83501 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 47ec3c9a-6f5a-37cd-86af-481eaf3f96b7 | -9.36617 | -45.94312 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 4b53e409-3b77-39cf-bc7d-0c23219d5bdd | -5.70982 | -41.7365 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 1c78b8b3-0dd3-3b9f-b192-83ec1b0dfd5b | -11.07968 | -44.00632 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 9aca9699-6c0f-3681-b547-a9ba93be2644 | -6.33283 | -43.34721 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| d971cf4d-09cc-3e18-a674-d11c0d9caee9 | -6.33865 | -35.13194 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 05560826-ac31-3aae-aec5-47e93c325696 | -5.18047 | -38.44837 | 2026-10-08 15:41:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 18.9 |
| b66fd239-f11c-3086-94a8-af952ac65169 | -5.72509 | -41.77681 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| cafbb9ba-455d-3ba4-a2a8-74dcac20d5d9 | -7.47825 | -42.79433 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1b8440ab-3c6a-3802-866f-4c25e97d9e5d | -6.67923 | -44.32214 | 2026-10-08 15:41:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 197c2117-ca46-3469-a8ad-ca8a1a243f4f | -11.24315 | -45.24392 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c84278bb-f5ac-3138-a623-d465cca8ceb6 | -6.34729 | -44.4129 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 977bf2d8-014b-3def-aab0-0f649625cc71 | -9.36694 | -45.94966 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 9f159f90-ede7-3398-8243-1af7a3e89485 | -6.53581 | -45.37315 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 9bf523ac-94c7-3d1f-b4ff-a0f158a59c34 | -8.21294 | -46.38881 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 288.6 |
| e3d445af-e327-3a13-a05a-b76957335143 | -7.18758 | -44.28427 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 93089c03-46e6-3f4f-9998-4ef4d1e31834 | -7.6375 | -44.37629 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 2a687e5e-5792-3ee3-b790-4fab780140ba | -8.93268 | -45.18512 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 4176e31e-b5bb-305b-824f-1b08f606512f | -5.74921 | -41.65461 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| bd35453a-25b6-35f6-9d8c-6ef908b553ba | -6.32106 | -35.13078 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| a3abda88-36db-3f65-8056-29605486f87d | -8.96237 | -45.1451 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.3 |
| b52da23a-2659-385d-aea0-6a0a30409bb3 | -6.84635 | -41.75087 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| 43daa968-e38f-3f87-865c-7edde19bad76 | -6.93395 | -43.66652 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 4323487b-578f-3f37-82b6-e7ebe523bf24 | -5.30275 | -45.72252 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 9f2babc3-7999-3e38-b50d-4911488803bf | -5.37639 | -44.19262 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 496d209e-452d-3a2d-8cba-ceaa3fbce195 | -6.59403 | -44.85822 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ca33380c-9ecf-3864-ab83-227e9d7b852a | -5.83013 | -42.42483 | 2026-10-08 15:41:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb5347ee-c443-3704-9c78-7f369a068630 | -5.71714 | -41.64416 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 46.0 |
| 081a3e1a-093f-3e3e-892e-78595c097db1 | -6.82197 | -39.54307 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 37bcad5a-3974-3c81-8df8-1012d6e22c03 | -8.94623 | -45.17559 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3ab6e348-0a65-36d8-9047-3dbf66a4e041 | -6.31875 | -35.13867 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 37.8 |
| 61ef5a25-b47c-390d-b42d-f1f14b517a47 | -5.76468 | -42.06704 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 887639b7-1456-3711-8dc4-eb56418efd52 | -7.48668 | -42.81807 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 31546422-a169-3cbd-a91d-98b104900209 | -5.78144 | -45.38066 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 5609284c-b3c9-353e-be19-da6ff9f2fcbb | -8.61796 | -44.87801 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 8c6f53fe-35ab-33cf-abe1-56e6083c2772 | -7.40332 | -44.45052 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 053af75c-e6f9-3c55-8876-43c06711bc50 | -6.33337 | -46.9519 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fc2d80b8-ea1f-315a-9a57-06cacea3c877 | -7.15428 | -35.79823 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA SECA | PARAÍBA | Brasil | 2508307 | 25 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 13c08d58-e470-3cb1-886a-b7707b1147f7 | -5.36687 | -43.20248 | 2026-10-08 15:41:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d181d5b4-9b1a-37a4-8453-1898545fe28f | -9.97313 | -43.52328 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 258e941c-5bee-3992-95db-ab46a149f881 | -6.97097 | -43.89334 | 2026-10-08 15:41:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f2e35c17-c42a-31b4-be32-ccdf91adbf6d | -9.34305 | -37.20813 | 2026-10-08 15:41:00 | NOAA-21 | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f58bcaff-dda2-3134-89a0-1eda373c5ac9 | -7.1865 | -42.0027 | 2026-10-08 15:41:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e1573a01-e525-338e-900b-2cfcf24dd561 | -6.64469 | -43.76513 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 897f85ad-b38b-3438-a289-3f78f8ac2e10 | -5.12096 | -36.86706 | 2026-10-08 15:41:00 | NOAA-21 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 54.2 |
| a41ccdf9-53b9-35be-8a00-fc25128d4ccc | -8.93201 | -45.17949 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 340.0 |
| c3e31028-180f-34b2-9b8f-371d35ed9204 | -10.98855 | -45.40454 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| ecbf0b14-25a4-3ae4-98d4-b768c0af73dd | -5.3758 | -44.64322 | 2026-10-08 15:41:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| de009540-79df-346b-9811-0e5382110721 | -9.39496 | -45.8902 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 3536c482-729b-3a2c-9f6c-a4922ba7f669 | -8.19564 | -46.36408 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 8881c425-40ca-39af-8f66-27cf9ef3a45e | -9.92078 | -37.59475 | 2026-10-08 15:41:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6734af14-e95f-3324-8d1b-0130c60f641a | -7.40549 | -43.7422 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae0f6e3b-650e-3294-bb14-9f0ff25c1a0a | -6.67986 | -44.32675 | 2026-10-08 15:41:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e7980805-387d-3643-a7a9-76f04a63a570 | -6.82252 | -39.54707 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 8085df8d-a409-390d-9e43-ee5d5ae6b3a0 | -9.03084 | -44.37701 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ce7eb5c2-ad75-377e-adc4-5a72adb53006 | -5.47808 | -44.60289 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e7aba431-ceb2-3ac6-bf07-ea8deb0a0cb8 | -7.21202 | -44.28172 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| d6a1b8a2-1fd8-3fa4-b44d-a0cd3955cbef | -9.14125 | -45.82185 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| ff70d641-70c8-3de0-9717-79e8f82f4b51 | -6.66637 | -45.36099 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 4b6316f8-3a73-37b1-8a51-438e0407667f | -6.77058 | -44.12077 | 2026-10-08 15:41:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4336cb5b-10cb-3c47-8953-cffde81137e8 | -7.47876 | -42.79797 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e939ec82-99af-3be7-b78b-14baf0a93b7a | -5.7346 | -45.14872 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 093e9647-db53-3097-a653-20b59b54a362 | -7.17157 | -44.8229 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| c286113f-49db-34a6-89c7-12d29b16c55a | -6.40795 | -37.78941 | 2026-10-08 15:41:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 7fa13dce-0eb7-37a1-ac12-c52ab1aebf16 | -7.47329 | -42.84564 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 35.1 |
| 4482e090-2653-3da7-b07c-2f5e66269ff8 | -7.26014 | -45.34392 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 8c5227d9-15d0-3a00-8989-3086819cabe4 | -6.99307 | -41.48039 | 2026-10-08 15:41:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3fd567be-2284-31cb-9194-8a2566ad1e9a | -8.95186 | -45.17795 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 01a082e6-8950-36d6-92ed-30d4d59bacc8 | -6.36324 | -42.91547 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 10.8 |
| afd51b53-2db9-3489-9539-ad688147e95f | -7.48333 | -42.79244 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f29751f4-bcdf-32f1-8f0c-19a876103cce | -7.39878 | -45.64278 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7b44fdfb-70d4-31d2-882f-64904cdbc5a7 | -8.68762 | -41.20418 | 2026-10-08 15:41:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 26.5 |
| abb3ca08-0db9-3a30-b817-0ec6fc4f8441 | -7.47822 | -42.79655 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 236a19b4-498b-39f1-88bb-741fc4cbe672 | -9.14038 | -45.82516 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 524c1042-6d3b-3590-aa87-603d48f9b1d4 | -7.46604 | -42.82898 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 7ad2f3ea-86b8-3277-b47b-a6d4c3638908 | -6.22305 | -44.97534 | 2026-10-08 15:41:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 82060420-b5e7-3659-a864-892b7b9b5e22 | -9.90396 | -45.19288 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 68f251dd-6347-3e98-8b21-5f605891b6a9 | -7.25041 | -43.50954 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| b6755754-62c8-3093-8ff0-e40dc0e3b31b | -5.74645 | -41.70821 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| a43dee54-46a1-3987-88f8-08ee5adf762c | -5.74588 | -41.74106 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9d8f9115-938b-3fae-80b1-4d27e271d39f | -5.73399 | -41.76665 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ea6d0aba-e67e-3a20-a75c-eee6770231ae | -8.21269 | -46.33013 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2da37c39-5ff4-3c94-a4d3-5489a1192a73 | -5.98612 | -41.3662 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 040b2530-a66a-375e-9159-7502bd8492f4 | -6.36229 | -42.90851 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e9719e30-8260-3fbb-9efe-17b264ac48a1 | -9.43775 | -44.6031 | 2026-10-08 15:41:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b5558e42-db27-3e31-88c2-57e9d4753fa3 | -5.3026 | -45.71835 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d8088be7-8d3f-3207-bffb-800cfe8b7708 | -11.21801 | -45.26493 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| e27a3c29-6c6c-3b0c-9537-c7bb0acf451c | -6.53002 | -45.37922 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2d681f9a-4628-3009-a843-aeee4da3216b | -6.16803 | -44.84965 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 8dda988a-74e9-37b0-ad11-103c2e667242 | -6.3479 | -44.41742 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 7b2a103d-1e2e-3043-ab83-46a324acda9a | -5.38765 | -44.18712 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 233bf5ea-44e8-3a87-8273-5beb8f9742f0 | -5.15805 | -41.17015 | 2026-10-08 15:41:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 08b75eca-ef19-3307-8273-725ee9aa0f2a | -7.11285 | -42.54023 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| be01c2ee-4d6d-3f34-ad6a-97071a7d8b34 | -6.16514 | -39.44107 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 9e38c89b-1491-3a6e-8b49-3771d4c11c43 | -6.1687 | -44.85468 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| f84e5c80-5d09-3183-9d2a-44108144f985 | -5.71648 | -41.64107 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 2e6f6675-9d00-31e9-9a68-775cff7b407c | -8.63657 | -41.04933 | 2026-10-08 15:41:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a6464502-cd50-3924-af5b-c07069904a5a | -6.49699 | -39.94653 | 2026-10-08 15:41:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3b7fbf1b-cc67-3786-bd70-a94c6f425617 | -6.6347 | -43.77458 | 2026-10-08 15:41:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README249.md)
