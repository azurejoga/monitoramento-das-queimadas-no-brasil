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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 718e795f-1742-360d-a2d7-74a923f9a107 | -8.53323 | -55.31897 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8acdb5e-426b-34ab-b25c-3ca8510f8e5c | -6.78822 | -59.43529 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1d4eb34-809a-3c3f-8b07-3126e90822e1 | -7.01739 | -59.55376 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bb9e327-3ff4-39e5-8785-97af9d198e65 | -6.77272 | -58.69424 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 071bbc6b-b47e-30b9-b554-7cee935f6aa8 | -6.96483 | -59.04838 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1bae566-4f98-300c-9a3b-6262b676cfc6 | -6.81356 | -59.40383 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0aed5e7-8535-321f-9dff-8973de638f74 | -8.54022 | -55.32494 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10e5ae56-7fb0-347e-aa33-e625f6526d05 | -6.78821 | -59.41399 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| a2a2d22f-0f2e-35a1-b69b-fd571fa008b0 | -6.80751 | -59.4206 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 875ce5e9-b26e-348e-abbf-c123cf2b8537 | -12.72423 | -48.41473 | 2026-08-22 05:23:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92e137c7-ef73-3370-b3a3-cd318af707d0 | -8.53951 | -55.32977 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01a558e5-61e4-3f98-8264-0989fd6eba88 | -13.25171 | -51.61005 | 2026-08-22 05:23:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9566034-3d4e-365a-970e-d46d3fe82273 | -13.92556 | -58.2593 | 2026-08-22 05:23:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcf2b2c2-b368-36e5-a862-1f969809048f | -6.60181 | -58.95897 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42c22200-3311-3e5d-8250-9e6e843b5110 | -6.67229 | -58.74966 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67a41c91-5f11-32e9-9b60-601e96ae1cd6 | -13.83195 | -53.99357 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ef82c28-ebc3-3f86-a79d-fa3caf4be41c | -6.13433 | -59.91505 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb4c19ce-b279-3a7c-8d70-a381a69b3f45 | -6.71243 | -58.99036 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ea62c15-3780-3e27-999d-f4b97c748780 | -6.37139 | -54.9444 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ec5c341a-1e9a-3889-8f63-1769df91eb83 | -8.59632 | -54.71705 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c373d9f9-81da-37d2-be9e-d3bfa8d89b9f | -15.00367 | -52.6964 | 2026-08-22 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14b863df-7846-30c4-9a78-c7804cff36ce | -6.23309 | -55.42474 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10ffd2ee-dda1-3de4-bef8-5018e1b4f7bf | -6.70077 | -58.93529 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfdc6d79-90fd-3b70-8d76-ec1c7f28b6a5 | -7.59488 | -60.93695 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 171985f6-fa90-3dc3-af6d-47e7fdd7ecca | -6.79069 | -58.64355 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| db2e78c0-0522-3a8a-98af-d06c7e1d26de | -14.00392 | -53.71025 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3611b49f-6973-390c-a6ce-9549d4d50ef6 | -6.43107 | -54.95586 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba717467-c3d8-3cdc-8bcb-f4d2d1a0cd6d | -6.75885 | -58.65283 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f7748641-f681-3f72-9bc4-b7611ccd43a7 | -6.95139 | -59.30519 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d7240c1-8357-32f1-8677-184b6be93968 | -6.88148 | -59.42532 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72cc2484-ad57-33b0-9a41-1e07319e247a | -6.81907 | -59.39052 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ebe3224-2182-3b72-8604-d9c0ab77cd13 | -6.86927 | -59.43752 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53fe8073-5a78-31f6-8c64-b4c5b5aeb3a6 | -6.79098 | -59.43927 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eefce7b4-fc03-3267-912b-7e3152fc049c | -6.79483 | -59.41504 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 074d9831-e9d4-3fa4-9980-5d8f2366d2d4 | -14.42696 | -51.80147 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a588759-7096-32e0-9f60-de2eb0f3edc5 | -3.68869 | -52.04141 | 2026-08-22 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 433c82d9-a531-3268-b378-2f4b633ae94d | -6.95905 | -56.40892 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5787b46-8f40-3741-8072-58b4e956ef19 | -6.85439 | -59.4458 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75915874-b169-359d-ad50-96a2d971818c | -6.92111 | -59.34648 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f13091e1-83de-3c88-acb9-a5678b76fb7c | -6.85665 | -59.02417 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a446ad1-b044-3cb0-847f-c2d9908351e4 | -8.51783 | -55.31659 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49090096-0b78-31dd-b6a7-5dcebaaddfc6 | -6.76223 | -58.69615 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb6175e0-2f66-3eb1-8707-dab48db761fa | -6.9181 | -60.06953 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64e7144f-0fbe-3874-85e6-b3a035471883 | -7.37404 | -59.95974 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e274d58-3be1-3c08-ab7b-dc03c3390cbe | -6.6587 | -56.34135 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1e517cc-7c0c-3f8f-9e3b-f90c04d0a737 | -4.12109 | -49.44776 | 2026-08-22 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87eab2cd-fbec-3a69-a6e1-90d930060d57 | -6.53327 | -58.53209 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d3465ec8-9816-35c7-bda5-ca6030c9e649 | -6.79429 | -59.4398 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08534281-408d-33fe-bbac-93ed8529a722 | -6.79925 | -59.42994 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6984d9aa-1901-3984-b1e1-3c591c4e7053 | -6.79124 | -58.64006 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 27ecee54-3aa9-3740-91e1-f699329328a2 | -6.89031 | -59.43382 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07506884-72da-3ad2-9d39-750ceca7768c | -7.60443 | -60.94221 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a4f6025-6eec-37ee-8bb3-a7e80204ac5e | -6.93211 | -59.31987 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bf6f9a8-45d1-35c4-95f7-333c1ad763bd | -6.93982 | -59.31399 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0b6e148-4c9e-3f7a-a96c-90ee0db335c7 | -11.7222 | -59.34742 | 2026-08-22 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be1e90f0-87cb-3cef-942a-f4e4ece6be2a | -6.38143 | -54.95547 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1dcda18c-bb45-3cb7-a02e-139778f6df77 | -5.99824 | -57.80698 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db21de6a-1188-3a10-a0c9-eeae069eff59 | -8.53701 | -54.82921 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dbe0001e-6d06-3f04-a43a-aff41c7c0da6 | -6.79656 | -59.59632 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fd3af519-7f0d-3b2c-a4c3-127970b3ae90 | -4.05891 | -49.10575 | 2026-08-22 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 289606ec-7262-3518-ae0b-87810cc1f913 | -8.52755 | -54.83837 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 67a07f39-2234-3cb0-8898-51dc9a008cef | -6.79347 | -58.64754 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bc6ac240-0ae1-3479-9626-ed7f23729834 | -11.81957 | -56.59641 | 2026-08-22 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13310ca7-0682-3d22-af1d-32db05dd1ba4 | -7.08727 | -55.45412 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c780884e-ba65-33c7-b4a7-c40fde83e4df | -6.9665 | -59.05929 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17e6cf77-00b4-3738-9068-9088e612e548 | -6.43562 | -54.95166 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ccec541-6bc5-343b-857d-e495d8bb25a3 | -8.58778 | -54.7482 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 379d2d7e-24b2-3d6a-925f-c09f47202d5f | -6.77163 | -58.70119 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cb86e21-7105-35fc-87e6-b5c164332b42 | -6.81358 | -59.42512 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df54c0dc-6e5f-3c4e-bb47-d52d3079b908 | -8.17315 | -54.98809 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1cf3b62e-dadd-3be2-bbf5-488e5252e7fe | -6.15113 | -53.7046 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcf81b8a-2fc9-3285-993b-c0b7751cd465 | -13.99124 | -53.6986 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a26772b-6d39-3afe-8bfa-cf0e51cf4930 | -14.00413 | -53.671 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ca85ce6-26bb-37f3-b995-14dbb6a26192 | -6.65514 | -56.34081 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8e0eaf7-7d80-3748-8960-69087a278a0f | -6.80914 | -59.38895 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 93a48227-b45c-330c-a873-64b416909feb | -6.93485 | -59.30257 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8853dd0-044c-3e8f-bc26-461a8844dfa9 | -8.1566 | -46.72052 | 2026-08-22 05:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b95c1d89-2675-35ee-889b-d04be05830dd | -6.59762 | -59.11426 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08dc26d1-d658-369d-976d-ad432cec5652 | -6.54155 | -58.52267 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 17631a32-64eb-3991-af03-3afbdbd38b94 | -6.12823 | -59.91048 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f423c367-f15b-32bb-99c1-4ee9b93d164a | -2.18244 | -60.22549 | 2026-08-22 05:23:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c683406d-6a0b-35ff-b3eb-ae09377a265d | -6.80257 | -59.45176 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f1357bd-bd69-365e-8fbd-67cdf6c9ff92 | -6.65159 | -56.34027 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a4dcc55-5a07-359f-b590-41cb545962c5 | -6.8494 | -59.41307 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13076800-fda2-3581-8f51-c6d5ea8c3541 | -6.25329 | -55.39157 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c3559d8d-9505-365a-8bf4-f15e5f893233 | -6.79178 | -58.63658 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ee43646-9858-3cb9-b64a-18734495ab1d | -6.13434 | -59.89352 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0d5a9ff-e9ee-3d56-a3cc-b915d808f0b5 | -6.80091 | -59.44085 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e14ea6e-36e3-3fd4-b77a-d372db61167d | -7.585 | -57.69389 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50634350-d410-3a07-93b6-c60ccc8acd76 | -8.5833 | -54.75103 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d17bdc7-26f7-3953-8130-525b1386677f | -6.7951 | -58.6371 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f243fc48-274a-3320-9916-c537d8c4bf3b | -6.12767 | -59.91398 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94b986c5-067f-3276-8804-1fe3f31958a7 | -6.53382 | -58.52861 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c9963004-6ae4-30ed-ab7a-06a21b63a63b | -4.53568 | -55.62067 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1212e40d-07d9-3d59-bece-62106560d210 | -2.89308 | -48.79628 | 2026-08-22 05:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bda2bfa-3479-3478-95b8-d9cd02460163 | -3.5358 | -48.18061 | 2026-08-22 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b379bd13-eb40-3d03-9f86-584d3aa2bac9 | -8.5873 | -54.7516 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3458e3ef-4f2a-36ac-b7d6-7c0d16c92967 | -6.86603 | -59.02919 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3bc77b31-d457-3dac-bcd0-314ad9a8bc33 | -6.24424 | -55.42641 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c2996f0-6bc6-353d-b447-9c0c66848afc | -6.76494 | -58.65735 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README59.md)
