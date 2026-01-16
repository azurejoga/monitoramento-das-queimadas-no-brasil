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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b8fa9a8-cbbd-3460-8ff5-fb798df25635 | -12.64767 | -46.76297 | 2026-01-16 00:49:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| cebbb795-73d5-3556-9179-4e623eea2cc8 | -13.6935 | -52.60587 | 2026-01-16 00:49:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d4c45a85-1a0e-39c4-9f56-798ccaac6065 | -4.21022 | -48.46933 | 2026-01-16 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 98635886-2cec-3324-9626-fe58309fc918 | -4.22169 | -48.47316 | 2026-01-16 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 861eb78a-e6ea-321b-a5f3-fd75f29e416b | -20.4298 | -57.8504 | 2026-01-16 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| b874b671-5529-348a-94eb-48b6c2450a78 | -1.16766 | -53.72975 | 2026-01-16 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| df80b40b-9b9d-3522-bd48-c80014b9a128 | 2.75891 | -60.32907 | 2026-01-16 00:54:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 224f31cb-850f-317a-b726-1a48b7a0a20a | 2.76037 | -60.31856 | 2026-01-16 00:54:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ce496c3c-187e-3698-85c7-e64695f261f2 | 3.59295 | -60.81552 | 2026-01-16 00:54:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9db48d2e-25ac-3d90-9b15-24d1f7946acd | 2.7638 | -60.32474 | 2026-01-16 00:54:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f9cd16c2-e6ae-350f-bf4b-a9cfaeb85ee9 | -17.8391 | -40.0798 | 2026-01-16 01:40:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| 5d04a4be-463d-3bee-9c42-f98e9f7ff7b9 | -18.8119 | -51.6134 | 2026-01-16 02:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 0a450658-34a9-3bb9-af0c-354df094eebe | -18.8325 | -51.5878 | 2026-01-16 02:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f6672525-86a6-3067-9901-f53ec59dd713 | -18.8124 | -51.5914 | 2026-01-16 02:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 77465e0c-f758-38da-83cc-b9988b7749d3 | -18.832 | -51.6099 | 2026-01-16 02:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 8a8f850d-53b4-3bea-9c8c-b23135a4b8f1 | -18.8119 | -51.6134 | 2026-01-16 02:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 93f71a47-fa63-34bf-ab0b-7d172794ab94 | -18.8124 | -51.5914 | 2026-01-16 02:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 66455b5d-c96e-3ea0-bf5c-273eace9d717 | -18.832 | -51.6099 | 2026-01-16 02:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 2ca738d8-6794-38cb-81c3-dc199f90cdba | -18.8325 | -51.5878 | 2026-01-16 02:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 30c44a92-e6dd-3ef5-ab76-0e5a69a763a9 | -18.832 | -51.6099 | 2026-01-16 03:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| aab9f180-fa2b-3169-a9bc-87e1e82a94f8 | -18.8119 | -51.6134 | 2026-01-16 03:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 122.9 |
| a0db7b25-2d9f-3331-8b12-6c3ae94b0fa3 | -18.8124 | -51.5914 | 2026-01-16 03:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 9de56a55-39c1-3969-8aae-8461011384e3 | -10.6033 | -37.0671 | 2026-01-16 03:04:00 | NPP-375D | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 10b414cc-d2cd-3a9a-920f-07c9c5959a10 | -9.4288 | -35.55243 | 2026-01-16 03:04:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 84f19a02-c774-3ef0-b1a0-81da601f4d27 | -4.67794 | -38.0455 | 2026-01-16 03:04:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| edf3c04d-b945-318a-ae28-f3d00a8864f6 | -9.42959 | -35.54829 | 2026-01-16 03:04:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 14bbead0-798a-3c9e-9b1c-cc357f64668a | -4.67657 | -38.05299 | 2026-01-16 03:04:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 30bf9a2c-f1a4-3b42-8197-7b549bb48aff | -10.6023 | -37.07206 | 2026-01-16 03:04:00 | NPP-375D | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| df356da2-59f3-3eeb-aee3-4ad53359a567 | -5.17558 | -37.76236 | 2026-01-16 03:04:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5cfe2130-60e9-341b-a59b-63cd0fb648e6 | -10.60954 | -37.06856 | 2026-01-16 03:04:00 | NPP-375D | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ce37d87f-b29f-32b8-84f6-36eb57209a77 | -4.67778 | -38.0482 | 2026-01-16 03:04:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7180810e-915d-34fa-98a6-d1a05f894ae2 | -5.13482 | -37.60723 | 2026-01-16 03:04:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0489a7e7-e876-36bc-9ea7-174a0bd324ce | -18.8124 | -51.5914 | 2026-01-16 03:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3346b718-3760-3508-a9aa-58db2618925c | -18.832 | -51.6099 | 2026-01-16 03:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 13c75187-36ad-37fa-8497-743fcb32b5a0 | -18.8119 | -51.6134 | 2026-01-16 03:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 9352de7e-e6ef-364f-9def-5ed02152a7df | -18.832 | -51.6099 | 2026-01-16 03:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| f702767d-2f8a-3e4c-b4e6-f8b7bdf2c7fd | -18.8119 | -51.6134 | 2026-01-16 03:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 4a749e13-7d80-310e-95b1-5e60ecdb1cb6 | -18.8124 | -51.5914 | 2026-01-16 03:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| b0d11160-d000-3d32-9725-179823b3c50f | -18.8325 | -51.5878 | 2026-01-16 03:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| dc5187ae-8055-3ab0-89a3-58d5748bde7f | -5.62246 | -38.64435 | 2026-01-16 03:23:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e5b60c14-7293-30f1-8b2c-d2f18b465f80 | -4.9578 | -38.5621 | 2026-01-16 03:23:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e5638d0b-dd96-3d66-8b28-b5dd4b83d2d7 | -6.48108 | -38.30986 | 2026-01-16 03:23:00 | NOAA-20 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6b89293f-a320-3f34-a497-ea28af41b7c2 | -8.01878 | -35.12831 | 2026-01-16 03:23:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 91d8fe7e-f023-3c3a-af6e-113ad6d9c606 | -5.75701 | -39.80296 | 2026-01-16 03:23:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0fecee19-b33c-3d7e-b601-5aeedbb03210 | -5.29104 | -37.70441 | 2026-01-16 03:23:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d2eed18d-ff7b-3232-8ca9-aa1390966f96 | -3.6651 | -39.21896 | 2026-01-16 03:23:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c3551af1-46c0-3404-ac07-042ae08d9b17 | -4.06101 | -38.24662 | 2026-01-16 03:23:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 8da6e35f-7e40-3517-b042-76dc1b709caf | -3.95811 | -38.4656 | 2026-01-16 03:23:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bb212990-505e-3662-a7fb-3c5aa7d535bf | -4.9124 | -43.467 | 2026-01-16 03:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 832fc6bf-ada2-3ce7-a047-3fbd77f33b3b | -3.6657 | -39.21547 | 2026-01-16 03:23:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e63a1bc4-2706-3bab-8a3d-9be96e0174ad | -5.17294 | -37.7648 | 2026-01-16 03:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3c256102-0bad-346b-9825-a8a0b01ee722 | -4.67428 | -38.04841 | 2026-01-16 03:23:00 | NOAA-20 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 6f65b94d-eaf8-39c2-b31a-1e58508e6a54 | -4.67634 | -38.05085 | 2026-01-16 03:23:00 | NOAA-20 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2d7ffa54-6e65-3e48-bdbc-cf44d34fd5d5 | -4.67729 | -38.0454 | 2026-01-16 03:23:00 | NOAA-20 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| fe9c564f-6a1c-3f0e-bd97-ed0c311f108e | -6.015 | -44.55154 | 2026-01-16 03:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdacf098-9284-3443-ab36-31727cd8fa35 | -6.0222 | -44.5528 | 2026-01-16 03:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39187eb4-0cde-3125-a7ad-bca1210f807c | -5.13685 | -37.60273 | 2026-01-16 03:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3eba48c9-f4e4-38c4-953f-20b9270e9504 | -4.9583 | -38.55916 | 2026-01-16 03:23:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 692bb324-fa60-3d90-b936-c53eefcdeb4b | -4.05649 | -38.24289 | 2026-01-16 03:23:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd3821da-c912-327d-baec-0d093c2bd5bf | -8.0226 | -35.12891 | 2026-01-16 03:23:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 604fc54f-51e1-3260-8d10-cbd00a1adcec | -6.48436 | -38.31181 | 2026-01-16 03:23:00 | NOAA-20 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d5955d1-2422-3fc6-bf9e-3a1007ca6fa3 | -4.90552 | -43.46582 | 2026-01-16 03:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d40d1b9f-de5c-3ed7-9b69-b17fff3a60b8 | -5.136 | -37.60773 | 2026-01-16 03:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6c7b0b0b-9ab3-3fa8-a55d-f764e494bc12 | -5.84241 | -35.49097 | 2026-01-16 03:23:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 76477c1b-d679-302e-b47e-9ba32b785b2d | -6.98265 | -42.86604 | 2026-01-16 03:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e3da0abd-5f7a-3ec4-9fa8-83f2b2262bdd | -4.06198 | -38.24089 | 2026-01-16 03:23:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a8f897e5-8af2-3f1f-a784-69e27ad5e6c8 | -6.98067 | -42.87658 | 2026-01-16 03:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 82d8b554-5264-33db-934f-bd7f4a7b9288 | -6.98165 | -42.87132 | 2026-01-16 03:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2dbe6f8c-3c8f-3d5d-86fe-92bf8ceb71e9 | -5.29264 | -37.70124 | 2026-01-16 03:23:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 47b63385-8b83-3dc1-b5e2-a6389e867f0d | -5.29187 | -37.69939 | 2026-01-16 03:23:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| cf2dcbff-e042-32a5-abca-a7db4fb4b832 | -5.75158 | -39.80217 | 2026-01-16 03:23:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 700d0e25-cdb7-378a-baeb-13fe783a8c7c | -4.06149 | -38.24375 | 2026-01-16 03:23:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c76c167e-6e13-3ed1-91f3-d9a0e737b890 | -6.98711 | -42.87767 | 2026-01-16 03:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 03ce92be-12a3-3670-8f42-b41025d52a66 | -4.06053 | -38.2495 | 2026-01-16 03:23:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 4431a0e1-3e30-3969-8833-d584c3a7570e | -7.53866 | -37.67469 | 2026-01-16 03:23:00 | NOAA-20 | SOLIDÃO | PERNAMBUCO | Brasil | 2614402 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f34c28f5-f7f6-3b85-88a6-87a5e34b79c1 | -3.95762 | -38.46855 | 2026-01-16 03:23:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0b51c47e-2451-3f1e-b832-33b5631e53b9 | -4.67917 | -38.04921 | 2026-01-16 03:23:00 | NOAA-20 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 92368fbb-0422-3188-ab93-4821f0c588e1 | -5.17397 | -37.76218 | 2026-01-16 03:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 40ee45c0-1e7c-3074-8a2c-eef48d8262e0 | -12.65589 | -40.97457 | 2026-01-16 03:25:00 | NOAA-20 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e9c618fc-718e-3dc0-a8cd-aa5b5ef65aa0 | -9.85977 | -39.97295 | 2026-01-16 03:25:00 | NOAA-20 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6ed493d0-1428-3e5c-b8ff-0f82788704d3 | -13.43013 | -43.85844 | 2026-01-16 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c5439d3-02d5-3fa5-8074-19b6599568c4 | -9.42805 | -35.54421 | 2026-01-16 03:25:00 | NOAA-20 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 97c026b9-1835-38f1-b43c-924c2768749f | -12.08277 | -45.29813 | 2026-01-16 03:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcc1ea2a-8677-3235-878d-058666c5c61f | -9.92369 | -36.36911 | 2026-01-16 03:25:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d1ad15b7-caba-3c5c-811b-9f740950967b | -11.95209 | -44.21484 | 2026-01-16 03:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07cc4547-124d-3682-9b47-eedd4be551eb | -9.92308 | -36.37265 | 2026-01-16 03:25:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8ce2645d-5297-3c0a-b274-b485a7204913 | -14.48078 | -44.3352 | 2026-01-16 03:25:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80238b96-8260-3725-839b-164003a38ca8 | -12.08411 | -45.29181 | 2026-01-16 03:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e914f66c-6a7c-3556-91a9-c721684a4b77 | -8.36683 | -41.7883 | 2026-01-16 03:25:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| abe6cacd-93dd-3d56-a225-2db19cbf22c3 | -10.61656 | -44.63874 | 2026-01-16 03:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb30f0ad-9b23-3226-b228-19b82abca1ee | -8.36603 | -41.79257 | 2026-01-16 03:25:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 67b5e0aa-ac64-3928-9e07-642fdd7a68c5 | -9.86257 | -39.97263 | 2026-01-16 03:25:00 | NOAA-20 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 89f9dcdb-d461-3b8c-9be9-ac78d9a1d574 | -9.91527 | -36.58848 | 2026-01-16 03:25:00 | NOAA-20 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f66e1396-a06b-3ac7-b4b2-01fbb0261b8c | -14.12402 | -43.42191 | 2026-01-16 03:25:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| add3693a-1737-339e-9af5-802112c4a7a7 | -12.08381 | -43.77209 | 2026-01-16 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3f242ad-0597-3abf-8504-27524061512d | -14.4736 | -44.33868 | 2026-01-16 03:25:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c6979a6a-7194-3851-9b61-0b31df3b806a | -12.65073 | -40.97346 | 2026-01-16 03:25:00 | NOAA-20 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 385a7aaa-5adf-391c-b725-d2dfa027ddd1 | -12.20707 | -39.32841 | 2026-01-16 03:25:00 | NOAA-20 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d69dd8e1-fd74-38dd-8c05-bf54c753a104 | -12.08475 | -43.7675 | 2026-01-16 03:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 589ee795-3cbe-30ba-82bd-5d861c475aea | -14.47465 | -44.33371 | 2026-01-16 03:25:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README3.md)
