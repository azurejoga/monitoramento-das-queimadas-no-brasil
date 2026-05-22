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
| 57be0377-2387-3361-83e2-0acaa32e7ae5 | -10.89067 | -53.74261 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7df11580-0db3-37f6-8c8a-a772f42165fa | -11.08852 | -46.68941 | 2026-05-22 04:53:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2f0d4c7f-4809-3e14-9788-5a6ab965ecd9 | -11.60948 | -47.90205 | 2026-05-22 04:53:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df7f9ccb-baff-32f2-8098-e77ab6126dc4 | -11.94809 | -49.29802 | 2026-05-22 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6080a7d9-2f52-34b0-882d-213ea3c0d498 | -11.99979 | -45.14717 | 2026-05-22 04:53:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adf63d9b-5d9a-3f52-a2e2-c899c29b57ce | -11.6057 | -54.19267 | 2026-05-22 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 14122caf-2e0e-309f-9b24-e013a521b21b | -9.94246 | -52.46573 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2702f5e1-be4c-3413-905f-e7801d80b422 | -11.18411 | -48.01651 | 2026-05-22 04:53:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ab85e40-cb95-31fd-bd39-f603f457e0c0 | -10.49271 | -49.35939 | 2026-05-22 04:53:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98a44388-50a8-31b7-b736-5913168a90dd | -9.94578 | -52.46625 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9532db5e-3fff-331c-aec5-bc59f11376f5 | -11.61738 | -47.90726 | 2026-05-22 04:53:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67d9109c-7a3c-3189-b189-853cc5f80689 | -10.88791 | -53.7386 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 056facb2-5008-3bf5-af29-5872805f21f7 | -10.91573 | -54.12368 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25edb801-dabd-315e-bd7a-7edd55a9707b | -11.15004 | -48.11256 | 2026-05-22 04:53:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5680a76-9a52-3a22-a874-1f31a485a274 | -9.94524 | -52.46978 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7109ab5-d0c9-3e5f-aca2-242bece770a3 | -11.3084 | -47.5796 | 2026-05-22 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4f83519-8e1b-342e-9a2a-ee00203fb213 | -9.9546 | -52.45318 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b32ea84-1882-3d2d-819a-e603d814b9ea | -11.30411 | -47.579 | 2026-05-22 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf2fbbfb-d338-3fec-abbb-82f6415c840a | -14.15112 | -52.89347 | 2026-05-22 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08d6f03e-a02a-3fc6-b4f5-8542f258d5ad | -11.31156 | -47.57804 | 2026-05-22 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9ad2113-4c58-3db9-832d-4961b6f9e0e2 | -10.39543 | -49.44238 | 2026-05-22 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87c7d697-3cb8-320b-9b20-406bd2ce6387 | -10.91242 | -54.12315 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e717b9ff-f062-38ef-abe8-b1dffb2775a4 | -10.4965 | -49.35994 | 2026-05-22 04:53:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 447e2dec-5d31-3d7e-b25b-20591f052e9f | -10.48825 | -49.36355 | 2026-05-22 04:53:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b0bd9b81-d291-3a40-9893-da97df21c24d | -10.9174 | -54.11313 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5dbe033a-c1ad-3152-8812-7c11ddc027ab | -11.15055 | -48.10875 | 2026-05-22 04:53:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42792e88-6895-3cc5-b72b-987876a294d5 | -11.61317 | -47.90663 | 2026-05-22 04:53:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b7ce55c-611d-3d87-b9f5-c3c7e0303811 | -10.67007 | -48.25453 | 2026-05-22 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfe4194e-7662-39e1-a7fc-3210a21e2d1e | -12.26798 | -43.51722 | 2026-05-22 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56e56331-2cee-3dcf-9953-9c357cb004fd | -10.66247 | -48.24961 | 2026-05-22 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdcc1b36-999e-3b8b-b88f-3b3693d50db9 | -10.66601 | -48.2539 | 2026-05-22 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86e92637-f4f7-3282-ab9d-61f32aae5aaa | -12.27324 | -43.52197 | 2026-05-22 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d00e4e1f-ea28-3e54-9fd6-54cb947536a6 | -10.88738 | -53.76358 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e4418dd-4695-329b-a164-79b074087ed9 | -10.59819 | -53.48085 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6edbc779-1073-3e07-9b7d-83dea7ad01d4 | -12.23646 | -44.26436 | 2026-05-22 04:53:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77ea1389-ba40-35aa-91a2-2b69bb5158c7 | -10.11688 | -52.41364 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6622761-49c0-398a-bdf0-0cc00bc5a47d | -9.9618 | -52.45069 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97d49890-351b-3c48-bbf2-a050975b8528 | -12.36892 | -50.0318 | 2026-05-22 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4645a952-2331-35c8-8f61-e43d3cad9d27 | -9.9447 | -52.4733 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8a9c426-dba2-3a3d-86e2-7a15af0c62be | -12.36454 | -50.0358 | 2026-05-22 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 853cfa54-d162-39a2-9461-db92cbad9c1d | -11.30896 | -47.57553 | 2026-05-22 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8c6907f-7483-310f-a1d8-65b518f0ace2 | -12.00017 | -45.14409 | 2026-05-22 04:53:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95a4efdd-94ae-32b1-9e56-9a092e726a83 | -9.95793 | -52.4537 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bac096ad-7046-370b-ba41-20616fa7f53a | -12.23603 | -44.26785 | 2026-05-22 04:53:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 09e6913c-11a8-3623-ab1f-c2882c07d931 | -11.04264 | -46.79118 | 2026-05-22 04:53:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 979a04b7-c9cd-3ebb-ba6b-e77c3c30bff8 | -12.88398 | -47.23819 | 2026-05-22 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e371554-cb07-35d9-bfe0-758d338f395d | -10.22789 | -52.66569 | 2026-05-22 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66862947-f982-35a8-ba55-5d0bfba8eb5e | -11.04327 | -46.78646 | 2026-05-22 04:53:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87b74a8a-ac61-3abc-a45a-a72cca238c9e | -11.9494 | -49.2996 | 2026-05-22 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a810816-bc80-3524-a8ed-1115eb8d5f73 | -11.31063 | -47.56342 | 2026-05-22 04:53:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de611da5-eab2-3e1a-961d-f067bfbd82a8 | -14.18302 | -52.88723 | 2026-05-22 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3553399-b0a3-3304-89ae-e366524b2377 | -10.91796 | -54.10963 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ed9a9a3-bfd0-3394-b854-d28c82a9b938 | -10.91409 | -54.1126 | 2026-05-22 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 040d4a8e-f012-3d6b-8c55-45760eca8b85 | -19.7672 | -54.07153 | 2026-05-22 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 391a6b6f-bf61-35cd-9ec7-54bd26c6a844 | -19.76494 | -54.06338 | 2026-05-22 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d260f796-fe76-32a6-aace-e65c4c8069ea | -19.1767 | -47.35931 | 2026-05-22 04:55:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bd33a58-8d7e-305d-8012-606d77d3e9b5 | -19.17312 | -52.54056 | 2026-05-22 04:55:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a7c54b7-0505-3ef7-8d33-75792b86ef7a | -19.7717 | -54.06446 | 2026-05-22 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 121ca7b1-6206-3cf7-b7f0-f9081ce05b48 | -18.11233 | -46.89441 | 2026-05-22 04:55:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7031140c-16b3-340f-a9de-ef78096e1dc9 | -18.63509 | -44.62307 | 2026-05-22 04:55:00 | NOAA-21 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7cbaa05-7526-3895-bb28-667b0f17aed0 | -19.77114 | -54.06826 | 2026-05-22 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aaddd7b2-6092-328c-8a0e-a0c4ec18c6f4 | -19.76438 | -54.06719 | 2026-05-22 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 989c07ff-3ba5-31fa-a638-0dc7736c015c | -16.27941 | -54.42957 | 2026-05-22 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef26617f-e1bc-3907-8ca8-75fd27bafcec | -18.9305 | -53.22906 | 2026-05-22 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36a3f790-29f2-3ee3-930e-651b4a2b6202 | -19.76776 | -54.06773 | 2026-05-22 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 53a921ae-16f2-377e-82f2-58d1088e18b3 | -19.76832 | -54.06393 | 2026-05-22 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 80bdb171-7784-3cb6-a662-f9e48e2e0c4c | -19.17351 | -47.35856 | 2026-05-22 04:55:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c438cbc1-d288-31b1-8426-bd58a4e3b326 | -19.77058 | -54.07206 | 2026-05-22 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 74bd2aea-715c-3713-83a5-77c95804095f | -8.55102 | -45.98384 | 2026-05-22 05:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ddb256ca-220f-3db5-a427-76c36b753391 | -9.92266 | -48.00909 | 2026-05-22 05:25:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a943f83-6553-3019-879b-242ecf82528b | -11.05995 | -46.7082 | 2026-05-22 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60aa0579-895b-33f8-8373-b7c3eac10cd4 | -6.56445 | -47.90333 | 2026-05-22 05:25:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a7e1a76-76d4-3dcf-9daa-a12330127a99 | -8.71475 | -48.3288 | 2026-05-22 05:25:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8979468d-0a38-3c5a-a01a-126ebe3ca49d | -9.94651 | -52.46682 | 2026-05-22 05:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13c99ecf-8274-34cf-a88d-b084317259ca | -6.56378 | -47.90815 | 2026-05-22 05:25:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04a78f20-a12a-3e27-b199-5e330a91cba6 | -6.56918 | -47.90261 | 2026-05-22 05:25:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2951cfc3-6899-38e6-9065-bf1b32b49511 | -10.509 | -51.94659 | 2026-05-22 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad334840-e52a-3a5d-a0ac-58ec6fa2584d | -8.92383 | -46.91462 | 2026-05-22 05:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85b3d653-d6bf-35e8-8397-7d743c7e338c | -11.05217 | -46.71383 | 2026-05-22 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d27a84b-5110-3d92-849f-653076100dc5 | -5.76691 | -45.12992 | 2026-05-22 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 009bff7c-6dd1-33f3-a491-4a3b01b930c8 | -8.55482 | -45.98629 | 2026-05-22 05:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ec127201-72f3-3aea-8192-7acf3e22cc05 | -5.77408 | -45.13121 | 2026-05-22 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 076fefba-b10c-3143-99dd-1d741a17fcb9 | -8.92984 | -46.92137 | 2026-05-22 05:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c899124a-a121-34ca-a8dc-fd65fe4cb9f8 | -9.31212 | -56.17049 | 2026-05-22 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c79e4bc6-2fd9-332f-8e87-aeff7f51bbb8 | -8.71539 | -48.3239 | 2026-05-22 05:25:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1dc2f4db-5b94-311c-ac31-00d52284ae56 | -6.57061 | -47.90429 | 2026-05-22 05:25:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 961131c0-6dce-31a7-a736-c57813da34d7 | -8.5486 | -45.9785 | 2026-05-22 05:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef0c2f20-4df9-3f00-a180-e7e1415454d4 | -9.94581 | -52.47197 | 2026-05-22 05:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d323484-7953-3787-88fa-5f3805d12982 | -5.77316 | -45.13792 | 2026-05-22 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88e2ec81-0fd1-3dd2-99c7-bde4eb9f395a | -9.94103 | -52.4713 | 2026-05-22 05:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba71b3c8-8bfb-3771-ae7e-c3884d8d2c74 | -8.55815 | -45.98455 | 2026-05-22 05:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6dc5220d-a43a-3e62-b192-800f29957766 | -9.94173 | -52.46614 | 2026-05-22 05:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99990d83-1e2b-3df7-ac45-4f541f9a3b30 | -9.92333 | -48.00369 | 2026-05-22 05:25:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2cdd9cb-8d67-3b9a-8d95-ce27eb51b2a8 | -6.56994 | -47.90906 | 2026-05-22 05:25:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c6cd664-79cc-336d-a80e-204f39a92c33 | -11.0499 | -46.71904 | 2026-05-22 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 943a9fbb-e5e6-3392-86a8-24cf4eb049e0 | -6.56854 | -47.90743 | 2026-05-22 05:25:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bc120e9c-4dab-357c-b14b-457b66e37bd0 | -11.06618 | -46.70082 | 2026-05-22 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d9b11c1-ca2a-301d-97de-03a6eac2cab5 | -11.05134 | -46.7208 | 2026-05-22 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c23e515c-0e66-302d-8aec-a39bc1e7ebd9 | -11.05068 | -46.71207 | 2026-05-22 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a92f459-0aef-3d3a-931b-7748002a2e01 | -7.64329 | -45.30456 | 2026-05-22 05:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README7.md)
