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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53b91836-3857-3ce0-a55c-c133e98a63c5 | -9.1066 | -60.3467 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07460d4f-33b2-3268-8786-f53738656ef3 | -6.79977 | -59.58524 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fe691975-eb61-3d52-aa7c-0e6aa72dd43c | -8.53454 | -54.86504 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34efb060-5f38-3343-9655-af3a0a731be6 | -9.46417 | -51.63368 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86751fc2-174b-383a-9d48-898358e6f432 | -13.40659 | -54.37215 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba952b0e-5f2f-357c-aec2-d603249afe17 | -8.55526 | -54.79742 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e29835e-7da0-3da2-b4ce-ec76c25f9a05 | -8.09663 | -51.66681 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cd6fb3ec-2adf-3c86-88b3-9293c02d403c | -9.98848 | -53.93919 | 2026-08-20 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 611fe846-b337-3220-b1e0-60fcd224fe99 | -12.94284 | -56.62842 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34ad6049-9095-3016-afa4-fd7f38013cc2 | -13.45312 | -51.42519 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44db44f9-c389-32ee-881d-8b7bdeda5f46 | -8.58349 | -54.75706 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| acb902f8-0d06-32bf-a619-66501524239a | -7.55034 | -55.56332 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89f98781-8da8-388a-992c-eb7267021287 | -7.60099 | -60.95734 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19b192be-5f96-3c86-93ab-44949e9779f0 | -11.21787 | -55.06089 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ef18bd3-d3a6-347e-8f19-c0e48003ae72 | -11.22203 | -54.00668 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df09a0ec-4a5c-3a5d-b1fa-ea0c7e0a4772 | -7.05752 | -59.84109 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 687c632e-31e5-364c-bfe6-c8ffbc4f999a | -7.54549 | -55.59469 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eec296bc-5299-3e40-bc91-c984e21878d6 | -10.90996 | -56.36794 | 2026-08-20 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9e341c0-ee72-3f16-8bed-1b2e3d1a55ac | -11.42611 | -54.3184 | 2026-08-20 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1490a254-b22c-3e72-bcbf-3b4f5d8ab853 | -8.40097 | -62.69944 | 2026-08-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c937a61-c333-3bda-90bf-a668e13d90cd | -6.76919 | -59.14767 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c205017d-b139-3d0c-9f12-ad06b3167fc9 | -9.50434 | -51.68169 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa2881ca-2cc8-38e8-9b58-35d1c4a7109c | -13.4489 | -51.81766 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b151607-515b-370d-9850-49f362f84226 | -8.64498 | -62.83164 | 2026-08-20 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6be3c9c9-93ac-3dd1-baab-6df103763c4f | -8.56294 | -54.65607 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95b099a4-9533-3689-8bbb-a7f2c373738a | -8.71633 | -49.61552 | 2026-08-20 05:06:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 923f43e9-5765-3c0f-9633-d008f4a38892 | -8.56649 | -54.76932 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be722a74-43c0-30a9-af45-660caf4c3726 | -10.94007 | -57.18068 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7e8c2f7-f7bc-33e4-98f9-7cde79858b58 | -12.94949 | -56.62947 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cda4d82c-8701-3fa3-858b-48d32c9d37f7 | -12.81479 | -48.44319 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4e2c809-b591-389a-8195-d002c383576b | -9.39049 | -60.56138 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05f0376a-aa54-3da0-bce7-ff139f4246b5 | -8.56593 | -54.77296 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da8d0eb6-1567-3c65-96c5-86125a0dc676 | -9.40005 | -60.59627 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45a2be26-d039-322a-8836-79ce2ca26d6a | -9.10792 | -60.92934 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16e3f6c6-1a61-3fc0-8a58-f46e870249ce | -11.74828 | -57.81352 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee8e9f15-f937-348f-8dce-92212f8f44e1 | -11.14594 | -49.04443 | 2026-08-20 05:06:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0083b6d-a9d1-30ab-856e-62c4bf41693f | -14.45262 | -45.62507 | 2026-08-20 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2ba6a648-daa1-3439-8b5c-92178d31daa6 | -8.53343 | -54.87232 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4779150-6863-303c-ad1f-cf03f0b6627c | -9.45611 | -51.60454 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a48d65dd-3553-37a1-a98a-1e2a3a2edc7d | -8.57662 | -54.74845 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0ad1ca8-f9db-3d1c-b809-a284653cdbc8 | -11.21131 | -54.00504 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72c1fcbf-ff87-3b66-9c60-f5e2b5b53401 | -9.42441 | -60.40761 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 100832bb-ed52-3b8d-8b3e-3b4a7df24303 | -12.01328 | -53.44271 | 2026-08-20 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74c93251-4e15-3e09-b2f2-56751ce3e028 | -8.28918 | -62.90046 | 2026-08-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6c3aade-d89d-3d3b-adcd-1eab8f8a4c6f | -11.1994 | -54.01171 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb0bc2fb-b509-31ab-a557-e3a4488c021f | -11.18476 | -54.01955 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 623970ce-44ea-3390-95af-dab09f31a312 | -8.54354 | -54.87397 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1d1068e-e105-39bd-a8a3-d08c13ed3982 | -9.21886 | -59.77676 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 50ab1206-89b6-32ab-a61e-d51e69fbaef8 | -8.5607 | -54.67082 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb736a80-975f-3230-8e87-ce0106b60d23 | -12.79481 | -48.43333 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6476a70e-fe41-3492-b410-f0c2d4bcdf90 | -9.21816 | -59.78099 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1fd3eebd-6139-3870-9dbf-122d27ea2c71 | -7.77644 | -61.15651 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b06bb3c3-e49b-3aa4-8bee-08691f39a7fb | -10.24336 | -49.42104 | 2026-08-20 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f8ef5ce-c145-348b-b291-3e0f5e57da61 | -11.81031 | -44.81281 | 2026-08-20 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d68193c-a4a9-37f8-9399-165aeea1da74 | -10.33177 | -57.56475 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88dc2753-2328-3780-8fde-4ac9a4a7518f | -9.39883 | -60.55474 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c69ad445-9f12-320a-b48c-fabba09c8200 | -10.90108 | -50.27614 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6628aeaf-36a6-3740-9059-e827adda7396 | -12.79901 | -48.43535 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86619545-0a00-3d31-98a1-8cb4be3d799d | -7.34233 | -55.67662 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 38c9a87f-b379-3a09-bcb5-e28b97f02de5 | -11.19048 | -54.02303 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36c60d24-124a-3309-932e-04469b0e39e1 | -8.49692 | -54.88518 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 247c3b11-7e5a-32c3-b2df-a58409ff7e1c | -13.40398 | -54.37844 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ee91a263-7b1d-3a66-bb5f-0dabb2c68d2c | -11.39049 | -46.37571 | 2026-08-20 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67fba81b-c8ca-36b1-abd3-61cc39e0f23b | -8.55958 | -54.67818 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8731aa8e-1ed9-3643-8229-8906a4f332e8 | -12.24978 | -43.17041 | 2026-08-20 05:06:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| e203881a-f1de-37f4-b2de-0a5367de40bd | -7.88124 | -63.29469 | 2026-08-20 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| add00cf6-01e8-32c7-8e06-672a209b82b5 | -12.781 | -48.45243 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 411d4266-d06d-395f-9c3d-752e1e783028 | -12.79865 | -48.43823 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 274272d7-615b-3b9c-8adb-de7d0b587d64 | -9.39959 | -60.55014 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8c70354-59e1-367d-b929-777f56c548b1 | -7.0538 | -59.84044 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8189823f-f260-336d-a6b4-b66bee43c9e5 | -12.94895 | -56.63303 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b75c67e-ba4a-3db5-bfff-df333d5af1d1 | -8.5812 | -54.74924 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b27f788-36ae-3a30-b983-f707e4e0f677 | -7.54101 | -55.57972 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54f4a0e6-a8c3-3af5-a90b-293ce0d17aab | -7.54602 | -55.5912 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f00a4889-fe18-361c-8838-9488f3fb9c6f | -12.95396 | -56.64478 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc2f59ad-d996-3643-8689-c74b418eb441 | -6.95495 | -59.04841 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9abe7670-3b49-34fc-9a03-d5f4a6327ab1 | -8.61836 | -54.70982 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e7039d42-fd84-3bf6-8d12-96f54b8c4feb | -12.76951 | -48.45977 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e3e499e-42c4-34e7-ac33-da0638ba8632 | -11.32202 | -45.21059 | 2026-08-20 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b1ea6fec-463c-321d-b5a9-4ffb8a253633 | -6.76492 | -59.15123 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 515b87af-db15-3ed2-a31d-21a9e398ae97 | -11.43052 | -47.24795 | 2026-08-20 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d6e781c-2270-38ae-b3a4-2a6b4f1a18b9 | -12.47338 | -54.19532 | 2026-08-20 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ffb83d-d9d3-3f1e-96e5-61b27106b61b | -9.22248 | -59.77736 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 36b6357d-5ea1-3b3c-b4d0-89fd34ec2e10 | -11.20539 | -54.81433 | 2026-08-20 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 289d109b-ce99-3aa3-bcf5-9d3902789a0a | -12.81514 | -48.44025 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66664479-dbc7-3a29-92c0-0c9144bcc46d | -11.39101 | -46.37138 | 2026-08-20 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d7c41f23-c446-35eb-bbaa-bcac0ac8f82a | -11.43116 | -47.24603 | 2026-08-20 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0659aab-11c7-3b7c-9b98-3ade5d1a4909 | -8.53792 | -54.86559 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77c2db53-2dd6-362e-a90c-13bdb52a65ea | -12.15814 | -57.21913 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f027307c-b7c2-3e26-acbe-e28b490d4dcc | -10.45355 | -54.66488 | 2026-08-20 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 97b62373-1ff9-3398-8f27-715893c7cfab | -8.58908 | -54.74295 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 264b3eab-e434-3099-8568-0403cc599f96 | -7.45023 | -60.00524 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9950357-8512-34dd-bc9a-e6b6403e84fe | -8.54172 | -54.79534 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0983c0e3-6937-348d-b10e-4a2fce3adb8f | -8.53232 | -54.8796 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcd1dadf-3b92-3ee2-b3a0-5493391bb408 | -9.40178 | -60.5633 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8482332-4dee-38e9-a3fe-279becd0915f | -7.44647 | -60.00467 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8da6b5fd-51a7-38d5-abb8-89c350b3de56 | -9.3988 | -60.55806 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44463e59-1527-3654-a3b8-99ce96289d86 | -9.3928 | -60.56795 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 537cadd2-a5b1-3ed2-92a8-1ce3f270f2bd | -8.52839 | -54.88272 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae3f2b81-205e-35e3-a4c7-e7cb977f7486 | -8.54506 | -54.77346 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README51.md)
