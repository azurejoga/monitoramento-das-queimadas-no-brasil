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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5f9f8d6-7c16-38a1-aa88-7b1bfa7a3ee8 | -10.51322 | -51.14363 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25018c29-67ce-31c2-b39c-376bfe06563f | -10.50907 | -51.14298 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d56ae6fe-1faa-32b7-b7de-70289d064a60 | -10.50429 | -51.14601 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 638e5368-8b25-3acb-8b36-3e9d583408c3 | -10.49949 | -51.14915 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32e4eacb-caff-3c6e-80b9-29455bdd6d8f | -10.49055 | -51.15151 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| af9d206a-ad80-3875-826c-b14755ed98d1 | -10.4899 | -51.15522 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 20017c4f-a508-30e7-9385-cfb8da0af511 | -10.48574 | -51.15461 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2648f19-7023-360b-a165-2844c0255ab7 | -10.47694 | -51.18066 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3270f11c-73b3-3e8d-a0ef-fe8bd1122f25 | -10.47633 | -51.18417 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 496241f8-0fae-3efb-8f45-1a5a5f52519a | -10.47215 | -51.18364 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2dd27740-bf39-329c-9348-c26503dcd5e1 | -10.45531 | -50.79795 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05c48a05-3553-357b-a179-abc1db4338a6 | -10.45468 | -50.80159 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 672cb4e6-0d6f-3978-ac42-85ed6ca251e8 | -10.4525 | -50.79002 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0eec2f3c-90f2-3cca-a1f2-1f2c1195c107 | -10.45125 | -50.79728 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72f08074-9d7b-361d-82dc-7865457278d4 | -11.12712 | -50.84093 | 2024-09-28 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aaf7a374-ee98-36b8-853a-8921ce052167 | -11.1264 | -50.83704 | 2024-09-28 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4394528-f120-3eae-8c68-2998036179de | -11.12579 | -50.8406 | 2024-09-28 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea9112ec-a422-3edb-82d6-3f43b7adbebd | -11.10259 | -50.80717 | 2024-09-28 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42701477-9242-3e64-a73c-596105b78fc9 | -11.01526 | -51.33622 | 2024-09-28 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c5994a5-c505-3306-8af5-b6c68a0f4ade | -11.01459 | -51.34006 | 2024-09-28 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af9fe6bf-3dce-3e9c-adc2-dc1fb631baaa | -13.63933 | -51.47231 | 2024-09-28 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e74a6b8e-f19f-3515-af8b-243e3b74c0e8 | -13.63597 | -51.46797 | 2024-09-28 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b4caa436-62c1-3914-b10c-63c3e0b87c84 | -13.63532 | -51.47157 | 2024-09-28 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0231ff31-bf4f-373f-87c1-2406571b8220 | -13.63467 | -51.47515 | 2024-09-28 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9b223e9-741a-35b9-b13c-846c0997a98a | -13.63402 | -51.47875 | 2024-09-28 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 701ff82c-5d1b-3e9d-ace3-274733d13613 | -13.63066 | -51.47442 | 2024-09-28 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99e0aa57-4468-3e3f-a040-b1f025309a05 | -13.63 | -51.47801 | 2024-09-28 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 505d4565-4255-3b68-96ec-6d54bfc0696c | -13.37187 | -51.30045 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7d39d48-3aa5-3264-ad21-b5d7da30dbc7 | -13.30825 | -51.34746 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cda46b54-82ae-33fb-a20d-b172173a0463 | -13.30425 | -51.34671 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b1dec72-90ae-3db9-bc09-7af207657357 | -13.25122 | -51.29663 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5d09d09f-6d0f-32ec-afe2-8a6df744906f | -13.23365 | -51.25689 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e3dd6093-c0ba-3281-95c4-297bbfdfeb75 | -13.23301 | -51.26041 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f2d13125-794e-3944-9f84-653ce37b3801 | -13.23238 | -51.26394 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5c0d5308-6ec7-35b1-af5c-0a804d2f75a9 | -13.23174 | -51.26748 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c5209fe-5298-3c6f-a97f-32cf3c8b0044 | -13.23161 | -51.2564 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd75a94d-e56f-3a07-8f70-1f9b5c621ebb | -13.2311 | -51.27102 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57c52b0d-6e74-3089-8add-6e91f053c798 | -13.23099 | -51.25994 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e5b41f3b-5d81-36d7-8973-d33a438b8b1b | -13.23046 | -51.27456 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a776696a-8bff-3394-b9a8-df6799910a24 | -13.23038 | -51.26348 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 712ea5c0-05c3-3cfc-9050-4c6148df9314 | -13.22982 | -51.27809 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 987bf35d-af3c-34ec-bbf4-029618e3ca1f | -13.22903 | -51.25969 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6a686da8-8e3b-3c5e-b3b0-4595553a32d8 | -13.22762 | -51.25568 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1b82e27-1ed3-3225-898a-3d5d8e94a897 | -13.22701 | -51.25921 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8aee3804-657d-31c6-b083-c862cb1c376e | -13.22364 | -51.25495 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 592f6bf5-79d8-3dd3-a190-0965202bad61 | -13.21292 | -51.2457 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0f79c42e-8ecf-3b7c-ac0e-e41b8838e525 | -13.2123 | -51.24923 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 99d3817d-eec5-3135-b658-7b229db2fd97 | -13.20893 | -51.24497 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 5f69a12f-83f0-34a3-8ae0-fb8ed5301ced | -13.20832 | -51.2485 | 2024-09-28 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4af75976-8283-33d7-871b-f3b093bc0615 | -8.3672 | -51.74051 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9275e89c-5a42-3484-88ea-c198a3a06a25 | -8.35497 | -51.74033 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3b79220-7394-3901-90c6-334c0bb2d4ff | -8.3505 | -51.73963 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bf90821-4acd-33b7-8b6d-91b709afb15e | -8.34856 | -51.74194 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9132938d-0941-38c9-a471-aeb500ce9284 | -8.34603 | -51.73891 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79d9f117-3241-3b07-afa1-c91b1ec15fd9 | -8.34076 | -51.74283 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7b3f5ef-9ada-306e-b457-c0da37a9a195 | -8.32737 | -51.74053 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e28b6d8f-9ec4-3b1e-9540-1aa5cd7b528e | -9.68831 | -53.49993 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8197f3d7-7dc7-34d1-aa7b-1f8f20c2e28b | -9.68682 | -53.49784 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d6c3b36-e34a-3b5e-b67c-c211f2dc60c4 | -9.68584 | -53.50335 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 206eff16-d6af-3486-bbcf-7fb874a8ffd8 | -9.68341 | -53.499 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8114a66d-56fc-3aa4-ac34-15f202af0168 | -9.67897 | -53.51354 | 2024-09-28 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37c20f91-f101-3c71-8a90-fa349aca4f6f | -9.58786 | -53.30147 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 071e7d66-ea77-3ab8-9fb8-10e94f59dd8f | -9.58599 | -53.30298 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c84a632c-f8a1-33e2-a1d3-8b94530601c3 | -9.58301 | -53.30055 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b338d60-f19f-38de-bb24-bbb06eb56523 | -9.57025 | -53.42884 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 162bda32-fe1e-37c9-b884-02734fdb724d | -12.8637 | -54.00961 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aace6b5e-3278-3d05-9c8f-988a1b9a632c | -12.8589 | -54.00871 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb760d25-29a0-3394-a2e1-808e76d73c0f | -12.83016 | -54.00691 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 32d6dfc6-8d7f-3a38-9687-622a0a980dcd | -12.82907 | -54.00853 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d3ebcec-1c35-3e0f-9f69-a460af406718 | -12.82634 | -54.00068 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5cb24e35-5d91-37c4-badb-0b18cd3b3681 | -12.8253 | -54.0023 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e086ba57-51c1-3c77-bc76-1abe369fb717 | -12.82154 | -53.99973 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8ed3fe17-bd44-3e63-b3ec-ad321ad2f2cc | -12.81674 | -53.99879 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 579d7c83-67c9-3cf7-9711-1e391fb7d208 | -12.79554 | -54.00578 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c0d6dd00-d7cf-36e1-bca8-ef804b4d60f1 | -12.79455 | -54.01109 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f0f691a6-ec80-3c23-ab64-b29824b89fbb | -12.79153 | -54.02721 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd159876-2eee-399b-8c97-93370d3ff484 | -12.79074 | -54.00485 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7615be49-8d23-3bdc-85aa-4a169dc7f851 | -12.78975 | -54.01015 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d088490b-db55-3ac1-8453-526d785f7692 | -12.78672 | -54.02628 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 060bd911-1b99-3385-9764-1606858ec8ce | -12.78394 | -54.01456 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| af0de1e7-ce60-3290-b68f-23d7c71133e7 | -12.78293 | -54.01994 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a40c4f17-cb6c-34c1-8f11-4a87ffec4494 | -12.78191 | -54.02534 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b166780-cb6e-3b8c-ad25-9d49019e0dc2 | -12.7771 | -54.02442 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7f57da51-558b-3ae7-8d31-0c417f0e943c | -12.77608 | -54.02985 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eaccbde5-f394-3210-b999-e83126a77cb3 | -12.77229 | -54.02349 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f64c14f7-e26b-35e8-a8e4-09510be728e7 | -12.76748 | -54.02257 | 2024-09-28 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f6081d4e-40e2-3910-9d7f-bf36c786573b | -12.59333 | -53.15766 | 2024-09-28 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a76d7c5b-2ab8-3111-8408-337b68cf3116 | -12.58422 | -53.15592 | 2024-09-28 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c8e978e-0dad-3c04-834c-52190f58b522 | -12.5317 | -53.1583 | 2024-09-28 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e065e9b-cf54-3342-a75d-506a53bf739d | -12.52626 | -53.16222 | 2024-09-28 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbc0d501-abf3-337c-9c72-a21f15b5eabe | -12.5245 | -53.17184 | 2024-09-28 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4dff6a6-177b-356c-8054-776525085c9d | -12.52082 | -53.16617 | 2024-09-28 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64e74955-8495-31cb-ad92-fd137491b15b | -12.51994 | -53.17099 | 2024-09-28 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cfcded1-e751-3055-aae8-58b32644424d | -14.77841 | -53.85302 | 2024-09-28 04:21:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e07beb41-9841-33c6-91d7-b7408b9e2fa1 | -14.77745 | -53.8581 | 2024-09-28 04:21:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bcc95fba-3fce-3cbe-b0f7-b8ed8dba3e23 | -14.2892 | -53.38383 | 2024-09-28 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d17118da-ff5c-3c10-a310-ed9ea35c22fc | -15.4895 | -53.38014 | 2024-09-28 04:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce9e1cae-c1df-351f-98a3-9edfb8e11476 | -15.48869 | -53.38441 | 2024-09-28 04:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48b31546-97f5-3fa7-a9c3-b3ac645603bc | -15.48512 | -53.37922 | 2024-09-28 04:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 657480e8-4584-3706-9d75-64555e3ee1be | -8.71473 | -54.8075 | 2024-09-28 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README57.md)
