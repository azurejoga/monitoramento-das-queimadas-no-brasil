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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4295b99-dc44-38f6-9c5f-d10a8281dcba | -9.65054 | -68.61394 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a03ff8b0-40ee-35b8-af15-010ded16ff96 | -9.1041 | -65.5079 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36e66f65-adb5-3aeb-8113-948c4813914b | -9.02315 | -65.44486 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b7dcf35-de1c-3cf4-9483-be1dd6da377f | -9.31722 | -68.72787 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62a10637-fce1-385d-bbb0-370dafa86414 | -8.60235 | -67.18983 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c3b28385-d2a9-332a-8048-535f5e3b3362 | -8.66809 | -66.94572 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e81f615e-4ba5-37ad-8e40-a63dadfd3660 | -9.16357 | -58.31467 | 2026-09-04 06:01:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b14700a5-d5e7-3c55-8b3d-1af12c8ee7c0 | -8.64207 | -67.00266 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7bb4e98-c1e3-3f08-8159-f90cd0e753b3 | -9.10872 | -65.50085 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f1278bb-5418-393a-9b96-27be349b21a5 | -8.48217 | -70.6146 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c4e85a6-51b3-37a3-9aa5-d3a03c7cfa8b | -8.66754 | -66.94923 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 423e3bd5-1283-3511-9c86-5106db6aefb5 | -8.87034 | -68.61178 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1269e05-5007-398b-9e19-05047f7eaec6 | -9.03064 | -65.73515 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca932486-9ee5-31c3-92af-c2833f62f28b | -8.89637 | -68.88495 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa4da42-b069-38b5-8c43-de1c0b3ea627 | -9.20986 | -71.62212 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8da02511-76e7-363a-9f94-0342274f2e2f | -8.91863 | -62.35476 | 2026-09-04 06:01:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c245a436-baab-3c8c-939d-cb4fde2db8fc | -9.17868 | -68.26503 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f03c1d93-23c0-3145-a822-57647c54d467 | -8.60401 | -67.17935 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 1790f304-215e-3bcf-8186-2cf227def22c | -10.28542 | -68.83421 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58ebaf3e-31ea-386c-a95b-8253f1de7ac1 | -8.63598 | -67.01963 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 129067cd-e6ed-3885-bd38-b57fc42c0286 | -9.05006 | -65.74582 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f49a6c48-27a2-3593-8341-582e0603ec9c | -8.87858 | -68.49604 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a01a8342-f075-35da-866a-b00f12143b6f | -9.11622 | -65.49812 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b183ef56-1457-3ffc-bb9d-3c08a391db6e | -8.70883 | -62.94531 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f0cd2c0-3b89-32e0-a4d1-5960fc9b6e9c | -8.86796 | -68.49796 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3b5aeb8-f1de-33ef-8653-1ba656d98825 | -9.17215 | -65.56011 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c80438f-5af8-34ad-8c4f-dec2d39a40f9 | -9.09661 | -65.51064 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1450862-c7da-345b-9ff6-e3c9ada18459 | -7.78683 | -66.95632 | 2026-09-04 06:01:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e976c386-1618-37e5-86d6-509a94d53802 | -8.76588 | -62.83054 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5f532e3-efe4-3587-a781-9949c07572de | -9.0472 | -65.74158 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4d0341b-affc-310f-a1c8-2afe4f5b125a | -9.25854 | -65.90999 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ed62adc-75ee-3482-9f8f-1d4e746bf19f | -9.53472 | -63.56477 | 2026-09-04 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f520654-a90c-3860-95ba-6be93d80f20c | -7.8794 | -71.76315 | 2026-09-04 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7ac40d2-6798-3421-90e3-13fdcffc7724 | -9.04148 | -65.73306 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65219da4-5564-3ae9-a3da-f8e10012dba9 | -8.89389 | -68.92171 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3941535-046f-3198-a1bf-f9a7a52a4ece | -8.67142 | -66.94625 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a290896-d857-374e-b582-dae9d401aacd | -8.6332 | -67.0156 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db51cbca-2ce5-313c-b725-731f2b13e442 | -9.15993 | -68.53064 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68d06a93-d37e-3e6a-9d6c-cc1c6d7fbf83 | -8.60345 | -67.18284 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 0e27eef3-5170-3a6f-826e-30f3fbe81678 | -8.60123 | -67.17532 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f26ab4bb-0af2-3c65-abee-831f80aecac9 | -8.86553 | -68.86134 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 438eaf0b-f3cd-3904-8419-8a60c7bfcfea | -9.03692 | -65.73997 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9412f7b2-7132-3677-bcd0-7a2900832097 | -8.98567 | -65.38832 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8beb2c25-00a6-3a9c-9e07-935a244c6525 | -10.54321 | -69.02772 | 2026-09-04 06:01:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6917b236-854e-3d85-8b13-0bce80999dc5 | -9.73877 | -69.07749 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c30de3c-dc9e-3ed3-88ab-964f486f1916 | -8.5968 | -67.18178 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c77b3a8e-e2d9-388f-9f83-3972cde5fba3 | -8.66698 | -66.95274 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48b12cd7-c925-38f2-8af3-0a6f210443b0 | -7.74659 | -70.54489 | 2026-09-04 06:01:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa832190-b45d-383e-8c2d-d3145c10c416 | -9.83836 | -65.06084 | 2026-09-04 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d648c8a-6452-38e8-bb53-589c5db68ea7 | -8.87245 | -68.49139 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af6a781f-ee7d-3f95-aaed-253f7d012f56 | -7.8913 | -71.73996 | 2026-09-04 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c114182-4bd0-31f8-bed5-1b162055a49c | -10.07957 | -67.75581 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5d8e814-c2a7-3c31-861a-1145ee370536 | -8.6029 | -67.18634 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 60ec6976-5852-3851-854d-d046c402b92c | -8.71121 | -69.99658 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10489f2e-f065-36dc-aff0-36690cc631e3 | -9.38949 | -68.72873 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cf86719-ba1e-3f6a-b5e3-25bd10755b72 | -9.04091 | -65.73679 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22acaf10-163b-36b8-bc3a-4275c26aa40b | -9.89832 | -64.81919 | 2026-09-04 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c4eb1452-1719-3f0c-97cc-14593842acda | -9.44159 | -67.42401 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da786f2b-49e3-3148-aaa0-cbad2f8af2c9 | -9.02256 | -65.44866 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d2d8163-383b-3460-9d74-523953673d9b | -8.99083 | -65.44764 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 118cab90-00c3-3150-aed4-a077bfbce5f8 | -8.88185 | -62.34942 | 2026-09-04 06:01:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8a11e19-b580-3e41-955a-4fc025085166 | -12.16371 | -60.76402 | 2026-09-04 06:01:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10ca84d3-5235-3902-a061-37c3059f23c2 | -9.04364 | -70.89648 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c65c1e1-a1f6-325e-8fba-707b647b283e | -9.16403 | -58.31123 | 2026-09-04 06:01:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4fe3135-15f0-3e14-b2e3-70173122c640 | -9.11276 | -65.4976 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91d5f0a9-8b36-38a9-94d0-670ad40abfb0 | -8.59735 | -67.17829 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a76a00e-2a7e-37d7-9a2e-fd13c785e1f1 | -9.17811 | -68.26855 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34aa12f2-15af-3e7d-8e9d-a81b2df7b7a5 | -8.99024 | -67.02551 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c51c7f3b-d5ed-3c83-97da-8c5e779e1142 | -8.88593 | -62.35003 | 2026-09-04 06:01:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be1901e8-8d38-3618-900f-3dadfa2533c7 | -10.63837 | -68.9582 | 2026-09-04 06:01:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 93d34f80-e932-3865-b624-8b9619a80df6 | -8.60456 | -67.17585 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a0d07417-c131-3ff6-8aa0-3d8deb63cbd3 | -9.04371 | -70.89816 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23522f40-965b-3f51-8872-20ce307900ef | -8.86853 | -68.49439 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7ee669f-7d7a-327e-864e-d76514cbd53b | -8.5979 | -67.1748 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 476bb95a-6cf4-315e-9c3e-da3515f4b990 | -9.17477 | -68.26801 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 172dfe94-ff2c-3e58-8943-cda1cc1f1cc7 | -8.56472 | -63.19678 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 218f8caf-0ef4-3994-a94e-a045b7a1d02b | -8.73515 | -69.59173 | 2026-09-04 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a8fe0f4-75f0-353a-82d6-663ad6bac477 | -9.71601 | -65.01035 | 2026-09-04 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5678b48e-ffc0-3e7e-858a-3cddef7ba5ff | -9.11218 | -65.50138 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 396357de-0f62-3eae-9e96-0ab018bdc3e5 | -7.57116 | -67.39657 | 2026-09-04 06:01:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1310ca96-3513-3c56-b22f-bac9a447b371 | -9.5309 | -63.56417 | 2026-09-04 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a1aa4ff-a5a2-3eeb-88fb-2a7070a06ead | -9.64719 | -68.61339 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 849fe054-9038-32ac-a234-c7dc3145a003 | -8.92469 | -62.37052 | 2026-09-04 06:01:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b44ea76-8ef1-3d1a-a532-0642cd68d8fc | -9.04663 | -65.7453 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c18674ba-8755-35b3-9cc8-0cdf672f0e32 | -9.11334 | -65.49379 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdd66760-73da-3f5b-a167-aabe33983746 | -8.90072 | -62.36325 | 2026-09-04 06:01:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d0e84e8-f9ff-344c-b2e8-1cf53fc6b613 | -8.87188 | -68.49494 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f110f579-975c-3498-83fc-b5983cef5a19 | -9.04777 | -65.73787 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bfe7fd0-2e91-3407-ae56-cac299954d79 | -8.80754 | -69.02387 | 2026-09-04 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e189e7e5-e127-3737-bb8a-4a1aa6a7def1 | -9.03406 | -65.73569 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03dc0e7d-8753-3044-9ee1-84c64c02360a | -8.60623 | -67.18687 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 07c1b427-362b-3d2a-8028-462fe2c3b85d | -7.87467 | -71.76741 | 2026-09-04 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca99647c-70af-303c-b9c1-71fa349ca30e | -9.10006 | -65.51116 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 011a44a5-cf87-311f-868f-be71d7838fa1 | -10.45246 | -61.20667 | 2026-09-04 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96563416-4672-387c-9cff-6a5f07bc256b | -7.3918 | -72.80099 | 2026-09-04 06:01:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d96d7a0-2ed3-3e98-9243-2a4f0c99dc16 | -9.76179 | -64.97202 | 2026-09-04 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2724165a-41f8-3dfd-9356-552888d0f75f | -8.83868 | -62.30645 | 2026-09-04 06:01:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 172115d5-5005-3107-af7f-fca52aed656a | -8.59846 | -67.1713 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ab606ed-8336-311d-833f-61c6890a2d92 | -8.87705 | -68.6129 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d79a27b2-bc5c-3472-b2a3-740211ac4fb1 | -8.56928 | -63.19256 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README36.md)
