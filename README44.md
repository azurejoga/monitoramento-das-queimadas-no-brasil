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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44d149c3-7c16-342b-8088-33df2f8cafcf | -15.62271 | -52.78144 | 2025-09-14 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0573ec59-878b-3823-8857-4fb2eefb3304 | -12.69944 | -54.69609 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 4707bad3-b7ca-3534-981d-149a27fb4d5c | -12.67821 | -54.66497 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f7df007a-8341-3d0d-8921-a0a4988d4a4b | -16.09576 | -49.9699 | 2025-09-14 04:42:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1378d4c-6b7d-3309-a619-eb69150bd3e7 | -12.67593 | -54.67825 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e87e519-20cd-3312-ba68-18842d6abd47 | -19.72762 | -45.8636 | 2025-09-14 04:42:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 909b69ec-e343-3a3d-9d6f-4711999f1b9f | -14.41481 | -46.3997 | 2025-09-14 04:42:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59443314-570f-3634-8edb-aab2313129d9 | -12.92111 | -54.74114 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| af0ffae8-8fc6-3fbf-83f9-59bbb086085c | -15.67453 | -52.24565 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 765f2ef0-4bc1-31c3-8da1-909efd0aa720 | -15.54289 | -49.98888 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d085d100-c1de-3683-a133-9103587c3e8c | -14.63452 | -52.10759 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc1eb9cd-7eac-3112-aa12-80c30c91b773 | -15.29947 | -53.78748 | 2025-09-14 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55dcb7f4-f770-3f92-abfe-738007811a8c | -18.62838 | -47.17383 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 381d5705-131b-35bd-aa11-333820284005 | -14.43278 | -43.20614 | 2025-09-14 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d475782b-ae32-3aaa-aeb8-ee7392b05607 | -18.60906 | -47.19662 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9da66941-5b3a-32b1-abc3-651df8afe96f | -15.67784 | -52.24621 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2f25e3b-7165-31a9-81df-ff8e59724ac4 | -18.15716 | -49.19816 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0d333e0e-c636-3cca-b836-8b3194082d52 | -17.82961 | -50.42275 | 2025-09-14 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7190fafc-b3cf-3c09-93ef-6fcb2d70e911 | -15.59709 | -54.75232 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e5b798e-2d32-35ef-989b-dfded90ac5bd | -14.41083 | -46.39906 | 2025-09-14 04:42:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69474fd4-ff07-3911-968b-d3828874e8e7 | -15.76919 | -52.25027 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97c28424-6937-3292-88d3-ffc93c607e6f | -15.18989 | -48.7238 | 2025-09-14 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2252963-2556-3453-b813-11762c940bd7 | -15.08705 | -52.47061 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb8063b8-4749-3c90-8e6d-9c9a5057f47b | -14.62382 | -52.02526 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06778767-2cc6-35a6-be11-25993cbc04b1 | -12.92554 | -54.73736 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 8dae7858-e2ad-3f23-9ae0-f22cc3e4641f | -14.3094 | -46.07498 | 2025-09-14 04:42:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c907398d-b335-340d-91b4-c5256f083333 | -17.32006 | -46.08451 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55d13d8d-4d44-319a-81fc-951eb9553b98 | -17.27679 | -46.12057 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e525b91-74f8-3b6e-894d-646dcdfaae25 | -16.87128 | -49.3508 | 2025-09-14 04:42:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14fb48b9-3a85-380e-ae59-49ad3c688fdf | -13.888 | -48.24841 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea7b069a-d412-369f-9779-371ad3e647fc | -18.72112 | -51.79342 | 2025-09-14 04:42:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5287f200-acbb-307f-b631-dd3b4755c63c | -19.99895 | -46.90501 | 2025-09-14 04:42:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 498425eb-4eca-3a4b-9730-884c6aa05167 | -18.06712 | -50.7399 | 2025-09-14 04:42:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce0e6324-9515-3b1e-8f34-26d89579a001 | -17.79666 | -51.72577 | 2025-09-14 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5343ccb8-4ed8-32a3-a23a-d4cc529fe16b | -12.92847 | -54.74247 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f41701bb-15cc-3258-b1ff-f17c00722dad | -14.62487 | -52.04006 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8404098d-fd2d-379d-ab4b-7a1748756a60 | -15.80582 | -52.21227 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 38eaf40e-ed07-3580-b5cd-59f0e50ec200 | -15.18993 | -52.3179 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc91a264-d67b-334a-8bf2-9f2e49d03505 | -16.54217 | -49.22166 | 2025-09-14 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08f273b2-040e-3431-8ba8-9c331e797328 | -14.36357 | -52.94081 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec5b75e8-9c01-3c05-a299-f3404ff938c1 | -17.31767 | -46.10368 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0573d81f-d838-3e49-84f4-ba1e8ec1d895 | -16.4324 | -51.79703 | 2025-09-14 04:42:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76115606-ca0e-36d5-a9b6-1766eada2476 | -15.64885 | -47.03877 | 2025-09-14 04:42:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78c4ec3f-9f33-3687-9074-263bbff06eee | -19.63306 | -43.73133 | 2025-09-14 04:42:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f304896-38ad-3df2-b695-55884ae218ad | -14.46286 | -47.31252 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48c81291-94c8-34d9-b9ec-7b462650916c | -12.70094 | -54.68724 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 8af4015c-c191-3d02-8560-c46a17450e5d | -17.99637 | -46.96404 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 65f277aa-e8dc-32c1-9e72-01a2bb76c1ca | -18.6279 | -47.17753 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b81b4b9-0842-3e53-b0f9-a4252b157daa | -14.1895 | -46.31797 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26e587df-51c6-35cc-8c6d-c704fb4b88b0 | -12.66934 | -54.67248 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0becc6e-5216-30d0-8ab0-7a3727c98688 | -14.62339 | -46.36357 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c5f6d87-d37d-38ad-b61b-b0d32ae424d8 | -14.63093 | -46.36837 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afcd8751-86c1-365f-a057-28c3ae8e4d12 | -15.76988 | -52.22466 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 92c355ae-6917-3390-90e5-9052baa9231b | -15.76239 | -52.2273 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c8637ad0-7161-34f3-aef5-3d57203549a8 | -12.92772 | -54.74691 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f805f26-1821-3ce8-bd37-296dddf5ad6e | -18.01608 | -46.97095 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 06a41c1c-b1eb-322e-8070-952f96a2fd64 | -15.59425 | -54.74752 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ef625f8-f0b0-3a42-99fc-d9ebf4c76ec0 | -18.01157 | -46.97394 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 998be55f-5edf-330e-96dc-4409c69878d7 | -14.37489 | -52.93512 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77128017-9ea1-3f02-9041-8293dd951253 | -17.60716 | -51.83135 | 2025-09-14 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e43029e5-bfd3-3a1c-9441-1f858afecf0a | -15.57499 | -54.77403 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71822f85-f1f0-3358-98ea-2f0d49229a5a | -14.4849 | -53.93119 | 2025-09-14 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f25f227-1674-31ef-9ee2-78e3b2002e12 | -18.90751 | -47.97906 | 2025-09-14 04:42:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ac2dbc11-2d5c-3631-a179-f0501d8937f2 | -15.18388 | -52.31317 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b46d8bc8-3e55-34c9-9b01-13df6a8944d1 | -15.7755 | -53.48076 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 546f7d35-4d9a-3dfd-bac1-5bf5a4c2b656 | -18.46147 | -49.57403 | 2025-09-14 04:42:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2994df2a-382c-30d3-83f3-bb8dbaf97f01 | -15.6751 | -52.24207 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bab7458-586d-3ef8-9744-01fde3c969b6 | -14.47665 | -47.32442 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 95efa322-c69c-3724-ac8e-f1bdc1dcd23f | -12.93658 | -54.73933 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 05d5c30d-1f86-3504-8226-49304b4db699 | -15.09635 | -52.49782 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b051cd4-4f15-3bdb-b504-2afd48a2de54 | -17.99822 | -46.94975 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 158f3831-b9a6-3bdf-8238-4a88477082cd | -17.29076 | -46.11225 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9fee241-dca6-3839-b6bc-50619bda1543 | -17.17459 | -49.37786 | 2025-09-14 04:42:00 | NOAA-21 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2caaecef-aa78-3151-9eed-074d7e9984b0 | -15.4247 | -58.77879 | 2025-09-14 04:42:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b7bc336-8fad-3e46-b503-a7a00f2ce1db | -12.67877 | -54.70603 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f9da95b0-a747-3f5a-b2ab-f46b5fc94afd | -12.92036 | -54.74558 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9bb54fab-cae2-34bd-bb58-6e52de860fc1 | -17.31865 | -46.09586 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfd411bd-0589-3a15-9a98-13e3e517de13 | -19.25866 | -51.4324 | 2025-09-14 04:42:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57088b15-1fe3-3623-8ff3-9c805ac63e77 | -15.68773 | -49.91498 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c79df526-f896-3141-96f1-3271d932636d | -15.29326 | -53.78238 | 2025-09-14 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68f1e7b5-e4fb-3b3a-905d-4e2a7c1439c6 | -15.19203 | -52.47388 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b9c242c-195b-3f7c-89f2-46ce30d6601f | -14.48666 | -47.33568 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f8eb44f-c720-3a75-aabc-34fa082db398 | -16.44018 | -45.69109 | 2025-09-14 04:42:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 01e6961f-7a13-3a67-a84c-e3c80893b1bc | -15.61937 | -52.78088 | 2025-09-14 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35e9447c-c7ba-3354-873a-ef9f91d6842b | -15.69942 | -54.36415 | 2025-09-14 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c6fa9c5-015a-3493-96e2-427605090f9c | -18.59658 | -47.19812 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d4df889-44c6-33c4-a5ac-b8c302451284 | -14.75833 | -60.21125 | 2025-09-14 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c40cf70-2d72-3acf-bf78-6e4f490ff013 | -15.76862 | -52.25387 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10ef92a5-21c1-356c-a509-f61e63976f38 | -13.88324 | -48.28196 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fac7f550-a919-3766-9cd0-8ff2b58f6e8b | -14.20392 | -46.18007 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a7f97aca-f909-3e0a-bcba-103fb9dc5811 | -18.46852 | -49.57513 | 2025-09-14 04:42:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c00d64fa-8649-3fa5-99ab-c25eda65946c | -14.35439 | -52.95451 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91949ebb-44af-31cd-be55-c619416574c4 | -16.71076 | -54.96177 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 978197ce-4512-350e-bfbf-9d525c35770a | -17.83244 | -50.42715 | 2025-09-14 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 377e797e-bf2f-3915-889c-a132545cda16 | -18.16071 | -49.19886 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9c6d1222-e8a2-3209-9741-00c8108a3bc9 | -15.18838 | -50.10954 | 2025-09-14 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 283b1376-02c4-35c5-8162-046eacb6bf5f | -12.69501 | -54.69983 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 00f49ce3-8b20-3819-a3b2-be565370ff67 | -14.62439 | -52.0217 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06127fb9-d7fb-3d53-a206-ae475e0798c0 | -15.79977 | -52.20759 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| decc829f-bc83-3ebb-909c-cc2cc93192b8 | -18.28058 | -45.3979 | 2025-09-14 04:42:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README45.md)
