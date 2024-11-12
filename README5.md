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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfc98275-b376-3726-8d74-85028281d189 | -2.73449 | -54.13848 | 2024-11-12 01:02:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9cc4467a-76ae-3daa-af0a-dca78530990c | -2.68392 | -48.6664 | 2024-11-12 01:02:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a15a2512-0fd1-30f7-8bfa-d876397c89fc | -2.67707 | -49.26765 | 2024-11-12 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a2436704-d2ef-34d3-bbb7-1397e8c92ff3 | -2.95706 | -49.09643 | 2024-11-12 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 45b129b4-0d5c-3760-86e8-39ac52fdf003 | -2.78511 | -50.30692 | 2024-11-12 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 64aeee11-11a3-3d37-b03a-8108f405d694 | -2.75168 | -49.34103 | 2024-11-12 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| f754d782-41aa-382e-8f70-d3814a6dff97 | -2.39496 | -48.89788 | 2024-11-12 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 19aaa20d-aa2f-3497-a6a5-6d144fc8f441 | -2.30015 | -49.53756 | 2024-11-12 01:02:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 737f6691-a8ef-34b6-a414-bddd3727ab1b | -2.7922 | -50.2986 | 2024-11-12 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 257690e1-b4cf-34d1-8ccf-664d434ed899 | 2.762 | -60.9598 | 2024-11-12 01:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 1fd46edc-845b-3d94-ab20-4a8ef4f887eb | 2.7621 | -60.9409 | 2024-11-12 01:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| eab4e4f1-053a-3999-9be4-97051475c20d | -2.7921 | -50.3196 | 2024-11-12 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e3f8e192-fb5b-37dd-92c9-6a748f3c6e60 | -2.7737 | -50.2992 | 2024-11-12 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 86a3265c-f3e2-3d3c-ae31-20bb794643b9 | -17.648 | -57.4229 | 2024-11-12 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| cc2e42aa-3f30-38a3-a82c-f9822272d880 | -17.6283 | -57.4252 | 2024-11-12 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 72634df0-3c2c-32bb-8b94-11eedcfd3dd1 | -17.6089 | -57.407 | 2024-11-12 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 5b6e24dc-af8b-3647-b77b-d1da0ad0100a | 1.048 | -60.5986 | 2024-11-12 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 7235221a-b7cc-3f1c-b878-5b919eadc4de | -17.6086 | -57.4276 | 2024-11-12 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 55adb025-8a64-339f-8f34-eed38096a0cd | -2.9913 | -51.3356 | 2024-11-12 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| e785abfc-4809-37c6-be49-15cd62063806 | -17.6477 | -57.4434 | 2024-11-12 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 312b826a-e0a9-3dfe-b0f4-af289d496dae | -17.6286 | -57.4047 | 2024-11-12 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| f4df1c51-d3c2-36c5-aba8-b315d136320d | 1.0663 | -60.5985 | 2024-11-12 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 24461641-a25b-33f6-84a0-4efae06d2b1f | -3.1096 | -54.3066 | 2024-11-12 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8a5c8ec1-96dd-3542-a990-8f90998c3a9c | -17.2737 | -57.488 | 2024-11-12 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| 6028045d-bc6a-34b0-814f-1e770973795b | -2.7737 | -50.3201 | 2024-11-12 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b6361c78-bcff-3265-b10e-ada5eaabd42d | -2.9912 | -51.3563 | 2024-11-12 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| f9842755-1e9e-3154-bb93-6d9c62bede71 | -17.625299 | -57.533901 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1cf4368a-b197-301e-a8d1-f4fc26b18a7f | -16.008301 | -59.365601 | 2024-11-12 01:13:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ad63b56-b2d4-3cb4-8279-4a4f8b1f9e41 | -17.316099 | -57.487 | 2024-11-12 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c8a716d5-f790-34e9-ade7-3dc87919b726 | -17.5865 | -57.497799 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 14a3cc4c-755a-3859-83aa-12c57672c187 | -17.2918 | -57.4701 | 2024-11-12 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7bcac38c-4392-3fa4-8b2b-a744518dde78 | -17.6012 | -57.4715 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d53f83fe-5c51-32f6-98e2-180f7c777954 | -4.3396 | -55.352901 | 2024-11-12 01:13:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6c56cbb-abf9-3fa4-a997-b669e6324b3d | -17.654699 | -57.526901 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82b5c840-124f-30de-a694-347ed8b532f3 | -17.615499 | -57.536201 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 35635014-2da8-3a2e-b12c-c6743c52ac77 | -17.614201 | -57.483601 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6ed34bfa-4921-3e73-810b-1dd887778aa1 | -17.613899 | -57.528999 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 809a81e5-45bc-3440-aaea-602e3df43f7c | -17.596201 | -57.495499 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6a3da78-8525-3bfb-ad29-35309953c4ca | -17.6406 | -57.416698 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1bda8118-86a2-330a-ae39-e4a87133e30b | -17.7185 | -57.488899 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ee6a6070-bb30-37c7-a3d4-fbd47f7302d6 | -11.1699 | -56.289101 | 2024-11-12 01:13:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fecd7ad0-1d92-3539-b060-28bd439087e7 | -15.9617 | -59.292702 | 2024-11-12 01:13:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45096fb1-efc2-317a-a11c-05cd19055e47 | -16.006701 | -59.358299 | 2024-11-12 01:13:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d600fc90-04de-3f65-adb8-ade400bdd44a | -17.6308 | -57.418999 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 07f15006-b699-3f3a-a30c-681fa9999065 | -8.9954 | -62.092701 | 2024-11-12 01:13:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3cfaa495-8fb0-33a8-931f-7b22453c636a | -6.7928 | -58.780602 | 2024-11-12 01:13:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16a3f9f1-32b1-3168-a864-1ca3caa3109f | -17.606001 | -57.493099 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 561af233-707b-3230-bb20-71bedc967413 | -17.597799 | -57.502701 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b66e5a8-bcd2-3bfb-8175-70c06200278d | -17.250999 | -57.472301 | 2024-11-12 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e5d05f4a-b9ee-338e-9d66-9d759036717a | -17.6194 | -57.4142 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a9c267ba-48a7-369a-b85b-0f090de33911 | -17.651899 | -57.421501 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4070b3f-a6c5-32b2-b7b3-7491f0a765f8 | -21.314199 | -53.920601 | 2024-11-12 01:13:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e10d86c2-4ed2-3a66-99cd-46b3a540eeaf | -17.280399 | -57.465302 | 2024-11-12 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0f6d99b6-1002-382c-8b25-098835d45c28 | -8.741 | -63.4781 | 2024-11-12 01:13:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f44f1e21-80d3-380a-b54d-362391ea0c58 | -17.7118 | -57.5056 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa7ee3a5-670b-3dbb-a394-a0cb6f2b0e4b | -17.718201 | -57.534401 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 929d88b0-33be-37dc-9f33-70532301310a | -16.092699 | -60.097401 | 2024-11-12 01:13:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b873ec62-b5b3-311e-9a1d-9d9a03c9670c | -9.8171 | -63.2379 | 2024-11-12 01:13:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 95d838b4-7703-3f53-9176-b96a787c5158 | -17.632401 | -57.426201 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 64604955-5e0d-39d0-a3c7-b3862e47762c | -17.2836 | -57.479599 | 2024-11-12 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e807794-052a-3ea2-9d24-e39e0dcabac2 | -17.7166 | -57.527199 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 85a7ab77-776a-356e-a6f5-36d696986fb6 | -17.616301 | -57.399799 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f5b0d251-93d7-3027-8d1c-62793cd25fe0 | -17.6178 | -57.407001 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9eadd2c9-527c-34ff-9b29-724e79092a08 | -17.623699 | -57.526699 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e542f22f-615a-3015-b0d6-b71777599513 | -14.4946 | -56.913101 | 2024-11-12 01:13:00 | METOP-B | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf2cbb86-6f1b-3007-bf53-3f99f72531b1 | 1.06 | -60.599098 | 2024-11-12 01:13:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ea84e68c-aec2-3d32-9b11-295a7beebfd1 | -17.5982 | -57.411701 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb45e50d-5fa6-3d85-8e72-c962ced4cfde | -17.2738 | -57.481899 | 2024-11-12 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5c0b8cc4-421e-3259-9361-c62107469285 | -8.7391 | -63.469501 | 2024-11-12 01:13:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 29163837-c8fe-3bda-a4ef-139faa77f083 | -20.318399 | -48.8297 | 2024-11-12 01:13:00 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3d3ffe66-0d85-3de3-bd65-e1a543f75b05 | -17.596001 | -57.540901 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5767d2e9-57df-3154-a91f-c5dc41af4327 | 1.0633 | -60.584801 | 2024-11-12 01:13:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3d86f220-85d7-3525-afbf-f26c73748e77 | -16.082899 | -60.099602 | 2024-11-12 01:13:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91ec3f96-4903-3755-8237-63ff828e5448 | -17.6042 | -57.531399 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 188b4385-8163-38fb-a3f0-95518e1fa362 | -17.6096 | -57.416599 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f413252f-627e-306e-816b-4adc91b5528b | -17.684 | -57.519798 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 23041b6c-843d-351c-a516-f7aba14e573a | -17.6465 | -57.5364 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a5d0a2e-efdb-3cbc-b28e-75b0bd03cc65 | -9.1624 | -61.681301 | 2024-11-12 01:13:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7e23892f-ca00-3084-8c3f-e986e3ab909a | -19.618999 | -54.151299 | 2024-11-12 01:13:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 12beaa3a-a046-380a-baf8-bf301479cd3b | -17.5944 | -57.533699 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 67b76a5e-c9dc-3bfc-8986-111d40c6e3ce | -14.4964 | -56.920502 | 2024-11-12 01:13:00 | METOP-B | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a5dda1e-4d23-3a4e-817d-3a47f3dc0ea6 | -17.621 | -57.421398 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e66f5bc-2c30-351b-a9dd-6678bfdcd035 | -17.6824 | -57.5126 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e4fe4970-1d05-3df6-9899-74918b37d0b6 | -15.9534 | -59.302101 | 2024-11-12 01:13:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30cb1595-8eec-3c49-9024-402ee3c67e9b | -4.3423 | -55.3643 | 2024-11-12 01:13:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c8a01de-219b-3106-9f0e-a555c7255f22 | -17.6292 | -57.4119 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 31434fc4-afde-3362-bbaa-2a3bba44fec1 | -17.591299 | -57.519299 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 994d5567-8d3d-3276-ba19-43bd7a0a4c5c | -17.7087 | -57.491299 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40a0d0c8-b0a3-3a1f-b5b6-3551a6e946ea | -17.644899 | -57.529202 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 06efd728-34d6-3510-ad29-5faa65ad9abb | -9.1507 | -63.237598 | 2024-11-12 01:13:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d970575b-bbce-3789-a6a0-442a04fe8a55 | -17.589701 | -57.512199 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3cfebbd0-d8cc-3723-b9d4-a1540c4745ff | -17.634001 | -57.433399 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1986001b-3823-3363-80a4-8255359f5942 | -17.5881 | -57.505001 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8f65c6cd-34de-3919-890c-eda8794fb411 | -17.643299 | -57.521999 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8ededadf-ba4c-3a82-a81e-278bd7cb1d29 | -19.617001 | -54.142601 | 2024-11-12 01:13:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5417d152-b9a0-3006-9e19-ed9e367ac6f3 | -17.282 | -57.472401 | 2024-11-12 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4860bdca-4291-318a-bbec-e3f5abcbeec7 | -17.5928 | -57.526501 | 2024-11-12 01:13:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7bdbdc7b-06cd-3a94-9f6c-f958c30c0eb0 | -19.4601 | -56.745499 | 2024-11-12 01:13:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7872cfe4-5f31-3293-af07-075c68f22c8a | -16.094299 | -60.1049 | 2024-11-12 01:13:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 452dd88d-8051-39f6-9bd7-3d3e7b93b69e | 1.0616 | -60.591999 | 2024-11-12 01:13:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
