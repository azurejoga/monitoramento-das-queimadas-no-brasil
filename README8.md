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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6acb6a6d-5631-3864-8032-1cdf6a0b6d81 | -1.1179 | -53.372101 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4501e374-5bc3-33d6-ab0f-6cf03a1f3f86 | -4.4034 | -45.6134 | 2024-11-24 00:25:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3046409f-7caa-3d43-8849-7c1199efe9f9 | -1.75 | -54.497101 | 2024-11-24 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e892259-93ea-3f59-b8ea-e92cb05d40ac | -3.9788 | -47.9119 | 2024-11-24 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a154b498-72a7-3066-96bf-7de8a81763c4 | -2.7015 | -46.282101 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce57b707-44d0-355c-9360-d8c4514649d7 | -3.843 | -44.033401 | 2024-11-24 00:25:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 082ea842-3b6d-3bc8-a3ac-d49d29766dc6 | -2.1988 | -50.668098 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90879fb9-e747-3e35-83f7-5f129069be24 | -2.5664 | -46.548302 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b5fc39a-3187-3f18-b572-ea2f61152752 | -3.2445 | -45.547901 | 2024-11-24 00:25:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb138f78-0c35-3025-81fd-5c66377f40ba | -3.9864 | -44.787102 | 2024-11-24 00:25:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74865d14-5adf-3a92-8fcf-444ee4c47df0 | -4.2423 | -48.622398 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7d590e7-802a-31d6-8f20-110004df796e | -2.5928 | -46.257099 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e4f638d-c880-3719-a80c-eae7e38262a9 | -2.0669 | -50.3102 | 2024-11-24 00:25:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ae5d89b-725b-327a-90ff-a115fa575115 | -4.4052 | -45.621498 | 2024-11-24 00:25:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a39049b4-e23d-38f3-b616-574c0aab161d | -4.2561 | -48.6838 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6996bbd-694b-3f13-b585-1c481103f8b5 | -3.0225 | -45.1189 | 2024-11-24 00:25:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bbd6db28-c618-3470-b5ee-ebbd699d274a | -1.774 | -53.594601 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e0a965d-8429-3c8e-95b8-bbf5e7b49336 | -1.2774 | -47.861301 | 2024-11-24 00:25:00 | METOP-B | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a27bd5f-0d01-322a-895c-739bba01b744 | -3.6845 | -47.114201 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce8b7b8e-4b3f-39ec-a5ec-129eaa3a9b4e | -3.5541 | -50.513699 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76e4f9f6-c757-3ef8-8e7d-031343898d06 | -4.537 | -42.904099 | 2024-11-24 00:25:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c00e9be0-a128-33f6-88fa-752cd1f04c7f | -3.8476 | -44.053299 | 2024-11-24 00:25:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 404cfdb2-d99a-31c9-93cc-954bef2c3cd2 | -4.9329 | -50.6054 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b086f33-1763-382a-afd0-c7315a9c327a | -2.8196 | -54.0037 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90671987-7ed9-339a-9ea4-1d2033f45418 | -3.8453 | -44.043301 | 2024-11-24 00:25:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 085b2e3a-03de-3d66-a689-c089ae38bc6b | -2.6997 | -46.2743 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa6ce495-a168-39ad-9d65-164fa03c71b8 | -3.1566 | -45.523701 | 2024-11-24 00:25:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aaf82b35-2884-3eb8-8ebe-f01c115ff90d | -1.614 | -53.292301 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a62ed75-34d7-38d0-8f05-762fdd217629 | -4.0817 | -49.2827 | 2024-11-24 00:25:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3063c4e1-fe00-3dbf-ada9-f7fc5986ab0d | -1.5121 | -54.167599 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28fabbdd-a010-366e-b531-0ad486ba6069 | -2.7131 | -46.2878 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5ef20dd0-b459-3758-af5f-8e0e25a83df9 | -0.0305 | -49.641399 | 2024-11-24 00:25:00 | METOP-B | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 340c9a3c-baab-364a-985a-398ecefab200 | -5.0628 | -43.6992 | 2024-11-24 00:25:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fabe0b5b-1fdf-3feb-9e8c-c14c0ee0d656 | -3.4278 | -49.9953 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a97ac681-c6b1-36ad-bf1c-3e1cc24d0dc6 | -1.1081 | -53.374298 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 378e4f49-435a-3c73-a136-c236fccf65eb | -2.439 | -49.0797 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2834ec4-3c4b-3947-9b82-731dcb4de772 | -1.06 | -51.740799 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2c5308de-7ae4-3d4c-bd71-246061b620b4 | -1.188 | -51.760899 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1269fff4-e384-39da-be12-7abd09a39e79 | -1.2221 | -51.729198 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16350b8f-9720-3d23-8131-941e8d468721 | -3.6829 | -47.106998 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 685e250e-c2c2-3a00-b8a2-0cd14de79b75 | -2.7033 | -46.290001 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a8ad19c3-b24f-320d-af48-63422aac62a0 | -0.8753 | -52.749802 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cc75cd7-eae3-3b8e-b97d-d53c54d03141 | -2.2369 | -49.188801 | 2024-11-24 00:25:00 | METOP-B | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77ffe551-7e04-3878-b9fe-e535b6c6101d | -2.5927 | -45.580101 | 2024-11-24 00:25:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 982e5b39-7ee7-3374-addc-957d8aadd2e3 | -1.9487 | -49.510101 | 2024-11-24 00:25:00 | METOP-B | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d27ba4-d412-3330-93ec-ce0a9dc2547a | -2.5882 | -46.1917 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0199fc29-cc03-33c0-97ea-1451cde19762 | -4.0476 | -48.307301 | 2024-11-24 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf947ce1-de10-348c-aaa2-3a77355d0e7e | -2.6863 | -46.260799 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94675c4a-4995-3b90-949f-e173be8edd38 | -2.9972 | -52.491798 | 2024-11-24 00:25:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3d19e90-6e9b-342f-bab3-239d0d0d2b94 | -3.8332 | -44.035599 | 2024-11-24 00:25:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d144aa4f-60d6-3b13-8ca7-14330c4d1b41 | -2.6575 | -46.134399 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db90b8ed-ba0f-3077-839c-35fd5ac0d8e7 | -4.8537 | -50.804798 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c88e897-a52e-3fad-841e-c03ca03f1bac | -4.0348 | -51.007801 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85128537-0a5b-39e9-90e9-904787920643 | -3.977 | -49.918598 | 2024-11-24 00:25:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a361d64a-1a49-3700-ba4e-a4c77fe1b3ad | -2.9301 | -46.697601 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eccda411-bd31-3b6a-ad74-2bf2cde21826 | -4.4119 | -49.6535 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e218aa6-8d3b-3096-91f7-f1b85797b80b | -3.1534 | -44.479198 | 2024-11-24 00:25:00 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ec90e1a4-e6a9-349b-9a7f-100192266e4d | -4.1768 | -45.6138 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73be4e45-1743-31cf-9872-ddc3160abbae | -1.7684 | -52.696899 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 470aebbc-6ed3-3b65-9e6d-fc42c1d05aa4 | -3.9872 | -47.720901 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eaf2b2b-be31-31ed-baf3-8fc7fcf84515 | -3.9443 | -45.993599 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 55d40df9-56ff-3024-b4a0-8af9df136652 | -0.946 | -51.646301 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0858b8de-b4f9-3b81-9f68-86264af80619 | -2.5375 | -46.376301 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 56b56aa9-221b-3ed8-a7d9-5c08c48d9840 | -4.5999 | -44.722099 | 2024-11-24 00:25:00 | METOP-B | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39f535d4-30bc-3c1e-9f06-7e47bcf904cd | -6.3552 | -47.299301 | 2024-11-24 00:25:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83d39cb9-641e-36b8-a2e1-ec3d4a3f82f1 | -0.8733 | -52.741402 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a06e871f-fdcb-3271-849d-9a4de73cc5f9 | -2.4142 | -49.106602 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddf877c7-a592-36a1-a232-d0b021980706 | -3.6764 | -47.1236 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92f8e296-0cfb-338e-b566-2e7333b866d7 | -1.8426 | -53.6716 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9a55444-3fa8-335c-82dc-037c36723425 | -4.0841 | -50.3517 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce7bef2d-9fd4-3fa1-b82d-a07bd5ed6d8b | -2.4144 | -48.970798 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fe6dc96-bb12-3552-a0ef-59e52b8f4517 | -3.9786 | -49.925598 | 2024-11-24 00:25:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56bf90fa-6b78-34fc-934f-21e888771274 | -0.5699 | -51.713402 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7610dda9-55ba-353a-b64b-34167458ed95 | -1.6845 | -52.643398 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f93186dc-e522-321f-81f8-e8a662176319 | -0.2131 | -51.181499 | 2024-11-24 00:25:00 | METOP-B | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34f4de47-b302-3c5e-bee5-0f5dd02b9aae | -1.5145 | -54.178001 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 259e1fbf-e61e-31fe-8eba-ce6e17acce01 | -4.3147 | -48.075298 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 872af0a3-7fed-3b7b-aecd-351c47428bdc | -0.9213 | -51.627899 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a358a8e1-7279-386e-a82a-968508142a01 | -3.9088 | -50.5811 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1cb0d79-8df9-397a-ba5f-15ea25d0ac5c | 0.4093 | -50.842499 | 2024-11-24 00:25:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 16e29dd2-438f-3e80-8818-c2fb1733c6cc | -1.4436 | -52.4403 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf3043e7-2479-3099-993a-e05d9d587c0e | -3.2528 | -53.690701 | 2024-11-24 00:25:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 916838cf-1ab8-3ae1-9100-3eec805ebc26 | -1.4584 | -55.164799 | 2024-11-24 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43658eaf-2174-34f2-a525-4450ae3c4935 | -4.0873 | -50.366199 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ef660c7-214d-3dac-a64e-56302e7ccc62 | -4.2297 | -44.636299 | 2024-11-24 00:25:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a851ac7-c69d-319d-8762-f4811bb31d96 | -4.1135 | -48.507801 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6df75858-f422-39a8-86c6-b6eaceaa890d | -3.8312 | -45.994499 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36ad69ff-cfc4-3fec-85a4-e79a1b7b0181 | -0.8877 | -51.706902 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7f44c4ed-121a-3b29-a1b4-b057221b12f3 | -3.8355 | -44.045601 | 2024-11-24 00:25:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55794469-b030-3645-adc4-141a9b3a0dc9 | -3.841 | -45.992298 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d656451-c4e6-31fe-8d50-262ee7a9f3c8 | -3.8534 | -50.425098 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47f50876-be9b-317c-83f2-7667f4a109b1 | -4.0857 | -50.358898 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 261725d3-5749-3feb-8996-b51eb0d9aa4b | -4.3687 | -49.7365 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35701edd-8f0a-3e2c-9e70-7ec8354754a2 | -4.2635 | -49.818501 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b32ddf0d-bb84-3c1f-b5ea-6d4388d6add4 | -1.9419 | -49.526001 | 2024-11-24 00:25:00 | METOP-B | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 771c356e-bedb-3dcb-ac5c-e3a6aa9c2b84 | -1.7604 | -52.1558 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 659a0588-3e10-320f-b891-50ef00866d09 | -1.2388 | -54.0019 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8529d95d-c6d6-3662-850a-98cc730542fc | -3.6434 | -50.2225 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49d8ec95-d4c5-3054-866f-4e41bfc94722 | -1.1934 | -51.9221 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6890736-d82c-33bc-9eab-44618a8cc5fb | -4.234 | -48.6315 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
