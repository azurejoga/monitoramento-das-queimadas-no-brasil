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
| 92ea987f-b2ea-35d8-a452-794924ce878a | -4.46281 | -44.64887 | 2025-11-09 05:44:00 | AQUA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 7eb67dd2-360a-318a-934e-46daaf16bdcb | -3.32363 | -44.36543 | 2025-11-09 05:44:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eb1f61d0-baf5-3c0b-8bc4-a15f17a731ed | -4.63326 | -46.38306 | 2025-11-09 05:44:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 71532e78-a0d9-3626-820d-8c568221b98c | -5.27588 | -44.95615 | 2025-11-09 05:44:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7cfd69fe-8bd9-3fe6-b3e7-b23504a8e17e | -2.91987 | -39.99499 | 2025-11-09 05:44:00 | AQUA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| d7def5e3-afed-3db2-94b1-e168f910b295 | -4.83807 | -42.8525 | 2025-11-09 05:44:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f92f1c4f-cb2b-3abe-bf65-a3a2d4a5793e | -4.05092 | -46.42205 | 2025-11-09 05:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 211eec58-5dec-3565-a8cb-4e1005404ff0 | -3.31811 | -50.09392 | 2025-11-09 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| f23bd54b-082f-3347-b861-014a06e69e59 | -3.59872 | -42.80541 | 2025-11-09 05:44:00 | AQUA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 687bc5ad-3fd4-3bb8-8c33-fedd470446d3 | -2.94529 | -49.33701 | 2025-11-09 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| fc133a78-8dea-331e-b613-979626484624 | -4.57897 | -45.61966 | 2025-11-09 05:44:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3c56d1e4-cc84-31fd-8f00-7da0309c2dee | -5.2775 | -44.94556 | 2025-11-09 05:44:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f2b8e89e-76fd-3845-badf-7eb575e77b66 | -4.3935 | -45.96472 | 2025-11-09 05:44:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9d94fd04-71a1-3dce-9dd6-ff3fa870527a | -2.60434 | -49.21443 | 2025-11-09 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| d22a5e42-8f65-35f6-92fb-de2845d469bc | -3.58689 | -41.66132 | 2025-11-09 05:44:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b8f80ae8-2411-31e2-bc42-5d4808f6810c | -2.61194 | -49.21065 | 2025-11-09 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| cd6b3c97-1483-3783-9baf-813043a4b9fc | -3.98018 | -45.44931 | 2025-11-09 05:44:00 | AQUA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9020801f-a7e1-3782-93d5-c74fe84371a0 | -3.20183 | -44.30899 | 2025-11-09 05:44:00 | AQUA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 2f6cb5fc-33a2-32b0-b3de-e6cf46258c5f | -3.59698 | -41.65386 | 2025-11-09 05:44:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 9c6a2781-cba7-3d19-9c68-08d844ac3e17 | -2.93728 | -49.34074 | 2025-11-09 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 510a47f4-0c7e-3a82-b7c7-a39b864c9e05 | -3.10062 | -50.30677 | 2025-11-09 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| c6a31e46-232d-3c4b-b757-2c435c1b2bcd | -4.63117 | -46.39628 | 2025-11-09 05:44:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| df8a8098-0ead-3149-95e7-eeca377d4db0 | -4.4644 | -44.63857 | 2025-11-09 05:44:00 | AQUA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 6b70e891-8e8a-3f79-9aea-73eeb88dfa90 | -4.7619 | -38.67443 | 2025-11-09 05:44:00 | AQUA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 3ef816e9-dd76-32c3-923b-60b6b421fa4a | -4.45491 | -44.6371 | 2025-11-09 05:44:00 | AQUA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1a9f25ef-36b9-3ec1-8ab8-baa4524ee0b9 | -12.11273 | -43.64561 | 2025-11-09 05:46:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4e628b55-3298-396b-9f1c-16239bcede28 | -7.55918 | -45.87516 | 2025-11-09 05:46:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6f212d14-9ace-3c9d-b5e9-5644681437a5 | -12.11407 | -43.63668 | 2025-11-09 05:46:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5a71a6e-65db-334e-b677-cc78225a675a | -7.18022 | -44.94744 | 2025-11-09 05:46:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aa69203c-1c03-3f32-a2de-160a738275b7 | -7.9214 | -43.30649 | 2025-11-09 05:46:00 | AQUA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b7fc468c-6600-35ce-a9fa-31abab2a19dd | -6.02058 | -43.76875 | 2025-11-09 05:46:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b7512a4a-c706-38b2-b1a5-88144c67f65b | -10.34089 | -49.61766 | 2025-11-09 05:46:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 73eb3294-c5fb-30be-a953-3997b7a65931 | -10.34139 | -49.62495 | 2025-11-09 05:46:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f664fca3-5df5-3e68-b4cb-92af6bdba707 | -4.0011 | -45.438 | 2025-11-09 05:50:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| fea114dc-f415-3d51-bd41-29f2f74ec66a | -3.9822 | -45.4838 | 2025-11-09 05:50:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 96.2 |
| f1f34ada-663f-3623-85c7-a28f8be6a98a | -3.9824 | -45.4614 | 2025-11-09 05:50:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 575.0 |
| c0a035e7-e17b-3970-a2b5-b2c29e4e379f | -3.9825 | -45.4389 | 2025-11-09 05:50:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 227.4 |
| 17fef095-2608-31ef-a344-e4eaa2877b0d | -4.001 | -45.4604 | 2025-11-09 05:50:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 197.7 |
| b669b765-af3e-32f6-ba0f-44b8f2dff81e | 4.22407 | -59.9416 | 2025-11-09 05:57:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1dc1402-e223-3fc7-82b7-8405f8dfb508 | 4.22435 | -59.94278 | 2025-11-09 05:57:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7669e858-102c-3f52-acba-cd16125fc8cb | -1.72582 | -54.67992 | 2025-11-09 05:57:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1135261b-c288-3e20-a1fc-586f1e9ede32 | -6.05127 | -58.05198 | 2025-11-09 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a6209bb-e1b1-3bc3-8cf0-3ece89d0c76b | -12.09654 | -63.88832 | 2025-11-09 05:59:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3795136d-655d-3fce-84a2-212381c20192 | -5.09276 | -56.16172 | 2025-11-09 05:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 672b2381-9b29-3815-a56f-eccb0a9e696e | -6.04518 | -58.05146 | 2025-11-09 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81a75728-09f6-388c-9bb9-55a057f5463b | -6.0507 | -58.05594 | 2025-11-09 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60251727-ff90-3236-b32f-cefb7269ed54 | -5.09924 | -56.16261 | 2025-11-09 05:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| babcccac-a5a1-3919-880c-f65522566cf9 | -6.05048 | -58.05603 | 2025-11-09 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e98ae7d-aefa-396a-82b1-2abe1cca2ab2 | -6.04542 | -58.05139 | 2025-11-09 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb6d8615-dd16-37bb-8d2c-97c99c0c2b0f | -2.71453 | -60.01395 | 2025-11-09 05:59:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2cd6f06-0f57-3fe5-b869-74f2cf50fdc2 | -6.05103 | -58.05206 | 2025-11-09 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef86b060-096b-3ba3-a439-9428fdb0d7e2 | -3.9824 | -45.4614 | 2025-11-09 06:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 256.4 |
| cae0a037-a58f-31ff-96ed-c09cc8e62827 | -3.9822 | -45.4838 | 2025-11-09 06:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7a1a54fa-832b-361c-8537-eee3d72b1542 | -4.0011 | -45.438 | 2025-11-09 06:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| be86c9ec-38e9-3fc5-a3fe-ed9e2dfac62d | -3.9825 | -45.4389 | 2025-11-09 06:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 98.5 |
| cbaac130-5f45-3bc6-a69b-b93e0f047300 | -4.001 | -45.4604 | 2025-11-09 06:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 849b6486-462b-3f69-856a-fa5d39fc86db | -19.73713 | -58.0994 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 75fa6674-2335-3b68-af0e-5e0c7aa6da94 | -7.9882 | -70.93262 | 2025-11-09 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 80b0b836-7730-3ad4-8b6d-a68c22102b66 | -19.72198 | -58.09868 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0180556f-e54c-34fa-b8cd-b2f86df7d234 | -19.78309 | -58.0439 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 32bf88a2-dd4d-3cda-880c-56efff08d0b7 | -19.76554 | -58.08914 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d2f07277-f9df-3763-b6f8-5984c45fb851 | -19.7556 | -58.04253 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 1008265f-0c17-3754-a2f5-cf4832ce3bfe | -19.78987 | -58.04583 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 19cdedbd-9a12-337b-aeac-0873b5264a34 | -9.62599 | -68.59934 | 2025-11-09 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb6e12ac-4a4d-37c4-b670-31acca8f9b89 | -19.73766 | -58.09295 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c00dc875-3f18-3e09-ba0d-bdcbddccb1a0 | -19.73661 | -58.10584 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 18db64ef-d9d9-3c73-978b-872d7623cf43 | -19.76245 | -58.04319 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a2fb7305-7233-3240-8515-53f5ed4452a7 | -19.71612 | -58.10383 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 467237ff-8c2f-3f88-a16e-90079626157f | -19.74237 | -58.11937 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| a2e435e8-7cf3-3b4a-b3e7-d4a624c51e24 | -19.76931 | -58.04385 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3e60307d-2bda-3357-9b94-093d40304fcb | -19.75186 | -58.08781 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 86a0e1a9-6645-3077-ae73-48fa80d4ff90 | -19.72142 | -58.10512 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 558018c6-9e66-3428-b69e-5b98fcc1a939 | -19.7587 | -58.08848 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fd486eeb-c0b5-335a-9699-a47f2da46c56 | -19.76392 | -58.10847 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 19b2fea5-3df7-3026-8db7-26154ed7e4ce | -9.75923 | -67.32982 | 2025-11-09 06:01:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a12a5a1c-50de-3ccc-bd04-b2086b1e12ac | -19.71459 | -58.10449 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 025ff2b7-48e7-34eb-9ca7-d8463e54aa90 | -9.75941 | -66.87235 | 2025-11-09 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a91cf3d-a3b5-38bf-81e8-59bec24eeb40 | -19.76285 | -58.12135 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 0fe8cda1-269f-35b5-86af-917e8c13ac5e | -19.72881 | -58.09933 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 14bcc095-e329-3cc6-a34c-b2c90304aa0d | -19.78943 | -58.0511 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1ee48d49-b872-3f5c-a4c2-9238d6da0d4d | -19.74973 | -58.11361 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ac78c984-8a8f-345c-b421-e1274f8416c3 | -19.75133 | -58.09426 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 15480142-d141-341a-aa6f-3ceb2f549378 | -19.77075 | -58.10914 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a94b1e27-fc53-3174-bd1e-18a6dd4aab8d | -19.7156 | -58.11026 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b3223054-2719-34b7-bed2-dfec91c2a1f8 | -19.72086 | -58.11154 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2379619e-f4b3-3f6b-82e3-110173a9eb9b | -19.72925 | -58.1116 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5b0dafcb-370e-33e1-a73d-03b6d9a9de4e | -19.7492 | -58.12003 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 7f659a23-c60f-3253-ae36-e2feeb09c427 | -19.7429 | -58.11294 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 27f08a1e-96ef-348c-b96d-4ddf2b77e4fd | -19.7445 | -58.0936 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b9bd53a2-fc6b-3033-bf3b-fa8cce122fb1 | -19.78994 | -58.04459 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c03a9b78-2f75-386d-b9ec-86a798ef4714 | -19.72768 | -58.11218 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d03bedee-e810-38f8-8966-6c19ea4b67ef | -19.72347 | -58.09806 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 64af03a9-98b4-30da-bfaa-ecc95830b223 | -19.72295 | -58.1045 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1e9fada3-a4c4-38ac-a3b3-f45366c401c9 | -19.75656 | -58.11425 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 9119eb1c-1a99-3711-8764-b2e54201ee6e | -19.78302 | -58.04517 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 52807d8a-196b-3725-9c8a-74470b8ae0af | -10.07866 | -66.92699 | 2025-11-09 06:01:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddb29f6b-700e-3085-b124-8ad46929295e | -19.77616 | -58.04451 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1370d97c-d057-3238-abb6-1128d49a0e75 | -19.78258 | -58.05042 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e2f36b38-adaf-3235-ab27-c63ee7d194d5 | -19.76338 | -58.11492 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 74b10003-73be-3a77-9003-e968c6304af7 | -19.7303 | -58.09873 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README37.md)
