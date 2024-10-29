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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73197a41-1cd2-3744-a2e6-e1849f487546 | -2.8507 | -53.32796 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 866cf3d5-7090-3861-b10f-20f9af598795 | -2.84822 | -53.34466 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb1bc3c6-4f0d-36fb-9b12-79a75d91a1f4 | -2.84575 | -53.3272 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 180c5bae-d086-36f1-8255-f55216e146db | -2.84327 | -53.3439 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1cc7d9c-f208-3b81-a4cf-5b8acff66604 | -3.53408 | -53.52246 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51cffb12-372a-392e-a8cf-d5aac1dce9a1 | -3.47608 | -53.25323 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d9ffe2d-0a88-3cfd-a5bf-20b4a9cfe429 | -3.47582 | -53.25352 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86291b33-8423-3e00-8fad-18ae43a38d76 | -3.47564 | -53.25611 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d75e634d-982c-3a49-842a-bc67409dcd19 | -3.4754 | -53.25639 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20733edb-0e75-3759-87d1-657d50b7bfd9 | -3.47147 | -53.24972 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd19e44f-668a-3a9c-8471-edb4f87c7c23 | -3.47119 | -53.24998 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 917f5cfd-8fe9-3c1b-84e9-1f826d7ce846 | -3.47103 | -53.25262 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fd217c6-26df-3471-a334-cae37589f716 | -3.47077 | -53.25288 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 311f56fc-d34b-3067-8849-75da59012acc | -3.41638 | -52.83685 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80e8fde7-75ed-3050-876c-382ff8a56776 | -3.41119 | -52.83627 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd781138-365a-3430-9ebe-44f741be09ea | -3.68177 | -52.28137 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fb26ba9-7016-36c3-aad3-7cd7788e079c | -3.67739 | -52.27375 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abf71c8a-2b05-3cea-9e13-a08cf04ea5fa | -3.67689 | -52.27719 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36e4f4ec-bb2e-3178-bc90-1e0820fc9f33 | -3.67638 | -52.28063 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26edf705-7f83-3063-8dba-e30e6ae483ab | -3.43691 | -52.48631 | 2024-10-29 05:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 671d356a-17a9-3456-9250-44eb9cc89190 | -3.73987 | -53.4066 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7175cea4-e28f-35a5-aa96-691abdb59d28 | -3.73945 | -53.40942 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e9cc860-ed0e-3c4c-a3f4-4a073583f8c6 | -3.88659 | -52.38324 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3779f08f-82b4-37aa-a1f7-dcf6c56e7f03 | -3.88614 | -52.38633 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7fa77ec-fc63-3bdb-b880-6a5e715ec2dc | -3.88162 | -52.37981 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd54d1da-d7a6-3d4b-9887-83a2bfd17b28 | -3.88119 | -52.38272 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46660959-719b-3166-aeb2-e354fe0d0d93 | -3.88077 | -52.38558 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12cbd067-bf55-37f3-896b-ce9798575841 | -3.88032 | -52.3886 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d461afd4-07ec-31e7-b020-2900b16225c1 | -3.83256 | -52.41591 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0e78e1a-231b-3c8f-becb-9b04992b1ca2 | -3.72148 | -52.34647 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1006f3e1-1c33-35a3-a462-f06764dd46e9 | -3.71612 | -52.34565 | 2024-10-29 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0a44ceb-ef46-340e-b810-2e75b160f24a | -1.20981 | -54.17534 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e57cdeb-63bc-36d0-92ba-2a476364747d | -1.20531 | -54.17434 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97018687-be3e-3782-a70b-71c35da3b85b | -1.18432 | -53.50726 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6e793cb-843b-3545-9b0f-e79f90402954 | -1.18357 | -53.5122 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9db51702-7257-344c-b4f4-df3e62d7a02c | -1.1834 | -53.51034 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae4d67a6-ccde-3d9c-93d9-b0c062b08ee6 | -1.18117 | -54.18013 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c9d76e6-1f13-3958-aa75-bdf86afd1ff5 | -1.18049 | -54.1846 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6b5b10a-827c-3c16-b70c-9c70a61e4f7a | -1.17966 | -54.1826 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0dbac5e4-ba07-37bc-b807-35e0ac833fda | -1.17954 | -53.50663 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa11b004-728d-3423-97d1-652685f7b413 | -1.1794 | -53.50487 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64f18b5f-322d-38e4-b96b-3410d730e5d6 | -1.17865 | -53.50957 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38ff7f46-0a46-31af-8b1e-24a643e2a973 | -1.17596 | -54.1838 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 526b4ec7-a125-3c4a-bc22-b6669c7f8c65 | -1.17477 | -53.50592 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf84e1a2-e2eb-398a-9e83-d469dadab1bd | -1.17464 | -53.5041 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99d2669d-6c47-3252-8bfb-5c0a608b3b10 | -1.17079 | -53.49996 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efbc3803-b691-3b26-b5c0-b0e66965de8f | -1.17001 | -53.50513 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 856863aa-4650-3b53-9153-327da7c7302c | -1.16989 | -53.50327 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94ff8054-b5a7-3bf4-8842-c98a93b8f39b | -1.16464 | -54.18938 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3b7212f9-2b0f-36c3-a41e-7c0f578e535a | -1.11718 | -54.13537 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55b594ee-7bc2-3fcb-a698-8c2821b37ef0 | -1.09024 | -54.22025 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03518015-af32-3bde-909c-c8417c74f390 | -1.08375 | -54.16548 | 2024-10-29 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1f413dd-96e3-34f8-805b-bad39502083d | -1.08295 | -53.65685 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c41d4d5-aae6-3fb8-a4e3-cb5b2fdfb56a | -1.08218 | -53.66186 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbbde484-4502-3174-a470-a1e8a2871e67 | -1.08146 | -53.66655 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87a85fc8-6622-3fd0-afc3-22963fef25e2 | -1.08074 | -53.67122 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d799d03-cd33-3ed4-8f2d-d893cf719128 | -1.07745 | -53.66127 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19b4334c-488c-3dd5-9c0f-88da7b2f2007 | -1.06808 | -53.65956 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41c125c2-8614-3607-8d37-5553df02a5ec | -1.06338 | -53.65884 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a2499dd-37ba-3776-ab2e-553d954ec938 | -0.98654 | -53.7062 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2b870dc-1cee-373a-9dd8-278b786b0f7c | -0.98186 | -53.70544 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b3b795c-a782-3d93-9871-44ece5ac550a | -0.98106 | -53.71065 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26728d47-7307-3d38-9b32-4dd3058e9621 | -0.98025 | -53.71585 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d55e2df1-cf9c-3f79-8df5-6af1f35e783c | -0.97631 | -53.71034 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26b347ce-8701-3b9f-8fb7-5f987008dc44 | -0.97547 | -53.71583 | 2024-10-29 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 315948c9-6867-35fe-b321-c0d266e79fea | -1.74918 | -54.44808 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fca91475-7672-3b22-8c88-64768c7a0e89 | -1.71841 | -54.70518 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d32ba73-4e8e-338b-a801-9845f028bb23 | -1.71365 | -54.52965 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 145dbe47-a59a-3129-804d-53ba779e0641 | -2.833 | -49.2413 | 2024-10-29 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 852feda4-1007-39d3-a5dd-dc369cb1fd32 | -3.128 | -45.2285 | 2024-10-29 05:25:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 33d37bc8-8298-3871-ba41-efc708e68719 | -3.1097 | -54.2865 | 2024-10-29 05:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 5844929c-3b71-3fd6-81a3-bdac7581a957 | -3.1794 | -50.3922 | 2024-10-29 05:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| f1fc70d3-883e-3306-85a2-a618a5cc6d56 | -3.2503 | -46.8709 | 2024-10-29 05:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 07ea9e52-7fc7-33cd-b660-0ed432ae8143 | -3.9289 | -48.3458 | 2024-10-29 05:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3f79774f-2761-3305-b452-6c75f6a43076 | -4.51954 | -55.45947 | 2024-10-29 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64a4a04f-6d26-31af-a50b-381863e138a3 | -4.10469 | -53.94503 | 2024-10-29 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a58f768e-bd2b-3fc7-8720-d9823b9376bf | -4.09982 | -53.94454 | 2024-10-29 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c7ec011-552d-395d-8880-a9d714a3f053 | -4.09578 | -53.93849 | 2024-10-29 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1fde17f-8834-3c11-9c2c-66f49f6f88f3 | -4.09097 | -53.93759 | 2024-10-29 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9294ae59-a00b-3364-a022-73d2fa173734 | -3.98807 | -54.13324 | 2024-10-29 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1df4fe19-7855-34e3-9ef5-7ebd8d56a57d | -3.98438 | -54.12972 | 2024-10-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2814f0f0-5333-3c14-81ac-dff2ba42f8f1 | -3.98412 | -54.12719 | 2024-10-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8163e44c-32ed-3bf8-b238-c2c47935a69d | -3.98363 | -54.13497 | 2024-10-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dae256b8-3c73-36ee-81b5-9decc381f57b | -3.98333 | -54.13242 | 2024-10-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 272600f8-8679-3552-8bca-479052170aac | -3.88394 | -54.14676 | 2024-10-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d18db7e2-7e6a-3c75-b87c-8cc7bb846bf9 | -3.88335 | -54.14627 | 2024-10-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60bd2c30-fb72-3237-aef5-84f61917b203 | -6.3888 | -55.37341 | 2024-10-29 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b28c4c07-de0a-3ebc-b354-124cf479b78a | -6.55568 | -54.95518 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 622c70a4-32b2-399a-9b1a-93162e471161 | -6.555 | -54.96008 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 696e0ff8-0a18-37eb-9046-4a7a35c594d9 | -6.55292 | -54.95795 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 438041d1-c4e6-39ca-911a-abfae6873c1b | -8.36692 | -55.16119 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 754e5902-e30b-30ee-8467-b5f0abc75cf8 | -8.32453 | -55.11859 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a975c010-5073-34c5-a6e1-3e91707e461c | -8.30624 | -55.11069 | 2024-10-29 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ad75ba8-b3c7-3f85-a9ed-b8773a6d4644 | -10.09174 | -55.40291 | 2024-10-29 05:27:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0e3934c-ca37-31d7-8732-0655932ae4f2 | -11.17267 | -56.29165 | 2024-10-29 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1856b40d-be6f-334d-8aa4-4d97f632f317 | -11.16811 | -56.29097 | 2024-10-29 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40b45abf-e259-3aa9-bcb8-9edbf16ab523 | -11.16355 | -56.29027 | 2024-10-29 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bdcb69a4-0934-3c53-a067-881adfd8eb0c | -11.16291 | -56.295 | 2024-10-29 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a3893e6-3229-3867-9252-c0aedf3b54ba | -11.13766 | -55.52968 | 2024-10-29 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b9af55f8-fecf-373f-8578-897700c8a669 | -11.13698 | -55.53493 | 2024-10-29 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README103.md)
