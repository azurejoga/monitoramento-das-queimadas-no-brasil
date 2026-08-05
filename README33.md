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
| e27bbf84-2333-3c13-899c-12dbf8c6e019 | -7.6288 | -45.3145 | 2026-08-05 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 691a73ee-bb95-3b94-a800-7178c6cd46dc | -11.3107 | -44.8105 | 2026-08-05 15:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 327d660e-71bc-3a3d-9101-251d7b29758e | -14.1972 | -54.4102 | 2026-08-05 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e6965294-3648-317f-a63b-b17de10d13de | -14.3579 | -47.5144 | 2026-08-05 15:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ed6517df-de9e-3ce0-9759-c80efa8a70cb | -14.3865 | -53.3877 | 2026-08-05 15:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| bca573bd-4fb8-3919-8d43-3eeaa03a5e55 | -12.58 | -46.92 | 2026-08-05 15:15:00 | MSG-03 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9cf71a1c-bf06-3797-81a9-d0b4adc97035 | -6.5699 | -55.156 | 2026-08-05 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 9be2ff7e-4f0d-3f05-b093-ba1dbc2ac2e0 | -14.3665 | -53.432 | 2026-08-05 15:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 796ae820-1d40-382a-8d7f-8d8383c2836e | -6.5329 | -55.1578 | 2026-08-05 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| aa92d77d-c4a5-374f-9e33-ba8aa0920164 | -12.4789 | -50.377 | 2026-08-05 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| e883e867-a64d-3dc7-bf79-77e2dd4699a6 | -12.4386 | -50.5109 | 2026-08-05 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 174.5 |
| be6d1b14-c89f-31ea-9ddf-c9c0a52f89df | -12.4598 | -50.3794 | 2026-08-05 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e183b56a-31b8-3c31-bf81-ffdfe553207c | -10.4492 | -50.2216 | 2026-08-05 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 47f7f7a5-c666-3494-8642-38e3cec36c43 | -10.6184 | -46.3646 | 2026-08-05 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| da5fbd95-9801-3fb4-9154-277acfa8cd3f | -14.1966 | -54.4517 | 2026-08-05 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 11192e7e-5246-308d-aeed-f8cea79fbe11 | -14.1969 | -54.4309 | 2026-08-05 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2c3715cf-22f7-38e4-b4cf-96bc24426b9a | -7.2187 | -43.3499 | 2026-08-05 15:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| c514f6b3-70c5-33a6-baac-35d26bc59973 | -14.3868 | -53.3667 | 2026-08-05 15:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 3e924729-6a8f-3153-a3f0-a19ca2d6177a | -14.1972 | -54.4102 | 2026-08-05 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| fbb8b8ba-2438-3db5-a742-76976855a585 | -12.4383 | -50.5324 | 2026-08-05 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 7e88a69a-2a61-3a30-bfae-29c850253738 | -10.4681 | -50.2196 | 2026-08-05 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| f56da02d-4bdc-39be-8ecd-c558b3b5e952 | -6.8904 | -42.4152 | 2026-08-05 15:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 6913795c-1f1a-3220-bac1-491fa91d4905 | -14.3865 | -53.3877 | 2026-08-05 15:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d8134c6b-3347-36f6-b956-a3097b3fe4f5 | -8.3494 | -46.394 | 2026-08-05 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 4de10124-92de-3da9-8e8e-19d96e17fadb | -10.9192 | -50.4283 | 2026-08-05 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| b082b8ee-386c-3194-93d9-e502b61c107a | -7.4913 | -45.8468 | 2026-08-05 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 8b5ab95a-8c5d-3c68-808f-914d0e60dab8 | -11.3107 | -44.8105 | 2026-08-05 15:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 7f08ac39-5d60-3591-96bc-e0b2a1646e67 | -14.3516 | -53.1612 | 2026-08-05 15:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| d56d3b88-d1aa-37b6-91a6-2b76aeb4298a | -14.1969 | -54.4309 | 2026-08-05 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 9d2a4a77-79bc-3965-afbd-33902439cd68 | -6.6538 | -56.4235 | 2026-08-05 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a7ac0b39-6a9e-3970-b10a-fdc7f93b6817 | -3.1939 | -43.1873 | 2026-08-05 15:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 159dc38e-8c97-30e0-8cb4-b4ee6eb7dd99 | -10.4678 | -50.241 | 2026-08-05 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 1d2f3553-ec83-3ad8-9296-a9cae5953c12 | -14.1972 | -54.4102 | 2026-08-05 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 4157aa04-2533-3ec7-9534-f1d5a9d80d40 | -7.2296 | -45.7575 | 2026-08-05 15:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 10ad607e-80aa-3719-8b2c-699a4b21f00b | -12.4386 | -50.5109 | 2026-08-05 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| e317e3f3-1b84-33ab-a68f-17f0c24231ae | -10.8121 | -65.091 | 2026-08-05 15:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 354e53ec-f976-34df-9e34-0ed9947a0cd7 | -14.1966 | -54.4517 | 2026-08-05 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 28984ab3-f9ab-30cd-8474-c7476de05994 | -11.3107 | -44.8105 | 2026-08-05 15:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 1fcae566-ed18-3de3-96e3-f9af92684d76 | -14.1966 | -54.4517 | 2026-08-05 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 90377770-eea6-3bc7-9ed2-f13b6789596e | -7.2296 | -45.7575 | 2026-08-05 15:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 497d4237-286e-3ce3-91ba-26fe10e8c816 | -10.1634 | -46.3304 | 2026-08-05 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ccf67d3e-01a8-3489-9b8c-e210f2b852f0 | -14.3868 | -53.3667 | 2026-08-05 15:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 59e7a0bb-b7b0-34a1-8351-e3dd78b69517 | -14.1969 | -54.4309 | 2026-08-05 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 52c2920f-3872-3b02-92cf-acee7eb303b0 | -10.4678 | -50.241 | 2026-08-05 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| aac5bf4f-be53-3fd6-acad-b58323753e2f | -6.6538 | -56.4235 | 2026-08-05 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| e633c107-d21e-34b0-b5bf-efd210351236 | -12.4386 | -50.5109 | 2026-08-05 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7c2efd52-7a6d-34a8-bc3e-1add4247ef30 | -2.8654 | -50.4643 | 2026-08-05 15:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 216ef81a-4736-3f54-b9d0-d6ff440cb20c | -14.3665 | -53.432 | 2026-08-05 15:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 2095076b-c08b-3672-8590-fc2e473e871b | -12.8994 | -52.8301 | 2026-08-05 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 39f991cc-0ad4-3117-bce9-158e879336bf | -8.5696 | -45.3569 | 2026-08-05 15:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| baf4e74e-48c1-3287-bbb9-762d8d8760ee | -3.1938 | -43.2106 | 2026-08-05 15:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 15ff78c4-6033-3295-a371-eadc7c200b10 | -12.4789 | -50.377 | 2026-08-05 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |


