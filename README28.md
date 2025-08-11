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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd658b5f-d23b-3c35-b78e-d5b343083f26 | -7.06321 | -59.19844 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d723ebf-09d8-3647-9b26-fed6bd87744a | -7.07591 | -59.20559 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0c765010-71ea-3c96-9900-e9923146aa0a | -7.06528 | -59.2097 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c6b26342-557f-3cac-8d96-029f6c54e72f | -7.06347 | -59.1729 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5bba18c9-b940-3af0-9730-a35bbd3feedb | -7.06848 | -59.18625 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5053bdda-ba01-3157-aa50-366d0623c05c | -7.07179 | -59.16202 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cd2f8e5-e2e7-38e3-b5d0-4619c7d91c5e | -7.07684 | -59.17508 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c33e08ea-ab83-3fe2-8d0c-58a7704a6621 | -7.06844 | -59.21062 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 00e6f5e3-2dd9-332f-8705-0c0f0956b1a1 | -7.06793 | -59.16195 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a6223b2-1580-3146-9d0a-eeeb968ed0ed | -7.07383 | -59.16911 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfb3a5a3-1552-3160-96e6-dbf7a4a45948 | -7.07305 | -59.17514 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff0c6c21-0757-3624-bd83-2ab70d9fe5ee | -7.07015 | -59.174 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba8b82ab-40ac-33cb-a9de-11cbbb1e9acc | -7.07069 | -59.1933 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f851a77-d678-343f-a3ce-4da26b277ffc | -7.06397 | -59.19258 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b8ce73e-6428-3e19-bbfd-c4b09a394e56 | -7.05652 | -59.19748 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 461bf662-2dc5-3f5b-a6da-bc59f413d2ff | -7.2556 | -59.99641 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 008bfcdc-4a94-3c50-890a-71909f83eb41 | -7.07226 | -59.18122 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2d990e0-77b9-3dff-a071-153e0e721fb7 | -7.06931 | -59.18015 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f13e0b5-56f6-31a6-82cd-3c36c8cae6ef | -7.06919 | -59.20487 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8c6e44e7-36d8-3142-bf13-96b9d0cc56b7 | -7.07461 | -59.16315 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2709544d-dbd0-3ebf-9da9-5b71a9665f8b | -7.08339 | -59.20052 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ea4c703-2608-38fa-bbea-a8d88dd6a196 | -7.07601 | -59.18108 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fe3c40d-62b3-337a-8427-80816d3f9b3b | -7.05345 | -59.19647 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5be36173-5186-3b75-ac9e-c9a26c4b1ad2 | -7.06172 | -59.20991 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2b7a1828-cfdc-3ad2-b410-20799af14e25 | -7.06606 | -59.20398 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d41111fe-5f7f-3a1d-945f-40026d572076 | -7.06093 | -59.1916 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b3dbecb-efec-3f0b-a627-055393ac5f93 | -7.06637 | -59.17403 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8e76e14-5fe5-35f7-a671-251c9476c06a | -7.07148 | -59.18722 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88e2dd02-eb92-3a2a-8714-347a46f413e7 | -6.10176 | -59.92215 | 2025-08-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21afdf96-f105-31fe-a750-6974efab543c | -7.05857 | -59.2089 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90d18e59-96f8-3ce6-bbd9-c85a6164da88 | -7.07818 | -59.18814 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4388a0d3-fad7-3183-97ec-a282010c75e5 | -7.06716 | -59.16793 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 260b0f0b-cb48-3653-8a4a-39fdabab7417 | -7.06175 | -59.18554 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 366ffab6-03af-37b6-aab0-cade35d6fd2f | -7.07098 | -59.16796 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62cd4ac9-4dfb-38e5-9885-a3bd7af8d40d | -7.06993 | -59.19916 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 544be276-2f58-3ff7-89c5-ee7491233071 | -7.05424 | -59.19064 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c1fe58a-1849-3ac6-97b0-c116710b19ce | -7.07358 | -59.19886 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f862e245-867e-3095-a228-637f32f904ac | -7.07765 | -59.16913 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c31415b9-65a9-348d-bf22-48eb54736a62 | -7.07667 | -59.19976 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 286f57eb-5c04-3be4-bf2d-0ca2624867bc | -7.07974 | -59.1762 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e71f2e81-3ade-32e4-bb9e-5dd26a43ec90 | -7.25682 | -60.00179 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 231866f2-2cf1-3ae7-ae8e-c711deed5d06 | -7.08492 | -59.18883 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f34bc57c-ec6b-3213-bbce-0e15ee63e723 | -7.06013 | -59.19745 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de78dcf3-796b-37e0-8466-742d1f5e4db0 | -7.07279 | -59.20461 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e9973d4-c8c9-3c58-8ade-030346ca3b37 | -7.25747 | -59.99675 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecb69e50-4b22-3810-b4c6-1ebf9c462d84 | -7.0645 | -59.21543 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ccfb87eb-2950-35a4-84b9-e345d40587ba | -9.37504 | -61.52528 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 602d59a6-7d76-33f8-add5-1b9f6dd9d8d5 | -9.38413 | -61.52539 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35369f91-61a0-3748-bf50-e07de783fe37 | -9.3685 | -61.52887 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65bdea53-c4a5-3eb2-a9a0-01dc0ec7615b | -9.3793 | -61.53933 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bad3e8bd-99da-3c27-9c26-442f128bbbe4 | -8.92862 | -60.73001 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 771a4857-58b2-38df-bd8c-7e3eddf16d30 | -9.37761 | -61.529 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79493d13-b391-313c-991b-d2dd0a846c53 | -8.93111 | -60.76 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ccff240-6d4a-3533-a01b-f4ce50f92280 | -9.37707 | -61.53343 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 88cd55fb-bce2-38ab-9b3d-6da238d4d778 | -8.93488 | -60.73074 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1c39fd10-2728-3708-99fc-41b2a7e9acc2 | -8.23976 | -70.145 | 2025-08-11 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| de362e5c-37ec-333c-bd60-b4a6d1155e74 | -9.37652 | -61.53786 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d9a0e7c7-e3ae-3533-a026-1139a53430d3 | -9.36907 | -61.52448 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07b3fc3d-fae8-3d53-82b5-f3bf9ff2c126 | -8.93173 | -60.75519 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a59aeb5-eff1-3494-9a7c-6c3fe0f0be5f | -10.96327 | -68.49469 | 2025-08-11 06:08:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be52c79d-669e-3c25-95a3-ca2ecedb7c9e | -9.38102 | -61.52608 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 79ed67e0-5373-3148-99ce-fd93b02fbbfa | -8.93361 | -60.74059 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e50dfbd1-56ab-3b87-b28e-e80a5976a9db | -8.76746 | -71.1077 | 2025-08-11 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab593e09-e758-307c-b1e0-5da726aaa050 | -9.37987 | -61.53489 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dbf965d0-c73a-3d50-8c24-fa987570fe24 | -9.37447 | -61.52968 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc711348-fd5f-3dd1-aa9f-df3e5217ba86 | -8.93299 | -60.74546 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 819e5f80-e48c-33c3-aca2-6f13ba58ec1b | -10.16626 | -69.00926 | 2025-08-11 06:08:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e35dfab1-8119-36b9-92f2-5597f05a3a42 | -8.93425 | -60.73568 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4de9761a-1176-3505-bd0e-1c614412e5aa | -9.37815 | -61.52458 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c12d129c-4bc4-3383-8cc2-9bc77482c92a | -8.93236 | -60.75034 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d22774f0-c048-37a9-98e5-38a5f3a5354e | -8.76691 | -71.11127 | 2025-08-11 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9c331d8-0119-34a7-9089-5d86d7bd531f | -8.77026 | -71.11179 | 2025-08-11 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f286689-68b0-3f70-b235-e77c635293be | -9.37332 | -61.53855 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a644059-934e-37b4-9b34-a4f1d5c3dc1a | -9.38045 | -61.53048 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4fb4ebe6-67d2-3bf3-b9e8-f5b7123253ac | -8.93797 | -60.75597 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b5b193c-2818-3f3c-8354-d8eb8f379daa | -8.92799 | -60.7349 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e862385-ca4a-3cbd-8c7a-ca8072d5403a | -9.3739 | -61.5341 | 2025-08-11 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6880b4fb-79ae-3674-93a3-6d583784265b | -18.6293 | -46.8394 | 2025-08-11 06:10:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 90fde871-eff1-37a7-9360-5c10a04620ec | -8.9401 | -60.7288 | 2025-08-11 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 49c65bb5-9628-33f6-8e8d-63d8d7a6583b | -7.0799 | -59.1964 | 2025-08-11 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 49993447-6546-3287-ba6a-f30cf4f6c68c | -6.5856 | -44.564 | 2025-08-11 06:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 6aa3417d-56b5-30c5-a9d0-e8a4b7785c3f | -8.9399 | -60.7481 | 2025-08-11 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 9a883321-2116-39c0-93e5-d1ce6a2072c5 | -19.2766 | -49.7711 | 2025-08-11 06:20:00 | GOES-19 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 07d7081c-19ad-3c1d-b66b-c604164f4158 | -18.6091 | -46.8438 | 2025-08-11 06:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| a207aa09-3903-308f-b879-926a66260a35 | -7.0799 | -59.1964 | 2025-08-11 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5e2387cf-2fb7-3fca-ad08-d82a6bc40eb1 | -18.6293 | -46.8394 | 2025-08-11 06:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 29ce2869-f882-34a2-babe-1e2ca82fa0b5 | -18.6287 | -46.8629 | 2025-08-11 06:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 50.9 |
| e1a7edb1-743e-334f-be77-49507d364ab5 | -18.6085 | -46.8673 | 2025-08-11 06:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 1d258fc7-a0f9-3930-8be3-a5235f4eb733 | -8.9401 | -60.7288 | 2025-08-11 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 20b2d965-57fc-3c09-9d1c-a729477718ae | -6.5856 | -44.564 | 2025-08-11 06:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 74b6673f-d7b2-36a3-8f2f-fafce9458806 | -15.4212 | -53.9283 | 2025-08-11 06:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 40102b21-5956-3c24-9d70-0dc7d2662348 | -18.6091 | -46.8438 | 2025-08-11 06:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 69c03ea2-d19d-3e78-9924-3e2bc0a63486 | -6.5856 | -44.564 | 2025-08-11 06:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| e587ce4c-9699-3555-bbfe-ec0f71b81c47 | -7.0614 | -59.1972 | 2025-08-11 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c86ac541-364b-32b7-8bd6-f098bac0a11a | -6.5858 | -44.541 | 2025-08-11 06:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3aa8e3e4-cbc5-3e2e-b369-2898a640d34d | -18.6293 | -46.8394 | 2025-08-11 06:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 930bf551-57a9-348c-aeac-ac46a22131ef | -8.9399 | -60.7481 | 2025-08-11 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 442358bf-3ba1-3119-9352-edce594c0687 | -8.9401 | -60.7288 | 2025-08-11 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 298a20f0-b73c-3a95-bcd5-3cf78c60a0bc | -15.4407 | -53.9258 | 2025-08-11 06:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| f17809d5-1d18-322c-b16d-f0a2133f99b5 | -7.0799 | -59.1964 | 2025-08-11 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |


[Clique aqui para ver as próximas entradas](README29.md)
