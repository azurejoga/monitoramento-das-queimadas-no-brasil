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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc6c1d72-5e7a-302a-a150-df7fe690b42e | -12.53986 | -48.49854 | 2025-08-18 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46d10145-c2cc-321a-bd55-662f489d3b40 | -13.58218 | -47.75932 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c469e02-f4c9-3919-ad3b-d808e835815a | -15.85609 | -50.21785 | 2025-08-18 05:14:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cb7f445-4aae-306e-b1f4-2b1571215fb5 | -13.86486 | -45.54958 | 2025-08-18 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f904c748-8fac-32db-be65-acd73c0f767a | -13.44538 | -45.88565 | 2025-08-18 05:14:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4faae4f7-552a-3b62-8c5b-3669c4185ac8 | -14.17456 | -45.29979 | 2025-08-18 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 944027f7-d630-3739-9e36-69f506c4b9ba | -13.133 | -57.15106 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34e85888-31f5-3a6a-a57d-eb5e78a46317 | -12.53415 | -48.498 | 2025-08-18 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85025eee-cf86-333b-a533-c8f7b46d3f70 | -11.31359 | -55.2198 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfcf6bfa-a816-3533-82f3-efc24e562160 | -13.20685 | -50.7549 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 382798d1-1da9-3d80-b031-f7675814ee96 | -13.01297 | -56.84116 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5426069c-00b5-34d4-a857-db730c34243d | -12.54509 | -48.5029 | 2025-08-18 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06b16709-c50c-337b-a17e-87f8cc9021b7 | -10.43439 | -60.29452 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa5efddf-0340-3208-9b5d-85d284b79963 | -13.00781 | -56.85202 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1fa19f7-6e5e-3430-8aa7-5f4a8918c9fd | -14.6308 | -54.90113 | 2025-08-18 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b74a03e9-ad15-388e-9274-653f3edfdd63 | -13.22096 | -50.7625 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| cbf5614f-5405-3430-bad4-8e741ed62a7b | -13.13128 | -57.13937 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f5a060a-d68a-35f1-ab66-b17a34023a48 | -11.31485 | -55.21136 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e034a9a4-9f3f-3db6-9899-6d4db834995b | -11.3603 | -55.43444 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 686c3566-d73a-3a3e-9440-e609c31179e8 | -16.1606 | -50.02562 | 2025-08-18 05:14:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16d7ac09-8c42-3088-8d44-808a42a486f9 | -13.58657 | -47.7585 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7939f738-78b1-3751-9ee6-96844a6d12d5 | -10.67568 | -51.56708 | 2025-08-18 05:14:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1cf4c55-7f93-37bb-80f0-b240328f0841 | -13.21671 | -50.75621 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 775df489-7af5-36c3-a15a-6af11fe7981f | -9.51402 | -60.52728 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10f9e6d3-95a2-3d17-909e-ecb6d878be89 | -13.22303 | -50.74563 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 079256fe-cfd7-3b08-971c-0593555989da | -12.99521 | -56.86557 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f50e8a74-00b2-3588-b6ec-1065d3cde8fe | -13.21178 | -50.75555 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9528c30-dc6e-3be8-90d9-5c02da85938c | -14.63781 | -54.90695 | 2025-08-18 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9dde8a2e-baa0-3505-a096-a0652d2afa81 | -13.21525 | -50.75522 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 85529aaf-a57f-321b-b99a-d4cc09c4d565 | -13.13412 | -57.14362 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9d3e479-edfd-3993-8008-2c3345d1cd3e | -14.17954 | -45.32117 | 2025-08-18 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e99e7269-da44-37dd-9ab3-648539fa3ce8 | -13.01525 | -56.84929 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6074f8c-eded-39ee-925a-e88c3514684e | -13.21306 | -50.77203 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| ecb585d0-b898-305c-92b9-878005894676 | -13.24635 | -50.80011 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| be07980c-0cb5-33f9-9ca7-f9eac3e5add5 | -15.61214 | -54.30373 | 2025-08-18 05:14:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 720aeaa9-f807-395c-bc6f-a31435959603 | -13.02149 | -56.84957 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce4f6734-d721-31ea-97bc-2b93f44b4a24 | -12.53938 | -48.50238 | 2025-08-18 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 588dcd41-e9ae-3195-94c9-a960fe3edbbc | -12.99751 | -56.85044 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db666e6e-1b5f-3714-beda-a29964bf582a | -13.00495 | -56.8477 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 336a6ea4-a567-360d-9277-840a19690464 | -15.00859 | -54.78448 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| faf72173-28ad-3878-8a8a-111859348864 | -13.8725 | -45.54348 | 2025-08-18 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03096ce1-67e2-335f-b259-bbb6de14288e | -14.18457 | -57.54876 | 2025-08-18 05:14:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bca605d-be19-35ea-b5ca-3fc3f985438b | -11.84676 | -51.57806 | 2025-08-18 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fa6e3f0-1128-3cfc-a2ea-6f63e986a578 | -9.51219 | -60.51934 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d82d82b9-30e9-3b88-af6e-7e79e43c9fc1 | -13.20393 | -50.76513 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 641b5f13-20e9-32d7-a6b4-532aef935598 | -13.125 | -57.11168 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19bde195-e009-3078-95a2-a2806ffeb60b | -13.58964 | -47.74724 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d35bc44-ddcd-304f-8449-f89b42ef4ea5 | -15.86784 | -50.20919 | 2025-08-18 05:14:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6510da9-8dcc-3840-809f-28bfb2a6b62f | -14.5892 | -47.96073 | 2025-08-18 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2465ee4e-3e4e-36dd-9776-2978f19556a3 | -13.20548 | -50.76614 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 97f441f0-2108-35ac-810c-42394a8fca9f | -13.22372 | -50.74001 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9de72e29-156c-3524-9bee-c9724602fccb | -12.54558 | -48.49893 | 2025-08-18 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dba9b16-162e-3c69-992c-9f7192ec95e6 | -10.99964 | -45.64832 | 2025-08-18 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4cbcb32-76e8-3ec8-b85f-fbc140dc79b3 | -13.14549 | -57.16062 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 495a379a-b338-31a5-8446-a846d9bad042 | -9.52173 | -60.52449 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a74415a2-84f7-3052-b84e-4506761d74c2 | -9.50867 | -60.51873 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6327a9fd-a571-3972-a7d7-5cb324520519 | -13.98366 | -48.10548 | 2025-08-18 05:14:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82d5858f-35a4-3395-9ed0-a7582995172b | -9.51572 | -60.51992 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7fb46824-d02d-36cd-9786-3c10e9a6d742 | -9.51754 | -60.52787 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 753462e0-493c-39df-979a-e510da90fbc1 | -13.01468 | -56.85309 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6534306-d73a-379d-882d-7732aeeaf172 | -11.74948 | -51.71272 | 2025-08-18 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b53b1029-0d8e-310e-a67b-79a6264088b4 | -13.22237 | -50.73904 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a70b098-df77-3917-876e-b5a876f36c61 | -15.86747 | -50.21239 | 2025-08-18 05:14:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f9d25bb-7b2f-3e4c-8485-727d8318e72c | -15.61568 | -54.30784 | 2025-08-18 05:14:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1432476f-a8e3-39f8-b66c-0baeadd18a15 | -13.20465 | -50.75953 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 88aae352-e5e5-3c68-9ac7-7f9fd1e09893 | -13.21809 | -50.74496 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d74868e-2795-37ac-978d-3937cbe8821d | -13.13469 | -57.1399 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbc6aadb-ff7f-3655-ad4b-3ef706fbe16c | -11.74886 | -51.71734 | 2025-08-18 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 362d030a-d95a-36b6-baec-008cd3a38d18 | -14.06814 | -54.08132 | 2025-08-18 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9ce785c-51a9-3082-9249-d7b8358029b3 | -13.21247 | -50.74992 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7eaf626c-cbfc-3c26-b3ee-102e4ca62c6f | -13.2174 | -50.75059 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb9a6c33-b773-3b3d-86c6-674044a5dd7c | -13.43442 | -57.02413 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7608cf05-7c2a-3804-b820-1d18dbf7c340 | -12.99064 | -56.8494 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c672f80d-2cf5-358d-9bab-ac8eccb82d67 | -9.51155 | -60.5233 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdc2c227-872d-3ce6-9281-95cba1c66166 | -13.17018 | -54.93202 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d6bb596f-bbd7-3c55-a548-544cddd8b2cf | -12.54693 | -48.50118 | 2025-08-18 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8625965a-dba7-3f85-bf8a-358cd7dfe999 | -13.17459 | -54.92803 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8ee48994-47fd-3aa3-9725-290fda64b2e1 | -13.01182 | -56.84876 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e1af60a-cc0a-3787-a13f-f2c023b5296e | -14.62563 | -54.91027 | 2025-08-18 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ba993b4-8d27-3b3f-9831-552d8aac0438 | -13.21534 | -50.76747 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 1b302e3d-7f39-3f63-a6cc-8bc9617191e0 | -11.35566 | -55.39155 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ce22ec0-132a-349c-951b-ec10af9b8434 | -13.61174 | -47.76859 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 834591e3-992c-31bf-8a3a-d13850517703 | -11.35925 | -55.39206 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00cca30e-1ee2-345d-8eeb-bb97aa32e5e2 | -12.98835 | -56.84126 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a324692-2bc5-37b9-9e48-651f4311de67 | -13.13697 | -57.14787 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 910068be-81b1-328d-89ea-bc7a2c36ae5c | -13.21751 | -50.79056 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03ba52ff-c77d-3b27-9c33-5d8dcab3836d | -13.59405 | -47.74704 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfbfe4c7-fa8c-3889-b3e8-5b1234f5c1d2 | -9.52326 | -60.53699 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61fd03fb-b47e-38a4-920c-18abe8600d25 | -13.13695 | -57.12497 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 678e22d7-dbfc-32f1-ae4f-1e5e470cda4b | -13.01124 | -56.85255 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8943fa70-f616-3dfa-9df4-f24fdc2bec54 | -12.13037 | -47.90232 | 2025-08-18 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fef29603-4bdc-3e85-9b89-8700c9737164 | -13.00209 | -56.84338 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a93a95d-4443-392a-a7e6-70ee6dadc5e4 | -13.14209 | -57.16009 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e76788b-9ee8-3d67-880b-cd816c1de049 | -9.51442 | -60.52788 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd3d84e4-4103-346f-b073-1ba728bf1ccd | -13.00896 | -56.84443 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1246e61-02fa-3a1f-b490-c88a683d5f18 | -14.17665 | -45.30933 | 2025-08-18 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c6d80951-ea8d-3458-b050-1373322e8077 | -13.22145 | -50.78452 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3ae6364c-d877-3082-9134-cb69431451fc | -15.00472 | -54.78389 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c04e676a-5f86-3c49-ae15-bda0f528cd14 | -15.87358 | -50.20601 | 2025-08-18 05:14:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc4ad41b-9be4-32a2-9f93-cfb65e69c4ee | -14.18091 | -45.30753 | 2025-08-18 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README30.md)
