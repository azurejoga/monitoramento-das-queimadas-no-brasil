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
| 32df7de0-baf6-3abf-b399-8f4b0dc8b69c | -3.76891 | -61.76397 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39131218-6f4b-315e-893b-965eade73bcf | -7.10112 | -56.51474 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 715359ab-c6ef-3a4f-aa94-882f4084cb01 | -5.65675 | -60.23771 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6df710e-a601-33af-b929-0ff1f9008153 | -4.67927 | -55.62956 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90624c88-526d-347b-8274-3db4e6716522 | -4.4778 | -55.0911 | 2026-09-06 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fc14597-01b9-333e-a8c5-bec16d0332f0 | -6.12696 | -57.74727 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d831648-cba4-3779-a8e3-adf876b81572 | -5.35634 | -56.04468 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59aab035-9f06-361a-841b-7a26de7cdcbe | -6.02236 | -57.69613 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 958ec3a5-7d46-3694-b30d-bda03246a0ab | -5.65307 | -60.23714 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5711e33b-700c-3c94-be19-06aafe212ff0 | -5.35787 | -56.03411 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fd33e04c-01c1-3169-9c0c-0c0271421f23 | -6.95486 | -59.73632 | 2026-09-06 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72c85d4f-0e6a-3470-8904-859ec3f7f977 | -5.35049 | -56.01691 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40fb74ec-5001-31a1-8cf0-4e12378e5727 | -5.14956 | -55.95409 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 805a5e72-dcf8-3174-84b4-8127cef465cb | -6.09093 | -55.59338 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba00ec08-88d1-316c-944f-44f922e0e5f4 | -4.92018 | -55.81342 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69db4c2a-f694-3c3e-aef5-a5ee8abc2c5f | -6.09176 | -55.58764 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 321e9199-97af-38a9-9fb8-7d8cbf731533 | -5.35379 | -56.02818 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d4143ac-fe73-3447-9365-10ba5d5b0f4e | -5.37159 | -56.04142 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 63586e08-264f-3f9d-8999-b9a53c2a45f4 | -5.34261 | -56.03741 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c16649e-816b-33b3-bddf-c3a4b0d3ac90 | -6.51604 | -58.29799 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea775a3b-3acd-38a6-bc9e-a6f004612b7b | -7.10663 | -56.5103 | 2026-09-06 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f626faac-eb6c-3180-b4de-1e8e10176b82 | -3.837 | -60.77386 | 2026-09-06 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f97df1e-77de-366c-ae70-e4703c29ea10 | -6.87033 | -55.61045 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 262e66fa-1d51-34e8-88e1-9cb90eb27872 | -5.27747 | -56.11639 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a325247d-893d-39dd-b62c-11d5bcae8996 | -8.50198 | -54.65461 | 2026-09-06 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b789fd9-5382-34c5-ab96-68fb21e5f0b1 | -5.34972 | -56.02224 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9770d2b-630f-30f3-a7b7-c11965d8b134 | -7.79397 | -70.04996 | 2026-09-06 05:42:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac4aedb4-dcf6-306f-b12c-f2720a0f6042 | -9.37026 | -70.4994 | 2026-09-06 05:44:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 376ff9d6-8197-3803-8a35-f9a570388d94 | -13.7906 | -51.63239 | 2026-09-06 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 074b6a99-6998-3240-aa18-c511fcc7bb38 | -9.13439 | -70.88697 | 2026-09-06 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3188b0e5-e35f-3d0f-ab9f-dd521abf2b34 | -9.13002 | -70.88616 | 2026-09-06 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09544c70-4e2b-3f25-ab90-bef50b2238be | -13.78347 | -51.6315 | 2026-09-06 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 425a6bdf-1f1d-349a-a61b-ba1ea27c1371 | -8.34045 | -70.56396 | 2026-09-06 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6ca3428-4c80-3d12-b6af-db09d6ca6ce1 | -10.05692 | -68.39305 | 2026-09-06 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79313fa5-3328-3ed1-badb-16164e8161d2 | -10.75529 | -60.71687 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe06a11b-3d81-312f-a0d1-0a86388c89a3 | -10.74007 | -60.76789 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e06b473-b21c-3804-8da4-2df8b865f5bc | -8.53448 | -70.46388 | 2026-09-06 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e4e7d3-1bd4-3739-a1c3-3a11f6766c5f | -9.13076 | -70.88188 | 2026-09-06 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5d7fbe9-ebfd-3adb-a5cc-378e07f81147 | -9.00805 | -65.42509 | 2026-09-06 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9756eebf-4944-3f9d-ac75-365476f0e4a2 | -10.75146 | -60.7163 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c9f6b966-dcf7-30fd-b818-38ca9be92ba6 | -10.75216 | -60.71154 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dc2bf32c-bd30-3872-ae03-9ef7abb9b490 | -9.37096 | -70.49543 | 2026-09-06 05:44:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86cd00db-d14d-3736-a27d-91902018e0b4 | -13.78276 | -51.63847 | 2026-09-06 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b187fc0f-d1e7-3dc6-9835-a92f9f41c199 | -10.74456 | -60.76377 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2178ae8-d192-3f3c-a16a-ec9038892af7 | -10.7432 | -60.77316 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ae48b54-6cab-385a-919c-607fe9dc635c | -10.06136 | -68.38926 | 2026-09-06 05:44:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28942b6b-e504-333d-a3a9-604cf40e5ceb | -9.50575 | -68.28012 | 2026-09-06 05:44:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6973ea6b-97da-38d6-b7e7-8b01b70acaa2 | -10.08495 | -58.54969 | 2026-09-06 05:44:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02698533-2c5e-3a47-b3c6-50216f008f9b | -8.30431 | -70.56616 | 2026-09-06 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d1c8788-0973-3d73-ba32-943bd8020154 | -8.98956 | -65.45477 | 2026-09-06 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b5e5c16-235b-3822-a5dc-cb16e5880704 | -10.75077 | -60.72107 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 174a9b03-070a-3374-9fe9-0476e34bf18e | -10.63192 | -58.81882 | 2026-09-06 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77734d32-3ca2-3954-aa6d-e963012ee4ba | -10.74388 | -60.76846 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73057c62-fe21-3934-b78c-440d0c8ceeca | -9.00415 | -65.42809 | 2026-09-06 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 574639a3-46b1-313a-8e0e-5acceeb5cca4 | -9.00748 | -65.42862 | 2026-09-06 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 056ba2cc-9536-3d2c-8b54-58e548f90d33 | -10.74764 | -60.71574 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3ca5e75b-ed40-3bb5-a9c8-3b57dcda20ff | -10.74695 | -60.72049 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f48513fa-70d4-3f21-9ae4-b7c9d2112784 | -9.5158 | -70.4874 | 2026-09-06 05:44:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2489ea2-d306-355e-897a-b32b85341469 | -10.74833 | -60.71098 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f2afe68e-bb34-3947-a9bc-ed41796f59cd | -10.17198 | -67.73428 | 2026-09-06 05:44:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbbb9ddf-5750-30de-bbf5-7301eb4c5a15 | -8.99014 | -65.45123 | 2026-09-06 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 259eadf0-3173-31c2-81cb-0fba0da09673 | -10.75598 | -60.71208 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74510a40-e4ed-3e05-b965-6ea6806e0b78 | -13.797 | -51.64022 | 2026-09-06 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c3905e7c-540c-3ffc-b71c-41bfecc4fdae | -13.7749 | -51.64481 | 2026-09-06 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| daa2119b-9a68-3f90-84cb-454599ce352f | -8.33745 | -70.56184 | 2026-09-06 05:44:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8817fe2-2e2d-3464-8f73-c2a8da464a84 | -13.76777 | -51.64415 | 2026-09-06 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1e696d1c-8bba-319a-a8ec-bd14edc2bb16 | -10.74314 | -60.71992 | 2026-09-06 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72c9d258-d82f-328b-ba08-b12171a2c08f | -13.35346 | -61.13316 | 2026-09-06 05:44:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9aef3726-367a-3334-8ffe-797a41cbb187 | -5.1423 | -56.2703 | 2026-09-06 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d95f1de5-336a-3c0c-b7b0-ffc83a4da3fc | -14.9246 | -44.6744 | 2026-09-06 05:50:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 59c4a282-5e23-33b5-bc0e-20707db236d2 | -5.3645 | -56.0447 | 2026-09-06 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 493c8af6-e0f1-3a22-95f9-9bac5e33eae0 | -5.3646 | -56.0249 | 2026-09-06 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 4bf40760-1df8-380b-b0aa-8778bc3bee5d | -14.9246 | -44.6744 | 2026-09-06 06:00:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e6a59b01-2ac6-3b09-b05c-ef6bfdecbfe9 | -5.1423 | -56.2703 | 2026-09-06 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| e2aff600-7e69-3907-9643-f851347bf47e | -5.3645 | -56.0447 | 2026-09-06 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 639433a3-09aa-396f-88b9-5231de4181db | -5.3646 | -56.0249 | 2026-09-06 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| ce676920-f949-340d-9b90-00bb2fcf2189 | -5.3646 | -56.0249 | 2026-09-06 06:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 921cb4cb-0122-35aa-a061-eb32a8005575 | -6.8944 | -62.956 | 2026-09-06 06:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 023c22d5-1a22-3dd0-9317-0db0db5fffa9 | -5.3645 | -56.0447 | 2026-09-06 06:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 37766243-f9fd-3776-8d15-02e6e8c57926 | -5.1423 | -56.2703 | 2026-09-06 06:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e545cbf9-7bc7-3994-aca5-e3dc0008c558 | -14.9246 | -44.6744 | 2026-09-06 06:20:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5a5cc38e-5b0c-373b-8b19-2b08e3e059ac | -5.3646 | -56.0249 | 2026-09-06 06:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 79297ed4-ff64-3ed3-bc84-1ff415acedbd | -6.876 | -62.9566 | 2026-09-06 06:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 404f3ace-6a11-37e1-8787-6da9baef4b5f | -6.8944 | -62.9748 | 2026-09-06 06:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| dac537cb-3058-3abb-9b5c-b792dd58b9be | -6.8944 | -62.956 | 2026-09-06 06:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| d72223ea-b144-36df-bfe1-1b6eb26021ac | -8.33998 | -70.56449 | 2026-09-06 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd2c625e-3204-369c-8c3d-21db33407db8 | -9.36897 | -70.50121 | 2026-09-06 06:27:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9a1be55-f460-3bc0-88a0-680f33b59012 | -8.73332 | -70.67468 | 2026-09-06 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d90b886-38b2-37b3-8c85-880bb853e01b | -8.73685 | -70.8109 | 2026-09-06 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b91c4ba2-c120-3c4b-9a43-7e9d75175c0c | -9.36962 | -70.49661 | 2026-09-06 06:27:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75edaedf-85a9-3257-8d5b-e96fc0a3eb70 | -7.83978 | -72.89796 | 2026-09-06 06:27:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f85c9106-1a35-3c25-9e40-a69ea2ac4cf3 | -7.79304 | -70.05057 | 2026-09-06 06:27:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 01fc99a3-dc70-358e-ab13-44633e04bd7e | -7.65018 | -67.39662 | 2026-09-06 06:27:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb7d9117-73ff-31ea-b009-b78e2619c69e | -8.3589 | -70.55823 | 2026-09-06 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12142b58-cd72-35d1-973d-abf748fbe5c4 | -9.3714 | -70.49847 | 2026-09-06 06:27:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 864c79c3-7e5e-3d0b-96fa-20b1ecbf862a | -8.97098 | -70.57939 | 2026-09-06 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9be8b805-0491-3352-aa12-52bf8266d004 | -9.51713 | -70.4884 | 2026-09-06 06:27:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d10899c5-afe1-32c2-bab4-112ed0948410 | -7.8387 | -73.0653 | 2026-09-06 06:27:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88c44ef6-95b2-3778-9e77-43f908eb2192 | -7.39317 | -72.80128 | 2026-09-06 06:27:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16efc188-6bc2-33ee-84e1-adbbbe2ca1de | -7.83907 | -72.90047 | 2026-09-06 06:27:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README34.md)
