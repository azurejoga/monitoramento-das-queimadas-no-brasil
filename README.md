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
| ca9c4686-4324-33d7-abdc-699203c8962a | -16.6984 | -51.3576 | 2026-08-07 00:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 79be03b4-35eb-3ef0-806e-cf7bc9d65493 | -11.1835 | -54.8584 | 2026-08-07 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| b5cb967a-b54b-3829-8a51-bd7113a9ceea | -11.1443 | -44.4865 | 2026-08-07 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| a9d6b0cd-af47-3094-8682-ccce61d27fbb | -11.1649 | -54.8397 | 2026-08-07 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| a803242a-543c-35fc-9376-0ec04edb2ac1 | -7.09 | -46.5526 | 2026-08-07 00:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 264b9e01-5d38-340c-b885-be512c5b0b08 | -11.1635 | -44.4838 | 2026-08-07 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8b0a630c-360b-34a3-9766-b5ecd575b874 | -15.1169 | -53.5898 | 2026-08-07 00:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| eeca67be-b814-3cde-a818-967b56ccebb5 | -11.1838 | -54.838 | 2026-08-07 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| db5a555d-3449-3295-a84f-53ef5dd96c64 | -22.933701 | -43.275398 | 2026-08-07 00:07:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a887e730-864c-37a9-a653-3c4192377166 | -15.8663 | -43.589901 | 2026-08-07 00:07:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 243807f9-4339-3dd2-b221-7ff47286cfed | -11.1854 | -54.828201 | 2026-08-07 00:07:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38480c8b-5828-30b3-a771-2d268b18a923 | -4.2627 | -48.192001 | 2026-08-07 00:07:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fbb8feb-c7bc-336f-b0f2-dece517871c8 | -11.0835 | -47.787601 | 2026-08-07 00:07:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51d17228-5578-3184-aeb1-7411c9092beb | -10.6069 | -52.2146 | 2026-08-07 00:07:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26c269ea-7c92-3cb4-8e1c-c133e34c3cc2 | -5.1069 | -49.372101 | 2026-08-07 00:07:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 688ddf64-908a-3ec6-98b2-dfcdcdc160d3 | -13.9637 | -47.362701 | 2026-08-07 00:07:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 876251c3-8747-3194-b918-056c935320f7 | -17.729401 | -40.237499 | 2026-08-07 00:07:00 | METOP-B | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 218644bc-ad5e-33ba-82c4-3b1a31ad5de6 | -12.5848 | -46.905399 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffd7706b-2a7f-340b-8e8c-b3ab29afdfb6 | -15.5229 | -49.997002 | 2026-08-07 00:07:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b3e259d-862c-3031-940b-e9b070b08193 | -12.5719 | -46.8936 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d733b119-aaff-35aa-9089-0bae22e507f5 | -8.5597 | -45.362301 | 2026-08-07 00:07:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7f8438b3-5a6c-375c-81b3-e10a0a3fc7c8 | -2.0846 | -54.426701 | 2026-08-07 00:07:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c18b56c-9dfe-3f64-9fe2-b34619218703 | -8.9717 | -48.1506 | 2026-08-07 00:07:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d2904d2-382f-3a73-996f-b9d1d51cf29c | -4.4579 | -47.917999 | 2026-08-07 00:07:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e39da3d-dc47-3ac4-b44a-cadbdb514486 | -11.4552 | -44.551899 | 2026-08-07 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e99cb22d-b308-3fc9-aa73-5e4b576a153c | -17.732401 | -40.249599 | 2026-08-07 00:07:00 | METOP-B | SERRA DOS AIMORÉS | MINAS GERAIS | Brasil | 3166709 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d46619a8-9a86-3f5b-a9f6-af3a7065787a | -15.8683 | -43.598301 | 2026-08-07 00:07:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3ab1c55b-c9cd-351a-89f0-f12b78862375 | -6.0099 | -51.062901 | 2026-08-07 00:07:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f5152d2-7c10-34eb-b6d6-4dcd1d1412f2 | -13.941 | -47.3531 | 2026-08-07 00:07:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be263e15-35ed-34c9-ad11-f4fd09f6739a | -6.6513 | -56.3866 | 2026-08-07 00:07:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b58b79e7-4e32-39ad-8b09-c87aa144dc9b | -6.4744 | -42.218201 | 2026-08-07 00:07:00 | METOP-B | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bc92f0ca-0328-3b8c-af49-8723c761b7be | -17.7227 | -40.2523 | 2026-08-07 00:07:00 | METOP-B | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db509cb7-ecdf-3d7b-b34a-cfa80af6cd3f | -8.5578 | -45.354198 | 2026-08-07 00:07:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f5626d4a-2f28-39eb-9ad3-d5e5b6ebe5f5 | -2.0869 | -54.4366 | 2026-08-07 00:07:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68606280-414a-3155-a809-2284d296d0b8 | -12.3495 | -48.2057 | 2026-08-07 00:07:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57a4bc3d-6f75-3854-abdb-d799e0673d5a | -4.3698 | -47.757702 | 2026-08-07 00:07:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 402b7dd7-bd1f-3130-9660-07c4b5141b5a | -12.57 | -46.931099 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2e43402-4359-3be8-8c4e-8212e42c332e | -15.108 | -53.584599 | 2026-08-07 00:07:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fbaee611-547d-3c02-ac74-db283c6b963c | -7.1509 | -48.937199 | 2026-08-07 00:07:00 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 646b6ac7-ac5c-3e50-811f-2f12b48a6e1c | -17.7197 | -40.2402 | 2026-08-07 00:07:00 | METOP-B | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b367ef68-39b7-32a7-82cf-01bcad7be419 | -12.5684 | -46.924099 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e712f916-2e11-3a17-a3f9-0341a0625e35 | -7.2716 | -50.123199 | 2026-08-07 00:07:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28d3e06b-8ba0-3432-9b10-e93d1af00553 | -4.4547 | -47.903801 | 2026-08-07 00:07:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33589b8b-f71f-3102-b2ca-966784bd34c5 | -7.0891 | -46.536598 | 2026-08-07 00:07:00 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69a94915-519d-309a-b69c-daaa7d7b109f | -22.5336 | -43.5606 | 2026-08-07 00:07:00 | METOP-B | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2c5aef0-0fa7-321b-8116-d6c0d0fccfb4 | -22.935499 | -43.283199 | 2026-08-07 00:07:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1794b174-13a9-3aa7-9ecd-870f098500d2 | -20.620701 | -43.956799 | 2026-08-07 00:07:00 | METOP-B | SÃO BRÁS DO SUAÇUÍ | MINAS GERAIS | Brasil | 3160900 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6f7f40ce-85b1-30e8-8303-de94c8661b61 | -11.4572 | -44.5602 | 2026-08-07 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07e558c2-2716-3787-8e80-978ab911d83e | -16.3974 | -49.9244 | 2026-08-07 00:07:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 86f74879-407c-3cf2-9588-de9641691eef | -13.8134 | -53.7048 | 2026-08-07 00:07:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 896c73cc-3ec4-3f15-bfa1-09aeb7e6cf11 | -18.478901 | -47.233398 | 2026-08-07 00:07:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 98d0a67f-9df5-3774-892c-2d9280be012e | -12.3312 | -53.153 | 2026-08-07 00:07:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c6811a1-3223-37a3-993c-01618acdd399 | -20.816601 | -44.598202 | 2026-08-07 00:07:00 | METOP-B | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c6319d2a-e7c4-3b75-82ad-f3875c5b01d2 | -4.3731 | -47.772099 | 2026-08-07 00:07:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c91862b-63be-387c-986c-0f4eb4401463 | -6.8611 | -45.995499 | 2026-08-07 00:07:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a54a2cb-0475-3b45-848e-9b1efb314f73 | -11.1501 | -44.483501 | 2026-08-07 00:07:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d272335-d6c6-31c4-be2b-db4cd2982f2a | -16.6961 | -51.360699 | 2026-08-07 00:07:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3ff91434-8e7c-3cd7-9780-f5d8007d1017 | -22.5319 | -43.552898 | 2026-08-07 00:07:00 | METOP-B | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5c5aa0e3-eec4-3320-a50f-ff37810b15e7 | -7.9899 | -47.273602 | 2026-08-07 00:07:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7913a199-3f26-380d-a11b-4c71aa6f3bcb | -13.9652 | -47.369801 | 2026-08-07 00:07:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 394ca6cd-0e62-3d97-af68-7469bca32437 | -16.3634 | -53.747601 | 2026-08-07 00:07:00 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd6fe28-646a-346b-9f27-958a395bcb69 | -4.3715 | -47.7649 | 2026-08-07 00:07:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3e21d59-a908-3a68-b64a-4905b61e1792 | -5.9815 | -52.144001 | 2026-08-07 00:07:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0984b29-714b-3bb3-b996-5665197f3cfa | -6.5384 | -56.525902 | 2026-08-07 00:07:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fa45a39-f77d-3b6a-8fe9-762e29d24bc0 | -15.926 | -43.9758 | 2026-08-07 00:07:00 | METOP-B | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b47af311-ce6d-3f4c-a232-4589ac2b37c0 | -6.7025 | -58.905602 | 2026-08-07 00:07:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1089f88-48b4-3e06-9d37-754cbeafa6c1 | -6.8513 | -45.997799 | 2026-08-07 00:07:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7bfcb3-e04f-3f62-9fdc-8fca16dd80b1 | -8.4728 | -49.557301 | 2026-08-07 00:07:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3fe4f69-89cd-3c79-ab0f-0a9b76ea083c | -4.2611 | -48.185001 | 2026-08-07 00:07:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7cf8d09-779c-339c-b248-cee6c6e3e26e | -9.8199 | -45.2365 | 2026-08-07 00:07:00 | METOP-B | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dc395288-f589-3368-902d-531fccfa1162 | -14.4789 | -47.976501 | 2026-08-07 00:07:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 75fca301-aad5-32bd-ac2d-de697615906c | -3.0582 | -48.740398 | 2026-08-07 00:07:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d504b59-0852-3255-beb7-46f456296597 | -12.5602 | -46.933399 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab09d657-3d02-367e-b903-42e7dc1c9f68 | -11.1579 | -44.472599 | 2026-08-07 00:07:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab478e5e-4360-33d7-a93b-b58893dc196e | -9.9367 | -48.691002 | 2026-08-07 00:07:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b7f147b-2e8e-3f7e-ad23-af42ca27a408 | -7.0926 | -46.551601 | 2026-08-07 00:07:00 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92fef868-528e-31e7-9ec6-df8a98711bb0 | -15.1054 | -53.5709 | 2026-08-07 00:07:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8e91ff4-b43f-363e-9fea-3a192fffdfe1 | -13.8206 | -53.689499 | 2026-08-07 00:07:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36e08672-c90c-31d4-90b2-71359d3ba979 | -15.5894 | -43.730202 | 2026-08-07 00:07:00 | METOP-B | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 2b513fb9-4aed-3b62-83e3-eb72e90134c4 | -15.5246 | -50.0056 | 2026-08-07 00:07:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 51794347-1891-37fa-b8df-b49b01385969 | -18.152599 | -47.971199 | 2026-08-07 00:07:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e4309b2-068b-3bc8-abee-c1960f6c56b3 | -12.5536 | -46.949699 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12a0e2c6-5865-3baf-a24b-176b19e9d0d2 | -3.2666 | -49.523201 | 2026-08-07 00:07:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b6bad4e-b1cb-3858-a8a9-8ff34c013515 | -5.4264 | -43.433102 | 2026-08-07 00:07:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3418dfbb-c585-3aa4-8b00-1610c571af46 | -11.1785 | -54.8447 | 2026-08-07 00:07:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17f413e1-3249-325b-846a-4b89b94f01ef | -13.7845 | -49.713299 | 2026-08-07 00:07:00 | METOP-B | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 69cde9e4-2c0d-38d9-86a4-acb6f01aace5 | -4.8467 | -45.220299 | 2026-08-07 00:07:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba73149f-c8b4-3637-83e9-a9061dce4c06 | -11.0866 | -47.801498 | 2026-08-07 00:07:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 003a95b6-97b1-36e6-8112-1fee99b6343d | -12.5832 | -46.898399 | 2026-08-07 00:07:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d5105d6-6812-3dcc-90b0-5f234d9f59a0 | -4.8446 | -45.211201 | 2026-08-07 00:07:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 413b6dbc-0768-3359-b8e4-89205d6c4ec2 | -15.5344 | -50.003502 | 2026-08-07 00:07:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c7458e56-addd-3646-a4f7-f3f661fd32a6 | -11.1357 | -54.883598 | 2026-08-07 00:07:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14157bcb-bc66-3ac9-a716-a2a33266541f | -11.3195 | -45.207401 | 2026-08-07 00:07:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca027c99-eb86-3c77-be6e-6da810094ea6 | -8.3776 | -49.638199 | 2026-08-07 00:07:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1f30c7a-3209-3a65-a46f-6e0d8b6aedb5 | -16.6842 | -51.3522 | 2026-08-07 00:07:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e96fbea1-50a9-3957-b459-e73c82fcc5ea | -2.6927 | -47.361198 | 2026-08-07 00:07:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 928c36f5-0757-34bd-9228-65ba2b51950a | -3.1248 | -48.579498 | 2026-08-07 00:07:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b7fb72c-bd97-3750-8638-0802555a8102 | -11.467 | -44.557899 | 2026-08-07 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 828d30a1-9788-3b5e-9d60-a6563bccff64 | -5.9833 | -52.152401 | 2026-08-07 00:07:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 662cb826-bddc-3d6c-bc40-44f11b9d58a2 | -7.1524 | -48.944099 | 2026-08-07 00:07:00 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
