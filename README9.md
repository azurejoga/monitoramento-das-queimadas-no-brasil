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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5939707e-cd33-3d06-91b7-e85836b9d5c8 | -9.0613 | -65.4542 | 2025-08-30 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 39707a2d-bc63-3c2f-933c-16e713414ec5 | -9.4247 | -60.5509 | 2025-08-30 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 932d4d50-6992-302e-8bf8-aff44b9e411e | -13.3628 | -46.9953 | 2025-08-30 02:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 6e6a2780-508c-3b62-810f-72d09201d6bd | -6.1853 | -43.3257 | 2025-08-30 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 64359b3b-79c6-3052-ac45-e15fcde387a6 | -9.462 | -60.549 | 2025-08-30 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| c4b210d0-8632-353b-9b12-eef6324991e7 | -13.3825 | -46.9697 | 2025-08-30 02:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 6bca3e22-85bd-396c-b9a9-1b009d973359 | -11.8572 | -46.3807 | 2025-08-30 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 172e3645-1753-3fb3-a0dd-102140588e5e | -11.8373 | -46.4287 | 2025-08-30 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 9f664b88-9307-3337-85ac-b63fe46ba54c | -11.8564 | -46.426 | 2025-08-30 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 3d348e45-aca5-3999-bfa8-e8dc6b3197a7 | -9.4435 | -60.5307 | 2025-08-30 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| d80dec9f-2e2e-3651-985b-e073d3da9786 | -9.1155 | -65.7699 | 2025-08-30 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| fe0972c3-62e8-30a5-a769-c7e469a84e5c | -9.4432 | -60.5692 | 2025-08-30 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 9a992335-9994-3dd2-839b-36980f3411a4 | -9.4433 | -60.5499 | 2025-08-30 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 183.5 |
| db0d7091-42b9-3a52-9640-f7ca1ace476b | -11.8369 | -46.4514 | 2025-08-30 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 899a5937-ca86-32d2-b236-25286dda390e | -9.4311 | -62.3493 | 2025-08-30 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 0ab8ae20-49e4-374b-935d-3946ef416557 | -9.4498 | -62.3294 | 2025-08-30 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 39d7c9b7-2102-3506-8af4-5a278dbff45c | -11.8764 | -46.378 | 2025-08-30 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 2867a7cc-f717-36ec-acd4-21f4280f32b6 | -13.3623 | -47.018 | 2025-08-30 02:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 122.1 |
| ca34bab0-ec1a-34d2-a537-2e97974ca10a | -13.9918 | -44.5884 | 2025-08-30 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 43307c33-a1c4-3ba0-ba73-f045960a11e2 | -14.0118 | -44.5614 | 2025-08-30 02:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 20227c42-b606-3def-b56e-20344808e221 | -13.3821 | -46.9924 | 2025-08-30 02:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ac45909d-c159-3908-8939-4998891977f3 | -9.4312 | -62.3303 | 2025-08-30 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 9fb7ffb2-0f33-3144-81aa-fb309ca42409 | -11.8568 | -46.4034 | 2025-08-30 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| debd7aa1-5db8-3003-bca7-985e51362e2f | -9.0614 | -65.4355 | 2025-08-30 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 451f2e15-55e9-3ed0-b731-002a14a4778c | -13.3628 | -46.9953 | 2025-08-30 03:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 74b27738-2c8e-3a9d-9751-6a0e4cac481a | -13.3817 | -47.015 | 2025-08-30 03:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 249.6 |
| 7abf9d70-fca3-362e-9a42-9b447791eaa6 | -9.1156 | -65.7513 | 2025-08-30 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e471be4a-42e6-3c51-a67d-7c96805658e2 | -9.0614 | -65.4355 | 2025-08-30 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 52be6a12-f1fb-3f13-8c21-c777f23ed453 | -9.4435 | -60.5307 | 2025-08-30 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| a961e7c9-0618-31a4-ae93-723cbc4cea49 | -11.8373 | -46.4287 | 2025-08-30 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 5e65beff-8fb6-30d8-a088-d97c6f2e0d58 | -9.0613 | -65.4542 | 2025-08-30 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 7a5a6ee9-69a7-3ee7-b7f0-498b18e27c97 | -9.462 | -60.549 | 2025-08-30 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 7ddaa1e4-9b3f-3b1d-a9c8-b3d4544c2481 | -13.3825 | -46.9697 | 2025-08-30 03:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 6eb830a2-97cf-32f0-b8fc-5f7a5ce6a0e7 | -13.3812 | -47.0377 | 2025-08-30 03:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 02ad99e6-b578-3114-8468-8709bf807221 | -6.1853 | -43.3257 | 2025-08-30 03:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 9ed2f31d-8384-3955-839c-751335365722 | -9.4618 | -60.5682 | 2025-08-30 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 333f3b43-7f3c-38d2-b861-833681a013ba | -5.6081 | -45.0038 | 2025-08-30 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d0fe5903-4bf3-311b-aa0f-45b8984cc608 | -11.8568 | -46.4034 | 2025-08-30 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e557cf4f-1b48-30f3-9b67-fcf2fcf52377 | -12.0153 | -43.9818 | 2025-08-30 03:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 14bf2e6d-ed8c-3ed5-b6a2-d07e2a076ac4 | -8.8843 | -60.7315 | 2025-08-30 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 525c3ccf-2686-3152-a36c-6a284360d214 | -8.9126 | -62.1058 | 2025-08-30 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 5336e2af-bd26-34c6-b7bf-d51088193cfd | -9.1155 | -65.7699 | 2025-08-30 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 694e257b-1206-3974-9be2-871a33019bf3 | -11.8764 | -46.378 | 2025-08-30 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6cc3c9a2-4cb3-3557-a7a1-1671cf62cd81 | -9.4432 | -60.5692 | 2025-08-30 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| cf609c2c-df7a-3211-b81b-397e768afe9a | -9.4433 | -60.5499 | 2025-08-30 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 176.4 |
| b03d2390-69e1-399b-a055-ffb42a6e4ff1 | -9.4247 | -60.5509 | 2025-08-30 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d51c86da-5a3d-318f-98ff-63d6241ad8f9 | -11.8369 | -46.4514 | 2025-08-30 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| bc4ce0a8-39be-349d-9287-a4de9af867e9 | -8.894 | -62.1066 | 2025-08-30 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c5481e64-457c-3ef5-bbaf-0efe2aa0b53d | -11.8572 | -46.3807 | 2025-08-30 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| a8ea5a58-51b7-3bf9-9da4-94f7698dbc8e | -13.3623 | -47.018 | 2025-08-30 03:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 178.3 |
| bf64fd00-641d-3549-b588-973fd354677a | -13.3821 | -46.9924 | 2025-08-30 03:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 3325b776-a851-3ebd-b9ae-afc7a1bed370 | -5.04581 | -37.99441 | 2025-08-30 03:06:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b53bc1ce-65cc-30fd-9044-c938959070aa | -5.25158 | -36.91123 | 2025-08-30 03:06:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fd0378b4-c324-319b-a8dd-2271c246abe4 | -4.98697 | -38.60135 | 2025-08-30 03:06:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 300ce597-2e2e-3835-958d-649436951bc2 | -5.04477 | -38.00031 | 2025-08-30 03:06:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 96ffba9c-02ca-3ed4-8aec-03f582aa7bc9 | -5.04799 | -37.9945 | 2025-08-30 03:06:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 227c218b-1a47-342b-9f66-719d79ea6566 | -5.04691 | -38.00038 | 2025-08-30 03:06:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 18b78677-1a00-3fa1-9130-02ee7272d329 | -4.98582 | -38.60773 | 2025-08-30 03:06:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 06f39b92-f223-3bc5-a489-bd3a6193de9b | -9.49634 | -37.96224 | 2025-08-30 03:08:00 | NPP-375D | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8ce1591b-77e2-3592-b375-0773a6d70b8c | -9.3128 | -40.21685 | 2025-08-30 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c37d1468-b0a6-3d43-a39c-554b0446ce9c | -9.49542 | -37.96706 | 2025-08-30 03:08:00 | NPP-375D | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f32830c4-64d9-3a7c-a8a9-dd3f7800c2c0 | -9.4684 | -62.3286 | 2025-08-30 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 747f4bb9-813f-3a0d-95b0-4c770086987f | -9.4685 | -62.3096 | 2025-08-30 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 34.0 |
| f88b6d56-3453-3399-a441-7e8ae9d7af13 | -9.4433 | -60.5499 | 2025-08-30 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 193.2 |
| 8723245c-d8af-3b51-91b5-c2c587071716 | -9.4432 | -60.5692 | 2025-08-30 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| acf378f0-3a0f-36cb-a5e9-9272ac5405d0 | -11.8177 | -46.4541 | 2025-08-30 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 94918464-73d6-3a31-86d3-b581dffeee46 | -8.9126 | -62.1058 | 2025-08-30 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 9685cde5-43bc-3e79-b011-1511f4579986 | -13.3821 | -46.9924 | 2025-08-30 03:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 763ca50d-fae6-38cd-ab38-f60975cfe1e4 | -11.8572 | -46.3807 | 2025-08-30 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 26bc14ff-358d-31e1-961b-a9a5d81e14d6 | -11.856 | -46.4487 | 2025-08-30 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 4f1ad0ac-3491-3e1b-b423-96bfbec1c8b4 | -9.462 | -60.549 | 2025-08-30 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 42b43925-54c8-3278-a461-450361ac96bf | -14.0113 | -44.5849 | 2025-08-30 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| bb273c98-5479-31c6-a44d-e3d0fe64473a | -9.4499 | -62.3104 | 2025-08-30 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 36.9 |
| a7ba5c14-0891-3de7-b395-fd1547854692 | -13.3825 | -46.9697 | 2025-08-30 03:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| a1ff26da-18e2-3665-a2b7-0c8c1c5e5c11 | -9.1155 | -65.7699 | 2025-08-30 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| c0738c59-d9f1-3026-b107-c55480796e05 | -8.8843 | -60.7315 | 2025-08-30 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 900c7efc-1ea9-3611-b402-6fb5d4b35d55 | -13.3623 | -47.018 | 2025-08-30 03:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| f16805ba-40a2-3fef-bb93-b6c0f514c92b | -9.4498 | -62.3294 | 2025-08-30 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 837c5cda-810e-367d-91ec-fb593dd2849e | -9.0614 | -65.4355 | 2025-08-30 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 4ddf1183-aa02-312b-9b7c-5047c997a0ca | -13.3817 | -47.015 | 2025-08-30 03:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 950172fa-cb49-3de4-9981-67435221b449 | -5.6081 | -45.0038 | 2025-08-30 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ff7e1e3c-7611-3776-9677-680ef68589d2 | -6.7814 | -43.7865 | 2025-08-30 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3e22b3ca-ff5e-3fd9-84ab-979f0cbfdc88 | -9.4247 | -60.5509 | 2025-08-30 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 372e89cd-0b55-3eaf-91fd-a851eb637d20 | -13.3628 | -46.9953 | 2025-08-30 03:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| de18ac68-21cd-3472-bf9e-8e9a4ff1b0fc | -11.8369 | -46.4514 | 2025-08-30 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 52e12064-1397-377e-ae3f-808517db5e73 | -9.4618 | -60.5682 | 2025-08-30 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 00ffe365-c0e3-3bfc-9b14-36ae99e0bd23 | -9.4435 | -60.5307 | 2025-08-30 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| f228a9f0-2ea1-30b1-bda7-cd00a4353629 | -11.8764 | -46.378 | 2025-08-30 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 70bdb7b6-14be-3a3e-9319-d28b67451ccc | -11.8373 | -46.4287 | 2025-08-30 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e8613062-081e-3ba2-95f5-5ef59adb5210 | -15.7838 | -38.93458 | 2025-08-30 03:10:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 92c103b4-34be-3ac4-b4cf-410b27336a1f | -18.49623 | -41.2163 | 2025-08-30 03:10:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9d6d3c5a-76fa-3808-b2b2-8835f4b62a96 | -18.50294 | -41.21857 | 2025-08-30 03:10:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f069d5d9-be45-3483-96e3-71e099abbd5b | -18.50243 | -41.21871 | 2025-08-30 03:10:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1d8e102a-89d1-3f3d-9b4d-9c76bff80141 | -18.49674 | -41.21613 | 2025-08-30 03:10:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7fdb8d7d-b1e1-3d0a-b86c-2684694a35be | -18.50376 | -41.21304 | 2025-08-30 03:10:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 01167607-5d2e-3a5d-a909-7729b2fea95a | -18.50423 | -41.21288 | 2025-08-30 03:10:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 431fd995-f2cc-3bbb-9e07-4b53d1bc82c7 | -14.0113 | -44.5849 | 2025-08-30 03:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 705c05c2-29fe-3bf8-97f5-e587cff56165 | -9.1155 | -65.7699 | 2025-08-30 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d5d0ad6a-e313-3c80-bf04-a98940ad7ff6 | -6.1665 | -43.3273 | 2025-08-30 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 1f66a218-c47e-31fa-a2e0-ffb69dbe186e | -13.3825 | -46.9697 | 2025-08-30 03:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |


[Clique aqui para ver as próximas entradas](README10.md)
