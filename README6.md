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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ed28e8b-9fbb-3726-b6d9-4bea63985339 | -14.74969 | -52.65682 | 2024-12-12 01:15:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| d9b36f79-9186-34f2-9c09-0634bde47337 | -14.75857 | -52.65548 | 2024-12-12 01:15:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| c896b737-c9b1-3962-a3d6-b90ff3d2bc9f | -18.04852 | -52.96067 | 2024-12-12 01:15:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 6285a881-bd83-34ac-a23f-dac1f90cbd29 | -14.74081 | -52.65817 | 2024-12-12 01:15:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 255aca4e-7763-3b2d-a20b-d1251c74a01e | -18.04214 | -52.98087 | 2024-12-12 01:15:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 81b6fd62-d1b8-30e8-ae4a-1ae4dd27ee16 | -18.04086 | -52.97144 | 2024-12-12 01:15:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 194a09b8-ef40-3a13-b8c5-880c3039baae | -18.0498 | -52.97009 | 2024-12-12 01:15:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 7ea2f7a4-06c0-35c9-a8d5-f32b805fa149 | -14.74712 | -52.63853 | 2024-12-12 01:15:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 79a2070a-94b0-3f26-9ce9-2e76501ff75a | -18.03447 | -52.99165 | 2024-12-12 01:15:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c75a7aee-c12e-3802-b6e6-8af3e554df32 | -14.74583 | -52.62938 | 2024-12-12 01:15:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 48cd6a10-c2ef-331d-a67a-1b00d3630724 | -18.04724 | -52.95126 | 2024-12-12 01:15:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 5c53d50a-ef4d-31bb-b2e8-3757d8217f2f | -14.7484 | -52.64768 | 2024-12-12 01:15:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| b7275b6a-9d23-3c05-86d4-1eab5433775f | -14.75097 | -52.66597 | 2024-12-12 01:15:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 5b46bd32-1fa4-3937-9ff6-29e5880c2730 | -12.5629 | -57.77331 | 2024-12-12 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3f76735c-e600-34ed-9ad7-d43fa46dbede | -5.1666 | -44.37834 | 2024-12-12 01:17:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e8d303d7-27a4-3ab3-b350-d0e834a58f3f | -5.92628 | -48.06057 | 2024-12-12 01:17:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 6595e53c-7b36-3942-9db7-817b14e5ccc9 | -12.53332 | -57.74128 | 2024-12-12 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1092f111-a6e3-3c36-b0a2-980a413629e4 | -8.6245 | -50.01462 | 2024-12-12 01:17:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b092e967-62d9-3b18-af4f-8e9a938f910f | -11.21227 | -53.82469 | 2024-12-12 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 48a3861a-edf2-3ad4-a832-31f2c4d4252e | -8.30549 | -55.11054 | 2024-12-12 01:17:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 76c6c6b1-766a-3617-951c-5624fa2d8dfc | -5.93613 | -48.0372 | 2024-12-12 01:17:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 3ee50481-e690-37a1-b4de-beef4d50c4e5 | -9.19785 | -49.48096 | 2024-12-12 01:17:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6093d4c0-035e-3985-ba62-0f388f66511a | -11.20215 | -53.817 | 2024-12-12 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 1024932e-f416-39d2-8eed-43a395aa1ec9 | -13.05952 | -52.04237 | 2024-12-12 01:17:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4461402b-b886-381e-942b-c8ca57a189de | -8.62147 | -50.02092 | 2024-12-12 01:17:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2452f9bf-aef5-36cf-be1d-2fa62adc74ec | -11.11507 | -54.66147 | 2024-12-12 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1e2142f6-d7c6-37a8-800a-c43a1ac9bec3 | -5.92999 | -48.06563 | 2024-12-12 01:17:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 172a062d-2b40-3323-8277-b30e32c75bd8 | -11.20465 | -53.83498 | 2024-12-12 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 6259f18e-61dc-364b-926b-67e7cabbd91a | -5.92291 | -48.03918 | 2024-12-12 01:17:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| cff3bab4-74e8-3311-96ad-dfb4ce9ff5cc | -12.56121 | -57.75953 | 2024-12-12 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| d0089c79-0089-3875-bb11-c8d5937ef9bb | -5.93946 | -48.05846 | 2024-12-12 01:17:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 84d01174-ec01-3d83-bf41-bc257b7c3c1b | -12.57206 | -57.75817 | 2024-12-12 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 44f11331-5f6d-33e5-a12e-6d03186f8f49 | -11.20589 | -53.84397 | 2024-12-12 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1ed55ce6-97db-3c44-9da7-cbf4532c3948 | -11.21351 | -53.83368 | 2024-12-12 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f9e1ffe1-c3c5-385d-b8a6-d2e93f60f992 | -10.29222 | -53.69951 | 2024-12-12 01:17:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7f6ddf9b-5b12-3ea8-8f82-770e463d377d | -12.57375 | -57.77191 | 2024-12-12 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1419b04b-6160-32fa-9732-d13f5455943b | -11.82226 | -57.82667 | 2024-12-12 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 28d00fdc-1c29-3025-9922-8e3e2f2eaeaf | -5.92681 | -48.04442 | 2024-12-12 01:17:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 272.5 |
| 744a4434-f0da-3c1d-89b3-84313f71757f | -11.2034 | -53.82598 | 2024-12-12 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 4bbe81cf-8b83-35c5-81b0-f23f438eba76 | -12.5362 | -57.73472 | 2024-12-12 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| c9596030-a265-34de-94f9-6ad2852a52c2 | -5.16724 | -44.38329 | 2024-12-12 01:17:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| f69346b6-bb8d-347a-8a63-0ed6f83837cc | -11.1138 | -54.65224 | 2024-12-12 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| dbe121a9-5e44-3db3-be15-3c1b2b17eb59 | -13.65768 | -52.9416 | 2024-12-12 01:17:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 383a5e5a-e836-3e58-b573-b91f7d6a9887 | -12.5424 | -57.72629 | 2024-12-12 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 16e056c6-5a35-3c32-b566-264b788a7fe8 | -11.12278 | -54.65098 | 2024-12-12 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 036502c9-5ba8-3d31-85f6-38a8c6260516 | -8.69549 | -50.19358 | 2024-12-12 01:17:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b16a9b00-43a0-3ae8-a293-92a0f5cb72a8 | -13.06877 | -52.04434 | 2024-12-12 01:17:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b066d0d5-2bbc-3aa9-8a4e-302d2335c8be | 2.47869 | -60.68973 | 2024-12-12 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 0d303a09-82d2-3c39-9d4d-5bae5887e9e0 | -3.23775 | -46.88292 | 2024-12-12 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 8af7dd7a-cfe8-3f8f-9080-08cf3561de65 | -3.25699 | -51.53183 | 2024-12-12 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 85f6bbec-3971-3044-82da-f6ded938ced2 | -1.909 | -52.83209 | 2024-12-12 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 232c596a-fda4-3884-8e93-4ce5685f7504 | -2.54291 | -54.33292 | 2024-12-12 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a20a9820-2054-358d-88ab-ba868376bf0f | -2.52624 | -51.78945 | 2024-12-12 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 773d3e5d-f0c6-3886-9752-65f527fd90bb | -3.25881 | -51.54438 | 2024-12-12 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d40e7d17-0e2a-33ba-bd58-a7beb2500a24 | -3.25 | -46.87364 | 2024-12-12 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 32b73d68-a494-33a3-a95f-4e33376a967c | -4.10008 | -54.6667 | 2024-12-12 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7cd9c92b-70e2-303b-a8a2-1ba781d8cbad | 3.62062 | -60.38289 | 2024-12-12 01:19:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 93b8792a-d532-3a73-9db3-b7bd21205ac6 | -1.87454 | -54.69039 | 2024-12-12 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 29295b3a-9d3b-3195-8c33-a5db2af6232c | -2.89556 | -54.15527 | 2024-12-12 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d2940240-72ad-3e57-b953-1f5fd2e8bb80 | -1.87328 | -54.68135 | 2024-12-12 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b8b4f43c-9564-3f65-a4ab-bf8c9f07d0ba | -2.41717 | -53.69502 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6d323fb2-8882-3006-b3f8-6f4d05ceba9b | -2.46411 | -53.64233 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 71d25804-3f32-36c2-9011-cadffbd01ee0 | -3.13147 | -53.28725 | 2024-12-12 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c234b73-cd88-38c6-8189-05959b733a34 | -2.30227 | -53.99988 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 333b4bf0-d690-3716-abe2-0c43c193273f | -4.10132 | -54.67562 | 2024-12-12 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 327fb25c-a7f8-3e0c-a591-8feef421c55e | -2.44415 | -53.63516 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 73fd76c5-364a-346e-a546-4edbaace5178 | -4.06786 | -54.30591 | 2024-12-12 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 15971993-32cb-37a8-a4a9-3246146232fc | -2.35049 | -53.87708 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cc022844-535d-382d-83a1-0152e12762f8 | 2.47675 | -60.70288 | 2024-12-12 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bceafe66-8071-37fc-aabd-cde737c128f3 | -2.75805 | -54.15877 | 2024-12-12 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a1c43b7d-085d-3d30-85d1-3dc8128a701a | -2.07701 | -52.28419 | 2024-12-12 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| cfa057cc-8f8d-3de7-93b6-f7283461fea0 | -3.09385 | -53.73577 | 2024-12-12 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a0593aa4-b2d4-31a8-a3c3-c1a2808b864d | -2.5778 | -54.2532 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8357b114-9647-3fda-a696-fe6c45594fbb | -2.26802 | -53.69233 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 67e69a2f-ba47-38a0-8096-857435c462ff | -2.79309 | -54.14792 | 2024-12-12 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| df057a49-86dc-3313-9e45-6904ff5b1390 | -3.09791 | -53.76428 | 2024-12-12 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e0c64de-9a43-342a-ab8e-e9d6b3e2b19a | -1.69828 | -52.78519 | 2024-12-12 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 16f36d18-031f-3829-8e46-7fc6998a1b3f | -3.26747 | -51.53028 | 2024-12-12 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b6d18191-0894-30ab-bfa9-34d82516aef3 | -1.61515 | -54.68106 | 2024-12-12 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e1031aa3-06d3-3b96-948c-819a7cc45f70 | 2.47284 | -60.696 | 2024-12-12 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 780624ee-e118-3481-80fc-0c948104288b | -2.57165 | -51.88352 | 2024-12-12 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c4ca653a-43ce-30a5-8f1b-a1f777d972e2 | -2.45709 | -53.98174 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1db6bc0d-67b6-31e3-b684-6fd6e9fd02bb | 3.62402 | -60.35883 | 2024-12-12 01:19:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7c5420a0-41f2-3dad-bc31-b34c6d58bd83 | 3.29675 | -60.07 | 2024-12-12 01:19:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e9c532b6-4a3b-3a08-94a4-fe088e27d958 | -3.7897 | -47.1074 | 2024-12-12 01:19:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 166afa41-e29b-388f-898e-6c091e4b6462 | -3.25287 | -46.8801 | 2024-12-12 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 3d7f48b3-101b-3870-b911-8f568c776eec | -2.29936 | -53.91337 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8682112e-af19-3150-bd28-9309b7af8ad9 | -4.07556 | -54.29566 | 2024-12-12 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 46bc5def-fbe9-33f0-b1ab-b0c27de04852 | -4.17158 | -48.75272 | 2024-12-12 01:19:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ceb036ff-43cb-389f-be53-9ef500288680 | -2.96473 | -53.72755 | 2024-12-12 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 60fd9996-506b-3317-996c-cccb5f747bc0 | -2.47338 | -53.64094 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 68a9f551-2bb3-352a-910f-88368eaffb94 | -2.47147 | -54.01814 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 44bfff53-9293-34cf-8b17-a1ae7faba03d | -2.4552 | -53.71292 | 2024-12-12 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fa4631fc-431b-30c0-aa9b-fcbdfc83df7d | 2.47469 | -60.68285 | 2024-12-12 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 431df500-9e60-378f-8a2c-f8e56bfff7f8 | -3.10708 | -53.76299 | 2024-12-12 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c5782afc-a545-3e4c-8ec6-7033e956e700 | -3.25455 | -46.90268 | 2024-12-12 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 5186ee04-5e07-303d-829a-22d616823806 | 3.62232 | -60.37085 | 2024-12-12 01:19:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 31.5 |
| bb7f619e-8611-3bf2-8468-46d78a520aaa | -1.90993 | -54.15372 | 2024-12-12 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| f84faef8-57d8-377c-87ac-79ff6c3dd49d | -4.07681 | -54.30464 | 2024-12-12 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f4c9e537-01fd-37e9-9e3f-284d2c404551 | -14.7457 | -52.6683 | 2024-12-12 01:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |


[Clique aqui para ver as próximas entradas](README7.md)
