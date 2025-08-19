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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50367c6f-a7f1-3185-ab36-9f440ab3c9e4 | -2.58551 | -51.92152 | 2025-08-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31ad1e7f-5b9e-35d3-a75a-a808eab62cef | -6.94079 | -43.62749 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1501154-283b-3f16-9672-42f0524dbbf2 | -5.7898 | -43.88876 | 2025-08-19 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14ad1870-91fb-3021-8242-5ffbb3290d00 | -7.16594 | -43.50888 | 2025-08-19 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88804eee-4dee-394e-ab93-39a54ee05d6d | -5.78532 | -43.61184 | 2025-08-19 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a07f02ce-0b07-3778-9ecd-750e18791c07 | -6.45241 | -45.45147 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33061404-d8e7-3cd7-abcc-9e06cb443270 | -5.97817 | -44.10085 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f57aa748-3bc2-30fe-98d7-89921e921daa | -6.42489 | -42.49258 | 2025-08-19 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd733df7-61e3-3088-a2bf-33db9fd7254c | -6.39629 | -44.25541 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75af9ae5-5992-3a6a-b027-bafc027b8af0 | -7.59146 | -45.42764 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aaa83521-ec7d-3be7-b978-944b703429a2 | -5.55171 | -49.06948 | 2025-08-19 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd20c346-b63c-347a-8b38-9bb49a24619b | -5.97582 | -44.11614 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d56dbd11-187d-3ff6-93c1-2bb31bf8cc56 | -6.02804 | -44.39257 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4b40696-77a0-3720-8577-a4b5c3d05b8f | -5.97637 | -44.13558 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca45e2b1-bb0a-3d70-b3e8-32e894f087b7 | -7.38271 | -44.90996 | 2025-08-19 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc09ed2f-4c22-3963-b340-eb41e9c20f88 | -5.64903 | -43.38927 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fccff661-0e9c-3bda-b885-c80b3d706c1a | -7.62918 | -46.21908 | 2025-08-19 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fef62f03-cf39-3a26-86f3-871265629a1e | -6.45528 | -44.5561 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61532257-3a8d-3c84-abb1-cb469eac3b6a | -6.55925 | -44.21754 | 2025-08-19 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7b9f205-3810-32a6-98c5-cee3ebae6e44 | -6.96765 | -43.59408 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4cc15849-2d15-33d3-be1c-15ebff3a9073 | -6.24857 | -44.83165 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 896f6d2d-6871-38b2-a4a1-4d5f10daef7a | -4.59222 | -43.31527 | 2025-08-19 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aacf300e-dc82-3789-b89a-3c225ed052a2 | -6.93374 | -43.60724 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bd040ca-8349-3320-86da-7b1c8e3f4421 | -3.47061 | -47.68804 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cadd64b4-6519-32b2-86a2-a49263d1f390 | -5.98671 | -44.13729 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2470e4b-0261-3320-8f01-83168d9a48ae | -3.98076 | -42.52139 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 38a4472b-1a68-3bc4-a546-22b1e07b78d9 | -5.06098 | -43.72741 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22a8150c-12f3-37b4-856c-be0a7a111b7c | -5.64841 | -43.39328 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abf84dc8-4514-39f7-b72b-be87e9d457da | -6.55111 | -44.01091 | 2025-08-19 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 390dd9b6-9478-36a3-80e1-18f5083f2e06 | -6.945 | -43.59895 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4569420-2d52-3bdf-8f17-27ab9b6a6b46 | -5.65013 | -43.40583 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c80af5a-6745-3e68-9d39-b955df51ceb6 | -6.95177 | -43.7739 | 2025-08-19 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53c951f2-e59b-350b-a584-bd97151bda92 | -5.78269 | -43.72437 | 2025-08-19 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a25c679a-31af-34ca-9f46-651686b1855d | -3.45825 | -48.96543 | 2025-08-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0fcf5f6a-6801-3c3f-9618-c8944083dff5 | -6.16049 | -47.27657 | 2025-08-19 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8dd06b99-c1e6-350d-b752-ad01907f7e3d | -6.54908 | -43.01041 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d9f728c-6ae8-3eda-922b-2659ce2310a3 | -7.62756 | -46.22953 | 2025-08-19 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cf151e4-6b5d-3b1f-980c-c141b4ce7710 | -6.9432 | -43.61118 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5871a41f-c133-3b4b-af56-b18b94a6ad85 | -6.94616 | -43.61584 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8cc2436f-a20e-3639-9541-35096839a7f9 | -6.49474 | -44.80236 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c206ddfd-bc90-32cd-ba82-9c9170f517ef | -6.0609 | -44.13203 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee1c89b3-5849-3b32-9ef0-ea49d740afbf | -6.59918 | -41.40462 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f1571d6b-b6e6-3d85-b83a-24748c9cf526 | -7.02442 | -44.27299 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c38d867-24b6-3653-9897-4e08e569c858 | -6.05778 | -43.75145 | 2025-08-19 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2cbd188a-f82d-37aa-97b8-f6abd442f138 | -6.93783 | -43.62285 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0418af6-03ac-3241-8b5c-d5149da503ff | -5.65027 | -43.38118 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8dce46e-b86d-3f03-a87b-67c6e351706c | -6.93845 | -43.5938 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 1c94d90b-0e1a-3f07-a66a-ceb2ed44ed40 | -6.93608 | -43.61589 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6035f287-5dea-3428-8eff-2362040e816e | -6.45296 | -45.44794 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1091ef2e-bc12-3de8-b628-e7489dde8ea7 | -6.95215 | -43.60003 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35260cdd-6760-3b46-a195-d9f555892a85 | -5.65847 | -43.39889 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9189034-396d-38be-9102-859ae873007b | -4.92174 | -43.24435 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e8ab2f1-65e2-3a75-af91-a06464a4f5eb | -7.20143 | -43.96551 | 2025-08-19 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db3444ac-305d-34fa-9afc-690a2a196829 | -7.29348 | -43.6898 | 2025-08-19 04:25:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f1d338bf-01fd-3f3d-909e-e2df7e1fe1f5 | -2.66043 | -47.39709 | 2025-08-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ca87f95-61e4-3556-af89-c9451327dec4 | -4.959 | -43.05023 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 346f9054-408f-3d2e-bea2-a86bfcce3fa2 | -6.39972 | -44.25602 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53abc1cf-f0bd-3dfa-9ce7-7cb1dc6fc363 | -6.94978 | -43.59134 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb55bcac-c03d-3280-a6a9-ba3636ef97b2 | -7.37349 | -44.28502 | 2025-08-19 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44499e00-be85-3775-8c08-61395490608e | -7.51046 | -44.9962 | 2025-08-19 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff8dcd75-26ed-3509-ace5-301557a4b667 | -6.93141 | -43.59858 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 74890696-1007-3922-9b6c-ad061a96d360 | -6.95396 | -43.58779 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ba5ebf4-f61c-3672-8d35-8a41adc7b1d0 | -6.95814 | -43.58422 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57610bce-f142-3085-85b8-fd56e94763a7 | -5.98045 | -44.10906 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 124f8da6-db90-3704-9a0b-e093fee09893 | -6.35806 | -43.26532 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e21143f-6e49-3a65-9f07-382472566b91 | -3.98741 | -42.52677 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f42cb3d2-7600-3a96-a0e0-fe2ae51add95 | -6.84447 | -43.61848 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2492976-a26d-3eba-b96e-1a739f38b7d2 | -6.37648 | -43.31488 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9864d599-e11c-3edc-9a98-9b38747f05c4 | -4.43196 | -47.75803 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efb6374a-74e7-386f-860f-183dd139185f | -7.5842 | -45.43017 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44df92a8-9e30-373f-a5cb-4488ea5cab18 | -6.96172 | -43.58477 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6045ca2e-e924-3b1b-a5ca-29d268515c02 | -3.10807 | -47.49612 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b12ebb50-8e44-34de-b82e-e9ba98ef6369 | -5.87685 | -48.12401 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0961cb46-de9e-337d-8c7b-83a2580bcfb8 | -4.59575 | -43.31581 | 2025-08-19 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3e61f787-7f58-308d-94ff-3432889f15b1 | -6.7428 | -41.53658 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b0db2538-8045-3497-93a6-debf9e8b2c4c | -3.48743 | -48.43946 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9dff019f-b92a-3201-8c32-7c02d36c85c1 | -5.89858 | -45.53819 | 2025-08-19 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6dc62279-423f-39ee-8bf3-e43c14b209ac | -6.03091 | -44.35096 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce2e6c76-f019-3d0e-8b9a-f0eb344bf07b | -5.78885 | -43.61236 | 2025-08-19 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1512611f-e89d-3f30-bcdb-4598629af919 | -3.48244 | -47.68197 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb77ae2b-172e-36b4-bd83-6324034562ca | -6.95632 | -43.59651 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b55153b-f463-3486-8479-7a4e27ef63ef | -6.75578 | -41.56 | 2025-08-19 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a5dbd6aa-f051-34e3-bac2-73852e85b7c3 | -4.59333 | -48.78097 | 2025-08-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4656ec95-a4b7-3554-bf48-bbf562acdaa0 | -5.37717 | -41.2272 | 2025-08-19 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a84853d8-7313-3e60-be4f-a1d5d1c6d1ed | -6.57107 | -43.01374 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed689a9a-f0ac-38fb-a1d2-18ccc14bb04f | -5.98888 | -44.14049 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e26aa444-fe80-3896-852e-aa2f6147cb5b | -6.93189 | -43.61361 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97ad4fe7-22a7-3112-8428-4f9eea6c202c | -7.14151 | -44.60802 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d7cb96cf-09a0-3f36-a99b-14b73a01afda | -3.97839 | -42.51232 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5afd1e73-7106-3df0-a909-c140e726fb73 | -6.67729 | -43.67391 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2421f53e-e88a-3db1-8960-5fb512a66cb5 | -5.87121 | -48.11559 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25f960e7-ab7c-3cda-8aed-63dd31b856a0 | -6.52394 | -44.54296 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 154125ab-2b8f-340c-ad90-3977e16fb15b | -5.61843 | -43.47072 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 121608a2-868f-3b7e-982c-f275d8ffa6a5 | -6.75082 | -41.53778 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 320605e6-458b-3de5-ae06-d2f234ef922d | -7.23752 | -44.25366 | 2025-08-19 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a245e943-e57a-3dd9-8313-3261d207af39 | -4.39167 | -47.77044 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10bd1721-1f8f-3ab1-aa93-19fd0fbeaad4 | -6.94496 | -43.62398 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5feccb8-380d-37d0-aac4-7acd9938dae7 | -6.51686 | -43.4444 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f6bc21d2-5298-307b-ab4c-487b4f396809 | -3.26378 | -39.39358 | 2025-08-19 04:25:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d0b4a389-9d48-3773-bc91-0f5d6c50face | -3.47119 | -47.68433 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
