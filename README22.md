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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0bda57a-1dc2-3c1c-bb55-f4f6c9e1f7d5 | -10.11514 | -42.40515 | 2024-10-31 04:25:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 56a82114-71dc-3bc5-a806-6a8fb717163d | -11.29272 | -41.85703 | 2024-10-31 04:25:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bdc98009-1f81-376d-9cb9-ed0c31d2bf2f | -11.29221 | -41.86077 | 2024-10-31 04:25:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f088e8a4-4ce0-35a6-8295-3f85cc52dc69 | -11.2917 | -41.86452 | 2024-10-31 04:25:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 897f5b4c-46c4-3f72-b00d-59887e8a1e58 | -6.21304 | -42.8859 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bba3debb-ed49-30a9-83b5-de25874222df | -6.18024 | -42.20061 | 2024-10-31 04:25:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9077ac1a-85b3-3379-8a7b-ed912016319a | -6.17666 | -42.20271 | 2024-10-31 04:25:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 56d68bc8-6671-3d95-9570-63bf9e25dcdb | -5.96878 | -42.60564 | 2024-10-31 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 23a7b265-87d6-3144-a6b8-b67b4384ba87 | -5.9651 | -42.60509 | 2024-10-31 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e47420af-658e-3d4e-9c61-a5252b1955cf | -5.96444 | -42.60942 | 2024-10-31 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3715fc80-9b37-36e0-8c74-7c87c167dd12 | -5.96141 | -42.60453 | 2024-10-31 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4cb7b038-ecac-3939-88c8-04d55f555d3b | -5.96075 | -42.60887 | 2024-10-31 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a6edc5a-67bd-3a97-b874-89a743fc021a | -5.83623 | -42.79284 | 2024-10-31 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 773c3fb5-1fc7-362c-9677-f6f280bfda23 | -6.31499 | -43.47394 | 2024-10-31 04:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d9d14e2-d6fe-3e55-8045-228d6894c764 | -6.2878 | -42.85635 | 2024-10-31 04:25:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 623c6052-44dc-3cb9-b47c-12cd93da67be | -6.23942 | -43.40158 | 2024-10-31 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daf2100e-b3d0-3d2a-a238-9f01790f2b34 | -6.23646 | -43.39709 | 2024-10-31 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96df27e2-fbe3-304e-b5ab-12c0589c10f9 | -6.23231 | -43.40055 | 2024-10-31 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 810b6756-f787-30d0-8588-397d202dd31a | -6.20111 | -43.42207 | 2024-10-31 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7b84539-648d-32e4-a854-089e05b20a5a | -6.2005 | -43.42603 | 2024-10-31 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b96b4665-d2c8-34bc-8dbf-27730cf4307c | -6.19967 | -43.42461 | 2024-10-31 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0f56ecd2-af19-338e-996c-f092f9960f92 | -6.19907 | -43.42859 | 2024-10-31 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81c6f2f7-f760-3609-8248-3c4733099a95 | -6.19694 | -43.42555 | 2024-10-31 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9bf4289a-23dc-341b-bc26-fb681698906a | -5.46071 | -43.17368 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5e5a438-25ee-30d4-87d2-594939352e80 | -5.46009 | -43.1777 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a479626c-d776-3be9-9441-697afe7b4c1c | -5.45715 | -43.17311 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5537ebaf-daf6-3067-9555-2dede8ed1635 | -5.45298 | -43.17657 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e935f7cc-7dcd-3243-852d-2fa33bbac044 | -5.44717 | -43.2615 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c722ac5a-0655-3115-a8e3-159085d5d140 | -5.44363 | -43.26094 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01ecefd1-63c4-3c48-a9a0-77e081776b0f | -5.44302 | -43.26491 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f91d819-2e2a-3662-879d-b590dc8b2c97 | -5.29808 | -43.05465 | 2024-10-31 04:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b04cadc8-0544-3b0e-ba63-5dc9d35c0ca0 | -5.29747 | -43.05865 | 2024-10-31 04:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fa94d6e-b8d3-377f-950e-7664be1ea32a | -5.2939 | -43.05812 | 2024-10-31 04:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc553227-4269-3c70-bd99-fefa95c634b6 | -7.92293 | -42.84082 | 2024-10-31 04:25:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 52df51c4-b513-3f58-933a-d8fa6e02a403 | -7.89802 | -42.95953 | 2024-10-31 04:25:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6c50d509-cd7b-3a70-94f5-bbd8b4b6d865 | -7.89738 | -42.96392 | 2024-10-31 04:25:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 181380ea-6fab-3feb-8401-206cfe12bdf3 | -7.89628 | -42.95671 | 2024-10-31 04:25:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f38f8129-933f-33ed-aeb0-d7aff359fe90 | -7.89561 | -42.9611 | 2024-10-31 04:25:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9d6276c5-b6b2-3fff-b365-555f64863ee5 | -7.89432 | -42.95895 | 2024-10-31 04:25:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 44143503-3f6d-3508-9c74-7601aacbc7c7 | -7.53331 | -43.09247 | 2024-10-31 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0f8e0fc5-8665-3e49-8508-2a79ea696f17 | -7.34564 | -43.54245 | 2024-10-31 04:25:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4c5974e4-83c6-3eb5-a951-009fe2d8fef2 | -7.34501 | -43.54658 | 2024-10-31 04:25:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 26f77e93-0d71-3e55-abb1-d8621e134b24 | -7.34208 | -43.54186 | 2024-10-31 04:25:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2346258a-316e-3f64-829a-6052e914c73c | -7.12229 | -42.57648 | 2024-10-31 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4f7b619c-d142-3657-bd7d-28b04f813c39 | -7.11854 | -42.57593 | 2024-10-31 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6bc336c-6a89-3bfd-83c1-8733a37ef703 | -7.08441 | -42.62612 | 2024-10-31 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c6921bee-7207-367e-a411-fd9f87bf02b7 | -6.51009 | -42.81937 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0e9d60bb-eee3-3e83-95d3-04016d5c8461 | -6.50943 | -42.82365 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e009f0d6-7e4d-3e10-95d1-00e949aa4370 | -6.50935 | -42.81728 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0b70e119-8b7d-301c-8da5-ffee00ac2d7d | -6.50643 | -42.81878 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 89650912-24f8-34b1-8bbe-9e5d27e7b8eb | -6.50568 | -42.81668 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| acde7b8c-6d30-393f-ac22-b002b7ed139c | -7.94978 | -43.26704 | 2024-10-31 04:25:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b32f724-eccf-3df6-aba0-97db2aa6dd51 | -7.94905 | -43.26936 | 2024-10-31 04:25:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 66379702-43cf-389a-aae9-53a531caadae | -8.24983 | -42.91993 | 2024-10-31 04:25:00 | NPP-375D | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd3a6005-6ae7-38f8-94c6-327d4cc5e3c7 | -8.89818 | -43.94163 | 2024-10-31 04:25:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ee19d06-1651-3f35-9597-51f997db1e66 | -5.93353 | -43.68418 | 2024-10-31 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 784321bd-89d9-34c7-b5cc-9fd73a90a5e3 | -6.24997 | -43.57018 | 2024-10-31 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b9847ac-cfd1-3baf-b784-ad26be898280 | -6.06581 | -43.62288 | 2024-10-31 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f07c991c-a160-35bd-b43d-d321e6c631e2 | -6.06516 | -43.62374 | 2024-10-31 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 251b849a-70b7-3079-b788-23e5fd877970 | -6.0623 | -43.62233 | 2024-10-31 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bcd5b9f7-a37a-3ff7-8584-236d409db14f | -6.06165 | -43.62319 | 2024-10-31 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f3fa0559-ef00-38e0-a359-aedab8dcd1fb | -5.73321 | -43.70178 | 2024-10-31 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68e63936-0c72-3f1a-99f1-25021a5749cc | -5.32121 | -43.73161 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afda646c-4eac-307c-b620-d5aff29ca72b | -5.32063 | -43.73541 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35cbf3b5-91ac-3b28-a6f8-48a0fb8b1a00 | -5.31832 | -43.72726 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d693bf88-9832-30f2-99bf-35b9df3af650 | -5.31774 | -43.73106 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35137715-33a9-3f92-9316-cab3c2ad55c7 | -5.31716 | -43.73485 | 2024-10-31 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac6138cc-ac3b-365d-b06a-d9f8c3dfed15 | -5.23041 | -43.59671 | 2024-10-31 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97163c9e-a35b-326c-9abe-29bdc0fc8510 | -6.14045 | -43.9603 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 7db289a9-eb47-38a0-ba34-d46657838293 | -6.13987 | -43.96412 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 2c41717d-3aec-3e45-8fe4-36776f95240d | -6.13698 | -43.95976 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5dadca0c-5702-38b5-ab73-b1b823dc3f2e | -6.13641 | -43.96357 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6c47a472-b4bc-383d-8a9b-f9a19caf2f70 | -6.13583 | -43.96738 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4018d4f-48ee-3b8b-8335-3e467d6830e0 | -6.13525 | -43.9712 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7cb486b6-9781-37fa-9405-51025d597a54 | -6.13352 | -43.95921 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bb28411d-11aa-3900-9674-3a601ba0011c | -6.13294 | -43.96302 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f0c162f5-d5d5-3617-be06-21a4dce865bf | -6.13237 | -43.96684 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 822586d8-9c4f-3f20-97bd-cce05ac76386 | -6.13179 | -43.97066 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d84c3d7f-79c0-3294-a2e1-189f2626163e | -6.13006 | -43.95866 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8f595b78-eca2-3687-93e9-c41520dc73f2 | -6.12948 | -43.96246 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 887ac6d6-cc9f-350b-b995-96588b1e225d | -6.1289 | -43.96629 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 55de8a6c-64b2-3413-99cb-011354fd1cbe | -6.12832 | -43.97012 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c38429ff-81f5-3191-9d58-562fc31b63c5 | -6.1266 | -43.95812 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f4a79e3e-9970-3a8d-ab9e-bb7c50a49922 | -6.12602 | -43.96193 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7a8a61d1-2906-3f4b-ab58-2950d6bdeb2b | -6.12544 | -43.96575 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a0da4e52-b3a5-35f5-aed0-aa0b2c5cb121 | -6.12486 | -43.96957 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3b9808a0-dfcb-3bca-8817-fe187e5ddb5a | -6.12198 | -43.96521 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0284e42-5b63-3d42-8627-2642b192c139 | -6.1214 | -43.96902 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2b0126f-a3c3-3254-b9b1-15f7a7e35603 | -5.62248 | -43.95362 | 2024-10-31 04:25:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71a4c080-3358-375c-8eda-6cbbd69f891a | -6.40816 | -44.13231 | 2024-10-31 04:25:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ea434e4-08dc-38d4-bb00-61e120dcef4e | -6.17791 | -44.01655 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 924d6afe-1182-3977-9bc8-1b6692397c24 | -6.17446 | -44.01598 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc32b71d-db33-3d23-8588-21b521553a4f | -7.5306 | -44.0336 | 2024-10-31 04:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23fd8b95-17e2-34c0-b618-d56152e93aed | -5.95551 | -44.46527 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 321b00f4-a8c3-300c-b705-f91e6222bab5 | -5.95494 | -44.46894 | 2024-10-31 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f58be04-bff5-372a-bf82-95bea97376e7 | -5.90574 | -44.60296 | 2024-10-31 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b5c5600-012e-3def-8a8a-e6f6e7116885 | -5.81547 | -44.12807 | 2024-10-31 04:25:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c144ff1b-7f76-3485-8f3c-ce93e58ad1f4 | -5.81204 | -44.12753 | 2024-10-31 04:25:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5831b6d9-6b8f-354d-b4b5-d0d1bd946313 | -5.81147 | -44.13125 | 2024-10-31 04:25:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 02db1ff9-0b71-3b62-94e5-a59cd99a5f0c | -5.68913 | -44.38093 | 2024-10-31 04:25:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README23.md)
