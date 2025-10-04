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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca90f6d7-878e-359a-b916-eca48f66c991 | -6.24686 | -44.23678 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc6e4db0-3383-39b5-bd96-4c72131db60a | -6.44396 | -44.80428 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7ea3dc29-51e6-39f6-8b8d-5e27f4b5e699 | -4.6498 | -47.54838 | 2025-10-04 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3a5c560-d4e7-3f6b-91d3-a12141212dd6 | -5.72505 | -42.68538 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8fb1348b-7a2d-3aa2-ab76-072fefbf5bce | -6.55806 | -44.15897 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2f59ddd-22a2-3615-b96e-f1d4e1601930 | -7.57034 | -42.39428 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 72ec6fc8-4fa9-3958-be3e-ca56fa557675 | -6.38574 | -43.5984 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a064e811-b9ee-3d74-8513-9fbb1081ac66 | -5.84052 | -42.85898 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a2ea529-ca1a-3279-a39c-90bc982a94bd | -6.27019 | -44.04726 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c3c8bae-e997-395b-9d2b-7a5d591e410b | -6.28154 | -42.45047 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 86c4bcf7-4068-370d-97fc-5a7151980e0c | -7.26634 | -45.48145 | 2025-10-04 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3468af1e-bb5d-3b92-8f97-db2c1f313370 | -7.29326 | -47.9566 | 2025-10-04 04:12:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99bd5f94-1015-30e7-967c-edd474f1a6f5 | -5.19183 | -43.58395 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e47489b-c4e8-3f8d-89ba-279072601ca7 | -6.20273 | -44.34032 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5c50e13-7474-36d1-a4ba-f38ca57b76e8 | -5.97667 | -45.2688 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 223e4116-ad4e-3d29-b265-a7e7d1baac5d | -7.74277 | -42.52934 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b38de215-b44c-33b1-a612-f4c596924ef1 | -6.70769 | -42.15956 | 2025-10-04 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cd77d5bb-5d45-3e19-bd7e-285dbfb96d03 | -6.18828 | -43.2577 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c3fc5d5b-d8bf-3628-b729-a0c1003abe68 | -7.04565 | -45.80645 | 2025-10-04 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88ec8199-a34c-3eed-b253-8d8b16c4b7b4 | -6.05836 | -44.84669 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cbe607f3-647e-340f-8de3-143181627442 | -5.31908 | -43.53273 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c53cde24-ce48-3c99-aae7-ba1aa98f9259 | -4.61533 | -43.15033 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| f8518c44-2d17-39b2-8e17-58d4088c57ce | -5.66393 | -42.70761 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93ab3728-a4f3-3e5f-9184-a11082ebedaa | -4.55082 | -50.47488 | 2025-10-04 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9f63745-6087-3014-909a-b20c4d517e05 | -5.79724 | -42.89482 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4d0deb83-a5a4-30cf-99ac-9d26993ff81e | -5.32161 | -43.77414 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cc2e27a-e696-31b9-a715-6a37f1a045aa | -6.54926 | -43.87201 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b9b3b26-0882-315a-8d1c-6c17eb2c5b11 | -5.84555 | -42.80341 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3455dec2-cff6-34f2-92d1-53840f35ec87 | -1.88419 | -48.39798 | 2025-10-04 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9dcb8e7-33cc-3158-8663-a8c4fa742102 | -5.4649 | -43.1711 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0773ecf8-6baf-358f-bec8-64c805bb4c45 | -4.16528 | -42.17101 | 2025-10-04 04:12:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fce4bc73-a3fe-37f4-9448-80ccc120374a | -5.93093 | -42.88736 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9c713371-a535-3002-9079-6c4b365a6217 | -6.05437 | -41.22987 | 2025-10-04 04:12:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 074f90b3-7ddf-3edd-80f0-4760b8cc563d | -5.47941 | -44.105 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 273f1e51-158e-3306-8d79-43b8c1003680 | -7.48109 | -46.04799 | 2025-10-04 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59858f95-8957-37b1-a13b-711cdff45e9c | -7.54539 | -42.4012 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8e009def-7c76-3a4d-ae16-ef7647ca1928 | -5.66062 | -42.70709 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0b9a0f23-dd7b-3836-ba0c-6e9255af15d4 | -7.05054 | -42.78803 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f7261b02-cb9f-30a9-93b3-91c91e2d7fd9 | -7.37165 | -39.19601 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6a8d12b5-6800-30cc-82c6-0d2e0980c227 | -4.44481 | -43.24054 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed253b79-6817-3cd2-8cf7-817f28fe1f95 | -5.31827 | -43.77361 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0d44286-aefa-3122-81e9-baf02c8273a1 | -5.19396 | -45.07164 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| eac260f7-4fe1-3646-b5c9-e4884f4a54a9 | -5.83467 | -42.87242 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e108a778-f5d2-3a13-8913-3fc91fe5a2a2 | -6.30859 | -44.27275 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 921e289b-f7a0-3daa-9263-67aaa34a8fcd | -6.29643 | -42.44211 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5ac667e6-7dfb-3422-b982-8ba4e5903f55 | -5.77417 | -42.93363 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 41b10f19-98c6-3310-bb3b-7d449e4db0bc | -2.68795 | -48.38831 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a51b1361-bfa1-3453-8b22-92badc7f4709 | -6.52594 | -43.37873 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1ab5069f-e85d-3dea-982b-4e9688532600 | -6.64636 | -42.80947 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c231e2af-33b4-3fc8-bce8-ff82588442e3 | -7.05656 | -45.78398 | 2025-10-04 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4acf79ba-30ef-3359-9563-9728639a78aa | -5.97965 | -44.09616 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a66d2e2-a642-33a5-a6a2-cdc686aae479 | -5.84664 | -42.79651 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8d536e0f-7b76-3737-9752-a92a45c6cfb1 | -6.66403 | -42.82643 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 787607ef-9c25-37d4-b9bf-9bb0e05e12e0 | -6.06804 | -42.51244 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fd8d3d17-7b7f-3c04-b6a1-00b6b5e50a43 | -5.72559 | -42.68192 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b98fe54c-cde5-3c24-991a-4556a1aaf16a | -4.05336 | -49.31562 | 2025-10-04 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be40ca80-d481-32b3-a694-87b57c9e7605 | -6.3382 | -43.89566 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20c7c6d4-f661-34d3-9f07-deef039bea0b | -6.01627 | -43.78706 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e92f8b6-a162-3056-ad80-44685071fee3 | -6.66671 | -42.78785 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7e269fa1-0409-37ed-9475-11ab731a2b67 | -6.85802 | -44.08693 | 2025-10-04 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d01f14a-0f71-3af0-8c09-91fd28def746 | -4.60648 | -43.14183 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb88965d-0f68-3590-a8a3-513a9bf6a81d | -5.2648 | -39.26139 | 2025-10-04 04:12:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea64c4ee-98cb-3d89-b6d6-d260c6299294 | -5.66774 | -46.55859 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f27ee2f-9f5f-34ff-bd41-461bd4e8cfab | -7.45912 | -47.18148 | 2025-10-04 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4678cc8c-06c7-378d-ab7e-64535cb72141 | -7.69895 | -42.57275 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 54ed4ea5-d8d6-3ae4-b186-c664efca5b23 | -5.69758 | -49.30729 | 2025-10-04 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f32e8aa2-3425-3a0f-ac10-c333b6f2a4f3 | -6.43639 | -44.45509 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a62cb36-fc5d-323b-b1f5-b73cd53cfde1 | -7.4363 | -46.46595 | 2025-10-04 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a91bb4a-afeb-382a-8f0c-affc26c06042 | -7.04475 | -44.34235 | 2025-10-04 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 699c4fa8-2bc2-3ba4-b41b-1052ae784a61 | -6.7147 | -42.80603 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 279e712f-9d75-3fb6-abfa-5638a92b9df6 | -6.23292 | -45.34678 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 285db192-1eeb-3fb7-a7fa-670a245e197c | -6.38518 | -43.60189 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eda87a70-4d0c-3a73-992e-ccd47ddb7cb1 | -2.67848 | -48.39117 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65dc17e8-3ea9-3d83-bf8f-6f9c3ca36a80 | -7.15989 | -44.99689 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b114ee2-fb13-3062-8498-7431c1c2198f | -6.55639 | -43.09991 | 2025-10-04 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05e002da-6347-373e-abc4-df8c0e8bacb5 | -7.36997 | -39.20742 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 539f748e-ff53-37fe-93ca-4112658d6cbc | -5.07113 | -42.63152 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aedfd64f-89f9-34d2-82d8-e59babce3cb3 | -3.39702 | -50.2749 | 2025-10-04 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d378ea8-ca77-3bc7-bf13-14cc4bfb9b15 | -7.00117 | -44.19346 | 2025-10-04 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2cd4099-7213-3eea-8981-23b85d11e10f | -5.89157 | -42.53441 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b021d19-4512-3576-a107-9b3efaca61b0 | -4.60815 | -43.15276 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0c397d3-007a-3b26-b918-f3f5ea96d6da | -2.89491 | -50.73694 | 2025-10-04 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 817e0332-649d-35db-bb10-afc1038b4e06 | -6.16499 | -43.14766 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 912015df-bf75-38e7-a1e3-7dfd0228f4fd | -6.2435 | -44.23624 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca038613-59f8-3a67-8e18-e5efc72e94c6 | -4.43097 | -43.24193 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7a1df03-ec4a-3e51-8ea3-3fd872406609 | -5.77496 | -45.75613 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 557ef846-0fee-3b2e-87a8-36e57e8d2c5a | -3.659 | -50.26997 | 2025-10-04 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abffa1aa-2dc6-3f31-a55c-baa5065e840e | -7.69786 | -42.57974 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74b22c8a-dd6a-3c53-8fbe-f6c54a9f8b39 | -6.3465 | -43.46009 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 262cafce-6054-3c60-a1e1-954d804a4b24 | -5.3129 | -43.10067 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cb7dd3a-c5ab-37c6-bc0c-065ec658d8ef | -6.87882 | -47.23861 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 24114daf-16b7-3133-ad26-ccfa9cbc6d26 | -5.71313 | -44.24086 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d4f3a67-0cf6-3ba2-b8aa-0bc3bff5625a | -7.75684 | -42.61401 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5a619555-da47-373c-b3c8-261c5721a40c | -5.73779 | -42.9279 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e9095567-5564-37de-8086-d7d9177816a5 | -7.04715 | -42.76616 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 62b06313-e768-3245-899b-49220ac9a208 | -5.94985 | -43.30471 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 69a5be33-eb1c-392c-9363-a17a0a03a7e5 | -6.0968 | -43.4492 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2911d415-5c94-361f-80c7-c0bb8c9956a9 | -6.39346 | -43.61396 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce8c8bc0-7f89-3a31-a8e4-c774a325b055 | -7.77028 | -44.14285 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac3cb02c-bf4e-3e61-8b5d-3a1dd9d1960a | -5.88416 | -44.27172 | 2025-10-04 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README54.md)
