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
| 2f649a21-b624-3f6f-a269-84b0340b4689 | -22.89765 | -43.75231 | 2025-03-03 03:08:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 94c15e7f-4e5f-352c-b2f6-fccb03867529 | -6.96258 | -34.89011 | 2025-03-03 03:53:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5a64b4ee-b94f-3801-b942-7b43e12761ec | -5.07038 | -37.71609 | 2025-03-03 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f69d86c0-ddf3-3ba6-b963-2f9faab3b6a2 | -13.96307 | -45.55587 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8040cc1e-1375-3287-9d37-c7df8a8c99c9 | -13.9583 | -45.55887 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c3d23a8-34e1-30cc-ac35-0fa652bd3bd0 | -13.96511 | -45.56786 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef2d61b5-dc2c-34d9-9d6e-ababe55d597f | -10.48578 | -42.41671 | 2025-03-03 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b3e65dc1-f8cd-36ff-b6fe-55e1c267c0c5 | -13.95967 | -45.55138 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 720a89c6-2a72-3254-91f8-2fad22b7fe1c | -13.96579 | -45.5641 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddefe665-22e9-3f09-a292-58440cbb9270 | -10.50718 | -42.39892 | 2025-03-03 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 1929e6a8-da32-3b5a-94e2-521a4ec381ba | -13.96171 | -45.56336 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb0ef754-ea64-3a4c-b6bb-4fe13b590821 | -8.1152 | -43.14058 | 2025-03-03 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f89dd545-f28f-3c5f-a052-b3ebc5f4aae3 | -13.66503 | -44.06144 | 2025-03-03 03:55:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c7eae710-5464-3f41-898f-21f44cebe9c4 | -13.96716 | -45.5566 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5bb1325-a1e1-38bb-b03c-469bee87df3c | -13.95899 | -45.55513 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 839ab4f6-6fd1-34f7-a9f4-80eae4b83067 | -14.12081 | -41.6781 | 2025-03-03 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 98947499-e988-3a80-ba8e-ef6346a80897 | -13.96239 | -45.55961 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5747543-bf1f-39b6-a0db-6aab01a36ada | -14.13592 | -41.69172 | 2025-03-03 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fb905d51-2771-3c8e-9827-7677b439f7fc | -13.95908 | -45.55849 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd487848-9282-38b6-a821-3d9f7f9beb98 | -10.50648 | -42.40307 | 2025-03-03 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cabc0ea0-c6e7-3a50-aa4e-234515117ebf | -13.9604 | -45.55097 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12947e84-9947-3859-8928-2a55cc5b1a22 | -13.96376 | -45.55212 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3c15fa6-72b8-3878-8cbd-9a60b6806e3f | -13.95565 | -45.55398 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a0eb5b5-d6a3-3d67-b9a7-e68bad0bff07 | -13.95974 | -45.55473 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e681235-25c7-397c-b810-c08568294e4b | -13.95842 | -45.56224 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d769e5d-d215-3152-99c6-92bb4964c118 | -13.34122 | -41.32336 | 2025-03-03 03:55:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| abd7cd95-22bc-3579-8e7a-7b7a347ea11f | -13.96648 | -45.56035 | 2025-03-03 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd2e4cd6-1bc8-3a31-a0e5-367f494e1017 | -10.48149 | -42.42027 | 2025-03-03 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 503d2c64-bf93-346d-ba55-6eeea49e4329 | -9.99759 | -42.47791 | 2025-03-03 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ce66f95f-9a7e-3c55-a5ad-4d75d70d2bde | -14.00732 | -45.56792 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68bc2a50-97e4-31b5-91b1-379255fbfc93 | -13.99236 | -45.58063 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6cdbc7f-379c-3bcd-82bf-f6d1404445bb | -20.90156 | -43.82 | 2025-03-03 03:57:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a055f21-b0b3-3746-8041-228e939daeb6 | -15.80202 | -47.99576 | 2025-03-03 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f444b50-cd2a-34a6-a9b0-98bbb0ac25b6 | -13.98556 | -45.59492 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f33bf7fa-ddc2-325e-8ad3-1e275f78bb13 | -13.99919 | -45.58966 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f20bf33c-8f8d-3e2a-9842-12491dafe43c | -14.00121 | -45.57841 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 62e46674-300b-3a59-a553-f6a536dcb059 | -13.99578 | -45.58514 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d182f9fc-523b-38cf-8fa4-16316287aa38 | -13.99645 | -45.5814 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21a1fb4d-3eb1-3707-8089-f8e0006cc080 | -14.00602 | -45.59872 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5d676ca-91de-358f-bc97-16745db33501 | -14.0053 | -45.57918 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6a5a34d8-115f-3d36-abc1-19f83d3508f8 | -13.98283 | -45.58663 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c9f0f6b0-399c-35ee-8648-b9d254b2a3c8 | -13.99101 | -45.58813 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 870cdf5a-bc88-378b-bc19-bb7a90224a26 | -13.98146 | -45.59417 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f547e51-e20f-3417-88bd-ebc106c94a7b | -13.9951 | -45.58889 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 561193d0-186a-3c91-a638-bdba154cc9dc | -14.00188 | -45.57467 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b30a61bc-d076-3e44-bb72-21b720b33a52 | -13.97942 | -45.58212 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59c28c91-eff2-304e-9b28-4299e0736ac1 | -19.71707 | -40.35118 | 2025-03-03 03:57:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eb1543e8-3549-3f78-862a-17b5cccc71a3 | -13.99306 | -45.6002 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 362bbd4d-4466-3b49-a441-bf0f7079b9ff | -13.98897 | -45.59945 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba4093bf-6a8d-35e3-ae49-a95f2348fd04 | -14.00938 | -45.57994 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57dbcfdf-bdb2-332e-9926-9bcc3ff4c61a | -13.98965 | -45.59567 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c09bed5c-81b6-3164-8a5f-cbc72d3be3fe | -17.39943 | -46.56248 | 2025-03-03 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c2b050a-bfba-3816-8fcd-1caaa6b0fca4 | -17.40015 | -46.55864 | 2025-03-03 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9462c815-e733-300d-890e-5d8a68c6209e | -14.45842 | -45.64796 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 082f35a9-8b07-3be1-b020-306bf07acbc0 | -14.00395 | -45.58669 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bf8ea4ec-993c-3ce2-b078-e2bd0e6e0f89 | -13.98419 | -45.57911 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 69c73190-0285-330b-956f-08d312fd10b8 | -13.98895 | -45.57611 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffadbfcf-fc04-3eaf-8eb3-86bd5f07ec23 | -20.34683 | -40.36125 | 2025-03-03 03:57:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 806be5ff-97b4-365b-8260-8461bcc37d63 | -19.96939 | -44.21655 | 2025-03-03 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8a0eb479-0552-34b8-bf5d-98fe047aa304 | -19.83397 | -40.1118 | 2025-03-03 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 33610622-dc34-36d6-9e00-7ca789f40289 | -19.83848 | -40.08149 | 2025-03-03 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 64f0c707-311c-3ace-b4c9-42445d8e3534 | -21.82156 | -44.20758 | 2025-03-03 03:57:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3900844b-942c-384e-b084-6ae8c819b3d0 | -18.19495 | -46.80631 | 2025-03-03 03:57:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c36665ae-8df6-377f-b8df-8db88f1773c0 | -21.81194 | -44.20162 | 2025-03-03 03:57:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6c382f66-ee9f-364f-8098-5736f24551e4 | -13.96988 | -45.56485 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b5b4f1b-a1a3-3664-824a-f522a064c0be | -14.01006 | -45.57618 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6be20a7a-796d-31a0-b9f7-4581cb1fcf04 | -20.35019 | -40.36181 | 2025-03-03 03:57:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c17f8402-505c-3ec4-9f34-9a516c4f049e | -13.98624 | -45.59115 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 00fa1c5a-1a19-3625-b358-29cad7bd092f | -13.98488 | -45.59869 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7955c270-140c-3b45-aa1a-cc641d984937 | -21.80783 | -44.20499 | 2025-03-03 03:57:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 93119c14-b6e4-3cac-ad9b-bfb6a5da65f0 | -21.37218 | -42.48011 | 2025-03-03 03:57:00 | NOAA-21 | LARANJAL | MINAS GERAIS | Brasil | 3138005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 035bc8e5-589d-3788-b389-ae7c6f8f0cf9 | -13.99713 | -45.57765 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 049e8dc0-96a8-32df-82fa-4076c56d9ce7 | -13.99033 | -45.5919 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33175b8f-7fc0-3ef1-99c6-91855c76e184 | -14.72856 | -42.8773 | 2025-03-03 03:57:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba9942e5-21c9-385d-ad6b-a1fb2c534e7a | -14.0026 | -45.59418 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7412df19-4987-36fe-bb9b-a4e1924827c2 | -21.82499 | -44.20824 | 2025-03-03 03:57:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ccc19d8-798f-3fca-b2e0-ee8c4c5257d3 | -13.9801 | -45.57836 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fecbe6d4-7bbe-3533-8535-5809d6c41ccb | -14.00256 | -45.57092 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0e111189-367b-3910-901e-71068ecf3c71 | -14.45909 | -45.64423 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98905f1a-7bd8-38f6-b9e5-a955dd0ef3d7 | -14.01078 | -45.59573 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d0dd447d-e38f-311b-a9ce-cd2275970a3d | -15.7988 | -47.99655 | 2025-03-03 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b34d5916-24b4-3b57-a0bb-868d1a6db75c | -14.00669 | -45.59496 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 255d2dde-57d1-38db-bdef-21d1a0725f2d | -14.00804 | -45.58744 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c7955fa4-302f-3683-a93f-5c9786dd2e26 | -16.04112 | -41.80325 | 2025-03-03 03:57:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da49c1ab-63e8-3537-b7d7-1ed2ad51e2bd | -14.00597 | -45.57542 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f7f261b2-b874-39f6-abd6-9ec1649b1c81 | -14.00328 | -45.59044 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b5a0398-6226-3666-b7f1-115b45b7460b | -13.98351 | -45.58287 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 81a331ff-4875-3b8d-838e-e9e183184a1b | -14.00871 | -45.58369 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 37b8394d-58dd-36a0-947f-7396754099ee | -14.00664 | -45.57167 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6408d7d5-5878-3de3-aec1-4965f03a7358 | -13.98487 | -45.57535 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a70f6a8-c80e-31ad-961e-9a6ca737b135 | -13.98351 | -45.60625 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 323131b2-6cc3-3cd3-a11b-8f48e14393f2 | -13.98215 | -45.5904 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 51ee704e-7893-3521-a5e5-4a76ba39b95d | -22.21278 | -42.84225 | 2025-03-03 03:57:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fa28f53d-7928-3f9a-90da-7d15ca29de78 | -17.39604 | -46.55787 | 2025-03-03 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a83cc97c-93ce-3047-b09d-9d0d00cbb688 | -13.98419 | -45.60247 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6afb3abe-f5f4-34d3-a9a4-fcab4f69be08 | -14.00534 | -45.60248 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d5c0fcb-84fb-3a27-bd8b-7a68419b0868 | -14.00943 | -45.60325 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 836a0bb4-dd01-37a4-b261-bb2cecc79cf4 | -14.00737 | -45.5912 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 83669efe-552b-30cc-ac46-9a3b08eb7142 | -14.00462 | -45.58293 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a15cec91-679d-34d3-ad7e-3af1d48d9d3f | -14.00054 | -45.58216 | 2025-03-03 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README2.md)
