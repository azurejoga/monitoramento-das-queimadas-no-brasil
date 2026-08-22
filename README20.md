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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0327b47-ef5e-3536-91af-51fb2106b022 | -6.75893 | -58.67014 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 49d7cbc0-1cb6-3209-9edb-141a716293b7 | -6.25067 | -55.39387 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c65e4abd-a5b0-3ccb-923a-89d58300c309 | -8.53059 | -55.32368 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 580c4abf-bed5-35f1-872f-ce9550dd0ffa | -11.16174 | -54.03428 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b2fdf84d-fc9c-31d1-86e3-8311d8e26260 | -8.62971 | -54.72588 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ebc9547a-b193-3fc0-9a8c-4e93c623ac6f | -10.70101 | -50.31342 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7abed680-b0a6-36d4-b80f-f59d3f962845 | -9.00035 | -50.72165 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b21c6560-ed6e-3a75-9763-3ff0b327108b | -6.82118 | -59.39056 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2fb01b3c-0655-3575-8dee-eabd7ee2ba72 | -6.779 | -55.70281 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee519f05-1c41-3e41-9657-b76f425df3a6 | -10.39773 | -50.43027 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61c6258d-47e3-373b-966a-9b1ce634cbc9 | -7.49042 | -43.81425 | 2026-08-22 04:27:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ff1e709-3bb3-3202-8a3d-01fe32f8c462 | -9.00346 | -50.73802 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56f4cb67-80d1-3af7-aa35-0eb5187aec0a | -6.94691 | -59.30846 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50aa8a84-59fa-3a1d-b30b-54974b5205c0 | -6.37687 | -54.9472 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b75bf0c-fa60-3d07-81b9-f14bc968ca2a | -8.52732 | -55.31891 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd5718ea-9914-369c-aacc-608713b5b315 | -6.82058 | -59.66835 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d545fd4f-7aa6-3611-9482-af662cb7e8f6 | -9.17148 | -59.46055 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 82bf7b95-8cc1-330a-a1da-54530e612b53 | -13.45522 | -51.76526 | 2026-08-22 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88980688-e1bf-30f8-b49c-ea92694a8324 | -12.26793 | -43.17599 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| aa2a3e5a-7289-353b-82ba-0f834c6fd9f0 | -11.5953 | -46.57849 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5fde84c2-f2ce-3064-a34a-babd7564b2f9 | -8.52225 | -55.31815 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13b4ac17-28b4-36c8-b60d-1c24c652ac5d | -9.1735 | -59.44874 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 711f2a61-f363-33a6-b2c1-2555b037c126 | -9.04631 | -50.83564 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28b7ec40-34f5-3fd5-b77a-fe9ee279bd95 | -6.80698 | -59.66571 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b30cabdf-aa79-383b-b537-345d42c1427c | -6.53557 | -58.53337 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 82e57abb-4dc6-3ab3-a3e3-48b12870faa6 | -9.21114 | -60.77115 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c923628-05e0-394d-830a-0018bb3b10e5 | -6.76187 | -58.65441 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 00cfad4e-3c9e-3a3a-8bb5-a9bff93eb915 | -6.65441 | -56.33771 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e38aa2b4-6a4d-3556-83a8-ce9eeeeec119 | -9.27106 | -45.64192 | 2026-08-22 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32afcf25-6992-3b22-8c5e-ed0260c94aff | -6.65508 | -56.33399 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7380e1ad-a613-3510-9e07-910d954be6ae | -6.53851 | -58.51714 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 794f068a-566a-3d8b-9de1-efa7c486c1e2 | -9.43492 | -51.62053 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85fe2f96-21a4-3ae5-ab43-973d32b51915 | -9.19406 | -59.44678 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13fb3953-4d82-3961-a8da-a8e884754ead | -6.4319 | -56.18737 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbd1a2f4-2767-379d-a670-ec01ca4b5db0 | -7.72289 | -46.14812 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0ad1042c-a7dd-3217-b549-14b52a43646b | -8.53691 | -55.32359 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd69e8c6-208d-3420-a9e2-8e498b9cfab1 | -12.77944 | -48.38649 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3006156d-c8c7-31e0-86d0-01dc07d5fcb9 | -11.13642 | -49.03893 | 2026-08-22 04:27:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cfe09ac-d0a9-3d92-98f5-901acf351187 | -6.38601 | -54.95512 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 006432dd-6599-38ab-9d26-631ee1d9c534 | -7.26059 | -49.87522 | 2026-08-22 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3b6e78d4-f3fa-35e1-bfe1-93bb5c904b2b | -6.76862 | -59.44947 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2c1c8bfb-e620-328f-b0ce-a0219854981e | -8.52842 | -54.8387 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4995da8d-dd78-39e9-ab61-05452505b712 | -11.16627 | -54.02995 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a08dc36c-b0c3-325e-a431-2fbbefa13ead | -6.43405 | -54.95099 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68344799-8d93-3285-9b52-41dc93d0d5cf | -11.84108 | -39.18764 | 2026-08-22 04:27:00 | NOAA-21 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 83f7fc28-05fb-394f-9193-f5386934b543 | -8.63609 | -54.69744 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab4af711-5da4-37db-8aec-27c48278165a | -6.76981 | -58.68316 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c46d16d4-1ce2-311d-89a0-502fcb7caa7b | -8.54144 | -55.32747 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0992f06c-1141-3884-9bf2-fc26b5af2b49 | -11.99777 | -53.4259 | 2026-08-22 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5371371-3ee7-3a91-8104-4ed696f1e2af | -7.48015 | -45.14366 | 2026-08-22 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dac2640-b7bd-386b-a5ae-f624509f4a65 | -11.05152 | -49.10466 | 2026-08-22 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82b3b529-9104-3a9a-82d6-f8e1f935ca00 | -13.69615 | -51.95273 | 2026-08-22 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7be71555-f4fd-30b1-b071-618d43125fb8 | -6.82348 | -59.41593 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ab3b3ee7-1920-36b5-9246-7afb86d675f3 | -6.94026 | -59.30719 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0eca1668-deda-3942-82cc-dda59241e0de | -6.81738 | -59.42565 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 28358b8e-6859-368b-8a10-615a663b593b | -6.85999 | -59.45788 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3c66da24-5504-34de-83fe-3d9ceaecb8b9 | -8.62952 | -54.73513 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de562c3e-1e89-3e6c-91a8-553c069bd8ed | -8.53532 | -54.8419 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1e75725e-301d-31be-bba4-c8b82c3edc2b | -12.72025 | -48.41636 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df284e59-8dec-331b-a199-f5e9fdf7446d | -6.82636 | -59.41491 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9e204c3c-c046-3861-a321-971b46104604 | -11.82183 | -56.59106 | 2026-08-22 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4952b23f-2350-3409-b86c-869e50145587 | -5.80327 | -57.54771 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91d10b13-a992-3fc2-a91c-cfb360444b1a | -9.15728 | -59.46272 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 95988be7-0837-3ea2-bdb6-ddfb41601786 | -11.65583 | -48.35116 | 2026-08-22 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e38c6163-620e-392b-9024-23f529715b2d | -6.90604 | -59.00011 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c6287b65-c361-3643-b096-8a96d712af5f | -6.795 | -58.65484 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 355be070-f485-3ede-9658-a4f23b505a40 | -10.43898 | -50.47159 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62802964-f426-3b7d-9080-0da434654e23 | -7.48687 | -43.8137 | 2026-08-22 04:27:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b910d20-6cf1-3df4-85c1-14d503a2f1b2 | -6.20709 | -53.09261 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1be97b05-ea96-3d4b-8ebf-8e153ded8656 | -8.08847 | -51.66721 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5abe8943-2f34-3299-8765-0d8bf3caf043 | -9.27052 | -45.64549 | 2026-08-22 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b75fd28-1ae3-3de7-bf46-d301a7900a35 | -6.7609 | -58.65956 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 942ea60e-c2fd-3120-aeae-2d60d70d049b | -12.65452 | -47.09205 | 2026-08-22 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24111630-d8e4-3644-91c7-1f2c6d33be0c | -12.21875 | -43.15172 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 974e5f71-4b12-3b94-8c52-50a9eb6e8c63 | -6.15371 | -57.74034 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81a0fdd4-f7d0-32d1-a702-bf4f35ad99c4 | -6.92892 | -59.31034 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 147ccd1e-2328-3c26-a4b9-ab415c0b45c9 | -6.66065 | -56.335 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cf0ef52-4db8-348d-86f7-46f037e36b01 | -14.13635 | -48.06123 | 2026-08-22 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abffaf88-421e-348a-85d4-49234f302dd1 | -7.47285 | -45.14621 | 2026-08-22 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ecdc4fb-6eec-3027-829d-8a08e98b3e71 | -6.25063 | -55.42038 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 843fd2b9-a7d5-3453-9a05-74977cecfac4 | -8.45425 | -51.55628 | 2026-08-22 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0761d9b-50dc-349f-9756-861b58ea2cc3 | -9.10303 | -60.92662 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1bda535-a335-308a-9b89-eff7dd18ccaf | -8.12606 | -45.89214 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8af34a2e-bad9-30f6-aacb-6a05f3cc83c6 | -12.2468 | -43.12697 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a587e748-cfc5-323b-ad53-9cfcf1f9bd13 | -6.64195 | -56.34304 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e317c85b-fa86-3a89-bfae-182092b14e4a | -8.99599 | -50.71359 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54160db6-5727-35fa-94d5-4e4990113cd4 | -12.1006 | -56.32011 | 2026-08-22 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6282cfcb-232d-3a97-b317-4dc91e9dba47 | -9.46447 | -48.29049 | 2026-08-22 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9463b069-71ce-31cd-b0e7-8cb9e5c7d01c | -11.10824 | -49.89283 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f014b0ad-3677-3e6f-9e61-6bceeb3f34e9 | -12.27776 | -43.16235 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c1d7ed5b-11fb-38a8-bf1e-146131882ee7 | -10.52135 | -50.76925 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2017332-e27e-349d-970f-1147969ae2c5 | -9.24793 | -60.79619 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 91780034-8ee6-3c35-ab83-35caf41542c7 | -9.17253 | -59.45501 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 14c7fbde-59f9-3e91-a495-487fc66ab655 | -8.0232 | -51.79879 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d313f7b-129a-3f3e-a2f1-39f80f8587f9 | -8.59359 | -54.71227 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f2fe1c2-f1dd-34b7-8034-511c4ea6493c | -9.4367 | -51.61011 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a19d3203-5330-32bb-891d-105039c28a03 | -11.61358 | -46.54841 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f822fa6-66a7-3281-91be-f24c2c3fd13b | -6.17689 | -55.44275 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4d86aa4-ab2a-3940-aed7-541676d0d411 | -10.39054 | -50.42907 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08d3d61a-10fa-3b5f-a10a-e4ce1f116ee2 | -6.7669 | -58.65876 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |


[Clique aqui para ver as próximas entradas](README21.md)
