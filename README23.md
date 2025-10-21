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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e94b552-a7ff-3f38-af9e-854e251f771d | -8.92222 | -66.89167 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20f1500d-fddd-37ef-9b0d-5b7d483dec1b | -10.59389 | -65.28934 | 2025-10-21 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae9ed940-3c2b-3afe-b1b0-e70d8da038ad | -9.00525 | -65.93434 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3c2c7205-d5c0-3e59-917f-45ea104edd78 | -9.04316 | -65.69922 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28d71b1a-92b7-3f56-9d90-2277fc282b87 | -10.06645 | -68.20653 | 2025-10-21 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ede790f-4d21-36be-94d3-8939539afc0f | -9.62173 | -68.60377 | 2025-10-21 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0430bd58-4245-35a2-a969-a27436422189 | -9.00704 | -65.92324 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 582fbf27-63c1-3923-84ca-e449ed771062 | -9.11383 | -65.36626 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab81388a-d8ea-3852-b8ba-6d7da58f6e47 | -9.56862 | -65.22064 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a4ab088-8576-3386-ac64-d02766f81c4f | -9.37694 | -62.62936 | 2025-10-21 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 593d4c33-6a35-3957-a339-f6d95b8b4ee8 | -8.57574 | -64.07066 | 2025-10-21 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00a7bcd5-8737-30ce-a7b0-67b9129409a9 | -9.66949 | -66.84645 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fd149ac-883b-3c02-871b-359a3f92aaa0 | -9.71916 | -67.48883 | 2025-10-21 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 244e2d26-e5dd-36d8-af8a-4c537a182a3c | -8.99444 | -65.93636 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 473964f2-1f86-3f89-acbc-204bdd8d09bb | -9.12055 | -65.36015 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1acf4e2-cb13-3587-8a6b-322e473958be | -9.3775 | -62.6257 | 2025-10-21 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e410b659-37cb-3b30-b2d8-f48b79ae5462 | -9.72051 | -65.87595 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5878cc2b-097f-37f8-8a9a-44aadbbe1575 | -10.30684 | -68.8636 | 2025-10-21 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3130ee4-b717-35ee-b4ff-c3b865910da0 | -8.99743 | -65.91787 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| af3b386d-2eb3-323b-9026-bbb4ec5bcdf0 | -9.24865 | -63.63546 | 2025-10-21 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc9aa297-69e8-3a55-bc72-e32e8db04abb | -9.97881 | -68.84985 | 2025-10-21 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 924ea581-53c4-30a8-a25b-7c56e2091d39 | -9.55317 | -67.40984 | 2025-10-21 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d30ff5f3-a90a-3738-afc2-95ab580e1f34 | -9.61817 | -57.8406 | 2025-10-21 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e5d4047-461e-322b-8770-91467a5ee56f | -9.62322 | -64.7495 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf12ba6f-10e7-3134-8ed2-13ab5b595bce | -9.31375 | -62.01281 | 2025-10-21 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38c0fb0c-85ea-3aba-8afa-bd9621d9645f | -9.79843 | -67.03071 | 2025-10-21 05:36:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 007bbf73-e93a-33f3-af4c-061463c585e7 | -9.72412 | -65.03227 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a7c6291-c606-3631-b49d-fb8ee8a73ef6 | -9.76054 | -65.08155 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73d2dae7-00a0-3155-8b82-8c1cd539c632 | -9.36872 | -64.34065 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc95e323-f95c-3aa5-834a-90df908b728c | -9.62653 | -64.75003 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 191d23fd-c2e3-35f8-9b17-e3c47d07db3f | -12.42083 | -54.42296 | 2025-10-21 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e14f11e7-2c0a-393b-bcf8-e476ce2383a6 | -9.52235 | -63.92561 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ad935e3-74d6-3965-bc86-2fce092f8ca0 | -8.99343 | -65.92101 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7bc5d042-8226-343f-87b7-1f4ce8890ccc | -9.89422 | -64.17483 | 2025-10-21 05:36:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95ecc12a-ca3c-382e-95e5-3072fcca8071 | -10.52347 | -68.04189 | 2025-10-21 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f5b8edf-0e95-335a-b3b3-58086d6abf3d | -9.18535 | -61.38621 | 2025-10-21 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 68f5265e-6f14-38a0-85b2-d932fa1f04e5 | -9.00984 | -65.9275 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 906d1963-e550-3f82-873f-a62f0b5ecf17 | -14.82684 | -54.70923 | 2025-10-21 05:36:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3eb6cef-4e93-333c-a8d4-392b59109791 | -8.64369 | -66.51411 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6df08177-8dce-3433-89af-4b20bfbc0c64 | -9.68566 | -63.17939 | 2025-10-21 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a5ab418-b99a-360d-ae20-f1a0f00a4c5c | -9.01104 | -65.9201 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6dcf218d-0e91-3392-bd28-e1a06273ee8f | -9.81809 | -64.227 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2940e42-2b63-3a64-92ff-a9729062e663 | -8.88803 | -66.8571 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41c61a60-97f6-3e09-9856-5221b234ae41 | -7.70249 | -67.03322 | 2025-10-21 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b5ca367-fc61-35af-ac6d-a343052075b9 | -9.1144 | -65.36269 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce3ca2d6-162b-3b87-90e3-0e7f1b94e019 | -9.64791 | -65.25563 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 054abfd4-db1a-3d0d-97cc-3385ccd04323 | -8.63694 | -64.13379 | 2025-10-21 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43fb83c4-0e31-3d6d-a622-3560b1dac2cd | -8.78313 | -66.72252 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e474fa43-a3c9-34bd-9237-49e6bd220e4b | -9.74808 | -64.19792 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee409451-5a19-3bbd-8e6c-c9071387f8a8 | -8.57188 | -64.0736 | 2025-10-21 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdb2ed58-2eb9-3cb3-99a1-42952f5ab278 | -9.01385 | -65.92435 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 548252fc-ab81-3038-80d1-a4f57a37f1f5 | -9.37257 | -64.33771 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 4e202caa-17a6-37a2-bde9-74ca96afe33f | -9.72056 | -67.48041 | 2025-10-21 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f34174e4-62f9-3306-9d76-d7d81742e7a2 | -9.68987 | -63.3077 | 2025-10-21 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2b2c1f0-5660-3709-bd3d-aa7edfdef2b5 | -9.64458 | -65.25508 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c239213-e8ee-3881-97f3-d58f1192e806 | -9.6109 | -66.11591 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f51e24a5-5e67-3a6f-ada0-18f804915f7e | -9.96169 | -66.74149 | 2025-10-21 05:36:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f3c659a-60eb-3cc4-ab58-df4fcd68b577 | -9.32623 | -64.65177 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a987e7a-8218-3d92-b587-7edcb6d6aff6 | -9.11832 | -65.35966 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff0a68c4-ad1a-3265-8cbc-9dbb94f49cfa | -8.90941 | -66.88128 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86a494c6-d4b5-317c-bc23-bde5807b98a4 | -9.64125 | -65.25453 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ab50c5a-4e32-304a-9614-d7f5bfba946b | -9.04257 | -65.70287 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 943645c4-1e83-343c-8362-86e9579443e8 | -9.65125 | -65.25616 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f61d769-0c03-32d7-b26a-f8049a98abca | -9.6226 | -57.84119 | 2025-10-21 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf3b05c5-b346-39c6-b3a6-f0dc31f7a3fc | -8.93998 | -65.92738 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c95421ea-2608-3057-bc33-22e39eb190ad | -14.82638 | -54.71338 | 2025-10-21 05:36:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8663530-965d-3d00-b738-20ba3d183bcb | -9.85839 | -64.16551 | 2025-10-21 05:36:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91991e18-295a-30ae-a6c2-c53a35b131cb | -9.48499 | -57.92874 | 2025-10-21 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3182603d-a21e-3246-b05c-a1c36dd84578 | -9.48067 | -67.06705 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 397c68b9-891c-3630-80ff-76cbee74bb63 | -8.1648 | -64.0051 | 2025-10-21 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a3aad4a-d428-3439-9c29-316aa8310964 | -8.6402 | -66.51353 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4c8107c-f781-33fc-94b4-34d7ccf5371e | -9.54222 | -64.57534 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 559e6cde-b781-3289-84d1-3d332761d4b7 | -10.29914 | -68.86218 | 2025-10-21 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9129bfa-8272-3fea-9914-1d491529810f | -9.00644 | -65.92695 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 18e55f61-24a0-3f2c-97fb-c4a00681c88a | -9.83335 | -67.56753 | 2025-10-21 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d03b4ec0-a8b1-3390-8d4e-77a5a341d66a | -8.93938 | -65.93108 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c619c571-a9cd-37d6-bdda-a9d786d78b96 | -9.04595 | -65.70342 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6d83d2d-2238-3935-93e3-9db6e2b68af4 | -9.11497 | -65.35911 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c1dbbdd-47e1-3de6-a32b-3baae6f39f3d | -9.64401 | -65.25863 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f90240af-e9ee-3512-afff-219a3a613629 | -14.82592 | -54.71758 | 2025-10-21 05:36:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6929e0f4-d998-365d-ac31-f17f29545cf5 | -12.39086 | -64.30092 | 2025-10-21 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fb824ee-22db-377c-99eb-debeb00a884d | -9.55677 | -67.41045 | 2025-10-21 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd4b02d7-464f-3a72-9942-c698db382f8f | -9.04654 | -65.69977 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf8decc0-d7d1-3852-bedb-15f1d6cb400f | -9.37865 | -62.64086 | 2025-10-21 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a079d89-5130-3b5d-abf2-7fc632567e3c | -8.96441 | -65.92761 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b202d96f-6a08-30ee-98cf-ff82973fe97c | -9.11048 | -65.36571 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64f11d86-4f5f-3262-9f62-dece99fe2c33 | -9.67629 | -64.4361 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45652f1a-bf5f-34b1-96d6-fb144a14fd23 | -9.00424 | -65.91898 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b382ce05-4306-3928-8619-f98d01554518 | -11.03904 | -68.49259 | 2025-10-21 05:36:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71b79e76-45d5-30c9-9970-2a5448994e77 | -9.00125 | -65.93748 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9443f9d-5579-3651-883a-23e0700ac1ff | -8.6368 | -63.02735 | 2025-10-21 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9160ebaa-6d71-31e8-a8bb-a9a4dd73cdb4 | -9.56918 | -65.21709 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f880d52e-5513-3139-9b66-4379e4c56591 | -9.01164 | -65.9164 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd2e44f9-aafd-3143-8614-44e0ceed68d8 | -9.642 | -64.7382 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42d40624-28d0-31a0-8c14-76762883c7b0 | -8.97382 | -65.89124 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 838fdf8d-463f-3233-9ec7-d41b083391f5 | -9.55176 | -67.41817 | 2025-10-21 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d8229f2-a462-3010-b1a5-aed2ed45dcfc | -9.00184 | -65.93378 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 68b42902-1e2a-3a01-940a-13b43e608928 | -9.00865 | -65.93491 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3af92db-dc15-3f48-b1d4-2b9d3f3ff63c | -10.04205 | -62.46882 | 2025-10-21 05:36:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32fe33e1-6e48-338f-bfb9-6976d50ab056 | -9.10713 | -65.36517 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README24.md)
