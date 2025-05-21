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
| 528988b2-8067-3674-968f-ec05db571153 | -11.80805 | -44.27686 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cd7cffbc-ef82-3e28-a404-54118ac2631b | -12.42451 | -43.7233 | 2025-05-21 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 666aec6e-1408-3d7c-99da-ca427de96d12 | -16.67734 | -43.88314 | 2025-05-21 03:23:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a999d32d-3274-3a3c-9c6a-ab6178a0e908 | -11.80777 | -44.27355 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4756ff0b-85a8-3ae0-96a5-85c1e90ca187 | -11.80692 | -44.28251 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 19a9ca39-48ed-3039-a653-f8fd62231d76 | -11.80542 | -44.28483 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6498cd0c-5595-3da6-8899-4fdca6660c4c | -11.80659 | -44.27921 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 843ba65e-4201-3f86-a822-e515d2ace925 | -12.42661 | -43.73067 | 2025-05-21 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4ace230e-f115-30d4-ae84-30093519a606 | -14.04038 | -45.51227 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 226aa963-31e4-3b8d-8fbc-1e0385682585 | -11.77973 | -44.28265 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85a51fa1-1a4e-3f97-ba1d-e5d0f8c98b72 | -14.1615 | -45.4837 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ad3e62b-085e-31bc-9199-e168f6416400 | -14.14949 | -45.47446 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d58b0708-a674-32e4-ba42-1f34d5aa0a96 | -14.15534 | -45.46736 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a72033d-0658-3cdd-a8a3-79063765cc81 | -12.86884 | -43.1858 | 2025-05-21 03:23:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c88725c1-e199-3c52-a87d-a301f4d49f48 | -14.16418 | -45.47137 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f9f5350-d0ff-3e2e-a135-19e242bea374 | -21.04117 | -43.2025 | 2025-05-21 03:25:00 | NOAA-20 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 66b603d6-1694-3c8c-8110-269bd678c886 | -17.91852 | -45.53062 | 2025-05-21 03:25:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb9636f2-7a1d-3e23-8f88-366a58c26d25 | -21.62706 | -43.46855 | 2025-05-21 03:25:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ec800814-4e4e-3554-8dbe-83f19b4f70d7 | -21.45687 | -47.35932 | 2025-05-21 03:25:00 | NOAA-20 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6ef50ba6-847c-3599-941e-a86a7cac0dc4 | -22.53912 | -48.81684 | 2025-05-21 03:25:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85025e94-7d3f-3217-8e91-52d6e56f3379 | -21.45267 | -47.3767 | 2025-05-21 03:25:00 | NOAA-20 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4c3a53fb-4f9b-3635-ba93-c229f351e10b | -22.89911 | -43.74982 | 2025-05-21 03:25:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b9b1fdc8-bf21-3e33-a486-e6d8cb7fe2b0 | -21.45543 | -47.36527 | 2025-05-21 03:25:00 | NOAA-20 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1f336136-48f3-318b-9c4f-f164d7e68290 | -21.45405 | -47.37101 | 2025-05-21 03:25:00 | NOAA-20 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 19.4 |
| acaf7878-e990-3f9f-972d-081e5eb0d7ac | -11.0901 | -54.7852 | 2025-05-21 03:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 95dba433-cab5-39f2-a164-5d2890efd223 | -11.0903 | -54.7648 | 2025-05-21 03:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d9782d79-5f19-3465-b55a-a84ff637a287 | -11.0714 | -54.7664 | 2025-05-21 03:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 5544a1a3-afbf-3066-8a06-2b2da44ec0cf | -11.0712 | -54.7868 | 2025-05-21 03:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a9c3996a-d40e-3780-9858-24f29ded1a5e | -12.2946 | -52.4785 | 2025-05-21 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 921d433c-bfce-329b-99c3-9b9ffbe87271 | -11.0712 | -54.7868 | 2025-05-21 03:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b76ebc44-1bbe-3066-8d78-7fea140ee45a | -12.2946 | -52.4785 | 2025-05-21 03:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| f08180b4-c817-3b83-9a5c-202792a1e981 | -11.0901 | -54.7852 | 2025-05-21 03:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6fcb39ef-9bf5-3776-a440-4ed1e4f32129 | -11.0903 | -54.7648 | 2025-05-21 03:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 8fa078d0-8963-37d2-a4b3-354aafd635cc | -12.2946 | -52.4785 | 2025-05-21 03:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9ffda12d-2f20-3775-86e7-c00d848e4ead | -11.0901 | -54.7852 | 2025-05-21 03:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| bb7ede5b-341d-3fde-9cef-d7e49db75d09 | -11.0712 | -54.7868 | 2025-05-21 03:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 4b7fcfd6-7281-3482-80f6-54bd83bd6504 | -12.2946 | -52.4785 | 2025-05-21 04:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 8448e6cc-85c2-3fb6-94a3-da152e5573c6 | -11.0714 | -54.7664 | 2025-05-21 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| cf2ec1ca-9e29-36fd-95d2-56e227185ead | -11.0712 | -54.7868 | 2025-05-21 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f63934e3-7e54-3fef-8575-d64128f0c70a | -11.0901 | -54.7852 | 2025-05-21 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a9782bac-2a61-38c7-a8ae-5b53c2ce967e | -12.2946 | -52.4785 | 2025-05-21 04:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 966cfda1-ffef-3655-8133-4475871fea22 | -11.0903 | -54.7648 | 2025-05-21 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 19981f32-b487-39da-b617-2d046e7bf03d | -11.0901 | -54.7852 | 2025-05-21 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 281c8a78-13cd-38d4-9bb6-f576125c7e2e | -2.95937 | -39.97115 | 2025-05-21 04:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dbf49740-cda1-3df2-8a54-54d504468b65 | -2.95997 | -39.96732 | 2025-05-21 04:12:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fb4cb34e-f2ac-365a-a588-ac1169ab5542 | -7.87263 | -49.67915 | 2025-05-21 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c8cc0b1-dcca-30bc-bc11-67c3825549da | -11.80868 | -44.27264 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb987fab-e332-3d49-bc7f-71c8472df668 | -8.79898 | -49.06701 | 2025-05-21 04:14:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3b5b91f-f1eb-3a51-9d03-9f506a54c4ea | -8.04764 | -49.65637 | 2025-05-21 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 178f83b2-a170-31fb-98cf-099833597feb | -10.36286 | -47.9685 | 2025-05-21 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e497c77-360d-39f8-a9aa-32195405f474 | -11.2358 | -49.49832 | 2025-05-21 04:14:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e75ae70-326f-32cc-a99b-acb6f8b61e0b | -10.34447 | -51.69525 | 2025-05-21 04:14:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96934e9e-d963-3b95-814f-0099c5f1b889 | -9.66439 | -47.56489 | 2025-05-21 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 68b4d515-37a5-3cf2-a19a-d7c93b582684 | -11.79054 | -44.2805 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae224c5d-9aba-3e62-b24c-9c234ae2e329 | -9.33653 | -49.91266 | 2025-05-21 04:14:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53789927-7870-3c70-9a34-b2b4dcb3dcc4 | -7.40888 | -49.66164 | 2025-05-21 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59f23f8c-0a09-39cb-854c-b207dd5dc485 | -11.81419 | -44.28071 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8255583f-20b1-3718-8388-57d99f34f9f6 | -9.5744 | -49.10691 | 2025-05-21 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5223ebd3-4f4d-3dc7-bfc0-35f4cb3f7d72 | -7.95295 | -49.76572 | 2025-05-21 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bcd5e2e3-8780-343f-9c8d-7b6499db1870 | -10.6574 | -44.4981 | 2025-05-21 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c256e20-8099-3105-b4bf-b74ad74cdbda | -9.66364 | -47.56933 | 2025-05-21 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d3a63e9-7b79-3314-a568-e86f3106f7cc | -10.62242 | -51.79549 | 2025-05-21 04:14:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 988bf304-2fdf-358d-97c8-293ead7b3062 | -9.33579 | -49.91682 | 2025-05-21 04:14:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a95ff90-f226-366c-9ed5-d733a15d3f50 | -10.58477 | -48.517 | 2025-05-21 04:14:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b413179-84a4-346d-98c4-2f645c44a078 | -7.4096 | -49.66157 | 2025-05-21 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 581debab-ed60-396c-9573-8ab72a6ba7f1 | -10.90759 | -48.53993 | 2025-05-21 04:14:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b96f2c3f-8e24-38f0-a224-1171d08a64d4 | -8.89811 | -46.91005 | 2025-05-21 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49c4d30d-e082-37b7-a8a1-56168f2ce774 | -10.90676 | -48.54475 | 2025-05-21 04:14:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c342971f-30f9-33cc-8a39-e10817cf4f8a | -7.96615 | -49.69001 | 2025-05-21 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c307d78-3004-3f6b-8a62-7657601ff359 | -10.35014 | -47.81728 | 2025-05-21 04:14:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eda57c52-c75a-3852-b63a-4bfa2afd01e4 | -11.78669 | -44.28347 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac9e90fb-9e96-3562-b00c-6a54a591ea2e | -11.15804 | -48.67449 | 2025-05-21 04:14:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d60346e1-426b-39a3-a53e-ac689cf639b8 | -9.66809 | -47.56548 | 2025-05-21 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29546d17-e4fc-378e-92bf-dce48a296ba0 | -8.79961 | -49.06328 | 2025-05-21 04:14:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b2a19aa-d103-3a4e-a25c-b04803c1ce1c | -9.03347 | -48.94099 | 2025-05-21 04:14:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b9d8119f-d237-38b2-bd02-08725ebe6251 | -11.78339 | -44.28294 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ed84438-3689-39eb-ab54-036181d2780b | -10.88012 | -44.9381 | 2025-05-21 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01d4f54b-3565-3509-9870-8ef3e3269a81 | -9.66735 | -47.56992 | 2025-05-21 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f9e3b4d-55c5-3d94-a77c-792bb5b7c386 | -9.34267 | -48.39535 | 2025-05-21 04:14:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 978c40f6-77d2-3b29-8330-488f2ec29b9c | -11.15637 | -48.68439 | 2025-05-21 04:14:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92c16ca7-08fa-3e8a-96b8-43000383111f | -10.8768 | -44.93756 | 2025-05-21 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d6e5510-21a7-3cfc-b7a2-a22f54ecd09b | -7.20557 | -43.09542 | 2025-05-21 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 01cbae23-3b36-38e3-9d13-cf9d01ce8a5e | -9.33223 | -49.91187 | 2025-05-21 04:14:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f40dc9ba-7a9d-3d9a-a3a9-a19a10e3a002 | -11.58477 | -45.02424 | 2025-05-21 04:14:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 921ef848-68d0-3bc7-a3a5-9b2f5cd02aa2 | -7.56767 | -45.83082 | 2025-05-21 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af1fe483-4dd3-37cf-acc3-e5ef60063ac3 | -10.34644 | -47.81658 | 2025-05-21 04:14:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fd0e5a2-2308-3593-9eee-daf20873d4fe | -11.1572 | -48.67944 | 2025-05-21 04:14:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c6c3c01-4a8c-343b-9fc9-408d0bb80692 | -11.15334 | -48.67878 | 2025-05-21 04:14:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec07d1e5-01d8-31a4-9ac3-c5e49fe61388 | -11.21072 | -49.16584 | 2025-05-21 04:14:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b02c3e2-eddc-3d1c-b002-69bf94b13deb | -10.79667 | -49.58825 | 2025-05-21 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da519546-614e-3528-ab51-ce1b0d19c805 | -11.78724 | -44.27997 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b77f8914-4298-3b36-9f03-219b95caaf7f | -10.24567 | -48.54164 | 2025-05-21 04:14:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 575cbe2b-9be3-3541-b1e6-2db8e7aee07c | -11.23518 | -49.50198 | 2025-05-21 04:14:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| babd10e6-77bb-3325-a1b1-24fea4a8d27b | -10.87348 | -44.93704 | 2025-05-21 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 405dbb00-0a1f-3b1e-a14a-209c09c4e15a | -7.5766 | -45.86407 | 2025-05-21 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12dd66ab-24d8-34a3-833b-30167fe0991c | -9.03753 | -48.94164 | 2025-05-21 04:14:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d5f4d6f2-89ec-32a6-b694-aced0fb7de0c | -10.59736 | -52.8498 | 2025-05-21 04:14:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c07d0e8-c00f-322d-b346-0a6c035569a9 | -11.81089 | -44.28018 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f705a61e-2efa-3bb1-a096-cb33390b5d57 | -11.81034 | -44.28368 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c53c278-4ce3-3e25-a864-778cfc214e94 | -11.81474 | -44.27721 | 2025-05-21 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README7.md)
