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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb2a2190-826c-337d-ab03-27528888fc5c | -6.1905 | -45.441002 | 2025-08-10 00:24:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc626bf7-7d9f-389d-8dfa-b3fad1e7eb25 | -3.2201 | -49.336201 | 2025-08-10 00:24:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8f6f18-ae30-30d4-94bb-036bc39cfcac | -4.3042 | -48.0788 | 2025-08-10 00:24:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce162317-d47e-33b7-8c10-d1fa9eab8c8f | -7.4182 | -43.992802 | 2025-08-10 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 11faec4f-73e2-362f-a760-5e61c4838f1a | -9.8664 | -44.704899 | 2025-08-10 00:24:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9b10daa2-0c22-3e29-9d19-f110b27fd84d | -16.079 | -43.632702 | 2025-08-10 00:24:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 46051249-1552-3dee-bfb0-1d26765201e7 | -14.1078 | -45.403099 | 2025-08-10 00:24:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c7d5d95-9b94-3c30-a08c-7cc82cf747ef | -7.0028 | -44.795898 | 2025-08-10 00:24:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b2ed1be-ae93-3430-b99d-4ae848ec286c | -8.3058 | -45.000301 | 2025-08-10 00:24:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 58fa2bf7-a399-323a-8a96-c55da3312dba | -7.3918 | -39.6768 | 2025-08-10 00:24:00 | METOP-C | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 7132d649-b950-3f0f-b190-202011ad4330 | -8.0471 | -46.330799 | 2025-08-10 00:24:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f3f1c29-d697-34ed-ad68-11cc57a9b223 | -3.6203 | -47.509998 | 2025-08-10 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 952bfdba-798f-3a56-a5c9-24125454c0fa | -7.1565 | -44.0662 | 2025-08-10 00:24:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8c89d5a8-9da8-30ac-b9ae-264b224fa58d | -4.143 | -46.4533 | 2025-08-10 00:24:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 270e56e4-1bb2-3029-ab26-fa35f87af575 | -6.933 | -42.9575 | 2025-08-10 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fa149c26-8abc-3181-9595-c9bcc7e86151 | -7.8734 | -45.551201 | 2025-08-10 00:24:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ac43903-87d4-3b6a-af9f-a937aa4162fd | -5.3136 | -44.3512 | 2025-08-10 00:24:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 563464da-0c77-3b9d-b5c6-45b4a2c75dd2 | -19.2054 | -42.0228 | 2025-08-10 00:24:00 | METOP-C | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bf96039b-56f3-3d14-bbc6-25f700057e76 | -13.6376 | -48.968399 | 2025-08-10 00:24:00 | METOP-C | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db0de8d6-d0ab-3a06-a160-fe654da23915 | -19.7904 | -43.973202 | 2025-08-10 00:24:00 | METOP-C | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3b9875fc-d628-30cc-8ce5-84a406521aac | -3.839 | -47.749401 | 2025-08-10 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4452fe6d-d696-39ce-aa95-a537782ad1ee | -10.3445 | -44.910702 | 2025-08-10 00:24:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79798de0-f649-3295-98df-620b49199d83 | -16.374201 | -42.533699 | 2025-08-10 00:24:00 | METOP-C | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fdd05bb5-e200-3bac-b536-a44df022dddc | -9.523 | -45.427399 | 2025-08-10 00:24:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a752dfcb-33a8-3c65-ab54-28573aeeff1f | -6.0571 | -44.897999 | 2025-08-10 00:24:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 751f69b7-b636-3f14-81c9-5f8f6585793d | -16.382401 | -42.5242 | 2025-08-10 00:24:00 | METOP-C | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f4198472-3c5f-3a4d-a952-c67361adeb89 | -6.9266 | -42.9296 | 2025-08-10 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fe682d7d-9bd8-352b-ac69-4355c6236dbe | -6.195 | -46.099998 | 2025-08-10 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe9db8a8-7a34-36ce-ae24-cda2ff7abf8d | -3.9706 | -47.876499 | 2025-08-10 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7569dde-adfd-3a65-aa34-45091a51223b | -8.875 | -44.7836 | 2025-08-10 00:24:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a30c6745-87dd-30e7-936a-0c6f98192974 | -6.0616 | -43.744301 | 2025-08-10 00:24:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03a3bebe-e250-36b0-8020-12d6d13cd7f9 | -11.3298 | -44.8545 | 2025-08-10 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0467a874-f3dd-32c6-bfca-d2ffa03eef94 | -9.6597 | -46.751202 | 2025-08-10 00:24:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c50ec026-e247-377d-991e-de7ce9085797 | -5.3152 | -44.358002 | 2025-08-10 00:24:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0633bd35-3841-349d-b71c-30e3ab5a994b | -5.3867 | -41.325001 | 2025-08-10 00:24:00 | METOP-C | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d598c384-1249-3163-8222-4b2052f746f0 | -9.4954 | -46.2812 | 2025-08-10 00:24:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ed92374-0279-3099-b381-0ff6f122a5e0 | -6.055 | -43.760201 | 2025-08-10 00:24:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edd8af59-c079-386a-8fee-60fb86706d00 | -11.3735 | -50.536301 | 2025-08-10 00:24:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74b78dcd-a5e8-3061-9412-5721abb44156 | -3.5909 | -47.516499 | 2025-08-10 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceb6907a-70e4-3c47-bf39-30ec54a235db | -7.8849 | -45.5564 | 2025-08-10 00:24:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f21b58d4-cc70-354b-b357-e278ac076679 | -3.9725 | -47.884899 | 2025-08-10 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78752d6e-a186-38e1-824b-3dae6eeae21b | -8.5757 | -62.6512 | 2025-08-10 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7614c09b-7ec7-3b31-b807-318e5feb88d5 | -8.3102 | -44.9967 | 2025-08-10 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 9f34db7e-5481-38f3-b0d9-643f58879bb2 | -9.3806 | -61.5315 | 2025-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 166.9 |
| 7731d9dc-ff21-3460-bb66-122dcd995341 | -9.3622 | -61.5133 | 2025-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| fe577b3e-9a4e-3889-8cfd-97b17cb32e03 | -8.9398 | -60.7673 | 2025-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ab4a2a75-81aa-3bad-b6f5-35952f6c1afd | -7.0614 | -59.1972 | 2025-08-10 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 5001ef98-90bc-3bfe-b252-01833ac805fc | -9.362 | -61.5324 | 2025-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 198.0 |
| aa2af6ae-1bdb-36c8-886b-85edec943037 | -8.5943 | -62.6315 | 2025-08-10 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 4d3b3c24-f0a5-353d-a26d-a09380d4d2ae | -8.5942 | -62.6505 | 2025-08-10 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 7f4b1a25-54e0-3aa5-9c66-05b42fdb522d | -8.9213 | -60.7489 | 2025-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 8da626aa-6e9c-39ce-bd39-1af045bdf3e9 | -7.0799 | -59.1964 | 2025-08-10 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 26a3fe7c-ee61-39d7-8c8e-5f6a4393a33c | -6.961 | -44.5546 | 2025-08-10 00:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 964a04b2-66f4-3375-861a-29b8f0bfd3c2 | -9.3808 | -61.5124 | 2025-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 007dcc86-5964-3621-bf16-ac8dbdbf100b | -7.08 | -59.1771 | 2025-08-10 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3433eef9-2e84-3abb-b7fb-fe23e47cb4be | -7.8891 | -45.5616 | 2025-08-10 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d84c8518-c5c8-30bb-8fbc-0103e8b38dc8 | -9.0638 | -49.5226 | 2025-08-10 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| adec8aba-205e-3d0d-9faf-c7a467a35d4b | -9.0636 | -49.5441 | 2025-08-10 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| ce4bfe45-f9c6-3e45-977b-9c884758ee7c | -8.9215 | -60.7297 | 2025-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 64bb999e-717f-3693-85e0-31592f570392 | -8.5792 | -54.6758 | 2025-08-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| b5b5679b-e62e-38f6-9832-20339ba3ee57 | -8.5604 | -54.6973 | 2025-08-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 5ed1e31f-b1fb-30b2-a2b0-6219f9c5a895 | -8.9401 | -60.7288 | 2025-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 45ef4ba7-248b-310b-ba2b-4037b1bbc882 | -8.5605 | -54.6771 | 2025-08-10 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| be3fb0c2-82db-315f-8774-be34f17bc382 | -8.9399 | -60.7481 | 2025-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 8ec40b54-c7bb-3bf8-b7d5-32d939a5da99 | -9.3619 | -61.5516 | 2025-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 9a493ef4-479e-3c3e-9f59-7c4f89cb92f8 | -9.0636 | -49.5441 | 2025-08-10 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a5984ca4-1885-366c-b3e9-30cb342882cb | -9.0638 | -49.5226 | 2025-08-10 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| de20f78d-ad4f-32a7-9bc2-bd9285189b88 | -8.9399 | -60.7481 | 2025-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| c113b32e-7de0-3c2f-901b-21f8fb7fb07c | -8.9213 | -60.7489 | 2025-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 16adfa0f-6d43-300c-bd7f-2cd25c38bbac | -9.3622 | -61.5133 | 2025-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7135000d-cf39-34c4-a310-0abb2829e46e | -6.0498 | -43.7554 | 2025-08-10 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| bdde6825-7b40-3f9a-9777-3e9a5eb1942a | -9.3808 | -61.5124 | 2025-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 7717fab4-5947-3e57-bd70-ccd75f3a5299 | -14.6175 | -47.1551 | 2025-08-10 00:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 4f447549-6005-3665-b284-905d6283222a | -7.8891 | -45.5616 | 2025-08-10 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d5e940ad-0991-3fbc-99f4-478af347b58c | -8.3102 | -44.9967 | 2025-08-10 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| be737636-6e2e-37fe-af23-0dc26877a9f7 | -6.961 | -44.5546 | 2025-08-10 00:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4c560472-85b8-3c3e-a742-32822ccf3f35 | -9.362 | -61.5324 | 2025-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 159.6 |
| f6e8d772-891c-36b1-966c-2bbe67125092 | -8.5942 | -62.6505 | 2025-08-10 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 67f79517-927a-38d9-9c10-a4b2b92b076d | -9.3805 | -61.5507 | 2025-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 6d2b2c1b-a68e-3cd4-ba6a-f5f229bbf166 | -9.3806 | -61.5315 | 2025-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 168.2 |
| 27a30c3d-4117-3de0-a1f8-643d94bc48d6 | -8.5605 | -54.6771 | 2025-08-10 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| bc43020f-42b0-34e7-b14c-aff9cef06eef | -14.598 | -47.1584 | 2025-08-10 00:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 28167e1f-f30e-35fa-9353-458323511370 | -8.5943 | -62.6315 | 2025-08-10 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 87a51f3c-a65a-3384-877b-b0143f2c5752 | -8.9213 | -60.7489 | 2025-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 71b23e1e-1a37-3717-9e09-de09bf294025 | -9.3622 | -61.5133 | 2025-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| dafca867-9cc3-38dd-86d4-a3a8bafdc8b8 | -9.3806 | -61.5315 | 2025-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 8bb21573-80be-3b57-93a8-20dd0233a11d | -14.598 | -47.1584 | 2025-08-10 00:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| cad8dc22-1b6b-31da-a96d-72a46696db8b | -9.3808 | -61.5124 | 2025-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 9fb03fbd-dc12-363f-a901-4978a6baa6f3 | -8.5942 | -62.6505 | 2025-08-10 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| ee2c0dab-0e62-368f-a821-3c7df9161c26 | -6.9422 | -44.5562 | 2025-08-10 00:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c8bd43f7-2bf4-3f9e-b1d3-7793e785fb1b | -8.9399 | -60.7481 | 2025-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 4447f469-3f5d-3e44-9e18-3468eca2322c | -9.362 | -61.5324 | 2025-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 374ab9dd-b0be-3b05-b751-22aab8478c53 | -8.3102 | -44.9967 | 2025-08-10 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 580e1ba1-142e-323a-8ed4-ecb96ee2dc21 | -19.5857 | -47.2088 | 2025-08-10 00:50:00 | GOES-19 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 0af94cf4-fc57-3b19-b873-b7b6cee1d98d | -16.3731 | -42.5425 | 2025-08-10 00:50:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 7f5f3d70-d681-3fe0-9cb8-947e119b3903 | -8.3102 | -44.9967 | 2025-08-10 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a15f446f-09a9-32a1-a71c-5eb9381b47a0 | -8.5943 | -62.6315 | 2025-08-10 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 224cfe9b-d5e1-3e11-9248-583dfc2c954b | -8.5605 | -54.6771 | 2025-08-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 1b39f4b7-ca61-3617-bed3-60adc77f361b | -8.9399 | -60.7481 | 2025-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| dd068455-a307-376f-984e-28548b2bf2a0 | -8.5604 | -54.6973 | 2025-08-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |


[Clique aqui para ver as próximas entradas](README4.md)
