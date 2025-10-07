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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddb023e4-0922-3f3c-acf0-ea3dfaf73ac3 | -5.65672 | -43.18778 | 2025-10-07 05:50:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5337da8d-2634-337e-956a-88443d8ec137 | -10.15973 | -61.9503 | 2025-10-07 05:50:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7703423c-3cda-376e-ad71-6f19a4cdb1d3 | -10.55746 | -56.5531 | 2025-10-07 05:50:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f45a190-762f-318f-8fcb-9a693494c659 | -5.84302 | -42.86033 | 2025-10-07 05:50:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 897b5aeb-c09f-3f58-bb51-e0140d862e20 | -9.41697 | -61.88708 | 2025-10-07 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56cf6363-ef41-3c22-a5f1-c6dd767bd164 | -8.78498 | -71.03262 | 2025-10-07 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 030393f1-3b7d-3cb1-9023-9577ed02d629 | -5.50064 | -43.05734 | 2025-10-07 05:50:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0e77931d-1717-3aeb-a90c-4e1deab60462 | -10.89773 | -69.55872 | 2025-10-07 05:50:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f0781d3-c81d-34cb-b886-eb5469db933a | -9.14053 | -62.36901 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba1b0e01-46c5-3e33-a542-520cf3c5144f | -8.15204 | -62.82854 | 2025-10-07 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6d4d3a9-21dd-3c20-b2e2-003b6fa56ac4 | -4.69319 | -45.84528 | 2025-10-07 05:50:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 20925f5a-befe-3d62-99e5-c255cfd94f30 | -8.2312 | -61.17056 | 2025-10-07 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 752d9371-958a-3749-b786-6247c30b31a5 | -12.90761 | -54.73613 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e305cb3e-0654-326c-98ef-3fc1f16dd164 | -9.55573 | -63.50743 | 2025-10-07 05:50:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eca4cca1-ab06-3601-96bc-9c4b3b52b60d | -9.45009 | -56.6605 | 2025-10-07 05:50:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a66cf5a-37d0-3dfb-a90d-f07c9a00742b | -10.87204 | -69.2042 | 2025-10-07 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1f5b972-9fc0-3ac3-a2bd-60220730cca5 | -9.14834 | -60.62151 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c46e174b-955f-3942-bae8-5ae5266b1a11 | -8.92625 | -62.20918 | 2025-10-07 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 119cc53e-3d71-3f5e-aaa9-387354ae3394 | -8.80614 | -72.74333 | 2025-10-07 05:50:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7032db8-6e5f-3f63-bad5-4005fd9fe770 | -9.63526 | -57.02206 | 2025-10-07 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14abac3d-0264-3f56-83d3-ba7409769918 | -8.86311 | -62.36278 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b900ed69-690b-339b-af85-4c9a126ab518 | -8.2306 | -61.17476 | 2025-10-07 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7bb0c8e3-d67b-35a6-97e8-63a3e910a237 | -9.32202 | -62.41009 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 303f2768-63f5-374e-aea5-ed95c063f36d | -9.60766 | -57.14595 | 2025-10-07 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f10d0e12-563a-3358-a455-79cf2ab0644a | -15.21962 | -56.76263 | 2025-10-07 05:50:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97eed0b9-3fde-3769-9fe6-57c51bad7fc9 | -9.74885 | -62.27068 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 989d3c0c-1b36-32cb-83f5-4f1d0a39dae6 | -10.15605 | -61.94574 | 2025-10-07 05:50:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c249a0d-1bd1-3403-a313-11332e1b1177 | -15.18795 | -56.82229 | 2025-10-07 05:50:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaf71422-c95e-39de-9182-2b27f2b81801 | -8.85454 | -62.36515 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03279352-2478-30da-9f48-946f8ffbd028 | -12.9161 | -54.72329 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 074a53de-40c3-35e8-894d-8981f8624fa2 | -12.89841 | -54.75554 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf665be7-5039-37bb-8c91-65f88bc6e290 | -9.14882 | -61.23576 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d8b7132-103f-3454-9388-73ed94e65252 | -12.89142 | -54.75459 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d497cfe1-d8fd-39b8-9f4e-ff33d93db38b | -11.86535 | -56.88948 | 2025-10-07 05:50:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2a23e6bf-3659-3820-9337-39548343247e | -9.40038 | -61.43912 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f742ae8-d87a-3146-add8-00d8a98a9f5d | -8.83632 | -62.36969 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5d1d183-4e98-307d-bb99-3b8c64947454 | -6.95542 | -71.49759 | 2025-10-07 05:50:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cae1bcb3-bb69-38da-8c08-1e0a15986001 | -9.19968 | -62.59573 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50cf4111-4cc6-32af-9d5f-8c90bf12b7a1 | -12.90685 | -54.74308 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 73d42b12-821f-3f99-b016-1069a621319e | -9.39981 | -61.44336 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b311474a-65cb-3f8c-ad95-2f82d1a9ce6f | -8.15981 | -62.82972 | 2025-10-07 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 396e6642-5ca1-3f0a-a076-f043acc5fff1 | -8.85907 | -62.36217 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e593962-ff79-334b-852b-e82462ceb3f3 | -8.14816 | -62.82793 | 2025-10-07 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d516014-5a55-3df6-8fa5-e6c263e1c2ea | -9.14769 | -60.62622 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cbdbeaa-aac3-39f1-9479-79083e5e479f | -8.93033 | -62.20979 | 2025-10-07 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddb8a993-1288-30b9-826a-cf3d444d10ab | -3.10008 | -47.00775 | 2025-10-07 05:50:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| b088912c-4e32-338c-bbd4-d8d794d29a98 | -5.39508 | -40.984 | 2025-10-07 05:50:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| a0463cc0-b987-3a6f-bdcf-64d2767ff2a1 | -9.14314 | -60.62553 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ae0460d-073b-378b-bb74-0d47d03052cd | -9.66811 | -61.9164 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97ca0f95-37b7-3fca-b36c-ac9c63f36d1b | -9.56332 | -63.50853 | 2025-10-07 05:50:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7230390c-d61e-3cf8-9e2a-f819eef989cd | -10.36268 | -57.83128 | 2025-10-07 05:50:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91d410be-e67c-3383-a997-adead304dda1 | -8.0708 | -72.34386 | 2025-10-07 05:50:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07febaa2-6ac5-3e5d-95ae-1277ebb2669c | -9.75706 | -62.27203 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db05c402-f8c7-3c8a-8522-ffb18d78b227 | -15.19188 | -56.82316 | 2025-10-07 05:50:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02080499-2d9b-3403-9d6b-68241f063627 | -9.03606 | -61.64718 | 2025-10-07 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd9b09e9-14d7-3ef2-9489-74db12f89db2 | -10.56358 | -56.55383 | 2025-10-07 05:50:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f23302e7-c319-35ec-9237-4046b75d4adb | -10.87262 | -69.2006 | 2025-10-07 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ea7ed56-7a0f-30e5-b3f0-96ab2678790c | -12.89843 | -54.7406 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 21ebf0e3-4fe6-3cf1-bdc8-8ef2051743bc | -9.14941 | -61.23151 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8e7fe59-1837-35d0-b4e4-669f2e01d605 | -9.75347 | -62.26763 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdcbf47d-3b00-3db8-ad90-b372d5fa76e5 | -9.84703 | -64.26597 | 2025-10-07 05:50:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a22d13ca-fae3-35d1-9a75-86e223f96317 | -15.03001 | -56.02789 | 2025-10-07 05:50:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 067a5452-7d40-3c63-a002-8fb96ffeb617 | -9.17926 | -60.36141 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb94ce18-ace1-3885-9346-a76e28d000d8 | -8.23 | -61.17896 | 2025-10-07 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 714d8042-e2ef-3df5-a352-bef803729dd3 | -12.89985 | -54.74224 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2eef02b6-7201-3e4e-88d6-33924ba8c099 | -9.75296 | -62.27136 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b834838f-dabd-3851-b541-667f864b6c50 | -5.24064 | -46.56245 | 2025-10-07 05:50:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d5029ce9-d057-3480-9a55-03a5b2670878 | -9.58795 | -63.90849 | 2025-10-07 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71255617-d39f-3dae-b3d4-d31b1e306018 | -10.93456 | -51.13259 | 2025-10-07 05:53:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ebb620ab-855b-38f9-9f0b-c78929ff3f53 | -6.44887 | -44.57366 | 2025-10-07 05:53:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 1ee35d97-c993-325b-931c-95927fe05f5e | -10.92316 | -51.14186 | 2025-10-07 05:53:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 8e00da1d-8bbd-308f-940a-728a538d1dd2 | -12.98964 | -46.784 | 2025-10-07 05:53:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 37b3af55-5729-315f-81c3-422617a694da | -7.75128 | -49.85175 | 2025-10-07 05:53:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 99ee7b7d-0afe-3524-a447-30174cad3299 | -5.21797 | -47.37177 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 903d6bd5-6cc2-3185-878f-06621f86c87a | -8.6495 | -46.27587 | 2025-10-07 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fe21143c-5c02-39f2-a360-7e142485326a | -12.72845 | -47.93668 | 2025-10-07 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 178ef738-f9eb-306a-84b5-8fca69ce335f | -5.67256 | -44.26011 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8aa6e7a4-efe1-3a1d-b750-3959320f4cc0 | -8.61366 | -44.9255 | 2025-10-07 05:53:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4dac2b23-b799-34c2-b51e-e424d8ab93dd | -6.23654 | -43.26685 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 5d6a7124-d8d8-3213-b24b-f7006214c3c8 | -5.71477 | -44.83704 | 2025-10-07 05:53:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 75948537-e156-3352-a402-6d262606560c | -10.91409 | -47.11875 | 2025-10-07 05:53:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| d4e2ae6c-4b29-3df8-be7f-5a9106cd7250 | -6.45766 | -44.57496 | 2025-10-07 05:53:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 4813fd0f-88e2-3dac-a512-d73a3a743f9c | -6.45503 | -44.59252 | 2025-10-07 05:53:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 52a9d2df-4344-3d7e-95ad-d4a60e6d1b77 | -11.506 | -44.96933 | 2025-10-07 05:53:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2e0034fd-8652-33d0-9013-15775f584c57 | -11.94381 | -46.42746 | 2025-10-07 05:53:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9cc0a2d2-140e-307d-b9f2-768bf0fac2cc | -13.54274 | -42.98714 | 2025-10-07 05:53:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 19e7b36f-772a-3796-b153-537dc12c5d01 | -6.44756 | -44.58244 | 2025-10-07 05:53:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 35fd7d96-b459-3556-b23f-62b7c5bf1e63 | -6.72665 | -42.82354 | 2025-10-07 05:53:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 402b31d5-c48e-3d9c-ad28-d9a96f3bfd20 | -10.02557 | -48.2938 | 2025-10-07 05:53:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 57ebd9ce-eec6-3ad1-ac29-6257033d61f4 | -11.88616 | -44.95724 | 2025-10-07 05:53:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fde399f2-73b1-39f8-962a-bc002ca6badb | -6.45634 | -44.58374 | 2025-10-07 05:53:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| c54b1346-4970-30c7-b326-f6472afd34f0 | -13.49976 | -43.66799 | 2025-10-07 05:53:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 6863be72-c17e-391b-a68e-558648aa737e | -8.6556 | -46.29536 | 2025-10-07 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| d1da852f-3ade-3909-908a-ae3f8a765c02 | -10.88405 | -51.01978 | 2025-10-07 05:53:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 735e6973-1a01-32d2-91fa-92325c6b2e1c | -10.0351 | -48.29566 | 2025-10-07 05:53:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b6e6b4d3-b1d2-30b4-ac93-9d6ff794b807 | -8.62113 | -44.93566 | 2025-10-07 05:53:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 4ac8fbcd-048c-3b13-bdcd-ad84cb4091c7 | -7.69012 | -42.4073 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 215c2b2b-c047-3a89-8b16-596f50236894 | -5.98687 | -43.51459 | 2025-10-07 05:53:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c322fa3f-e95c-3d59-ac64-a6af993c3c76 | -10.03692 | -48.28421 | 2025-10-07 05:53:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| feedb5a7-3a63-36b2-a036-fef320d0d20e | -12.02068 | -47.78902 | 2025-10-07 05:53:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README107.md)
