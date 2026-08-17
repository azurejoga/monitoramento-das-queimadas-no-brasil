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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22f6f9ec-cb0a-3bfb-850d-f04bbbeaeb4e | -13.4402 | -57.03698 | 2026-08-17 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed872ce8-4bd0-328b-af18-e14100252b36 | -15.2269 | -57.65091 | 2026-08-17 05:18:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc822652-5f40-3930-bf7a-3afffcbea799 | -11.46896 | -46.57822 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fd575f2d-8e13-3aa1-a6a7-1a20f64635c9 | -14.31057 | -53.05014 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94664a40-20ee-3678-9b87-5dda02431bc1 | -13.51116 | -46.22826 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf686719-681b-3d94-9087-7f67c4af5790 | -11.5064 | -46.6044 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a53879b-d215-30db-b785-8c6970602f96 | -14.46633 | -52.07399 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 78f1b7be-700b-3a2e-b5cc-601003cf7fb4 | -16.22324 | -49.70452 | 2026-08-17 05:18:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7100229a-5de0-3ef8-b87b-23aba076f371 | -10.91425 | -62.76841 | 2026-08-17 05:18:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b19acfc5-a463-3c98-a321-fcf66a055e37 | -11.23315 | -54.01279 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 075ba7c7-9bd5-343e-b3cf-bec85534e706 | -13.51118 | -46.29003 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e82a7555-594a-388e-94c4-8d6bd772f1c9 | -11.20582 | -54.81826 | 2026-08-17 05:18:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 533a5d68-55bf-3e14-ab30-7296005e5be6 | -12.6787 | -48.50985 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4479772c-dabe-32c9-aa2d-5f77cb5fcdcd | -10.05428 | -62.46056 | 2026-08-17 05:18:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77f9d4bf-4493-3736-a8fe-48da54eb1d61 | -12.02695 | -46.42822 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 320901b7-cb02-32bc-92fa-830c805bee6a | -12.03957 | -46.49307 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d0342d18-8b31-3364-813e-813392932ffb | -16.29751 | -53.19079 | 2026-08-17 05:18:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2588d4f-1447-367d-9e2f-0e0675d58c98 | -11.78495 | -51.78916 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20d268af-ac18-3624-9f60-4cc7d3fdf9f5 | -15.02769 | -47.0373 | 2026-08-17 05:18:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d42a84b4-23b4-3e96-b9f5-525f0b52fe3a | -12.75823 | -48.43651 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56b82bd4-610e-3fbc-a04c-defa27f47a9f | -12.18259 | -45.14632 | 2026-08-17 05:18:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ce66c8a-f2e9-3ee0-9b7b-d5574f92f6d1 | -11.83284 | -51.7785 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6447bb51-042f-3d1b-822b-f534bd851514 | -15.78412 | -55.57306 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5500dff-4adc-3589-b3b4-171757b17085 | -11.79027 | -51.7823 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a14b5b3-0838-3df2-9e80-9d31f813347f | -15.12616 | -50.05139 | 2026-08-17 05:18:00 | NOAA-20 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e31c81fd-375e-3433-9d78-64c07ceb6a20 | -11.48358 | -46.57571 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88e6c6f9-18a4-3edf-a5c7-242a3678ab4e | -15.13397 | -50.05205 | 2026-08-17 05:18:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21350fbc-2728-31cd-9d8d-204383abd8bc | -11.71189 | -54.60358 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06b4b80a-b3d2-382f-b042-4e22af8febd9 | -14.49235 | -45.67631 | 2026-08-17 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9f5176c-0d3e-3de2-ba48-8063675f4583 | -12.04095 | -46.48491 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d16b89f0-efbd-3d43-9431-f5ceeca7bbf1 | -14.4657 | -52.07906 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8c78155e-3805-3520-b23a-1bbfe888a0e5 | -11.70496 | -54.59768 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b08469ef-22ca-36b6-81d1-f0a92c2cc2d0 | -14.18785 | -53.06493 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7020ba0f-a092-305c-877d-6402d57261db | -14.31493 | -53.05081 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f811323c-7ba8-3649-9b61-e914690250b1 | -11.21743 | -54.01063 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fd03da8-117f-3056-bdf7-deeac7cfa5da | -14.47761 | -45.68169 | 2026-08-17 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1f44c380-8b02-3d7d-8ee9-cc13a599ca66 | -11.81509 | -51.77114 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 503119e1-045b-3093-ade8-cbfba09193cb | -9.36756 | -62.36476 | 2026-08-17 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0e9c012-4f7f-3d13-8a31-aeff81e2dd93 | -9.58504 | -60.5 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76e8b203-d7bf-3c13-b6a0-6a3171ba6ff4 | -11.82889 | -51.77298 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| e65956cd-3e62-3275-9aa6-391c046d0f57 | -15.85418 | -56.33955 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abecbf2e-900a-37d2-be70-a1aeb7824385 | -13.41357 | -57.03355 | 2026-08-17 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe4031d8-288a-3c3f-9e46-905357bb58bd | -11.70739 | -54.60776 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d5e7b31-363e-39e2-ad32-412cb106c406 | -11.79084 | -51.78025 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b017cc6c-5fcf-3e7e-bba8-8e2835e8f377 | -14.08931 | -58.4426 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f372ebb6-5abe-35ee-b339-c7803cf17eb9 | -16.17822 | -55.95134 | 2026-08-17 05:18:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8d4f6245-d540-3648-b844-5db639a7f497 | -14.41547 | -53.07074 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29add0a5-83c7-330b-b98c-d1cf6256229f | -14.50243 | -59.32195 | 2026-08-17 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b0a60a1-82f3-3110-b265-315ebac3a923 | -14.32366 | -53.05198 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e1fec87-66c7-3655-a6f4-b57e9bdc262a | -14.09708 | -58.43649 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 49cdd79b-9f02-39a1-b070-9bb2cceb9c13 | -11.80529 | -51.77462 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66e95dcd-a093-33c9-9d7d-b66668fc1786 | -16.23004 | -49.70906 | 2026-08-17 05:18:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2738c8ae-7bdc-39ee-8ce6-992723b3f6fc | -11.49396 | -46.5875 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0c3fcde-f079-31ad-a186-e818ba552c23 | -12.75927 | -48.42805 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e0f3f2d-09ab-3c03-9e78-211773fa7220 | -13.4741 | -57.06993 | 2026-08-17 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9daa52b-2cf2-36fc-9a06-e0b55d43b9aa | -12.65604 | -48.50264 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3581c782-c59a-3b57-975b-40d5f4f43c0d | -10.91809 | -62.76888 | 2026-08-17 05:18:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 90760aa6-4198-3d43-8e46-75d73cee69f6 | -13.52658 | -46.23691 | 2026-08-17 05:18:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 073f14b9-e36c-312c-b74f-fb8e9c00357a | -14.32487 | -53.04958 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 719ee133-35d2-333a-bd2a-f53d026dd1a8 | -12.74805 | -59.77798 | 2026-08-17 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11d47c99-da74-3046-a058-ffa8c50a1a0f | -11.30178 | -54.8769 | 2026-08-17 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 219e32c2-6b9b-3dbe-bb8c-c10a4873e2e6 | -12.75827 | -48.43576 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4abcf8c6-a50d-3753-9bc1-fb4fdb7c38e6 | -10.05128 | -62.45528 | 2026-08-17 05:18:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f039f99-a474-3317-aba2-8c7422d087db | -14.87703 | -46.64596 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbb6c874-a269-3fc7-aec9-9f8c042a44d3 | -14.20566 | -60.20178 | 2026-08-17 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0c0c09c-0bc6-3e94-a763-515ef1d7163c | -11.4697 | -46.58307 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| efabe28a-f4cd-3e65-8147-4980b7e3e254 | -12.75874 | -48.43171 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a61b9c7a-3a40-3154-a102-2dc6ea5dc5cc | -15.81422 | -55.52466 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8800bd29-ca0a-34c8-899c-160a6623f06c | -11.88174 | -50.22208 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d66e4ec0-aabb-31cb-b1be-eb50282707d1 | -12.70724 | -48.51694 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a2d2568c-9aeb-32c3-96b7-3f1b692953b0 | -15.24082 | -56.47655 | 2026-08-17 05:18:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b6bfbe4-f5aa-3b33-8393-795fed0cf357 | -12.65652 | -48.49857 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75393425-07bd-3d93-a22c-a2d0b2400795 | -10.05451 | -62.45864 | 2026-08-17 05:18:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb2de884-c5d6-37fb-a460-0609d4014cab | -11.5059 | -46.60874 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae779b09-76d9-3f01-afef-9b0307ff25f3 | -11.92735 | -64.1002 | 2026-08-17 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c20e9611-1835-31b7-9b49-887f3b51e8e8 | -12.68847 | -48.5266 | 2026-08-17 05:18:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82826b2b-9d05-358f-ba92-abb9aadfb8ed | -14.02442 | -53.6108 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d42300fa-12d4-3001-b8c5-23343509bd39 | -14.87775 | -46.63882 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2b2d0717-f8a4-368c-8318-804a9e89ed6a | -15.90834 | -55.5398 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 9f3b7ca2-c41e-3db7-ad04-621b32400e81 | -11.44775 | -46.59198 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9b4e3ab-1955-3835-98a9-427190151b6f | -11.70671 | -54.61248 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f72c6a5-beb6-3430-b6fa-6440409e1a3c | -15.92715 | -56.48217 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34ad5875-0126-39f0-8e0e-803b3d910c05 | -12.70196 | -48.51199 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0db791c-db84-37f9-ae43-d19359982597 | -12.69617 | -48.51126 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e08951f9-a849-3730-81fd-6927ec63c582 | -15.8168 | -55.52721 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8c0b9bd-1439-3551-bb91-7f2660cdb2fc | -11.72715 | -54.60576 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96680dea-425b-3a27-af58-ff7068dec098 | -11.22529 | -54.01173 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63357fe8-4e56-38ec-a0e6-4ed36b9c96ff | -11.23244 | -54.01782 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2e378ba-9ad5-33d2-9f76-a41d14198f10 | -9.47642 | -60.54197 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6e19392-a6c6-319f-8e31-4cdf8aee7912 | -16.67228 | -49.45094 | 2026-08-17 05:18:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1b363d2e-2066-3851-9232-9192a2727b7a | -14.18728 | -53.0692 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9e53ffe-1708-3a3e-8f92-d1f592f2413d | -10.94308 | -57.14939 | 2026-08-17 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30d059cf-3025-3941-9c29-6a0f0bf76f6b | -12.32688 | -47.2584 | 2026-08-17 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d09eea84-4b8b-34c3-a5d2-a8be8e606c76 | -10.06367 | -62.45072 | 2026-08-17 05:18:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a2c0ead-db9e-3f6e-888d-48cf9cbc6f31 | -16.29481 | -53.1764 | 2026-08-17 05:18:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84e0953c-d389-36c2-9bc9-0f6267f0ef90 | -11.71501 | -54.6089 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f01c9aeb-dbf9-345d-aff2-7f6f8a74643d | -11.20648 | -54.81367 | 2026-08-17 05:18:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a86ed7e7-2b8c-3731-b924-8f56646f1563 | -11.78952 | -51.78989 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87e59d84-45c2-3e79-b1ad-67ab985fbbdd | -9.58567 | -60.49619 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf296c4e-59b3-3784-ae97-f281822055f0 | -11.46855 | -46.59321 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README57.md)
