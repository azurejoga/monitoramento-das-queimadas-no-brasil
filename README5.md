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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9049c053-291b-33a1-a494-0945d840a930 | -4.0977 | -47.9927 | 2025-11-12 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 85d2813d-74b2-3421-82c3-b69008e4ad6f | -4.116 | -48.0352 | 2025-11-12 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 67a80eb5-69c3-3e01-96f5-26c2edbc62d9 | -4.0974 | -48.0361 | 2025-11-12 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 245abf9f-4bad-3edd-bc26-0461b672ff4a | -9.8389 | -36.0331 | 2025-11-12 01:30:00 | GOES-19 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 81.0 |
| e33a5555-5248-3779-b24d-f7c925697723 | -4.1162 | -47.9919 | 2025-11-12 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3492d4ce-5758-366b-847d-e0c656e60aee | -4.0976 | -48.0144 | 2025-11-12 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 260.6 |
| 40de9801-09d5-316e-9bd3-29f1fd6d2b83 | -4.1161 | -48.0136 | 2025-11-12 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 209.1 |
| 999ba13a-6bc4-3b72-a97c-be52166b34b9 | -4.0974 | -48.0361 | 2025-11-12 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 7e76dded-10cd-354c-b5a7-e094f0b9280e | -4.1162 | -47.9919 | 2025-11-12 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 6d9e3c41-0575-3f66-b0f6-97757e156d1d | -4.9643 | -43.7182 | 2025-11-12 01:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 0a9d9a4d-9308-3272-9b02-877762ae7b42 | -4.0976 | -48.0144 | 2025-11-12 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 97831dd6-b5ad-301f-a067-999515be6ec9 | -19.7223 | -58.0491 | 2025-11-12 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 6f7ce955-dab7-3d35-92df-1632ecf61e77 | -4.116 | -48.0352 | 2025-11-12 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 11182f2f-25bc-31e0-9fe3-58a9936db341 | -4.9643 | -43.7182 | 2025-11-12 01:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 187ce35e-8733-3642-b0c0-a22e0d5444d8 | -4.9456 | -43.7194 | 2025-11-12 01:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| d87c917c-c353-3a63-a7ac-2e7cf8aa3907 | -4.0976 | -48.0144 | 2025-11-12 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 295.7 |
| 287d8fe5-15ff-3907-9e58-8d319eca09f1 | -4.0977 | -47.9927 | 2025-11-12 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 00890ddf-4251-376a-9430-483a3f816fdc | -4.116 | -48.0352 | 2025-11-12 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 1bc4d3ba-f6a2-37b2-a31d-aac6f6146b1c | -4.1162 | -47.9919 | 2025-11-12 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| fe7d9d31-042d-363b-aa38-7eec5ac53109 | -4.0974 | -48.0361 | 2025-11-12 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| d0dcb9d5-7daf-392d-849b-285f3ca776cf | -4.1161 | -48.0136 | 2025-11-12 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 222.0 |
| 291ea70e-005c-3efa-904d-3d8d5c2770ad | -4.9643 | -43.7182 | 2025-11-12 02:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 23a5df85-a000-344d-a987-65406e20e8b5 | -4.9456 | -43.7194 | 2025-11-12 02:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5093f1ec-7e17-385e-81fe-2bf4b497e63b | -4.116 | -48.0352 | 2025-11-12 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 56a10dcb-5753-3494-9720-eaeae02e3319 | -4.9641 | -43.7413 | 2025-11-12 02:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 7b1dfa1a-7a5e-3c86-ab91-03bd2e635a24 | -4.1162 | -47.9919 | 2025-11-12 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| bb7f5516-2d1d-3c8b-af2e-f1c2d00a2de0 | -6.5631 | -51.1126 | 2025-11-12 02:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 20f1ce8a-b05c-3dd6-b701-f1ce480f8a92 | -4.1161 | -48.0136 | 2025-11-12 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 218.8 |
| 47e193a9-c722-3deb-a328-090626fea276 | -4.0976 | -48.0144 | 2025-11-12 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 280.4 |
| 4eed2574-6bf2-3185-9d0e-5fc5285f9101 | -4.0974 | -48.0361 | 2025-11-12 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 8ad72016-3a2b-3df1-98d1-7a978aed97a5 | -4.0974 | -48.0361 | 2025-11-12 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| ca518a16-60c5-3185-8005-2d15c4883f2d | -2.6299 | -49.2045 | 2025-11-12 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 0f75ff02-821a-30ef-8c49-63d087d39485 | -19.8235 | -57.9943 | 2025-11-12 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 090fedcf-a9c6-33b4-af86-8f07f0b07ef0 | -4.9641 | -43.7413 | 2025-11-12 02:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 458938f1-df1b-3d45-b5bd-9e52323159f9 | -4.116 | -48.0352 | 2025-11-12 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 94e05e45-3fec-3238-8c88-a37070ef240c | -19.7837 | -57.9788 | 2025-11-12 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 846fcf16-b4ca-3a77-b607-f86260b49b61 | -4.9456 | -43.7194 | 2025-11-12 02:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 60c7ae86-323c-3f88-954c-4a8c0b4ff46e | -4.1161 | -48.0136 | 2025-11-12 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 174.7 |
| 5ce5d519-dc34-3e2d-afd0-d6d5ca4d22cd | -4.0977 | -47.9927 | 2025-11-12 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 14f7ac9f-506a-37c2-98e0-10666c1d843e | -4.9643 | -43.7182 | 2025-11-12 02:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 756f92fb-2853-33d7-a18c-e7fbc928e999 | -4.0976 | -48.0144 | 2025-11-12 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 274.5 |
| a3186d0d-044a-38c1-a5c6-c05a4f9e8071 | -4.0974 | -48.0361 | 2025-11-12 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 62d1c18e-44d5-3091-b938-9f73ce299bfb | -4.1161 | -48.0136 | 2025-11-12 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 191.9 |
| c31a5735-73cc-3c9d-a3f8-7ddc4a4fd712 | -4.116 | -48.0352 | 2025-11-12 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| efdd885f-e4ea-343f-92b9-ff507f2f29b5 | -4.1162 | -47.9919 | 2025-11-12 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| db6f9611-3f17-3cd5-89f2-4f4535109f63 | -4.0976 | -48.0144 | 2025-11-12 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 197.5 |
| 41de33d7-38a3-3e3c-b1b2-dffc56819b9f | -4.9643 | -43.7182 | 2025-11-12 02:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 392822c5-3cc8-389a-88d3-205c7a54c059 | -4.9641 | -43.7413 | 2025-11-12 02:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 7999df67-561c-3859-af3c-b8d18fbcf9bf | -4.9456 | -43.7194 | 2025-11-12 02:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 612b17fa-0f91-36e1-8a50-8f15a4e10c99 | -2.6484 | -49.204 | 2025-11-12 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 6a2b64c9-a1d6-383e-9d5b-0c546180f13e | -4.1161 | -48.0136 | 2025-11-12 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 183.5 |
| b11b40db-fa1c-366b-80e6-6b5f1fffcd62 | -4.0974 | -48.0361 | 2025-11-12 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| d8040377-c961-31ab-ae92-d2228f760369 | -2.6484 | -49.204 | 2025-11-12 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 0eb38ccf-bd7a-3196-b8db-d9708b3f8f2a | -4.116 | -48.0352 | 2025-11-12 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| be811680-23f9-397a-8c70-49f7a9aa77a7 | -19.8235 | -57.9943 | 2025-11-12 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 8e43e4df-562c-3e23-bbdb-79f3af76e5ba | -4.1162 | -47.9919 | 2025-11-12 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7f648976-2151-3ab3-821c-5320a366ea05 | -4.9456 | -43.7194 | 2025-11-12 02:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 01e76145-16f4-3212-a2c5-5a1bab5973bc | -4.9643 | -43.7182 | 2025-11-12 02:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| d9deed16-09ab-3d9d-b3c8-d542109799d3 | -4.0976 | -48.0144 | 2025-11-12 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 9c755e20-0025-38d0-ac3a-d75fdc183a3e | -4.9641 | -43.7413 | 2025-11-12 02:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| baa49c7c-d7a7-390b-be1f-56bba24a001a | -19.7837 | -57.9788 | 2025-11-12 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.4 |
| 9b8182d7-8db7-327f-942e-c689c7cadc62 | -19.7837 | -57.9788 | 2025-11-12 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.0 |
| 26beb851-c306-3ddd-9324-a2a4a688ace8 | -4.9456 | -43.7194 | 2025-11-12 02:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b37c1272-cb6c-3091-9e66-bfe5e9f8b293 | -19.7223 | -58.0491 | 2025-11-12 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 1341cc1d-2437-3052-af96-246710f43ffb | -4.0974 | -48.0361 | 2025-11-12 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 2b7d7347-6bdb-3706-94b7-91f479a4751f | -4.0976 | -48.0144 | 2025-11-12 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 215.0 |
| 5bbc532a-d102-37bf-abe1-9d956ab32e3a | -4.9454 | -43.7425 | 2025-11-12 02:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| f14cdb02-0d5e-3a17-9290-394ce6e7618a | -4.9641 | -43.7413 | 2025-11-12 02:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| e5ad77f1-39db-3268-9e3f-b4c0dca11b84 | -4.9643 | -43.7182 | 2025-11-12 02:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 64b0070a-4524-3f90-899a-626908e1e10e | -4.1161 | -48.0136 | 2025-11-12 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 175d55a9-cbfa-3f83-8d9e-13da0dcee240 | -4.116 | -48.0352 | 2025-11-12 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 182373f0-4c14-3d07-b0dd-28ff628f5476 | -4.0976 | -48.0144 | 2025-11-12 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 164.3 |
| d82e5f7c-14c7-3492-8b18-725a30e55b0e | -19.7837 | -57.9788 | 2025-11-12 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.3 |
| a586ff31-dec8-337f-9de5-d20cdfe77f0f | -4.1161 | -48.0136 | 2025-11-12 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 5f41d02c-4145-33ac-9399-be02fd1a8fa4 | -4.0974 | -48.0361 | 2025-11-12 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| db1a1f4f-bd4d-3ff7-9f49-7d81b47b1599 | -9.6487 | -40.3364 | 2025-11-12 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 334dd372-8ce1-34bd-a489-5a22a04426f0 | -19.8235 | -57.9943 | 2025-11-12 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.5 |
| bca13c2d-c94e-374b-9d6a-ee3de4ba9a84 | -4.9641 | -43.7413 | 2025-11-12 02:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| c6565b23-971d-3129-b0dc-23540b471706 | -4.116 | -48.0352 | 2025-11-12 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 8bcc1f05-3e24-38fa-b6db-7cc446410b1e | -4.9456 | -43.7194 | 2025-11-12 02:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 51554d03-aff5-3f1a-9dae-2fba84652640 | -4.9643 | -43.7182 | 2025-11-12 02:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| f9661f7f-b365-31c0-a896-d39251390413 | -7.4192 | -35.28025 | 2025-11-12 02:51:00 | NOAA-21 | CAMUTANGA | PERNAMBUCO | Brasil | 2603603 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| bb404cb1-2175-34cc-8adc-4697d21e8e61 | -9.84132 | -36.03318 | 2025-11-12 02:51:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8393bd0c-4780-38dc-be11-593c67e8038b | -7.37706 | -34.90002 | 2025-11-12 02:51:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c1bad9ff-c67a-3da3-8816-fb521797c69d | -7.42016 | -35.27517 | 2025-11-12 02:51:00 | NOAA-21 | CAMUTANGA | PERNAMBUCO | Brasil | 2603603 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e368209f-54e6-3542-8fb0-9da7746479e8 | -4.116 | -48.0352 | 2025-11-12 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| abef693e-9f66-3dc9-b685-e28c7c17c709 | -19.7837 | -57.9788 | 2025-11-12 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 00959a1d-b2ec-39de-a4ef-675a8eddf3e6 | -4.9454 | -43.7425 | 2025-11-12 03:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 0ed40312-4384-3ac9-b19b-17261290c9db | -4.0976 | -48.0144 | 2025-11-12 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 159.7 |
| ca6e7e5b-fa7f-3e08-9f5b-9c4d59540f73 | -4.9641 | -43.7413 | 2025-11-12 03:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 072242b9-af9b-35d4-8cc2-61d4f0cca792 | -4.0974 | -48.0361 | 2025-11-12 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| f2706a83-c06a-3643-8ef0-79392ccdfc55 | -19.8038 | -57.9762 | 2025-11-12 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 2f64410a-cdff-3ce3-b572-0739165d7c10 | -4.9643 | -43.7182 | 2025-11-12 03:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 111cddc2-fee8-3fb5-bec8-a14f25fcd640 | -4.9456 | -43.7194 | 2025-11-12 03:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 73e1b5a7-85bc-3104-9705-028c7fea67da | -10.5076 | -44.944 | 2025-11-12 03:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 76473903-5c8f-30af-b98a-ce38cb55f6cf | -19.8235 | -57.9943 | 2025-11-12 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.3 |
| f4bb0567-2f4f-39b5-89f7-d5fb5ab57cba | -4.1161 | -48.0136 | 2025-11-12 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| ba4df283-0142-33bc-985f-9e1ede887d10 | -4.0976 | -48.0144 | 2025-11-12 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 86cd7f5d-5bc7-38e5-a351-10c6b6861e8d | -19.7837 | -57.9788 | 2025-11-12 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 07b18df5-56fa-347a-a815-a38a067aef7b | -4.0974 | -48.0361 | 2025-11-12 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |


[Clique aqui para ver as próximas entradas](README6.md)
