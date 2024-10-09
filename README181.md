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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 441b28b7-9544-3367-be4e-f9a2de21fcde | -11.1491 | -60.61134 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4cb96bb-5c80-377c-80ce-ba6169d2a461 | -11.09064 | -61.36111 | 2024-10-09 05:04:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c0d4a8c-1591-3c46-9850-703923f1f3ed | -10.99 | -61.4074 | 2024-10-09 05:04:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec713416-e066-318e-a6ce-61c22c53f8fb | -10.96311 | -61.12333 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8584d7c-2d64-3b8b-9e3f-1cb36272170e | -10.9603 | -60.9879 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5482b99b-0c53-3e05-93b3-7ef4dd7e1a13 | -10.96011 | -61.11784 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b6cb2487-b7b6-3871-8791-85443fc83860 | -10.95927 | -61.12264 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3cb16d6b-452d-3965-8be5-67e22c12955d | -10.95856 | -61.1155 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9037ff3f-92ae-343f-99a8-c29526aa4cde | -10.95775 | -61.1203 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a656b739-6dd3-3edb-ad4d-0d50a4e70a96 | -10.95628 | -61.11713 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04db6cff-c76c-3eb9-8f25-0a805f8b5114 | -10.93091 | -60.95324 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a1df673e-690c-303b-ab53-fd91e2658876 | -10.92793 | -60.94777 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1ab3a40-7d9b-3dcb-a5c5-e9c485d8b753 | -10.92413 | -60.94709 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 702275c0-27a8-3084-b91a-7d0b51f1f40e | -10.92033 | -60.94641 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e6fb71e-a798-33aa-9c52-98b6a43679a6 | -10.91461 | -60.91133 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7be628a-71c5-3976-9de9-802345ca49fa | -10.9138 | -60.91607 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42af3167-3db6-30b1-8778-9d58ec99515a | -10.90297 | -60.93357 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da620a9a-e3e1-3fdb-8020-3d86d9edfe27 | -10.88394 | -61.3453 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc47f754-2da1-3d36-a48a-073a0a51c1e6 | -10.87054 | -61.35329 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7cb4c68-6808-369d-96ba-ceaefb01f615 | -10.82113 | -61.40654 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86c6bcf1-7771-37fe-a6e3-f73cabde1e09 | -11.35327 | -60.56622 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24703f23-6dbe-32f1-ab7c-51d6f8371cf9 | -11.34957 | -60.56557 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 858d7d86-b621-3e9a-987b-c7bc594be3f6 | -11.34883 | -60.56999 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bf12795-95b9-36b7-af3a-7261b5dbb867 | -11.3444 | -60.55106 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b73237d9-eeef-33d0-aaf3-a6c5a948914f | -11.33115 | -60.53944 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a24fcc9-2a30-37de-b3de-aa1a388e9350 | -11.30077 | -60.56146 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d483d5e7-9a18-3f2a-b9b0-5527f62b540d | -11.29706 | -60.56091 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc83497f-4a65-336c-9149-3a642bf79033 | -11.29335 | -60.56033 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41d2fbfe-bf8f-3a7e-9b23-136ca1d82b06 | -11.29259 | -60.56479 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d8326b3-1bfd-332d-93d6-7e8bc3cf5046 | -11.28358 | -60.33307 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bdf70ee7-2c39-342f-bd12-66caa10101a8 | -11.27752 | -60.60817 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ed3f5c6-fa8d-349c-a686-7c0ae0ab03f7 | -11.27041 | -60.38937 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e3bf6140-863c-3721-82f9-6710797dbe8a | -11.26969 | -60.39371 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| be0aa251-565f-38b0-b832-e4f5ec5ffb42 | -11.26895 | -60.39815 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| fdd6f572-365d-3fee-8605-e6d8b92c26f5 | -11.2675 | -60.38424 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4fe43c74-f37a-3175-877d-3e3cb20fb31a | -11.26601 | -60.3931 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b10a5d7b-3ca5-3bc3-a194-fe70fa412949 | -11.26526 | -60.39762 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1a0f4323-5837-3195-8c33-4eff74116dd3 | -11.26448 | -60.49289 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9cb20551-c82e-31c7-8628-b7808e576a26 | -11.26368 | -60.56619 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38a80e8d-bfe1-3372-b11a-2478aece8507 | -11.26235 | -60.39248 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cf9cd4b1-4839-3553-8bc5-ec6ca704b269 | -11.26225 | -60.56392 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 652dbd70-1d2d-3cf0-b71b-8b834921e166 | -11.26158 | -60.39708 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6be58beb-c80f-3e04-956b-d741e31a6a0e | -11.26153 | -60.48784 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3d487cbb-d32b-353f-a900-c5e381d746e5 | -11.26093 | -60.3784 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ea110ce-314a-3c5b-a74e-834bdd81a1e4 | -11.26082 | -60.4016 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9f9af7a7-3452-30d7-8512-986d3ade12c4 | -11.2608 | -60.49221 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ba55390f-07d1-3481-bed9-9ae3c1cf5ef3 | -11.26018 | -60.38285 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54a94be6-27af-3a91-a9a4-a546dbc5be05 | -11.26007 | -60.49658 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 276832d5-51d4-3040-9b03-85c77c70750d | -11.25997 | -60.56561 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a93ba945-5593-349d-84aa-b2c24fe6039d | -11.25924 | -60.56997 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dfd6987-f07a-336a-b825-9766bb13b3ed | -11.25853 | -60.56338 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eebdcb6f-f45c-327c-9b64-2f66376f1a82 | -11.258 | -60.3734 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 78469bc5-5c22-3ba7-a49b-e59ee147f205 | -11.2579 | -60.39653 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce08c9cb-6a7f-34d8-80e3-2c0e9c6dc472 | -11.25786 | -60.48713 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f6ade35-5f1d-352a-8266-00ff854f068a | -11.25777 | -60.56774 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 607c386a-c499-3e55-b1f1-2a51c0abc1ce | -11.25726 | -60.37782 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f62a3ce1-b6b8-3052-a17f-2131ad01775d | -11.25714 | -60.40104 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd850cbf-3a59-31db-9e29-379e65df1aa3 | -11.25713 | -60.49149 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a78dfc4-c27d-322a-84a0-757ec46cfbbe | -11.25702 | -60.57212 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60cd56d8-d6e6-32e7-8ef4-b165e78db879 | -11.25639 | -60.49586 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98a2511a-138b-3799-b12e-d0f265591016 | -11.25625 | -60.57654 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 943348ee-8684-3e11-8da1-2a30a3e974ca | -11.25625 | -60.56508 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b97bd3f-dbcc-31cc-ab15-31ba7f566128 | -11.25552 | -60.56944 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 817f50df-830e-3e3b-bb0c-1d5dac30ed2a | -11.25421 | -60.39597 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e41e300-6d5b-3baa-81d6-e8d93f11ccba | -11.25346 | -60.40047 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dee498c5-bb63-3894-ac66-a6bcb67599bf | -11.25197 | -60.4996 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae7abc58-97f9-3bda-a4e2-086b74a2c045 | -11.25179 | -60.56896 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 442f085f-c147-3fac-b121-51bee5a11601 | -11.24755 | -60.50333 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbc9a570-4085-3273-a709-d3b367aeead8 | -11.24733 | -60.57288 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1fdcafdd-7c1b-3f17-bf70-f045b336869f | -11.24385 | -60.50272 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 690e2589-4128-3691-9809-c33aba3c6e93 | -11.24361 | -60.57232 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d21cccaf-bd8f-3682-8dd9-090fc482dcf3 | -11.23418 | -60.49253 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7cec773-8ab7-303b-b3a7-a19fe67de2a5 | -11.22972 | -60.49645 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d452d505-6dcb-39e0-b0c9-8ecdb20dc82c | -11.22803 | -60.57426 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59c2515c-9f67-3d95-ad86-9c42d206950e | -11.22726 | -60.57881 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac4d65ca-7bf8-3d19-b2bc-a42e7afdb237 | -11.22508 | -60.56914 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07d48abd-50e2-36c5-aaf4-6a636fbd5964 | -11.22193 | -60.38593 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 864ecf92-8a7d-3af9-8c9f-a7a42efd0621 | -11.22117 | -60.39038 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d19bc48-2212-3927-9cce-f6230a8384a9 | -11.18492 | -60.44755 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b9a8c65-d717-3340-97bc-98f241f7060d | -11.18047 | -60.45138 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b15c796-2444-3b14-9309-3b88ce5ec887 | -11.1797 | -60.45581 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e67aa80-5a61-3809-8bf3-477db1164538 | -11.17895 | -60.46023 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbb63191-8de1-3354-a7c2-1d8d6eb0caf8 | -11.17611 | -60.46135 | 2024-10-09 05:04:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94a7f83b-d481-3368-a2c7-72be6071f6f4 | -11.15946 | -60.61789 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d48f8087-e440-352c-be76-145b310fb902 | -11.15651 | -60.61276 | 2024-10-09 05:04:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fba182eb-cc64-3a7c-bb76-2ec930354956 | -13.70214 | -60.69633 | 2024-10-09 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c77e9e6-6cc4-33e7-b0df-0097aa57df5d | -13.42371 | -61.91939 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 720f035e-5d5f-35c3-a1cd-2b28849de209 | -13.4234 | -61.91741 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 551a8cb8-e014-3fef-9f53-ef3d79247679 | -13.42282 | -61.92438 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 194a0f79-2678-3cf7-8707-f2dd64b9f6d7 | -13.42254 | -61.92241 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e76afefa-321e-3414-9d6c-16d46722c133 | -13.42167 | -61.92742 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f685cfa-0c2e-30a1-b7cd-763cd33b3a9b | -13.41984 | -61.91866 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| da7798fa-8cf0-31ef-a11c-af783eed37a0 | -13.41952 | -61.91668 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c860aa3e-aeb3-335e-b1a9-6452e28dace8 | -13.41894 | -61.92366 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 791bf15f-c147-3ab6-b124-a464e423acbc | -13.41866 | -61.92168 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97a0d057-097c-3e54-93eb-348ee43dd5b6 | -13.41507 | -61.92294 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e33d453a-5f76-3665-b1e2-0f9c8eb5af75 | -13.41417 | -61.92794 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 482c0c73-96be-3492-9760-e71ffba9bb99 | -13.41392 | -61.92596 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 60ba6de4-d853-3658-ac67-4b533b7ed41b | -13.4109 | -61.92023 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab4e29a4-cbab-3601-8c13-a0c749b1ba63 | -13.41004 | -61.92525 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README182.md)
