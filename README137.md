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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1093201-2956-31f6-9a23-b59494bfcebd | -11.0867 | -45.6459 | 2026-10-07 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| d8447c86-91a5-3d7f-b2d1-66aea3370129 | -8.3391 | -72.6012 | 2026-10-07 15:00:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 123ad90a-885d-33eb-b64b-f4687667aa7e | -7.8146 | -45.5009 | 2026-10-07 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 9f06fb53-ea82-32a9-b4ea-9080af0aaae7 | -8.6106 | -67.0486 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 3a7158dd-507a-3fbc-9ba7-81c7df606599 | -1.4569 | -54.796 | 2026-10-07 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a6a5829e-ef88-31c2-8f53-f8d86aaa0d06 | -3.2577 | -54.0217 | 2026-10-07 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| dac1fb1f-5abc-3c13-ae0b-9376e152d023 | -7.7579 | -54.9499 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| e76dbf26-b120-3764-ba1b-dcc8f0c10409 | -6.1973 | -52.85 | 2026-10-07 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 075c91ce-b917-312d-8472-114b040f655b | -6.0074 | -53.5325 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7239a6f2-c95b-3d7f-8542-8a4325371e07 | 1.7121 | -55.6063 | 2026-10-07 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| b9bad6e5-1541-3ee7-8d98-8169a62e7d40 | -1.2455 | -49.062 | 2026-10-07 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 4bc40204-071c-306f-af9e-2fd7f798e80a | -9.1408 | -64.3836 | 2026-10-07 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f2297042-099e-3ebe-be0f-6593ad32269b | -10.6199 | -60.4852 | 2026-10-07 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| d0475dd2-0699-3415-9811-08cd11aa0371 | -7.2 | -55.1026 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 436.9 |
| 6e18c6dd-de55-3728-b64e-a6090413b907 | -3.0002 | -54.0483 | 2026-10-07 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 56b48ef7-475a-3651-b024-a8ce7c417480 | -2.998 | -54.7492 | 2026-10-07 15:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 76eac88a-4059-3319-8d39-6b2a35eb419a | -11.0863 | -45.6688 | 2026-10-07 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| c6c552ae-4c19-3d54-8710-48aab91cc991 | -6.6879 | -45.578 | 2026-10-07 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 421915bc-65d8-3e9d-bc5e-fe8fd0c8dea4 | -6.4756 | -52.8142 | 2026-10-07 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| b4ff16c7-3eb4-33db-ae5e-6162023d3bd9 | 4.2247 | -60.7051 | 2026-10-07 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 68096a71-991f-3100-9d69-e823dbeb2653 | -2.9816 | -54.1291 | 2026-10-07 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 42c8f9fb-ab51-380f-a202-6e7f4e7d0c4e | 2.0048 | -55.8392 | 2026-10-07 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 9873b550-0bef-340e-b5db-13884cc6950d | -11.1054 | -45.6662 | 2026-10-07 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| be492a09-0b6d-38cd-8a28-a81c6cc40266 | -0.3768 | -52.0153 | 2026-10-07 15:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 4c2ceaf3-3183-3fe5-a650-0a439724646b | -3.0 | -54.1287 | 2026-10-07 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 61c4e1d7-c433-36a3-98f2-98b0a2ef9487 | -2.9451 | -54.0497 | 2026-10-07 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 5a266678-6f36-390f-a8f3-70b1266fb0e3 | -6.1217 | -53.0584 | 2026-10-07 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| efddd3aa-d753-376d-b6ab-f837c11ffbbc | 1.6385 | -55.8047 | 2026-10-07 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| a355e707-2006-3754-ba78-5dcfdffb7a6b | -8.2621 | -54.717 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| efa0d5cc-483d-3d9f-ac93-9d47c8503a00 | -3.2214 | -53.8818 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6d3e7a46-bd4a-325e-a5b1-a8384e48aaee | -11.2337 | -44.8446 | 2026-10-07 15:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| e86ed050-bbd7-3e4f-a453-6fd83beab023 | -10.8054 | -46.5662 | 2026-10-07 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 2c51b277-b609-37bc-b817-5dc92ae8b0e8 | -11.8315 | -43.5391 | 2026-10-07 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.2 |
| d7e6ba0d-d134-3298-9231-7f1ce4e0d3b8 | -8.5912 | -67.3084 | 2026-10-07 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 5cc01587-98e6-3346-8d33-ba080e388f56 | -9.0987 | -65.3783 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 39c35012-53cb-3a7a-8c77-ea14b004a806 | -5.8204 | -53.8457 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| a5470ecd-7691-385f-8096-b46b88753830 | -4.1194 | -50.8192 | 2026-10-07 15:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 984809af-32e3-3f28-af51-f9c89e503a88 | -9.0046 | -65.6988 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a2322dd2-aaa4-3831-87e5-c62f1db58156 | -3.0559 | -53.9062 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| cecc3f34-21a1-31ab-9a68-6517d0db7d2e | -9.1356 | -65.4145 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 854ebb2a-0fa5-30ee-ac4d-7d82253da039 | -8.2314 | -61.3732 | 2026-10-07 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| aee5b9b1-1984-3162-a3d6-4ce7a5ff4f4d | -2.9819 | -54.0488 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 2cc9becf-62b2-3ff9-a443-6c533d8dc835 | -3.2577 | -54.0217 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4d466b11-9084-3ab0-bcac-6e8a24cdf927 | 3.9497 | -60.9198 | 2026-10-07 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d316aca8-7047-3971-806c-54dc6d208146 | -9.3394 | -65.4638 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 06929f7c-8df7-31a0-b4bd-50d6147c03bb | -3.0373 | -53.9469 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 8cd29066-3f62-348d-bc39-14ca79cc22bc | -9.1363 | -65.2835 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| eb7661b3-9420-3571-ae51-ac5e7aa30fea | -8.7503 | -69.6474 | 2026-10-07 15:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ba99f1e2-75cf-385f-a6e4-d2a3a49d894e | 1.6385 | -55.785 | 2026-10-07 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| cdec4cc8-b697-3a53-bc25-a73246fe3397 | -7.2179 | -55.1817 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| bafd5e62-dc84-39e7-8ab0-2ef599abb2b6 | -1.4569 | -54.796 | 2026-10-07 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 8c10f8ee-f599-3321-803e-6daf81db9f81 | -9.1222 | -64.3843 | 2026-10-07 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| d8a38bca-fea6-37ca-b657-6d8c084627ed | -9.1174 | -65.359 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 01f477d1-d0db-3f58-ad20-2c1640df2532 | -3.2945 | -54.0006 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 22c4f236-3c98-3c39-9ebb-735b077a0b00 | -1.4569 | -54.7761 | 2026-10-07 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| a59f75f6-ece5-3a3a-89ed-9f355db44a29 | -9.5313 | -46.8513 | 2026-10-07 15:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 47b34d27-3cc4-3510-a14e-b5d5fc4221bb | -6.8094 | -55.3036 | 2026-10-07 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 03e25388-cbaf-3298-8deb-da8918def7f7 | -6.4413 | -55.0224 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 7dc16174-16fe-3258-b368-56ba06463b34 | 1.7121 | -55.6261 | 2026-10-07 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 97a4fec6-80ec-3c7e-ab0e-527fdf302f69 | 1.7121 | -55.6063 | 2026-10-07 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f5865bd8-fa5e-3dcb-a583-b31df88b6057 | -12.2132 | -44.6991 | 2026-10-07 15:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 238.8 |
| c8d17d4e-f0cd-37db-bea9-9bcc6fdf300f | -3.0375 | -53.9066 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| e93f637f-d89b-3e12-90d2-db4ff91ef1e3 | -8.8364 | -62.4321 | 2026-10-07 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ae1f5213-9f7c-37c0-bd84-8a40830c98a1 | -9.0244 | -65.4181 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c5e7bb67-1055-3919-b4e9-f921ee9fcd38 | -7.5332 | -70.0331 | 2026-10-07 15:10:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| de43e502-bcae-3b4d-bda6-8b7c95a4d9c0 | -9.2363 | -67.9591 | 2026-10-07 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| c173d64d-f219-3dc7-9665-57ab6fca493a | -9.1542 | -65.4138 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 72614633-61fc-3ede-8739-2ea02faeff4b | -3.0002 | -54.0483 | 2026-10-07 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 3178e2fe-77f1-3733-939c-55dcfd45cb77 | -7.7579 | -54.9499 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 875673ac-f5ad-3974-8be5-6a281f5240e6 | -6.0076 | -53.4919 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5e6393ea-9f04-3b84-870c-dad33996fc00 | -9.1408 | -64.3836 | 2026-10-07 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 863b0234-9ce1-3b7e-afc2-cfb7c2fd99d3 | -3.6021 | -55.311 | 2026-10-07 15:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1285cf80-4ebc-3932-864c-ddc5d04b89b1 | -11.0935 | -47.6019 | 2026-10-07 15:10:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 0030d2e8-3f4f-32bb-89d9-6e6a2efc27b9 | -9.4124 | -45.8767 | 2026-10-07 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.9 |
| d8c1d5f5-f47b-3d60-a2b8-28a3c6cc4ff5 | -9.4751 | -64.3336 | 2026-10-07 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8009db4d-5b64-3371-b5bd-7f68ca7a9b27 | -8.629 | -67.0667 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 5bcf2045-c871-3f24-bb66-9170e122f33b | -8.655 | -54.5494 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 083570e6-cc48-3c08-8a9a-bcd5f3fcf516 | -9.006 | -65.4 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 84706cc3-738a-3b5e-b7a6-82228b3d5eb7 | 1.8221 | -55.5456 | 2026-10-07 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| eeb97245-e122-3181-ae3f-222b9089550f | -7.1814 | -55.1036 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 31a67bc0-79fd-3603-8a84-1a62204360fe | -2.9979 | -54.7692 | 2026-10-07 15:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d4e93a07-65b3-32f6-ad08-a8bf5444d206 | 1.7671 | -55.5661 | 2026-10-07 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| faa51070-4bce-3b15-bbe0-dc3286c52cbb | -8.9874 | -65.4192 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| fb275d94-bb0b-3884-b491-db76facec77b | -10.6199 | -60.4852 | 2026-10-07 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 132e6e60-7103-39b7-873e-58e64df1ac22 | -9.9175 | -65.0313 | 2026-10-07 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6d0865ac-aa83-3705-9a0f-c050b70319c6 | -8.6291 | -67.0482 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 452126ab-870d-3a86-ba08-a6104ae1f474 | -11.2295 | -46.2403 | 2026-10-07 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| c9998ae5-8cf1-3357-9ceb-4b269dc22565 | -3.0558 | -53.9263 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 39e84d9c-410d-3270-ac15-88312c7f12ec | -9.6757 | -65.0401 | 2026-10-07 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 30556b8a-5fee-3013-9a0c-27a740a58ddb | -6.4756 | -52.8142 | 2026-10-07 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 3c347243-0566-3457-80ee-a9891b40f359 | -1.2265 | -49.381 | 2026-10-07 15:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| caddb758-6791-3ceb-8383-fcace91538b9 | 1.5283 | -56.0227 | 2026-10-07 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 77b43468-2538-3d86-b773-50b165af6cd6 | -9.0612 | -65.4916 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ff76efae-d42a-33d3-b575-b0eefb924732 | -8.8365 | -62.4131 | 2026-10-07 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7a6d3499-04dc-3568-82dc-425fbcb05ed1 | -9.0612 | -65.4729 | 2026-10-07 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| aa065385-e370-33c8-9ea8-b923254da763 | -12.1746 | -44.7051 | 2026-10-07 15:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 9c927525-c75a-38b6-a5a4-900559c6a1bb | -2.9451 | -54.0497 | 2026-10-07 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 075922a7-8769-3e48-8e5d-3ce9afb1a788 | -12.2136 | -44.6758 | 2026-10-07 15:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 77b639d0-2828-36fb-bd40-7e74d2e80677 | -11.0863 | -45.6688 | 2026-10-07 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 7dc119d3-15e0-31cc-889e-a30f75246cf6 | -7.89 | -54.7206 | 2026-10-07 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |


[Clique aqui para ver as próximas entradas](README138.md)
