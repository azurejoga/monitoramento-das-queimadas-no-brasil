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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e22ba3db-1835-3451-a902-d4b5ad445966 | 2.5434 | -60.7357 | 2026-02-20 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 77f71349-b326-3287-a3b5-6d56d7558d8f | 2.5621 | -60.5458 | 2026-02-20 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1054e72d-e7ca-35a7-a8a7-6d0055345264 | 0.4648 | -60.3925 | 2026-02-20 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 6ade92ef-df23-3e8d-84e6-24a8830e8c85 | 2.5438 | -60.5651 | 2026-02-20 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f61473c2-7fd0-31ac-b885-53e25346e981 | 2.5435 | -60.7167 | 2026-02-20 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 757fe3aa-ff7b-34ec-a43c-50aa4b096b28 | 2.562 | -60.5648 | 2026-02-20 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 173.7 |
| b4ac4147-df91-36e5-937e-781012188082 | 0.4648 | -60.3925 | 2026-02-20 02:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 15091ad2-ba29-39c2-8573-3b22351345a3 | 2.5438 | -60.5651 | 2026-02-20 02:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 156f76a9-8c03-322b-a950-df889699670c | 2.5621 | -60.5458 | 2026-02-20 02:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 57b1f2f8-83eb-34de-bbb0-7108b85b5cca | 2.5435 | -60.7167 | 2026-02-20 02:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 1da7ef46-46e1-32b6-9e0f-ca37b1048263 | 2.562 | -60.5648 | 2026-02-20 02:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 220.8 |
| 3d931fce-c894-3a5b-b2f8-8e3c2f7f4527 | 2.5621 | -60.5458 | 2026-02-20 02:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| ad065ac0-2c7d-3de8-80bd-2b0fab114cd3 | 2.562 | -60.5648 | 2026-02-20 02:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 179.2 |
| 9ad93665-992f-3fb3-9789-d1107ad60256 | 2.5438 | -60.5651 | 2026-02-20 02:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2027ce2b-a4f6-3256-ae38-e5d9e7c44206 | 0.4648 | -60.3925 | 2026-02-20 02:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c9c54be9-956a-3e92-8b80-02bb523e4161 | 2.5435 | -60.7167 | 2026-02-20 02:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 08c6733b-0aff-32ec-ae41-292d9b41728c | 0.4648 | -60.3925 | 2026-02-20 02:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a5749e69-dcc9-3b30-94a6-c25763d4b090 | 2.562 | -60.5648 | 2026-02-20 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 63cae8fe-6312-3f70-bf86-d1f6d6bc7c44 | 2.5621 | -60.5458 | 2026-02-20 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| e815f820-8642-3349-8444-f8a67b108b16 | 2.5438 | -60.5651 | 2026-02-20 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 5bd93dd3-35dd-3aa3-bc12-b2c7c7f44569 | 2.5621 | -60.5458 | 2026-02-20 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f20f55f3-0b3a-3acd-b194-68c9bec99009 | 2.5438 | -60.5651 | 2026-02-20 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 211e747d-e28b-3808-8034-4040f3c538bf | 0.4648 | -60.3925 | 2026-02-20 02:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 0c11c7e4-6f12-340e-a9ff-d032429ca03d | 2.562 | -60.5648 | 2026-02-20 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 166.9 |
| 329f7996-a672-3a61-b2b9-4a31867f8f0c | 2.562 | -60.5648 | 2026-02-20 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 121.0 |
| d0aba5a5-358d-3785-b9ea-37a90f0ea75e | 0.4648 | -60.3925 | 2026-02-20 03:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b38f4aa5-eed1-374f-82ef-e810aba0b80e | 2.5438 | -60.5651 | 2026-02-20 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| fef35f11-ba61-3791-8c17-31dffe906194 | 2.5621 | -60.5458 | 2026-02-20 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 29627652-7f49-3cba-8a88-fb558d0d353b | 2.562 | -60.5648 | 2026-02-20 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 828938da-7a85-30b6-b5cb-c3213b41af54 | 0.4648 | -60.3925 | 2026-02-20 03:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 7e1935b7-9f6d-3c00-bc81-90048cba275c | -7.20703 | -35.78088 | 2026-02-20 03:17:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 600dbedf-5b45-3d46-9860-51ee319ce847 | -7.20568 | -35.7789 | 2026-02-20 03:17:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb57a0b7-c7c5-3e6b-8a20-0fadc2bbf009 | 2.562 | -60.5648 | 2026-02-20 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 489e2bd1-2776-310d-9fba-bae231ee9b69 | -21.69057 | -41.98964 | 2026-02-20 03:21:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bbfbfcf0-f46d-3561-95cc-74818dc33cbc | -18.43348 | -39.93354 | 2026-02-20 03:21:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| b2edcf7a-9698-3961-b83a-d91b777f16f8 | 2.562 | -60.5648 | 2026-02-20 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 1ec38c17-7cdd-36a6-bebb-a72402ce3386 | 0.4648 | -60.3925 | 2026-02-20 03:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 60971a3e-45a9-3951-95d2-6bafee4dc00f | 2.562 | -60.5648 | 2026-02-20 03:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 15252869-7190-39dc-9d5b-0c305ea43292 | -7.20603 | -35.778 | 2026-02-20 03:49:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc47866f-0b78-3bce-910d-86ef10a7c4a9 | -7.2088 | -35.78202 | 2026-02-20 03:49:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9db43649-6f6e-37e6-a689-21ef8b8dd38d | -4.87535 | -38.37275 | 2026-02-20 03:49:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d2fab9fe-c051-35cf-a99f-e301536f00f1 | -7.20547 | -35.78149 | 2026-02-20 03:49:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ec88c936-0b7e-3b96-8f8d-71a2ca682d3a | -5.18392 | -35.55632 | 2026-02-20 03:49:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1a749307-57de-3c1e-9f24-97cb40b2909a | 2.562 | -60.5648 | 2026-02-20 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 112.3 |
| fec39d09-8a1a-3d6d-8a86-803a0f298d10 | -9.98821 | -44.46039 | 2026-02-20 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c6a84dc-79f3-3c24-90bb-f372f2cff999 | -9.99325 | -44.4613 | 2026-02-20 03:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89292175-1f36-36ca-8e20-a14cea83b386 | -20.74082 | -50.54275 | 2026-02-20 03:53:00 | NPP-375D | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 681374e6-6993-3023-b720-732827b71418 | -20.934 | -48.66501 | 2026-02-20 03:53:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9a56f10f-235b-3aa1-b574-f5dbb06fe472 | -19.03497 | -40.97636 | 2026-02-20 03:53:00 | NPP-375D | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bead6471-b89b-325e-839f-c3cc86309c6a | -20.9287 | -48.66347 | 2026-02-20 03:53:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a5169616-9a8e-3e83-9532-a83a578f627b | -22.25201 | -47.22726 | 2026-02-20 03:53:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 242fc826-8dd4-30eb-9d55-131890aa2b80 | -18.69721 | -40.01526 | 2026-02-20 03:53:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d4f4300e-1b3e-3fdd-81b5-81754c049a15 | -20.93481 | -48.66135 | 2026-02-20 03:53:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ce84a5dc-8ad0-3ae6-9b42-eee04fb21dd9 | -17.24333 | -39.23162 | 2026-02-20 03:53:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 18584898-6b1d-3060-a56b-faa3fe8c3005 | -20.92949 | -48.65987 | 2026-02-20 03:53:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 296c0b9e-83c1-3753-b56e-ba300b21a5bd | -20.52375 | -49.12652 | 2026-02-20 03:53:00 | NPP-375D | ALTAIR | SÃO PAULO | Brasil | 3500907 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddee714d-1f48-397e-9c10-6152c34cf21e | -19.30327 | -40.3416 | 2026-02-20 03:53:00 | NPP-375D | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 71228bdf-6d68-3122-9c86-7afbfa8a32a8 | -18.43433 | -39.93182 | 2026-02-20 03:53:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5665e072-c1e1-39fc-b31a-f5740724b0c3 | -22.40122 | -47.10312 | 2026-02-20 03:53:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3426310-0a0a-3082-a915-949aeef54f43 | -20.93559 | -48.65779 | 2026-02-20 03:53:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a1b6044a-19af-3a02-a012-03cf692ffacf | -20.74187 | -50.53819 | 2026-02-20 03:53:00 | NPP-375D | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ea57a634-c8d3-359f-b458-8cb88f241bcf | -22.30173 | -47.17654 | 2026-02-20 03:53:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1835a23-2062-32dc-a730-cd3e498b079e | -17.24395 | -39.22786 | 2026-02-20 03:53:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2f8936f8-8268-376a-83b7-5ac5101e74d7 | -18.96879 | -52.93285 | 2026-02-20 03:53:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4fecf0e-4a32-3fa4-99c9-244219b47a73 | -18.43366 | -39.9357 | 2026-02-20 03:53:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 79db1ff2-8f8b-330c-aee3-38c441dd1f04 | -22.40188 | -47.10249 | 2026-02-20 03:53:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9aa92f1-4c2d-3d5a-964f-7f8b3389962f | -18.97051 | -52.9258 | 2026-02-20 03:53:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ee3b686-bd2d-30f2-aabe-b01589a904a6 | -22.9333 | -48.67651 | 2026-02-20 03:55:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a2cc435-3ac8-3721-b0db-e90d3d80c3eb | -22.93325 | -48.6768 | 2026-02-20 03:55:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f16bda7e-f4c4-3b5f-bae6-ab6acfbbbf3d | 0.4648 | -60.3925 | 2026-02-20 04:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 62f31ea7-4b17-3086-b20e-b59c3b7fa5f9 | 2.562 | -60.5648 | 2026-02-20 04:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 91.0 |
| d0666565-9a2f-3161-b543-8f093e4a8e8a | -4.67724 | -37.80119 | 2026-02-20 04:08:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3536ead5-d4bd-3871-a900-d9af37f5a3a4 | -4.8785 | -38.22452 | 2026-02-20 04:08:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fa7aff92-0f4a-3872-adb1-8008b587d4c7 | -7.20346 | -35.78019 | 2026-02-20 04:08:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 15691042-5b11-3c21-9307-4be80ae97146 | -5.093 | -39.71031 | 2026-02-20 04:08:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 21623d06-50d4-3f54-8b59-cc1d3b7cc7f0 | -7.20778 | -35.78081 | 2026-02-20 04:08:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8dd4caed-211a-317a-95f8-c24bf4d332ac | -4.87405 | -38.37485 | 2026-02-20 04:08:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 91343625-2b6a-37e6-bce3-b8b004d52850 | 2.562 | -60.5648 | 2026-02-20 04:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 103.3 |
| ea54ba16-3568-322c-99fd-ad04b6b01f7f | -11.84451 | -49.22776 | 2026-02-20 04:10:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 269dc64c-3684-3a03-9036-c84b0292b89f | -9.99129 | -44.46154 | 2026-02-20 04:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96f6bf3d-23bc-3389-9715-433d3337c357 | -11.84092 | -49.22271 | 2026-02-20 04:10:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bfcd1ec-4b96-3b26-b987-c5298befb4d8 | -10.91991 | -49.43723 | 2026-02-20 04:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b75e67b-bbc4-3b5e-a0c3-68338b66aa33 | -8.54062 | -44.3204 | 2026-02-20 04:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccd4f700-3beb-39b6-a161-33f665ad98a4 | -11.84527 | -49.22346 | 2026-02-20 04:10:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97d3c478-0f49-3f49-8913-0043cbb057c4 | -11.84169 | -49.21841 | 2026-02-20 04:10:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acfed7f2-a981-38c1-89dd-6dadd8de4209 | -10.92073 | -49.43269 | 2026-02-20 04:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ab5b133-ff96-3b9c-9cea-b8119d7731e5 | -17.24174 | -39.22852 | 2026-02-20 04:12:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 21f1ba2f-f1c3-3b3a-9085-b657c856533d | -15.49559 | -39.08735 | 2026-02-20 04:12:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| cb87e92c-a196-32a0-9b63-65edc94c65c4 | -15.49629 | -39.08223 | 2026-02-20 04:12:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| cb5fdd3b-9823-3238-a8a0-2932d5bd0bf1 | -15.49951 | -39.08792 | 2026-02-20 04:12:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| f6f443f1-13d7-36fa-92e7-fb6340381605 | -18.43223 | -39.93536 | 2026-02-20 04:12:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a337b57d-3815-358e-bc4b-87749f3cedae | -22.93513 | -48.67415 | 2026-02-20 04:14:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78e1c478-7f0b-3ab8-98af-f3ac838bf890 | -22.02158 | -49.50368 | 2026-02-20 04:14:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f63ba733-8fc0-35a5-bcf7-6205249b2c9a | -20.47777 | -50.37689 | 2026-02-20 04:14:00 | NOAA-20 | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c02c18c0-2665-341c-b695-a6ef534d7ae4 | -21.69188 | -41.98916 | 2026-02-20 04:14:00 | NOAA-20 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3d3df5c7-42da-3496-825e-fad0c37ad0ee | -22.85694 | -42.34638 | 2026-02-20 04:14:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0666536f-98ef-3047-8881-07ef52e1969f | -20.93619 | -48.66086 | 2026-02-20 04:14:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0af9507a-8899-34c7-a91a-25fd87762da4 | -20.21291 | -50.749 | 2026-02-20 04:14:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6cc2c812-76e2-3fae-bf17-f1833bf15c84 | -20.93256 | -48.66008 | 2026-02-20 04:14:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 77af9b98-a744-3fd5-b95a-549d0653cd90 | -18.97307 | -52.92596 | 2026-02-20 04:14:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README4.md)
