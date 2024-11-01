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
| 69235b57-f315-3b94-b9c6-c87416839246 | -4.9024 | -47.0357 | 2024-11-01 00:45:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f4eb8445-4cf8-3083-8bac-7cdae5383418 | -4.9209 | -47.0566 | 2024-11-01 00:45:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0720094d-e650-3d0a-83c3-9b9333d0f242 | -4.9211 | -47.0346 | 2024-11-01 00:45:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 00512d9f-6c94-3c23-a733-df4952aa12d3 | -5.2529 | -60.1643 | 2024-11-01 00:45:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| f55bd01e-2b81-3250-b063-001e8c53883a | -6.1039 | -43.9824 | 2024-11-01 00:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 0f0169a9-64a2-307b-9466-5ffb9f4e1087 | -6.1041 | -43.9593 | 2024-11-01 00:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 16fb6cfa-e8b5-3754-a31e-06c1a8428f5a | -6.1043 | -43.9362 | 2024-11-01 00:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 86b7c20d-f187-3f48-9007-227db5b7b325 | -6.1226 | -43.9809 | 2024-11-01 00:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 97baf8a5-1012-36ba-892c-0ce5c824f7de | -6.1229 | -43.9578 | 2024-11-01 00:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 208.8 |
| d878815c-7117-3f16-a8fe-b1b715fb506d | -6.1231 | -43.9347 | 2024-11-01 00:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 6b79d33c-5dd3-3401-bd30-b829eebac15f | -9.4387 | -40.3419 | 2024-11-01 00:45:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 232.6 |
| dbfd1582-1778-397a-87c0-e2845bc09d22 | -9.4391 | -40.3171 | 2024-11-01 00:45:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 287.9 |
| 3dcd9952-9e37-39af-8d9d-a1c9eeeb6413 | -9.4578 | -40.3392 | 2024-11-01 00:45:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 138.1 |
| ce9ffca0-b970-35bd-a02a-8c854e5ea218 | -9.4582 | -40.3143 | 2024-11-01 00:45:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 170.7 |
| 69cf9329-ce1a-34a4-8e6e-889507e64e1b | -10.0885 | -68.3828 | 2024-11-01 00:46:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 592c7885-fd42-3ba4-b048-005aef243146 | -10.6819 | -65.002 | 2024-11-01 00:46:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 047c0477-e2be-3593-b70c-527bf121cf15 | -10.682 | -64.9831 | 2024-11-01 00:46:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 71d83f99-49d0-371f-a50e-41c944e9c7cd | -10.9811 | -45.1104 | 2024-11-01 00:46:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| affae801-6da6-373a-9240-1bdb0ef44103 | -11.0003 | -45.1078 | 2024-11-01 00:46:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d9026a2b-1f19-34ab-bcc3-b3a10316b893 | -13.3655 | -61.3376 | 2024-11-01 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| e8b2be81-4d5b-3171-b661-431d46c417d7 | -16.9008 | -57.5313 | 2024-11-01 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| a297fa2c-73bb-313b-8315-ff1cbc7c0678 | -16.9012 | -57.5108 | 2024-11-01 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 72146226-a94b-3f01-b8f7-48bd86ccab73 | -16.9204 | -57.5291 | 2024-11-01 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 2b77bfe6-d85e-3fe8-b438-412b0d5bf2c6 | -16.9207 | -57.5086 | 2024-11-01 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 06312c72-801e-3873-84fa-8e1c35b46a4a | -17.6467 | -57.5051 | 2024-11-01 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| ca258d8b-374d-375a-99b4-91baac6e089f | -17.6664 | -57.5028 | 2024-11-01 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.8 |
| e531c5e2-4ae0-3afd-94bc-52187353c363 | -22.9568 | -49.2058 | 2024-11-01 00:47:12 | GOES-16 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b9d74371-1b0b-3efe-8c26-13f7ace2bbb7 | -0.6896 | -51.6847 | 2024-11-01 00:55:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 170b9207-c95d-35e8-b616-575d4e844f59 | -1.2292 | -47.7299 | 2024-11-01 00:55:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e45c1212-45d3-3971-b216-5aec9963027b | -1.847 | -52.3285 | 2024-11-01 00:55:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 44d35e50-0151-38a3-a528-00e2ff2eb62f | -1.8471 | -52.308 | 2024-11-01 00:55:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 57a8ef0c-106b-30f2-987d-53e6223bdee5 | -1.8654 | -52.3282 | 2024-11-01 00:55:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 09a32eb4-f081-3163-8839-b436667fcb8c | -1.8654 | -52.3077 | 2024-11-01 00:55:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| a857cc5b-d858-3613-9e37-2c732362f03b | -2.1695 | -48.7252 | 2024-11-01 00:55:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2025d5ff-a9ab-368b-8561-f2d3a0adf7b6 | -2.3545 | -48.678 | 2024-11-01 00:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5ecc4c50-ebe6-3d43-ba97-e1a3f9c3884c | -3.0353 | -49.4901 | 2024-11-01 00:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 225.2 |
| fd37757d-18d1-3d9f-8ffc-9a9a8d8a9d1a | -3.0354 | -49.4688 | 2024-11-01 00:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 256.1 |
| 7f6918dd-1b4d-30c7-80a2-b4536637506e | -3.0538 | -49.4895 | 2024-11-01 00:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 365.3 |
| ba7b1704-66a9-33de-b74f-f40d78b5336c | -3.0539 | -49.4683 | 2024-11-01 00:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 434.0 |
| 0bd26eb4-b11e-39e3-bbbc-28cdad661b83 | -3.054 | -49.4471 | 2024-11-01 00:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b37a39a8-4902-3f8d-8348-fa4122fd75b4 | -3.3385 | -44.0599 | 2024-11-01 00:55:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f056b4cd-9839-36f9-be7f-5ec85c847fb3 | -3.3572 | -44.0591 | 2024-11-01 00:55:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 2c366de9-2004-3883-a8df-2b6072a29058 | -3.5446 | -47.3855 | 2024-11-01 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| db0a3a55-4188-3135-89dc-ee5317c22266 | -3.5631 | -47.3847 | 2024-11-01 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 270.6 |
| 596120b1-4801-332b-867b-c965b9960679 | -3.5632 | -47.3629 | 2024-11-01 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| d4367e62-7ea3-3a56-a2c4-ccf5c3a16241 | -3.5817 | -47.384 | 2024-11-01 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f770f7cc-072c-33d1-b001-82d630843068 | -3.7703 | -43.5323 | 2024-11-01 00:55:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 6d163286-b088-39e4-b568-1a39ef21ca21 | -4.3164 | -45.6241 | 2024-11-01 00:55:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 54e1df40-6b25-3882-8ceb-96859771ab99 | -4.3867 | -43.4757 | 2024-11-01 00:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 498.5 |
| 7d7e341c-daaf-3c80-b63a-c47dfe6d1e03 | -4.3869 | -43.4525 | 2024-11-01 00:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 193.9 |
| 1ce1f112-b50e-357d-b725-4a770a0a8345 | -4.4054 | -43.4746 | 2024-11-01 00:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 328.1 |
| c05a1682-a552-3248-b480-ca493abba768 | -4.4056 | -43.4514 | 2024-11-01 00:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 1d5a1e69-29da-3b2e-89cc-159ae083aad3 | -4.4554 | -44.3477 | 2024-11-01 00:55:31 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4fec62c1-1273-3a1b-a784-4bc2ff0ef535 | -4.4555 | -44.3248 | 2024-11-01 00:55:31 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 27faddd9-1acb-300d-b7d0-531f66e8b259 | -4.9023 | -47.0577 | 2024-11-01 00:55:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 8b55a751-b96d-3484-b271-ada942cca274 | -4.9024 | -47.0357 | 2024-11-01 00:55:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 924c5137-e817-3c82-83d0-709c8df9ed0a | -4.9209 | -47.0566 | 2024-11-01 00:55:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 93.2 |
| bf1a5110-86c5-3943-bb42-0047dccd7af4 | -4.9211 | -47.0346 | 2024-11-01 00:55:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 93.5 |
| f7642ea1-54a9-35d2-8fe3-036247a386a3 | -6.1039 | -43.9824 | 2024-11-01 00:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 33d5ef65-6efc-348b-afbc-e2c7544e3d07 | -6.1041 | -43.9593 | 2024-11-01 00:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| e9e449cd-cb8a-3091-a939-57cf73925587 | -6.1043 | -43.9362 | 2024-11-01 00:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 11df02c7-78ce-3687-9993-384d660d4ccc | -6.1226 | -43.9809 | 2024-11-01 00:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 60765f8e-5cbd-3078-9574-12a32eb486c0 | -6.1229 | -43.9578 | 2024-11-01 00:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 227.6 |
| 510bf2a8-a5c9-353d-b592-77c8fb9b230f | -6.1231 | -43.9347 | 2024-11-01 00:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 29ab767e-623e-37f8-b4b2-ca82b03cd844 | -9.3789 | -35.95 | 2024-11-01 00:55:58 | GOES-16 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.5 |
| b91e9a1e-c01f-322e-83c1-034b1111f583 | -9.4387 | -40.3419 | 2024-11-01 00:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 181.7 |
| 52924eed-2757-314b-910c-1118561e45b8 | -9.4391 | -40.3171 | 2024-11-01 00:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 225.5 |
| 47e0e6f1-aea8-3011-95fb-d1db16ab0ebb | -9.4578 | -40.3392 | 2024-11-01 00:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 111.4 |
| 8814e50f-0829-3bd7-a9c7-aa845b3f4649 | -9.4582 | -40.3143 | 2024-11-01 00:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 140.4 |
| 2e36c823-4ad5-3c20-a20e-6665a6e84dee | -9.8567 | -36.1111 | 2024-11-01 00:56:01 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.5 |
| e92fc964-6a50-3272-8547-ff50fd5395f3 | -10.6819 | -65.002 | 2024-11-01 00:56:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5e418b42-bbe9-3990-9b1d-66c3e9d2c07a | -10.682 | -64.9831 | 2024-11-01 00:56:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| af79b691-d96e-3b6c-8fbf-dd564f856fc4 | -16.9008 | -57.5313 | 2024-11-01 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| de3fd1ad-99f2-34b4-8e7d-e5e56d1bada8 | -16.9012 | -57.5108 | 2024-11-01 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 540d7a06-855d-3072-b72f-eeee2519c862 | -16.9207 | -57.5086 | 2024-11-01 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 000f3bc9-d2ea-3b57-84e7-f056cf850ea3 | -17.6467 | -57.5051 | 2024-11-01 00:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 41cd928c-2adc-3c03-b62f-cb1aec287fd8 | -17.6664 | -57.5028 | 2024-11-01 00:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.9 |
| 491c25a7-339e-3564-b340-b9c7323fd4f6 | -17.6667 | -57.4822 | 2024-11-01 00:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 23a2bb7f-d065-34e9-b8db-4dd4267d1263 | -4.39 | -43.44 | 2024-11-01 01:05:02 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67e13dbf-5616-3eff-bb81-00445ea4d3c2 | -4.39 | -43.49 | 2024-11-01 01:05:02 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07759a40-a3a9-3b8a-adff-d0b0ca74ca10 | -3.56 | -47.4 | 2024-11-01 01:05:07 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58a035a7-9567-3c08-936a-c04625a92b7e | -1.8654 | -52.3282 | 2024-11-01 01:05:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| aa1c7a13-a483-3877-9013-664f5f3cf90d | -1.8654 | -52.3077 | 2024-11-01 01:05:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 09771fba-ca52-3ec2-a59a-6adc47f3e487 | -2.1695 | -48.7252 | 2024-11-01 01:05:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a42fb2bd-0568-3cde-9930-9115ba3da36c | -2.3545 | -48.678 | 2024-11-01 01:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5859f829-85bb-3596-b03a-272aea50ccb8 | -3.0538 | -49.4895 | 2024-11-01 01:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 344.6 |
| 77e185c0-c651-3a4b-973f-fcc7d4adcd30 | -3.0539 | -49.4683 | 2024-11-01 01:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 339.6 |
| 7e66b31a-3a78-34e6-9fcb-0621e0b08b8b | -3.0353 | -49.4901 | 2024-11-01 01:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 259.6 |
| 548f3df7-ce3c-37e8-a6f8-a16007875f1f | -3.0354 | -49.4688 | 2024-11-01 01:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 257.1 |
| 428acce7-f015-31ac-80cf-7c9b8865675e | -3.2719 | -50.3473 | 2024-11-01 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| fca1470f-e2bd-3565-88f1-cd4e9ec273a3 | -3.3572 | -44.0591 | 2024-11-01 01:05:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 6cd988e8-eeb2-335a-81bc-9d18d00761f1 | -3.4012 | -50.3431 | 2024-11-01 01:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 73d6dbbf-306b-354d-9e3a-3b18c4c1f50d | -3.5632 | -47.3629 | 2024-11-01 01:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 9cbb010d-44d2-366b-ae5f-2745385a4a38 | -3.5446 | -47.3855 | 2024-11-01 01:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| b93b87ef-0173-357c-b2f1-49583b9b87bc | -3.563 | -47.4066 | 2024-11-01 01:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c37dfdc2-aca9-36a3-8cd6-2b1e84db1b15 | -3.5631 | -47.3847 | 2024-11-01 01:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 289.1 |
| d76fd151-c6ca-3aa2-9ad4-39ccca66291e | -4.0184 | -45.6616 | 2024-11-01 01:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 97c4cc77-15af-340d-8992-42e027d4a42a | -4.3164 | -45.6241 | 2024-11-01 01:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 8e1c7342-9cd6-3f0a-85ba-ca27be3d56f6 | -4.3867 | -43.4757 | 2024-11-01 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 35977120-a3aa-3fab-aeea-334fffa4fe04 | -4.3869 | -43.4525 | 2024-11-01 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |


[Clique aqui para ver as próximas entradas](README6.md)
