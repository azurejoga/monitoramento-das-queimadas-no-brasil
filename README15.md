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
| be06c82f-370d-3489-b84c-ae0d58a9561f | -7.44244 | -40.10891 | 2025-09-22 04:17:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3624894f-b23a-3fde-941d-07d569ec15b9 | -12.36212 | -44.21509 | 2025-09-22 04:17:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 767663e3-60dc-39b2-a82b-9e0aa6157904 | -7.23256 | -43.75905 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6eb4488-869d-3c2b-b514-0f334beea2de | -0.94558 | -47.35224 | 2025-09-22 04:17:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6be406cb-98ac-315d-bf17-5a2e4e32c22a | -14.98352 | -44.4146 | 2025-09-22 04:17:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dc2a256-8f67-3b89-ae36-f0409eb6f8da | -12.07407 | -44.8535 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ba3efa0-4581-3ced-8ad9-d6edd73d849c | -3.21599 | -43.33128 | 2025-09-22 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ee8e78d-cebf-3efa-8159-e479f62ec757 | -6.90022 | -44.7695 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 03d7b5fa-ddcf-33dc-9e07-01d0edb9ac69 | -12.70427 | -40.47314 | 2025-09-22 04:17:00 | NPP-375D | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 36ccb05d-2756-3425-a2ed-a0551a6caef1 | -6.00968 | -44.33576 | 2025-09-22 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74cb266d-e89d-3432-b39b-4f08e52a7aae | -14.84415 | -45.13047 | 2025-09-22 04:17:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb7e134a-9304-3b71-9d9d-67370daeffb0 | -4.30698 | -48.09867 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ca774a4-0ed2-30f6-903a-4e2418186287 | -11.99221 | -47.19556 | 2025-09-22 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31305719-1404-3adc-8cb6-606f6c7d4a84 | -12.34563 | -47.76271 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94b2e3d1-e8c9-3413-add4-f28b64660dd6 | -7.93916 | -44.10128 | 2025-09-22 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b6b53f47-77a3-3841-9409-1d6029afb08a | -7.22756 | -43.74752 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a415a9e2-8213-3102-a7ed-6b109186d0bb | -7.8177 | -46.48239 | 2025-09-22 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4478d7d0-94d3-38d1-ae5f-59b74602ed74 | -14.9696 | -44.416 | 2025-09-22 04:17:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77f5711b-4cb0-3300-8f79-de91a085d720 | -12.72546 | -46.82748 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85640fa8-dd6d-3a96-9bb4-37a34cbd06e4 | -8.84716 | -43.0201 | 2025-09-22 04:17:00 | NPP-375D | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ec099027-fb38-38b9-bbc3-466e365d1356 | -5.65626 | -51.46627 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 755196be-91e2-3a68-a90b-63544ab0a67a | -7.962 | -43.893 | 2025-09-22 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d561ba4-24b8-34eb-9060-bbc17adfd651 | -11.31175 | -54.34484 | 2025-09-22 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01d88660-0a0e-3b85-9daa-172d57834504 | -13.71165 | -47.57715 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da31db40-b5d6-3232-9d58-a8f3c3faea3c | -11.63915 | -44.33717 | 2025-09-22 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eb6c59e-4d98-3179-831a-889274f4dba0 | -7.22312 | -43.77543 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7e3e5d3-01d4-37b4-b62b-1546377d2288 | -14.33178 | -47.79816 | 2025-09-22 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 156ac689-d689-3050-bf88-b9645b335c52 | -7.81701 | -46.48655 | 2025-09-22 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0798cd33-8662-39cb-a020-f5526b6f1b9b | -0.94852 | -47.36049 | 2025-09-22 04:17:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dccf3313-07fd-3528-82d0-27950143f92b | -7.81483 | -46.19806 | 2025-09-22 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 584281a0-2aea-396f-89f8-36775ee0a8fe | -13.49788 | -47.25913 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e5d9bfa-59b2-33e0-a441-5da4ecb59b28 | -3.8458 | -51.33929 | 2025-09-22 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb7a50c5-176d-3319-9310-2df3b54d22da | -11.27453 | -46.20568 | 2025-09-22 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc5d521d-d27b-367e-9520-5f84d6700bde | -4.87151 | -45.80991 | 2025-09-22 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9612a279-fddd-307d-afbd-6e4e131a7a0f | -5.57455 | -42.12685 | 2025-09-22 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 9e1bd3eb-c209-3b51-ad42-cf4a815024cd | -3.88281 | -38.39983 | 2025-09-22 04:17:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 828cdd15-116e-3dcf-8d06-268984d68eb7 | -7.60879 | -44.49133 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c12254be-4f1f-3c47-bba9-8a5948fe6226 | -5.03677 | -43.60761 | 2025-09-22 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40d30a9e-4fc1-37a0-b993-38b665be9e39 | -4.83327 | -49.54146 | 2025-09-22 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7380a3a-4b0f-3b0c-924d-8e78b1ea3962 | -4.13422 | -41.55365 | 2025-09-22 04:17:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c6d75b9a-313b-3ca7-af64-69b61197b92d | -13.74496 | -47.84238 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a51e2f77-77a1-3293-b24a-10d346ee8586 | -11.61876 | -52.23478 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91755159-2453-3414-8f0c-33cdc80ac9f1 | -11.32366 | -54.34351 | 2025-09-22 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 717bc267-c742-3906-b359-c2c47b4c3b67 | -5.81293 | -43.87836 | 2025-09-22 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad4c445f-eccc-310f-9eeb-715598616733 | -3.13938 | -44.42561 | 2025-09-22 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 677d242f-f944-36f7-97bf-575796117c29 | -3.17223 | -41.05974 | 2025-09-22 04:17:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd3b00b2-f495-3b44-9621-45709a6702c7 | -3.84646 | -51.33971 | 2025-09-22 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad1ad754-0552-3613-8c2c-7732500c6cbf | -7.44307 | -40.10469 | 2025-09-22 04:17:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 89e70a1b-97c8-3126-a58a-251645b5585e | -13.61968 | -47.41449 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb02d0ea-64c7-3081-8fa2-a0a49c0a9c03 | -3.85116 | -51.34383 | 2025-09-22 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc35fc58-a8e0-3fcf-ae23-5b2b68bdf1e3 | -3.85322 | -40.34187 | 2025-09-22 04:17:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2c5d30fb-e606-3610-a37f-a93af5e0e1b4 | -6.11428 | -44.0053 | 2025-09-22 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cc524b5-3db2-39e9-8cd4-b7d993247bff | -14.33607 | -47.79452 | 2025-09-22 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17bd1f48-45e1-3f3a-a5de-1b538aadaa7b | -3.87898 | -38.39923 | 2025-09-22 04:17:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f7a2617f-f728-3f66-a726-4c108ea078fb | -12.45119 | -45.10517 | 2025-09-22 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9380b736-636f-35cc-af0a-85a737f01d94 | -13.30373 | -47.29693 | 2025-09-22 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 841f4a25-3943-3cb7-99e1-d1939a959aa4 | -13.31136 | -47.27332 | 2025-09-22 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 149e079f-db3a-309d-8d9c-10bfa050c163 | -12.71341 | -47.7094 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e2140a8-fdd5-30b0-bd32-aa6e67568e8a | -14.26972 | -44.3808 | 2025-09-22 04:17:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd0c5420-5a65-3eae-9bce-3fa81f9d829d | -14.97461 | -44.40572 | 2025-09-22 04:17:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dff40296-28a4-336c-acc4-e7d6dbac1daa | -11.26987 | -47.47559 | 2025-09-22 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6219605-0f92-36a5-b8ca-a2ccdfe203b3 | -8.84994 | -43.02415 | 2025-09-22 04:17:00 | NPP-375D | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f1d5e2bd-9570-30e2-8baa-a84e739fecf0 | -14.23135 | -44.31936 | 2025-09-22 04:17:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddc74d19-272e-37f5-aac4-f1de530e5037 | -11.42607 | -55.01126 | 2025-09-22 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98d87768-842c-3bb4-af98-e9dc713d6a69 | -7.60936 | -44.48777 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9ad9cb4-9cf8-371c-8b8c-91a8bb8613e9 | -4.31177 | -48.09561 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| df884ae1-cc78-350d-a403-87b63036025b | -7.38203 | -44.57611 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 549e1ea7-66d5-354d-99ab-70dab04ba1dd | -12.30214 | -47.42652 | 2025-09-22 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c31778c5-bd24-3142-92e3-5771bdcf79a6 | -7.37924 | -44.57195 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59eda007-4d5f-30f7-8922-fbd90956c4f9 | -12.71702 | -47.71004 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b94f87ce-bd73-3dd2-8409-a63628da3418 | -5.10833 | -46.16409 | 2025-09-22 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32fde0cf-976c-353f-8f8f-ee4a14b46e25 | -7.8013 | -46.19142 | 2025-09-22 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 75abfe0d-dec6-3513-890d-fb6234bb83ab | -13.07508 | -47.02269 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 453de356-3856-37ef-a2c5-9580be67e48f | -7.22089 | -43.74646 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 228dbfb8-ae91-3e17-8195-f7b1e2a4113b | -5.55113 | -42.13431 | 2025-09-22 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| beaa2fa2-e5ba-328f-a50b-636444852877 | -4.4289 | -47.26699 | 2025-09-22 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53da91e0-fd93-326f-b591-c23e28a6021c | -11.73373 | -47.80318 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 842eb40a-7e1a-3dc3-bfae-a40411c9f805 | -7.91371 | -43.8745 | 2025-09-22 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2db7aec2-bdaf-3159-bb35-af0bf1ee53e1 | -7.79841 | -46.18676 | 2025-09-22 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ee4eb4c-b053-3b1b-99b5-97a5981cffad | -8.01558 | -45.71763 | 2025-09-22 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e352ae5-fea1-313c-bc0a-c206a108d2a9 | -12.96336 | -46.38798 | 2025-09-22 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7fb7f45-0899-3606-9df8-1bb0d47dc16d | -7.36412 | -44.55841 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3d8959a5-c51f-3f92-b747-dd55c76ebd8f | -7.3725 | -44.57083 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27b3d35d-45e9-3b83-bbba-2b4f9064cf47 | -12.4271 | -45.14878 | 2025-09-22 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8a5d472-fdef-3216-aaa9-f5665ab5b775 | -5.81349 | -43.87483 | 2025-09-22 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e39e9a3-4aff-39fc-950d-e00401d8d8d6 | -4.31115 | -48.09937 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ae0a8f7-d29e-37f8-8ced-5f0ba3368f78 | -12.74671 | -47.7547 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb67c6f6-a800-3d7f-b90f-9e0ab809afeb | -11.9299 | -43.43095 | 2025-09-22 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8d0a2ed-4df8-343f-aeca-41543b20debc | -4.63427 | -45.61131 | 2025-09-22 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a60656f-f9ae-3fe5-adbf-a9b231b4551e | -14.98018 | -44.41404 | 2025-09-22 04:17:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2177339-baf3-3622-af4b-cd233bfc2f3b | -7.93582 | -44.10074 | 2025-09-22 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 611eb224-314f-3c8a-9a5f-4e0924b6c315 | -6.01364 | -44.33272 | 2025-09-22 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c3fb4ae-2966-33c5-9f73-dc98f66e8bcf | -7.51308 | -43.69255 | 2025-09-22 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c46a8a50-8fc2-3346-93a4-c8f2fd6efc12 | -4.3124 | -48.09184 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e7bcd7cd-48de-37f2-91b2-c46af04263f5 | -12.9664 | -46.93964 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75ce43a3-9319-3e62-bbc9-84deaa4ed1bd | -5.56188 | -46.28286 | 2025-09-22 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1592538-c353-3f1b-8089-81c9a3e25aeb | -6.44885 | -45.67918 | 2025-09-22 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02d1d40e-b5bb-3b99-9382-7486e5ffc45a | -12.69245 | -46.84663 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7f5e62c-7fc2-32ee-8503-76c97cf83a8d | -12.97705 | -46.39023 | 2025-09-22 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b51359b7-2551-3db6-951b-cddf67bc4be3 | -15.54981 | -41.01411 | 2025-09-22 04:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README16.md)
