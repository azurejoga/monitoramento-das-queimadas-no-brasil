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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a19f9d0c-0968-3fe6-8e5b-1a1eda554532 | -8.8552 | -62.3933 | 2025-08-21 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 042ff249-8874-3b69-b3a6-e58c8ca71de2 | -13.0317 | -45.1724 | 2025-08-21 06:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 252.7 |
| d146a90d-e59f-3212-9c0c-6022c9a4b004 | -13.0128 | -45.1523 | 2025-08-21 06:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 641ae421-c1f0-3f2a-9d27-51a3a525ed78 | -13.0321 | -45.1492 | 2025-08-21 06:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 40028c35-b99d-3d6e-88c4-cdcb970e2842 | -13.0123 | -45.1756 | 2025-08-21 06:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 187.7 |
| c4c052f4-cc14-33d7-9b62-b08f4d360e5d | -13.051 | -45.1693 | 2025-08-21 06:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| cfb63b08-a785-3751-9242-f689bbab63a7 | -7.0354 | -44.6167 | 2025-08-21 06:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| f9641bb7-cea8-39e3-9edd-2e1f54a3c299 | -7.0164 | -44.6413 | 2025-08-21 06:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| f03d8fba-3e74-36da-b084-1e95c64bcaae | -7.0352 | -44.6396 | 2025-08-21 06:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| be7ce55c-77ce-3144-8ac5-809ea0f31851 | -8.8737 | -62.3925 | 2025-08-21 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 0ccbb77f-3315-3744-892c-e9ea423d05f4 | -8.8551 | -62.4123 | 2025-08-21 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c42fa346-b6c8-3967-b556-1059bf857eea | -13.0312 | -45.1957 | 2025-08-21 06:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 71680f01-e9cb-322e-bc8a-d5eb7afa76b2 | -13.0317 | -45.1724 | 2025-08-21 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 267.4 |
| 1f11fa0a-5ac3-3ed4-bc71-38dad6c5c5b1 | -13.0312 | -45.1957 | 2025-08-21 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 8358c23e-a088-34ca-9657-bc760b6281e5 | -8.8736 | -62.4115 | 2025-08-21 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 92c4086d-0d15-3c6e-8f06-bbb81c23a48b | -7.0164 | -44.6413 | 2025-08-21 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 767409f5-fc97-3583-a065-8d900875258c | -13.5356 | -47.0363 | 2025-08-21 06:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 3a090fa2-d3fd-3dd6-916f-47c2b78f8a39 | -7.0354 | -44.6167 | 2025-08-21 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 2beded38-34b8-3b01-99ac-260080fddbe0 | -14.8543 | -47.9279 | 2025-08-21 06:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 8dff969a-ae17-306e-9b10-522916148442 | -13.051 | -45.1693 | 2025-08-21 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 856f2911-3cec-3798-98d2-1a4f9b96cc3b | -8.8737 | -62.3925 | 2025-08-21 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5e06e884-0f0a-38cf-b942-123b9d0c08d3 | -7.0166 | -44.6184 | 2025-08-21 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 63c0a816-3838-3321-9b0c-f714452b30d0 | -13.0128 | -45.1523 | 2025-08-21 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 8eea46df-dcef-3667-b4bb-ba08a96495cf | -8.8551 | -62.4123 | 2025-08-21 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 83e8805f-29eb-37f5-9f0d-437228d1fda8 | -8.8552 | -62.3933 | 2025-08-21 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 9cb7df7c-9fe5-3434-bd40-3d651dd3b28c | -13.0321 | -45.1492 | 2025-08-21 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 931fb0fb-5dc2-3556-a647-097b7839cf4d | -7.0352 | -44.6396 | 2025-08-21 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 8aefb40c-0a96-3004-8438-e9bd0ce08524 | -13.0123 | -45.1756 | 2025-08-21 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.0 |
| ce2f8810-6f6a-36f6-ae39-4226249c7249 | -5.88526 | -57.74918 | 2025-08-21 06:40:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 69cd4cb6-bfe2-321f-94e1-814e5d8a55d8 | -8.86789 | -62.39682 | 2025-08-21 06:40:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7782516d-f1ba-33dc-b31b-bd422fe9eb72 | -10.41035 | -59.37706 | 2025-08-21 06:40:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 805abf24-cd95-33f9-b2af-110a2cbae919 | -8.85768 | -62.39516 | 2025-08-21 06:40:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 123.4 |
| ee1ad56d-4e58-3b7d-973a-38fd19d3403d | -11.80267 | -55.51774 | 2025-08-21 06:40:00 | AQUA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| efaf18be-dd8e-383f-a6ab-bf58ff38eba6 | -10.40156 | -59.37572 | 2025-08-21 06:40:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6b3c395f-0613-3047-a7b7-d57787d311e3 | -8.86983 | -62.38461 | 2025-08-21 06:40:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 3f164154-49bf-3c2e-a749-c5cef8938e1e | -8.85963 | -62.38298 | 2025-08-21 06:40:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| bd9f537b-3ead-3f91-9250-3d421afff9a9 | -9.18859 | -59.63103 | 2025-08-21 06:40:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 93be9084-5931-3169-88e0-0cc3d402b38a | -7.55148 | -63.84635 | 2025-08-21 06:40:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7d01fbb7-48a8-3a16-82d7-89b590a59ac7 | -6.34522 | -55.5561 | 2025-08-21 06:40:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0f064d92-e46c-33af-b917-132f38d95c79 | -8.86594 | -62.40905 | 2025-08-21 06:40:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 468272bc-a624-3c7f-92ff-726fa67c81ce | -5.88395 | -57.75796 | 2025-08-21 06:40:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fd2dcd12-8d2a-34d4-a00b-2263ccb4e5a6 | -11.80096 | -55.53048 | 2025-08-21 06:40:00 | AQUA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 95f5630d-5fe8-3ee9-b519-4c89becf5db2 | -8.87616 | -62.4107 | 2025-08-21 06:40:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 5a787521-582c-32ef-b4b5-68741b539a2e | -9.15729 | -59.59871 | 2025-08-21 06:40:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 87fcbb52-d10e-38c1-b9f7-004944a169fc | -10.41169 | -59.36818 | 2025-08-21 06:40:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f5a4b8c9-c9e4-3ed4-beb3-9d094eaa956c | -14.65061 | -54.87434 | 2025-08-21 06:42:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3555d88d-5347-368c-b1cb-890bba095f58 | -12.58081 | -60.36235 | 2025-08-21 06:42:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f73c434c-d75d-34d2-ad39-85cb8fcfe0f6 | -12.5822 | -60.35328 | 2025-08-21 06:42:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b80d5306-1870-3513-98e8-a549bcadf121 | -13.14435 | -54.91888 | 2025-08-21 06:42:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 426366dd-7f86-3bf2-98b5-75cce30a32b7 | -13.14346 | -54.91326 | 2025-08-21 06:42:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 79676bb0-663a-3b49-8e3a-526038d3431b | -7.0352 | -44.6396 | 2025-08-21 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| b8e86595-5386-3bc8-b2dd-ab1538272170 | -13.0128 | -45.1523 | 2025-08-21 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 9a899b35-8457-357d-a72c-ba52abc5eca4 | -8.8737 | -62.3925 | 2025-08-21 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4e8c73f3-3d7e-3edc-b46b-074a531eb378 | -8.8736 | -62.4115 | 2025-08-21 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 936d11a4-29fc-35a3-97e7-57acf1c05973 | -8.8552 | -62.3933 | 2025-08-21 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| bb096eed-70d7-3d21-b70e-904f9e5755c5 | -13.0312 | -45.1957 | 2025-08-21 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 30ee3d2c-1356-3cef-8629-c7dd1e7aca62 | -7.0354 | -44.6167 | 2025-08-21 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 156.9 |
| e2a75f6a-1de9-3b65-9e82-01e2cfde7e7e | -14.8543 | -47.9279 | 2025-08-21 06:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 3c396b0f-4b0f-3794-bea1-388506c71ecb | -13.0123 | -45.1756 | 2025-08-21 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 34fa9338-93af-32c7-bbce-cf210eb44dd2 | -13.0321 | -45.1492 | 2025-08-21 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 3f715d28-b175-3c57-b9fa-bd4dd119cc94 | -8.8551 | -62.4123 | 2025-08-21 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 5681d7ab-3793-3406-be6b-1de64ee2e7ae | -13.051 | -45.1693 | 2025-08-21 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 07d4b111-2c15-357f-a3d3-c0d0867c9de8 | -13.0317 | -45.1724 | 2025-08-21 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 243.3 |
| 9f2a1f1f-58de-3802-bd80-841dc720c596 | -7.0164 | -44.6413 | 2025-08-21 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| a029f781-e399-3507-a95d-17308cd5fd05 | -7.0166 | -44.6184 | 2025-08-21 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 1c54ae51-c8e2-3a5f-87f4-ee037a8d8aaf | -7.0354 | -44.6167 | 2025-08-21 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 18ebb3c2-f74f-3723-9a5d-d1809b63915c | -7.0166 | -44.6184 | 2025-08-21 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 155.0 |
| a6618c6b-5efb-3352-aaef-d8848071693a | -8.8552 | -62.3933 | 2025-08-21 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| fb6f344c-7abc-31d7-baad-6848ed633654 | -7.0164 | -44.6413 | 2025-08-21 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 4427f5a8-f745-3926-b51d-6d932e115ab2 | -8.8737 | -62.3925 | 2025-08-21 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 105.4 |
| bd13aecf-966f-393c-a354-87cf950e5079 | -14.8543 | -47.9279 | 2025-08-21 07:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 38.8 |
| c3241606-efcd-3531-97f8-6b16a1165603 | -7.0352 | -44.6396 | 2025-08-21 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| a88631c9-07db-3594-a8f0-b61ad3ba2402 | -8.8736 | -62.4115 | 2025-08-21 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ebd4fceb-cc04-33e5-b618-9da58eca321c | -7.0354 | -44.6167 | 2025-08-21 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 31e33703-e20f-3d21-b027-0d400fc4ae6f | -13.0123 | -45.1756 | 2025-08-21 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 171dde47-568d-3d4b-b9c6-e47b984e4dbc | -8.8737 | -62.3925 | 2025-08-21 07:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3035397f-1d14-3886-944a-6981751a8d6e | -13.0312 | -45.1957 | 2025-08-21 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 7f728ca9-2a54-3363-81f1-d275ae168af6 | -7.0352 | -44.6396 | 2025-08-21 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 4b4ed00c-8ed3-3dcd-8bb6-c563e41bd1ea | -7.0166 | -44.6184 | 2025-08-21 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 3cf64de1-2409-3db7-b0a2-c17b31576421 | -13.0321 | -45.1492 | 2025-08-21 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 93f71a0c-46bf-33eb-8756-a57943ff3a52 | -13.0317 | -45.1724 | 2025-08-21 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 227.6 |
| 2c1cebf7-0fce-3ba1-9122-3fe1ac8189e2 | -13.0128 | -45.1523 | 2025-08-21 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 5ab1e894-f4ee-3808-b815-fb5dc9178f56 | -7.0164 | -44.6413 | 2025-08-21 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 334cb834-ecd8-3253-8673-7050d2ec08ec | -13.051 | -45.1693 | 2025-08-21 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 188036b4-5c59-305f-b7f4-38cb6bf1bcfb | -14.8543 | -47.9279 | 2025-08-21 07:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 291d1893-bce5-3aff-b37f-8d606364fdbb | -8.8736 | -62.4115 | 2025-08-21 07:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b77dc28f-7fc2-353e-88aa-b5d9c2e4f354 | -14.8538 | -47.9504 | 2025-08-21 07:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| c5443354-d983-33ee-8387-d2fa9116dc72 | -8.8736 | -62.4115 | 2025-08-21 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| def6c39a-0ec5-375d-923c-81ec8c855f97 | -8.8737 | -62.3925 | 2025-08-21 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 0d8cff3f-b173-3d10-96dc-d344ae293433 | -13.0317 | -45.1724 | 2025-08-21 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 56c804bc-8d1a-3c15-b8f8-ff82672e2383 | -8.8552 | -62.3933 | 2025-08-21 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| e241d6fd-40ef-360e-aa55-c7f419877a9e | -13.0128 | -45.1523 | 2025-08-21 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| d513e11a-7b9d-3396-9cd9-d1a1d36c4ec4 | -7.0354 | -44.6167 | 2025-08-21 07:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| dec3aa2b-8608-3fab-9575-9d9d17c5aeac | -7.0166 | -44.6184 | 2025-08-21 07:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 52c7d6e8-5e11-3d0a-a21e-2f7aa0240d4b | -7.0352 | -44.6396 | 2025-08-21 07:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| d7dabd80-3a5c-3519-83f1-27c1c63998b9 | -8.8551 | -62.4123 | 2025-08-21 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 32.0 |
| ceb1ea60-ef2f-32e9-8d01-fdf5f60e6c77 | -14.8543 | -47.9279 | 2025-08-21 07:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6d2d5aef-8c2e-3c04-bea1-b873c127b231 | -7.0164 | -44.6413 | 2025-08-21 07:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 31377e47-2810-3d47-969d-16892fd8a13e | -14.8733 | -47.9472 | 2025-08-21 07:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 576221be-52ba-339d-8890-0c4c08bb8328 | -13.0312 | -45.1957 | 2025-08-21 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |


[Clique aqui para ver as próximas entradas](README59.md)
