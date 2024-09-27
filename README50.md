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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b0d9aa5-7451-3045-8174-cbd02395b22f | -11.09043 | -46.16542 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e769e40b-47e8-365d-9d06-a17b630947d3 | -11.0876 | -46.15261 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04aedf82-a9c4-3227-94f5-978263c1f191 | -11.08706 | -46.15555 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffac444a-b92d-35bf-a6a4-470b02bb6892 | -11.08651 | -46.1585 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0d4ba9d-3b3c-3b82-b20f-94bfc660b035 | -11.52026 | -47.42044 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd0523c4-524f-376b-8d95-980a87af81f8 | -11.5196 | -47.42392 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfe5571d-d85d-3240-9cf5-5231b30578f6 | -11.27536 | -47.13297 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e61afd43-e865-3549-ad30-98c0c4f40118 | -11.27228 | -47.13427 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c43ed62-16dc-383a-aae5-23a39da2ad49 | -11.26628 | -47.13676 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e973ef5-0a3d-31da-87d9-eb17bf3242d2 | -11.25817 | -47.12093 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba887f87-5f68-30d9-8ec1-14ee48f9a72f | -11.25413 | -47.11298 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 972d50df-1f1d-3113-9989-1dc4e1ce61f3 | -11.25348 | -47.11644 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ca1420cc-dd95-35c7-a997-1c4c4365954a | -11.25283 | -47.11989 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3ee16b32-f7c7-3da4-98ac-200230467566 | -11.25218 | -47.12333 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8de7246b-8f0d-3011-b97e-62ede2f12437 | -11.25154 | -47.12674 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d9cd60ab-430b-341b-b96b-d60d5f64dd65 | -11.24816 | -47.11529 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e74ea3dd-ebea-3372-b836-bd376cf9d21f | -11.24751 | -47.11875 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 748216f0-9b91-3bf1-b161-86c42d4b61a0 | -11.24686 | -47.1222 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c4e61a98-dc42-3430-ae19-7c1a82120831 | -11.24622 | -47.12561 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 30f9fcc8-2466-3cd5-a17d-b1938734335c | -11.24557 | -47.12904 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44a6c9a2-ff5e-3d4d-8562-ea4492e993f5 | -11.24154 | -47.12105 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6662f5ff-5c2e-3135-a221-cb9fe769a8c9 | -11.24088 | -47.12452 | 2024-09-27 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f07d3ee-d8fa-3e3a-9aa5-d9f1d6bb9d5e | -13.48052 | -48.03261 | 2024-09-27 03:47:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3eb5375e-8202-3306-827e-e8f1c3141aed | -13.47989 | -48.03582 | 2024-09-27 03:47:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2c0fa03-a88c-31e4-89be-1cf184ad7356 | -13.80968 | -48.12987 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8500f02-2340-3f0c-83c2-ac0afeb3cc70 | -13.8087 | -48.13473 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b0d9233-981c-30a8-b41b-6415c7be97f4 | -13.80845 | -48.1317 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84baac74-1eab-3306-9c04-cabfbae43eca | -13.80751 | -48.1366 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ede4c2af-8844-3980-9c87-8e007e90200c | -13.80398 | -48.13006 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bacf0752-aa3a-3960-afc2-bffec632cce8 | -13.80296 | -48.13509 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a535c802-3056-39f4-974b-329c95fedcc7 | -13.80275 | -48.13198 | 2024-09-27 03:47:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c7ca791-dc4e-31c7-9766-913b6cbbdd05 | -13.7287 | -47.58748 | 2024-09-27 03:47:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a16b83b-4b62-32fe-aad3-aa2d4a535139 | -10.7115 | -48.75954 | 2024-09-27 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30a5ec4e-ec48-378d-9b39-b92a0d512b0e | -10.70497 | -48.57171 | 2024-09-27 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e25cf1b-c7b8-3a42-add3-f12fbc82a1bf | -11.68476 | -47.84187 | 2024-09-27 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b06204f-1ee8-3259-a63a-5daeaa7ec18b | -11.68383 | -47.84006 | 2024-09-27 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0685fc2b-2f1d-371c-b46a-6627947795c4 | -11.67923 | -47.84065 | 2024-09-27 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 360985d5-f119-3b44-92c7-7bd240c2f004 | -11.51941 | -47.8403 | 2024-09-27 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb9fe9fd-a2d8-34da-9558-55e65d12a99a | -11.51869 | -47.84404 | 2024-09-27 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67b8cf02-0951-3e93-80c8-9f84c0595899 | -11.51462 | -47.83524 | 2024-09-27 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78469b84-62e6-3679-b5a5-5dee03ecec56 | -12.67061 | -48.06656 | 2024-09-27 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16cde87a-e58a-3f15-a999-ac11b0badd8c | -12.66582 | -48.06166 | 2024-09-27 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96c5acd9-efb3-3400-bdb1-94c624dff49b | -12.6651 | -48.06535 | 2024-09-27 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64d00e80-dddf-31ba-8cc9-d5206dac4db9 | -12.47359 | -47.96769 | 2024-09-27 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34d678eb-ba31-3819-9baa-2f72b89801fd | -12.46809 | -47.96651 | 2024-09-27 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7b08ec9-14f5-34bf-800f-d8b8d5c4bbb1 | -12.46737 | -47.97019 | 2024-09-27 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d3bc9ae-0eb5-3a80-ace7-65949c59860e | -12.46664 | -47.97388 | 2024-09-27 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59378cae-a9e4-3093-8d32-3ffd493ffa37 | -12.46187 | -47.96899 | 2024-09-27 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 999d6ca3-aed4-363e-bb5f-409c657bf3af | -12.46114 | -47.97269 | 2024-09-27 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6309de03-dbfe-331b-9c0a-118ca3b07c58 | -13.46908 | -48.58299 | 2024-09-27 03:47:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c92ee6a1-1164-3025-8cdb-9f4f721de8ef | -13.46345 | -48.58184 | 2024-09-27 03:47:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ccdf677-9ba2-36c7-909d-3348f5218ad8 | -10.63384 | -49.90703 | 2024-09-27 03:47:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e13032f5-7cdd-3d4b-ac19-33966cb28ffd | -10.63278 | -49.91241 | 2024-09-27 03:47:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d642be32-95d9-3d3f-ba13-a73c179a2f7d | -12.19527 | -50.85191 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 920b1524-5429-353f-925b-2e5152b7ca77 | -12.19405 | -50.85777 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 712d8180-505a-3c20-ad42-bf323e9dde6a | -12.19097 | -50.85165 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5782bc4b-6a40-35fa-ad67-d4c88cf0b3b9 | -12.18869 | -50.85044 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c5b715a-5cdd-3ffb-a577-ebdf009ebf34 | -12.18823 | -50.81979 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f25065be-6391-328a-99a2-f915e9b74eef | -12.18579 | -50.83147 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d7bc3583-1a6f-36f0-ade8-2d42055ef8e9 | -12.18558 | -50.8443 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f4ecb76-c7c3-33ef-8ac0-265f5ce36e68 | -12.18495 | -50.81355 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 90d3186e-7785-3e67-a44b-5aa3fecf5cd2 | -12.18457 | -50.83728 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 54976ccb-fef4-3e60-87f0-1da69259193f | -12.18439 | -50.85017 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60e2f6ef-00e6-3c76-910c-3ee1f7e19221 | -12.18376 | -50.81939 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| baea4018-728b-3930-ac76-79119bdfe68d | -12.18334 | -50.84314 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85a1c4b5-b5a4-3be9-8a7c-41f0b527657c | -12.18289 | -50.81251 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 959081af-0fe0-36d0-83f4-a2c739e32bed | -12.18257 | -50.82524 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1c2202d-fc4c-3416-8c41-ea74034e8d0f | -12.18211 | -50.84901 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37215649-0301-3201-a5d7-e54f12e81757 | -12.18166 | -50.81833 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9a043c4-63c8-3fc3-a510-7c5cc268cd35 | -12.18138 | -50.8311 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b5c01f3d-eee1-3bd6-8c39-b8e77714baad | -12.18044 | -50.82416 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2483f031-05bc-316a-9208-ffb1a444b85f | -12.17921 | -50.83001 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 703ff6d5-983c-3c9c-8e1e-d78c46bd2fba | -12.17781 | -50.8487 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0352d8e-cfd4-3288-899e-41f02f674043 | -12.17719 | -50.81791 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2e3a6f8-a873-31f3-91c0-115fd33ed9c3 | -12.17632 | -50.81105 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5439487-785e-3164-9e1b-8cbd31b0e666 | -12.176 | -50.82377 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7ab7b95-6e7c-35a7-8324-46b1b957e3c1 | -12.17553 | -50.84755 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc18b2c7-6bc1-3d31-b08f-a65746b4ac8b | -12.17387 | -50.82272 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0997cd2-acdb-3906-b245-134b3e25492c | -12.173 | -50.80478 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 98c27b09-0507-3d4b-92e2-361fd85e1966 | -12.17263 | -50.82858 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30bc3242-8617-3fa1-91e4-88840bfe8b5f | -12.17181 | -50.81061 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 26d8ec30-c1b8-3cec-a5ce-ae81225f3c8a | -12.17098 | -50.8038 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6547cc73-9ff4-3c51-afb1-8e36fea6cdeb | -12.16975 | -50.80962 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c7e0e03-dae3-3743-8413-76367be36aae | -12.16943 | -50.82229 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69fad4b7-79df-3e54-858d-0c10e5dedaba | -12.16823 | -50.82816 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33b0ef0e-716f-3f24-a167-7d49d5fcd72b | -12.16729 | -50.82127 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50a1c4c4-abc1-3f74-82eb-4c018f776fb5 | -12.16704 | -50.83401 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82860665-76e7-3c61-b44c-852db040ddac | -12.16606 | -50.82712 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfe009b9-141a-335b-9267-58dec54b176c | -12.16524 | -50.80913 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97a916aa-47b1-3afc-a9f5-9c80cb517406 | -12.16483 | -50.83295 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f2237bd-b0d2-330b-9938-e4cb82c9bc0c | -12.16318 | -50.80817 | 2024-09-27 03:47:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| edbab1fe-ad10-3e8c-b39e-72f17c4f8091 | -11.59345 | -50.51056 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2620f3b6-5742-3339-847b-fce744980ad3 | -11.58811 | -50.50346 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0635fff6-29ae-3743-88d7-3a5496329997 | -11.16624 | -49.73227 | 2024-09-27 03:47:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 886c6b8f-5b74-3840-84b1-1484ac8a6656 | -11.15996 | -49.73091 | 2024-09-27 03:47:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 56b41540-d4bc-3291-bc42-fc15a8c61a6e | -12.47433 | -50.41748 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a59df7d0-b062-31a7-b448-f39b5841ff23 | -12.47404 | -50.41441 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bbb46e6-ee36-3e89-9baa-b542d5409123 | -12.4732 | -50.42289 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79d3f2a8-7601-34a2-93ae-47fb3ef1945f | -12.47294 | -50.41984 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43c5fae5-b3a6-3051-81ff-0a442b0e151d | -12.47207 | -50.4283 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README51.md)
