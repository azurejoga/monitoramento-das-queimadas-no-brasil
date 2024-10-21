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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 785be9e1-8f13-3dcb-8b71-6cdae568afa8 | -10.20017 | -64.84665 | 2024-10-21 06:20:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f7a0156-2681-3948-af92-c8cb8c063e66 | -10.19697 | -64.84289 | 2024-10-21 06:20:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47450219-0255-3826-b828-496013be32ea | -10.19477 | -64.84143 | 2024-10-21 06:20:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de179059-011b-3527-938f-94664ba7fcfa | 1.8327 | -50.4879 | 2024-10-21 06:24:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 8e73bd4a-e258-378c-bd6d-80a8e05e53bd | 1.8327 | -50.5088 | 2024-10-21 06:44:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 42.7 |
| b494b049-db0c-371a-a7e4-84320642b32c | 1.8327 | -50.4879 | 2024-10-21 06:54:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 88a0cc9c-0104-34b4-bd84-fff3c693a37e | 1.8327 | -50.5088 | 2024-10-21 07:04:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 26eecb62-85f1-3f04-8aca-1d65ab429896 | 1.8327 | -50.4879 | 2024-10-21 07:04:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c348d765-5576-3847-98aa-129367e01d04 | 1.8327 | -50.5088 | 2024-10-21 07:14:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 6cfdaf76-664c-3e95-b0a9-5fb1232f64c7 | 1.8327 | -50.4879 | 2024-10-21 07:14:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 70.5 |
| d48ccd44-bdbc-3add-a6e8-7ec9f2e13411 | -12.5147 | -63.3014 | 2024-10-21 07:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 485878e1-9318-3430-9e42-890d5438b365 | -12.5336 | -63.3003 | 2024-10-21 07:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 7dbafee4-0d8c-3ddb-a33b-35a812cb9957 | -18.2828 | -56.0994 | 2024-10-21 07:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 0e756430-ce63-3c04-bb14-428382385c96 | 1.8327 | -50.5088 | 2024-10-21 07:24:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 48fd721c-0f5b-3dbf-97d8-94fd824dfff4 | 1.8327 | -50.4879 | 2024-10-21 07:24:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 270ac814-79a3-39e0-9286-4cef15f8d9c4 | -12.5147 | -63.3014 | 2024-10-21 07:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 25897db1-cf8a-3a63-bbab-ae68b56c33ca | -18.2828 | -56.0994 | 2024-10-21 07:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.5 |
| d8ea5f08-c92c-30ee-98b8-632fb365f3f8 | -12.5147 | -63.3014 | 2024-10-21 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| e5161a7b-c232-35a1-b238-b99e0db0c15a | -18.263 | -56.1021 | 2024-10-21 07:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.1 |
| de220e71-996a-3a17-8363-0f0627939d15 | -18.2828 | -56.0994 | 2024-10-21 07:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 1ba041ce-71fe-35bf-abfa-d4db2107be6f | 1.8327 | -50.5088 | 2024-10-21 07:44:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 00f8a505-9a9d-3aae-a392-152a04b597b2 | 1.8327 | -50.4879 | 2024-10-21 07:44:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 88.4 |
| a16e1c78-1b6b-35bb-b383-7ceaabdcde47 | 1.8143 | -50.5092 | 2024-10-21 07:44:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 09afb71b-0759-3713-b64b-6f373707b574 | -12.5147 | -63.3014 | 2024-10-21 07:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 5bf8c80c-0589-3417-860c-06ae4c038610 | -18.2828 | -56.0994 | 2024-10-21 07:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.4 |
| ad87ce0c-af70-363b-9b90-83ba36683478 | -12.5147 | -63.3014 | 2024-10-21 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 0a465e6f-34bd-37a2-b24c-5a8f15e9e405 | -18.2828 | -56.0994 | 2024-10-21 07:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.5 |
| 7e136dc2-f58b-336f-95b6-0785ecd0702f | -12.5147 | -63.3014 | 2024-10-21 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.2 |
| a59bd618-6d7d-3c96-8c7f-7045467db571 | -18.263 | -56.1021 | 2024-10-21 08:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 16e1439c-abd7-3355-bdbf-57a130fb6d1a | -18.2828 | -56.0994 | 2024-10-21 08:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 6e002324-c717-347a-b5dd-681a593ec54c | -12.5147 | -63.3014 | 2024-10-21 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| d56b27b5-31a7-3b92-bb4a-74d24fc0352a | -18.2828 | -56.0994 | 2024-10-21 08:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.9 |
| f9d2ab3c-4c2b-38aa-8400-79853f9aa9de | -12.5147 | -63.3014 | 2024-10-21 08:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 4825953d-ea0d-30c5-afa6-be6ce890daf0 | -18.2828 | -56.0994 | 2024-10-21 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| d4d27dda-6528-36a4-b3a8-95fac14b1dc6 | -18.2828 | -56.0994 | 2024-10-21 08:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.5 |
| fdd79404-fe10-3a91-bd6d-c7dfe019c287 | 1.8327 | -50.5088 | 2024-10-21 09:24:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 9954bec4-9d07-3c56-8ec5-db6a30b0103a | 1.8327 | -50.5088 | 2024-10-21 09:34:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 110.7 |
| d21713e7-2b24-3a16-b4c0-f28bfee735c4 | 1.8327 | -50.5088 | 2024-10-21 09:44:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 2ba1be44-c491-365c-978c-392302d504df | 1.8327 | -50.5298 | 2024-10-21 09:54:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 91.8 |
| de721713-bbb6-3769-858d-ad8f6ef149f3 | 1.8327 | -50.5088 | 2024-10-21 09:54:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 9c7e1a23-2b29-36ca-a897-0199db822834 | 1.8327 | -50.5088 | 2024-10-21 10:04:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 76.0 |
| d3890c70-2e76-3a49-bb6d-8c3aa738984d | 1.8327 | -50.5298 | 2024-10-21 10:04:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 72e1dc7b-7ca3-3191-a1ef-ff2017eeda79 | -18.2828 | -56.0994 | 2024-10-21 10:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.9 |
| 07dfa33d-1760-3c36-bdfe-cb6ea1b498d5 | 1.8327 | -50.5298 | 2024-10-21 10:14:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 160.0 |
| d757ea3f-bfab-323d-9e9c-a8ea0f946d0b | 1.8327 | -50.5088 | 2024-10-21 10:14:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 04aea872-50ed-3d31-92bd-1595aea0ae4a | -18.2828 | -56.0994 | 2024-10-21 10:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.1 |
| 83b5cb36-252a-33b1-9502-567b989b4828 | 1.8327 | -50.5298 | 2024-10-21 10:24:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 329579d2-9547-3a71-8260-f9bc975ec047 | -18.2824 | -56.1204 | 2024-10-21 10:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.9 |
| d292fa92-192b-33ea-a980-1e3e46109dfc | -18.2828 | -56.0994 | 2024-10-21 10:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.9 |
| 2dc67cca-7ee5-33b7-99cd-459182b7566f | -18.2828 | -56.0994 | 2024-10-21 10:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 185.8 |
| a81d75ab-89eb-3906-a852-ac21fe4d9971 | -18.2824 | -56.1204 | 2024-10-21 10:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.9 |
| e75f1ed5-323f-37db-8288-022f05ac0a7d | -18.2828 | -56.0994 | 2024-10-21 10:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 169.8 |
| 7998fd6a-de5a-36e8-9ca9-a6134657cec4 | -18.2824 | -56.1204 | 2024-10-21 10:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.3 |
| cdbf1f94-d4d3-37a7-bb30-aafb863defe8 | -18.2828 | -56.0994 | 2024-10-21 10:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 232.5 |
| dc2f239e-1028-3ca7-a978-21266b15f4de | -18.263 | -56.1021 | 2024-10-21 11:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.7 |
| f2970dc9-eb9e-3aac-a415-66b4e504b9b6 | -18.2824 | -56.1204 | 2024-10-21 11:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.3 |
| aa5790d0-7f40-3f3f-b3d5-6edcf31a3b41 | -18.2828 | -56.0994 | 2024-10-21 11:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 228.0 |
| 80fe0700-4997-3cdd-a93e-ffe3a55ccad6 | -18.263 | -56.1021 | 2024-10-21 11:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.6 |
| 78d71a7f-e8c3-3f09-8111-d531852e05b3 | -18.2828 | -56.0994 | 2024-10-21 11:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 269.4 |
| 6ee005eb-fc42-3432-82de-49dcc18e3f5c | -18.2824 | -56.1204 | 2024-10-21 11:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 175.8 |
| 3d4cfe97-3614-3806-8cd6-2e3346d78a42 | -18.2828 | -56.0994 | 2024-10-21 11:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 348.3 |
| cb9fb401-9e09-3fbd-b4da-2954a4b3cb5d | -18.2824 | -56.1204 | 2024-10-21 11:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 249.6 |
| 0b0da196-fb52-31ac-84ec-267854dacb0b | -18.2828 | -56.0994 | 2024-10-21 11:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 417.3 |
| 92eeac35-8f1b-37db-b757-69c4e53b2cf9 | -18.2824 | -56.1204 | 2024-10-21 11:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 285.0 |
| d34c7484-641d-3f4d-b8c6-70d7583211a5 | -9.82757 | -36.36309 | 2024-10-21 11:49:00 | TERRA_M-M | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 0270ca2f-cb61-345c-8995-da2dc7589827 | -7.36312 | -40.30056 | 2024-10-21 11:49:00 | TERRA_M-M | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| b913260f-1baa-381b-847e-5473219cb70c | -10.44191 | -37.16987 | 2024-10-21 11:49:00 | TERRA_M-M | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 109.9 |
| fe46785a-1655-3ccd-9250-ee5b7ac00720 | -13.79455 | -41.49202 | 2024-10-21 11:51:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 42.8 |
| 1c4c4ef7-018c-3217-b36d-1536484f8654 | -18.2824 | -56.1204 | 2024-10-21 11:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 260.7 |
| 06ff3c00-7d06-3947-b1f1-8eb18705b6ff | -12.5147 | -63.3014 | 2024-10-21 12:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 92086241-790d-35c4-a5b5-6e386067d05e | -18.2828 | -56.0994 | 2024-10-21 12:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 461.7 |
| 18bad666-6811-3846-9b29-a3f2005924e4 | -12.5147 | -63.3014 | 2024-10-21 12:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7e92a9e6-86f1-3b6b-95dd-c3909a5f5f59 | -17.7065 | -57.4569 | 2024-10-21 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 76b44f02-ac72-3ad7-82e3-9aa42e916909 | -18.2824 | -56.1204 | 2024-10-21 12:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 211.7 |
| 2fe2f7ca-359c-3bce-96ab-50be05dc2cf4 | -18.263 | -56.1021 | 2024-10-21 12:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 16845735-8e33-34cd-b0c6-eeb553c96de5 | -18.2828 | -56.0994 | 2024-10-21 12:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 328.9 |
| 57c05cca-ffc3-39bd-8448-056206da9d74 | -12.5336 | -63.3003 | 2024-10-21 12:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 87891df1-f9ff-3054-98b3-d08e883bd965 | -12.5147 | -63.3014 | 2024-10-21 12:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b3e5d807-ab85-376a-86ac-bc28821f2916 | -17.7065 | -57.4569 | 2024-10-21 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 6526e75e-40bb-36b0-a4f4-505e6ced4e3a | -18.2832 | -56.0785 | 2024-10-21 12:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.9 |
| beb7c2df-b18e-3fc4-a337-9f9be15dd547 | -18.263 | -56.1021 | 2024-10-21 12:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.8 |
| 6f4e3e4d-6456-33cb-acd3-a7d3eab7ab5f | -12.5147 | -63.3014 | 2024-10-21 12:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 5af10261-324b-3d44-b200-2736337d40c4 | -12.5336 | -63.3003 | 2024-10-21 12:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 15cedae4-f14c-3cc8-b83d-d8dc08e564bf | -17.7065 | -57.4569 | 2024-10-21 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| 99e40830-e1d3-3423-a215-fc5beefb43fc | -17.7069 | -57.4363 | 2024-10-21 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 80c5680e-e0a8-3f3d-a1b0-1fbde77d51f1 | -18.263 | -56.1021 | 2024-10-21 12:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 88801083-6412-34e9-b864-4144e7bb2390 | -18.2828 | -56.0994 | 2024-10-21 12:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 430.2 |
| 080a975b-973e-3688-a09d-38e4531efa12 | -18.2824 | -56.1204 | 2024-10-21 12:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 271.8 |
| 02bfeb04-1a75-3047-b25c-ec7d347850a8 | -12.5147 | -63.3014 | 2024-10-21 12:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e1a0a1e1-1350-3f15-93cc-70d7bfe68dd8 | -12.5336 | -63.3003 | 2024-10-21 12:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bb13a5c8-7b2d-3350-9d17-aa15fce68f97 | -17.7065 | -57.4569 | 2024-10-21 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.6 |
| 04792582-2fab-3580-a903-b45169efd238 | -17.6871 | -57.4387 | 2024-10-21 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| a87630a8-c0d8-390a-afc8-6aa45115ae77 | -17.7069 | -57.4363 | 2024-10-21 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 8f52a86e-9c03-3859-b3f1-70f926493da8 | -12.5336 | -63.3003 | 2024-10-21 12:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 594e6544-19ed-3055-828f-f1f5b426c8ef | -12.5147 | -63.3014 | 2024-10-21 12:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 85fb77fd-add9-3303-9947-2a73ea4fea2a | -12.4967 | -63.1874 | 2024-10-21 12:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 7917d513-6c72-3d99-84e2-e8a0e06bf240 | -17.7848 | -57.4885 | 2024-10-21 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 56c92260-37cf-3542-b574-dcc7edca7808 | -17.7266 | -57.4339 | 2024-10-21 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| cbdac62a-5704-39db-8f28-bc7194a8001d | -17.7069 | -57.4363 | 2024-10-21 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 388d6183-9d53-3630-a98d-c0dc77307d9f | -17.7654 | -57.4703 | 2024-10-21 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |


[Clique aqui para ver as próximas entradas](README64.md)
