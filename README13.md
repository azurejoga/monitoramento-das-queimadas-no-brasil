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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a81ba82-b790-359d-9c7e-93860b3ca081 | -3.2938 | -49.094299 | 2024-10-14 00:39:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53e5a689-a885-3cbf-8e61-bd49add7cddd | -3.2955 | -49.102001 | 2024-10-14 00:39:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4580986-edbe-3ab4-99fb-ee022a9d9ca4 | -3.2822 | -49.088699 | 2024-10-14 00:39:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d670a49a-261b-3c34-8bf2-a8d072f03d45 | -3.284 | -49.0965 | 2024-10-14 00:39:12 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb6fef5-d851-37a5-b88a-c36ed2cd19ec | -3.2226 | -48.916901 | 2024-10-14 00:39:12 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfb14472-6175-3ee9-9df0-601bcdc0b289 | -3.2111 | -48.911499 | 2024-10-14 00:39:12 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dd1685c-f295-3990-8dac-257f1e3baa7a | -3.2128 | -48.919102 | 2024-10-14 00:39:12 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 444b7db1-5187-3974-a2bb-c8de55abf903 | -3.2145 | -48.926601 | 2024-10-14 00:39:12 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1926958-8698-3888-b4eb-4ffa25b6451f | -3.4548 | -50.306499 | 2024-10-14 00:39:14 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 346a16fe-5c93-38df-bea4-9120fd5d3171 | -3.357 | -49.918999 | 2024-10-14 00:39:14 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc51530-47d1-30b0-9481-c3d78975680d | -3.3589 | -49.927502 | 2024-10-14 00:39:14 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce711bb2-5f98-350a-b18a-b682eaace9e5 | -3.445 | -50.308601 | 2024-10-14 00:39:14 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f5a8ce9-46f4-307e-bef2-c6f15d69909f | -3.447 | -50.317501 | 2024-10-14 00:39:14 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c66b0b58-92d8-3055-bec1-a522650ea435 | -3.4855 | -50.4884 | 2024-10-14 00:39:14 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73259970-8dbd-3c33-939d-5c04a43b06c6 | -3.3491 | -49.9296 | 2024-10-14 00:39:14 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc017a8a-33be-3bc1-b1ed-bd50194b20ff | -3.4757 | -50.490601 | 2024-10-14 00:39:14 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61f35382-4faa-3637-a37a-86d6478ac432 | -3.4778 | -50.499699 | 2024-10-14 00:39:14 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2290842e-d95e-3bd4-aece-ed67b87ef1d7 | -3.864 | -52.268002 | 2024-10-14 00:39:14 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75a2bc0a-4af5-3cee-9ad7-0adf05a6bc64 | -3.8667 | -52.2798 | 2024-10-14 00:39:14 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b37d6d04-d352-316a-a411-53c51d25a0d6 | -3.8569 | -52.282001 | 2024-10-14 00:39:14 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cb3438d-e962-3262-93e5-bb60ce454ed7 | -3.8596 | -52.2939 | 2024-10-14 00:39:14 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d64dd08-a3db-39d0-bd6a-8f4e634d48df | -2.3997 | -45.949501 | 2024-10-14 00:39:15 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2782eaaa-fb96-34b3-bf9f-1de109bfe04a | -2.426 | -46.1534 | 2024-10-14 00:39:15 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 07a8d70f-a5e5-348c-90dc-6d92b04385b0 | -2.4146 | -46.148701 | 2024-10-14 00:39:15 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5bcf8428-9d0c-3b79-b12a-05030eab4812 | -2.4162 | -46.155602 | 2024-10-14 00:39:15 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b73c6936-b00b-35b5-8fc0-7acd89470044 | -2.4178 | -46.162498 | 2024-10-14 00:39:15 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88e1e751-f3a8-327a-9717-538686d940be | -3.3666 | -50.325802 | 2024-10-14 00:39:15 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 195cdb8b-9f04-371c-aed2-8e0e2e4f8194 | -3.3312 | -50.305698 | 2024-10-14 00:39:16 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caf41089-01a8-3c09-8ba1-fb14f8bd11a1 | -3.3332 | -50.314499 | 2024-10-14 00:39:16 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16418c08-c26d-34c5-8c90-9ce0f83ae3c8 | -3.3214 | -50.307899 | 2024-10-14 00:39:16 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffafdef5-ec8f-3fa6-bf4b-06f126d96bff | -3.3234 | -50.3167 | 2024-10-14 00:39:16 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e09bc709-45ba-31f1-acec-5b78e2cf9721 | -3.0573 | -49.368 | 2024-10-14 00:39:17 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ddd5a4e-47f4-32a3-9bde-3ab746c95e59 | -3.0475 | -49.370201 | 2024-10-14 00:39:17 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b23fc9f-1391-3274-b42f-f6a4a7c18908 | -3.6111 | -52.007099 | 2024-10-14 00:39:17 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb9d9b6c-763f-367f-a043-98cbb3c377af | -2.4449 | -46.909401 | 2024-10-14 00:39:17 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9ca463b-1be2-3ed9-afd7-32c9cf4c8e42 | -2.4465 | -46.916302 | 2024-10-14 00:39:17 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 704968c8-032a-3a63-a621-feb33b3b48a1 | -2.448 | -46.9231 | 2024-10-14 00:39:17 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9f45da0-19d7-3936-99fa-818189f44459 | -2.4496 | -46.929901 | 2024-10-14 00:39:17 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce55976-3aa3-30ff-ba21-2e6adf5186df | -2.4351 | -46.911598 | 2024-10-14 00:39:18 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 293e0243-4fd8-3820-9222-5bfc7d3301b3 | -2.4367 | -46.918499 | 2024-10-14 00:39:18 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03ec19af-4d9e-30c5-b073-49b0680f9f59 | -2.4382 | -46.925301 | 2024-10-14 00:39:18 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 138e7aae-e543-3b78-a7fa-1f2084bf67e7 | -2.8686 | -48.899899 | 2024-10-14 00:39:18 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41f3bdd1-4157-37c8-a54c-44725e03c151 | -2.8704 | -48.907398 | 2024-10-14 00:39:18 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b1255b8-afc0-3b43-9eba-3b73ddc9c13c | -3.1862 | -50.3004 | 2024-10-14 00:39:18 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d890997-8de7-35f3-a895-eb9b9e2601f1 | -3.1882 | -50.309299 | 2024-10-14 00:39:18 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa8facb1-30a1-3bd0-8aed-762746c321d7 | -2.7447 | -48.400799 | 2024-10-14 00:39:18 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87fd3e86-8874-3ca6-bf98-ecf9d9214777 | -2.7463 | -48.408001 | 2024-10-14 00:39:18 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98fb8552-f2f7-337d-b2e8-a45ba64db1ad | -3.4544 | -51.582802 | 2024-10-14 00:39:18 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa0cc01b-94bf-3ad0-9b5f-7c21a11a79ea | -3.4568 | -51.593399 | 2024-10-14 00:39:18 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c16b4b2b-66f6-3f04-bf45-140ce352bbca | -2.4376 | -47.147701 | 2024-10-14 00:39:18 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdc39a74-16af-3269-a4ab-53655a4fbe4a | -2.2307 | -46.290798 | 2024-10-14 00:39:19 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4025f5e9-16e6-3151-9d56-38427759d750 | -2.2322 | -46.2976 | 2024-10-14 00:39:19 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb949cc2-99f9-3fe4-8bbc-fc9ad833cca1 | -2.2338 | -46.304401 | 2024-10-14 00:39:19 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85de419b-40b4-3bcf-a700-ad4737fae316 | -3.1713 | -50.462399 | 2024-10-14 00:39:19 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 295a97a9-6f7a-3c7a-8241-5cb6693d9dad | -3.1615 | -50.4646 | 2024-10-14 00:39:19 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81829923-05de-3d6b-956b-f8c52ce2ffd7 | -3.1636 | -50.473598 | 2024-10-14 00:39:19 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb1406d6-c41c-35eb-973b-f10cf3af54c7 | -2.195 | -46.449699 | 2024-10-14 00:39:20 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 450a51a4-e2d4-34ac-a95a-55c3b938ca67 | -2.1966 | -46.456501 | 2024-10-14 00:39:20 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec346a5c-1729-3107-9287-cba62377d1e8 | -3.3345 | -51.642399 | 2024-10-14 00:39:20 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a28323b-5773-3c38-9413-60b77c3fa678 | -2.2494 | -46.7313 | 2024-10-14 00:39:20 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71bdc5fd-c1b8-35c6-97a8-474703944755 | -2.2396 | -46.733398 | 2024-10-14 00:39:20 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c0f3b51-eb35-342e-aa90-b526d9d97362 | -2.2411 | -46.7402 | 2024-10-14 00:39:20 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43f5bcbd-8925-38da-8880-5ff25de6fb99 | -2.2427 | -46.747002 | 2024-10-14 00:39:20 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd7bc1f0-4ae2-399f-a719-c8661b7eb761 | -2.2443 | -46.753799 | 2024-10-14 00:39:20 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca749e6-71d5-309b-94da-55681aa4437e | -2.2458 | -46.760601 | 2024-10-14 00:39:20 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04c4bf28-c639-35a0-ba87-c8857bbaefe2 | -2.2375 | -46.7696 | 2024-10-14 00:39:20 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2536f147-2f7c-3cbf-a4b7-b4934b1f2b7f | -2.2261 | -46.764999 | 2024-10-14 00:39:20 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18917ab3-94ef-3894-a123-6ed4aa9408f1 | -2.2277 | -46.771801 | 2024-10-14 00:39:20 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c10b940e-6a3f-314b-b968-afcffcef2376 | -3.1954 | -51.024399 | 2024-10-14 00:39:20 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a610d250-4324-32af-af41-b9ff8da75d55 | -2.0764 | -46.2029 | 2024-10-14 00:39:21 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f87c3af2-f8f9-3ca3-b338-61ef6c987a19 | -2.782 | -49.288799 | 2024-10-14 00:39:21 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55cb35fc-c90f-3282-ab39-34623847a776 | -2.7838 | -49.2966 | 2024-10-14 00:39:21 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a4f3514-dd97-31e9-9013-f9d804084f36 | -2.7856 | -49.304401 | 2024-10-14 00:39:21 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 178a7ba9-ac71-3431-a793-f08e817a53cf | -2.3832 | -47.5853 | 2024-10-14 00:39:21 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 938fed21-d6fd-3807-ba00-d54c417ac400 | -2.3848 | -47.592201 | 2024-10-14 00:39:21 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 801d9c90-c4d4-3a2a-990c-764a7669e112 | -2.7811 | -49.4207 | 2024-10-14 00:39:21 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c5b6241-e1c2-39dc-bf2b-9f2853dde459 | -2.4685 | -48.183701 | 2024-10-14 00:39:22 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64d53c02-acff-3aef-9aaf-f5b58505729b | -2.4701 | -48.1908 | 2024-10-14 00:39:22 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c23f12bf-0814-3c69-bcdf-b3d23d0a16e7 | -2.4717 | -48.197899 | 2024-10-14 00:39:22 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 925fe803-3253-3728-b3fc-fe8655d6764a | -2.6216 | -49.081799 | 2024-10-14 00:39:23 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2cb56c-749a-334d-ab25-0510641d83b5 | -2.6101 | -49.076302 | 2024-10-14 00:39:23 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40b4566f-8920-32da-9772-ad38db4e470f | -2.6118 | -49.0839 | 2024-10-14 00:39:23 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d55233c-1031-3d69-b77b-c9d73eabe7cd | -2.6135 | -49.091499 | 2024-10-14 00:39:23 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff505ce-e64f-3504-94b4-37cc91f74dec | -2.617 | -49.106701 | 2024-10-14 00:39:23 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d36fad46-7497-3f42-b062-7c8eaa59461c | -2.6188 | -49.1143 | 2024-10-14 00:39:23 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a79c03f-67d9-3bb9-a535-12d9bd7adf17 | -2.6055 | -49.101299 | 2024-10-14 00:39:23 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e5aa1c4-b143-32a7-b798-71aa7ff93ae4 | -2.6072 | -49.108898 | 2024-10-14 00:39:23 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e74e0214-5379-310f-b288-ae0f8cff0245 | -2.609 | -49.116501 | 2024-10-14 00:39:23 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37704ace-1145-361e-b082-6b4d98503943 | -2.0802 | -46.847801 | 2024-10-14 00:39:23 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c289815f-b09c-360e-80a0-574db19fe905 | -3.4213 | -52.761299 | 2024-10-14 00:39:23 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a15c222-355e-32ff-a511-82f4419248fe | -3.4241 | -52.773899 | 2024-10-14 00:39:23 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 037d118c-2e98-38c0-86d6-6f53c1b16e13 | -2.6387 | -49.5187 | 2024-10-14 00:39:24 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f328312-2e03-3715-8654-d928d84eaaaf | -3.0935 | -53.033798 | 2024-10-14 00:39:29 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec5a619-f2c7-38f8-9595-30a3a69e4745 | -3.0964 | -53.046799 | 2024-10-14 00:39:29 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce9ca8eb-983f-3143-b77d-da9d066a1482 | -3.0808 | -53.0229 | 2024-10-14 00:39:30 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1739619f-db77-3947-a9d1-d92dfe7ed269 | -3.0837 | -53.0359 | 2024-10-14 00:39:30 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ce865b8-1703-3b9f-ae07-ee16c245f997 | -3.0866 | -53.048901 | 2024-10-14 00:39:30 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cdc7f97-c244-30eb-bea4-8bff6306c085 | -1.2889 | -46.321301 | 2024-10-14 00:39:34 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 836d9977-7c89-3136-86a1-4540bb434b56 | -1.2905 | -46.328201 | 2024-10-14 00:39:34 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0577eebd-7fc0-36a4-9239-0815c17ef64b | -2.5692 | -51.843201 | 2024-10-14 00:39:34 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
