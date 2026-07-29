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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5051228c-63c2-3280-bc00-869f3eb3ba1a | -13.1331 | -51.3238 | 2026-07-29 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| fa994745-b272-3fc3-9f00-146b5848dc25 | -18.0623 | -51.2843 | 2026-07-29 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 835501b2-e3c1-3f81-9e9f-17264c0a1994 | -10.342 | -49.7613 | 2026-07-29 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2feb4fce-e910-3276-a8d2-76c75806160b | -7.341 | -45.8602 | 2026-07-29 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| c613603e-1ad6-3b08-ac5f-2ac79165790c | -12.3626 | -63.4436 | 2026-07-29 00:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| e335ba45-5019-398b-906a-93b124f3259c | -7.36 | -45.8361 | 2026-07-29 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 9aee1871-b395-3b77-a6fb-ff2e37ad1113 | -18.0424 | -51.2877 | 2026-07-29 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 4bbf010f-3b55-3b4b-a4ad-3bd94862365c | -18.0419 | -51.3097 | 2026-07-29 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4031dab8-5cdf-345b-9da6-b3992566a09d | -7.3598 | -45.8586 | 2026-07-29 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 8a9c3182-c2b9-369d-b706-09db8bf52648 | -18.0619 | -51.3063 | 2026-07-29 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e7636012-b27d-31c0-b967-dfd82809d441 | -7.3413 | -45.8377 | 2026-07-29 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 273ad734-33e4-3e71-b207-3f20d21a7c69 | -13.1334 | -51.3024 | 2026-07-29 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 2dff039c-0ca3-33db-9eca-71f455fe4444 | -6.8708 | -46.0126 | 2026-07-29 00:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| f2306cf8-8cd0-363f-9b87-eef02994f029 | -14.199 | -51.9122 | 2026-07-29 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b1ba8bee-d20e-39f2-a9d4-b4c91d6f84cc | -7.341 | -45.8602 | 2026-07-29 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 166.6 |
| cb9d38b7-865d-33b5-8f0e-b671c74a5333 | -7.36 | -45.8361 | 2026-07-29 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| efbc0cd0-00b7-38ec-8290-707de33fb583 | -18.0419 | -51.3097 | 2026-07-29 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 6a443f39-e5c2-35df-9355-aff4223fc501 | -18.0623 | -51.2843 | 2026-07-29 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 132.3 |
| f3af71b0-053e-343a-a9b1-635eed6a3800 | -3.6916 | -47.6411 | 2026-07-29 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2be274a9-de72-331c-9f42-dea1b9b15915 | -18.0424 | -51.2877 | 2026-07-29 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 5940ea9b-c34e-39c2-af75-e776fcf8cd74 | -7.3413 | -45.8377 | 2026-07-29 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 218.8 |
| a1126f26-807b-3ba7-a9c4-534e25c30ea7 | -18.0619 | -51.3063 | 2026-07-29 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9b458e15-9f37-38ae-ae69-67db4086996b | -6.8708 | -46.0126 | 2026-07-29 00:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4f10eb10-1218-39e5-9aa5-957917fe2696 | -6.8895 | -46.011 | 2026-07-29 00:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| fb053b58-92c0-3db3-9ddb-27ed16a82f09 | -7.34 | -45.85 | 2026-07-29 00:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a5f1a4d-8358-3797-bf2f-36a707ee8940 | -18.0623 | -51.2843 | 2026-07-29 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| d7d1f961-b7fa-3447-b7a7-4b0523ff7dfe | -10.9397 | -43.0593 | 2026-07-29 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 2ff1b8fe-2ff9-31aa-9f62-2983d948e391 | -18.0619 | -51.3063 | 2026-07-29 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 0741c34b-d07e-398c-b63f-a09f54c77580 | -7.341 | -45.8602 | 2026-07-29 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 207.4 |
| c00d99af-9f33-3e3c-a7c3-4ddf8a841fb6 | -6.8895 | -46.011 | 2026-07-29 00:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 3ce5b872-c537-34e2-8293-12af92717455 | -18.0424 | -51.2877 | 2026-07-29 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| bdc23b59-ad34-358c-bad6-b516ce4cd70e | -14.199 | -51.9122 | 2026-07-29 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| a4ddfbc3-1b4d-3264-9378-62dfa8bc6421 | -7.3413 | -45.8377 | 2026-07-29 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 283.6 |
| f111a5be-0674-35ec-8500-ae3186732919 | -13.1526 | -51.3 | 2026-07-29 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a2f3b7cf-fe9b-3d99-8be9-152429cc6f22 | -13.1334 | -51.3024 | 2026-07-29 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 37360242-1732-337b-8c71-727b73a78278 | -6.8708 | -46.0126 | 2026-07-29 00:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| a2753891-daec-37c3-aa54-43ff55a69eac | -18.0419 | -51.3097 | 2026-07-29 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 5b235331-f9c5-303f-951b-236285f9b2e7 | -13.1331 | -51.3238 | 2026-07-29 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e7e32cb4-6084-3d05-b35b-4121dea21297 | -7.36 | -45.8361 | 2026-07-29 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 793b7596-2b2a-37d2-8751-a481060f85ea | -13.1523 | -51.3214 | 2026-07-29 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| bf32b99d-08d0-398b-932e-9954d33716e6 | -6.8708 | -46.0126 | 2026-07-29 00:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 0b9ccde4-c595-3820-b6fa-0a078b116fee | -18.7999 | -51.2638 | 2026-07-29 00:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d0445bba-66ad-3f3d-a83c-0f6eade5a69c | -7.3598 | -45.8586 | 2026-07-29 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| bb52a9bd-59d0-3bf2-bbee-18530f165afe | -18.8004 | -51.2417 | 2026-07-29 00:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 9ebe342f-d43f-3199-a10c-63618314a75d | -10.9397 | -43.0593 | 2026-07-29 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f7cce457-84fc-3de2-9028-3a01a762d226 | -7.3225 | -45.8394 | 2026-07-29 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 61ede698-3cfe-35ce-8141-5014fb399cf5 | -13.1334 | -51.3024 | 2026-07-29 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 5381a0d1-14ad-3a79-bc68-b45c01ab553d | -13.1331 | -51.3238 | 2026-07-29 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 850ca293-3401-3d26-a21e-4b0b6c174b0a | -18.0623 | -51.2843 | 2026-07-29 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 11b76f27-ae93-3c04-831d-391a2936d38f | -14.199 | -51.9122 | 2026-07-29 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 83f89b02-1415-3eb4-8287-94f8389f8615 | -13.1526 | -51.3 | 2026-07-29 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 25077be8-76bc-392b-a1d3-d0d0cff7e44e | -7.341 | -45.8602 | 2026-07-29 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 160.3 |
| c350b254-53b2-34aa-b756-fe2201f61e36 | -7.3413 | -45.8377 | 2026-07-29 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 295.2 |
| 3c0b1d69-fd87-3040-abbd-18e966dd89f6 | -7.36 | -45.8361 | 2026-07-29 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| be0001bd-b827-34c1-a738-10b3d8513d1f | -13.1523 | -51.3214 | 2026-07-29 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| ec5a9b90-169e-30ab-947b-ebab205b414f | -3.6731 | -47.6418 | 2026-07-29 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 19e75d3f-55f1-3f76-b451-e85b27b2a017 | -10.3236 | -49.7202 | 2026-07-29 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 149.9 |
| a977355b-6ec8-3087-adb5-08cb025e82c4 | -15.4243 | -49.5702 | 2026-07-29 00:40:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b6a52537-3d27-3893-a554-bf07182afd14 | -7.3598 | -45.8586 | 2026-07-29 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 78798444-8d5d-351a-bacc-7e3f7bcd69f6 | -10.3234 | -49.7418 | 2026-07-29 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 5455e6a8-7f93-3415-bc34-7e4385b3c728 | -14.199 | -51.9122 | 2026-07-29 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| dbce004c-4fca-3464-9673-c1f99991437e | -18.8205 | -51.2381 | 2026-07-29 00:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 836d007b-5ed6-3ccd-91b0-e76259bfd380 | -15.4434 | -49.5892 | 2026-07-29 00:40:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 7422fbe2-0bca-3a6e-baae-14f0d1bc4c52 | -7.3413 | -45.8377 | 2026-07-29 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 285.5 |
| 8568a56c-a1ba-3392-a2ef-7af66ed6ac00 | -15.4438 | -49.5671 | 2026-07-29 00:40:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| bfaf3200-256b-3d52-8ba7-c00d17f047b4 | -10.3612 | -49.7378 | 2026-07-29 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b9e46bdf-252c-332d-80a8-97187c2e37d2 | -10.9205 | -43.0622 | 2026-07-29 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 0aac4ec1-c3dc-3271-9ede-4f6d3788702f | -13.1331 | -51.3238 | 2026-07-29 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f1012f64-9bef-31ae-9dad-5a189873f204 | -7.36 | -45.8361 | 2026-07-29 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 71ed4c02-958f-3fa1-9118-00bb1c1750cd | -10.342 | -49.7613 | 2026-07-29 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 4f51d163-1d70-3c8d-9b77-22a451346a7f | -18.8004 | -51.2417 | 2026-07-29 00:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 362c2ce9-77fe-344d-af75-79af69800d9c | -4.3774 | -47.7627 | 2026-07-29 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 85bab4ee-46c6-37ce-987a-4e330289d8a2 | -6.8708 | -46.0126 | 2026-07-29 00:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ea923490-d890-3f89-aaaf-5ba60408c393 | -13.1526 | -51.3 | 2026-07-29 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 0245b18f-234c-3d9d-b27e-e11e47d2fd49 | -3.6916 | -47.6411 | 2026-07-29 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 50f2c811-0929-3a8d-8605-45220bb58b68 | -10.3423 | -49.7398 | 2026-07-29 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 294.2 |
| 34855b17-b511-3815-a710-9eb9d0de3b9f | -10.3426 | -49.7183 | 2026-07-29 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 85969690-ca92-31ff-ac77-c3dbd57bc0f1 | -18.82 | -51.2602 | 2026-07-29 00:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 593a5ff3-78bf-391c-892b-97c290c72245 | -13.1334 | -51.3024 | 2026-07-29 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| f0139e84-faf4-3037-8103-dc2263e26822 | -7.341 | -45.8602 | 2026-07-29 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| b7c0a25d-5b03-3d80-ad05-057ad3ede132 | -18.7999 | -51.2638 | 2026-07-29 00:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 732cad40-1d4a-30bb-bef0-4411809ef890 | -13.1334 | -51.3024 | 2026-07-29 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 4469a335-6f5d-348f-928f-38a3df377661 | -7.3598 | -45.8586 | 2026-07-29 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 346706be-fa5e-38fd-a183-190718e0a797 | -13.1331 | -51.3238 | 2026-07-29 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| f876e3fb-08fe-38a4-8fd9-bc7d971cba6a | -21.9726 | -56.031 | 2026-07-29 00:50:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 26b29b45-e8a9-3984-ae24-8b71cf8129b4 | -21.9731 | -56.0095 | 2026-07-29 00:50:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c2dbceec-1015-3ede-bc24-2db67b79dde6 | -10.9397 | -43.0593 | 2026-07-29 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9df3989a-1e4c-35d6-bad8-6f155a5ad1a6 | -7.341 | -45.8602 | 2026-07-29 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| a36d9d66-7cb0-3841-8507-44a842158aee | -18.7999 | -51.2638 | 2026-07-29 00:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 3c5c8135-bb7c-3683-a48c-5c6646a44daa | -18.8004 | -51.2417 | 2026-07-29 00:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 15565563-e144-319c-901f-68cfd6257e96 | -7.36 | -45.8361 | 2026-07-29 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 2a9f2f4c-2b0c-388e-a199-01eef9ed41ff | -7.3413 | -45.8377 | 2026-07-29 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 230.2 |
| d4682212-0877-308c-a803-d7b1a34a49fa | -10.9205 | -43.0622 | 2026-07-29 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4be46887-de36-3e99-9d1f-c8debba1b673 | -6.8708 | -46.0126 | 2026-07-29 00:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 364e7739-2d3e-3ca7-b3d0-5f56d17a13f6 | -14.199 | -51.9122 | 2026-07-29 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5d520acc-65ae-398f-ade4-c6c534f2ccf3 | -10.3423 | -49.7398 | 2026-07-29 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 77bad21c-2d3f-3580-85a4-6e5d089044f9 | -18.7999 | -51.2638 | 2026-07-29 01:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 103.1 |
| dfd46579-3852-31e2-96fd-a32dd571c2e6 | -4.3588 | -47.7636 | 2026-07-29 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 66e873d2-08c6-3a26-bbbf-38deda48aa14 | -10.3426 | -49.7183 | 2026-07-29 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| da9649f0-6ad7-3d7d-99a4-60517a8245c0 | -7.341 | -45.8602 | 2026-07-29 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |


[Clique aqui para ver as próximas entradas](README2.md)
