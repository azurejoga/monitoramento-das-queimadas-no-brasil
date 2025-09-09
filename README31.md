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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c6699e1-4dcf-3cd4-aa48-d9d3db4431b0 | -6.21337 | -43.36401 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ddc38eb-443c-31c1-b81e-6dc298c632a8 | -6.09685 | -44.14132 | 2025-09-09 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cec6435d-3b24-37ad-b98a-d966057788ca | -5.97094 | -47.42457 | 2025-09-09 04:32:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98df4ccb-e186-3b66-b082-3f054ff3f40d | -7.08801 | -45.19787 | 2025-09-09 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 662b7471-1c54-3558-b2ac-ff9690deb743 | -6.23119 | -45.60441 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3cd36e59-1738-3312-a228-4ff870ad8222 | -5.43853 | -43.41877 | 2025-09-09 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0df176e9-bff6-3f12-8481-eb089b17c137 | -6.7862 | -44.78732 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f13c4fa0-970b-3282-8685-1b03908fda6a | -5.48639 | -45.34625 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d57ea865-038b-34b4-9746-1cabab282294 | -5.67111 | -45.39677 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd43cba6-f132-3191-9053-fa91ddbaba19 | -5.41428 | -42.85563 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 79533de5-adda-38ea-9b1b-bf1ea1979897 | -5.63218 | -45.44214 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 736e8fb9-c887-3423-afea-bf691f6f214e | -5.11905 | -44.66736 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d608c213-cc8c-36de-a463-71e313d632b4 | -6.41111 | -44.4882 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f7e3efc-ff94-37ff-893f-0997ee01886b | -7.08445 | -45.19733 | 2025-09-09 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5a8752d8-5a09-3d14-b7c0-6377a2ca7c97 | -5.35691 | -44.79671 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9240539-863c-330f-86f4-0da05239ae77 | -5.9441 | -45.74542 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fd219fc-fed8-368f-b91f-a2ff1efc06b4 | -7.20119 | -44.89095 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57509314-3ec3-337e-914b-8ed4bbdcf41d | -5.82311 | -44.11348 | 2025-09-09 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b888712-02a9-30ff-b058-376b6fc1bc5b | -2.43757 | -47.19665 | 2025-09-09 04:32:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0194d6b8-6fc9-300c-9ec5-9e91adb7277e | -5.42501 | -42.81119 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 143ee376-4074-3b8c-8409-d60a870f1b6b | -5.68577 | -45.11038 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3ce8bf9-0046-3966-b6a9-110b18c62268 | -5.89643 | -43.95467 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3762039e-baf2-3750-9ac1-c9a12703967f | -5.71419 | -45.40644 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| acdbdb75-153e-3b88-a673-664b39c61124 | -7.08088 | -45.19678 | 2025-09-09 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3de722db-0422-32f8-99c9-bc86aedb60d3 | -5.74147 | -45.41468 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42c90b08-4a02-3f4d-97be-ebaa88fc4caf | -2.63464 | -48.06532 | 2025-09-09 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90b225d6-11f9-3f05-8e3f-d66845a5a21a | -6.2217 | -45.58367 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8fb299e2-0a02-3415-a9f5-bc475e2bb286 | -5.8108 | -45.6515 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39289173-179f-3381-8e9d-2b4488b230be | -6.67453 | -44.5546 | 2025-09-09 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50194f89-eb16-3896-80d2-245026da3cd5 | -5.85406 | -49.82697 | 2025-09-09 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7118b3f5-cdbc-39c4-93a1-f08b6d4ace48 | -6.06131 | -43.12069 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f32700df-5708-31b9-bb65-43e7bdd4a4af | -2.43419 | -49.31358 | 2025-09-09 04:32:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb2c715d-2f6e-364d-8af0-7b816eb0a65b | -4.89432 | -42.21297 | 2025-09-09 04:32:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 716edde7-2190-3d7a-9444-b86ad877f498 | -5.88042 | -46.09344 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90840ad6-504c-3988-b18c-bf770775cdaf | -5.78217 | -45.40492 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7587837-8271-3774-a376-3493df7f8fc5 | -7.19024 | -44.9084 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cf979c3-18c1-329d-95f3-5907b59cd62d | -11.12167 | -52.03917 | 2025-09-09 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d986fc2-c98f-3bdf-baad-b14205a16f1c | -8.23488 | -43.0329 | 2025-09-09 04:34:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 33e42ba5-8a47-349d-96db-afc236f70fa4 | -9.16619 | -59.38201 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9b7d20e-d8d1-321e-98fd-7ad48121eef2 | -12.63488 | -56.963 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a88601ea-2e0c-39b9-a137-d17a6ebefb24 | -12.96491 | -54.76083 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed306213-81f3-3b2f-85a4-2b6f079489d8 | -10.9671 | -46.8111 | 2025-09-09 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4982ca0-ca46-3f20-ab88-e17d5f8fdb38 | -9.15193 | -49.8495 | 2025-09-09 04:34:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7abcc2bc-ade6-3e86-a5c2-cdc19d96cbca | -11.54053 | -47.31414 | 2025-09-09 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b358d824-b2c6-3143-86eb-56f9ed821ab7 | -12.95216 | -54.76212 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 765e0616-dd9b-3eb7-ac79-f9a993513b39 | -9.449 | -60.52364 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8078d420-0cea-3311-987a-76c18b2716a1 | -12.07786 | -42.58232 | 2025-09-09 04:34:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 50ecf49a-355e-3e4f-a763-22e055ac06c6 | -7.78297 | -46.08234 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 64e54628-7640-39f9-b6a3-538c573407c0 | -9.46149 | -60.52602 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c33a473d-7063-3632-93a1-b34a4dc4f362 | -11.04432 | -46.05926 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fcd0601-7d7b-30fe-a1af-77d6435f164d | -11.41223 | -43.66512 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e703c15d-8ed6-3026-b26e-d31b8655ace1 | -12.1959 | -53.9191 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6efa387-65c6-3047-b30a-fe6ce5d333a6 | -10.08819 | -59.17184 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92ea1219-f0df-32c0-9d6c-4155a826ffe2 | -13.82726 | -43.85982 | 2025-09-09 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29488494-d0eb-3413-8486-0f6ee4add717 | -12.95749 | -54.75564 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1fa63322-5bd5-36ec-9122-9610ddcb1e77 | -13.03603 | -48.02709 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3af179d-f76e-3604-a9d5-e16df924e7d7 | -11.16759 | -48.36493 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 522bd698-20b8-35b8-99e6-99c33fa39abe | -12.19866 | -53.88601 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1300cf8a-1761-3865-800a-f9da3c10ff33 | -11.12153 | -52.01817 | 2025-09-09 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f78467dc-1411-3514-9ce2-5d5f672135b4 | -13.80809 | -46.29861 | 2025-09-09 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7532e81-3797-3662-a5db-0872ae374843 | -12.94407 | -54.76067 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac75251e-53f1-3e52-a389-48a0860b4e43 | -12.93063 | -54.76578 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c80a5516-e584-33c4-959b-1ea1308cec82 | -11.46549 | -49.24984 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21d24711-1935-3898-89f8-7b165e1feb92 | -7.78239 | -46.08614 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 54526fbf-b520-3698-a9e0-044ac4345038 | -8.43014 | -47.28753 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d4086763-3ea0-35fb-bc32-85af4ed736e0 | -8.46731 | -44.85085 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71dbd128-b98a-34df-b855-b76979ef195c | -9.92815 | -47.86919 | 2025-09-09 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5f378a1-d378-30bd-bcfd-f55a0716ef3c | -12.82932 | -52.94388 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c97903f3-d99b-3f6c-b32e-6ee434d2a2b6 | -9.08824 | -46.97873 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44596a6b-a099-3dbd-aa13-26e37078ef4c | -8.2143 | -50.13643 | 2025-09-09 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e898606-29b9-34d8-bc1e-072503abd746 | -13.14052 | -47.15673 | 2025-09-09 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a181c1c5-ce17-39cb-a0db-6db77a278069 | -12.84828 | -52.94272 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4429320d-c596-3fd2-b718-76402f6249d2 | -11.16342 | -57.18889 | 2025-09-09 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d3547cd9-8d53-3fa3-b58a-99b6bac77a18 | -14.60767 | -43.9223 | 2025-09-09 04:34:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b82bf1d-2141-3a8a-9c19-3f6c31f7e199 | -8.4893 | -47.34373 | 2025-09-09 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65fb25e8-652e-3367-aa30-4a0e77733d8b | -10.23765 | -48.19976 | 2025-09-09 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a13c40b1-e835-3bed-8ebf-c66f17569bb7 | -11.03792 | -52.06387 | 2025-09-09 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17ebd302-5016-3f57-897f-110cbdc3b2ca | -11.44347 | -49.26066 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99becaaf-96b6-3fca-8469-bb4b6cfe9ed1 | -14.28169 | -44.95287 | 2025-09-09 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f73a51b2-48d6-3fd4-858b-522744d71035 | -8.37672 | -45.00795 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06940d49-ea42-37c6-b74a-226d99342cee | -11.3079 | -47.39407 | 2025-09-09 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6453947e-b6f7-38e6-8862-7d620d828475 | -8.08788 | -54.75242 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| add05e18-d782-3f99-9172-66c2d7f6ff3e | -7.53519 | -48.23395 | 2025-09-09 04:34:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b63544ee-64e7-3b47-9324-458fa1338ebf | -9.72635 | -46.79062 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d9553e8-c88e-371e-92b0-ec4f0c451814 | -11.36855 | -45.59218 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b4a3ca6-6bb4-39e1-904c-f1238c92fcb0 | -13.27081 | -51.76384 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 379f315b-329f-326d-8052-8286ce1e1b56 | -11.30901 | -46.49876 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e907cdc-6c95-38bb-aa11-f4fa7c5a87d6 | -8.18848 | -44.76553 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16c1c288-49c5-3547-8f1a-e9e4a8702b7c | -7.38745 | -44.84281 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fe12417-0d51-3581-ba0e-50fb83fad961 | -11.13191 | -48.94511 | 2025-09-09 04:34:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd1535a6-9844-3141-95b5-dc633e0fb5f3 | -11.45944 | -49.26682 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 64454af3-a13d-3906-8c56-a5ddc3d1cd45 | -11.93883 | -50.96919 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 41f3155f-9c76-3e0b-8772-801bfdf24ba4 | -11.154 | -45.2707 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2667f585-3b33-336f-bdd9-27c9ff9e708f | -7.57873 | -44.66064 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f849fc39-e683-39da-b31d-002c6669cbb5 | -10.97892 | -45.09743 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 77d1e72f-e7ca-3b65-8a94-0184b851bd2d | -7.98514 | -46.36626 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3349fa5-c912-33e5-96ac-75c84cf98999 | -8.04685 | -45.49036 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41f49495-ed3f-3cf3-995b-d8a506537c4c | -12.19005 | -53.88955 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cc6b3b6-0da6-33e7-9bfd-e3e552b936af | -10.96421 | -46.80677 | 2025-09-09 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 705304db-36a8-37c2-bb8b-a97996daca81 | -7.79614 | -46.08336 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README32.md)
