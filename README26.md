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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea39724b-fccb-3854-a364-9f01c7dce0d1 | -8.38719 | -46.24572 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9946fd9f-9cf6-3f40-a9e6-5c048c561356 | -7.10915 | -44.74737 | 2025-10-17 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56c06568-0527-3d53-b569-eaf2a2e8dac3 | -5.9843 | -44.15288 | 2025-10-17 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70d43124-5424-32e1-b01d-8e8ae8a4fed1 | -6.2016 | -41.75179 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b2516369-6c5f-3704-86c9-e12ecaadb020 | -8.23962 | -44.01986 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1adc8a96-6723-3fbf-bbf0-25664cc1b440 | -7.84134 | -45.46124 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a52e0c14-0c18-3228-8a27-cb300ff5170a | -8.25603 | -44.07033 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43930019-731d-3d02-b7c4-41823c267be7 | -4.95621 | -44.96384 | 2025-10-17 03:28:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 707c7abd-aab2-37b7-a46f-b15c69c56b09 | -8.52214 | -44.57718 | 2025-10-17 03:28:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01f74737-78a6-3465-a990-e986db179a72 | -8.4031 | -46.29486 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4234991c-a806-31db-8fe4-5cc156548a07 | -8.38512 | -46.25638 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1a1fe037-ca8f-335d-8ddf-c670838398dd | -6.40183 | -41.48538 | 2025-10-17 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 822f741f-dd2d-37d3-946f-a601a41c5f01 | -8.30277 | -43.42333 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7b485a16-315a-379f-8af9-57541b0a58c4 | -5.85349 | -43.88177 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d154aec5-ef01-308b-b775-aef69a35a8fe | -3.98022 | -42.49718 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| afdbdfda-e95e-3879-bb42-c149127cdf35 | -8.39813 | -46.24603 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0cb84773-9ef6-3523-bd69-a646775a6d38 | -7.94469 | -44.11795 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ae8bb830-80b8-351b-9caf-ca0bb4d2c78e | -7.17828 | -42.37357 | 2025-10-17 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6189e5f7-e213-3d36-9236-dc88440f6453 | -7.45585 | -42.15792 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc1974d5-9ff9-3f73-beb3-7f3fc3597685 | -4.39914 | -43.41542 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0d6f70fa-c92d-3fcc-a1a2-1603deaa7899 | -8.56551 | -44.5947 | 2025-10-17 03:28:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3877221c-0ebb-38b4-bd65-a63f6a154a5c | -6.7473 | -42.37759 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d7321704-ba85-30ac-82f5-6bf88d1672af | -7.07773 | -44.94826 | 2025-10-17 03:28:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1e3a021-5fe7-3224-ad46-933c04706992 | -7.13306 | -38.21746 | 2025-10-17 03:28:00 | NOAA-20 | IGARACY | PARAÍBA | Brasil | 2502607 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4208a5a8-22f8-3dd4-aec7-3312e6d998c0 | -5.88302 | -43.90023 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e853e5cb-deb7-316b-98ba-e666a3287d34 | -6.74215 | -42.37296 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ed864836-5ab5-3525-8557-bf880cc31e34 | -7.45516 | -42.16183 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e100ca16-b67e-3f32-a608-213a6c40aea5 | -7.47263 | -42.75517 | 2025-10-17 03:28:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| de495816-67ce-3458-aa8c-769be2373012 | -4.0023 | -43.2781 | 2025-10-17 03:28:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a9b6ad8-3a15-3f71-a1a9-0a7139f898ce | -5.84801 | -43.87542 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2351959-d673-37c5-957b-ec5140fd403e | -8.16484 | -43.31145 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 31b46969-a2a2-3557-9e5e-71c8cbf412a0 | -5.45764 | -41.01871 | 2025-10-17 03:28:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 64bfdf1b-b67b-317e-9118-7346b9d0a645 | -7.28238 | -41.95594 | 2025-10-17 03:28:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 27eb7ed4-c926-3e2f-bcdc-ba58cd9a7515 | -8.19397 | -43.32185 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 3d938f96-df31-3328-9ef1-a9f08c6dca68 | -5.57449 | -41.3217 | 2025-10-17 03:28:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9ab71807-47cc-3452-b808-b13a56983da5 | -5.88485 | -43.89251 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef901cc6-6cb3-31bf-9713-bfe683d60d32 | -7.46004 | -42.66668 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ee296ba9-a2e5-3870-95fe-fd17c318d5b6 | -6.20434 | -41.73632 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 885b75ef-0efc-3742-ad16-890f7c9e1f4c | -7.35579 | -43.8598 | 2025-10-17 03:28:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5a7094ce-6b65-3086-b9dc-f656393ed4cf | -7.46076 | -42.14674 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2228407-6b78-38c8-a047-dbd966bd47aa | -8.40931 | -46.28381 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5501207-f3a1-30dc-bad0-da8ff5d7e677 | -7.83316 | -45.4665 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ca38c23a-ec66-3eb9-ab3f-22e0781c29b7 | -7.27848 | -42.31708 | 2025-10-17 03:28:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7c375502-773a-33f5-952a-5d7b73271e98 | -4.38464 | -43.38524 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af325c00-d03d-3c65-a7a8-f3089c620381 | -8.38541 | -46.3307 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0a1658f-0ae2-306d-b066-ab8e81248328 | -8.3045 | -43.44687 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a9d29243-008f-3c71-953a-a57bf03229a0 | -7.03308 | -41.82364 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eb3018ba-9540-354c-85aa-4618f5cfa1a6 | -5.25917 | -44.2168 | 2025-10-17 03:28:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8bc9f7f-6279-3b33-b449-a270cda512b1 | -8.4497 | -46.24632 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 854000e1-ffcd-3dd8-800e-6be3ea30910a | -6.29024 | -44.01468 | 2025-10-17 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0c23254-c745-3778-a113-03898550ea62 | -6.94433 | -41.56202 | 2025-10-17 03:28:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50f8b26e-f9d1-3dd7-98d3-ee0412975fcb | -4.41376 | -43.40749 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1d0b1e26-f862-34ed-a0c2-6dd53ed19b8e | -6.74811 | -42.37307 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 12851313-aa6a-36fa-ae23-ad9ef50c2e2e | -8.25945 | -44.08669 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61b52926-3ba8-3bc4-892c-7dfa7e2d44dd | -6.3165 | -40.94592 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 60aa89f7-a4f5-3961-b653-18e2018332f9 | -6.39641 | -41.48505 | 2025-10-17 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 658a8ce3-a2e2-35e2-9b3e-4216ac026929 | -7.20694 | -45.50124 | 2025-10-17 03:28:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| df3f03a6-7fd7-3bac-bc13-9d933504d215 | -7.05584 | -45.05588 | 2025-10-17 03:28:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 924bdb92-7aa7-3491-9b8a-f2968a0b2a5a | -6.08871 | -42.38617 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fc0dd5a9-3863-34b1-9996-e8da547271e0 | -7.10365 | -44.74003 | 2025-10-17 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8321348-3e03-303f-859e-8458fee48d45 | -7.33451 | -44.16166 | 2025-10-17 03:28:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35697567-91f6-3806-8488-6c80960ffba3 | -8.07042 | -45.4156 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8720cdf-93eb-34aa-bc1f-6d85b46cffc8 | -3.62542 | -42.77652 | 2025-10-17 03:28:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 61dbc3bb-71f8-314c-ba5e-15b35e479521 | -6.13846 | -41.73007 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 635f0c2e-042a-3123-a455-bd570267561b | -8.39423 | -46.24743 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9a18ff26-0bd5-3d7f-9b2e-fa6805928fda | -6.12909 | -41.75055 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 61301774-45ef-30ef-88d5-179ff3ec05a6 | -9.03843 | -40.57834 | 2025-10-17 03:28:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ad4327e-9a05-3cf2-b390-0e34e3d18352 | -7.48006 | -42.74783 | 2025-10-17 03:28:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 466f4a7b-b0bd-3e01-8e0c-2f7353d72d51 | -4.39186 | -43.41922 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cdfc80ee-10ce-3a22-9efc-b0d7b2e63a67 | -6.13582 | -41.7452 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 15e0eba0-1201-3446-9c6b-2d807e960fb3 | -7.20129 | -45.49323 | 2025-10-17 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1700a336-14f3-36bc-b0ed-6e7ad67347e1 | -8.20171 | -43.31363 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e130bae2-6ee9-3ed8-b945-c12fe4baa15c | -7.82746 | -44.13705 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04fae157-1367-38b8-8111-4e6aa5212f6d | -6.07154 | -41.912 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 167e4580-3ddb-358a-b351-d25e508cffcf | -7.35262 | -41.90854 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 54ea31d8-306d-3afb-a141-d4cc11f8fef5 | -7.33343 | -44.16127 | 2025-10-17 03:28:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 213a4a9f-58fc-3f26-9fcd-fa8a764b9f5a | -7.35251 | -43.85989 | 2025-10-17 03:28:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3d43d8ab-14a1-345f-848d-f42a5acacf20 | -8.3062 | -43.43802 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 775c0422-cb0b-3285-9f33-3477fa90f424 | -6.25527 | -43.91335 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44d7eb6d-6a51-37cc-842d-b5fe8039073f | -7.32815 | -44.16024 | 2025-10-17 03:28:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42050273-4ee3-3d8b-a46c-b994782bdd18 | -8.19139 | -42.35678 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 74845dae-df80-353c-9549-e638ee4dd7ae | -8.40794 | -46.29087 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| deb7c8a4-8fed-3acb-ac51-e6feda522171 | -6.54246 | -43.91895 | 2025-10-17 03:28:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a8e29ae-7ce4-31f1-aa1d-7c0ec410aa33 | -8.07175 | -45.41284 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba8422ce-b4d9-3511-9e04-2d1a82263950 | -6.99193 | -39.22962 | 2025-10-17 03:28:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 15793682-597b-338d-a079-08326acf07fa | -6.19874 | -41.73526 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 05ea4f41-0349-3e1d-80f2-69fe3ba30f57 | -8.44305 | -44.18209 | 2025-10-17 03:28:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f14859e0-15f5-38e5-a6df-01a0691438c2 | -6.20091 | -41.75565 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8f58e2a9-7c5d-3331-96fc-0bce44a4749b | -8.30446 | -43.41453 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f086f6d0-fd99-37f6-9efd-27422d0297ac | -6.1262 | -41.76708 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 26d44e5d-fb31-3975-acf8-6980132eca33 | -7.46578 | -42.16768 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f306a9cc-de47-3f8f-a185-06a7b2b951cc | -6.01355 | -41.93042 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e412ee50-f0d7-3544-a93e-5aa15d9102a6 | -6.0196 | -41.93957 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a4f00138-b108-392d-83ea-eab1ca46d684 | -6.54147 | -43.92434 | 2025-10-17 03:28:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2969758-93b8-358e-bc8d-c1ec40d8ac3c | -6.02744 | -41.9287 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 03ca9472-833b-377c-86db-929f6537ac82 | -6.13712 | -41.73774 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 27f8b935-825f-3f79-b8ee-f78d81e305af | -4.40832 | -43.40086 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 26f22ecb-4056-3254-89c9-8c418a9498f9 | -6.74887 | -42.36885 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 57f585d3-73d7-31f2-bd39-1a11fdeaad4a | -6.07083 | -41.91603 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b9486ad4-df0d-3d1d-9ba7-9722bfef74c0 | -7.4718 | -42.75961 | 2025-10-17 03:28:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README27.md)
