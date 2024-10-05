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
| 0ca4b6c1-4fa8-3548-a687-c651c369d221 | -7.4957 | -44.8311 | 2024-10-05 00:23:24 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bcfb41cd-1fe7-3a78-b34e-8eec8241abd6 | -7.4418 | -44.7272 | 2024-10-05 00:23:25 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1e9b40e-3e24-31df-b115-ce1dfc66e22e | -7.4436 | -44.7351 | 2024-10-05 00:23:25 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c296d682-a27b-37cf-b3d3-0b7222ef0cea | -7.4338 | -44.737301 | 2024-10-05 00:23:25 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f7418536-4b5d-386d-ae81-ffd97fafb73e | -6.8376 | -42.819302 | 2024-10-05 00:23:27 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bfee13f4-7781-3bb2-b49d-43ed50119789 | -6.8392 | -42.826302 | 2024-10-05 00:23:27 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 172d64b1-81c8-3407-8857-7b92ba7b942b | -6.836 | -42.812401 | 2024-10-05 00:23:27 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 40e6a603-96fe-38ad-9ba4-a67ffba36087 | -6.8246 | -42.807701 | 2024-10-05 00:23:28 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e2b0cd26-2dab-3b9c-bf46-68e244f5b85c | -6.8262 | -42.814602 | 2024-10-05 00:23:28 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c158275f-f6d9-37bc-821d-d1fc02cf9175 | -6.8278 | -42.821499 | 2024-10-05 00:23:28 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ac4a0c73-0146-3bc2-8794-db2cd4a6f08c | -6.3199 | -40.923901 | 2024-10-05 00:23:29 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 508a7206-0bbe-3c4e-ab0d-6ed893852f30 | -7.0868 | -44.425999 | 2024-10-05 00:23:29 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8756030b-fb19-3d39-9b8a-753257c1f32f | -7.0884 | -44.433601 | 2024-10-05 00:23:29 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48d7859e-5d99-3200-bd09-4c91ca2e84d4 | -7.1598 | -45.0299 | 2024-10-05 00:23:30 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ce31907-eec6-34a3-acd3-4dff482ed5ff | -7.1616 | -45.037899 | 2024-10-05 00:23:30 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0dfa609-2af5-3dcb-a118-965384a0ad52 | -7.008 | -44.395901 | 2024-10-05 00:23:30 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fbbc23f-f1e2-396f-a81d-a2a1c099d618 | -7.3699 | -46.119999 | 2024-10-05 00:23:31 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff0b1536-7e16-3018-8950-a766016075f7 | -7.3719 | -46.129101 | 2024-10-05 00:23:31 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d72af2a-9b71-363d-9cea-467154656a64 | -7.2755 | -45.784401 | 2024-10-05 00:23:31 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5db5ee72-3eb3-3478-92fb-fa8713e87dc4 | -6.653 | -43.049702 | 2024-10-05 00:23:31 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25f886f1-cf48-3af5-a5e1-44ed2837c266 | -6.6546 | -43.056702 | 2024-10-05 00:23:31 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4fc8ca4-0848-3d2a-87ba-7301f86278ad | -6.6432 | -43.051899 | 2024-10-05 00:23:31 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e0e7f23-fdb8-3868-8a6e-97aca807a3ad | -6.6448 | -43.058899 | 2024-10-05 00:23:31 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4739321-156e-359e-8dfc-026a1b6b629b | -7.456 | -47.169899 | 2024-10-05 00:23:33 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e89ba1a-0fa4-32b3-8515-7e8f81b30d37 | -7.4583 | -47.1805 | 2024-10-05 00:23:33 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7aed46ea-bfa5-3807-ab4d-086e503a189c | -5.1134 | -37.548599 | 2024-10-05 00:23:35 | METOP-C | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 46eb256e-bf64-3b71-bb83-ea64f7f3b262 | -5.116 | -37.5592 | 2024-10-05 00:23:35 | METOP-C | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 715ab8b7-5852-353a-8cb6-82d8c11e1df3 | -5.1185 | -37.569801 | 2024-10-05 00:23:35 | METOP-C | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 016561e6-e587-38dd-9c34-c10063ba8689 | -7.3697 | -47.2439 | 2024-10-05 00:23:35 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c0edbd3-1178-3d9b-8a0c-8cdc013b0223 | -7.3599 | -47.245998 | 2024-10-05 00:23:35 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8160d5e5-723d-3494-abda-d5c023a41e5d | -7.7485 | -49.195801 | 2024-10-05 00:23:35 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| aa756a12-c75e-3c3d-a423-129c19349b6c | -7.7516 | -49.2103 | 2024-10-05 00:23:35 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8b130b62-f24c-341b-8a53-5a206a872ab0 | -6.4631 | -43.348202 | 2024-10-05 00:23:35 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e04bdeac-6fa7-3418-8dcb-a93cd1849045 | -6.4647 | -43.355202 | 2024-10-05 00:23:35 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5434949-5971-3a5f-90bd-c1fe3f4e3cd7 | -5.4643 | -39.116699 | 2024-10-05 00:23:36 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c726b8a5-7521-3246-af2f-9b9bdf159906 | -7.7356 | -49.1833 | 2024-10-05 00:23:36 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 73839871-ec7b-35e0-ab18-ee59669f8774 | -7.7387 | -49.1978 | 2024-10-05 00:23:36 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 0de39b50-2452-3e8b-b528-70fdfaa73d0a | -7.7418 | -49.212399 | 2024-10-05 00:23:36 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8cdb5edf-a222-3909-84fd-2c7eee4fc2dc | -6.7164 | -44.563301 | 2024-10-05 00:23:36 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15bb9328-9c42-39b9-b13c-4d351949027f | -7.7259 | -49.185299 | 2024-10-05 00:23:36 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| aaa16b90-d457-37e7-8ab4-5de61f27f891 | -7.729 | -49.199799 | 2024-10-05 00:23:36 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 914e3af8-d310-3ff6-b7d2-f2b0e005a403 | -7.7321 | -49.214401 | 2024-10-05 00:23:36 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6c7ac155-6475-3530-b9e6-edb313948e0b | -7.7192 | -49.201801 | 2024-10-05 00:23:36 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 409f5bf9-c08b-3603-a79f-e3c2385592c2 | -7.7223 | -49.2164 | 2024-10-05 00:23:36 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 395c1632-2363-3380-835b-bc8b41f15f1a | -6.4676 | -43.413399 | 2024-10-05 00:23:36 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 196f70c8-ece3-3d05-95de-ba04e9c7a319 | -6.4692 | -43.420399 | 2024-10-05 00:23:36 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88c5978c-663d-30df-a8a4-44f1d890374f | -6.2772 | -42.756802 | 2024-10-05 00:23:36 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 48198f35-b823-377e-9c36-f2faa6a6e32a | -6.577 | -44.1712 | 2024-10-05 00:23:37 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0138a8b-5958-3d65-812a-5bce711f6706 | -6.5786 | -44.1786 | 2024-10-05 00:23:37 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd3149d-5074-3773-a888-cb14deea8b5e | -6.5689 | -44.2271 | 2024-10-05 00:23:37 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7409247c-7cb7-3c2a-be0c-e7ff3f8d928b | -6.5706 | -44.234402 | 2024-10-05 00:23:37 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e871c1c-0eb2-3f0c-91e6-9e777b0b1c2a | -6.2762 | -43.250599 | 2024-10-05 00:23:38 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7c5fb81-23b3-30a1-99c1-46536a1cd03c | -6.3171 | -43.476398 | 2024-10-05 00:23:38 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c675148-9145-3708-8480-d6dd82d7f1bb | -7.7702 | -50.2118 | 2024-10-05 00:23:39 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9465d591-1ac6-3a57-ac57-b524e1d6dd09 | -6.8799 | -46.130798 | 2024-10-05 00:23:39 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a70746a8-dd26-3713-b9aa-62464c982c11 | -6.1977 | -43.268101 | 2024-10-05 00:23:39 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd5a212-d058-330e-95d5-fc4b3af293f7 | -6.1993 | -43.275101 | 2024-10-05 00:23:39 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9bb18ec-a434-34c7-a5ae-912e43583752 | -6.4196 | -44.478298 | 2024-10-05 00:23:40 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65ee321b-01cf-369e-8c8a-c0291d09b121 | -6.1764 | -44.129501 | 2024-10-05 00:23:43 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3561927e-30ce-3846-9898-2d5167d06240 | -6.165 | -44.124401 | 2024-10-05 00:23:43 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 067b28d7-c087-3913-8495-680f80267b29 | -6.1568 | -44.1339 | 2024-10-05 00:23:43 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38e7d559-90c5-3015-8de3-dce4eec32e52 | -6.1584 | -44.141102 | 2024-10-05 00:23:43 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb33f205-51f2-3994-b1d5-1af081ecc066 | -6.1486 | -44.143299 | 2024-10-05 00:23:43 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec54b72a-16c1-390c-aa1a-bf70897a5ac4 | -4.8437 | -38.3661 | 2024-10-05 00:23:43 | METOP-C | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8397b725-28b2-35e1-964d-b0717151fbc1 | -6.3411 | -45.691002 | 2024-10-05 00:23:46 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8966a1f8-6da4-30fc-ab3f-a8fb3d6c42bb | -6.3275 | -45.676201 | 2024-10-05 00:23:46 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b213c525-699b-3c96-add9-2346db0fb50f | -6.3294 | -45.684601 | 2024-10-05 00:23:46 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53b59bf8-852f-36de-b531-dbd630576bff | -6.3313 | -45.6931 | 2024-10-05 00:23:46 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1ff8afe-493a-32bc-82f5-6eec7b17de72 | -5.8752 | -43.707901 | 2024-10-05 00:23:46 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08bf2343-8b6e-3072-9aa1-2768207f60b8 | -5.8768 | -43.714901 | 2024-10-05 00:23:46 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28f8db0a-746b-3a9a-ae05-46a76002c25b | -6.0775 | -44.695999 | 2024-10-05 00:23:47 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e04c4df4-8a98-3bb8-a7e1-f024ace35b18 | -6.0792 | -44.703602 | 2024-10-05 00:23:47 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 651bb742-b803-3a51-af45-b9b8e47f9bd7 | -6.066 | -44.690601 | 2024-10-05 00:23:47 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f11ebb16-d45b-33e6-8f82-a0f11d1bc867 | -6.0677 | -44.6982 | 2024-10-05 00:23:47 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22d5a308-be7c-36de-9bcb-b56240eea334 | -6.1687 | -45.424702 | 2024-10-05 00:23:48 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd6a97d0-9ecb-3b2d-8279-eb5de753784b | -6.1705 | -45.4328 | 2024-10-05 00:23:48 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7336d7d-31fd-3e9a-924d-523332f04385 | -6.1723 | -45.441002 | 2024-10-05 00:23:48 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b429a7cd-e466-3781-b55a-82c83887d84f | -5.5383 | -42.771099 | 2024-10-05 00:23:48 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bf2ddcc2-64ff-377a-9776-b306b4580d7f | -5.5399 | -42.778 | 2024-10-05 00:23:48 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bb4e18e6-325b-348a-bd8f-460a3d491080 | -5.5415 | -42.784801 | 2024-10-05 00:23:48 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 41ce7afa-ee5b-384e-aadf-eb229c45755f | -5.5317 | -42.786999 | 2024-10-05 00:23:48 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 193dcbeb-1325-3434-8dc7-f204a053af6c | -5.8235 | -44.116501 | 2024-10-05 00:23:49 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65e52e74-07d6-3e2b-a9bb-4b25b3621ec5 | -5.8251 | -44.123699 | 2024-10-05 00:23:49 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd4150d6-62d2-32c4-acd1-15d7922024f6 | -5.8267 | -44.130901 | 2024-10-05 00:23:49 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a3e234a-ed3b-37ea-9db6-311bbbacfef9 | -5.812 | -44.111401 | 2024-10-05 00:23:49 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab889670-2715-3ac5-b2e0-86e2149e852f | -5.8137 | -44.118599 | 2024-10-05 00:23:49 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6bec3b0-e918-3206-959b-59a10670e52e | -5.8153 | -44.125801 | 2024-10-05 00:23:49 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6fe3017-38a7-3e3c-bb07-e922480af5bf | -5.8169 | -44.132999 | 2024-10-05 00:23:49 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3deaccf0-98e0-3f6e-a15a-8f050ae06dd3 | -5.5203 | -42.782398 | 2024-10-05 00:23:49 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b668cf61-aa62-3c7c-b05f-aed66d28f18d | -6.1228 | -46.418701 | 2024-10-05 00:23:52 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e5b70e4-dbd4-35d0-9a2b-39bf192d4b71 | -5.3982 | -43.1054 | 2024-10-05 00:23:52 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58a81309-ea1b-36e6-b8bd-12e27c72224a | -5.3998 | -43.112202 | 2024-10-05 00:23:52 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a849865-4aaf-3839-8a2d-a4847b575ae7 | -5.7119 | -44.808399 | 2024-10-05 00:23:53 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce020e4-c7ac-3135-92b3-e8cd27c73933 | -5.5262 | -44.3041 | 2024-10-05 00:23:54 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 391e2cdc-53f7-370f-b406-e0e24f65ef44 | -5.5278 | -44.311298 | 2024-10-05 00:23:54 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05a08368-0fa8-3271-9183-dcbf68e5d0f0 | -5.5294 | -44.3186 | 2024-10-05 00:23:54 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1681d80-8270-35a9-baef-7eb21a6a50a5 | -5.4446 | -44.034599 | 2024-10-05 00:23:54 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26dc7c10-33c9-3ef0-a932-ed835974b9db | -5.4462 | -44.041801 | 2024-10-05 00:23:54 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 943f38bd-d765-3ee2-aa95-05b50202a629 | -5.9778 | -46.644299 | 2024-10-05 00:23:55 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53663d52-1eee-3891-bd7f-ab05c1b1b792 | -5.8848 | -46.271599 | 2024-10-05 00:23:55 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
