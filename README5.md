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
| 83aa5a44-7e33-35d2-8d65-a5e7ff751b83 | -4.48216 | -47.67123 | 2025-09-05 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| da584887-c8a0-3a2a-bf36-886f1f30c247 | -5.56212 | -46.18734 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| dd997193-b00f-33b6-85c5-0a9d1cd75bb2 | -8.77741 | -49.62373 | 2025-09-05 00:33:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 122be8f6-ef68-3858-919a-a50cda5d886c | -9.07068 | -46.99197 | 2025-09-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 34f3572c-cea2-374e-b2da-9493de880981 | -7.72878 | -50.31937 | 2025-09-05 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b8137d42-ffac-358d-aff7-b0b2dde77803 | -8.01586 | -45.4361 | 2025-09-05 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a7f73bb1-5b57-38bb-8fd9-5d7921ce8d08 | -6.2683 | -53.43769 | 2025-09-05 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| a5c549c2-e3f0-3916-bd33-2c0f4f45f184 | -9.25 | -57.06866 | 2025-09-05 00:33:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| f73f506d-5e72-3a2a-b5bd-fd6efaceda04 | -6.21092 | -43.40271 | 2025-09-05 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5d3611b7-33b8-3e6b-97ec-813af53f44c7 | -6.87675 | -45.57901 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 8001d427-3cc1-34ca-b020-ddf5121415f3 | -9.07446 | -47.01882 | 2025-09-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 53e0bd18-bdad-344f-a4a3-0fdd12791094 | -6.01137 | -46.68354 | 2025-09-05 00:33:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 618081f0-bef0-39d3-8db0-42982e13d184 | -7.6726 | -48.74468 | 2025-09-05 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cef5d5e2-b28b-38a8-aa31-5ea698e8757d | -3.78867 | -44.13972 | 2025-09-05 00:33:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| e50618b1-ed66-3a14-bebc-b8446ce7c3b1 | -5.88203 | -45.57689 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 8098ef9c-ab0f-3232-ade3-229270771b27 | -6.59417 | -44.56113 | 2025-09-05 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 196bf78b-9c44-38c9-b271-c87f0c4b028a | -8.3487 | -48.29931 | 2025-09-05 00:33:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 45b07bc1-eb85-3cab-b86e-198e06611c9e | -6.62551 | -51.01216 | 2025-09-05 00:33:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 46895c27-b9bd-3a46-8fc6-6ef806a1e472 | -9.0732 | -47.00988 | 2025-09-05 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 33494c1c-4d24-3c40-b1f7-e7fcd48c3dfa | -7.44632 | -48.97908 | 2025-09-05 00:33:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f1d1a336-b2b5-3628-817d-7abfe05a746e | -2.43219 | -49.30967 | 2025-09-05 00:33:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 6f557786-7062-3e34-9dc7-0ccb828872d7 | -8.52568 | -51.32193 | 2025-09-05 00:33:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| ab6a7601-d5c9-3687-9675-7e4ed8d95aff | -6.59532 | -44.55447 | 2025-09-05 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 20d1cc36-a14c-370c-ad84-804ad1a096a9 | -6.67581 | -48.40814 | 2025-09-05 00:33:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c95e0601-c760-31dc-bbcc-4e013c326dec | -6.35599 | -47.09822 | 2025-09-05 00:33:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 67a105dd-242d-3a9c-9b56-ff9c1902cd9a | -6.12051 | -42.95379 | 2025-09-05 00:33:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| b521cb24-1400-3755-81a0-f61c7997505b | -4.68024 | -41.01242 | 2025-09-05 00:33:00 | TERRA_M-M | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| a4d522a2-89e4-3831-bffa-00c4a312ac31 | -7.69225 | -50.2618 | 2025-09-05 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 365c3326-620b-33ca-a1e7-f29989086a15 | -7.90013 | -45.30581 | 2025-09-05 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7274ce09-bbc5-3011-9423-a94f633074b5 | -5.72938 | -49.28907 | 2025-09-05 00:33:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 0c6f6b85-fe48-3409-9eac-46475ab997a7 | -6.02317 | -46.70122 | 2025-09-05 00:33:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| db1c07be-b6b1-3fbc-8ffb-cec67710ac8f | -6.55129 | -43.91383 | 2025-09-05 00:33:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d63c9676-0be4-33ee-a4c8-a781780bdaba | -9.062 | -50.44033 | 2025-09-05 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e6b628ec-474c-3baa-bf21-b7ff10441e8c | -7.69531 | -48.77826 | 2025-09-05 00:33:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f5888d89-6334-3033-80eb-34e78159047f | -6.81536 | -45.65852 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a0ccc9c7-5c3d-303f-b498-1d3d57aac02b | -6.68799 | -49.7715 | 2025-09-05 00:33:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 49ea1e25-523c-34c5-abfe-e102437dbf5e | -6.8833 | -45.5568 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 393b25e3-6cff-385c-a561-07ff90abe9e2 | -6.02183 | -46.69173 | 2025-09-05 00:33:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 34166a5d-cfec-3813-a8db-c3b6d25dffc4 | -2.78761 | -49.61909 | 2025-09-05 00:33:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| cf15dac5-c6e1-314d-88d0-9f9fa4cd4476 | -7.89057 | -45.30728 | 2025-09-05 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 239.5 |
| beaacba2-7e62-34bf-9913-675f70ab8675 | -5.62756 | -45.73045 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 5ef3c8b1-5ffc-3a63-b4fa-be72df17cd72 | -6.02715 | -43.71049 | 2025-09-05 00:33:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 104e2bc6-046e-33bc-a8e6-2079c37fa33a | -6.01272 | -46.69302 | 2025-09-05 00:33:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e380201d-0f39-342f-aa90-98ed84a85150 | -7.34497 | -46.2704 | 2025-09-05 00:33:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 85ac7d93-f5cd-3f49-9f39-6419016b43a5 | -2.55398 | -47.72981 | 2025-09-05 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 04d11b14-4b10-34a2-ba80-da23a42749bc | -6.68672 | -49.762 | 2025-09-05 00:33:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4de87692-b0ec-37d4-a1af-3fb3e1853f4c | -3.99727 | -47.37088 | 2025-09-05 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 47c8177a-f5a0-363a-9750-9e12b33ae325 | -8.52736 | -51.33463 | 2025-09-05 00:33:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c2d275b0-acee-34ea-a0c3-4a4f32b5b046 | -4.79672 | -47.22083 | 2025-09-05 00:33:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a2a3b879-19cc-348c-bbd0-7917cebc5390 | -8.9757 | -44.45019 | 2025-09-05 00:33:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| deafa824-cec2-344f-8afd-3efb4cdfe0f3 | -6.04341 | -45.99401 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 24e8dcfe-705b-3e91-b5ff-fd830ff349a5 | -6.99854 | -45.65008 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b57a4b79-99dc-3e18-ba0b-4e4a3bcfab75 | -7.89862 | -45.29519 | 2025-09-05 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 37d1e770-786a-324a-8617-b525c6ae78e9 | -6.025 | -43.69624 | 2025-09-05 00:33:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| cd1db6ff-d708-34e7-915e-3e99ddc78c79 | -8.99975 | -45.52893 | 2025-09-05 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b2c51aae-ca5a-35b7-ab7b-bb9fcf11cb00 | -6.29517 | -43.50488 | 2025-09-05 00:33:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 505a84e6-bccc-3f9a-92fe-7044147dcb1d | -6.58989 | -44.32044 | 2025-09-05 00:33:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9a2a6e89-7dd9-351a-b092-520c697d5b85 | -6.28197 | -53.45216 | 2025-09-05 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 99640cb0-5c11-3858-be14-36f118f960a6 | -5.0277 | -45.32975 | 2025-09-05 00:33:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 56fc261f-06b3-335e-9977-001c0e08f4c7 | -5.77282 | -47.21576 | 2025-09-05 00:33:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e7b9cf7f-377f-3e06-884e-0bce9d5ddb88 | -9.70574 | -51.06849 | 2025-09-05 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 219.1 |
| c028471b-bcf1-3aed-909d-40611086e94b | -2.34112 | -47.59336 | 2025-09-05 00:33:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bf45616d-7885-3760-9518-91d3473e8cbe | -7.69763 | -50.30241 | 2025-09-05 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0395d847-b732-3b8a-b028-80ba6b687179 | -8.89556 | -45.77258 | 2025-09-05 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fdab0683-deaf-374f-8478-c113268be100 | -8.11335 | -49.96922 | 2025-09-05 00:33:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ccd694dc-45be-3a87-babd-09bdffdbc12f | -7.76185 | -48.79065 | 2025-09-05 00:33:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9bfabece-71ff-38a5-a5dd-cce3a362c4d8 | -9.69631 | -51.06308 | 2025-09-05 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6c6bb45e-b556-3bd0-aec7-85e39fc48d58 | -6.67458 | -48.39929 | 2025-09-05 00:33:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 44ac82ea-0c11-3047-b99e-6f9a0d620d3a | -7.89105 | -45.24212 | 2025-09-05 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9ad22120-356a-3300-a0e8-38d07de238de | -5.73062 | -49.2981 | 2025-09-05 00:33:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 4db1d44e-45e1-3353-803e-87ec57ff73d0 | -6.59237 | -44.5491 | 2025-09-05 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 1a0d306f-79f8-38a9-bb37-742ab4389d0f | -6.23687 | -46.25879 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9581142e-fe17-3990-8b80-75edce852fee | -3.69458 | -49.57643 | 2025-09-05 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| efe5fbc0-ba8d-3971-b2be-4e35a5e480e6 | -6.00867 | -46.6646 | 2025-09-05 00:33:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 21839c5c-de41-3750-abac-5636c4e62673 | -6.21038 | -43.55324 | 2025-09-05 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bdda3684-66d4-326c-a787-cc68ee62ac4f | -9.38284 | -50.38412 | 2025-09-05 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c96783be-0f4b-36fc-829c-a1eb1d674b36 | -4.65897 | -46.45145 | 2025-09-05 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 815a974f-5db8-317c-926a-5f2648f9ce8e | -2.3748 | -47.63595 | 2025-09-05 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1be5038d-29d5-36d0-bc01-f315d0cdfc4c | -7.9036 | -45.23389 | 2025-09-05 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5387bd82-51f4-3431-8195-0333df683c14 | -5.79725 | -45.62792 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 98d40380-9c2c-3b05-a354-1c8a168ce6df | -6.05283 | -45.99268 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d9b1b182-2bc1-381a-ba1f-6ad6edbca5b1 | -5.57734 | -46.54268 | 2025-09-05 00:33:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da00189e-56e2-3b7b-8e21-4da8441b352a | -2.35018 | -47.5921 | 2025-09-05 00:33:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 700b2526-fdfe-3658-85e2-1af25526db27 | -2.38254 | -47.62539 | 2025-09-05 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| e61d9fd0-0083-3b1f-b807-baa943156f49 | -7.07716 | -46.20099 | 2025-09-05 00:33:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9a9dbb94-bd2d-3ce5-b17a-c00d7e759c2a | -4.27833 | -48.1906 | 2025-09-05 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 3e87cdca-df71-33cb-829f-4ae21e72af78 | -7.05616 | -50.86707 | 2025-09-05 00:33:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4493b77e-7509-3a99-b777-515dcb58a296 | -6.00361 | -46.69429 | 2025-09-05 00:33:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d23fb666-0d73-3c50-8a9b-17171622e48c | -6.27034 | -53.45364 | 2025-09-05 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 20b44234-29b5-3d78-8eae-f8680eddd033 | -7.59509 | -44.67575 | 2025-09-05 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 62eade56-4b76-387e-8bb9-0171b5c06e2f | -4.29889 | -48.07946 | 2025-09-05 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ecca0923-7e1c-3d61-a7fb-b3e21af396ec | -3.48931 | -48.95399 | 2025-09-05 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2105dc17-67a9-3fe8-b488-14928759e1c3 | -6.32973 | -43.95846 | 2025-09-05 00:33:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f720565b-51f3-398d-867c-4235910aa7d7 | -5.60816 | -45.02432 | 2025-09-05 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 207.9 |
| 0bd08b2e-7e88-3fc6-b758-465f3cd87bbe | -7.44545 | -46.13155 | 2025-09-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8fc3fbb3-d678-360f-990c-a865fdc7e85b | -8.07838 | -45.33163 | 2025-09-05 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dead2c98-3be8-38e8-847e-e74eb5581b0e | -3.48809 | -48.94521 | 2025-09-05 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 002ccbf5-4d1b-331a-b25a-2b038f2b2d8b | -6.59705 | -44.56654 | 2025-09-05 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| d2a417cb-2a62-3e67-8823-9c86b526eacd | -9.70726 | -51.08066 | 2025-09-05 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| b7b80086-cfb3-3129-bda7-bc2904510b3b | -6.34704 | -47.09952 | 2025-09-05 00:33:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README6.md)
