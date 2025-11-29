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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 816a023f-6baf-3587-964b-e78c9f5b75a9 | -2.43954 | -47.07051 | 2025-11-29 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdc743cc-4826-39d7-a52e-63d22c2dd193 | -4.38354 | -43.83014 | 2025-11-29 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00d27825-8ee9-39be-a8ba-e01ae65b65eb | -5.36453 | -43.03125 | 2025-11-29 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4ffe9454-a373-3e8c-9ebe-b8b343fa88ff | -2.63412 | -48.54546 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a486ac31-5e97-3988-a38f-ea747b81e209 | -4.16743 | -43.75081 | 2025-11-29 04:42:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58c09630-9603-3c18-8585-713c5264fe2e | -2.64654 | -48.03791 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3f6c4ab-4593-330b-abdf-17f1003dbe6a | -1.68836 | -53.65934 | 2025-11-29 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d33efa5-89e3-3d08-8d73-b8d5abfc4926 | -3.20624 | -48.92913 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9becdf25-d947-38d8-b776-f94e01434100 | -2.53986 | -45.38685 | 2025-11-29 04:42:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5f94ea71-2a39-3fc6-bd43-7690e204bbf7 | -2.23496 | -51.56811 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 51bcad18-18d5-323f-829c-e9aa56f752d7 | -3.30139 | -50.21077 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4009af56-3738-3723-bbd3-aa6033cfd62c | -2.4721 | -50.24107 | 2025-11-29 04:42:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cd6a00a-aabd-3ea3-a35d-2a5890a1368f | -3.28322 | -50.25958 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2eaef73d-8831-3fe9-b89d-c79de944c5a2 | -2.78682 | -47.43153 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9502a62-56d9-357d-87d4-c0a457140d3c | -2.64485 | -48.02699 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dbdaa2a-de40-31d8-a4bc-8955947035f5 | -3.66626 | -43.56097 | 2025-11-29 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 369a39ee-c7a6-36cd-8bc4-e2327087db44 | -3.22538 | -50.31705 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb67cbfb-795b-3c76-be16-654cf76b4c48 | -3.72941 | -43.00161 | 2025-11-29 04:42:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d910160-6401-3cb6-9dd3-c8ea58497e51 | -6.78246 | -41.71033 | 2025-11-29 04:42:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a620568e-257f-3155-b381-2d6f4f360ac6 | -2.74314 | -49.33105 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 696dba92-e5ff-3d91-b5cc-a9455d64f330 | -2.2475 | -48.31538 | 2025-11-29 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a51fe61-203c-320f-a8f2-fb99d4cdb3c8 | -1.68955 | -53.65211 | 2025-11-29 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e4cca0a-653e-3c26-9625-674f3f577ee2 | -2.30032 | -47.98032 | 2025-11-29 04:42:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33e4b0b4-303e-3a67-900b-126afa0a9653 | -2.63744 | -48.54597 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 05c566d7-e8e5-3d91-b4e8-7914253995b7 | -2.55278 | -48.39506 | 2025-11-29 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d398336-7eb2-3d75-bac4-e6e5d953a7e1 | -3.07661 | -50.35014 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 949ab70b-1e3e-39e9-89e6-b396d230423d | -2.46986 | -50.23325 | 2025-11-29 04:42:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2de5ae98-c726-32c6-ba2f-0e1e5cb9289b | -2.93713 | -53.2752 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70ee572d-b237-3373-8283-463a6f775877 | -6.71542 | -40.81031 | 2025-11-29 04:42:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 06126fc8-6756-3d47-9ca4-02257545fd49 | -3.23036 | -50.19955 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27ec6a82-26c1-3f40-ad53-a3d3e181226f | -3.2248 | -50.32067 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48ca3326-9424-37c1-a84f-cbbcbd51dcf6 | -6.46601 | -41.72723 | 2025-11-29 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0cf6c876-a1c3-3438-bc36-5aa539e2efa3 | -1.35611 | -53.0999 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd5a0f72-8e01-3df4-ba23-86a203ebf2ce | -3.17016 | -45.23788 | 2025-11-29 04:42:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 646371a5-f123-3e3f-90df-a615f62c3114 | -4.62864 | -43.99159 | 2025-11-29 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df9eaab4-ce07-39d0-896b-85b2fb6f4d36 | -5.07234 | -40.82432 | 2025-11-29 04:42:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3a847345-bdc4-3ca2-9303-37adc4341e3b | -2.78514 | -47.42036 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6718023-2c9d-3a7a-bb8f-e016b96c3cf9 | -4.05355 | -49.5022 | 2025-11-29 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca668bd2-49cc-38a6-a67d-9d0f56b47b28 | -3.38494 | -50.25666 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c831637a-170d-3baf-be2c-324cd8a60b0e | -3.84174 | -44.12777 | 2025-11-29 04:42:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 649cd3e5-9c86-3aa7-b3a6-ec6b936e595c | -3.61475 | -50.3705 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8122f596-13da-3517-8320-2db700bdaf3a | -4.17043 | -43.75872 | 2025-11-29 04:42:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 202c2a22-a6ed-3721-bb23-01ce92a0277d | -3.40848 | -53.30892 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 364ede92-5c3f-3392-b8d1-6f47be1d74e4 | -2.63798 | -48.54253 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07a6a9d5-8f78-32f6-a958-20e081cdd3ac | -4.85945 | -50.82599 | 2025-11-29 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d4ad4e7-1eb5-3d13-804f-2a14b2ea90bb | -1.48408 | -45.79325 | 2025-11-29 04:42:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1f095e9e-0f6c-37b4-b3db-35f62fc81a07 | -2.78233 | -47.41628 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a2c6161-2dd6-3e79-b59b-dd2f0c3efe68 | -2.63989 | -48.03688 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19d28fc8-8254-3d91-9f4b-8a9d8e83145e | -3.90138 | -46.33817 | 2025-11-29 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7057a713-84d8-3f37-a7a1-5232c1f46a17 | -3.21085 | -46.82034 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14285456-6243-3405-ba6b-d3e4f7c63d9c | -4.85059 | -38.74257 | 2025-11-29 04:42:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3b33f8f-4d90-38f5-82ef-b9232602d057 | -3.86373 | -54.35392 | 2025-11-29 04:42:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e1441f3-29b3-3935-b4cc-c4ef633324a0 | -3.1784 | -45.62014 | 2025-11-29 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b52e1d0b-0fe5-3dea-ba6a-d5b798690016 | -3.31822 | -50.2831 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73fa6ab3-8b88-35ed-b57c-35a9f66a2ab5 | -2.42554 | -50.29346 | 2025-11-29 04:42:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb201251-8c84-3f5f-96f4-47592209d33a | -6.69685 | -41.45932 | 2025-11-29 04:42:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| dd2d4bbc-9100-3ded-8e38-4ec7e75ca165 | -4.22552 | -46.50124 | 2025-11-29 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4eee6ea-7630-3094-968d-81f6cf5c7a11 | -3.08254 | -45.27507 | 2025-11-29 04:42:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 324a2d3d-8419-390c-9707-67a8908680a6 | -3.17424 | -45.62039 | 2025-11-29 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| febf3102-8351-365e-a93a-8b6e1812e2f0 | -2.46408 | -48.22946 | 2025-11-29 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5682ff55-1406-31de-866b-faab643b442b | -3.32292 | -53.31765 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3ba6bac-375e-31a1-a1fe-54803a8f9e90 | -4.20229 | -48.90205 | 2025-11-29 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e09e826-a01f-38e2-aaf9-3cf5110b5806 | -3.83969 | -44.13039 | 2025-11-29 04:42:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aaa4aed3-7494-381b-9a5b-b05fa3c607e4 | -3.17245 | -50.16486 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8129e547-c224-3d24-ab52-5e0cae47dcbe | -3.31541 | -50.27896 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b858daa-8865-39cc-985c-8057a99f1850 | -1.35868 | -53.09876 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be873c0e-e208-3220-8782-968b447601f4 | -2.27209 | -53.64874 | 2025-11-29 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b055247-5dd3-3083-9fd4-4b66704cbce8 | -3.43964 | -45.4197 | 2025-11-29 04:42:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1d1b924-fb59-35fb-b279-206fa422fd24 | -3.95302 | -44.76342 | 2025-11-29 04:42:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a619463-81f3-34ff-957a-39d54ec97a0d | -2.96011 | -50.99624 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c91fd67e-a189-3a89-9591-7c9f1dfb27d5 | -3.21028 | -46.82405 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cfbb05c9-7e2d-3d89-8a46-d6958bd32ad9 | -2.91112 | -53.06669 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 61b9172b-be45-3361-a5aa-c7a1c60b35e1 | -3.14154 | -40.18018 | 2025-11-29 04:42:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 018afc2b-2529-3080-9b8e-658a1f1746f8 | -1.75938 | -54.78315 | 2025-11-29 04:42:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e1b718a-2821-3d2e-9207-bcc1ea69b3b9 | -3.00334 | -45.42438 | 2025-11-29 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4748c281-5692-33a9-8ecf-ef759493f1db | -3.84098 | -44.13289 | 2025-11-29 04:42:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c38cd4f8-0c56-34a5-b423-edcdaa0629d1 | -2.42895 | -50.29399 | 2025-11-29 04:42:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fa5f12e-c74b-36b8-a114-96b7100a2a97 | -2.73142 | -45.25693 | 2025-11-29 04:42:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1ed6899-be3f-3297-947c-9249dc63138a | -3.1135 | -49.21533 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 477fc7b7-1611-3259-bdc1-af4bb44b376b | -2.75368 | -49.32914 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7ba8ec3-7cc4-39f3-9d20-4279966883ad | -2.74457 | -51.90631 | 2025-11-29 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40563b96-2d70-360b-84ff-43bf77fe878e | -4.20284 | -48.8986 | 2025-11-29 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e66ffc76-8eee-34f7-9a99-790d811613ed | -2.6454 | -48.02353 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f2168c4-9aca-3b2e-8dba-f324c5ed964b | -8.16965 | -43.1911 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5d5d310c-42cc-3ee3-bbef-fcb44ee79efd | -7.61224 | -47.02115 | 2025-11-29 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95fb9437-f339-3d42-8807-59ab019c1e7b | -8.02901 | -43.13625 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7773c36e-d7b1-357d-884b-99cd76ce0c22 | -8.16495 | -43.20163 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 62a2e3ce-a1b5-30b6-8dfb-b57782605222 | -9.28923 | -43.15187 | 2025-11-29 04:44:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 073ba3f9-464f-3255-8c79-29d10f683105 | -9.32155 | -43.08829 | 2025-11-29 04:44:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 96d0b261-bd67-38dc-b275-aa53004f319b | -8.03485 | -43.12777 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 8680488f-26ae-3ec8-ad85-9d59dff56bc1 | -11.64855 | -49.96125 | 2025-11-29 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d374e9b-a9de-38bf-88fc-fc20307a3784 | -7.32108 | -42.56854 | 2025-11-29 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f25e47fe-959b-3f74-96ae-5131c301b790 | -8.16681 | -43.188 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 72ce15f5-9270-3dc8-8e2e-6ad2929ab32b | -9.95988 | -42.33055 | 2025-11-29 04:44:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f09742c1-51d5-3f27-b004-4e21ddc7f315 | -8.16946 | -43.2023 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 0ae391e0-a2d5-3b9c-8ddb-0ee495470fcc | -8.17285 | -43.20083 | 2025-11-29 04:44:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 627da46d-b6fc-38a7-9818-360cdbdbb1a5 | -6.73692 | -46.29529 | 2025-11-29 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a1756ed-716e-3c8c-8e32-949bbcff1773 | -7.45727 | -44.74581 | 2025-11-29 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48cad10e-86a5-3138-b6b1-3f0f2cbd728b | -7.45274 | -44.74865 | 2025-11-29 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e31f2112-c2b2-329f-adc2-fd0a386ce91b | -7.61177 | -47.01982 | 2025-11-29 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README24.md)
