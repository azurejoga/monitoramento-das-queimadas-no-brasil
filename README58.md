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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0147e195-ccbe-3b2d-a9b5-51f4d099fe43 | -5.4031 | -41.33796 | 2025-10-04 04:12:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2ef7f89f-7c76-333c-b971-c5705ba73127 | -7.26981 | -45.48202 | 2025-10-04 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 546c28ba-7d73-3b2b-8ceb-2ae22f57ab55 | -5.32858 | -43.34499 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cf69b2b-7405-3639-bb28-d3dd92f9bb30 | -5.79636 | -42.72848 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c063e617-3422-35eb-a0ea-12012a4dfdb2 | -6.66295 | -42.83334 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| be26f628-1694-3fe6-959e-abd5004a76d8 | -5.08906 | -49.06192 | 2025-10-04 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b3c2527-ef27-3cdf-b65f-b469ed67e63f | -7.00311 | -44.49363 | 2025-10-04 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18dc14ea-7f20-359d-b777-5fe3f7b0983f | -6.7223 | -44.14866 | 2025-10-04 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c64c6098-969c-3084-a243-e9de1788a8ab | -4.44538 | -43.25846 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f227e68a-59be-368d-bde8-0a4113dfc639 | -5.8881 | -42.9655 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 73649686-e498-389a-9772-f17fd36ef513 | -5.30188 | -43.10602 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b22c8c54-4eaf-3478-870f-2cc5251c49a9 | -6.76579 | -44.80931 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d84ee5e8-6711-33ac-932e-c4b3e6157016 | -6.28078 | -44.04535 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e37b860f-aca9-37b7-90ea-b29dbd157e47 | -5.88857 | -42.91959 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 39fcd754-a0a4-3210-a7f1-2f0544ad11fa | -5.69174 | -42.83219 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1e306584-58bb-3acb-a7ef-115a1166f0d3 | -6.36154 | -43.89938 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0e6aff22-55e9-3c99-ac44-468562c30e9c | -5.27235 | -46.17683 | 2025-10-04 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7df116f7-af99-3910-95b5-f071afdffc8b | -7.26447 | -45.48188 | 2025-10-04 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ef2f8f0-39bb-3b16-b7f0-03e39d1d5af6 | -5.93605 | -43.30608 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8172481-4b32-3750-9c3d-d6a69bb4e43e | -5.66615 | -42.71503 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| a2886dfd-8523-3cb6-ac1f-a0b24ed441c5 | -6.27466 | -44.04076 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcbad23b-7506-3ae8-97d2-96afe8380631 | -5.96708 | -45.88918 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d242e14-eed2-3f49-bbc8-2e01c46a2b0d | -7.80316 | -42.53527 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7706d6d2-1ba7-3465-9798-a99124d1294c | -5.32773 | -43.77872 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 784c7bfa-5bfc-3f3a-908a-df6da74f0ada | -6.28183 | -43.63154 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdfcbbb0-1bdf-3db9-9b32-e4186e12c890 | -5.32241 | -43.53326 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f842df26-29fa-33cb-a00d-5b44f1f9cf1c | -5.99718 | -45.79378 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af22cbbf-af68-3ee6-9e5e-6de5a84de5c4 | -4.45035 | -43.24854 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac1e9d13-5012-3cb8-a4cf-4917ab5b018d | -6.13781 | -43.81021 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f42831ff-9843-3737-95e1-cc3a7195af37 | -6.07466 | -42.51348 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 1611d1bf-455d-3ae9-9eb0-8a7fec87de39 | -6.71361 | -42.81295 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e642c238-6e09-3e84-940b-aca10ea48d55 | -4.44703 | -43.24802 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cecd48d9-6863-3981-9634-68dcca92ed95 | -7.21465 | -45.72469 | 2025-10-04 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fc0a1b5-100e-39fc-ad86-5fe0772272e0 | -6.67678 | -44.20333 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76ee8040-672e-33fe-a4a0-44b862e6c367 | -6.72971 | -45.96807 | 2025-10-04 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 63732e93-3d5c-334d-ae16-0af40e1ae9c2 | -6.34319 | -43.45957 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cf3fb52d-4983-3a40-b12f-71b012098b1f | -5.79277 | -45.7591 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b61fa574-89d8-375a-871f-1711698054e6 | -7.05162 | -42.7811 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 22f46074-4361-300e-88d3-74179f472d39 | -4.89114 | -49.96507 | 2025-10-04 04:12:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6132bf33-4a33-335c-85f8-76b9146a2205 | -5.98296 | -44.24697 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fb879e0-6a4d-3a2f-bb07-2caa2e8c9ffb | -5.93533 | -42.88098 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e1984a15-0dcd-31bc-89b7-330771d4d03a | -7.79765 | -42.54877 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7fc71228-186a-32b9-9d33-c953c31a50e6 | -5.32146 | -43.34711 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ed6384a-569d-3be6-a999-01a7a4e3da07 | -7.00004 | -44.20055 | 2025-10-04 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 471fc28b-726f-3728-b860-db5be293a3d4 | -7.73799 | -42.60393 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ac21fcf2-aad3-38d0-a37c-474748047d68 | -7.7577 | -42.52095 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 431c8cfa-08f2-3348-8a5a-0d2866f7d4df | -5.88479 | -42.96498 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a6733ed9-5d0e-3439-b4b1-775af47dc4e1 | -6.35423 | -44.37584 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11cd1dca-c45a-3e67-912f-d6067da096a3 | -6.34098 | -43.45211 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cd29c60-57d6-36e6-a8e1-4e9800372b23 | -5.81981 | -42.88069 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 57205830-1458-3b5d-af08-cce7e15304cd | -7.04777 | -42.78404 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a86a4d2a-ac66-3314-8d75-4adf3c20be6e | -6.55308 | -43.09938 | 2025-10-04 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35c8f9be-1898-3b27-9dc2-8c22de0f08d0 | -5.28319 | -44.01521 | 2025-10-04 04:12:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b645e696-2d1b-3380-bd9c-1eb1e5a6d4e7 | -5.76581 | -42.18806 | 2025-10-04 04:12:00 | NOAA-20 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d46de03f-3902-313e-ab23-a2c111eb3046 | -7.56368 | -42.39326 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 31715bb1-f75f-3c14-8072-2a5056f10fb5 | -7.78609 | -42.57924 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5af589ce-5001-31a5-8a47-e7bc576fdcd8 | -7.47754 | -46.04741 | 2025-10-04 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb066234-d32e-3b03-8cc1-0f097b7ed93b | -4.31031 | -48.08982 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de899fa1-ac81-34e2-b397-5ad81d432fef | -2.25609 | -47.8546 | 2025-10-04 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cd66d98a-b95f-3336-bd16-7caab71d2376 | -1.1331 | -47.80414 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ddcf1f4-d6b6-39be-9238-ab3303caf76f | -6.45971 | -44.5775 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b4f70a72-ccfc-303c-851f-a427d8a731bb | -2.68356 | -48.38764 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcc4e91f-5280-37d3-abca-2e83d035768a | -5.40874 | -41.34606 | 2025-10-04 04:12:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b8564f32-99ee-33f7-a360-200791fe21ef | -5.31797 | -43.53971 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1da3c10a-b506-3ca8-9fc1-5cad8da39082 | -7.04661 | -42.76962 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aaf075c2-20eb-33c0-a6f0-886602a16154 | -7.70173 | -42.57677 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4e6b92be-2da2-3f9d-a2d4-31d7e4341c4b | -3.83595 | -44.55452 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 344012b6-33d8-38bf-a60c-9d4698c40f25 | -7.0145 | -44.76676 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 444d04ce-5206-36f8-9ed0-bbbb38b00874 | -7.70614 | -42.57029 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f7a8454a-1bef-3443-83cd-7406a2611fa0 | -5.87042 | -42.66917 | 2025-10-04 04:12:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8cf871fc-f2f5-320c-aa2c-5566fa8689bb | -5.6901 | -42.84254 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5326aff7-76a9-3708-abe9-f68617d4d1fe | -2.90004 | -50.73779 | 2025-10-04 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b9446c1-1baa-371a-8bc1-8e672ca462fe | -5.9825 | -43.61311 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06e9017d-b8b7-377a-8cfc-f49cc6be8b12 | -6.36595 | -42.8859 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f2161beb-7590-3067-8ac2-d7e8b7968060 | -6.6144 | -44.29224 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3dec4af-a5e0-39ae-b596-11374350c341 | -6.8758 | -47.23328 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| aac7cb5c-d041-3c04-b5f3-57510b92898e | -5.82202 | -42.88811 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f122c122-0cca-33bf-b806-3cbf38f46005 | -5.90078 | -38.4819 | 2025-10-04 04:12:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d9f0cf70-3389-35b1-b2f8-6b9463cf3ba8 | -6.23571 | -44.22035 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dd2c85e-6290-34bf-ab1c-9c875fbceedf | -2.89641 | -50.72781 | 2025-10-04 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9860c771-e298-3b3c-a4c0-509ce3585b32 | -7.53919 | -42.4009 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7f88ee82-4d21-38fc-ac75-b6e1125dc5eb | -6.35089 | -41.61868 | 2025-10-04 04:12:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba74e559-85df-3fdf-b07b-dc492fda6751 | -5.29913 | -45.27119 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e274ceba-398c-39bf-9aef-2ceb89e49745 | -4.26023 | -48.55927 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a768e89d-1dbc-3cb0-a7ca-27dbdc8c12f3 | -7.74386 | -42.52236 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| bf23f32c-b3ee-3414-b50b-9b501219909d | -4.44758 | -43.24454 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 159f7bd7-4f8c-3e1e-9b9c-ab508430e4b5 | -7.47566 | -43.04343 | 2025-10-04 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 57b15a80-4204-356c-8116-71a9729a12b4 | -5.73943 | -42.91755 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fbdc2f34-9967-3b84-b531-2eba167ea5fd | -5.73888 | -42.921 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 175969b5-0ef5-348d-a76c-0b724c0bd597 | -6.17209 | -43.91666 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fefae65-5b54-3c7e-a489-51c68d2f5a11 | -7.36689 | -39.17643 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 68d3d4d5-203b-31f9-a43d-6b378081b74f | -7.78663 | -42.57574 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 66ed016c-1f07-3c6c-8694-34bd265276e5 | -6.72904 | -45.97218 | 2025-10-04 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eb75f640-defd-30e1-a0de-90015ea00284 | -6.65683 | -42.80756 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5949863a-2e7a-3da7-a0b7-85dd17f0b15d | -5.9763 | -44.09564 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a26825c-4a8d-3436-a14d-d45f00569157 | -4.6105 | -46.45956 | 2025-10-04 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45f8590e-eb05-364e-bbc8-02c2cc559f1c | -5.65849 | -42.74212 | 2025-10-04 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 99efdd51-5c4a-3cf3-9c4b-0d0f553f3144 | -7.77562 | -42.60268 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7c09d609-13a4-356b-b65d-d8dd769136e4 | -4.4509 | -43.24506 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cedf78b1-3f3e-3a0a-ad4f-570587c83e63 | -6.31195 | -44.27328 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README59.md)
