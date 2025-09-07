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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 039fff63-85fa-3184-b075-164e645036ad | -8.96918 | -62.96562 | 2025-09-07 06:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 103a3fd9-b5b6-3d1d-b97d-8c44b1b08969 | -10.42331 | -60.75237 | 2025-09-07 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0a526f6-9796-3b63-99e6-7fd22d6cd421 | -10.16764 | -61.14408 | 2025-09-07 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2cb9e84d-d4ee-3609-a7f2-d1ce9f8125b4 | -12.35903 | -63.63939 | 2025-09-07 06:01:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58bf5809-e65b-3b06-b8d2-e7ea188f0742 | -9.10701 | -60.97419 | 2025-09-07 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d15a9bc8-4053-3ece-a9b2-efa9df0cb840 | -14.42414 | -60.19705 | 2025-09-07 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cca1bc1-7964-36f7-bd60-0c1a15f9fa4c | -11.78167 | -60.89297 | 2025-09-07 06:01:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00d01f02-7d5c-3e94-94b5-93867dadb48e | -12.35833 | -63.64479 | 2025-09-07 06:01:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab058b69-781d-35e0-8336-8a7bbaee902b | -9.10709 | -60.97845 | 2025-09-07 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3d84b58-3c17-3c0a-adb1-cc8c74b60261 | -14.4192 | -60.19874 | 2025-09-07 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ef3d808-0098-30a8-803b-2e5947364cf5 | -12.41254 | -63.90112 | 2025-09-07 06:01:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 997c7469-599c-30e2-9d73-e86bb33664be | -12.4173 | -63.90175 | 2025-09-07 06:01:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be047c2b-1c0c-3e67-a704-973e2c5fc7cd | -11.78076 | -60.89343 | 2025-09-07 06:01:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6de0fe8-55e7-38f1-9b05-8f94ef084f3d | -12.35419 | -63.63876 | 2025-09-07 06:01:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ed377f6-0e33-3a39-b8a7-05b9d6eebb3f | -9.10607 | -60.98158 | 2025-09-07 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb050c92-984d-318c-bcd0-ff2e8a391e9d | -10.163 | -61.14404 | 2025-09-07 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51376e59-ad53-374f-b21e-d59151da13f9 | -12.41797 | -63.89656 | 2025-09-07 06:01:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 160d561f-5aba-3ba9-b4d7-f4533826f09d | -10.28031 | -63.44101 | 2025-09-07 06:01:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 318e5b1b-61f9-3f31-a0f3-5e60d535692e | -14.41789 | -60.19651 | 2025-09-07 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46245dd8-dfcb-3525-8eed-4229632075e4 | -14.41841 | -60.19161 | 2025-09-07 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce44510e-cd20-348e-a0c1-32132e118039 | -9.10654 | -60.97788 | 2025-09-07 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 446d1d1d-f4d5-30a7-a932-0f51c79ee457 | -12.9477 | -54.793 | 2025-09-07 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 74672819-3788-3964-b50a-727c5e96825b | -12.9289 | -54.7744 | 2025-09-07 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| a7d32f6a-688f-390c-8537-abef25bffa7b | -12.7153 | -56.5632 | 2025-09-07 06:10:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a3bb6f3d-757f-3f10-a4e4-c6c9b85852eb | -12.9482 | -54.7519 | 2025-09-07 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 9b515d4c-0418-3cac-8309-555a35036682 | -12.948 | -54.7724 | 2025-09-07 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 748470ae-764e-3010-9d92-33d2eddb772a | -12.8055 | -48.0182 | 2025-09-07 06:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 9fa44b01-1f84-3459-ae25-bee273436ec8 | -6.19877 | -53.26456 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 08ee3d51-3247-388e-b803-74c7dc266844 | -8.19251 | -50.12695 | 2025-09-07 06:10:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cc478932-a80e-340e-9be5-0d52fb505934 | -2.42938 | -49.30691 | 2025-09-07 06:10:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d7b419c9-eca7-343e-933b-6403ea976726 | -8.0637 | -52.38118 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c84e74e6-ece5-34e0-85e7-d423a59e50ad | -8.61846 | -54.64481 | 2025-09-07 06:10:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 98b899d6-c5a5-3993-a868-8b0a3d1079b3 | -3.59505 | -47.50826 | 2025-09-07 06:10:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 87e854bc-8141-364d-beb8-75cd8242c2a9 | -2.81648 | -49.19135 | 2025-09-07 06:10:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca0a6b46-3943-345b-b9e6-9272d1896446 | -6.77723 | -52.80161 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c3a5dd04-2af4-37ec-8b3d-8fb86ae5268a | -8.15119 | -44.8873 | 2025-09-07 06:10:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| a9213f8b-8f16-37e8-a183-26e90049f312 | -4.2689 | -48.18191 | 2025-09-07 06:10:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5baea9ad-fe50-3a68-9e6d-1d6145845f74 | -7.74979 | -50.74798 | 2025-09-07 06:10:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ddabc8eb-e61f-3191-9cb3-c902aebe09fc | -6.53526 | -44.81018 | 2025-09-07 06:10:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| fd62a5f0-e83a-324f-ab72-8033ab42f153 | -3.59354 | -47.51833 | 2025-09-07 06:10:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ee16f05b-c7c0-30a5-8618-7ef3668b42ac | -8.3527 | -52.55083 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 299b0563-c00a-35eb-a090-91b20acdeae2 | -6.29966 | -51.40821 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 36fac77a-e730-3a46-ab76-c3a0b2ceb85b | -6.18085 | -42.62733 | 2025-09-07 06:10:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| a22d8ff7-4a73-3cba-b50a-4f94d6351fa6 | -6.19656 | -43.58052 | 2025-09-07 06:10:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 8adbe93f-b4d2-36f9-9279-0f341feee236 | -6.19471 | -43.36584 | 2025-09-07 06:10:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 02b776df-2170-3b14-91a3-b108b01b9ab0 | -7.67095 | -47.333 | 2025-09-07 06:10:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e01bf4a1-fbf2-3d21-aa15-be8e3c057b72 | -5.9861 | -44.14004 | 2025-09-07 06:10:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| a0796273-2567-34bc-825c-4dac47231e7d | -7.05688 | -50.85609 | 2025-09-07 06:10:00 | AQUA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 316e09b3-faaf-3ee0-b407-4de968e4c882 | -6.19251 | -43.58739 | 2025-09-07 06:10:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d09ee238-3641-3b6b-946e-4567b4de1315 | -3.58415 | -47.51699 | 2025-09-07 06:10:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ed1c8d43-8738-3f98-8480-98da6c3fdc1d | -6.26024 | -43.48651 | 2025-09-07 06:10:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| e64c0a0b-a99a-3b36-84bb-0751280e7a1b | -7.67263 | -47.32133 | 2025-09-07 06:10:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c9f279b2-ff40-3093-a290-ff475c55a109 | -4.25237 | -48.54349 | 2025-09-07 06:10:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e443b0b-90c5-33ad-b12e-a28dbdb7392f | -6.17748 | -42.65219 | 2025-09-07 06:10:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 560ccef2-a8a0-32b3-bd10-db13dae394a0 | -5.86573 | -51.94933 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 16766be3-05d7-304f-ab22-1271ff6ec00c | -5.8937 | -51.94115 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f3911ebf-655b-3567-adae-de8984823297 | -7.68426 | -50.31182 | 2025-09-07 06:10:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cd56cbcc-8075-3a0b-a747-5b57fd68b00c | -7.60602 | -44.66516 | 2025-09-07 06:10:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8fb9abbc-3124-37a3-bdae-0eb5d3463ee9 | -7.75856 | -50.74929 | 2025-09-07 06:10:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5e37b032-92b2-34a2-a185-f7ed68070a08 | -8.37527 | -52.52536 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3fb176f0-49b1-3e3d-b128-45c15a998cf9 | -2.42191 | -49.2969 | 2025-09-07 06:10:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 366a65e1-cbc7-39e5-8daa-8e21825207f3 | -7.67679 | -50.3017 | 2025-09-07 06:10:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 27266447-8f74-31ee-a189-9b3cb5e10864 | -7.73304 | -50.30676 | 2025-09-07 06:10:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4cf11b9c-58bc-35b3-b0c2-70e6e6e7d001 | -8.34356 | -52.54966 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c566973c-6a77-3e78-a017-64b41dbd9d15 | -8.18235 | -50.13457 | 2025-09-07 06:10:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 86965eee-f2c8-3e96-a439-4c693be6b998 | -8.37382 | -52.53481 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8242c8d1-f0a3-3abe-8783-827a27e0fd7c | -8.68255 | -45.29916 | 2025-09-07 06:10:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 6ebb71b9-cc42-3131-b031-ea4c56ca8933 | -5.99874 | -44.14122 | 2025-09-07 06:10:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1e4e06b2-6d29-38f4-a63b-902e6f45611e | -5.5756 | -49.08966 | 2025-09-07 06:10:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 94bbf908-f49a-35df-9e49-e652a025d976 | -6.81634 | -52.79711 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b2f7ad37-2f46-384f-ac0d-dedda1130c80 | -7.66933 | -50.29147 | 2025-09-07 06:10:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1e0cd00a-10ff-3793-84b1-a75aa4ebf78a | -6.5328 | -44.82775 | 2025-09-07 06:10:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 042baada-f3fc-35b4-976c-aae8eb842200 | -6.88409 | -45.59433 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 48aa52f1-77ce-3310-b13a-5f958b1cceff | -6.20056 | -43.35889 | 2025-09-07 06:10:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| edbeaa82-9bf9-377a-9fdb-5bf91e8e94ae | -3.58566 | -47.50692 | 2025-09-07 06:10:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8c51945f-1be8-3193-9d51-9f6e37003b53 | -5.98354 | -44.15834 | 2025-09-07 06:10:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 00e02145-3048-398e-9bde-1af048618936 | -2.81517 | -49.20013 | 2025-09-07 06:10:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ee8d9ee-1b1e-35c1-83bd-61a39c875db2 | -6.81476 | -52.80725 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a7d60809-790d-383a-ba11-acc05d34369a | -9.09106 | -46.98477 | 2025-09-07 06:10:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| db86e1d0-04e0-379e-867e-e9d5b077010a | -6.19508 | -42.62952 | 2025-09-07 06:10:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 2ed467eb-29dc-3a5e-82bf-04754df7d46f | -6.27472 | -53.43002 | 2025-09-07 06:10:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8e208720-e38c-3dba-90fc-66cf911e6d54 | -7.73171 | -50.31563 | 2025-09-07 06:10:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 93e53f1b-868a-30a8-830e-d9e342137c8e | -7.67463 | -50.25603 | 2025-09-07 06:10:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 79bc14b4-6fc1-356b-9e92-a440b03af27e | -8.13893 | -44.88567 | 2025-09-07 06:10:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8ab62784-bbcf-340c-877a-ef83353b8b65 | -6.27007 | -43.4925 | 2025-09-07 06:10:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 4e5abf8e-ee7f-34f0-b547-be59dcc3418d | -6.83819 | -52.84211 | 2025-09-07 06:10:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 32a6759a-a075-379e-b53b-077345801e30 | -8.68746 | -45.30675 | 2025-09-07 06:10:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3c0e0e1d-9789-37a4-aedd-3e441ce4048e | -14.84655 | -46.68961 | 2025-09-07 06:12:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 10aa65aa-ebe8-3b27-91a4-60b02fd7df81 | -15.72623 | -53.54481 | 2025-09-07 06:12:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3f4743f1-98de-36e0-a19d-108230fb0919 | -16.93405 | -45.7537 | 2025-09-07 06:12:00 | AQUA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| eeec62f9-ed7a-3865-9b2e-252afdf896e4 | -11.09177 | -52.05169 | 2025-09-07 06:12:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5e45aa77-b88a-3c30-9db0-02f03456d345 | -10.06971 | -49.29467 | 2025-09-07 06:12:00 | AQUA_M-M | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b02237ef-e234-300a-a81b-9c761d4695fd | -12.9236 | -54.7742 | 2025-09-07 06:12:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 39993c48-4caf-3ae2-bc5c-1db3a674d0d0 | -12.81372 | -52.93872 | 2025-09-07 06:12:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b9124113-efff-36c9-978c-19225132badb | -12.77514 | -52.95159 | 2025-09-07 06:12:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b1f53f49-87d3-3a76-9ccf-7f419c9ec25a | -13.70956 | -46.87526 | 2025-09-07 06:12:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 95d66ce6-38b9-3f3c-8de1-c7c42c0146ab | -12.94748 | -54.77236 | 2025-09-07 06:12:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 9c1e6498-b0f1-3561-a7aa-685b3fa13cb0 | -12.80099 | -48.01507 | 2025-09-07 06:12:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| f663acf0-36ac-3565-b853-20e89d2ccff6 | -12.71591 | -56.55868 | 2025-09-07 06:12:00 | AQUA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| c4ba5dd4-720a-3801-b92f-99bb0757a452 | -17.39657 | -49.30305 | 2025-09-07 06:12:00 | AQUA_M-M | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |


[Clique aqui para ver as próximas entradas](README82.md)
