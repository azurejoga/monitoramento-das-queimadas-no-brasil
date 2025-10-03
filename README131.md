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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82ff9895-2864-3775-9085-f5d7b8998a8d | -17.83383 | -44.30471 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6b6973a-711b-3af1-8043-f322b724a613 | -14.41333 | -47.86733 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76598424-f1e9-3bae-b083-4905de5edf38 | -15.21723 | -47.98953 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e8603a8a-2af5-32f3-92ea-299d840b6809 | -12.37784 | -46.5276 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e3505a0-c1f1-3e9a-9287-37d0f7139299 | -14.44333 | -46.12117 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7c910c0-aa34-3461-bb98-88d419d5e2e7 | -13.05109 | -47.0579 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 574492c5-36c8-3d5b-a9b5-999ba94faff7 | -13.33876 | -48.10412 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c485839d-c554-3ccb-9158-329917e57c89 | -19.72381 | -45.88136 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 741130e7-fec9-33ac-9ac8-1abeff721611 | -15.24086 | -50.12439 | 2025-10-03 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91bd13e2-fe0f-3e9c-bb38-bb528fe0f6a4 | -14.74256 | -48.10132 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27164e72-42e0-3fbb-bb7c-5b98299e0b49 | -14.94656 | -47.52579 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e396810-9553-399f-97c7-3793e6bf7f84 | -12.60139 | -47.00834 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a259452e-ee24-307f-a5e0-e47a3d4a7483 | -12.60197 | -47.00449 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a42155f-0f86-3c3f-8792-14b4b0d4e010 | -12.61946 | -46.99795 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2227253e-9162-3c9d-af96-7ef48862380e | -13.26443 | -47.24773 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69d4e471-dadc-37f3-bf0c-1a7324248c60 | -12.64124 | -46.97012 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 24cdf926-f581-3e6a-b5ef-edd0a5cd1fd6 | -14.57582 | -52.46959 | 2025-10-03 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 924053c3-cdc0-3cc3-872f-2d8caa11462e | -16.17187 | -57.58865 | 2025-10-03 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0a41e1e4-5260-3d48-8bd9-c580b2b8d81e | -12.62567 | -46.95584 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17559852-4343-3f78-b0e0-c6e94c7964a1 | -20.38061 | -44.12852 | 2025-10-03 04:34:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a58ecb96-5c5b-34c0-ad46-ad291f931d58 | -14.68441 | -48.08848 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 597926dd-db64-3dbb-9c10-1db03b3245ca | -14.21138 | -46.12609 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fd50fe0-1d7c-38fa-af9c-07c91cd0550b | -13.13599 | -47.84176 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d03250f8-2f39-3549-8a56-6c7b58d44e29 | -14.87672 | -48.29694 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07e764e6-bd0f-3cf3-ac90-393b6edead42 | -12.81475 | -46.91368 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 722e3b01-7d1a-3caf-85d9-04e5dee313de | -18.45491 | -43.70877 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86ff741b-8078-3725-9f6a-5790eba272d1 | -17.05974 | -46.62271 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dc4a2f3-014f-337e-baa2-885aeacdd476 | -16.62888 | -49.41306 | 2025-10-03 04:34:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52e2c50c-3f6b-3136-93e8-568d39e948c6 | -12.49598 | -48.00525 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f56b7410-19a6-33ee-a76f-7271806dd90c | -14.94214 | -46.88563 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 298bfe57-49ca-3f4d-b031-47ef327e1d03 | -15.70409 | -46.27311 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d576a90-0ec7-3322-bc94-d1993fd0a86d | -13.77042 | -47.58397 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c6083671-7214-3073-a007-87084bbcf396 | -17.98488 | -45.01719 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5892d032-8bc5-362f-8634-25fd928ea5a6 | -14.85719 | -48.35746 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfa93018-8f31-399c-8718-61b833b414f6 | -13.7503 | -47.94714 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32af9a8b-3873-3556-adf0-30ff0c80f70a | -11.07672 | -54.78765 | 2025-10-03 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 817b16d5-7ccf-3240-8193-5b60df6cb98b | -14.70536 | -48.20122 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ead64c85-35af-3bf9-a0b5-e397bd5535c6 | -16.04469 | -50.91474 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 128989ac-ab79-3b83-a02e-830c8ddb9aac | -12.6158 | -46.95967 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f7168b2-3a2c-35d4-9ab2-c80e6c66c2b7 | -13.34046 | -48.11558 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4938eab6-649e-382c-8b1c-3169fec99d48 | -14.94715 | -47.52177 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e8dd54e-526f-3233-be57-34f2e782430e | -12.86771 | -46.99986 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9da2956-b6c6-353d-982c-b13b860e8c1e | -13.96948 | -48.12421 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86a054f7-ca41-3223-8462-4e2607ae8435 | -11.90378 | -54.82907 | 2025-10-03 04:34:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9edf39c8-e2f9-3fbb-bd7d-4d0b7aebd09a | -13.6832 | -48.64611 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c67657b4-2c14-3a61-8f6b-6259bc5d2d36 | -15.20304 | -47.99122 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cac1ab9-20af-30ac-9945-b6d5c9fc13b6 | -15.57374 | -46.95785 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dc525f8-6e21-36bc-901d-87b6ff06c92a | -14.57023 | -48.33085 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 164f6fc6-5ce4-30a8-8849-47e91b77fcef | -14.93635 | -49.98914 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cf1cfb2-32a8-3e8d-a6eb-5f9ae51dd831 | -16.26885 | -47.09398 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b55f3cc6-d332-3a01-ba7b-5b3bbcac20f1 | -15.24251 | -49.31614 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cff9447-b5d3-380b-9bce-8fcd708bec14 | -13.31304 | -47.80928 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bff58cba-4c8d-356b-9f61-29801f35f919 | -12.34598 | -54.15917 | 2025-10-03 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98891499-26ed-3634-9453-65575b818325 | -14.89546 | -47.82502 | 2025-10-03 04:34:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b5d0fe8-c7d8-319a-8f44-15c1925680b8 | -13.48677 | -48.57807 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1600576-f496-3eb1-b303-075294c35359 | -12.71638 | -48.57928 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5dbbf586-1d09-3e08-acfe-e5bcc9b5265d | -13.23154 | -48.49754 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9de80394-e4af-3a7d-9af5-4ba879f763fb | -14.93454 | -46.91323 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 53d46074-7a69-3ad7-95d2-2bfe41aae880 | -13.05223 | -47.05016 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 275d1fe4-c040-3a36-8c6c-0c164fa6b467 | -13.97285 | -48.12473 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b566e725-aac1-38d6-9010-81745c84c2cc | -12.85561 | -47.00994 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a24013b-c652-3b7d-9687-bc17ae9055b0 | -13.2238 | -48.50352 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 014af748-6d61-3eaf-86f1-b27a24dbaa09 | -17.62646 | -44.44789 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4cf6f7f-0153-36bf-b8b6-de668847de94 | -14.93511 | -46.88414 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2a9efcf4-6a8e-33fa-b5d7-d5362c5acb15 | -12.80669 | -46.87256 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5094fda1-eaf8-39b1-9ccf-3f7aec9d37e9 | -14.21698 | -46.08697 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e89567d-1b54-36ad-9781-d23da2ba12ee | -13.30677 | -47.2469 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abab1a69-1972-323b-90ce-114bc39d4ed2 | -13.15662 | -47.89718 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06fa2f97-0690-3a05-a868-9bcd92ff4bb6 | -18.22512 | -53.35508 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1a7b8e1-467b-339c-a763-7f1cc03e38f5 | -13.12929 | -47.84047 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 736c1638-3607-331a-8b80-1185ddb1ce37 | -15.34026 | -46.26073 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c891a190-9156-3b23-b7ef-1272409a560a | -13.84102 | -47.92695 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 485a8259-bd85-38cc-b416-5b2c134e63ca | -15.99331 | -50.89851 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5c4838a1-0f20-36a1-b5bb-dd0a1a7b47b6 | -14.73031 | -48.13684 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a61794c5-b388-3b54-9c73-6c6e695b92e5 | -14.19621 | -46.0756 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9e0db39b-cacf-333b-ac2b-a7376f920686 | -13.65205 | -47.30186 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30db666f-f7ba-318a-95a9-3d6dac3bced8 | -15.34942 | -47.06346 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d1c9575-ea12-3252-8351-65d2bb44c369 | -15.30851 | -46.30362 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00a61301-089a-3833-8571-07aa567065f0 | -16.04234 | -50.92914 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7ebcd2b-4587-3bfd-a297-4c1cb56a16f4 | -14.98231 | -46.85847 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f728fc7-261f-3be2-b22b-422ce680c906 | -14.36132 | -46.14591 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f2c5bd2-6d9d-3c99-9fe7-12e5ee0836d7 | -14.20298 | -46.05422 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 39d2735e-9c72-3077-b431-86368573436e | -13.75982 | -48.06558 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b68e7cad-bc1a-321a-857e-e68db5b8ae77 | -15.57903 | -46.94627 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96b895c1-264d-33d5-9d1f-7e03c2278ebf | -12.92376 | -46.3755 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b69c586-ff65-3fbf-9aa7-d4086c9ba5eb | -14.16055 | -49.20166 | 2025-10-03 04:34:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69d2bbab-4cf8-38d3-b01a-c4d4366eba94 | -14.44468 | -46.37526 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cb57e2b-1e95-35d8-9786-dde498a0ed4e | -16.16583 | -57.59464 | 2025-10-03 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4bbb1e6d-6a67-34fa-a538-a56368ebca83 | -13.76862 | -47.54928 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3af8887-8b8c-309a-946b-74046b491d64 | -14.87395 | -48.33787 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8733f895-6b91-3a66-8c96-092e8947ca4c | -14.7369 | -48.09283 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b203c11-8642-3320-b7e8-939b961c8ee6 | -14.90927 | -48.33221 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c40a6871-6736-3273-939c-514d1bbce87c | -14.93051 | -47.01609 | 2025-10-03 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 310d65a3-087a-3e26-8d2e-f0ea971d82ae | -13.96329 | -48.10922 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8b0fbe2-bdb0-3b8a-a1e2-108b47042f88 | -13.15188 | -44.53271 | 2025-10-03 04:34:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c5aa175-d0ed-3b4a-bebb-eebd20d68bc6 | -13.28551 | -46.98522 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5b8fb17-051f-3903-bb02-8513ae571839 | -14.4641 | -48.40425 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f7521f23-fdcf-3dba-9d09-43a6729b0d0d | -19.72451 | -45.87582 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dd9dfc5-f4d1-3cdc-beb8-82a4cdeaf460 | -13.26855 | -47.26728 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f90081da-fb8e-3920-8696-2a1457edeb40 | -15.33592 | -46.29191 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README132.md)
