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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7754bc69-6f4d-3d92-9144-929f55f82b20 | -10.58603 | -51.36341 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ed233db-170b-34fb-a233-0e286e019dd0 | -12.67177 | -54.71016 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c9dde9f9-fc18-3ced-b531-226bab879050 | -10.96528 | -58.95866 | 2026-09-13 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3862848c-e9c2-339f-b9e9-c97de39a7025 | -10.68503 | -54.17781 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6739630a-7858-3ce2-b818-14ead34416de | -11.72087 | -46.73529 | 2026-09-13 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0350c929-469c-3969-88ad-db9da41ca3be | -11.19656 | -42.78727 | 2026-09-13 04:51:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 257849b8-b546-3f40-9454-92882a7b01cf | -8.81214 | -46.91614 | 2026-09-13 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e57e8450-603c-37d7-a1bc-19f7a722ac7d | -9.38099 | -50.12007 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 402c8e2a-447e-3450-89a2-4774c735ccd5 | -13.61197 | -47.878 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 814e01de-41fb-3f96-84d4-68f6a5141020 | -13.60772 | -47.88159 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60e44589-b1ce-3aea-87ce-9e0f058f90ff | -9.89876 | -47.59102 | 2026-09-13 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 955dc7ff-d0eb-36da-948e-390dbced3f42 | -11.24075 | -54.14252 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46aba0f0-5111-30ac-a717-1255f302ad8e | -8.03561 | -54.85244 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6eb94f1a-3a50-34db-8e4a-d9635a0548b1 | -9.38986 | -50.12866 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65c363c4-fd59-3f24-b23c-393d67365b27 | -10.68875 | -54.17847 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 55b61373-dd7e-306f-b97c-03de7f3d3756 | -9.88573 | -47.60547 | 2026-09-13 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e55715c-22dd-3e1b-a629-8b8786bf8e0f | -6.59189 | -58.83854 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fefd060b-5ca9-3146-a2e9-7a87db3f058b | -13.30422 | -51.70152 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e4ff455-a493-3016-9d4e-d4bea9338097 | -10.68208 | -54.17265 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6f283159-3b57-3b12-9c91-eeca06fbb51f | -10.68363 | -54.16368 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b2f62abb-3766-3421-9e10-b827583354ba | -6.18703 | -57.71537 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84e082b4-5cd8-3e8f-bee8-9af44dd4ceef | -10.63469 | -46.0999 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffb6b80a-647e-3e15-b940-415184946f24 | -13.75124 | -42.59959 | 2026-09-13 04:51:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 655ccd11-5d5f-39f2-b14a-6ba1d1b13b49 | -6.67471 | -58.88169 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73d38fb8-0515-3274-b2d8-ce7d6ce999b7 | -15.26445 | -42.79864 | 2026-09-13 04:51:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 569277cb-a8a3-3fc2-a162-0e2b9ec355cd | -8.04828 | -54.851 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb33512f-a0f5-3fd6-bdda-ffbba999d502 | -10.97139 | -48.35612 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b072a91a-e823-3faa-b93d-8c4ee1d1e0b0 | -10.21725 | -45.18797 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 471e3319-0d91-373d-94b4-1560e9ed1bbf | -8.02233 | -54.85739 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4858c75-7992-338d-a056-bc902140fcd5 | -6.66762 | -50.91691 | 2026-09-13 04:51:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55829278-b1e0-3dba-b882-671885af5990 | -12.49053 | -48.04108 | 2026-09-13 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b0a4d7a9-f9df-3161-8be8-a7445a9e385c | -13.30134 | -51.71935 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa3a7ce6-6dd9-3de0-a167-99a7dee48fcb | -9.69957 | -54.35215 | 2026-09-13 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1ab7ba4f-aac9-3460-b127-1cac5d45e35e | -11.24888 | -54.13941 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9701e63d-de36-3880-84f5-8683aaeda5ac | -7.46982 | -46.14445 | 2026-09-13 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b344362-064e-3d66-ab2c-d7de9dc5c4e8 | -9.57302 | -55.15827 | 2026-09-13 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 450dd6d7-86b4-3cf1-bb31-079fb2da2033 | -8.21081 | -47.86581 | 2026-09-13 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5584e2c-ccb2-3dd7-8df8-4f33a0983100 | -10.5726 | -51.34959 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94fd970e-acfb-3cf0-9c7d-11e35ee78937 | -9.71563 | -54.34997 | 2026-09-13 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55cb1b76-a68f-3a78-9704-0cf1323f95a0 | -13.61256 | -47.87165 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9b669a7-9110-361d-aa0b-f0d4d7c0603b | -6.34763 | -52.74897 | 2026-09-13 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a7ba818-ea70-3759-8f72-75185a3c7cde | -10.69107 | -54.16497 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4fcda37-4761-34c2-bf56-f06b72035b86 | -8.04023 | -54.84956 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57e7c5f1-9178-33d6-9eee-910a0a0dc1ed | -8.74698 | -46.43655 | 2026-09-13 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9ee68b5-62d0-32f9-a76e-b9e5612bd4c6 | -7.87156 | -54.69722 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cebcdbe6-01b7-3413-96ed-b75065c725dc | -10.51654 | -57.45178 | 2026-09-13 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d09e8c83-82ff-31d8-8fe1-6040cb1acaad | -11.82335 | -46.39788 | 2026-09-13 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1880c82e-919b-39cd-bf8c-be8f4037db34 | -10.94081 | -47.91227 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36a314f7-ef22-32ca-a42f-68e619331f26 | -9.18489 | -59.44703 | 2026-09-13 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4456ef9-784c-3567-9e57-e91d14ef4e0c | -10.57929 | -51.35072 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a9d7830-fd88-36f3-a5c4-bd25373d8896 | -6.60163 | -58.85419 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d26b32dd-fa25-3cb2-a0b1-2c8e57e10ce3 | -10.93436 | -47.9071 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ab64690-1893-352e-a65a-449246bd8539 | -10.63374 | -46.10296 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b285430-6dd0-3ff8-9deb-1063e52d160f | -10.50077 | -51.30472 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b47fdedb-078c-31f5-81e5-f687ffb5e5ca | -7.86172 | -54.6989 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6767dac0-c438-3619-a988-ab6ea8785eaa | -14.9164 | -44.6671 | 2026-09-13 04:51:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a717a6b3-4d3e-3351-a24a-8128512966ef | -8.05349 | -54.84462 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5721eb22-4fb3-36c9-b3b3-a61c85174c72 | -6.11508 | -55.64972 | 2026-09-13 04:51:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48974a44-fc3b-334c-bdff-98b2a9ac1ac6 | -11.06244 | -49.72709 | 2026-09-13 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 051dd437-f387-369b-9d0c-1d1fe7b933dc | -7.86742 | -54.68938 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63468f26-fd83-3bba-a545-55b5929d20b6 | -10.69478 | -54.16565 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4e0b1a6-aec3-38c8-8b55-a12c4bdf37e9 | -6.28498 | -59.93356 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| febdb0eb-58a8-3a4e-b21f-08f3c59165a3 | -10.95972 | -58.96051 | 2026-09-13 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f46e87f-a7ff-3c9a-87c5-0557730b57dc | -8.28085 | -39.97374 | 2026-09-13 04:51:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17af71e5-ec2d-37ff-bcc8-8704824f1eec | -10.47288 | -48.63413 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac778647-9e0c-3e68-8b11-066d61e4ea38 | -9.38154 | -50.11657 | 2026-09-13 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5243006d-2bb0-3594-85f1-03b818c09759 | -13.31194 | -51.71746 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db25f195-373e-3465-9740-fd841da0e2cc | -8.05634 | -54.85239 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c289045b-986f-3cd8-87ed-3f95bbaa77f0 | -13.60346 | -47.88529 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7968be9f-ef87-366b-ad47-acfd4227eaf2 | -11.31675 | -48.54502 | 2026-09-13 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b44895e-cb29-3d01-a4c2-cbd37fd7e75c | -10.68812 | -54.15984 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7be72db6-a79c-37e8-8ad5-37315d6fddd4 | -10.93376 | -47.91113 | 2026-09-13 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2544678f-5d27-3d86-bec4-fe4618c587b7 | -10.63012 | -46.10427 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79344434-bffe-3540-a2e6-fbb6c1246fde | -10.47178 | -48.64645 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57821819-bea6-3910-bae1-d9fcfae1239a | -6.59485 | -58.8534 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ced4d1d-5d96-3246-ad8c-80b9f3f8af71 | -7.876 | -54.71919 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ed917e1-5ffa-388a-ae79-b9108bce8f93 | -11.25039 | -54.13055 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bca94ad1-53cb-39cf-b1ab-f492f0b9e6c5 | -10.7576 | -46.24309 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db30c8b3-a5fe-3acb-acb1-825f674d53cd | -10.57364 | -51.36447 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea057527-3435-37b6-810b-69cc1cc9683c | -6.66931 | -58.88072 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ae1d0c6-1666-3a20-8a4e-6007479f3b8b | -6.61781 | -58.85713 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c6f0083-22bf-3935-b952-fc76be612883 | -13.05262 | -48.7341 | 2026-09-13 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a0290fb-a2ea-385b-bdc8-4e39ea7ccf8f | -10.53944 | -51.38459 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e8d0a6f-b4e3-3776-9e92-75b3b53c4648 | -10.35626 | -46.67781 | 2026-09-13 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c95b2104-e436-3359-b1a9-dd91b92f2efe | -13.61499 | -47.88065 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e1dfd442-9937-353d-b30b-b160a6f70a65 | -8.76942 | -61.3965 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17af53ec-02eb-3c77-ab41-96885bf53940 | -10.54002 | -51.38098 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40d8afac-d9ed-32df-880b-b5d3fb21b15e | -10.5462 | -45.20415 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a6e67db-adcf-3a9b-afff-c4d17e5ac682 | -6.13517 | -57.69464 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ce02c49a-0582-3cd6-936e-5495b6b3e648 | -6.72045 | -50.95517 | 2026-09-13 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 568fb989-0f99-3423-87df-2f1d61219944 | -8.03904 | -54.85668 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 120b1fe6-2731-38b7-a5ed-a1d6e3d053f1 | -8.12153 | -54.81388 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f05af247-6fab-389a-b2b0-aefeeb641c2c | -13.2934 | -51.64097 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0866799d-11c2-385f-a22a-ee8bc57933fa | -6.67193 | -58.71013 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdffdda8-7c00-3ae3-a5d4-1dda691dcdab | -7.86722 | -54.72226 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2eb48d68-a7fe-34aa-a8a2-d222016e2c7b | -6.67532 | -58.87825 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 895b873d-97bc-3fe4-b535-a89390775d98 | -6.72072 | -50.47231 | 2026-09-13 04:51:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66911881-61f4-307b-9d83-504defbb41ea | -6.11432 | -55.65411 | 2026-09-13 04:51:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 208ccab5-fbe2-3cc6-b63e-de7e686fd862 | -6.2807 | -59.92821 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7571409b-7939-3a63-9d85-2162728ab10b | -9.70061 | -43.39314 | 2026-09-13 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README35.md)
