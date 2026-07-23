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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5848d257-bbd1-3218-b87a-a1033e34ecb8 | -8.83654 | -48.33293 | 2026-07-23 04:44:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 303fbc15-0e3a-397d-8c38-483b005c581b | -8.83937 | -48.33717 | 2026-07-23 04:44:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d7ed014-1282-3a8d-a44b-150da59a19f0 | -8.83994 | -48.33346 | 2026-07-23 04:44:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9123b50e-ae57-3571-8885-f70a482bcfba | -4.47202 | -45.9147 | 2026-07-23 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be06ec98-afac-346c-bca7-7bbb86a1f430 | -6.21 | -49.43008 | 2026-07-23 04:44:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 184494bd-4c06-342d-8c6d-c04fbce3d0ed | -9.10616 | -49.65428 | 2026-07-23 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fe09830-b2dd-35cf-91c0-213afb714112 | -4.23774 | -48.55617 | 2026-07-23 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbda1caf-4551-3863-b9b1-a08bf77b7636 | -10.62431 | -47.80383 | 2026-07-23 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efaba47f-8571-38ee-8ea3-d593c55807de | -5.14833 | -47.60262 | 2026-07-23 04:44:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac70721b-8bcd-3921-ab26-c4df602bdf78 | -5.48941 | -45.11683 | 2026-07-23 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e222238-dedf-3fed-9fd4-e161de8aca21 | -7.00752 | -45.41498 | 2026-07-23 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbe8e6d5-385a-3be7-9245-481e69dfe52c | -5.79962 | -43.63792 | 2026-07-23 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2364543-33e9-35a7-8330-44c76d39af74 | -6.41465 | -51.23633 | 2026-07-23 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0c00de6-c582-3746-b3f6-572d3c1505c3 | -5.67461 | -43.57516 | 2026-07-23 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18e5ea58-9067-3cd7-aca0-9be38a1b5c65 | -6.31007 | -43.6565 | 2026-07-23 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc78e3b3-5030-3417-95ae-f202a8f1e9fb | -9.17155 | -58.31314 | 2026-07-23 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c69af698-2c02-36f5-b73f-af3290e7fd9e | -5.76116 | -49.08632 | 2026-07-23 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ef6a925a-d89b-3b07-8421-f415f81188ce | -9.17006 | -58.31311 | 2026-07-23 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc034948-c8ba-36c5-9699-21da02b0542c | -9.51798 | -47.12886 | 2026-07-23 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8928572-2afb-3204-9951-0a086fea5281 | -6.04138 | -43.87245 | 2026-07-23 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9668af2c-1562-3a8a-b51d-0729a52189b0 | -8.83381 | -47.07442 | 2026-07-23 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78a20f31-e612-3228-890d-e660b76605a8 | -5.38622 | -49.28843 | 2026-07-23 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64697378-655c-3e33-9b95-b29f5a0c4d96 | -9.81633 | -50.66525 | 2026-07-23 04:44:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 168b15a5-f102-3af4-ae08-2bf90d00fa34 | -6.04558 | -43.87304 | 2026-07-23 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af9bff12-b009-3521-8d75-c7a76e9c5e82 | -3.09537 | -54.51462 | 2026-07-23 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7755f58d-0fbd-3892-93e9-98805bb0ea30 | -8.80109 | -49.36918 | 2026-07-23 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3596ba1-2ba3-33fa-b870-324e1e7308b3 | -7.88738 | -46.90384 | 2026-07-23 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8912a84b-61ef-3fa0-867f-7c82319a0c66 | -7.61181 | -55.26505 | 2026-07-23 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 201c8ab2-48fc-3384-8b12-8695b7e71f0a | -5.32208 | -43.56769 | 2026-07-23 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 294ab50f-6d79-3f8b-b2ab-59ec9e6dcddd | -7.8838 | -46.90328 | 2026-07-23 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce8e655f-7fb0-3ea0-acb4-ec5dd6bdc8c8 | -9.5252 | -47.12996 | 2026-07-23 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b92d0c7-a1d4-3014-9f0e-b2807ab6f254 | -6.04673 | -43.86539 | 2026-07-23 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9174b01-a25d-3766-9484-7d5c840724a0 | -9.16272 | -58.30586 | 2026-07-23 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7506f566-34d8-37a7-88fe-97320916f1cb | -4.03243 | -43.23386 | 2026-07-23 04:44:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83cf1393-a9bd-3faa-90f2-4623145b5180 | -6.05093 | -43.86596 | 2026-07-23 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b410c07b-2638-3662-8fd4-546efa30734c | -5.82264 | -44.13303 | 2026-07-23 04:44:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93bce4c1-4585-39c4-9555-dff6ea0300cb | -6.23156 | -48.98995 | 2026-07-23 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f3de507-f5ac-3d9e-8984-e0a834a3db1c | -6.41126 | -51.23577 | 2026-07-23 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af0013a3-5df5-3a75-a598-919c51b05602 | -2.85289 | -54.4878 | 2026-07-23 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e9eab5d-88b6-3b88-b239-f399509dcb04 | -9.16119 | -58.3058 | 2026-07-23 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b63a564-dfb7-3dbc-a03f-e611d3f4573f | -9.16171 | -58.31136 | 2026-07-23 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e4b7f52-5301-3f25-a009-39a2a7f2ad34 | -3.95919 | -48.1239 | 2026-07-23 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 216242fd-5ebb-3de5-a914-4c01f766dd0f | -8.06925 | -48.01588 | 2026-07-23 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec2eb157-3b37-3422-b131-215e2b4526d2 | -2.84372 | -54.68078 | 2026-07-23 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 491c227a-3b73-3261-b967-a686392d2d81 | -5.8469 | -49.06059 | 2026-07-23 04:44:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08dc7e94-a7b9-39c3-83fd-998216ad3b40 | -6.30758 | -43.65321 | 2026-07-23 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 434718e6-140d-3904-872c-fef0432cc9a4 | -3.84611 | -49.03382 | 2026-07-23 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 259fe531-1c20-3273-a402-fd6bae5072a0 | -7.75952 | -55.32457 | 2026-07-23 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 793c8a17-9a53-35ce-b49b-06543fd1cce3 | -8.80054 | -49.37269 | 2026-07-23 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16ff6da4-dfc5-381e-bdfe-4659dd670b85 | -10.17818 | -47.91122 | 2026-07-23 04:44:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edd0e575-e3cc-34c4-8f97-18d59d077fb4 | -5.64072 | -44.12909 | 2026-07-23 04:44:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3a97671-423c-301a-bb0f-5e88862010df | -5.82608 | -43.48593 | 2026-07-23 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fefdfc95-e498-3975-aeff-73f0b308c3f3 | -7.61118 | -55.26878 | 2026-07-23 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c8906a3-2ddf-3ef5-b8ce-dc55a27cd10e | -5.32266 | -43.56381 | 2026-07-23 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 48402890-746a-3969-b94a-bd83b22266f8 | -9.16514 | -58.31221 | 2026-07-23 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27d9323b-1a4d-3245-8917-3488107a207e | -9.22575 | -48.5579 | 2026-07-23 04:44:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b389f1f-1825-307d-adb3-fd365781b84a | -4.22177 | -48.57138 | 2026-07-23 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 936fe209-9e41-3bd6-996e-1be81132753e | -8.83527 | -47.07676 | 2026-07-23 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 314c455d-32be-3791-8374-5eaef0795c33 | -4.03668 | -43.2345 | 2026-07-23 04:44:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b43851ab-1203-3715-9303-dd39e62a09cd | -4.21846 | -48.57086 | 2026-07-23 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 633bf70e-cb3c-37d0-adb9-1cb200cb3f07 | -5.76062 | -49.08977 | 2026-07-23 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8ede06f-ed83-38f7-a3f3-b49315526668 | -6.54132 | -43.10635 | 2026-07-23 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0120a56-0ecd-3dd9-bb54-e15cd0197372 | -6.30949 | -43.66061 | 2026-07-23 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cc69f92-8d5c-3edc-a5bb-bb1c0f5a6abe | -6.41634 | -43.0669 | 2026-07-23 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d818d706-4556-3810-83b0-54c3d932979f | -6.4208 | -43.06758 | 2026-07-23 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28e34eb2-5975-31cd-b788-92b488788f88 | -5.63662 | -44.12847 | 2026-07-23 04:44:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bad16121-cf5e-345d-afc0-83a8ed27fcc3 | -6.59901 | -51.70081 | 2026-07-23 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19b17e65-4af0-3b44-a050-60500f2524fe | -17.58218 | -47.5034 | 2026-07-23 04:46:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35fa175f-f43b-3931-8d8a-fbd9476336de | -23.27163 | -51.20582 | 2026-07-23 04:46:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5527fdcb-dd95-3e3e-bc9a-a933dde86176 | -11.57692 | -48.39755 | 2026-07-23 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39e7ba2d-0b7f-327a-8910-0ff5606677ec | -13.36532 | -54.29762 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f85294f5-acbb-37e5-b0bb-e91756baf402 | -11.84199 | -50.33525 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 51414cb5-ea70-3428-b64f-ccd4641e92f2 | -11.94638 | -50.36313 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d694dc0b-0f46-37b8-adfc-6d6f6c33e3ec | -11.78406 | -47.10019 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 139dfd4d-7b1a-3003-a462-8ea9b6ef5056 | -11.79828 | -47.10685 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fc308d7-99e0-3ea7-ae68-c20318dfc1ba | -11.66924 | -50.35427 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 89ec5277-1a67-3bc3-958b-64edb8af30c8 | -11.68746 | -50.34638 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c419dee-1205-3711-bd5d-d51d7b8a8597 | -13.31037 | -54.32838 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec4b5c8b-5258-39dd-9b8c-5bb695b6d47d | -11.78035 | -47.09966 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 594f9125-744e-352b-a52c-93eb460e56a3 | -13.3218 | -54.30446 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 454d7a23-df78-367d-86fe-15ba7eb949f5 | -11.81827 | -47.33149 | 2026-07-23 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f027e1fa-c2dd-37f2-879a-7c3f57fad308 | -11.70683 | -50.37502 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1a8058f7-357f-3be5-a08c-7221b54be1a9 | -11.33744 | -62.22407 | 2026-07-23 04:46:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81c65d40-1f2d-3943-abfa-871b30d96dc2 | -13.36819 | -54.30243 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22487836-d879-31fa-91a7-c85a7c6066e5 | -11.95411 | -50.35714 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cca7e869-dbf3-3b36-a035-9afae22a9c42 | -11.91109 | -43.84123 | 2026-07-23 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 33fdf9df-08d2-319d-b4e3-23c1db664137 | -14.34789 | -53.05697 | 2026-07-23 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e40cac0-53f3-316b-bbb9-1e25c8124e3c | -11.57983 | -48.40198 | 2026-07-23 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed8211d9-d7f3-3b55-b016-209fe8b255eb | -11.68525 | -50.36046 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6cae2643-0122-3603-9fd1-46c21ac34496 | -13.32827 | -54.30991 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27c5a933-bdbe-3531-b968-547b32c5b9cc | -11.67918 | -50.35587 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 759aeefb-07ca-3dc3-a019-d6f9dad601f0 | -13.32039 | -54.31281 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 090744f8-a56f-3490-8fa3-2d7bf2b50567 | -11.94748 | -50.35607 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 928c536b-e712-3b3e-bb34-e38889a8083d | -11.93865 | -50.36911 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3bf80fb-77b0-3ba5-8db6-63fdc9dcf757 | -11.9961 | -50.32772 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab99c6b8-257c-37ca-8ffa-9d870dc69b73 | -11.96351 | -50.36227 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 18daa0d2-13d1-3717-be64-28d54978387e | -11.79085 | -47.10576 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 78d2fc96-8a8a-3cd3-9828-4c9d61de52f0 | -17.57758 | -47.508 | 2026-07-23 04:46:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7961efed-8828-3314-9c48-ea1fc87d972a | -11.57287 | -48.40091 | 2026-07-23 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04a8cf75-df30-3d27-83d9-ce7a27bc6c31 | -17.73466 | -52.74633 | 2026-07-23 04:46:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README15.md)
