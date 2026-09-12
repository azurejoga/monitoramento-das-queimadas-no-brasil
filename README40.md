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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26d83671-8d63-3ad7-bc19-28d7afa3bd9e | -9.18349 | -59.44917 | 2026-09-12 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cc7f525-f5ef-38b5-bc5f-ab57ec311377 | -6.10906 | -55.64181 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62ada0e6-a178-3db5-a795-e06863c557fb | -8.82415 | -46.02348 | 2026-09-12 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63b71483-dfef-3593-88e3-db57e259d811 | -5.77574 | -45.09654 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3709c792-c1be-3dce-abc7-f144d4e98a3b | -7.18574 | -45.92262 | 2026-09-12 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d1cb0e6-3e06-38e6-b671-84fde7020243 | -6.22558 | -55.6161 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcf40741-25cf-36ff-8661-8b39b5d9b68f | -4.30011 | -55.72681 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e48a76e1-d1fe-3f51-92fe-3fe3e39f83b0 | -5.80766 | -53.81378 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57a4ec58-0868-31c2-afeb-7c3d19e3e862 | -10.63023 | -46.12268 | 2026-09-12 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceb84b52-da76-3253-b6ef-a3ec20ebc541 | -5.57598 | -48.68488 | 2026-09-12 05:10:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d93149ba-169c-382b-990e-8b902141818f | -4.35892 | -54.77477 | 2026-09-12 05:10:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f965e50b-c737-399a-82f4-0efe898477a5 | -6.28691 | -59.93089 | 2026-09-12 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89848cb0-3010-35fc-9d79-f3929a51c7c0 | -6.34221 | -55.3008 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d9352ef-4262-33d7-a2ae-1dbb0047db47 | -10.48516 | -51.36417 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9abcacfb-5c16-3c0b-b8b0-6486c7de153b | -3.85807 | -49.21955 | 2026-09-12 05:10:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 234be73f-1c84-3c35-94b2-ea63918f098d | -10.34122 | -48.01987 | 2026-09-12 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12ce5776-91e3-3301-98e1-f742e1d5fbd3 | -10.48581 | -51.35968 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75d27c09-aed6-3350-8c9e-a74fa5a5b2b3 | -5.60601 | -44.84723 | 2026-09-12 05:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfd60958-1cf2-3e44-91bd-e78e896efe41 | -8.46315 | -47.53375 | 2026-09-12 05:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 587c99c8-fb63-354f-9186-fd3715eabd44 | -6.84562 | -55.58241 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 098e55be-5b7f-3baa-ab4f-ce8fd78547e5 | -5.97802 | -57.77909 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4a898e2-d9f6-3d4c-b547-fda1dce45b98 | -6.87667 | -55.6311 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddcbf84d-610f-310c-89ae-58008d8f4f10 | -6.32536 | -55.86309 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7f6632d-cd83-3bb0-af8b-2e634c424756 | -6.07488 | -53.49216 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac7cf7f7-f7ff-38b1-907e-88fc514ed465 | -6.10624 | -55.63765 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97eafb04-9ae6-3a40-8b4b-8ad94a0e8ab9 | -4.53514 | -54.96239 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed6650f9-134a-3adc-8733-e867b00ca998 | -10.56227 | -51.36184 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 783a6aa6-86d4-3c47-8c28-1fc074d5519e | -6.10848 | -55.64545 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a526fb57-aefc-3f78-b9be-61be8f20ccbd | -8.81791 | -46.91199 | 2026-09-12 05:10:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7dbe80f1-cdb2-3055-a840-3dd260d243fa | -4.08425 | -49.49271 | 2026-09-12 05:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82531320-6e5e-3e3b-9606-7c8920d6ce0c | -3.81552 | -55.89099 | 2026-09-12 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3df5732-1392-3c2d-9ccc-6e6b18731b4e | -4.35949 | -54.77125 | 2026-09-12 05:10:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 217fd312-6d93-345c-bdb2-5be4fd6d5df5 | -6.24534 | -51.69873 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20159378-14e6-3a8c-a5a2-ce8c5c90bcef | -5.98083 | -57.76174 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 205018b6-4d49-36a8-a477-3cdfe3edd79a | -6.88504 | -55.6435 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 901dd792-dd38-39fe-9fec-2ae97e8a7348 | -6.84393 | -55.81081 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a62e368a-3efe-3cc1-81cc-75e5b7f9785c | -6.2082 | -57.77551 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46f68fa4-511d-3eaf-8a61-1d29339ea53c | -6.84416 | -55.80767 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 293f9584-339b-3a44-9d8f-1098ff5777e9 | -5.80968 | -47.22545 | 2026-09-12 05:10:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47a74cc7-90e1-3d84-af29-c7c76960b689 | -6.28997 | -56.01593 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b25c71f3-d25c-3a17-a4f8-3b10b0b08d83 | -8.12056 | -54.80115 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0baef891-63a1-34e6-87eb-b41acec3007a | -6.81616 | -58.99412 | 2026-09-12 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd73acb5-59d7-3c8b-bcbb-bb8d3e91afd4 | -10.54787 | -45.21409 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f9f0010-01ca-3742-9d20-877124df86ff | -9.54851 | -45.47652 | 2026-09-12 05:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b78288f-aa0f-34f6-9d8c-fb7f5c2f2010 | -4.86162 | -55.99894 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f033c579-08af-362f-90be-d582c38c9dd0 | -9.89974 | -46.22733 | 2026-09-12 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 313ea7cd-40d4-3c4d-a66c-5037dab4acd9 | -11.38006 | -46.83018 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f643cb2a-8ba1-3a6a-8400-f3c6885341f7 | -6.20893 | -55.26447 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26d92f80-0295-38da-a585-a9a3d6bc1eb0 | -8.11779 | -54.79713 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4fba71a-fbc2-3376-b185-97921106bda7 | -11.37965 | -46.83327 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 821707bb-60d4-3e67-9268-419f34012656 | -6.12336 | -55.64378 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46497388-fbfd-3a3f-accb-85cdb6281a5d | -8.97474 | -49.66698 | 2026-09-12 05:10:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 171b9111-c17a-3c89-9524-cf4e9dae15b1 | -3.8753 | -51.18277 | 2026-09-12 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f3bc152-82a6-31ae-b5e5-a604037ebea1 | -5.79104 | -53.81117 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6daf01c5-5fad-3dae-a5e2-3ab0c86d4a03 | -10.7198 | -48.96255 | 2026-09-12 05:10:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2719ac0-a2eb-3005-9a0a-80ec7f0f4649 | -5.38949 | -54.44358 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c7dc0fe-d881-3a8a-9910-9c8000e75728 | -9.71308 | -54.35537 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3540ce2f-63ad-3884-acf2-293cc6868cf8 | -6.86347 | -55.25702 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b31c9ab8-1991-3234-bdba-6188b884522a | -4.82135 | -55.76588 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1514ea6d-96f6-3dee-94c5-1289e9a8b3a0 | -7.95812 | -44.01008 | 2026-09-12 05:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03e0e6f6-19a2-38e9-b17f-3c53e69a2493 | -8.57045 | -54.56568 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54413946-1b7f-37d8-a58c-c2a26ef4f819 | -9.71141 | -43.39455 | 2026-09-12 05:10:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 748abe89-d6f7-3280-9693-33f7b63c5b87 | -6.2377 | -51.7016 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f5719e9-fa9c-36f2-aa4b-2e0e405bb646 | -8.12167 | -54.79419 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 366b600c-db56-331d-beda-3273bf61c085 | -6.57512 | -55.61598 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cf7012f-081e-3e59-8460-fb24f600cf60 | -4.53292 | -54.95474 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34ce7212-5325-37a9-9d54-bfb8fe80e4f8 | -8.91899 | -50.86127 | 2026-09-12 05:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be8d1235-c9a4-3002-99a6-e0235f5ad6b4 | -9.93269 | -48.51855 | 2026-09-12 05:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68962257-a611-3f17-a79e-390197448cf3 | -3.33978 | -53.26897 | 2026-09-12 05:10:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c207a608-b987-3620-b34f-40b3e2a5e53f | -11.36908 | -46.79446 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76318012-d11c-3899-a475-cf540d4c0f9c | -6.28334 | -59.92634 | 2026-09-12 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 848fc7b6-f908-3b89-966f-165aac22c92a | -8.57378 | -54.56621 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68af6512-4270-304e-b12c-1bd72e5a25af | -4.86709 | -56.01817 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c8bf0d4-937e-356c-b1a4-0341d609af9a | -6.28815 | -56.02706 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bff7d295-0067-381d-8a8c-993998916229 | -9.70974 | -54.35483 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30f95a15-ac25-3d36-aab9-bfedaaf4dc7e | -7.27675 | -46.80116 | 2026-09-12 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17d84e72-dc9f-387d-8ed1-1b1e8b60ff9b | -6.1154 | -55.64993 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12044c21-188f-3967-bc4c-a1fe0acc4f80 | -4.53907 | -54.95937 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3d3215a-5342-397c-8d36-33e3bf87c762 | -2.73137 | -57.63403 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0d01c2c7-2a6f-3668-8788-26465f8f79cf | -6.40085 | -54.97736 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9388fb69-9da6-3990-985d-66fcc4680a06 | -10.55766 | -51.34003 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 198ecd32-95ba-3224-861a-0257c5805931 | -5.97712 | -57.76114 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e4e5841-5d37-3fe8-865f-e5c21c618446 | -2.73755 | -57.64478 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 895359f0-298b-3043-a577-94cd8b64df72 | -3.73509 | -61.74896 | 2026-09-12 05:10:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 02fd9175-4841-3452-a169-e8ee9fe4255b | -7.30862 | -45.99176 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 366dd12d-e73d-3144-97ae-7daeff5c7c17 | -4.87357 | -56.00021 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9f05dad-5e65-3618-a065-671477da4dbf | -6.39807 | -54.97333 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0629400-6b39-37b6-8ca3-3be9f39cf859 | -6.11069 | -55.65336 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f7d7938-1b36-32bb-b86d-592239b5684f | -6.42517 | -56.10902 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98cd7b47-d22b-3acc-90d9-fd63eaa1fa6c | -6.86093 | -47.43425 | 2026-09-12 05:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80368a33-7823-30f9-a273-2b1d0d7d4e9c | -2.72752 | -57.6334 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b93bf545-2a22-350b-b815-3465416cf92f | -10.9009 | -47.83305 | 2026-09-12 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b1c52141-9c98-34f1-a4dc-082bc6565f6c | -6.33484 | -55.71886 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3ebfdc7-4f17-373a-8cad-8f2cd5a60a5d | -10.55397 | -45.21116 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c7a278c-ad14-3f46-8bb1-26ad08811415 | -4.05428 | -56.33342 | 2026-09-12 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75e7d9d0-237b-362e-b5fc-4a2dac23bda9 | -6.11021 | -55.63457 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 377ddace-9633-331f-bdbf-f7086a58dec7 | -6.61209 | -44.20425 | 2026-09-12 05:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9b1b6e8-cdeb-3c96-910f-9b5667a56af8 | -6.21115 | -55.27208 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d19b45ab-8893-325b-9eb9-ccfbb446eaa4 | -7.0308 | -55.39244 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c8febe4-251d-3c33-bfbd-401925127848 | -6.06542 | -53.4871 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
