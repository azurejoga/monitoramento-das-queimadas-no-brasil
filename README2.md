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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83eee23b-06d4-35f8-95b5-16ea93647c52 | -4.6883 | -43.1314 | 2025-10-13 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 462.0 |
| a8c47171-bc1d-3a14-9f53-f8a6e91bb222 | -2.5239 | -47.7899 | 2025-10-13 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 168.8 |
| 466aa2ae-675e-3159-ae43-a57e080bd896 | -13.4974 | -51.3206 | 2025-10-13 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2b31020b-b8fa-3e2d-8037-528a668eeddf | -17.338 | -53.8135 | 2025-10-13 00:30:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 118.9 |
| d0834bf8-6926-3158-92da-1e9fee966b80 | -11.7309 | -64.9579 | 2025-10-13 00:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 73cbbdcf-5256-3543-82cc-f548e265d735 | -3.1057 | -50.3735 | 2025-10-13 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 50bcf0ce-ba62-33f9-8e8d-06375336bf3c | -13.4977 | -51.2992 | 2025-10-13 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 155.3 |
| e0515acd-1c99-359f-8885-06aa7b6b493f | -14.3015 | -51.5573 | 2025-10-13 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| c4783a07-5a8e-3465-9b49-23fac2bb9afa | -3.1433 | -50.2044 | 2025-10-13 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 9a5ae03f-807d-35e3-b51a-eb392788ede2 | -4.6885 | -43.108 | 2025-10-13 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 29388d78-9bdc-325c-85a6-b47eab63d53b | -2.5423 | -47.811 | 2025-10-13 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| e97184b0-ab1e-3d27-80a6-218b01681b9e | -13.517 | -51.2967 | 2025-10-13 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| dbae20d5-559d-3d14-8433-f1f81572c3a7 | -11.7497 | -64.9571 | 2025-10-13 00:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 134.7 |
| ae6b8170-2980-3e83-8b70-82c462031e37 | -14.2639 | -51.4982 | 2025-10-13 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 447c5f6e-4d7e-3fe2-819e-dfe3d5b05e27 | -3.1248 | -50.205 | 2025-10-13 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 14f3dbef-8365-3107-ad27-c67d5c361b2a | -11.7308 | -64.9769 | 2025-10-13 00:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 1cd8b89e-fc1a-3bc8-b188-4f808f432734 | -4.6696 | -43.1326 | 2025-10-13 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 268.5 |
| f11c8415-7a3b-3ae1-a2f5-eeeeb4f9ea4d | -4.6698 | -43.1092 | 2025-10-13 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 74aaf1fc-19e8-39c4-8c56-3e9b823f341f | -13.8762 | -45.4714 | 2025-10-13 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 0067d7de-482d-3241-9c9e-1950c24ebc9b | -11.7495 | -64.976 | 2025-10-13 00:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 108b6849-3d1b-3e5a-80e4-717a0a7a05ab | -16.1207 | -53.9625 | 2025-10-13 00:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 784450c2-5ea0-3d42-9e53-a4db00b2d4a0 | -14.2825 | -51.5384 | 2025-10-13 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 89820fbc-1d18-3ba8-bd0d-0e27e53f5a05 | -13.8952 | -45.4913 | 2025-10-13 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 570ad0cc-c008-3a7e-b37d-ec5b1d6563b1 | -2.5239 | -47.7899 | 2025-10-13 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 0e599fca-ba65-37be-bc09-746e552bf4a3 | -17.3384 | -53.7922 | 2025-10-13 00:30:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 6668be22-fb5c-326b-a9c4-a67ddc7b2c34 | -14.3019 | -51.5359 | 2025-10-13 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a094c54e-db1e-3707-bc2b-1195fe4ef449 | -14.2636 | -51.5196 | 2025-10-13 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 35417436-83a3-3057-aac6-c7fad79ee754 | -15.5428 | -41.8179 | 2025-10-13 00:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 16ccdb96-b85e-3be8-9da9-8be2ebac6464 | -17.898 | -45.0 | 2025-10-13 00:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 25bc8a79-827a-3126-b1c0-38d1714991cf | -2.5424 | -47.7893 | 2025-10-13 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 02d6aaf6-ef60-3719-910c-149823b531a0 | -3.0726 | -49.404 | 2025-10-13 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| d83b382f-414f-3bb0-b69a-663721e92d1f | -4.6883 | -43.1314 | 2025-10-13 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 279.8 |
| 51767cea-0746-3c5f-aeb0-a449300e0979 | -2.5238 | -47.8115 | 2025-10-13 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 4e79f07e-b590-373b-8b2d-f382128ee7ca | -13.8757 | -45.4946 | 2025-10-13 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 632c06bc-44ff-347e-9871-1079976fde72 | -11.7497 | -64.9571 | 2025-10-13 00:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 134.3 |
| d64201ed-0334-3c07-aca9-b0351e751f2b | -7.6943 | -41.4694 | 2025-10-13 00:40:00 | GOES-19 | VERA MENDES | PIAUÍ | Brasil | 2211506 | 22 | 33 | nan | nan | nan | Caatinga | 138.7 |
| 1e98eee1-41c3-326b-991e-c1048f0f26d5 | -14.2825 | -51.5384 | 2025-10-13 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 6948521a-6cbe-33d8-a980-e989e231978c | -13.8757 | -45.4946 | 2025-10-13 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0441b473-88d3-3c1b-b8c3-cacf964103e1 | -14.2636 | -51.5196 | 2025-10-13 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 5aa555bc-8ae0-32f6-a612-75244af0135e | -17.3187 | -53.7951 | 2025-10-13 00:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 3c659cee-29ac-35af-845d-7b7f2930044d | -17.3384 | -53.7922 | 2025-10-13 00:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 165.5 |
| a8606467-0e5a-3933-9c43-5354d67cd6f4 | -3.0726 | -49.404 | 2025-10-13 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 1823420a-6e9c-39e5-acb7-5c865e516a4f | -14.2639 | -51.4982 | 2025-10-13 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 732b1f5b-415e-333d-a7fa-e2485c2f8571 | -13.517 | -51.2967 | 2025-10-13 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 994e8de9-7d40-3a58-ae00-5bed70af5a79 | -17.3183 | -53.8163 | 2025-10-13 00:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 89.1 |
| fc554492-56c9-35a8-998f-bbb3866587ad | -3.1433 | -50.2044 | 2025-10-13 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a56fc5e5-4206-33a4-a6dd-befffea4187c | -4.6883 | -43.1314 | 2025-10-13 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 1d014191-a689-37ac-8982-5704dc9f0522 | -14.206 | -51.5059 | 2025-10-13 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1374a3e8-c409-344b-904d-2e9a296137ae | -13.8762 | -45.4714 | 2025-10-13 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b9a3818e-f526-3dfb-bff0-4ff918a4dd9a | -2.5238 | -47.8115 | 2025-10-13 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 56f51f3d-5bc2-34bc-aaae-fedf31db7bbd | -2.5424 | -47.7893 | 2025-10-13 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| c90e056b-feda-35b7-8a1a-df571f2e5d5e | -14.2822 | -51.5599 | 2025-10-13 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 14069d7e-91d6-3885-bfa3-e68fba962a05 | -11.7308 | -64.9769 | 2025-10-13 00:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 80.6 |
| cc7b1e9f-8790-33fa-be27-387430ae40a8 | -17.3582 | -53.7893 | 2025-10-13 00:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 78.6 |
| b281b87d-bd1f-39fc-9ac4-fe31a666ce13 | -2.5423 | -47.811 | 2025-10-13 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| ea97f49a-21d2-3463-8d11-92a923aee70b | -14.2056 | -51.5273 | 2025-10-13 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| dcdb8952-39ab-3248-9fdd-e0b6a0afac2a | -13.4977 | -51.2992 | 2025-10-13 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 0bb8ee34-f757-3bb2-b7fb-ceb6de12a891 | -4.6696 | -43.1326 | 2025-10-13 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 170.3 |
| f6be168b-eba8-3461-8cd7-60108eb8f51e | -11.7495 | -64.976 | 2025-10-13 00:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 85.9 |
| c0fdf08b-be1c-327d-a34f-60973bde1bb4 | -14.3015 | -51.5573 | 2025-10-13 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 8d5fb939-fefb-31ad-9823-5af4d3f2fee0 | -17.3578 | -53.8106 | 2025-10-13 00:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c461f21b-fabe-354b-a767-889ce5bee5fc | -11.7309 | -64.9579 | 2025-10-13 00:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 348dc607-b98e-395a-bc21-108db1804cd6 | -4.6885 | -43.108 | 2025-10-13 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 52d3f422-c742-3edd-a76e-cd9bf665e893 | -17.338 | -53.8135 | 2025-10-13 00:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 75459372-99a3-3d10-acfa-9097b62bd21d | -3.1248 | -50.205 | 2025-10-13 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 3cf349b2-7335-30bd-b46c-f6ba9868597e | -2.5239 | -47.7899 | 2025-10-13 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 2eda5f1d-6699-306f-a5e6-efd5966d804d | -3.1057 | -50.3735 | 2025-10-13 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 1ae40ff4-5fbd-335f-b279-03014d173f2b | -4.6698 | -43.1092 | 2025-10-13 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 1e9ba470-4059-3450-ba92-7ed6c04385ab | -14.2829 | -51.517 | 2025-10-13 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 8c5c2b26-fc69-3f3d-b2f3-1ac4aba7e718 | -13.517 | -51.2967 | 2025-10-13 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4124473c-3185-334d-bcb5-9cfa748e5a87 | -3.0726 | -49.404 | 2025-10-13 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| f19490cc-213e-362f-9d8f-f800e0f9ff33 | -11.7497 | -64.9571 | 2025-10-13 00:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 24f4644a-d1e7-3945-9b89-ed684802c882 | -14.2056 | -51.5273 | 2025-10-13 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 39785eac-61b6-363f-8437-bcd443a651c4 | -17.3384 | -53.7922 | 2025-10-13 00:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 843530d4-53db-3471-b66b-eb841e4ab08e | -17.3183 | -53.8163 | 2025-10-13 00:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c1945ebe-d3d6-314e-9118-92c8e4ebeaeb | -4.6885 | -43.108 | 2025-10-13 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e6f61c87-9967-33a0-993c-81d7476d8119 | -11.7308 | -64.9769 | 2025-10-13 00:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 0b2371a7-dbe2-3ba8-99b8-639b0a9023b9 | -3.1248 | -50.205 | 2025-10-13 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| da86de8e-0277-3b14-9b0c-7f83de3d3a09 | -4.6698 | -43.1092 | 2025-10-13 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f4a5fb22-62e6-317c-9ac7-986b621d2abf | -11.7309 | -64.9579 | 2025-10-13 00:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 1501deaa-cc0f-3cbf-86bc-209d2c0f8ae2 | -17.338 | -53.8135 | 2025-10-13 00:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 8583bb1c-5e49-35db-96b9-41c1c6c4f315 | -13.4977 | -51.2992 | 2025-10-13 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 52c27c34-dd44-3892-b62d-a5840ae31580 | -8.8909 | -45.3224 | 2025-10-13 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 0ee4d371-ca0f-314b-adca-cfff390db600 | -4.6883 | -43.1314 | 2025-10-13 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 91b75a33-a40c-3a41-98a0-7eb044d2b297 | -8.8719 | -45.3244 | 2025-10-13 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 4d2dc2f0-c259-3639-864b-fc118f0a9ab3 | -11.7495 | -64.976 | 2025-10-13 00:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 22702ec7-a2cd-3949-bf91-1e8e73c0a8e9 | -8.8722 | -45.3016 | 2025-10-13 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4933b7c8-353d-3098-b692-97d99683219f | -4.6696 | -43.1326 | 2025-10-13 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 81bc2a3c-6741-38b9-a90d-a74ef30eed2d | -17.77956 | -54.9312 | 2025-10-13 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8f2ecac6-96f9-3804-9686-34a56afcc40e | -17.32233 | -53.8043 | 2025-10-13 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 564bc7e6-d1b0-329a-adb4-759365ca08cf | -17.34189 | -53.81159 | 2025-10-13 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 113.2 |
| e44ce337-a1b9-3fdc-828e-124e5b65b400 | -17.33017 | -53.79299 | 2025-10-13 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e3242f70-e35d-3821-ba03-a013bf4cf64a | -17.99122 | -54.00436 | 2025-10-13 00:50:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1bde583f-6827-3148-8df4-de82a2bf6b1c | -19.07848 | -57.51189 | 2025-10-13 00:50:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 947e87f3-ffc8-356c-a8be-3eec83a8438e | -17.33146 | -53.80295 | 2025-10-13 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 239bfa37-2840-391d-861a-d2be2e65ea5a | -19.03448 | -57.55325 | 2025-10-13 00:50:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 45.9 |
| 3897f239-bc05-317e-9cf4-b1ab348044da | -19.0225 | -57.55468 | 2025-10-13 00:50:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 1311e9fc-6549-33df-9bd5-89b7e3fd3ec8 | -17.33929 | -53.79166 | 2025-10-13 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 06b0102c-c716-373f-9a15-894c75e47992 | -17.33276 | -53.81295 | 2025-10-13 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 283dc20f-74e7-37fa-bfa6-a864094f3336 | -19.02892 | -57.55954 | 2025-10-13 00:50:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 52.4 |


[Clique aqui para ver as próximas entradas](README3.md)
