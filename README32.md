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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cdfc08f-3675-3743-b9cf-7372dbda1eac | -7.02088 | -49.17998 | 2025-06-27 12:46:00 | TERRA_M-T | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 14.0 |
| eeada1f9-ec8c-386c-a863-cba1842fd691 | -10.45511 | -52.73859 | 2025-06-27 12:46:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 861758a4-6504-3839-9f3d-9b3a0f610c08 | -10.81539 | -55.86418 | 2025-06-27 12:46:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 83f85133-7849-3b78-9b7e-46fee08c1fe5 | -8.67673 | -51.29647 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8056c58d-ac7d-3fa3-9302-ef2b5399f45b | -7.61551 | -50.6503 | 2025-06-27 12:46:00 | TERRA_M-T | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cdae21e0-9732-35b3-a46b-8079c80c7302 | -12.00682 | -47.15811 | 2025-06-27 12:46:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 3bea5d7c-c8d7-3cba-9cb5-b5b8a49feabf | -11.57647 | -52.10833 | 2025-06-27 12:46:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6d1657bc-2203-3df3-817c-35d428a2e24c | -10.30064 | -57.1239 | 2025-06-27 12:46:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 3f750317-0f8b-3cfc-b01e-841a97b667bd | -11.58418 | -52.11895 | 2025-06-27 12:46:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 9c567cff-e66e-3c5c-a843-a2203ac69c09 | -11.57516 | -52.11768 | 2025-06-27 12:46:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 53b7f425-6d99-33e8-86d5-905e0a7ba62d | -8.58166 | -51.58122 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 18c7d25d-9c0e-38e7-a7a0-ed79f2de9640 | -10.6263 | -46.71172 | 2025-06-27 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| c4993a2c-5e41-34e8-9800-6989255c3733 | -6.4986 | -43.66393 | 2025-06-27 12:46:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 4a54d06a-382c-38e6-b34b-1b56fdd2a3e4 | -7.88697 | -49.73124 | 2025-06-27 12:46:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| a1fda257-5052-3dca-a7ae-1b395384708a | -8.37603 | -51.07546 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 778300d4-c724-36bc-aec1-a41b5d551b92 | -6.96651 | -44.02626 | 2025-06-27 12:46:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 495a8fdd-fc7b-3ac7-a3b5-ab556a9971be | -6.76609 | -44.9119 | 2025-06-27 12:46:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 13a06f5b-3c65-3849-83a3-cf0542e9e23c | -8.80737 | -44.58979 | 2025-06-27 12:46:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 7d7c8f07-366c-3885-8310-e0ef15cc8568 | -11.38667 | -56.54921 | 2025-06-27 12:46:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fbc52b8b-bfba-3f52-906e-0226ddbd1003 | -6.21768 | -43.36034 | 2025-06-27 12:46:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 1438e260-f2ee-3de6-bdcc-d38d902bc1cb | -11.55426 | -47.87232 | 2025-06-27 12:46:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| d2978744-63e6-3573-b281-2b374f4f84e3 | -10.85681 | -54.04023 | 2025-06-27 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e699c896-19ce-3345-bafb-86e2a8fbde89 | -6.75788 | -44.92984 | 2025-06-27 12:46:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| b2bc22d1-45be-3a96-bf65-1741a9e5330c | -8.80751 | -44.58427 | 2025-06-27 12:46:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 4002b182-30a7-3e9a-a99d-c0ac273f2c96 | -6.97055 | -42.89095 | 2025-06-27 12:46:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 6f48446d-9dc6-303d-aa27-2eca9161a911 | -6.96488 | -44.03303 | 2025-06-27 12:46:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| dd7e968a-3236-369e-990e-f46d1145045d | -10.85564 | -47.19645 | 2025-06-27 12:46:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3a2cdb8c-ac91-3866-9aef-07da330ad853 | -10.15695 | -53.91245 | 2025-06-27 12:46:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3fa913b3-f8f7-3bb0-adb1-9af292b6c320 | -5.71535 | -43.8416 | 2025-06-27 12:46:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 82287e67-48ec-38cf-aace-9bda7d3f0b1b | -8.49173 | -48.26561 | 2025-06-27 12:46:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b980c313-967f-3403-acab-bfee9ec0d26f | -7.74391 | -47.58879 | 2025-06-27 12:46:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 27617a38-0fe1-3a6b-847e-17b1326e8c65 | -11.21332 | -54.19801 | 2025-06-27 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4157fd37-8f09-3bd4-ab17-c58664b0b466 | -8.57267 | -51.57996 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 01914127-87ee-38ab-bd05-481e8e2d5ed2 | -5.71908 | -43.81334 | 2025-06-27 12:46:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 3fdcb200-5e89-395d-8942-f5c187b12104 | -11.45011 | -48.52298 | 2025-06-27 12:46:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 67a7df8e-e575-3591-8b19-0d87334ec7da | -5.87762 | -43.63955 | 2025-06-27 12:46:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 1a23c86f-28de-3387-8e66-f398cec41c56 | -11.13384 | -53.91462 | 2025-06-27 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 166a54c1-c227-3e72-a894-c5414ca48fdd | -8.14079 | -47.11728 | 2025-06-27 12:46:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 6a8c8509-c327-3876-9a38-21223f068b3c | -9.12044 | -49.44101 | 2025-06-27 12:46:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5343e6c8-a248-3a0a-a448-bf269b38372a | -11.95724 | -47.02589 | 2025-06-27 12:46:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e4526f2e-3892-354c-afea-37dc5bb1ed2e | -10.86325 | -47.21063 | 2025-06-27 12:46:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| f34463cc-3e8f-3c1c-92c4-69e60b333e5d | -11.37893 | -54.57331 | 2025-06-27 12:46:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7fa5b298-a8a0-3bca-a580-b2b5bc79d0ec | -5.91605 | -43.46152 | 2025-06-27 12:46:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| b1340157-19d2-386b-80aa-06d76c700c3b | -10.3796 | -46.80985 | 2025-06-27 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 8af1f06e-0167-3f0b-a9c8-ff96ab109928 | -10.30403 | -57.13103 | 2025-06-27 12:46:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| cc6f55f0-8c01-3d80-a10d-85ccd9ddecbc | -6.50253 | -43.63418 | 2025-06-27 12:46:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ef4d5860-ffe2-32af-9a71-b9be2eed4f94 | -5.71411 | -43.84818 | 2025-06-27 12:46:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| f5e67ea2-0a46-3512-a205-6a36cb1208b7 | -7.55157 | -45.82811 | 2025-06-27 12:46:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 57f34f42-d023-3eaa-9a45-93825bd71d1a | -11.42984 | -54.47678 | 2025-06-27 12:46:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3e5ec92b-addc-388c-b145-7808163b8b12 | -8.61893 | -51.57698 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| ab6644f9-0f39-3235-8632-5623ee1bc439 | -8.80326 | -44.99594 | 2025-06-27 12:46:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| f4eae9de-40b7-390c-aaec-845f729c4f38 | -6.49845 | -43.64061 | 2025-06-27 12:46:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 00533ba5-71ac-3c53-af59-a8cdefe4d64a | -9.10629 | -45.2622 | 2025-06-27 12:46:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 800e6100-0f00-32d2-9317-f190e2659454 | -7.71653 | -50.78865 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e040f3ea-e330-3bfb-9b80-4a6936635302 | -8.59455 | -51.55476 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7b747145-0268-3a10-9a50-6d07fb4fc511 | -10.55144 | -46.36068 | 2025-06-27 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| eacc4991-1efe-3465-9704-06d8436bde41 | -10.85341 | -47.21521 | 2025-06-27 12:46:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f36db303-eb67-3ead-88ca-f8547f85c238 | -10.03211 | -54.31814 | 2025-06-27 12:46:00 | TERRA_M-T | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 52debc05-b244-366c-9699-802bb1830691 | -10.6392 | -46.71309 | 2025-06-27 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6f1d78d7-0dda-3a9f-bc6d-f939c6c0ebdd | -10.81377 | -55.87477 | 2025-06-27 12:46:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 69036b5a-0826-3444-b78b-337ba9e40d01 | -10.80908 | -57.75407 | 2025-06-27 12:46:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b2cb163a-b6ac-303a-b804-943e299d6479 | -5.71763 | -43.81993 | 2025-06-27 12:46:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| f5d9340b-c24d-3cf5-921c-0be4f632810a | -10.03074 | -54.32741 | 2025-06-27 12:46:00 | TERRA_M-T | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d2ce3126-6c93-364f-9294-bbfeb4a6d00e | -8.37217 | -49.23755 | 2025-06-27 12:46:00 | TERRA_M-T | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 26adc55a-5e62-3596-8aae-5342fa8dc239 | -9.07138 | -49.4285 | 2025-06-27 12:46:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| b6991cbd-d435-3912-bf51-bfee68f53c33 | -10.38188 | -46.78441 | 2025-06-27 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 82d3bf41-7cff-3900-9874-6cc9e57f3cf3 | -8.48077 | -48.26418 | 2025-06-27 12:46:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 10f2ace8-50f4-329d-93d1-bc009c21f783 | -6.17658 | -48.08596 | 2025-06-27 12:46:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 305d4a19-6270-33f6-b2c7-aad9837fe515 | -11.4388 | -54.4781 | 2025-06-27 12:46:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ce0913e4-8c94-3da6-b6b4-41b18b6a152f | -10.82799 | -53.74122 | 2025-06-27 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 8c3e3c17-5e25-3495-af65-27ac04e59cc3 | -7.7179 | -50.77896 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9953cf01-eb27-3255-81b0-d8aee67ef0c4 | -9.10938 | -45.23622 | 2025-06-27 12:46:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c419f212-d6e0-3cd5-a00d-b2217e5359f0 | -9.1162 | -45.25808 | 2025-06-27 12:46:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 9e0f7209-2a19-3722-922e-56a398c83bea | -6.76311 | -44.93598 | 2025-06-27 12:46:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| e3c99420-d1c7-3892-93a9-10417cf68da2 | -7.55442 | -45.82288 | 2025-06-27 12:46:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 4e1d11b2-f06e-39f1-b44f-9eceb780bd13 | -6.57832 | -55.00065 | 2025-06-27 12:46:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 809b0e81-5161-3c9a-a140-b2c3f71abb84 | -14.74742 | -54.25542 | 2025-06-27 12:49:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 479ce9f3-2c94-3fb6-a1b0-d17a8e3cc54f | -16.13285 | -59.85463 | 2025-06-27 12:49:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 5875417f-e2e4-3fb5-8658-46101d44f361 | -14.97052 | -54.62376 | 2025-06-27 12:49:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 86b83d93-42aa-30d2-a7c3-5cf5c1022a2e | -11.78014 | -55.04058 | 2025-06-27 12:49:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8ba48295-23dc-32a5-99a7-44ff2ebad759 | -12.52939 | -57.18072 | 2025-06-27 12:49:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9c59ec3c-30f3-369e-82a2-c5318e186936 | -15.72275 | -43.61052 | 2025-06-27 12:49:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| e76e6d2b-36cd-3828-926a-ab837f026263 | -13.49314 | -52.96067 | 2025-06-27 12:49:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ee5dcf90-c95d-39ae-b761-5d3dda9fab09 | -13.48422 | -52.95939 | 2025-06-27 12:49:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5d44b8f2-6f16-303c-a043-ea4bd3d6af8a | -12.52554 | -57.20493 | 2025-06-27 12:49:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ee944489-0607-3eb1-86ad-95c7e91cf826 | -14.25818 | -45.49677 | 2025-06-27 12:49:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a7b48e99-b5b2-3c76-af2a-870653ea23d5 | -13.14375 | -56.80133 | 2025-06-27 12:49:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5c645854-587b-35cf-92e7-3a8a41fa32fd | -14.25696 | -45.50338 | 2025-06-27 12:49:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 394e4d1d-a7b2-3d46-8e40-d5aad837c987 | -11.91525 | -54.81519 | 2025-06-27 12:49:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 5580c4a0-7c4d-3ee7-a990-5a2de178d259 | -14.96301 | -54.61329 | 2025-06-27 12:49:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ed8b6321-836f-3ecf-8cd4-c0671266ea8c | -14.24197 | -45.50175 | 2025-06-27 12:49:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| fe980b35-34b9-3bda-b19e-e099ccdc5e18 | -14.96168 | -54.62239 | 2025-06-27 12:49:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e9d7dc5e-5cbe-3c00-beea-6f2baaf49c0b | -11.78156 | -55.03104 | 2025-06-27 12:49:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 03348786-42e4-34ca-ba92-170c04dbf476 | -13.29386 | -57.08518 | 2025-06-27 12:49:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 61c3bc25-3f98-3c3d-b163-3d072d69c104 | -14.54004 | -53.83598 | 2025-06-27 12:49:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b6d9122c-899d-36a9-a04f-145a0cb4b31a | -13.78246 | -54.29916 | 2025-06-27 12:49:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b36ea8e3-644f-30ec-8057-0fdcea69ac15 | -13.93728 | -54.50196 | 2025-06-27 12:49:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 6473f1c5-e361-35d5-9183-3482774cd177 | -12.53132 | -57.16859 | 2025-06-27 12:49:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 3ad435f8-1b06-315f-99a9-e279c369e12e | -13.93862 | -54.49283 | 2025-06-27 12:49:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 294f0b42-b703-31f1-b1b3-17497bdac520 | -14.23999 | -45.524 | 2025-06-27 12:49:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |


[Clique aqui para ver as próximas entradas](README33.md)
