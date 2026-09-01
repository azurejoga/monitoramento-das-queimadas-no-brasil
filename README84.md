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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69632151-e11b-39eb-9f63-6c9bfd42c8b6 | -6.86516 | -59.48079 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a20a94b-2c3f-3eaf-ab0f-a83f8c58950b | -9.39583 | -60.57496 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 645d7f78-a2cf-379f-badc-ec2e7a4219e9 | -7.62052 | -57.61701 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e237bb0-e46a-33f0-9f30-432a36451f5d | -7.34336 | -55.19632 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acd44548-e8da-354c-9842-7170eb0527ab | -7.68518 | -55.3433 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5eeab97-ebe3-35f8-a8ed-705f2fa6714d | -6.59148 | -58.59853 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21be637d-8538-3350-9f31-8e2a70fdbae6 | -10.82915 | -50.71338 | 2026-09-01 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bbad7b33-e33c-3ded-9b86-09ba946589b3 | -7.34873 | -60.57792 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0b66dacb-4311-3666-8f74-feaece6e1328 | -8.13841 | -54.96995 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 91c4263d-4580-3781-a0af-f199e1d069c1 | -6.12496 | -57.67759 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd83ebf7-5431-3e92-8731-c2c17979b860 | -7.56209 | -60.46361 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53d90910-cad0-3004-a328-6412a84f30fe | -7.58228 | -61.35261 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5ede681-5833-324e-bade-05c578034cdd | -9.16132 | -59.54019 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac7ec979-0e8b-3f80-8b12-def8d276ed1e | -8.50534 | -55.30613 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d33c7386-990c-37e8-8332-f8d67ef1c158 | -9.46862 | -57.0169 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31574e59-0255-33f5-b643-935195e1235a | -9.17631 | -59.63885 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3e54143-ea09-3264-9386-083e56c6361f | -5.58042 | -60.23653 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 187e05b8-5345-3a67-b445-f6bae8b86827 | -7.88449 | -63.7608 | 2026-09-01 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2589c774-e854-3af3-9799-cc08e55e7cb4 | -6.55814 | -58.56617 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 972c915d-0a16-3ee7-8ecc-28a7d063836d | -8.87873 | -66.88861 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 325c7129-150e-3d96-839b-7132cc819834 | -6.70352 | -55.4069 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a5de95c-8c92-362b-b3d9-482b0d3e930f | -5.48317 | -57.14755 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62f81ef9-5674-31f1-ad57-eaf0c8496159 | -8.11815 | -54.96342 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 89fcf30c-727c-3454-a974-73cdb2be1f09 | -9.03402 | -65.3979 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fecd702-15bf-36cf-abf7-05cf4796d607 | -7.57891 | -61.3301 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2be34e29-de33-3d0d-ab95-c0ec7bf881ab | -9.20342 | -59.55834 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a52ddc9b-7d0b-3b16-8365-b74036a516a3 | -6.58775 | -58.59794 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 582ad740-75a3-3eb1-8623-9bc8a58c13b8 | -6.81698 | -59.44511 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8ca5d05b-eadf-384a-9710-eea231a633af | -7.05016 | -52.71932 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aa37ffb-37e0-3670-992d-44b34d5696b3 | -9.0593 | -65.48988 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 18ed595a-d1aa-3f00-bb90-9372402a183f | -9.06695 | -65.48711 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f5cc3fc-8ed0-3f27-a644-e770d4e3a884 | -9.45924 | -67.45756 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42309657-383a-3834-beba-5542f5dc62fa | -8.77522 | -69.34161 | 2026-09-01 05:36:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 16938a9b-5e5d-31b2-9069-73df6c8480a4 | -10.34808 | -50.00521 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efa5eceb-bec8-3283-b31a-00c7d04156fe | -6.12667 | -57.69324 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3011df9-f608-3822-9c1e-071691648abc | -11.25617 | -50.58473 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf209cc8-d25a-38fa-a306-0e5686f00b52 | -6.56629 | -58.56282 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5d69eaab-3038-3606-a7fd-de7fe915469a | -6.81403 | -59.44046 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 554fde9a-fe0d-3953-b3e6-2a53d44a5704 | -7.58564 | -60.47123 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f1378377-a758-3b21-a4a5-cfce2419ae25 | -7.19755 | -60.67275 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 705d7d0b-f5ab-38f9-9adc-f17c9503553c | -10.06306 | -59.40347 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f2a9a891-ba30-37e9-b298-bc18c1ad41f2 | -9.02573 | -65.44884 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd934e24-2cc2-3489-b319-4292e0a10fc6 | -5.47966 | -57.14348 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a2e1f3f-fa92-3713-9e43-88978616ca54 | -7.47904 | -61.38483 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0f60664-039f-38a4-bf1f-047ea7a5a544 | -5.96049 | -57.6791 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 294516cf-aa3a-3ec0-9db2-da098e4d06a3 | -6.95329 | -55.65245 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2829e943-4598-3ad1-ba6c-ed7ed1c49f71 | -9.22456 | -59.79212 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e15595c5-d5fb-3502-bd97-9a2353ec2c4b | -6.82158 | -58.87556 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 545a3ae3-7cc0-32d0-9025-529fff45c322 | -9.85546 | -64.98235 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9be1795-c09a-3da1-86df-08a7715bedb6 | -5.57757 | -60.23228 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2992016-85b5-3dc1-b71b-c31f6c880e61 | -10.41725 | -57.22893 | 2026-09-01 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c1239f0-186f-3cbe-8734-9d4fdc774a25 | -8.93172 | -66.9434 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99f69039-a253-3766-a337-b80f7452bb1e | -7.57168 | -61.37655 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe00632c-d702-3994-ae63-eb7ebe0d2cb4 | -7.57301 | -60.4615 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faa2cb67-9246-3a1e-8875-05d733dcac3d | -6.15538 | -57.40064 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb0ce8f8-a410-3882-9a7e-10e41da58595 | -7.48407 | -61.39658 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccdbae80-abda-381b-8196-8302c9910602 | -10.95032 | -61.65676 | 2026-09-01 05:36:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c3300afb-2fe1-3d54-9eb9-fd424df5da42 | -7.37598 | -65.38886 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 353b6a65-1fe5-32b7-a1f1-1703698aa2a9 | -6.98199 | -59.59283 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3545cac-2d52-39cc-937d-0b08e83e44a1 | -9.45069 | -67.46111 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9b35224-e815-386c-ae1b-626777801e89 | -7.09786 | -63.04711 | 2026-09-01 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b6338a8-5af1-3a4d-86b4-029d0cb057a9 | -7.28521 | -49.83154 | 2026-09-01 05:36:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c1bb866c-c465-3991-b755-fa5a71fb5f74 | -10.8218 | -50.71839 | 2026-09-01 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf701f99-9038-3508-b856-422cf1afffac | -8.79963 | -70.79754 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8aa8f1af-bb0a-3acc-aa40-abb59d1e34db | -7.35443 | -60.58651 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 087a2126-b117-3129-854b-d85a4d2e6484 | -5.48369 | -57.14405 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c69b3fbe-9e86-3b8e-ac26-e3bd3542e45a | -6.85826 | -59.42953 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4876c112-5ce7-3ca2-8b89-1aa210daf615 | -7.73096 | -60.98343 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2f35b98-ee74-3f1e-98a3-bcba920c2709 | -10.50108 | -59.61491 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2da38f30-8e3e-33b6-bdd6-869fdee8f38e | -5.96517 | -57.67464 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4a301ce5-e29b-33a0-84d7-b56159080d5e | -7.34701 | -60.58915 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01bde4d7-d671-36ba-a26c-bd6a1f467f9c | -11.26142 | -50.57108 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a660da07-77d8-362a-98a0-2a6ca43005c4 | -8.51204 | -67.13374 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc061ad7-6d4d-3175-8776-7ae792019f2b | -9.47123 | -57.02968 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c2c8f6e-097b-36b5-b08d-4178f90bc529 | -9.06661 | -65.40247 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dc3d1f7-2aa4-38c2-a1b8-115f890571ca | -6.95466 | -55.64316 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f41e3944-f70a-3081-98cd-e5f30839fc81 | -9.03751 | -65.39849 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 975e8ce6-90ac-3f84-a44a-a74123f0f5c6 | -9.01485 | -57.54136 | 2026-09-01 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b538a294-48f4-3dc5-9f15-e848e00122db | -11.2448 | -54.00705 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cd79060-e1bc-3ffe-92ca-dd97f00e493f | -9.02952 | -65.45256 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e5fe154-a5b4-3258-bf47-3d9b64285095 | -6.94816 | -58.95548 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21497dfe-9aba-34d3-b0ff-03c9324c7881 | -8.58659 | -54.76929 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbbdce3a-53db-3589-bd25-79c0f9ccddd4 | -9.17754 | -59.63338 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f6bc368-8b5e-3caa-813e-eb3a4686fc27 | -9.06655 | -60.48369 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbfedf27-d2c0-35fd-b0fd-62809ab4962f | -6.60267 | -58.60029 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f939c9a-896b-34c1-8236-74213f504c26 | -7.59253 | -60.47237 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aea07d06-0043-3f96-9a5b-7dc2343b5d3e | -7.8689 | -63.75098 | 2026-09-01 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7824574b-6444-3c64-a1ec-e27ea6be9036 | -8.80255 | -62.49349 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01e87bf2-d006-3c6b-abf7-8bd8ff0a43b4 | -6.3743 | -51.76283 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9f01e15-33cb-377e-a52a-d86edf16e2fc | -15.0159 | -52.76706 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8f89d94-e3bc-31e3-88cd-adba9636d442 | -15.76858 | -56.09436 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0c8a41ff-2f06-30b5-8155-80c28b5d7e02 | -15.25351 | -53.88764 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ef4a237-3abd-3113-b825-f2097e217c3a | -15.7679 | -56.09998 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6528de34-b288-36b5-9b65-e5033c38085e | -15.0098 | -52.76588 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1028a914-ad06-30bf-a5c7-a9d9ebfb9038 | -15.98256 | -55.96267 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ef18c07a-bbd2-336c-a30c-e3c64ae0ce88 | -14.46451 | -52.52645 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db88667f-4170-3e19-861b-50d1c55af230 | -11.61202 | -62.38992 | 2026-09-01 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4d1b2df-f6d9-3468-a93a-b3105024c72d | -15.49298 | -56.0173 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c352f45a-ba77-3f11-ae24-c9800562c454 | -15.74655 | -56.41487 | 2026-09-01 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| beeea272-a6e6-361d-b4fd-53c015e0069a | -14.59069 | -54.11751 | 2026-09-01 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README85.md)
