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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50975565-347e-329b-bf37-9ef9bb5acea1 | -8.59495 | -63.88343 | 2025-08-07 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ecd8e47-6b20-3d12-91f5-8de29bf5e8a6 | -8.92433 | -60.55424 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6986c524-92c1-3d75-b4fc-a9be29ac4fa3 | -8.91963 | -60.58794 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2459fc51-3d47-3f19-ab4f-08089b9535e5 | -8.90532 | -60.55306 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a97385ce-f398-309c-b4f4-06ff6512277b | -8.9212 | -60.57667 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20723170-23a2-3f11-96ff-39e7dc83e195 | -8.9089 | -60.5574 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f8544ce-0ccb-3f28-b4bf-86ade7f3db9c | -8.90877 | -60.60551 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 602732fd-e8d8-3709-b3b8-100e8db2c60e | -8.90865 | -60.5879 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a777b722-cc88-34f6-8aec-3dd3dbd3464c | -9.93353 | -60.45801 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ec5ef43-2b73-3cc0-b11b-d1c25945a3e7 | -9.94089 | -60.467 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f65f29c-39ad-38d7-9779-7c8f3b2c03e1 | -8.90645 | -60.60292 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e02d6545-7ebe-3bd2-80b8-48d3fa9aae86 | -8.91759 | -60.57233 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb082dcb-668f-3f8c-8f38-8ac7e910aceb | -8.91085 | -60.59051 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76f993d1-3d71-31cc-b4d6-164d4f90ccd2 | -8.90563 | -60.5798 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d0218d9-c587-358e-b75b-14c473e416f8 | -9.93667 | -60.46642 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc25ce16-b9e6-3959-8cb6-63e5ad43fff1 | -8.91294 | -60.57547 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57b5be17-e849-362b-892c-55581ed7ff0b | -7.4135 | -60.0088 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9656514f-e35d-309a-80a2-cf409193b520 | -8.90477 | -60.5568 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01a0e474-b1dc-3616-8923-119443654abf | -9.93486 | -60.51023 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1946583-73db-3f9e-a8f3-2c6460c62f1c | -8.91278 | -60.58849 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 866dce45-b19a-31f5-b8c5-83c624913e07 | -8.92428 | -60.58479 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e46ee72-c381-3cd4-9517-11fed9b02831 | -8.91753 | -60.60299 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74db39e5-cabb-32a0-b63d-00bad0d8ccc4 | -8.91112 | -60.59977 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59ca1f27-acf9-33b5-aca2-aa969b61d63b | -8.9145 | -60.56429 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf17eb03-0436-3da8-a4f7-39e4f9fefe0b | -8.91886 | -60.74226 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2dfc9c92-00e8-3607-b4e0-abe64382cb6f | -8.91935 | -60.54365 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82010bef-bcbd-3cf9-b140-301055511905 | -8.91341 | -60.60238 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fdedc62-e239-3ea0-949b-aacb18d0ac1c | -8.91388 | -60.581 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a049b4fe-2bf6-3bb8-98f0-3f41ac3b3fd2 | -9.93558 | -60.47428 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0e50762-3fe9-32fa-a93a-fe0d8f2eef6e | -8.92322 | -60.59232 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcf71a1f-bbaa-3d26-b1ba-286257bf1bd6 | -8.9081 | -60.59167 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21474b0b-c491-308a-8576-f36d4d440384 | -8.91763 | -60.54179 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28cde629-8c92-3253-a4dd-2926177b2446 | -9.93244 | -60.46587 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f466dfe9-9c71-3846-bfd5-847b51ac840f | -8.91522 | -60.54306 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c16caa47-eba1-3219-84ab-95c6a75836f9 | -8.91731 | -60.75319 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d5fdb4a5-8a07-3a25-963f-1fb77a1657c7 | -8.91445 | -60.5949 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72e037b5-5e21-3369-8cc5-cbbee702fd3f | -8.90233 | -60.60234 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4287d387-2a7a-3b1a-906e-b1e9e4b65336 | -8.92172 | -60.57293 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6910f4e1-d2d1-38ab-a470-b187a1098e41 | -8.907 | -60.59918 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 499e5095-6385-376c-b43d-e2374aa7ba41 | -8.91916 | -60.56114 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b432fd43-e64b-36bd-91fa-2fb45193a8b4 | -8.90673 | -60.57227 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7588aaec-3298-32cd-9791-a357b609054e | -9.93722 | -60.46247 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e92a853-e65f-35db-9c42-35759cfff441 | -8.91349 | -60.54119 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e755f4f-1fbb-3a4d-857f-f51be84321e6 | -8.9103 | -60.57665 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b87a949f-2997-321b-befd-bb3b9f434cbb | -8.90423 | -60.56054 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55cef6e8-a8e3-32db-9487-3a69dcd8942d | -8.91393 | -60.59865 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c53ccbaa-56e7-34cd-9987-4389158acd9e | -8.91716 | -60.5586 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7c61497-6c1f-3fa1-bf39-8df7a09b1afc | -8.91805 | -60.59924 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4b39dc0-28b6-39d5-9528-a1bc9a8766b4 | -8.91938 | -60.73861 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 71769336-8a5c-31d7-bc5d-bfffb7a8b6b0 | -8.9227 | -60.59607 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cee749ea-faa9-3e18-b900-7e7468467095 | -8.91628 | -60.7605 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d3c29d4-f869-34c4-8026-18b536af7777 | -8.91826 | -60.55111 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd317d0e-53fe-36e1-a753-937e8f54be76 | -6.91738 | -52.84896 | 2025-08-07 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 334eb2d2-8a21-3869-a37c-fe9a7c5ba981 | -7.19189 | -59.83915 | 2025-08-07 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 103a5559-1c3a-3e37-9114-7cb655048e67 | -9.93299 | -60.46191 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82971bca-abca-3a68-a4a2-73b61b61097b | -8.90288 | -60.59858 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35e3a9db-f179-3a13-a9b7-9f20dae28690 | -8.90945 | -60.55365 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5650bb2-5eee-3fcc-82a2-66a8a00ab4f3 | -8.91303 | -60.558 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d73c9477-b319-3a9c-befe-5d59c4a1182f | -8.92276 | -60.56549 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f87d62a2-f753-381e-aa0d-831d507124f9 | -8.92243 | -60.74647 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 16cd5ad0-1def-337a-bc21-6563f5d442f2 | -8.9114 | -60.56916 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf144adf-9e8d-36ea-a483-d998a4adef34 | -8.90777 | -60.58239 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb022297-3847-3d58-bb0d-beb447c9a650 | -8.91037 | -60.56367 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be8d2f28-9d1d-3322-b45e-53838a4f10f0 | -8.9083 | -60.57864 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48b5cf55-d102-3fdd-a3ea-48745426db60 | -8.90986 | -60.56738 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6be036cc-5a41-388c-88bf-d5aa960bd93f | -9.93706 | -60.49448 | 2025-08-07 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d503432b-f400-3c47-a34e-c583c3fb3d60 | -8.91529 | -60.73808 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24549e72-df27-39aa-a9d2-144d448c8db0 | -8.92088 | -60.7574 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a3eb0619-8b54-33ab-b4a1-877f4dbf0129 | -8.91297 | -60.54494 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51f6dbfd-8f1e-3dda-8c48-7024285fff94 | -8.92381 | -60.55799 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a417756-b296-385e-b6da-a6b138c00096 | -8.90755 | -60.59543 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fc6e22f-9f5d-37bf-b143-d238bfd9c9ec | -8.9092 | -60.58415 | 2025-08-07 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06017a0c-c0b4-3d33-a2fb-5d884c5391e7 | -12.2814 | -63.83346 | 2025-08-07 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7dbe5119-5aec-3d43-bc0b-ee1e96c1e36e | -14.24986 | -59.67846 | 2025-08-07 05:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ccfde9b-d360-3796-bb38-5b7a883c09cb | -6.98654 | -43.39956 | 2025-08-07 05:46:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2147260c-649f-363c-a531-dea11f98bbf1 | -7.18786 | -45.48004 | 2025-08-07 05:46:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 33a2a686-18cc-3b55-9d81-3686372930f6 | -7.23777 | -44.63875 | 2025-08-07 05:46:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a0a6800e-9e93-3b2b-a808-4672fd79de01 | -7.275 | -44.3223 | 2025-08-07 05:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d3d8bab6-1f83-344f-949b-98037a73561a | -6.85319 | -44.3062 | 2025-08-07 05:46:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1069d152-ac4f-3976-b9cd-6ab52fd0738a | -11.74919 | -48.18542 | 2025-08-07 05:48:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2177d28a-55bf-3528-906c-183181fb1b8e | -12.54479 | -47.14611 | 2025-08-07 05:48:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2ef5c66c-bcd6-3117-8df6-dec20a9f60ef | -10.62981 | -44.73314 | 2025-08-07 05:48:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 011d8d81-3b60-3a35-b414-2036b7e0583f | -10.42041 | -44.39188 | 2025-08-07 05:48:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e70919fc-d343-309c-be15-ef342c26f6d8 | -9.07932 | -45.056 | 2025-08-07 05:48:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ad2deb61-71fa-3f7c-a9a6-80a7ed1947cf | -8.51827 | -43.30427 | 2025-08-07 05:48:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 2fd21916-39bd-3dec-81f8-ccca6aecb098 | -12.536 | -47.14476 | 2025-08-07 05:48:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c61739b4-a9d8-3bc1-84a2-95360af8dd12 | -10.62841 | -44.74288 | 2025-08-07 05:48:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 13382af8-abd6-3b11-8c67-03ea4fa7b8b2 | -10.64678 | -44.74556 | 2025-08-07 05:48:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c15a8883-7080-39db-924b-384875d7ec9e | -9.46148 | -40.38071 | 2025-08-07 05:48:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 726f3b38-58f0-3e6c-baac-c8d50c462350 | -9.65092 | -43.83892 | 2025-08-07 05:48:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 08b719ac-0739-32fe-bb15-1e2ecd660be9 | -10.44479 | -44.35482 | 2025-08-07 05:48:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4b54ce62-4b22-3ec3-9131-1cb73ebc15fc | -10.6362 | -44.75394 | 2025-08-07 05:48:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 7ece6964-6c50-337b-a727-d411e2c658e4 | -10.43261 | -44.37327 | 2025-08-07 05:48:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 18f67ca0-8882-3027-adae-2e7c98d21ba0 | -9.46638 | -40.36982 | 2025-08-07 05:48:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 2d5434a6-1398-3978-a124-f700fdc29207 | -12.54344 | -47.15504 | 2025-08-07 05:48:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 7f2d5f5c-ecab-32ae-9780-9d04de8e9585 | -10.42973 | -44.39325 | 2025-08-07 05:48:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4ca52ba3-eb53-3ccd-a6a5-0239df11a665 | -10.43117 | -44.38323 | 2025-08-07 05:48:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 534222c0-a0b2-3319-94b5-d6a3e4aa4466 | -12.63904 | -48.10625 | 2025-08-07 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e254b58c-bbb9-3ce2-a40c-fc5d8b574da0 | -11.76011 | -47.51443 | 2025-08-07 05:48:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a171dfc5-ab90-3a55-b6fd-3328a3704b7f | -12.72382 | -46.38105 | 2025-08-07 05:48:00 | AQUA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README27.md)
