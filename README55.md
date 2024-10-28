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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70e0214d-a2c5-33b2-8d4b-8e7f3874115f | -3.49665 | -49.93883 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99e82a9b-e1c9-3041-a963-3d69c9cffb87 | -3.47004 | -49.27536 | 2024-10-28 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaf44b2d-7438-3aaa-9a24-40d7daf136ca | -3.36514 | -49.53111 | 2024-10-28 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a767473-db20-3098-911b-cf6a9e81276b | -3.36444 | -49.53565 | 2024-10-28 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dcf2e9a-41d3-3aa5-a657-c21ecf1782a1 | -3.33427 | -49.92048 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52292d86-969a-319c-a274-fc206302848a | -3.33361 | -49.92482 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f21779cb-46c1-37ed-8e63-d981d551b5b1 | -3.33059 | -49.91993 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8ad7828a-bfb3-3ca1-8fe4-2fcb0f85681f | -3.32738 | -49.92063 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 929709a9-0e71-353a-a8cf-c1aee4d6c261 | -3.32691 | -49.91936 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 496fb467-22bc-3145-8be7-0443337dc3fc | -3.32626 | -49.9237 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0af7d45f-61bd-304e-a63e-6035631b54db | -3.30636 | -49.46148 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 375c85ac-2078-3857-a3ab-2157f16d8b25 | -3.26209 | -49.49467 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffeb19af-1400-3067-b594-5b1f68b04a47 | -3.25833 | -49.49409 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ee626ce-1f21-3de3-b3e8-a8dbd81e213c | -3.25762 | -49.49866 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| beafe39b-3d0a-3a01-8aa9-b1f19e54a1ab | -3.60475 | -49.36039 | 2024-10-28 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db560796-1d88-3e72-9b43-b6be5d597462 | -3.60094 | -49.3598 | 2024-10-28 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f99e8f82-18d9-37cd-a8ac-d69c4930c870 | -2.93563 | -49.54823 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5708d830-606d-3d78-a98e-8515f749aae8 | -2.93457 | -50.27507 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb0ea6c9-ded6-37e3-8d4b-9d51ae4ed33e | -2.93189 | -49.54768 | 2024-10-28 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f438e068-338d-36c0-b6aa-59e35fa687de | -2.93119 | -49.55216 | 2024-10-28 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 91d9c515-060a-3534-bc79-da3194a375bd | -2.93098 | -50.27454 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5db8c03b-117a-3799-963e-a6b70acfceaa | -2.92674 | -50.27808 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7509b4e4-8d15-30a2-acfe-f6701608ea0c | -2.92315 | -50.27754 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e37032b3-a0c2-399b-b28f-f83d92f9431c | -2.91956 | -50.277 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36b5433b-b3e8-3875-aad1-bd7e71c179e8 | -2.91892 | -50.28109 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66284494-0c2f-3096-bbb9-11207ff3f958 | -2.91829 | -50.28518 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef1cb93d-80c4-3a21-b93a-fb164c758de0 | -2.91597 | -50.27644 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3f4e5b2-b60f-32ba-93ae-086f2b62393b | -2.91533 | -50.28055 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cdbdb928-142a-37c9-a4a3-e5ab813c2dec | -2.9147 | -50.28464 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8ddbf6e-7771-32de-9ba4-cb8185bb9a6d | -2.91406 | -50.28873 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b3b3c21-182e-337e-82f7-d5bc773d20c7 | -2.91343 | -50.29281 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 634ca7ff-7e2b-3874-aa5e-c8917044c6c7 | -2.91174 | -50.28 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59fd7191-af54-3029-9eaf-ff0ede5027fd | -2.91111 | -50.2841 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b847bec1-5d94-3c5c-bfea-76dab6446e01 | -2.91047 | -50.2882 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ad50977-5253-388b-9452-40ddf0bba5fc | -2.90343 | -50.40418 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26e6a872-5b79-3f5c-90b9-23e0e55569f7 | -2.90278 | -50.47839 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 981ddbce-d792-3ac0-9330-a4838f5c3b22 | -2.90049 | -50.39956 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24d89ef5-8bf0-39e0-9ad5-eb520677273c | -2.88707 | -50.43895 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc7055db-e55d-3fa9-bdac-f61d664af0ad | -2.88507 | -49.50362 | 2024-10-28 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 678fed64-df6b-38a3-8f68-f361ab43de3f | -2.88133 | -49.50304 | 2024-10-28 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1498987-447e-3646-a995-43266ad395f8 | -2.86636 | -49.44986 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b6447ca-8730-3532-b1a0-8ed6af02af4b | -2.8626 | -49.44928 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e67bb8ae-314c-3915-86c6-0ec0e9c0cce2 | -2.85985 | -49.36484 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c3e2015-8d36-354b-9cc6-8ab74556e64a | -2.85965 | -49.36282 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37ffa509-b816-35ba-bc70-7aa6d3378ce5 | -2.85885 | -49.4487 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ffe02d91-d4b3-37a7-951f-bafa6fe6e7d1 | -2.85817 | -49.45322 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 630b667a-fd88-3c22-af2e-f03e72b0c986 | -2.85749 | -49.45773 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf3aa70f-6546-334f-81b5-15dcdd4d7fd7 | -2.85681 | -49.46225 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e179725f-f7d0-3619-92ac-e0f2342676e5 | -2.85656 | -50.47137 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea8da6b0-c4d3-3621-af31-1ba2daed5b68 | -2.85595 | -50.47535 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd81c20e-93f7-337a-b9e1-cdb548e1b662 | -2.85508 | -49.39677 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d198f9b2-6fcf-3ca9-b14d-16e3f1274a2e | -2.84997 | -49.37539 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c813e49a-8789-38a5-8e17-321d1b213f8c | -2.83979 | -49.70128 | 2024-10-28 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7644526b-065c-3b69-8fa7-677062d1fa28 | -2.8309 | -49.34893 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb9738ca-6ecb-3ee1-84e4-ad4a952871ab | -2.83067 | -49.40035 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddc0cce1-595a-3805-9b5e-848b0d6565c4 | -3.50741 | -50.52733 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86136cd7-c291-34b7-bff6-d8ac47c1aea2 | -3.49473 | -50.3702 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a47d6e56-4cc7-3f56-8eb8-12a47479578a | -3.4941 | -50.37436 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c014ef32-4f2a-39ec-b179-375f7df22475 | -3.46824 | -50.61649 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb589c1c-0f09-3507-a94f-c7bb8f536870 | -3.45162 | -50.08599 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88974fdd-214c-3ad1-b466-12ca1eff0579 | -3.44797 | -50.08544 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0cf262c-7576-3a86-8e32-79b3519417e9 | -3.44367 | -50.08916 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8961d5ad-4214-326d-a8f7-b397cdf97918 | -3.44302 | -50.09345 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73f88722-bab5-30fb-9ba4-11caf6fcd115 | -3.44003 | -50.08857 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 672c94c4-47ee-32a2-a915-bc8bd54c3412 | -3.43794 | -50.32065 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4f7de64-167a-3eb3-b6ec-8d25aa7f5af1 | -3.43433 | -50.32012 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78f0b785-59ab-3e73-9788-9784b215dd0d | -3.43372 | -50.25182 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3ce5be3d-10ed-3960-9887-2d29ca302f13 | -3.42204 | -50.35215 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d8557a0-bd4a-3d80-b04e-e0f946fcbacf | -3.40867 | -50.29486 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fac11d31-360c-30a8-a4c0-5a9793e4cb55 | -3.40506 | -50.29431 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc6060fb-29af-362b-9057-b57bde439f78 | -3.40145 | -50.29375 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e0adcee-b434-312c-80b3-6f367e16c335 | -3.37498 | -50.39548 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 892ecb1c-88ed-3fcb-a221-d728108b7086 | -3.37286 | -50.55374 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 679abaa1-8116-34bc-8442-0ed0144e396e | -3.3714 | -50.39492 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49f14ff5-bf15-3ede-81fc-2b6596bed8b8 | -3.33822 | -50.09225 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f523631-d9d0-38bd-a011-c5bcfd082c42 | -3.33433 | -50.11775 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b4bc780-7b97-3276-b860-4e53187f5a2c | -3.33092 | -50.09121 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2eca83fc-d8f6-3114-b03c-30a3b48e7ff9 | -3.31998 | -50.23606 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31517657-716a-304a-bcac-ae48c729a941 | -3.31934 | -50.24026 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bbbdc52-129b-364c-beae-23fcd28a1370 | -3.31637 | -50.23551 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5467481-0224-3298-8efe-f286e8d2ccc7 | -3.29448 | -50.08562 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a1cb061-1774-3cb4-bb87-b73283d8a416 | -3.29396 | -50.08659 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0c6e06b-c3b0-316b-9672-e5b25bfbad51 | -3.27037 | -50.02192 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52b5b65a-8636-3cd1-8479-f1c380051558 | -3.26972 | -50.02619 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26c57d3c-0233-3aef-b2b5-df710fac948e | -3.25661 | -50.36215 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b56b89d4-9c81-3d87-9a2a-bd7fe0b48f7f | -3.25453 | -50.3626 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ee68bc5-8778-3997-bdcc-7fcf730febe9 | -3.25302 | -50.3616 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0feffee-d60f-3637-a3e1-db25855a415f | -3.25159 | -50.35794 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9adb882e-ae01-3ac5-af32-ebff66b52cea | -3.25094 | -50.36205 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fa1fda7-93a1-3109-8f76-baac1e4369db | -3.23342 | -50.1894 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d874d6c1-56ce-333f-8709-838d6b30a79a | -3.22449 | -50.17518 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28a603ba-ecc7-31e6-bf69-ca0638b13758 | -3.22385 | -50.17936 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a91629dc-4f37-3b34-a666-17b8e0c1549e | -3.22086 | -50.17464 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c12d9a63-1d75-39c1-a73a-9a6f813ae4bf | -3.22022 | -50.17883 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 320625a6-d9bc-302d-bb00-f46fec596116 | -3.21788 | -50.16989 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d31c0cdb-4472-3677-b374-779d4b27fa53 | -3.21724 | -50.17408 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edb2a721-810d-31de-b9fe-0504a5daf440 | -3.2149 | -50.16512 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3bc7169-0b3b-357c-84af-e8760619da33 | -3.21426 | -50.16933 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 031a0194-af1d-3a74-a0b3-2ec08322af2a | -3.21022 | -50.22001 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 952728e5-4625-3a2b-9a6a-9aafc5f05585 | -3.20938 | -50.24973 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README56.md)
