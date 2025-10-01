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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 413a01c8-0a53-36c6-8f3d-23fe78e4f234 | -6.23442 | -45.33537 | 2025-10-01 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4a0c8840-1cec-33fd-8fb2-807ce63fb9c4 | -7.30541 | -42.8671 | 2025-10-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ff34f515-a1f8-30a8-8d65-731ac6a4714a | -5.79657 | -43.07685 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 62fa1856-51b9-3aa4-b933-4a7ba39992d5 | -7.05153 | -46.4099 | 2025-10-01 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3266663d-d4db-3e23-99e9-d7bc4b92bd6b | -3.46429 | -50.08609 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c4a75158-8d37-30bc-95ea-4bc070f66d25 | -6.49698 | -44.2889 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2cfe086a-e405-3572-98f9-e00d128ac194 | -3.94481 | -38.36078 | 2025-10-01 04:19:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b7ea324c-e71c-33e9-9f95-c371bc51006e | -4.0111 | -43.27444 | 2025-10-01 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 581e4db7-3184-3fa9-9b8b-8e632e47e059 | -9.33209 | -45.70044 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91a43db1-cfcd-37d1-8d80-40169428b1b6 | -9.2694 | -45.69049 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d73f1e4c-c7c4-3a1f-82ff-e10d905e2da4 | -6.04799 | -43.21513 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 11013c24-8ea0-3d16-b51a-2d2b77b2ee70 | -5.38161 | -42.85472 | 2025-10-01 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1372ec60-1722-3523-9e71-ca4d9eace2d0 | -3.09508 | -47.00681 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 164e1d4a-8a98-36db-871e-747315269341 | -6.46362 | -43.93433 | 2025-10-01 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22f7a54e-f2d6-3d32-be38-f0cdc1b18b29 | -2.14447 | -47.50547 | 2025-10-01 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 831274f1-b13f-3da3-a2da-93eb805e0fe8 | -5.2206 | -44.83466 | 2025-10-01 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9bab2c5c-d097-3bb5-861f-4aa058893564 | -8.09141 | -46.54742 | 2025-10-01 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d695694d-8595-3019-99d5-168cf95a3105 | -9.94049 | -43.60058 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bfb2a0ec-bfaa-3415-bfd2-efd5058f41ff | -5.70349 | -42.67849 | 2025-10-01 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 46e5aabf-f40a-393c-8c4f-39dec8f1c1c0 | -7.5575 | -42.4091 | 2025-10-01 04:19:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 762803c4-076a-39f5-ac2a-bfe76af22d7c | -8.55563 | -44.74818 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fa898fd-a5ef-3754-9853-074e61b0bfa7 | -3.46297 | -50.09407 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 39b1bad0-19ce-38a9-a930-d076f9b99623 | -8.54852 | -40.60741 | 2025-10-01 04:19:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f9c42f53-6dc5-382a-8891-8e92c4a1eb3f | -8.54219 | -44.63543 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81aca2d0-4f45-3e2e-8bb8-7e1da4d5e111 | -5.53972 | -51.44007 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 461c0974-f1f5-333f-b0d7-b20bbcaea222 | -7.56498 | -46.28292 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d051265-cc93-3742-8742-58e404f6281a | -6.7351 | -49.64075 | 2025-10-01 04:19:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e96566af-cb14-3d45-a87a-9e3f1bf5e4d0 | -5.83494 | -42.80368 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 87975177-7fbb-3316-b961-6e50d2757ee3 | -5.64166 | -43.94867 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05db65fb-42c3-3107-bbf2-1ccd1d2536ab | -5.93676 | -45.8629 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a660b90-a214-3c84-ae18-94753abf8eb6 | -6.72223 | -44.59331 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 515b1900-e726-3abd-97bd-932bd402bc78 | -8.54495 | -44.63945 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de110260-df70-32ee-8fde-33c20b634c58 | -6.90293 | -44.98171 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 865dfc3c-ac38-30e2-8916-6b5e196bd421 | -9.94345 | -43.65075 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f31f2d7-54ef-395f-8af1-523b0b825bc2 | -4.6711 | -45.68816 | 2025-10-01 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 313b9297-9963-3800-8941-944ef32a0c4f | -8.64703 | -43.98003 | 2025-10-01 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c1021d2-59a4-33fd-bf68-6fdc45212e44 | -6.24158 | -45.33297 | 2025-10-01 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e31e0d8e-497e-349e-a668-e8cd50b412ef | -6.0894 | -42.46792 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 315e928e-efa5-3950-a5ee-fd72b277a9c6 | -6.68013 | -42.80515 | 2025-10-01 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7267d758-6433-3521-955c-b214d14e7cd7 | -7.51145 | -44.28439 | 2025-10-01 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d088902a-7912-3a15-8e0a-7f482843693f | -5.78528 | -43.30648 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7f404b4-1f2c-3811-a6b0-80e0dda29a59 | -5.94641 | -43.31689 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 68b4194e-8f64-3939-90e5-099752119834 | -5.78021 | -42.85939 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ff8aa423-df89-3d33-8824-c02f9a287cb7 | -8.22084 | -45.51861 | 2025-10-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 561f0a0a-76d0-37f5-b2eb-d8bbfa89ed1f | -5.76213 | -42.86404 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fe384d24-ff24-3c1b-b834-f417fe7a9a1e | -5.41396 | -41.32639 | 2025-10-01 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e1f1eeaa-08eb-347d-a3d2-14b0e788fd9c | -7.04848 | -45.17839 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d038c136-995c-3d13-9e10-912634438a30 | -9.92813 | -43.65987 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1cbe909-f4c2-38c6-9334-148ac0293d49 | -5.4772 | -43.0762 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8dd11546-b58f-3671-a0b9-0fd8908776ec | -3.22442 | -47.13078 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 250284aa-15e2-3d1a-ae59-21c4b87fd3a7 | -5.76608 | -42.86094 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 43eea3d4-f45b-39a5-904c-a19b23fc9bf2 | -5.62109 | -43.90639 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| acc1ecb5-a77c-34b4-81e1-d50bc6bc2130 | -6.28544 | -42.49237 | 2025-10-01 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1fcabac3-ae15-3e71-bfd8-7e2d02448d7c | -9.9378 | -43.66518 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dc1bd2aa-fd69-3eab-80ac-7d66ea9f559e | -5.64104 | -43.93082 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 948b8459-0772-36da-8fec-541b4a1ca4aa | -5.74701 | -42.41304 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5c501d09-1883-3e3f-8d9f-26efc04459c9 | -5.8332 | -42.79227 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 84c2fa76-18d2-3770-a117-d98461238c1c | -7.51582 | -45.43357 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ace3a02-4e02-34cc-8265-778c6bd5e865 | -6.40292 | -43.95344 | 2025-10-01 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c95e02ef-0d68-3f59-b02e-7ba8066ea78f | -8.28902 | -50.80426 | 2025-10-01 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f7ed5db-8a24-3bdc-95ba-8cfa2a038279 | -7.74158 | -46.20165 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4368768e-fba5-3d83-8f05-3e12efe91686 | -8.58368 | -44.74186 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 90669735-9a9c-31a6-807a-d17acc1ef565 | -3.42039 | -46.96887 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab265262-8abe-31b9-a258-ed83d06f7081 | -5.31957 | -43.3258 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c98d591-71ee-3c5f-a675-7659df0e0fe7 | -10.21533 | -43.04343 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c7f93fd0-88b9-31ec-9336-94c9f7ebfbdb | -9.47282 | -45.56263 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7705460-7f68-3083-92a9-0714cc401d45 | -8.24837 | -45.53713 | 2025-10-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b782359-8c00-371f-a3f2-33b13ca5c7d4 | -5.39236 | -43.58159 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85e03349-1918-3db7-b5d7-c56bf5759406 | -5.75102 | -42.40977 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e43d8fc7-f4d1-3e3e-a9ea-c9b6515c9cc9 | -6.58323 | -51.68341 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db90a36e-2017-3649-b209-9f817dd2e4c1 | -9.12991 | -50.77599 | 2025-10-01 04:19:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 818f7a36-2ac3-35e2-9b54-fd5e75707a2a | -2.69358 | -54.76497 | 2025-10-01 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05a06c48-1351-3777-9e9c-69620452d0af | -7.72214 | -47.22521 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 825a3a41-5114-31de-9e68-c1e6d3d2f9d0 | -3.76306 | -43.3605 | 2025-10-01 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95905119-2226-3dfc-8d7f-ba3c27f33478 | -7.76582 | -45.76936 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7733ba38-cb03-30e8-b2f0-59ca3e2e0f2f | -4.51948 | -43.79029 | 2025-10-01 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c512782d-d791-3574-96a3-f5c03aa04c7e | -6.01502 | -43.80029 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7758936c-3f4d-3a30-bccf-03a8c9ca0e3c | -5.80735 | -43.73545 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4176cd4f-07b8-361c-bfad-2f9398f24f0e | -5.24287 | -43.09522 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90f499db-bc92-3cd6-9488-cd1c2b91097e | -5.79093 | -43.06861 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4755ea62-f998-3d9b-bed5-65d7f85d226f | -6.03485 | -43.60583 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b84127be-e717-35f9-9690-94350df4f731 | -5.80372 | -42.7802 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ceb81399-7dfc-33e1-900c-8bc1d681f6eb | -9.26225 | -45.69293 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51507da9-825b-3554-99be-011cef94f94f | -5.7277 | -42.88489 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d842581f-dd9e-3ab3-9d26-7950b2e76665 | -4.70457 | -46.47747 | 2025-10-01 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ca1701d-339b-3fe7-a5a9-c159be42914e | -5.27321 | -43.16559 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05459a7d-822f-3457-8c88-21260cdea1aa | -8.90233 | -46.62611 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1df87eb8-f2e9-3181-9f8c-0c0b359981dd | -5.79474 | -43.28968 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74d04412-4f4f-3e8a-ac4c-27575fc4603d | -9.99171 | -43.6085 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 846c154a-56ca-3626-bb21-c7b7082cd4da | -7.79993 | -42.5116 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a14c6ac1-94f4-3a1f-9939-d8a8978b0cd8 | -7.46117 | -47.27782 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b3c5435-c603-3b53-8287-cb95cbc421af | -7.05433 | -46.41404 | 2025-10-01 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1c30691-49ec-3282-bedc-f67c7e0627da | -3.93098 | -41.57712 | 2025-10-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bf0d5f3c-5e44-3cea-89e5-ac17c050f982 | -5.82622 | -43.94169 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 093bc550-9fa8-3065-9574-24ee71f15641 | -7.95471 | -47.30911 | 2025-10-01 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ac2ed8d-bdd8-3947-a8fe-e373b2e68c5b | -5.70293 | -42.68218 | 2025-10-01 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 67a24353-647b-31d7-b0fc-272b646c6984 | -6.11855 | -43.21813 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 94091e9d-661b-3c27-91e6-fbfcb87d96c2 | -6.01224 | -43.79631 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a77a0a73-4ce3-3238-8375-2d0039d25e85 | -8.57857 | -45.49413 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54fb2234-17bb-3eae-92dc-ed556c64219c | -7.55809 | -42.40518 | 2025-10-01 04:19:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README34.md)
