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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff527a6e-bc95-3bb5-be03-1b88d968ed9f | -9.87202 | -60.30414 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3232f61b-bdb6-35ca-9169-e581ec95d384 | -8.89769 | -71.3969 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 871b3a93-e157-3dcb-836e-b06e4b5bf76e | -9.25826 | -57.07639 | 2026-08-29 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ca2a026-154e-3b21-ae30-982230b3fd9f | -10.50511 | -59.62947 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 906d17ad-3bbb-35ef-8755-813d511cd70b | -10.50614 | -59.62215 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ba3fbfb-8769-35e1-8220-6603ae4661eb | -9.30848 | -56.80281 | 2026-08-29 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2b7b454-8b2b-36bb-917f-2f5363fd2d23 | -6.5875 | -68.87708 | 2026-08-29 05:38:00 | NOAA-21 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e899410e-8d3c-3151-a49c-ee09e9d755b9 | -9.88145 | -60.26613 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 071d9758-54bf-3f1f-a57f-93f354f86611 | -10.49216 | -64.49931 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5b0ec2d-c191-3c5e-9a34-5329438c98f1 | -9.93367 | -60.43788 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba4f96c4-6a68-3417-a480-01cf2a04708b | -10.54204 | -65.35381 | 2026-08-29 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f99a368-11aa-3362-bf0e-a7647467d915 | -14.94034 | -56.3304 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc96e335-197a-3c19-81a8-980c555af725 | -10.47615 | -64.49319 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1713df67-b7fc-30d4-af9d-a5aabcaedc37 | -11.02628 | -57.24921 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0bd7e31d-8238-32f8-818a-61b3bb3b91c1 | -9.40175 | -55.97409 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d602ab52-d216-322a-bb79-f6969c93ac9a | -14.89842 | -56.33725 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74edd954-bcd7-3ad7-b7c8-5ff679b808ee | -14.9124 | -56.31091 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c495b9af-7013-351e-9e30-a359d47cc927 | -10.48885 | -64.49879 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 826c911c-dfe6-3b0d-932d-d54c15ff28c3 | -9.96488 | -53.93454 | 2026-08-29 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b9fee75b-90ee-305d-aa62-2f972de5cbf0 | -11.26785 | -54.03321 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5100f755-8980-3f2b-8dff-57a90f8882fc | -11.27229 | -54.047 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d69c95b-c484-31fe-8547-c3120d5ec945 | -8.53287 | -55.26746 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d930f431-f336-3d90-9511-d705c501bda0 | -9.205 | -67.77837 | 2026-08-29 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a37d8d06-4dca-334e-9f69-b8746242621e | -9.87098 | -65.03694 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12b50791-2525-3ea0-af58-bd5cd8200cfc | -14.90665 | -52.63078 | 2026-08-29 05:38:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e946633-4838-3ded-b839-cd59abc8e9a6 | -10.39073 | -61.23341 | 2026-08-29 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0030a751-3885-3665-9502-d60442a50f6f | -8.60486 | -54.77457 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15c15b7d-354b-33e9-b6d1-da38ede89d62 | -8.04613 | -69.962 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52e23164-ca47-3150-a262-f1fc7b0b28de | -10.39008 | -61.23783 | 2026-08-29 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63f1832e-5d8a-3ead-81b0-aec5c97342ee | -14.92033 | -56.33652 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b273fbbd-27a5-3533-9e0a-a8d9d0a44cbc | -8.82444 | -70.63561 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b71fd21f-6ece-38b0-a9cb-9353fd23ace3 | -11.03933 | -57.22418 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0a52c7e-6509-3f0d-ba9e-c56bdddc6272 | -8.9878 | -65.43892 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f28dccf-ffd6-38ad-a206-c75b60c06cfa | -11.1932 | -55.09516 | 2026-08-29 05:38:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a4ba547-a61c-335f-a784-032d12b20ffe | -8.95459 | -62.38943 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a9ca5e8-94ee-32c5-9728-c2cfd9a43643 | -9.86822 | -65.03292 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd5cf96f-1e3c-3e8f-b8df-a3639e8ecaf2 | -9.34052 | -68.88757 | 2026-08-29 05:38:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 087d7b3a-3f91-3894-9242-470e1ddbf4d2 | -10.55628 | -59.6215 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4f443bc-3062-35ec-909b-90f7d2d7c7e9 | -9.92287 | -60.43152 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31a9511d-2b14-3db3-982c-787462665589 | -9.97077 | -53.93535 | 2026-08-29 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4a76cf75-783a-31ec-bf2f-32b6fd8328dd | -14.46553 | -58.52369 | 2026-08-29 05:38:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c53dcfa-5f2e-33a8-bae2-681515519349 | -9.86546 | -65.02891 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b568771-558a-3e0a-b65e-f51bedf9749b | -10.28758 | -62.82212 | 2026-08-29 05:38:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3ce15a1-5ba9-312b-bc5e-78e0c051cb3a | -8.95522 | -62.4088 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 513be2f9-fce3-3573-b1e9-4062ee093f44 | -11.02974 | -57.22272 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 410541d3-9fe4-3c31-9cd9-6616d89438e2 | -14.41429 | -52.57663 | 2026-08-29 05:38:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53ad18b9-5da7-3b8e-b15f-3123c8d2fcdd | -11.02836 | -57.23329 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73e549bc-0764-3842-972c-9e477a7d9720 | -11.26635 | -54.04611 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d8256a3-ee33-3fdb-82f0-ad62a21999a1 | -11.22571 | -54.00429 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6ea38f2-9f0b-31b6-8cca-d7dc7b2b4b35 | -11.23329 | -53.99163 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2999fe27-e2a9-346a-980b-e051dfe5e51a | -8.99726 | -65.44407 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 377968e4-8d1f-3d8a-a187-6208c67ec146 | -11.03177 | -57.24452 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db1f5a97-a112-3ad3-8c88-2cf0d7d9bfbc | -8.2482 | -70.09989 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 694750fb-1e90-3081-b04e-539a6726893e | -11.71062 | -54.53626 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 801e88fb-389e-3795-b185-6d4fa2a36c53 | -12.06882 | -64.72231 | 2026-08-29 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bcb48a9-07f9-3d11-a51a-cb627777ef06 | -9.06616 | -65.41512 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93b83056-6444-3cb4-956b-0a90c8d69ae4 | -8.0458 | -69.96152 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db9dad72-7549-3206-a48d-32203a9a379f | -8.59035 | -54.75787 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d82617b-4785-3dd8-afa4-91613d1dd61e | -8.53691 | -55.27057 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 608ea003-fde5-31ee-9465-a7ce35161764 | -14.20355 | -52.84744 | 2026-08-29 05:38:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8379c3ca-5c09-3b3f-b605-4b3f35be13cb | -9.17713 | -70.89591 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10ce9438-11ac-311a-9fd5-a3e05be7c2a1 | -9.38385 | -66.52269 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cca7959-d4ab-33e0-bd73-4e38677d269f | -10.4723 | -64.49616 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| bb9bef70-dd89-3175-8eab-728ae17bd309 | -15.12286 | -53.5808 | 2026-08-29 05:38:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 311d70a0-0220-3776-8510-a4cc8b41dd7b | -8.33445 | -70.71954 | 2026-08-29 05:38:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fc60e55-863a-3513-be8b-6aabf441ead5 | -8.53816 | -55.26826 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27243a59-f7ba-3e60-b60d-6c4f9ee1a8c1 | -10.50562 | -59.62582 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00eca348-264e-36a0-a83a-4f9e8c8f24dc | -11.24213 | -53.99364 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 336a7386-cf16-3f10-80c2-41da54e6441a | -8.59939 | -54.77959 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a39a911-8395-3dec-ac3a-65a690d63253 | -9.09053 | -65.47719 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44e6c3c8-6be5-34a4-b8f6-6775898e3c51 | -8.59054 | -54.79817 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79019c63-6f59-3c61-a437-dd7133b28724 | -9.86601 | -65.02541 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1434ebbf-f257-3b7f-8766-a821ee6ba57d | -14.17697 | -52.84469 | 2026-08-29 05:38:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d89dc580-d799-3ed7-9113-5fc3e16930bb | -9.06672 | -65.41158 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3174e54-726f-3ed4-9739-a6777da6eefa | -9.96542 | -53.93018 | 2026-08-29 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 582243a6-2c18-3b3f-9df0-aa4fadd32ed6 | -8.98447 | -65.43839 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 314f7368-c01f-3c54-899d-b789257335ab | -7.58334 | -61.33837 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d2ba1c9-e43b-35ea-9bbc-67fe267c4cd2 | -11.26735 | -54.03751 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5a024ac-c1b6-36ad-bef8-578c9370a5da | -8.15601 | -63.99997 | 2026-08-29 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1b6cb2e-9626-3641-b2f7-b672887c46f5 | -9.09387 | -65.47771 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80434b09-46e1-35ed-aa04-839c453fad7b | -8.65426 | -70.75346 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d97292c-199d-392f-a796-1d742bd71b47 | -10.28831 | -62.81775 | 2026-08-29 05:38:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbde63c3-3bcf-33eb-8ef3-09f2afdcb664 | -9.61062 | -55.12566 | 2026-08-29 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4076787f-d7e5-3c94-b221-41040d295f57 | -12.34055 | -63.73752 | 2026-08-29 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf6eaa5b-1338-3665-96d0-5f6aecbfdc66 | -8.1527 | -63.99945 | 2026-08-29 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5b9e7c6-e508-3939-9378-663cbc71e2ed | -9.86712 | -65.03992 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17f406c7-89d0-3600-9a9e-9cedd41a364d | -9.28139 | -68.78114 | 2026-08-29 05:38:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29e878ea-b746-39e9-8049-5bf4d453a792 | -10.47946 | -64.49371 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c223b6c7-0c82-3b1b-816c-e9bf31f9eba0 | -7.56081 | -61.31991 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d24b67ac-4dea-3f5d-8bdd-3dc58fe5b056 | -8.58986 | -54.76153 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99dc3cbf-3d37-3267-8491-9bda7e6d6132 | -8.95115 | -62.38891 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e2379e5-8e2a-3efa-a5d7-e4197476bc49 | -8.95383 | -63.27623 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b8a4d90a-2539-3cc4-bb69-7a4587304b00 | -9.7143 | -64.53964 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 239c8bc3-1775-3b32-b369-e34561c83363 | -8.95227 | -62.38137 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c39a1da3-356d-3117-8280-984be2f4d0bb | -9.48605 | -66.62743 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99078f6c-a8de-3d5e-84b2-a7a1d548cf5f | -10.56085 | -59.61831 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 020aedb2-dce1-3a03-8008-f822028699c5 | -8.60299 | -70.21192 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dbe850f-713d-3761-9492-48342c7e6697 | -11.03524 | -57.21811 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e10e3659-70d9-3172-962f-167effdd8a9c | -9.22447 | -59.76558 | 2026-08-29 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca5eecae-8500-33b3-8750-b98567f9e096 | -9.04332 | -65.42963 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README66.md)
