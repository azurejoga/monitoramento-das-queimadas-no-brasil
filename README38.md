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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90ad8520-5746-387a-a0f1-645da9ed23c0 | -17.9937 | -44.404 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82e99950-4fd5-39f1-a675-4b8e2bca18c1 | -20.65494 | -46.56256 | 2026-08-23 04:49:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 50c3c272-e38c-30e5-b85e-e7f2709a15b1 | -17.92831 | -44.49413 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47538feb-fa12-3680-a2d8-267bc9b9535b | -20.3543 | -54.52576 | 2026-08-23 04:49:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d6193a5-4c52-30d6-8c48-93aeacb7e4f3 | -16.57256 | -51.62912 | 2026-08-23 04:49:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eaa89e3f-c236-3e61-ad4f-24e294f0457e | -17.7146 | -43.49908 | 2026-08-23 04:49:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1a0ac00-d1a2-30ff-8633-230d99dc968f | -21.45514 | -46.14596 | 2026-08-23 04:49:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 05fd7993-633b-3750-90de-68824b551293 | -18.77582 | -43.77799 | 2026-08-23 04:49:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beaf79a2-fb39-3436-901f-6e12429f6160 | -21.4506 | -46.14912 | 2026-08-23 04:49:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 549c26c2-d2e4-33da-b801-25a6b22edf63 | -17.2148 | -47.52108 | 2026-08-23 04:49:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9feb668a-57d4-3ab2-b8d7-204f9805d075 | -20.27126 | -48.65879 | 2026-08-23 04:49:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0caa1b56-fcac-3687-8215-c3c1c18710a6 | -17.90992 | -44.50093 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b9032b9-522d-33de-92cf-c79008221d68 | -18.53129 | -47.1611 | 2026-08-23 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 60ed60f1-b2f2-3a7a-af81-e00542947f37 | -19.41719 | -44.34309 | 2026-08-23 04:49:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25bdce34-661a-3570-b987-d919a9a1a4ee | -17.93265 | -44.49449 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53000773-a885-32ae-b645-7668e930228f | -17.75446 | -47.03466 | 2026-08-23 04:49:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d070570c-1636-3f6e-9842-8fc4006f3fae | -18.5276 | -47.16052 | 2026-08-23 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8a0d68da-88bf-3aac-b030-da218bd31d0c | -18.59902 | -47.12368 | 2026-08-23 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 635e3be7-54aa-332b-be78-4de9d33b39b5 | -17.21258 | -47.52238 | 2026-08-23 04:49:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43e877ff-8127-3be8-ab04-e39fc7598fa0 | -17.88859 | -51.67105 | 2026-08-23 04:49:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0111f94f-13aa-3b02-9ac4-2bb4a6eb7425 | -18.51364 | -46.60008 | 2026-08-23 04:49:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50fff5eb-7b00-3305-ad0a-b30841d2168b | -20.35789 | -54.52649 | 2026-08-23 04:49:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4362e9d3-7054-3b10-86cd-0d55e6df997a | -18.5947 | -47.1276 | 2026-08-23 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94843419-e2cb-3093-b7a3-3b37c8d83af1 | -17.92723 | -44.5025 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 687a548d-eed6-340a-ad49-bf9014f5dc43 | -18.95183 | -50.63753 | 2026-08-23 04:49:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1f3563eb-fcf9-3dcc-9335-8b27a708d1f4 | -17.93158 | -44.50277 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2263e45c-5dfb-39f8-8e8f-5c4ce965a314 | -20.662 | -46.56956 | 2026-08-23 04:49:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fccbdb0-f666-3399-9e98-ef0877f8e86f | -19.81905 | -46.92798 | 2026-08-23 04:49:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20ec17c5-6472-3b36-b66e-2fb011ed6da4 | -19.81045 | -45.63922 | 2026-08-23 04:49:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfd044f1-1e0d-3790-a14b-63362c8bdb60 | -20.65884 | -46.56326 | 2026-08-23 04:49:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3dc43a40-4540-3b08-903f-57c82acffeac | -21.4475 | -46.14093 | 2026-08-23 04:49:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 979a5dd0-3ab6-3ded-a822-83fdeecf2fb1 | -22.2838 | -49.60267 | 2026-08-23 04:49:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 54257f9f-b8b5-360f-bee2-dfd24e6cfb48 | -17.83801 | -44.46364 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aed778a1-30ee-337f-aee7-d3dfd78910c0 | -21.45563 | -46.14214 | 2026-08-23 04:49:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 79c2eabc-7f40-36cd-9959-2e08591c5727 | -18.53931 | -47.15776 | 2026-08-23 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e767a190-0c4c-3eee-8c72-ded6265ab06f | -17.64214 | -50.49094 | 2026-08-23 04:49:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c0ee0ae-860a-3496-8df9-bf579b1b24c5 | -21.45156 | -46.14156 | 2026-08-23 04:49:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| bfac857e-e5ff-3db3-a96e-fa1374d1e25b | -18.54443 | -54.75174 | 2026-08-23 04:49:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1158181f-48c9-3c0b-8c9b-3065fa008232 | -20.14323 | -44.92515 | 2026-08-23 04:49:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| feef6762-3885-384d-9dc5-47e14d59eb6a | -21.44702 | -46.14473 | 2026-08-23 04:49:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 62c0d1e8-32e8-398f-b3d2-d1286d051552 | -15.49951 | -57.92294 | 2026-08-23 04:49:00 | NPP-375D | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90f90bd1-2503-39ee-a024-3a1be70c4995 | -20.66593 | -46.57013 | 2026-08-23 04:49:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9103f301-bc44-30f5-b9e0-729e6fbc855d | -19.64691 | -45.7243 | 2026-08-23 04:49:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9d19a98-9746-37a2-8660-e58984391964 | -16.33498 | -55.37817 | 2026-08-23 04:49:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad408181-4450-39a8-9c2f-2941c10d159e | -18.58096 | -46.91497 | 2026-08-23 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3806856-9a9e-38e5-a7c8-c2ed64fd4658 | -20.25388 | -44.05464 | 2026-08-23 04:49:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8b146f30-fa0d-3bba-a38b-9eb2046b79ae | -20.27478 | -48.65936 | 2026-08-23 04:49:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c704faa-723c-37de-bc19-300416533a3e | -17.80183 | -44.40331 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd02c28b-4a8e-3d01-b889-0e012bba34af | -17.92274 | -44.40031 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc00f416-219c-34e2-9450-335414afab80 | -19.459 | -46.81468 | 2026-08-23 04:49:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e137506d-6d5d-353f-93db-8c0ba630454d | -18.9485 | -50.63695 | 2026-08-23 04:49:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e703a3a2-0933-3ec9-abac-ac85765fb43d | -17.92861 | -44.38881 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc66967c-46b9-398d-b663-dd4bb0110e9a | -18.77579 | -43.77633 | 2026-08-23 04:49:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7ce9fea-aace-3181-9279-05a0cd43b4df | -17.96683 | -44.4431 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65da930c-28db-38c4-8cbc-2e2106e1712b | -20.65353 | -46.57321 | 2026-08-23 04:49:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd94d7c2-49f5-397a-9480-c4600cdac811 | -20.49065 | -47.12975 | 2026-08-23 04:49:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 931b9f87-eb2d-3226-a642-58b3e0d9575b | -19.64333 | -45.71982 | 2026-08-23 04:49:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 345fe4d6-feb3-3a48-b8fc-5879c17806de | -18.53498 | -47.16167 | 2026-08-23 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a91e6d5-8cf9-3ed0-b758-ba83e7707406 | -18.99399 | -46.3188 | 2026-08-23 04:49:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a93d75f6-ec42-38dc-a27c-ddac7244482b | -21.45971 | -46.14265 | 2026-08-23 04:49:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 61fbf104-083d-345b-bf55-edab04372d71 | -17.21064 | -47.52469 | 2026-08-23 04:49:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f2b2866-51d7-3e24-93af-864d60e2e314 | -17.209 | -47.52185 | 2026-08-23 04:49:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 691b09ca-6b46-3bd3-bf73-480f6d4273d3 | -17.92223 | -44.40432 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b87f399-c8ac-3424-bd2b-0eb3929cdd79 | -20.67408 | -45.27536 | 2026-08-23 04:49:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 614dde4a-326a-31b2-a4f5-dde5955ff96b | -17.98937 | -44.40336 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cb1c8f2-23c2-306d-b0f1-fe06d25f2f5c | -16.31019 | -53.15821 | 2026-08-23 04:49:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80f3e51d-0586-319a-ab70-178f9f29bd3e | -20.65742 | -46.57399 | 2026-08-23 04:49:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9608e9a8-3053-3e52-9030-ab8f7a68fa40 | -20.66275 | -46.56398 | 2026-08-23 04:49:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e15988ec-56dc-3398-a5e9-03e192af367c | -17.91296 | -51.7327 | 2026-08-23 04:49:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ffc6360-7cad-33f5-aafa-c28e2f8b1d2b | -17.75574 | -47.02544 | 2026-08-23 04:49:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ca51849-a377-3525-8e4d-288a5dd3c776 | -6.8188 | -59.6696 | 2026-08-23 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 86d0d708-864a-3840-8a3e-4da5dd30ef6b | -6.1101 | -57.84 | 2026-08-23 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 5a0719a4-63a7-3ff6-8d86-ee9b5acf8a89 | -6.8062 | -58.6469 | 2026-08-23 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 5fb97ebb-7890-3f73-bfed-06d0f280b4e3 | -6.695 | -58.7291 | 2026-08-23 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| fd82ee47-ffa5-3f62-a8fe-ead0274d39f9 | -6.6765 | -58.7492 | 2026-08-23 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 151.4 |
| a19de243-2444-3e19-84ee-83da9e42a744 | -13.1505 | -51.4281 | 2026-08-23 04:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6f148062-9518-35e0-9f7a-023f84bebde6 | -6.8061 | -58.6663 | 2026-08-23 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 9ba85eef-0e11-3faf-8060-cb34b8b14f43 | -13.1697 | -51.4258 | 2026-08-23 04:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 05921c66-aa03-37cc-9bae-fe7d5283c519 | -6.6766 | -58.7299 | 2026-08-23 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 056de535-a368-3930-8232-934c0f6b49c3 | -6.9699 | -59.0658 | 2026-08-23 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d1046a13-97a4-3d4e-813b-2f22e9a1c371 | -6.6949 | -58.7485 | 2026-08-23 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| d15b898f-6471-3684-8f42-5b4850b39d67 | -16.0706 | -50.4332 | 2026-08-23 04:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 6068347f-baa1-3dbe-8b5b-081f8fcafc38 | -16.0509 | -50.4363 | 2026-08-23 04:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 5d09a145-340f-396e-ac26-b1966380a473 | -6.1285 | -57.8393 | 2026-08-23 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| cbc60d58-2c5c-31e1-900a-2ff7d7353c04 | -6.1286 | -57.8198 | 2026-08-23 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 698eb1bb-0b1f-3a62-bcec-417b8cee3d2d | -13.1509 | -51.4068 | 2026-08-23 04:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 0761588f-67bd-3806-ad43-8db93bf4b9ff | -16.0514 | -50.4144 | 2026-08-23 04:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 5682ed4f-4972-329a-b671-bd23329dd97a | -13.1701 | -51.4044 | 2026-08-23 04:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 95ea2d9b-8bb8-38fc-be92-5f3afdb3ae99 | -6.9514 | -59.0666 | 2026-08-23 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 35e9405a-9e57-34c6-a3b5-d6f8ffd62733 | -23.74031 | -54.58783 | 2026-08-23 04:51:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1649e5c5-7491-36b9-9279-3167a5e18f2a | -28.06142 | -48.67125 | 2026-08-23 04:51:00 | NPP-375D | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e9d978dd-f75e-3e93-8b67-d811117df1f1 | -25.46691 | -49.64928 | 2026-08-23 04:51:00 | NPP-375D | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 8f6c7b6f-6c6d-326c-9681-6e708e5743c3 | -23.73755 | -54.58299 | 2026-08-23 04:51:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 477b1722-0ffb-3ed5-921c-c2aca616a1dd | -25.51231 | -50.04653 | 2026-08-23 04:51:00 | NPP-375D | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 439737c0-a6c0-3dae-91a0-62a9302797dd | -25.4663 | -49.65366 | 2026-08-23 04:51:00 | NPP-375D | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 48989873-dfa1-3e4d-a22e-3b28ed8fec9f | -23.73683 | -54.58715 | 2026-08-23 04:51:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2c4387fe-548e-3a3e-b61a-1ca98567e4f6 | -23.77106 | -54.57669 | 2026-08-23 04:51:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8b3447b5-f4c5-3bae-bbd3-268a3538a8de | -6.9514 | -59.0666 | 2026-08-23 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| cea5924b-defa-3472-b6fc-c69fee528493 | -6.658 | -58.75 | 2026-08-23 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 3cf1ef6b-403f-3235-9eef-3460cee684b3 | -13.1505 | -51.4281 | 2026-08-23 05:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |


[Clique aqui para ver as próximas entradas](README39.md)
