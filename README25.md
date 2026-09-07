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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a200c1e-4c47-3465-bb85-9d621019735c | -5.8916 | -45.54573 | 2026-09-07 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1091e8d2-24a4-37a2-b311-52a11fa3cc21 | -13.31373 | -45.23516 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 2bf31dde-f8d4-3483-bcce-73acbb59626e | -11.33277 | -45.09226 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ca68732-af94-3b01-a1a2-6fbe8f163b66 | -11.03648 | -44.33984 | 2026-09-07 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7bb07a49-442e-3a2e-9358-2d8b2c6f7f42 | -5.30317 | -60.13125 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b03eac8b-b6dd-37d4-9659-a56b823b986c | -9.7336 | -43.39123 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9f05c27a-05ec-31f4-aede-a7157f514075 | -5.29832 | -60.13041 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8038eecb-d50f-38f8-bc70-9038e46244f2 | -5.28798 | -60.11894 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf36991e-a922-3ab2-a826-4e5ee9223c89 | -13.30295 | -45.24044 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 22317050-93ae-3982-8db9-1368600bad8c | -11.51199 | -49.623 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0329470-b6ed-3a13-a508-685c838615f8 | -5.37163 | -56.03413 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c23c4148-ba38-3f15-b7a6-36cb778d8ce3 | -7.10052 | -56.51314 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e63c052-b3a8-384f-845b-c881e02d886e | -9.74201 | -43.41568 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5c1ceaba-1e1f-3597-90b7-7d10305c6de6 | -3.61577 | -60.56983 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9962caa1-9b66-3189-acf6-ee4aac0b56ca | -5.30363 | -60.14355 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4f456ca-9728-3b5c-b3ae-b705e6d9274f | -4.41223 | -60.07495 | 2026-09-07 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66132144-57fa-3d1e-908d-30e94fc1de41 | -6.11019 | -57.63847 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90e842cd-54ba-342a-964c-c80ac48f7f70 | -10.73761 | -45.07842 | 2026-09-07 05:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c81ee7e-3b79-3ac4-b620-0e8e353f7846 | -5.13045 | -49.60026 | 2026-09-07 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c666cb9e-8aa8-3108-aa0c-eecba75b1a63 | -7.16542 | -46.45757 | 2026-09-07 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2be3376c-77ad-3105-bf05-00eee7500650 | -11.5064 | -49.60745 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b45a711-925d-3d8e-a910-6e69f6bd3b60 | -3.38296 | -61.32219 | 2026-09-07 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75a2e14e-e0c8-34e6-9314-6d02fbdfd0e9 | -10.7372 | -45.0815 | 2026-09-07 05:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eda373a2-efd6-3eea-9597-ef6a79faf2ed | -5.59347 | -60.24926 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71f15568-0e2f-3ef5-a386-64c9eacdee42 | -3.82882 | -60.76691 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05718fdd-6589-308b-b162-dfcf83e08881 | -5.59833 | -60.25016 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fa86f6e-2532-3197-a318-98da251f112a | -5.37017 | -56.04289 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 052dc9bb-4825-3801-9b13-f77630953d88 | -4.40733 | -60.07415 | 2026-09-07 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b7860cd-de43-3820-9232-0c5ce83a6650 | -8.75761 | -62.42626 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e049e977-82eb-360d-a2b2-b6c482108c8d | -8.72354 | -62.44813 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92b04d56-d4e2-3186-af08-af2dc101cca2 | -9.73535 | -43.42262 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b647e8b4-8a3e-39a1-aa80-155eb01a716b | -5.99207 | -57.69778 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 72f0515a-691f-38bf-bf79-571f8d548431 | -6.11078 | -57.63493 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37e32073-d8f1-3555-bebc-3151d789a704 | -5.36196 | -56.02351 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c0b1deb-6098-3fa7-ba76-786ebdb0601f | -9.74921 | -43.40459 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| de1bc379-4f2a-3e27-9eef-bd20ab64235a | -13.30357 | -45.23046 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8ce4ae77-3d37-3732-89eb-c822ed91402f | -4.97724 | -50.6304 | 2026-09-07 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a714aa12-b079-3af3-a5fa-ea6e5b6e8d29 | -3.61115 | -60.56594 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f188f2a3-5679-3ffb-9741-3b78cb4893c8 | -5.25955 | -60.1237 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d26bb63f-5d77-3df7-b3cb-42c5e4154572 | -13.3024 | -45.24026 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d032593-06f5-37fe-b60f-eb4829338452 | -5.28611 | -60.12957 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 343b9d9c-3fd8-34d2-a5ec-f27559a9093c | -7.09979 | -56.51761 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aade9fd0-b789-3f7d-bf8c-d826dce87cc2 | -5.15212 | -55.96095 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c89ec3dc-aef5-3120-ae74-b8fc73d39b25 | -5.3568 | -56.03165 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ae2441c-7297-3921-88da-ecc6f032352e | -9.93396 | -48.04906 | 2026-09-07 05:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 858c6bd7-1b04-35f0-8db7-7a8710723390 | -8.76576 | -62.42831 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fc71c2f-3424-3e23-8cb0-0d287f54fabf | -7.91125 | -47.66687 | 2026-09-07 05:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52303eef-2025-3803-b773-c24b8190066c | -8.72541 | -62.43791 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa295f19-2c9c-36e6-88cf-f151aa320779 | -8.56939 | -45.98378 | 2026-09-07 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d196299-23ca-300e-9774-5da56392077a | -6.92701 | -55.61898 | 2026-09-07 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4e2b787-ff42-36e4-a37f-8438d1861366 | -5.29743 | -60.13573 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 69c7c90e-cb11-3004-ab25-9a99f00595df | -8.72478 | -62.44134 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6e74a1e-a6b1-3db5-87f4-4ca09f412a66 | -7.10586 | -56.51214 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 485af1cf-9ec2-3d0f-913b-d7bb043657f1 | -8.75635 | -62.41941 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49bbb58b-e99c-3da6-8d57-12cec90d5ef2 | -8.75573 | -62.43624 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 587e734f-6e84-305b-8cbd-eed8f9c6e1ab | -11.51967 | -49.62414 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42018969-a022-34ec-ac71-6f701abd1bc9 | -5.97761 | -57.68435 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91090e51-0e46-3e51-976a-51b7480b604f | -9.74102 | -43.42342 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 54bd287b-d6ff-33fc-8405-78466e8a6c5c | -13.30461 | -45.2274 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| ab341855-5d1c-3b88-a7f5-b8f65d3e2e9d | -8.75271 | -62.4395 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bbbad824-fbe3-33ba-be8d-d6bcb783c198 | -8.68775 | -62.46237 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06b9764f-609c-3399-9a45-7fa7434e6f0f | -11.32175 | -45.09599 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8740f015-cdfc-39ef-a7c2-47db9b972f14 | -11.32728 | -45.09397 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fb416f1-b033-3232-ab6d-435d97010782 | -5.36742 | -49.19982 | 2026-09-07 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e36e3232-1447-3ff9-a276-1a146dc01877 | -11.51513 | -49.62834 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ef8fbae-f34d-3529-a7ff-61590b5ed29b | -11.52982 | -49.61763 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0c3e5928-6b6e-3d24-8905-9aab5d412a41 | -13.21372 | -61.74436 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9f48b77e-5150-3d24-b523-aa9c32aea96c | -13.21058 | -61.78619 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce044ee1-197f-3b06-bf7c-2571761a2c52 | -12.75906 | -52.84556 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a29a330-4011-3374-b626-355fb7844920 | -12.75793 | -52.85287 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76d6b125-78d6-3faa-9f13-138db3fbfd97 | -13.21538 | -61.7856 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cd4a3d6-c359-3ebb-84ac-12318a6ebfdf | -13.22478 | -61.73446 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 731432de-69a4-3043-b9b5-6871448d9679 | -13.07166 | -62.20876 | 2026-09-07 05:06:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44308194-989e-3b77-8af0-0492f161ee7c | -13.28051 | -61.75243 | 2026-09-07 05:06:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1243b4d4-7a67-377e-91f0-0a164eca80d2 | -12.76131 | -52.8534 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85418fd7-7c27-3117-ae5d-141b453d216a | -13.22291 | -61.74466 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06110c18-9bfd-3a5e-92f2-e93a8e3e69c4 | -13.25882 | -61.76396 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fdeb1d8d-0dbb-3e3f-8908-b5217ce0862e | -12.75568 | -52.84503 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60d94c48-ceb3-31d5-848d-305c7560c94f | -13.24276 | -61.77136 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| afa6c1d5-422b-3ee2-92d2-f43391257e6b | -13.21632 | -61.78047 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c32238d-bd25-390a-93a0-f55af003f440 | -13.26448 | -61.75979 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e65e3f1-a049-3835-8c7e-c2ad12fe191f | -13.27955 | -61.75753 | 2026-09-07 05:06:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f948447-7fdc-370c-b8cd-201017713896 | -13.24844 | -61.76719 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cdf62ec2-e1e4-366f-a2d9-83f921f6289e | -13.22668 | -61.77876 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2c49e64-d996-3c48-b507-71d16ada93ce | -13.24747 | -61.77229 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c36e1033-b2bb-3de0-a115-0a821c67d017 | -13.21914 | -61.7386 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97c8b6ad-9ede-33e7-bd4b-a5601135bfc8 | -13.21627 | -61.782 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d87890c8-c4db-3316-b029-2425fced996b | -13.26352 | -61.7649 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb138415-3ea8-3b17-8f70-cd997da4635b | -12.76244 | -52.84609 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 150d1d07-c03e-3bde-9cf1-e800cd42aabf | -12.7585 | -52.84922 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 138ae303-ba62-3ee9-a337-cc49ac888dd0 | -13.23139 | -61.7797 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f9773ac-d59f-35a4-b036-a9ec01152278 | -13.2147 | -61.73928 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d116044-b76a-369b-b2fa-f5787b4ff296 | -13.85144 | -43.64878 | 2026-09-07 05:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de972bc3-8563-32f3-9568-df7191545a3c | -12.76187 | -52.84975 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1f92870-e81e-375b-80f8-faefe51a9499 | -13.23805 | -61.77041 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35d83e4a-fac7-329c-a4c3-c3fa3352600b | -13.28616 | -61.74828 | 2026-09-07 05:06:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee1ea02a-62c2-39fe-8476-bdae64f109f2 | -12.75962 | -52.86435 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d931a514-4293-3b72-9d46-4fa49d92394e | -12.76075 | -52.85706 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ec73ad4-63c7-330b-b3df-255a91bcddc3 | -14.52604 | -59.80389 | 2026-09-07 05:06:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e3b9ccd-6c53-3fca-b36e-73dcf9a44d41 | -12.75962 | -52.84191 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README26.md)
