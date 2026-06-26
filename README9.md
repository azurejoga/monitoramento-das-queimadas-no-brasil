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
| 1ff3ec46-bac3-3d1c-8406-a8f679215b70 | -12.74978 | -44.49247 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d62319f-e8e4-3a1e-b4fd-9078abc82686 | -11.51505 | -56.12984 | 2026-06-26 04:32:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b359bca-8521-3a93-9746-1930f3025316 | -11.87393 | -51.72684 | 2026-06-26 04:32:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b7b16544-e4d7-36f7-9121-d8e90febae6e | -13.7327 | -54.05612 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| bca67bb4-4a60-32fe-9c02-a429fc31b2b7 | -10.39184 | -56.76856 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d9072c43-894f-3d80-b249-64cfc6a00a8e | -10.39098 | -56.77301 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c682d70-65fd-35e7-91e5-b50a50c08182 | -12.55203 | -54.58831 | 2026-06-26 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d8728ce-8012-3467-ba9b-694409655726 | -15.1649 | -49.82606 | 2026-06-26 04:32:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e96f922-d7ae-38f3-8bc8-d789fdd66e9c | -11.37866 | -47.82022 | 2026-06-26 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e74701c-715a-3d9a-a239-4f5e61c5f192 | -14.83732 | -48.12621 | 2026-06-26 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ceeef4ff-56f7-325c-b6a9-f8dbf2523c8b | -10.27406 | -48.30499 | 2026-06-26 04:32:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2c3777b-9f32-3fb7-8c47-a333ad997963 | -13.92588 | -47.34292 | 2026-06-26 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69c25568-0070-3c46-9ef6-a348ccb196a0 | -11.77204 | -46.44682 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f543f48-22c5-3a54-a55b-8f5b9ff47834 | -10.54288 | -47.7128 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4bb7836-5fbd-3dd6-b55b-7cc46115ec5d | -12.5208 | -48.28724 | 2026-06-26 04:32:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9acc5e9-ba14-347e-85e7-495b0d5aff50 | -11.87259 | -51.73439 | 2026-06-26 04:32:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d461dc74-e611-311b-984a-bb5ad676c09f | -9.09556 | -47.52536 | 2026-06-26 04:32:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b05244d-3b02-3af9-8097-029a3af5b2f8 | -11.25271 | -43.32043 | 2026-06-26 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 542516fd-68df-3996-813a-b771e95b1c9a | -14.6958 | -46.15081 | 2026-06-26 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c261bd1e-e406-3136-855f-4d97af00b5c6 | -13.06632 | -53.36016 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f38f5b9-c20b-3277-9c27-cc51ffbc885a | -10.35831 | -47.34787 | 2026-06-26 04:32:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb4c43ae-94ad-317d-8567-b1f38589eb23 | -10.39269 | -56.76414 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fc85978e-8a2d-3cdd-a9bd-b13bf36210f2 | -13.25434 | -54.4349 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b5f535c9-c4cb-36cb-80f1-907e289c786d | -11.63919 | -52.85946 | 2026-06-26 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c9c80e4-07d2-3570-8d0d-f8e4016f3821 | -15.59909 | -48.35952 | 2026-06-26 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ead7e2df-e3cb-3f61-9e3e-9a49da09c755 | -10.11027 | -47.56261 | 2026-06-26 04:32:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d705d41-644e-324a-b2c4-4e45bd77da25 | -10.93888 | -56.8591 | 2026-06-26 04:32:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c28ffc1b-0d24-3a7b-83a5-c19230903684 | -12.86731 | -44.33534 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ae6fa86-ce28-37b6-9cf2-db899a8c85ae | -10.62993 | -47.03041 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 04bcca38-26ce-375e-8956-25353247a06f | -13.73178 | -54.03503 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c22d19f-6847-320b-975a-bae5620059a4 | -9.66238 | -50.70699 | 2026-06-26 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6be9951-d90f-3ce2-83f5-efa5543c734d | -10.56412 | -47.2016 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55af8292-52c4-3a3e-ac14-8f9b43057082 | -12.87247 | -44.34793 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49bf25df-54d8-3cd6-96e7-f088845f1dbe | -12.87018 | -44.3397 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee43abc9-11cf-35e4-b207-cf0da6536ef2 | -12.07042 | -45.77849 | 2026-06-26 04:32:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3733965-5981-36cb-82a4-d97f7e4e5cd0 | -13.45787 | -47.8642 | 2026-06-26 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8182328c-8365-34e1-8ff4-9cbb68f5521f | -13.87801 | -47.1513 | 2026-06-26 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3f9bcf0-e5af-3ca5-9e2e-e9b063e76745 | -12.35501 | -47.42617 | 2026-06-26 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcea747f-c93b-374e-9f24-d3ae6f9e4a09 | -11.91113 | -43.78061 | 2026-06-26 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aca17313-0c12-3023-89f7-6908046a043e | -14.35084 | -54.52898 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bdcfcad-4e3e-323d-84c2-a43d0a3cea89 | -12.43986 | -49.57965 | 2026-06-26 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84255e9d-4d63-3335-8768-463ccce756e8 | -10.38282 | -56.71981 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7315dfe-67c3-3048-9050-bb827dc2807b | -11.77649 | -46.4403 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f93d552-cb02-3392-9b8a-5d6c2bc8a500 | -12.22927 | -46.60873 | 2026-06-26 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3b6972e-1a1d-31f7-b936-1dba980ef473 | -14.21068 | -45.62506 | 2026-06-26 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c5799560-943b-343b-acb1-7a1c815c09ff | -11.38613 | -47.81301 | 2026-06-26 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2a1cb76-dfa3-3b31-88cc-b1cca0fe4eed | -12.518 | -48.28283 | 2026-06-26 04:32:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ee0c819-4435-382b-be13-aff98004fcac | -13.90425 | -47.32833 | 2026-06-26 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a774871-1040-3250-bf9b-54e7d0f0107f | -9.09901 | -47.52592 | 2026-06-26 04:32:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| edcfdd9a-71db-35a0-b6fb-1540fc726b4b | -12.0807 | -54.60825 | 2026-06-26 04:32:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 644abd89-0e8e-3f8c-a2cb-7c4fd0d8e408 | -15.9154 | -47.44874 | 2026-06-26 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c44ca9a-2f50-313e-bfac-eb3ae7a36080 | -11.77147 | -46.45036 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 654d33e3-2694-3bc2-be20-bfa4c3d8d239 | -11.77982 | -46.44084 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70637114-9b88-392c-93ae-7320d3ef671d | -12.74749 | -44.48438 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a606ebf2-5339-3a55-b1d3-0774485c910d | -13.06267 | -53.35458 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e3bf6cd-bc12-36de-b148-0755eb9f7e62 | -10.36349 | -47.33743 | 2026-06-26 04:32:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eec923e7-e64f-3145-b722-38a880c10c40 | -16.42981 | -44.42393 | 2026-06-26 04:32:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83d62efc-eaff-3b36-a3ba-7e89da117e56 | -10.10042 | -49.59106 | 2026-06-26 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4decf7c-4426-370e-9afd-d73b8f0239b0 | -12.6262 | -57.89269 | 2026-06-26 04:32:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f39a1200-95b9-3854-81c6-321f5da9fa66 | -14.69302 | -46.14666 | 2026-06-26 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91078a3a-5b64-3697-83eb-678b8f101cf9 | -10.55897 | -47.21189 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 35e83287-8b50-38e4-8c4e-203960a4516b | -12.51239 | -48.27405 | 2026-06-26 04:32:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e1c00d4-9e4e-34a7-a4ec-b58fba88ec69 | -13.92138 | -47.34959 | 2026-06-26 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d77d237-062d-34bc-8e6e-2601fea89e38 | -10.93394 | -56.85307 | 2026-06-26 04:32:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bac527c9-c97b-38e8-8f5c-fa39cc98396a | -11.94335 | -57.70384 | 2026-06-26 04:32:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81bd23c7-31ac-3b10-9305-60ece36c966b | -10.10573 | -49.58583 | 2026-06-26 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2b14b3b-088d-31db-b07e-2d0f8f507b83 | -10.35771 | -47.35155 | 2026-06-26 04:32:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec3152ed-2ef3-3e4e-8e51-abc49c1a3a5b | -12.75721 | -44.48978 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8347ddda-b0aa-3069-be0b-121b40581700 | -11.25625 | -43.32103 | 2026-06-26 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b61a5448-0ab7-34c7-beb4-64d6704d82f7 | -12.75321 | -44.49302 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a46dc9d6-276c-30f7-ae53-2b279e98dc2e | -11.5158 | -56.12607 | 2026-06-26 04:32:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3309dc7-19cc-38de-a632-459d2e0792d4 | -9.1294 | -47.64395 | 2026-06-26 04:32:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d861fd59-b83c-30e4-b173-dfa56321cde0 | -10.10494 | -49.58716 | 2026-06-26 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d7ecf81-c923-34cc-a1f5-de29898d2cf4 | -14.27865 | -47.41688 | 2026-06-26 04:32:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04436ca3-01ba-3044-b9be-909ee0b0d812 | -10.83608 | -49.38583 | 2026-06-26 04:32:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5410abb-30c4-3fec-a265-1fef037a1616 | -14.34607 | -54.52797 | 2026-06-26 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 168438d7-222c-3916-b490-56777b55213c | -10.16439 | -56.61225 | 2026-06-26 04:32:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e766231-e316-318c-934d-9b5e8023c7e6 | -11.51297 | -56.12239 | 2026-06-26 04:32:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce9ddd5a-60d2-39c6-8ee4-61f2b62b3022 | -13.7346 | -54.04596 | 2026-06-26 04:32:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c77b8ee3-235c-3f9d-870a-b3f230a28a0a | -12.74349 | -44.48762 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60818dc0-c95b-3da8-8305-0a3448213497 | -11.77705 | -46.43677 | 2026-06-26 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f02cffb0-dc29-34da-8a4d-8d6853239e9e | -13.86946 | -47.12822 | 2026-06-26 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b448db3-d4c5-3c20-9ae8-24bf4e2cf251 | -11.51096 | -56.12125 | 2026-06-26 04:32:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3d1af7bb-d66c-3e62-ab0d-3349ee83645b | -11.54545 | -48.26385 | 2026-06-26 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 580ff9d9-394c-338c-ae74-b6fed6b1dc47 | -12.74006 | -44.48708 | 2026-06-26 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16f113a6-a4d8-3071-9b61-2efd25f6b458 | -9.48836 | -57.32583 | 2026-06-26 04:32:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6188ccc-cff6-31f3-b169-daf42700b278 | -11.51784 | -56.12725 | 2026-06-26 04:32:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41337f2e-0ca6-3139-a25a-482f6ff37889 | -10.3601 | -47.33685 | 2026-06-26 04:32:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fbf7f30-119b-3629-9a2b-6de70f6f6452 | -10.10119 | -49.5865 | 2026-06-26 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 370837ec-0d37-303f-89c4-866eef71ff94 | -12.55696 | -54.5894 | 2026-06-26 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ccb24c7-fcb1-3c76-b680-78c7fb922adf | -14.63032 | -54.45845 | 2026-06-26 04:32:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6acd4570-aeaa-3fb4-946a-465f004f0faa | -10.35891 | -47.3442 | 2026-06-26 04:32:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06fa7a7a-1efb-37b8-bc8a-3f2d8a9cf472 | -13.08829 | -48.17571 | 2026-06-26 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84560029-ed82-335e-9521-25cb5d5d2f27 | -15.60308 | -48.35634 | 2026-06-26 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f7118a6f-04c7-30c4-bcf8-ad972d3fed60 | -8.50598 | -50.15321 | 2026-06-26 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dce13ce-007f-35b4-9838-2fd45750f115 | -13.9298 | -47.33985 | 2026-06-26 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b932991f-7148-34da-9c02-f71650e94dd7 | -12.44859 | -44.7527 | 2026-06-26 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d335a306-5a2f-3119-aebd-d4f29922cb3c | -14.59174 | -47.97946 | 2026-06-26 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f83cba1-20aa-3bcf-8676-c0d66ca8d2e0 | -9.89159 | -57.40501 | 2026-06-26 04:32:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 944d2285-37e0-3082-8354-a640dd0d8f32 | -10.27055 | -48.30439 | 2026-06-26 04:32:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
