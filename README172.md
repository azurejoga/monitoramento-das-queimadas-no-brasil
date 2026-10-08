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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdce2cf9-4449-3026-b064-fd5bdfb6604f | -14.93571 | -48.10487 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00e7aff5-ea86-3f12-95e7-be9ae860cbc3 | -8.24921 | -54.66147 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14398903-e20e-3e72-a472-d48a1570d904 | -10.77773 | -46.58126 | 2026-10-08 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5601c94-f4b8-32fa-9fd4-3f80569a8527 | -9.90027 | -44.81188 | 2026-10-08 05:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0601b94d-6b26-3bdb-9ffc-f46c7c717f7e | -10.16825 | -46.7091 | 2026-10-08 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7656d8cf-a94b-3bf5-90ec-10933b11edf5 | -9.40558 | -49.00826 | 2026-10-08 05:25:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b56a24d-c420-3d68-8bf6-5dda558d4d15 | -14.92498 | -48.09089 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41486674-0255-337d-a04c-20eeac4cc92e | -6.72828 | -63.0512 | 2026-10-08 05:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09900c1f-3818-397f-b482-0b2d0e87a9d8 | -8.08003 | -55.30044 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a0c187b-d921-3581-8645-dbb66cdbf31b | -8.08063 | -55.29657 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2e3185d-c414-3728-805d-6a9b3b1c9bc0 | -10.16765 | -46.71394 | 2026-10-08 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 733e883f-f5d5-39e7-91bb-3e1f0772d5b4 | -8.28806 | -50.27095 | 2026-10-08 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9d5ae5e-30ac-39be-b4b4-f6d850e693a0 | -6.9862 | -59.10617 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 909dddf6-5694-3b3b-97a3-91d017cfa197 | -14.91742 | -48.10458 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9989f0d0-bf70-3f4a-ad45-1da139d0691d | -6.99063 | -59.12202 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 429b1358-3b1a-33ca-998a-e8d790c74f6c | -9.26016 | -45.63754 | 2026-10-08 05:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffa55840-35cd-35de-81ad-a0f668a2a966 | -6.99465 | -59.11888 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cafd2b35-fd52-3acf-9ef7-3e416cc246fa | -10.77162 | -46.57881 | 2026-10-08 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6162d832-c4d0-3385-a0fd-c8aae254eb84 | -6.99183 | -59.11465 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaedc3cb-a2b6-30b5-8cd5-0e141ab4b604 | -14.92183 | -48.10319 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6293acdb-0d93-34d3-a5eb-dac514eb1aff | -10.44335 | -46.85023 | 2026-10-08 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba160520-39f4-3b45-bf5c-cda0c0bea65b | -9.90111 | -44.80493 | 2026-10-08 05:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0539ca5-a00f-3ef8-9fb8-68304b343857 | -6.98782 | -59.11777 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1adf2f14-2a46-37b1-87e2-2116ab42a798 | -8.16467 | -54.75075 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e89d0761-b140-3e88-8efa-e4611e5e1129 | -6.99747 | -59.12312 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1140441b-2f9a-326b-a4c5-f9f1f8c9982b | -6.73364 | -63.04319 | 2026-10-08 05:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9a8eb59-88a3-31fb-9845-f9d1c0052aa1 | -6.72807 | -63.05023 | 2026-10-08 05:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57992cc1-ea5e-3eae-bb27-3d48c9f1021c | -11.24578 | -44.87277 | 2026-10-08 05:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c586acdf-62cc-39ea-ad9b-d52998c00a80 | -16.12843 | -46.88789 | 2026-10-08 05:25:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b4b8ff4-5793-36e4-ab2b-f8ed402a5d4e | -6.99645 | -59.10781 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75a20f91-9afd-38c4-ad46-851bdad7f571 | -6.99021 | -59.10304 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59d3f1dc-db1c-3bc9-979f-088540c74eb0 | -8.17922 | -54.72785 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5234f988-2ad1-32fd-bfb2-76330b84e60a | -6.9856 | -59.10986 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d476739a-535e-3ca5-8e99-4d079c5de048 | -10.18551 | -52.56153 | 2026-10-08 05:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40ca4a28-5a76-379e-b98b-a1d5edd332fb | -16.75922 | -53.37661 | 2026-10-08 05:25:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 358972b7-7e60-3302-b060-eb3db994ee33 | -9.39987 | -49.01066 | 2026-10-08 05:25:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 821f2811-e41b-3b91-a70b-e886014283e1 | -19.99431 | -49.08669 | 2026-10-08 05:25:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d5a9c2e-7d45-385b-83bb-bf853d35cb28 | -6.98961 | -59.10673 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a30e8b3-904d-3d9c-8c24-3ca9ac5f2b00 | -8.88385 | -45.60131 | 2026-10-08 05:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11fc642a-68f8-3f37-8fea-48ee0f5fce65 | -6.97705 | -59.95388 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a029083f-e39c-35f0-b846-196f6a4fd62f | -14.93398 | -48.10385 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b5285a78-3c68-3cb2-bfc7-14a4c55f6bc4 | -6.98902 | -59.1104 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9c645ce-c8a3-38be-85fc-c98d6f42f684 | -8.2542 | -54.72576 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27f1b692-e1f1-37d0-bb1b-d0ab83875b96 | -14.92443 | -48.09609 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d40f5309-993d-3fbd-ae63-7d8557c3e076 | -7.0055 | -59.11684 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e7c020c3-e77c-3fe7-9231-00667c0b7990 | -14.92887 | -48.09502 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50be6e3a-dd01-3793-947c-abe6db9f2975 | -9.4227 | -54.77709 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe1f9b0a-9602-3002-ba2b-ea77543d65f6 | -8.08473 | -55.29321 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7101dd69-5db1-348d-9fc9-750acd2d5a19 | -8.98173 | -45.91587 | 2026-10-08 05:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be252733-2664-3fd5-a50e-b0ed10c77d7f | -8.29335 | -50.26918 | 2026-10-08 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b693abf9-4c10-3c73-acf5-a77e83c3e7f7 | -7.44184 | -63.54968 | 2026-10-08 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eb2f2b87-748f-39f7-8ac9-5035bec40a45 | -9.51637 | -54.74598 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc9b41b3-2233-3869-93a2-29a51add554f | -14.92961 | -48.1048 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65f61c85-2ae6-3a19-af84-ba148b9984e7 | -8.25358 | -54.72988 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c9acbc6-ff59-3b6c-850d-cf56e5bfbd31 | -9.37049 | -55.9719 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 859d33aa-2d6a-36ac-956c-f66113418d4e | -8.29355 | -50.26656 | 2026-10-08 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1404f26a-dbeb-389e-a2d2-bca320fb0c08 | -6.99585 | -59.1115 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48d3ad51-99aa-3020-aa0a-be820aaf2822 | -14.66684 | -51.46383 | 2026-10-08 05:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c08bb6cd-22f0-3591-8fe4-34caa7763e8e | -14.36067 | -55.03087 | 2026-10-08 05:25:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb21a861-0b43-3565-babf-df50fb2fee15 | -8.60236 | -63.06638 | 2026-10-08 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b933d37-c55c-3c10-9d49-e53723c258e8 | -8.17626 | -54.72317 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2dc99f47-b5f5-3cfc-bf91-5cf2301db39a | -7.75086 | -54.9557 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c59ebf57-83f4-3a3f-8934-1b24eb496174 | -8.28879 | -50.26584 | 2026-10-08 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28860908-df5c-3452-aacc-5f140ca956a1 | -8.2508 | -61.39136 | 2026-10-08 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9cf3c0f-0ba9-3787-967e-c348053167f5 | -7.45408 | -63.55605 | 2026-10-08 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6dc7aef-a081-3617-9b2b-58476b0b7fe6 | -8.08293 | -55.30485 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 486524c2-b18e-37b9-9659-d9a680e3ac00 | -8.2186 | -56.09163 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bbe4ec4-5977-300b-8a03-704af714aa89 | -14.93353 | -48.10781 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7160ef5a-e19a-36f8-84f1-d6223a7263d6 | -7.8987 | -54.71735 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d98a2d64-9bf2-3ae6-a7fc-25227856a26f | -8.28928 | -50.26333 | 2026-10-08 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43fb3815-9b40-331f-b01c-f99107b59fdd | -16.75867 | -53.38083 | 2026-10-08 05:25:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a21fe48f-98d6-3ce5-bc7f-a5fb9417ef90 | -6.99243 | -59.11096 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a61f1ef6-0110-34f6-a2c3-d9b5e77226ec | -8.08413 | -55.29708 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93ae2564-6510-30b2-98cf-b18492a55fd9 | -10.76926 | -46.57733 | 2026-10-08 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b41a4aaa-1c5a-3827-9c43-85b7a3045268 | -9.26672 | -45.63831 | 2026-10-08 05:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b74a1a4-755f-3163-bbd4-79ddfd484536 | -8.29282 | -50.27168 | 2026-10-08 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b34401a-4d2c-33da-a744-87b26f7fcbe1 | -6.86228 | -59.35257 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 565bffdd-4ff6-33ac-938c-0202bc833a48 | -6.99123 | -59.11833 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2b38b4c-1a9b-301c-86ae-e27910520cfa | -6.99807 | -59.11943 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ea1dfc7-2a83-3aa5-b694-cb093f6c2e23 | -7.75146 | -54.95173 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f963ace8-d736-3ddb-929e-c86f5c1b26ba | -9.64977 | -54.47273 | 2026-10-08 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b2e5cc2-cfdb-322f-8023-fcd69580a389 | -7.43534 | -63.5359 | 2026-10-08 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3910c77-07e7-300d-8d84-61cbec7160f6 | -6.98842 | -59.11409 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 781fe252-5639-3be8-b1f0-200c52d69c5b | -14.93452 | -48.09908 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c14cf3f8-f3f9-3e50-bea7-f0f601f85e9b | -14.35999 | -55.03564 | 2026-10-08 05:25:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9d69bc4-ed96-3725-9743-085a0d86d134 | -14.91565 | -48.1038 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c42265f-cb23-3be0-8212-21ee1dd1bf73 | -7.53383 | -55.83032 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f4bd909-c330-356a-967d-e289363d0369 | -14.92835 | -48.09963 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2f7dae3-90a9-3f6b-ba93-d74c965dcab8 | -16.12989 | -46.88772 | 2026-10-08 05:25:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae33d994-13a0-345d-b219-ddb401126553 | -8.98211 | -45.91652 | 2026-10-08 05:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f72be97c-da6c-3239-9442-0a5a0e7bdc14 | -7.44113 | -63.55378 | 2026-10-08 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d52ca454-902e-3769-ac41-9df09d10f3cf | -8.24998 | -54.72932 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35e947ca-fd4f-35de-aa2c-72ea3fce4d87 | -8.76703 | -61.38353 | 2026-10-08 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 866fd9f3-694b-38fe-85e8-1a14bf99bb05 | -14.36585 | -55.02185 | 2026-10-08 05:25:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bfa1815-7504-31bd-a91a-173e9524985b | -6.4846 | -62.85627 | 2026-10-08 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 192d0623-72d1-3015-8ef7-8dadc5e60e0c | -9.5121 | -54.74963 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 909a0d8d-edb5-350b-86e9-0e972f0df5fb | -6.48814 | -62.86081 | 2026-10-08 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09154517-ffff-3cc8-b2a6-3140e8b5e963 | -7.902 | -61.65224 | 2026-10-08 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6328ae9-b643-36b5-be91-83cf901690d2 | -6.84923 | -59.78915 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49fa41bb-87f2-3416-b5ba-400c1d2894d2 | -7.00208 | -59.11628 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README173.md)
