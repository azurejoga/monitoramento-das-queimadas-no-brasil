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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1702a520-7440-3fbf-a5b6-180b1c01cd43 | -7.12964 | -60.1217 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02dd583d-ffb7-3ac9-a472-0297837a9e1c | -7.80623 | -61.34387 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 972dcbc6-606a-31ed-a0c2-9805062828d1 | -6.88516 | -59.15401 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50534047-4072-365f-90a4-8e8c967d1218 | -7.2822 | -64.69634 | 2025-08-15 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 611a11eb-4846-366c-afbe-bd73abd9522d | -9.18548 | -59.6641 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e92da695-e064-30c0-bc94-bad630acaed5 | -7.29818 | -60.62423 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c66100f4-668d-3817-9451-e31b3c5c0c06 | -10.35677 | -64.44579 | 2025-08-15 06:10:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 542731a1-33ca-372b-b9ec-5e782d7eca5b | -9.50946 | -60.54258 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1fb528e8-0b6f-3b80-a5c8-d9967429dde1 | -6.93198 | -59.53017 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d861a73b-8d60-370e-9d4f-ed20a2ce0b25 | -9.50314 | -60.54185 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46007c9b-f647-3a60-954c-00e385408328 | -7.60141 | -63.50484 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6c3b85bf-19ec-311e-959f-1f68033ce8c3 | -6.7076 | -58.82378 | 2025-08-15 06:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6c942837-b36d-3815-913a-39fa695e6e10 | -6.93845 | -59.53125 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18dbe07a-74c9-3e5f-850c-0e84331bd0c7 | -7.3238 | -60.61856 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4d6e4b7-d6f2-32a7-8f91-5e4ac455a845 | -9.17886 | -59.66319 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86878112-c794-321a-8566-0ba461726d54 | -7.08253 | -59.22958 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f597d4b-4ec1-3c03-9086-cd6065492b3e | -7.9564 | -61.76255 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff870805-fbf3-3810-a208-671c1c6a1bb8 | -9.34513 | -62.58903 | 2025-08-15 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9e2e6f5f-c8d8-3793-b943-976f3ed4aa71 | -7.61999 | -63.51945 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be51f0bd-a747-3cbb-97f7-ff2a6625b6b3 | -7.28755 | -64.69217 | 2025-08-15 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5229d6ac-357e-3d25-97ce-8a5b300bde49 | -7.53479 | -61.34693 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c75cfe8e-7dda-3b6f-89b0-62ef925c9c4f | -11.73411 | -64.89649 | 2025-08-15 06:10:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af12b156-2e45-3dea-9522-698c1c8000b2 | -6.90163 | -59.13266 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b84c7e7f-6bd6-3fdb-914f-b490b61af0c9 | -6.70372 | -58.85366 | 2025-08-15 06:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad556e58-1344-3d0b-8264-3090c41a12b2 | -7.08792 | -59.21255 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f43c4f9-1481-329d-b869-185480e257a4 | -6.94709 | -60.00369 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ac52aac-6f10-33b4-8a5b-a197d22198e1 | -12.89044 | -62.09289 | 2025-08-15 06:10:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c31d7f71-1a7e-37b6-9140-bfc6adae8cae | -8.1032 | -61.18083 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 184af485-fd9d-3a5c-891b-b31409a02f24 | -9.16875 | -59.69044 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2970655-7068-3437-8020-a7e6061a2c99 | -6.94777 | -59.9987 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 708ec9ea-1d91-348b-9f62-f3779166b8e1 | -7.52541 | -61.32867 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e32289a-d913-3321-8ef8-153951625893 | -7.07389 | -59.21645 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 891b36c3-a551-3adf-9186-68daa66cba19 | -7.60322 | -63.52902 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef1a4114-efa1-3d7e-ad32-6f1cb428caf1 | -7.62464 | -63.52309 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3592d122-45d9-3ee9-80f9-d9f3bca745f8 | -7.87865 | -61.80677 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ef13d0e-e8a9-3c7c-a6be-8f36996ed6b0 | -8.10633 | -61.20327 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40da3481-fa82-39fa-b9f1-abebe33dafc7 | -7.52977 | -61.3358 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7b564dff-2370-33ab-bd2e-94b96dcfae3c | -6.91 | -59.14555 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f89a7ade-3542-3e7e-a683-f48587c9da35 | -6.93126 | -59.53571 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| caa57fe0-fb61-3384-9fa4-1dc219b6d9a9 | -7.33583 | -60.62108 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fee2a03-cd91-334b-a2d0-d0c47fe456ad | -9.2002 | -59.65417 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d545d207-719c-3d9f-a142-0bb58032053a | -10.32631 | -63.6191 | 2025-08-15 06:10:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92d04e00-9ffd-33a6-8429-0683d51bfb57 | -9.18479 | -59.66966 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd599fa0-45a9-39ed-bf04-8f86bebd5225 | -7.30417 | -60.6258 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63f079e3-d449-3cc2-b1cf-550b66051946 | -7.61494 | -63.51874 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be853d14-7725-3ba5-b317-5f1548876b92 | -6.88418 | -59.1361 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81c56755-365c-35a1-ad4c-4f25c883617f | -7.87083 | -61.82159 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39e336e4-1fab-3e45-a3b2-016ae0b95efa | -9.49871 | -60.52612 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0431cc1f-e510-3e99-9233-aac1cb534ac5 | -7.08714 | -59.21827 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 45675832-9083-38f6-9e76-d808d431eab8 | -7.53958 | -63.48082 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4ae0cd5-ff93-3e6e-bc01-4f90e11f8c37 | -10.00971 | -59.22306 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 015bbc4a-1d7a-3f32-9e28-867881f33713 | -7.54804 | -63.49397 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cfdc4b1-5234-3136-a49d-dfc226d4bb3a | -6.92401 | -59.14193 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32332372-299e-3e5f-ac21-a42edf8d90a4 | -9.50819 | -60.55256 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aee83eea-7a78-32d8-9f03-272c4a258f35 | -7.53451 | -61.34501 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e61b197-073b-3fe0-b3d0-eeaaf5a27d83 | -6.89822 | -59.13225 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10735066-fade-3f98-8f88-b56c4d72de94 | -9.1869 | -59.65278 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f523dc2-5c24-308f-8f05-92518542940f | -9.39125 | -60.54485 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f27ea3a3-449d-3198-8628-619894a65982 | -9.92082 | -63.18541 | 2025-08-15 06:10:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ce2cb4c-2d21-37b0-97b7-181d093bfe77 | -9.20453 | -59.65485 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bef97f01-dada-375d-9a2e-fafec4671a54 | -7.81434 | -61.32795 | 2025-08-15 06:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78489f32-36d7-3bdf-9dca-5dac7d5a6e00 | -7.32257 | -60.62746 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ffabb35-70da-3a0c-98ee-8bd1dc5428b1 | -7.88079 | -61.80753 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5cd4073-3384-3999-bdfb-7ba4fca09ceb | -8.11283 | -61.19975 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bb42a2e-2f67-32ae-8e72-a5dafce76982 | -7.6301 | -63.52087 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f481e6c-00ad-3985-819f-3ef75a71d7db | -7.87812 | -61.81063 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f20ccbaa-ff3e-380d-a3c5-58539ed9acc4 | -9.63532 | -63.09266 | 2025-08-15 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8abb7339-0e48-3eeb-9023-b7deb296e2ba | -6.9248 | -59.53458 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdb0516a-0de8-3fd9-86d4-fa090a31fbf1 | -9.6327 | -63.09542 | 2025-08-15 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7aec7168-e963-3337-abb9-ea1915d1002b | -7.87876 | -61.82323 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dde3765d-b714-3848-874e-a9acd4bf2ea1 | -9.50378 | -60.53679 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 75e49cc0-eb0d-334c-b441-35402f725641 | -10.36171 | -64.44646 | 2025-08-15 06:10:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7ca5283-138a-37a0-9ad8-abd3e9f9327e | -7.60222 | -63.49899 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 40656511-cf15-3ca0-b477-731d4986667c | -7.96107 | -61.77108 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78bff5b2-4cfe-3c6e-a839-88f62fd88a5b | -6.72628 | -58.83864 | 2025-08-15 06:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3e37c513-6725-3748-814b-c2dd1d424d3e | -9.20616 | -59.66034 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a2b94e8-2783-3810-ad3e-2bd49296e28c | -9.89777 | -68.59305 | 2025-08-15 06:10:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 188ebb95-1cdb-32a3-a522-f50d7a51cf1f | -6.72192 | -58.81949 | 2025-08-15 06:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 164b0e1d-4ed1-317f-97ed-2b6d9fd9f542 | -6.87287 | -59.83389 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 245a497a-b71e-3a6b-90f0-9b0e44ea4759 | -7.29208 | -60.62341 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58127090-f5d2-3810-8a46-acb347925406 | -7.28151 | -64.70112 | 2025-08-15 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd77cc57-41f5-30d5-9e0d-1a65d236761d | -7.52448 | -61.33081 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a16dadec-4cd0-3a14-8dde-86a034be70e1 | -7.59817 | -63.52828 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05c1672a-3999-3875-85df-27d8390f082f | -9.62951 | -63.09534 | 2025-08-15 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cc47a28-65cc-3e5b-80cc-9ed5af093c78 | -6.94936 | -60.00467 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a53c565-7907-3855-b1f9-ceb63398536f | -6.91764 | -59.5389 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffefbcc0-ce0e-3d99-b9a9-067576f7a70c | -7.28599 | -64.69389 | 2025-08-15 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69d4bb62-753a-34c9-b236-19efb6e5fb12 | -7.30475 | -60.62137 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 147c479e-aadd-321f-abd5-37b41d3f3ece | -6.95096 | -60.13985 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67c9bb26-044a-3b00-a7b2-f6ddc8564921 | -9.2083 | -59.64333 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 394fc444-02d9-3c4f-87f4-59518b5ec475 | -7.31708 | -60.62224 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 758fb1e7-3240-3fd9-85b7-7ec6a54bd562 | -7.61918 | -63.5253 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f674139-940b-3193-9691-00da8b66e186 | -8.09968 | -61.18705 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52e8c9f2-ef8f-314d-a93c-9028d9bb7c6d | -7.95836 | -63.46791 | 2025-08-15 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c6a98bc-8bdf-3a78-875a-154053c8f1bf | -6.87851 | -59.15316 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f88e49c2-4411-352a-94e2-b6e2de3b0c18 | -7.32363 | -60.61941 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe0f30dd-b4c1-3b45-ba9f-ec3781785659 | -7.29198 | -60.62417 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7ebe725-55c3-315f-94ee-65c849fbb1ae | -7.60101 | -63.50779 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d55f3370-2d1b-37b3-89d9-3d1b55e6d9d7 | -6.89008 | -59.14276 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55d927c9-cc03-3d95-bd14-91efe697aa52 | -7.53068 | -61.33364 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README70.md)
