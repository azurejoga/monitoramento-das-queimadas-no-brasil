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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0e92c8c-29f8-35b0-bb8a-239ddbe9c2de | -21.78016 | -52.74136 | 2025-05-15 04:29:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd3c418d-2e1c-3116-bad8-359403a2d775 | -19.83066 | -51.04121 | 2025-05-15 04:29:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cc1b9b1f-ba8f-3afc-a6c6-900abbf6b5b4 | -20.61889 | -48.954 | 2025-05-15 04:29:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7dff4715-9bfb-3e4e-a165-e24377d6346a | -19.0583 | -52.44725 | 2025-05-15 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d0291b7-4554-3327-aad9-692452f3b236 | -20.20879 | -46.75799 | 2025-05-15 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4987ed24-72f0-3185-bd65-c285be7f64ea | -21.72023 | -55.37122 | 2025-05-15 04:29:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da81e85b-7d41-3a58-a1bc-3d89e73c6dbf | -18.96923 | -50.22592 | 2025-05-15 04:29:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3d64d33-d697-3571-a72e-1db8a510fb27 | -21.78473 | -55.31839 | 2025-05-15 04:29:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53de3a7e-fb39-32ab-a517-cd885ff9f05c | -19.1568 | -47.81729 | 2025-05-15 04:29:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 372677f9-0786-3954-aaa5-9dd43c8f435a | -20.20471 | -46.76157 | 2025-05-15 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a6757342-4ca2-3d32-bdab-8b7929c1d541 | -19.97062 | -44.21785 | 2025-05-15 04:29:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b8e60471-49fb-310a-9219-a4e64d2abd2f | -29.95313 | -51.61368 | 2025-05-15 04:32:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 71a78269-a34c-37bb-8032-b63b6897b565 | -24.36018 | -49.957 | 2025-05-15 04:32:00 | NOAA-21 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e743cf7e-bf39-33dd-b831-24482ce41405 | -24.36076 | -49.95321 | 2025-05-15 04:32:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e36c075-3e50-331b-a356-85ece42ab517 | -26.09747 | -50.17529 | 2025-05-15 04:32:00 | NOAA-21 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 46158c69-152d-376c-9fde-1bb26e90897b | -23.6487 | -54.56681 | 2025-05-15 04:32:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| f6043dde-4f81-3493-95f7-a6e9d41c5395 | -27.38043 | -50.72145 | 2025-05-15 04:32:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b0663654-7b52-337b-8ff2-f3655d6a076d | -30.15145 | -52.02586 | 2025-05-15 04:32:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| b6a46731-06ce-3bcc-ac1e-be5977f16563 | -27.64284 | -51.22575 | 2025-05-15 04:32:00 | NOAA-21 | CELSO RAMOS | SANTA CATARINA | Brasil | 4204152 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| df898dcb-e759-3ca1-bbc0-ac6a4f1e0b4d | -27.11752 | -50.5739 | 2025-05-15 04:32:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 54b4fca9-4569-39ea-9a91-1ef5ac239b3e | -29.27151 | -52.25067 | 2025-05-15 04:32:00 | NOAA-21 | PROGRESSO | RIO GRANDE DO SUL | Brasil | 4315156 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| eb551a76-27c1-3db6-a9ac-7851909fcd83 | -6.04935 | -47.95976 | 2025-05-15 04:51:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbd3203e-2a18-3a50-bece-530ccf40c166 | -8.58473 | -45.89161 | 2025-05-15 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24316801-55d2-319e-a200-de8b7f787dde | -8.59083 | -45.88205 | 2025-05-15 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe8e2421-1322-3abb-a01d-4b782069a594 | -7.95251 | -49.76281 | 2025-05-15 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e942c6d4-0ca5-3604-9409-72ad20968405 | -6.17104 | -48.05733 | 2025-05-15 04:51:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08acb69b-99e4-38d6-85a1-b2dcbbf82bab | -8.59015 | -45.88708 | 2025-05-15 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e0223e5-8020-3c7a-9ec5-089752506029 | -7.07244 | -44.39231 | 2025-05-15 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef65bcd7-8c4a-318c-b1c4-4fb10c1f708a | -8.1615 | -46.49791 | 2025-05-15 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 216df95d-8a40-3ad5-b83f-467dd452fe7a | -5.74223 | -47.98956 | 2025-05-15 04:51:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66b829e4-7080-3d8f-ab09-236766368cff | -7.74526 | -46.33578 | 2025-05-15 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b08ab50-163a-3e0d-981a-6c62267c8279 | -6.64836 | -41.9907 | 2025-05-15 04:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 79dfee99-b734-3a86-a427-e483ed70bb0f | -6.66079 | -43.19405 | 2025-05-15 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 40ea0fc4-8706-3e55-8fba-0b5256894dfb | -6.64894 | -41.98633 | 2025-05-15 04:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0986dd18-40d5-315e-a7fe-7525b723bcf4 | -8.58541 | -45.88657 | 2025-05-15 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e08b622-4b0a-3ff4-ae6f-4500a4b9587c | -8.59152 | -45.87703 | 2025-05-15 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dad999b1-6ccd-32fa-b7f2-dc3142651655 | -7.74643 | -46.3343 | 2025-05-15 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baeee6d1-8ca8-33d2-b3e5-c3a2fa09e79a | -6.64778 | -41.99507 | 2025-05-15 04:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| f500fd1e-7a5a-30a4-8f51-e7b201f8d58f | -6.65289 | -41.9851 | 2025-05-15 04:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ac6554a2-29c0-3966-8351-5fd7fec248a7 | -6.65434 | -41.99141 | 2025-05-15 04:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| a32bd148-1ec3-3885-bfad-7b6dfee342dc | -6.65493 | -41.98695 | 2025-05-15 04:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| aa73fa92-721a-32a3-8bc9-24df8dea61c6 | -5.78632 | -43.61671 | 2025-05-15 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ad382ef-62b0-3325-b384-f2c7f30431b5 | -8.16025 | -46.49598 | 2025-05-15 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e47d40c5-d4b3-3c21-a234-21c2996832c0 | -7.73622 | -46.3346 | 2025-05-15 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7503837f-1124-30d5-8e74-6bda48e5a490 | -7.94887 | -49.76223 | 2025-05-15 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fe61fbb7-2b5a-3d40-8514-0378cfa5cb6c | -7.07499 | -44.3948 | 2025-05-15 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c888e7d2-7357-399b-8835-0edcb6916b49 | -7.07028 | -44.39116 | 2025-05-15 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04da20b9-f765-3a00-b346-764f4ae10b4c | -6.55276 | -44.49499 | 2025-05-15 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae292d5c-0340-3f88-be67-8750a2baef3a | -5.39585 | -46.95962 | 2025-05-15 04:51:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2faaf793-76e9-3093-82c2-40b100c85eb2 | -6.66028 | -43.19765 | 2025-05-15 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a0432d4e-e3f3-3dda-8008-e8a965a0e126 | -7.07068 | -44.38823 | 2025-05-15 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 420ec494-03e4-3363-922a-0743417afbe4 | -5.40003 | -46.96021 | 2025-05-15 04:51:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de2bce1c-8847-39e4-b151-51f8655c16d2 | -7.80003 | -45.33836 | 2025-05-15 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3320e902-4b02-3aba-ab09-d86604bfaa16 | -5.78585 | -43.61996 | 2025-05-15 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 992333a5-78bf-3b81-a3c8-038eee953aa9 | -8.57998 | -45.8912 | 2025-05-15 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50db5056-0888-3f73-bf7e-18dfe51ab61a | -6.65228 | -41.98947 | 2025-05-15 04:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 6a1cbe18-94d1-310e-a994-6dac84267a07 | -7.74074 | -46.3352 | 2025-05-15 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04aedb71-fc94-333c-b3d4-611e37c2da26 | -6.16068 | -48.53153 | 2025-05-15 04:51:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c494174f-5ddd-390f-8be7-281ebd7585f9 | -7.75098 | -46.33466 | 2025-05-15 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e5decd1-ee5b-337b-9fab-f6b76d100e28 | -7.74981 | -46.33618 | 2025-05-15 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69efb1af-f118-34bd-a78b-3e8410577a01 | -6.17029 | -48.06236 | 2025-05-15 04:51:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0099c940-b443-39a3-b0a5-362e20bf92e0 | -5.78056 | -43.61922 | 2025-05-15 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59e14ce2-afdc-3edd-b511-390715fb9052 | -6.15686 | -48.53091 | 2025-05-15 04:51:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e52afab-b71a-3ca0-abd8-f0eaeecf97d2 | -7.0754 | -44.39183 | 2025-05-15 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aeeea295-7847-37da-bf7d-be7b40f1b3ce | -6.65166 | -41.99386 | 2025-05-15 04:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| d720ac39-3d32-3abe-941b-eccb9a3c9dd1 | -7.07286 | -44.38937 | 2025-05-15 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba9888d3-8f33-315a-bd0b-998bc5c1ad9a | -5.78453 | -43.61803 | 2025-05-15 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24f29327-a98e-363a-9174-461bd98687d3 | -5.7383 | -47.98901 | 2025-05-15 04:51:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db679c6b-a1f0-3aac-b07f-2d97e7ff1084 | -6.64569 | -41.9931 | 2025-05-15 04:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4de23f28-1d66-3aad-b6b2-937dc5c02a41 | -10.34219 | -47.67885 | 2025-05-15 04:53:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4327cb1a-8c73-336f-92af-a7e777b9cf93 | -10.65631 | -44.48891 | 2025-05-15 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a260126a-a368-3c91-8cc0-96a64018b3a4 | -10.35129 | -47.97642 | 2025-05-15 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1559d47e-979f-30d4-8434-422ee232cb1c | -8.71038 | -50.24575 | 2025-05-15 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ef99493-de64-33e1-b459-54aa6c26841a | -10.37805 | -49.30876 | 2025-05-15 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2b8509d-178c-30f6-af9d-cfac61f61e3f | -9.32246 | -44.83152 | 2025-05-15 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f944050-9a50-303f-930d-57e3439ced9d | -9.65845 | -47.55956 | 2025-05-15 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48ca5d2e-1272-3399-b2ea-57144527e93d | -9.31693 | -44.83384 | 2025-05-15 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac7651d7-6bde-32a5-a180-a55e5ceb0bf5 | -8.71397 | -50.2463 | 2025-05-15 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e46c2a5b-a6f8-396f-a44f-01330ef466f2 | -10.45135 | -49.07544 | 2025-05-15 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f30e708a-3524-33ea-b734-01e54c4c2831 | -8.89172 | -44.78603 | 2025-05-15 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fbabdb2-33f3-3c4a-8611-9738aa331bcf | -10.63584 | -48.09304 | 2025-05-15 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ea4a820-f159-35c7-9484-297f6412eb48 | -10.47007 | -49.14022 | 2025-05-15 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7388e69-24eb-32fc-8afe-b1fa42cc7406 | -8.71336 | -50.2504 | 2025-05-15 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3fc6ee2-8677-375a-afbc-d38e6dad31ce | -9.93976 | -50.85629 | 2025-05-15 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e01bb98-377a-3bcb-8e44-594c773d4295 | -10.33454 | -47.97379 | 2025-05-15 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 723aabdb-ae46-3113-8110-440d463e150c | -10.47329 | -49.14381 | 2025-05-15 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0c35e757-7ecf-3ac0-be4c-95b63bdccb46 | -10.47396 | -49.14082 | 2025-05-15 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f84f7a0-f4d8-3f94-bf71-58efbabe9527 | -10.48175 | -49.14207 | 2025-05-15 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6842232a-6ed0-3657-af4f-b670d1986cf4 | -8.89213 | -44.78308 | 2025-05-15 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11f9ea4e-f031-3e21-9281-09df0748f8c4 | -8.71957 | -47.97934 | 2025-05-15 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2327a59a-d061-317c-8a72-5bdf6f71f2c4 | -9.65789 | -47.56351 | 2025-05-15 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e849078-8d4d-36fe-aa64-e9890e969cfe | -10.35654 | -47.96947 | 2025-05-15 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4035497f-8a38-3580-882c-e8b036c6ea2d | -10.00504 | -47.84244 | 2025-05-15 04:53:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90a8baa7-d578-3cb5-a4aa-d939e688fe58 | -10.356 | -47.97329 | 2025-05-15 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3aaf7a42-fdd7-3b89-85f5-8df560dc3a78 | -8.79934 | -49.82038 | 2025-05-15 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b602c719-eda8-3179-b53c-703ede7ab520 | -9.31734 | -44.83082 | 2025-05-15 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4c734bb-89d8-364c-a388-9deb8ef729db | -10.47327 | -49.14574 | 2025-05-15 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e45d76f-1800-3416-b965-bea1c4166c2d | -8.72009 | -47.97567 | 2025-05-15 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6d8a30c-b2dc-3694-90e1-4697bb17f2d5 | -10.00471 | -47.84351 | 2025-05-15 04:53:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a24fc744-fd3e-3c66-a71d-10324ad002ff | -8.33766 | -55.09459 | 2025-05-15 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |


[Clique aqui para ver as próximas entradas](README9.md)
