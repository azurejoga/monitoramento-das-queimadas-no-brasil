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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b91fc49-1bf5-3b99-bf73-a2450b44179f | -9.1895 | -59.6364 | 2025-08-23 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 006a30f8-92c5-3632-bab3-ef146ba8457a | -19.7293 | -45.7124 | 2025-08-23 00:40:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 52.1 |
| ee347756-94c1-3085-aed3-e0cd168c758d | -7.0164 | -44.6413 | 2025-08-23 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 703dddd6-2400-3a91-9ad5-597500553d64 | -8.8921 | -62.4297 | 2025-08-23 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 155f687e-2aeb-3357-8c95-6ae480e9f687 | -5.7614 | -57.6002 | 2025-08-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 166d2d8d-63fe-33eb-965e-f0480952b292 | -9.1712 | -59.5987 | 2025-08-23 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 9e5b3f02-6637-31ce-8c2a-96ed019aadc6 | -6.4138 | -41.2132 | 2025-08-23 00:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 161.9 |
| e6dc98f0-3c8c-3991-a218-c54f905db21b | -9.518 | -60.5268 | 2025-08-23 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 243.0 |
| 5c19eab6-7ccc-32d3-b35c-ca49739bc3cd | -5.7431 | -57.5814 | 2025-08-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c8553fdc-6b14-3bf8-b9d7-ac8ab9ff2f9b | -15.0186 | -54.8735 | 2025-08-23 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 3480e506-c531-341d-b7ba-04f5ffb88c28 | -14.684 | -56.6136 | 2025-08-23 00:40:00 | GOES-19 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 677e98e3-abd3-3b8d-95a1-a77522052bf8 | -9.4449 | -47.6585 | 2025-08-23 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 3130c691-7261-37e7-acdd-87bccf188a38 | -9.1909 | -59.4619 | 2025-08-23 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f6e7d410-5a4c-3565-aa51-b4345bdf6245 | -6.5781 | -59.871 | 2025-08-23 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1b21a429-5169-3898-80c3-54e681e1f0e2 | -17.2757 | -46.7538 | 2025-08-23 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 87.8 |
| e85b8189-9788-33b8-9fa1-f98abc3bfb96 | -7.8131 | -63.5468 | 2025-08-23 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6e66e07c-49a2-3e78-a574-510a3fb66889 | -9.1711 | -59.618 | 2025-08-23 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 28b17482-383e-374a-9143-44b394f55bc0 | -5.7429 | -57.6009 | 2025-08-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 6daeb745-ac8b-3f51-9256-ec5eec282c07 | -7.2491 | -39.275 | 2025-08-23 00:40:00 | GOES-19 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 62.4 |
| f58adaf5-7e88-3331-985c-03d3991ffe8d | -3.444 | -49.0297 | 2025-08-23 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 7664b7f4-fed4-3d8b-8b7f-38ded31e6720 | -10.6122 | -55.413 | 2025-08-23 00:40:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 0bc9ef88-abbc-3a9b-8909-44f2bc82c92a | -6.4327 | -41.2114 | 2025-08-23 00:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 178.8 |
| f97381be-7900-3646-8e44-3c332402a436 | -9.1897 | -59.6171 | 2025-08-23 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 6b7c08d5-03be-3767-b9d5-5e7e2f803e3a | -11.1208 | -44.7449 | 2025-08-23 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 7b12a40a-2ece-3322-97e5-db2b343fea52 | -17.5979 | -46.5715 | 2025-08-23 00:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 101.7 |
| dea3fc15-8e1f-3ca5-9731-dca38839cb2c | -9.5179 | -60.5461 | 2025-08-23 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 00cc4b41-475f-3e85-9c30-0c32f72eac09 | -7.813 | -63.5656 | 2025-08-23 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 38876b2d-be0d-369a-8f74-d3453abf2473 | -9.2095 | -59.4609 | 2025-08-23 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5cc706b6-e6eb-349c-989c-b9a195377c33 | -6.4324 | -41.2357 | 2025-08-23 00:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| e7e7bf85-be14-3a3c-904a-7cd1c70ffaaf | -6.8733 | -59.8213 | 2025-08-23 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 23797109-af2d-3540-ac5b-aecc3cc9943a | -3.4439 | -49.051 | 2025-08-23 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 6f232091-c69e-3d7e-996b-07fa43828316 | -5.7615 | -57.5807 | 2025-08-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c0fc04bb-0f19-3872-8097-761b22864dad | -17.2751 | -46.777 | 2025-08-23 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 956928b5-97b2-373c-81ef-a704e1103980 | -9.5181 | -60.5075 | 2025-08-23 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 160.7 |
| ab6bf003-7c43-3ed7-b4b8-1f228e108d38 | -17.5785 | -46.5523 | 2025-08-23 00:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ecf186b1-66bb-3b40-bd4c-170d24fecd90 | -3.444 | -49.0297 | 2025-08-23 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| bc0a595a-7ef0-3857-969c-48f5d4ae1619 | -9.1895 | -59.6364 | 2025-08-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| d873de32-d1ba-3218-b285-9690c6b38350 | -6.4138 | -41.2132 | 2025-08-23 00:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 3d3b7b74-8989-30a8-91e8-0c2117102a57 | -19.7293 | -45.7124 | 2025-08-23 00:50:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8addcc78-41a3-3a6a-ad03-37f87b76f3fd | -19.73 | -45.6884 | 2025-08-23 00:50:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 123.2 |
| b429d59e-bcf7-3854-a17d-788c48c12c4f | -10.6122 | -55.413 | 2025-08-23 00:50:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a6624f14-7852-32dd-a843-861371103108 | -7.8131 | -63.5468 | 2025-08-23 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 712b9b1d-f391-34cf-a445-bec657633ab4 | -9.2391 | -60.4834 | 2025-08-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 8375e5ab-7e39-332b-8ad9-096812a870b1 | -9.1897 | -59.6171 | 2025-08-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| c594ac04-7aea-34c6-a146-2e9edd0681a1 | -6.5781 | -59.871 | 2025-08-23 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6c2ffa94-d574-3558-822c-3948325e715a | -9.4449 | -47.6585 | 2025-08-23 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 2dcb90a5-2960-3b69-99e4-a32cf04e7067 | -11.1816 | -55.0211 | 2025-08-23 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| da21a350-eee9-30b4-9939-bb40b99a6445 | -5.7431 | -57.5814 | 2025-08-23 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 5900ccbb-c3a2-3060-b0b4-37810f0e54c4 | -7.0164 | -44.6413 | 2025-08-23 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 290d6398-c51b-3f48-b0be-af00c4a9a682 | -14.665 | -56.5952 | 2025-08-23 00:50:00 | GOES-19 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 12c243e0-e2ca-365d-b242-cade2954c17b | -11.2005 | -55.0195 | 2025-08-23 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 972502f3-8a07-38de-a86a-0560076a4178 | -9.1909 | -59.4619 | 2025-08-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 97e08784-4f81-3b4c-af49-80eff9627766 | -5.0992 | -43.2211 | 2025-08-23 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 2dc7596c-2575-3d71-941d-8fe4cd56295e | -17.2757 | -46.7538 | 2025-08-23 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c2809861-d3a9-3fbe-b68a-73bbe118698f | -17.5979 | -46.5715 | 2025-08-23 00:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 82f1fce3-f798-3364-b2e7-bf0a3f06a2b0 | -14.3126 | -58.5431 | 2025-08-23 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 13ecbc06-7ad6-3a00-84ef-7b68ef34d6e6 | -6.4327 | -41.2114 | 2025-08-23 00:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 138.1 |
| 6d4ddb96-6e67-3dd1-a852-505092971344 | -14.3317 | -58.5414 | 2025-08-23 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 31120cb2-abc1-374f-8f30-97ca5850e603 | -18.9689 | -46.9043 | 2025-08-23 00:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d418dfc0-ef44-3dbc-8b8a-b5cfa8ef5dd8 | -20.097 | -47.7676 | 2025-08-23 00:50:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 2872fae1-04d2-34b4-acf7-e0dc46821aa0 | -14.684 | -56.6136 | 2025-08-23 00:50:00 | GOES-19 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ee5d04a8-cdbb-3500-bf95-8ac25702f788 | -9.2083 | -59.6161 | 2025-08-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 076c5dd2-c801-3a1e-81c1-da6ab81751da | -9.1712 | -59.5987 | 2025-08-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 135c4427-8a3a-333f-a7af-9d8823d5bae9 | -7.813 | -63.5656 | 2025-08-23 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 8360244c-0257-3b17-89fa-869743cd19c5 | -17.2751 | -46.777 | 2025-08-23 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 71.9 |
| a9483ea3-1f54-3e01-a91a-e7d211757fd8 | -18.9683 | -46.9278 | 2025-08-23 00:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 46.9 |
| e610d6e6-9284-3434-8ecc-8ac91251920c | -15.0186 | -54.8735 | 2025-08-23 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| b84c8420-f178-35a1-9db6-d8c671613fe3 | -8.8921 | -62.4297 | 2025-08-23 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 93.4 |
| d8825e13-3552-33a7-8aa3-165bcd859df1 | -12.9921 | -45.2252 | 2025-08-23 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 4f14d198-75ed-37a1-a316-01620c8efb76 | -17.5985 | -46.5481 | 2025-08-23 00:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 44bfaa1c-eba0-35e9-ac37-80df0222e581 | -14.3123 | -58.5631 | 2025-08-23 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 928856cf-738b-39fe-bb48-65f0825fc382 | -7.0352 | -44.6396 | 2025-08-23 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| c10ead26-d6c9-3de4-a132-66842838a19f | -9.1711 | -59.618 | 2025-08-23 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 709fad30-569a-3460-a098-c66e7c2406e7 | -3.4439 | -49.051 | 2025-08-23 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| e13023be-bdb0-360c-b3d0-030f348190e8 | -17.5785 | -46.5523 | 2025-08-23 00:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 3f048308-11c0-305e-8ce7-016d3a52fd83 | -9.2083 | -59.6161 | 2025-08-23 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e74d1f1a-4da8-3b6f-afd0-484237795a65 | -9.5179 | -60.5461 | 2025-08-23 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 1cac30b5-b010-3970-90ef-7ba7e7813496 | -9.518 | -60.5268 | 2025-08-23 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 213.3 |
| 29103d13-48b8-319e-a104-1500acebd413 | -17.5985 | -46.5481 | 2025-08-23 01:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 0dd8bf7a-967e-3328-9627-7cdc209b5578 | -17.2757 | -46.7538 | 2025-08-23 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 107.9 |
| e4eba508-7ee7-3d97-abe1-c4a629abf68e | -14.6843 | -56.5932 | 2025-08-23 01:00:00 | GOES-19 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| b858ac11-3a3e-3881-a30d-c8efadc800b9 | -20.097 | -47.7676 | 2025-08-23 01:00:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 54.2 |
| ab02aca8-18dc-3593-9436-207ad1b05d18 | -9.5181 | -60.5075 | 2025-08-23 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 6948e284-58f5-33bb-8740-98767ff55f85 | -9.4449 | -47.6585 | 2025-08-23 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| d21d1d95-7512-3241-ac52-8f6307faaed3 | -18.9683 | -46.9278 | 2025-08-23 01:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 8ec179e4-88f8-329b-9e19-48e77d754a34 | -17.5785 | -46.5523 | 2025-08-23 01:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 026d5c79-89b2-3423-82e0-e0ff62a4b3c8 | -18.9689 | -46.9043 | 2025-08-23 01:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| afafd17a-0360-34fb-a389-babce37605d1 | -3.4439 | -49.051 | 2025-08-23 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 24fd59c1-6175-365f-8d87-d0bb630d8e1d | -8.8921 | -62.4297 | 2025-08-23 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 5ef02a44-c887-349a-9e4d-e42e5819462b | -9.1897 | -59.6171 | 2025-08-23 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 65d8179d-b8a6-3d99-a25c-c84bcaefd254 | -17.5979 | -46.5715 | 2025-08-23 01:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 3019adf0-949f-3491-a0b1-db8a6230f6bc | -7.813 | -63.5656 | 2025-08-23 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 138.3 |
| a6c4bd55-2af1-37d7-babc-6bcbc993b8e1 | -19.7293 | -45.7124 | 2025-08-23 01:00:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 47724e5d-bc4d-3b69-90f7-80bc496012aa | -5.7429 | -57.6009 | 2025-08-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 431348cd-a55b-32c9-9434-bfb332f9fbd7 | -7.0349 | -44.6625 | 2025-08-23 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b7200dba-83b0-3a96-8da7-c0308db8ea0b | -7.8131 | -63.5468 | 2025-08-23 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 18c019ed-af00-346d-a941-7d3338131265 | -5.7431 | -57.5814 | 2025-08-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 1503d788-c948-31f5-a871-f9990affcb51 | -7.0352 | -44.6396 | 2025-08-23 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 25a06094-0fab-3d99-a0b4-ef00f03c54e6 | -19.73 | -45.6884 | 2025-08-23 01:00:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 127.0 |
| be1b6808-9242-3a36-84be-8a2c2ad9134d | -6.4138 | -41.2132 | 2025-08-23 01:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |


[Clique aqui para ver as próximas entradas](README7.md)
