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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 291f8a8d-1f9e-3d36-a093-b787958efa05 | -14.89329 | -46.98834 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f6a3985-424f-310d-a0f7-3a361c4b0c29 | -14.70279 | -43.89328 | 2025-10-03 03:45:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 87681600-92c9-3008-a6eb-b1c098fb8030 | -13.24644 | -47.30058 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e5faa02-694d-3708-b44e-fe621b988c17 | -13.76735 | -48.04898 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c6fab465-33d2-36e4-93f2-a7ea43874953 | -15.92131 | -43.30257 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af57d938-05de-3e05-9554-873cde657f50 | -12.37912 | -46.531 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5d63304-ec01-33e0-8dfb-16d0d43e782e | -12.83415 | -46.945 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a57a09e-7ab4-37f9-ac0b-0921750a9dfa | -11.06216 | -47.79516 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f50d136-8619-3109-b7f6-457906ba02f5 | -11.85675 | -44.96258 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0249fc0-c169-3c03-8542-3ee6bab5678c | -14.22385 | -46.08907 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 922c8651-6c28-3450-9618-86b5330b9376 | -12.11398 | -43.44424 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 598831c2-5874-3b32-aabe-1e674ffda2c0 | -13.14944 | -47.83257 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1f6f440-7baf-3350-be38-61da52c1d007 | -9.95419 | -43.70125 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12915859-6fbc-3722-9e7f-22ab91ed25f5 | -10.8674 | -46.67008 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 54d67d7e-74dc-3fd6-9baf-767de913c88b | -11.29622 | -47.83352 | 2025-10-03 03:45:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd27a4c9-9ff9-3706-bff8-0b9131b3c43a | -13.20032 | -47.88364 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26796607-12ca-3493-8e40-a283107bbcaa | -11.91508 | -46.2739 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 12a915a3-53ae-376d-a32c-228915fd354b | -13.24305 | -47.3462 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05b6c92a-3c10-3f70-b5bc-faa8acc48845 | -12.81047 | -46.85986 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 135c0e03-a42b-3824-89de-54d5528c4842 | -13.8693 | -47.93897 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99f820e9-ef39-3620-ad6c-886d795baf6c | -13.47336 | -47.23745 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8fdbc33-50e2-3534-bd7a-47acdec8859e | -11.84356 | -44.9524 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b732f00-877f-3dd5-9beb-5833037f80d5 | -15.51817 | -46.80261 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8d1f442-956b-3ef6-9c27-73f062fa94ca | -11.41484 | -43.49375 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e52c8c67-eaf6-398b-bcea-009a797b3a0c | -14.61971 | -41.46566 | 2025-10-03 03:45:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b28c1a81-a64f-34a5-a4f6-c479a4ae3ffc | -14.67815 | -48.07462 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b80225d6-4474-33e8-b213-f46c953c00e2 | -11.80719 | -45.00822 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3953141-5b07-3ee5-a824-3a6a605446a8 | -13.58453 | -47.589 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9c649ed7-60f7-35c9-8454-c475ac4c5c1f | -11.90567 | -46.29353 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10a66923-66a8-3670-8607-d40868eb1079 | -11.09225 | -47.80495 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7897ac1-e4da-3e92-a3f6-6218d74f543d | -13.3381 | -48.11873 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23bd170b-3f84-3fc2-a405-2214d9ff69e1 | -15.79073 | -43.68245 | 2025-10-03 03:45:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c2d08a1-de8b-32e1-8498-dc2045c307d4 | -13.65942 | -47.3036 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 354edf3d-1110-315b-8e52-8f38a000e35c | -8.81221 | -46.67067 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bce9fd3c-c2d6-3141-96b7-bd4f6695331c | -9.94266 | -43.76468 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 489cb43f-5996-39e5-96b6-9b0b14864951 | -14.63999 | -48.25972 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cdf034e8-2266-37a2-8225-a470db3b5b39 | -11.04401 | -46.65273 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dba4a3d6-f5eb-3a54-85d0-bb4659931e09 | -11.44782 | -44.96413 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 867a5a25-64f8-36ed-8446-3d225b6e8ab1 | -11.99666 | -47.19386 | 2025-10-03 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bd7ba63-380d-3e3f-8c33-49db260d5874 | -14.65156 | -48.29287 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dce32c15-3b4c-365c-9605-4bfd8ec4d6d1 | -14.58878 | -46.71402 | 2025-10-03 03:45:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a60f85c-eac2-3949-9864-58a551f6b206 | -9.91826 | -43.76415 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4c919600-c796-30af-8984-143d4d45f2b9 | -14.29521 | -46.03312 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c2827c9-c45a-3cb5-9205-dadde526b541 | -12.61819 | -46.99976 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e26e3e84-b9ff-32bd-ac71-27a2d569110c | -10.8713 | -46.67158 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e9697323-6cdc-32c1-95e1-cda9ed81293a | -13.75512 | -48.0783 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2a1820b8-f4cd-3494-bdd5-3224f4a34f1a | -15.19566 | -46.40196 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7132969d-4ab9-398f-a30d-dee82a71fa1c | -8.59033 | -44.78625 | 2025-10-03 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 262d5cda-2cbd-31ce-9500-2146df9e370a | -14.68051 | -48.09262 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ee9f785-0408-3b60-8e6e-4b5094309251 | -13.13907 | -47.89392 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da15224e-fe94-3cb7-b9b2-c6f6710a913d | -11.48919 | -44.99443 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7018522f-2993-3381-b873-3cf18bc84533 | -11.83401 | -45.03211 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 511193a6-8395-301c-b332-1fc59c7ca03f | -11.83016 | -45.02471 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8530790f-6b67-3d22-ade6-e049edf133a1 | -12.75784 | -44.90822 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4a91478c-a577-3f18-8f7c-b35f7235fa92 | -13.13768 | -47.83923 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a2d0f575-97ff-3617-bc47-96d0462c0359 | -12.85863 | -46.99818 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9656f4d7-26eb-3509-82cf-7a89adc59235 | -11.45796 | -45.13366 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88a9d685-1fde-30bb-a2ad-5b0c411c57e8 | -14.66849 | -48.26089 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb585f70-437f-310c-b7f7-a0a098bff955 | -15.64952 | -46.2579 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac311613-4ff8-3402-b238-4963a160f087 | -11.06134 | -47.79936 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43548a01-7bf2-3804-a9d4-1f02be32865c | -11.56222 | -47.64986 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3602eb4-9d32-3171-9470-9b0b2db5aae6 | -14.68147 | -48.08794 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c29f74f0-8f8c-3b79-8cf8-e6fb9edabbe2 | -11.41571 | -43.48899 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa7187fa-25e1-3a4e-a22d-66f495f00113 | -12.6425 | -46.96529 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6d20373b-1f11-3e69-a137-6867d99d7b05 | -12.6217 | -46.98195 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d42a14db-67b1-3932-8f0a-81d3b06dedfd | -10.8442 | -47.2187 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f832688-4ad6-3ae8-8a26-f0dcd005da91 | -8.55372 | -47.6481 | 2025-10-03 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 545d114e-39ee-319f-815e-dec92f68d75c | -12.92988 | -48.43154 | 2025-10-03 03:45:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c100005-38ca-368d-bf59-676942309402 | -11.90225 | -46.31141 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a592a4c7-0b8f-3e90-be31-165801336b00 | -13.14287 | -47.83473 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ee6fa748-52d2-3f22-aa6e-113cf7719acc | -14.66439 | -48.26025 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e39adac8-b7a9-340f-90d2-22070fd6976e | -13.26379 | -47.26149 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 901b9ac5-13be-3755-91c0-d038add28b75 | -13.13995 | -47.88947 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 508fcf2e-1f36-3db6-b552-51b2f93e1ab6 | -14.71808 | -48.19967 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90066e21-76f9-3461-9ce2-f0ff5828cfb2 | -15.92471 | -43.30756 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61ac4bf3-2499-37ee-9fb1-769b5f13114f | -13.96531 | -48.1694 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e34b1c10-2510-3e3f-bf59-8a1cbe03a0ee | -14.94676 | -47.5192 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e70be97-909c-3313-b936-50e329c8830d | -13.75 | -47.98502 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 45b12606-06cb-31ff-a052-18c021bcc889 | -13.5797 | -47.58331 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5ee24167-227d-3632-96a3-d31d631cf5ab | -11.80543 | -45.01764 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e84f1b2e-f300-3542-92ce-f770dde077fe | -12.61995 | -46.96111 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e0970dd6-0fee-3783-8a14-838f12e9a84f | -13.63657 | -48.67602 | 2025-10-03 03:45:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5dadbbe5-8244-32c8-a314-e3d8662f53fd | -16.33944 | -42.38468 | 2025-10-03 03:45:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 526820b9-caa3-3d6c-9ffa-b2fb6c2faf77 | -14.42737 | -46.35352 | 2025-10-03 03:45:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe40641a-3f4f-310e-be74-5abb9241935d | -14.41172 | -47.87461 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2213980d-1097-347f-9ab9-dd7c6fcbde0a | -10.87949 | -47.81977 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 48af8e1e-9492-3321-bde8-bcdc6a19ed82 | -11.82544 | -44.9106 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e91951f6-0d2e-301f-aa92-9a656ff59805 | -14.67211 | -48.07459 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ccba505-9ae3-3a2c-8b6e-a6dea0ae8159 | -9.9398 | -43.75324 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f5a65851-b5ed-350c-a691-d31d62f16636 | -13.30731 | -47.2622 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1703bbe1-da67-3d45-904a-0ee2bfa35d76 | -15.29879 | -46.29699 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2251661d-c281-3efd-bc67-529787eb61e3 | -10.77349 | -46.59791 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efee3758-b1bf-3e9b-b06a-9dd2d8877320 | -15.70842 | -46.25436 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4461ccf8-2a0e-3156-ad96-efe6c3c3a420 | -8.58972 | -44.78962 | 2025-10-03 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 446ac4b7-87d7-38bd-a3ed-fb8a7efbe87b | -11.91881 | -46.28398 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6b47af94-0e89-31da-8809-1d2718aa1d82 | -11.80272 | -45.0043 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f4ae542-9797-30d8-8a5e-2e2e0e064903 | -14.63029 | -48.12993 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9f9e09d-487c-31b3-ade5-4d70b6ed7cf5 | -12.63099 | -46.99424 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8dca333-4b1e-36c7-b896-c05680e7f105 | -12.29743 | -45.37159 | 2025-10-03 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af64b210-51ff-39f5-a9e7-423db38e5ea1 | -11.85633 | -44.96745 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README32.md)
