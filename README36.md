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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4846fec-d312-3947-9769-8cafb573b6b2 | -12.68788 | -44.93359 | 2025-08-13 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| fe055e43-ed97-39ea-b8d2-2f02b2511954 | -7.85317 | -44.21271 | 2025-08-13 12:34:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 6dc9b5e4-8b39-3dec-888b-5bacae1ac9af | -13.13611 | -46.86311 | 2025-08-13 12:34:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| aa985a42-5483-3794-b0e0-acfa688d0ff1 | -11.7206 | -50.12782 | 2025-08-13 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3044916b-f0b1-362f-867b-e8d8739d84be | -7.85622 | -44.21886 | 2025-08-13 12:34:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 66eb95de-b9f6-365a-9496-da7afae3f089 | -11.69176 | -51.6142 | 2025-08-13 12:34:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7d1d56b5-06f2-3db8-99a3-915e4d4a04d3 | -7.85074 | -44.23115 | 2025-08-13 12:34:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 39.3 |
| b37ea995-d934-3ae1-9cdb-88e361877f75 | -12.68556 | -44.95279 | 2025-08-13 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 2d11fd40-7d38-3c2e-9e2d-ec2ecbf67a32 | -7.79931 | -44.95494 | 2025-08-13 12:34:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f1836a81-81ab-378c-9943-63b2f617c04f | -6.8956 | -59.1462 | 2025-08-13 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 4b3d0048-7bc5-3ff8-b7f1-0e6cf99e148e | -6.8957 | -59.1269 | 2025-08-13 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 27fcdf9b-7448-364d-b068-6dc4f5fc41c1 | -8.106 | -55.5701 | 2025-08-13 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 6a7f3d49-ef4d-33bc-9622-ebd67fabe90c | -6.9141 | -59.1261 | 2025-08-13 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 8232443e-d5d6-39b8-9611-5b0205efdd3e | -6.9141 | -59.1261 | 2025-08-13 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 6a898b39-f20f-334f-90ad-0e696718757a | -6.914 | -59.1455 | 2025-08-13 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 694dbfd4-c7de-3d75-b260-dbb275609d12 | -8.106 | -55.5701 | 2025-08-13 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 36c951b2-438a-3dc0-b5a9-67d4b28b516f | -6.8956 | -59.1462 | 2025-08-13 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 664cb66a-fcb2-335c-be79-d4343b1306ed | -6.8957 | -59.1269 | 2025-08-13 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 3cb94c08-f4fd-32d0-8ce6-cfd172486d30 | -6.914 | -59.1455 | 2025-08-13 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| b9df3e10-e6df-3d9f-b227-2649ecc2395f | -8.106 | -55.5701 | 2025-08-13 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 1afe8e4f-8fca-3b6a-87bb-6cdbae71a6fa | -8.1246 | -55.569 | 2025-08-13 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4b4def16-4013-38e0-8a43-0cc7ca79f941 | -6.8956 | -59.1462 | 2025-08-13 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.4 |
| a26a5d25-8d66-3abd-bcc9-2000ed169258 | -6.9141 | -59.1261 | 2025-08-13 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f16a7c23-76d8-3599-b141-e68a0deeccf3 | -6.8957 | -59.1269 | 2025-08-13 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| de121117-1046-32a5-aa9b-3eee9a4ddcfe | -6.8772 | -59.1277 | 2025-08-13 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c3a2aa15-9c3a-3528-9624-904f08eaf016 | -6.914 | -59.1455 | 2025-08-13 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 7859eeea-2a02-3551-9375-1df871eaabad | -8.106 | -55.5701 | 2025-08-13 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| f07dadba-e792-3b8e-b641-2262e73aff29 | -6.8957 | -59.1269 | 2025-08-13 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| ade2f4ce-9d30-3bba-b69e-5fa10b02aaba | -6.9141 | -59.1261 | 2025-08-13 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| dd6438a1-35b7-3966-b70e-fe19d78f64a0 | -6.8956 | -59.1462 | 2025-08-13 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 192.0 |
| 32cc1707-a290-3dc8-90b5-3c5c114e2628 | -8.1246 | -55.569 | 2025-08-13 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| f51f5b2e-b697-3350-8001-c7d135f0c0d1 | -6.8772 | -59.1277 | 2025-08-13 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e3434d7f-e397-34e6-82b6-34b6312ad0d5 | -6.8771 | -59.147 | 2025-08-13 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 993bb82d-7b82-30b0-ab98-3809643079ed | -8.1246 | -55.569 | 2025-08-13 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 3a793c21-71a7-366b-8e25-03ef3f040ebe | -9.1894 | -59.6558 | 2025-08-13 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| debe21a4-5ca5-391a-a278-3f1e2b647668 | -6.9141 | -59.1261 | 2025-08-13 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 64e02693-d460-389a-a8b5-039f2e7768b8 | -6.914 | -59.1455 | 2025-08-13 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| b753b1e1-ec93-3823-a890-893ddc5d0e1b | -6.8956 | -59.1462 | 2025-08-13 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 217.4 |
| 99bdec22-c119-395a-ba2e-5b3b22afdfd5 | -8.106 | -55.5701 | 2025-08-13 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| d4644cef-ae44-3c4f-94fc-e7c3194aa99f | -6.8957 | -59.1269 | 2025-08-13 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| c14b93a2-1c62-3ea5-abb9-d651a0460214 | -8.1246 | -55.569 | 2025-08-13 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| feb4ba93-f8d5-36cb-a17b-9884ffec332e | -6.8771 | -59.147 | 2025-08-13 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 1c8aedb6-3303-3bdc-80d6-4e8899f9afa1 | -6.8772 | -59.1277 | 2025-08-13 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 33c21966-7e6e-316d-b331-aaf7f421ea26 | -6.8957 | -59.1269 | 2025-08-13 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 10b5a4bc-db67-3c62-9b90-79762d534537 | -8.106 | -55.5701 | 2025-08-13 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| b65f5065-6593-36a5-928a-a0f8adeb0e0c | -6.8956 | -59.1462 | 2025-08-13 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 249.0 |
| a61153f1-e5c1-328e-b3c4-f902cb4cb4bf | -6.914 | -59.1455 | 2025-08-13 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.6 |
| cafb15a8-2e33-3b43-8c4c-700852643733 | -6.9141 | -59.1261 | 2025-08-13 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 6ec456ab-1f52-3509-8a0e-0a1c9ce9d34a | -8.106 | -55.5701 | 2025-08-13 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 238.6 |
| 374453f7-2e1b-3c8d-b949-e6a73ea591c3 | -9.1894 | -59.6558 | 2025-08-13 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 07b2cdce-a399-3284-8732-e5b0870c5785 | -8.1246 | -55.569 | 2025-08-13 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 74978e38-b59d-3b62-a6f6-82a48118cc54 | -19.7917 | -46.3624 | 2025-08-13 13:40:00 | GOES-19 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7084f5f3-2138-300e-ba3a-e7511012b676 | -8.1246 | -55.569 | 2025-08-13 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| e07e41d1-8ddf-31ff-b4a0-4ec44e69fabd | -8.1058 | -55.5901 | 2025-08-13 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| cc1bc813-8715-3887-ba9c-bf9b9eaf4bf1 | -9.1894 | -59.6558 | 2025-08-13 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| fb28b639-6634-36ac-9761-bf6c90aed04c | -8.106 | -55.5701 | 2025-08-13 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 4f209ca8-aca5-3f12-a730-3bdf34616d7e | -6.0992 | -59.9267 | 2025-08-13 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c51c2ec9-2727-30b6-83c9-01bba42920d4 | -8.1246 | -55.569 | 2025-08-13 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 0f770751-dc55-3138-869e-a1932ca92de5 | -9.1894 | -59.6558 | 2025-08-13 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 4e35978b-ae82-3daa-a76e-f26ee24375a3 | -8.106 | -55.5701 | 2025-08-13 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 707c9ce5-2ed6-369c-97cc-6c418afc63e3 | -9.208 | -59.6548 | 2025-08-13 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 8b94d98a-a166-31ca-9ace-1f6e0e4537ca | -7.6472 | -63.5148 | 2025-08-13 14:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a15b04fd-2e4a-34a4-9d7a-c02da93c2845 | -6.0992 | -59.9267 | 2025-08-13 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 66c17dad-4683-33d2-a2ac-8ae17f0ab83f | -9.1892 | -59.6752 | 2025-08-13 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 2ade060e-85e1-37a6-bdd3-1ad2cce85894 | -7.8487 | -44.2172 | 2025-08-13 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 0e3e8293-d4d8-3912-bdd1-ffa43c1bd0bc | -8.1058 | -55.5901 | 2025-08-13 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e0e85dbb-a3ca-3106-b5a0-a798ae5bdd72 | -7.8487 | -44.2172 | 2025-08-13 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| b86524ca-6598-323d-80eb-b21f57b40c06 | -6.0992 | -59.9267 | 2025-08-13 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d02a3a13-0207-31ba-a53a-b368da4f130f | -9.1894 | -59.6558 | 2025-08-13 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b3c0959b-86a7-3404-b86e-d5c205ee959c | -9.1892 | -59.6752 | 2025-08-13 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 828e352c-7451-372c-8ec2-2d3eb6c38d03 | -7.6472 | -63.5148 | 2025-08-13 14:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 828dca3e-924e-3d2c-af2c-bc564a10a0e8 | -8.1246 | -55.569 | 2025-08-13 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 0f625ef1-c790-39a0-b557-2a5f67897b36 | -8.106 | -55.5701 | 2025-08-13 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 5e9c8e4e-2873-33c3-b0ff-f47c3af8660c | -6.8957 | -59.1269 | 2025-08-13 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 476.5 |
| 1303ab02-7e14-30d4-8d83-39c080119390 | -6.8772 | -59.1277 | 2025-08-13 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 8cee560a-9f11-3efc-b833-cdcc002d20fb | -8.1246 | -55.569 | 2025-08-13 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| ba0165a7-56e6-39ac-ac69-5ee458d342f9 | -8.1058 | -55.5901 | 2025-08-13 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f7aab4c9-2287-315d-b4f8-0c57f30364e0 | -9.1894 | -59.6558 | 2025-08-13 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 1959b66d-bf96-3f5a-8781-4be7ce61c890 | -6.9141 | -59.1261 | 2025-08-13 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 472.5 |
| f351343b-6395-3875-9857-43138fba89ec | -6.9326 | -59.1254 | 2025-08-13 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.4 |
| dd2ca7d9-0567-34eb-ab5e-31cd95d7ed4b | -8.106 | -55.5701 | 2025-08-13 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 189ce12e-b6f2-3c24-88f6-d4a770fa284d | -6.0992 | -59.9267 | 2025-08-13 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7c768031-f210-361c-a3de-e617edcef85e | -9.1892 | -59.6752 | 2025-08-13 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 8805cf1e-2e64-3ee5-9887-ae88131052cb | -6.9325 | -59.1447 | 2025-08-13 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 246.9 |
| f51de11d-7d29-3e97-b45a-913d8efd9053 | -2.9108 | -48.254 | 2025-08-13 14:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 853e33fc-9061-3545-bcd7-6f806cde6d78 | -6.8772 | -59.1277 | 2025-08-13 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 3249ca23-9847-3626-9c03-07b2ab3ff487 | -9.1894 | -59.6558 | 2025-08-13 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 782c7c35-2b9e-3e7f-845d-58bc928c2b3b | -9.2079 | -59.6742 | 2025-08-13 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 54134793-3423-30f7-b7fc-4063ab41beae | -9.1892 | -59.6752 | 2025-08-13 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 75a7cadc-e837-3535-9e35-9c7e2b978970 | -6.9141 | -59.1261 | 2025-08-13 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 640.5 |
| 5272e13a-39a6-3533-b146-92122147c4b3 | -8.1246 | -55.569 | 2025-08-13 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| e44621bc-e952-343d-8a8c-e55c6734a67e | -12.3754 | -59.846 | 2025-08-13 14:30:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 8b1a9296-3e48-3bd5-9582-af2dabf68c21 | -6.9326 | -59.1254 | 2025-08-13 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 2b03b6bc-8c14-3ea6-a64e-2a96b2ddb636 | -8.106 | -55.5701 | 2025-08-13 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 4d7427f4-447e-39a1-954b-afc79bae787e | -6.0992 | -59.9267 | 2025-08-13 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 3f854707-3f5b-3e1c-9014-91c63921a40d | -6.8957 | -59.1269 | 2025-08-13 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 531.4 |
| 7a92e619-a6e3-3e1b-8c97-e570c5572a99 | -9.208 | -59.6548 | 2025-08-13 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 0c3fcee6-6473-3b64-af9e-e2bb0b9e2b20 | -7.6472 | -63.5148 | 2025-08-13 14:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 13e10dcd-20a1-3106-a95d-cf9f8a4447ff | -6.9325 | -59.1447 | 2025-08-13 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 262.4 |
| 787736d8-5314-3c09-9e7d-a89da46bbcd2 | -9.1892 | -59.6752 | 2025-08-13 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |


[Clique aqui para ver as próximas entradas](README37.md)
