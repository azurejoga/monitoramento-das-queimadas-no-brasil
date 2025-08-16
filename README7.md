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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78340bd6-6fd4-3674-b438-0404518ccaf0 | -7.0612 | -59.2358 | 2025-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a7289b61-0d7f-3676-9916-5e3c7081e274 | -8.9706 | -61.7224 | 2025-08-16 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 1902c48e-40ee-3895-9e93-c7e4549bd717 | -13.127 | -57.1092 | 2025-08-16 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 1aff888c-dd99-3889-9bfd-9c6b69363e4c | -4.9118 | -43.257 | 2025-08-16 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 13cc9830-5ac1-36e2-a537-8a2b2dd44fff | -11.2599 | -50.4553 | 2025-08-16 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 591aba8a-a937-398f-b442-42f4a1d6a273 | -4.9305 | -43.2558 | 2025-08-16 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| b23f8786-5d19-3ed1-8847-228636e9ccf5 | -14.9435 | -54.7374 | 2025-08-16 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| d969d3ce-852b-3c1e-a4ca-6a89cbd3fedb | -11.2593 | -50.4981 | 2025-08-16 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 7a2d615c-1659-3c4e-acd6-794b8cfedf6c | -8.9708 | -61.7033 | 2025-08-16 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 118.3 |
| e8affaa3-c1a5-3253-8709-0f6416c326f0 | -17.615 | -46.684 | 2025-08-16 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 39.9 |
| d224338c-8b3a-37f5-93ea-126ace7ede74 | -6.7995 | -59.8242 | 2025-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f276b2c8-40f7-317b-b07f-a3e6bf431fb9 | -14.9438 | -54.7166 | 2025-08-16 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 162.4 |
| d6054ea5-c956-386d-b7bd-1bd996ffe99d | -4.9116 | -43.2803 | 2025-08-16 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 79bb68f2-7322-33db-aae2-c1b48b07b399 | -7.0796 | -59.2351 | 2025-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 656ada3c-9cd7-3233-93e7-a443527165e6 | -14.9628 | -54.7351 | 2025-08-16 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 1c9167a0-ec76-39e2-b0c4-6af1ca685dcc | -7.9148 | -61.7478 | 2025-08-16 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d486b3b7-a108-3f06-a5f2-eb5806afe3b4 | -6.9302 | -59.5497 | 2025-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 215a01d0-1509-3bba-bf42-f6a19f9bbebb | -7.0981 | -59.2343 | 2025-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 028b96a4-0126-3918-80c4-1d56ab1d23fa | -8.9657 | -61.6763 | 2025-08-16 00:47:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 80a2bfe5-ce5b-36bf-8a85-b3a5b37fcb13 | -18.519699 | -50.752399 | 2025-08-16 00:47:00 | METOP-B | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 450aa703-7c25-3569-b815-5ced764c1d63 | -12.5934 | -46.930801 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7483dd8-86a1-3166-a109-6252abbe4e6a | -8.9823 | -60.505699 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48b2e5e0-0f7f-361c-9a0f-113da06a76cb | -16.238701 | -51.122101 | 2025-08-16 00:47:00 | METOP-B | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f17ba5ae-bfe8-376e-9e09-2f7f35c38e86 | -13.1254 | -57.158001 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 188f6416-9f32-3530-a8e2-1b2d4c28afc5 | -7.5045 | -63.8027 | 2025-08-16 00:47:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d7efa8fe-8c1d-33ea-ac7f-b3203904729d | -9.1702 | -58.909199 | 2025-08-16 00:47:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3eb7d6c-db56-3155-9f38-f0cf5d83b220 | -11.3503 | -55.431 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9077ee5c-2636-37e6-9a38-5973201353de | -8.9921 | -60.503601 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eeee3322-5fc1-38f6-87d7-f2ab53c94a00 | -7.9506 | -63.208099 | 2025-08-16 00:47:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87916b0c-5aa2-3685-93cb-95981fb13417 | -13.1367 | -57.1628 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78a21a52-07da-3ebf-bc37-b19f018e0e2f | -12.6085 | -46.9492 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 644c6184-966e-3aab-b286-d0a4a77e8add | -7.0445 | -59.6203 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee210fd-fa64-3ae2-9e2a-d3c0d952aef9 | -9.2267 | -59.640701 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5aada11a-9ef4-35e4-ae9a-925ffa3d946b | -8.6877 | -64.201103 | 2025-08-16 00:47:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5d68183-bf19-37a2-b5c5-b1c92f6f15c3 | -8.9082 | -60.733398 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 597826f6-57e1-3806-9452-0bfafd8174c2 | -14.9639 | -54.726299 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0597e237-0e17-34c7-a2cb-1a69ceb270bd | -8.1018 | -61.1782 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22c43b7b-b681-3bd4-a722-c8f6fbc239e5 | -6.1322 | -57.922699 | 2025-08-16 00:47:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12f4b484-525c-3a19-9e48-dc2be158b055 | -13.1465 | -57.160599 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33870af6-2bd2-30ed-9563-0b93eeaf8f5c | -6.4787 | -62.9184 | 2025-08-16 00:47:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34e458e0-8471-321e-b044-da5f889ed942 | -7.0527 | -59.610901 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c7ed656-1b7a-354d-91cd-7acd4b9d66c6 | -8.9975 | -60.528599 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c8a90e3-e88f-37f6-8b0c-3e507b9c7c70 | -8.9796 | -61.693501 | 2025-08-16 00:47:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99f9de15-9666-3900-aecd-5d986e906302 | -9.1727 | -59.628201 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6bff7814-c6b2-378e-bcf8-b437e0adb05c | -14.9362 | -54.6945 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d27560b6-ff19-3ad5-bf16-ef345ccfcf85 | -13.4054 | -43.6455 | 2025-08-16 00:47:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba6f1241-ce27-3719-9cb3-f3d84df2828e | -8.6681 | -62.445099 | 2025-08-16 00:47:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65c3644c-cd1d-39b1-8ee8-5de0a62e79a3 | -10.017 | -59.212799 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ef2f082-b597-33b4-9bc2-25eff4fc4a3c | -9.0623 | -58.932899 | 2025-08-16 00:47:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33e8af43-b627-31bc-8ac9-dc1e072bc2ba | -13.0083 | -56.858501 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46437aaf-603d-3473-97dd-e4c944ae02d8 | -8.1135 | -61.184898 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36394e84-092c-34db-8883-c863d57b4b4c | -13.4487 | -56.662201 | 2025-08-16 00:47:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fcfccd9d-1882-3834-b80d-47d165d35396 | -6.7992 | -59.8134 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b32ec282-512a-3e28-a890-c1d4807b7947 | -9.1631 | -59.678699 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2f4d61d-1a14-334c-9e98-e9999c40982e | -9.176 | -59.6436 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05cc6d7c-d98b-3b71-81a5-d0b5cd8de4cc | -8.9931 | -60.555801 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c097b9b-fdd6-3348-808e-411770e8e65c | -14.9704 | -54.7094 | 2025-08-16 00:47:00 | METOP-B | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0cd9ddef-67a4-3a80-a5b6-6a26dc53aa5a | -9.1598 | -59.6633 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c0d4bb1-1904-3065-a24d-4b0c81f177a6 | -9.0002 | -60.493099 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2776f2eb-e668-3dce-a0e9-9aa1dcda52bf | -9.511 | -60.532902 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ecdcaf4-8d66-3aba-ae4d-7f451a2945a4 | -9.0462 | -67.374001 | 2025-08-16 00:47:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79db4faa-cafd-36fa-b834-cab116b14c67 | -11.2524 | -50.4743 | 2025-08-16 00:47:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea92d0ea-fb6f-3f25-97bc-4709490b3fea | -10.1204 | -57.758598 | 2025-08-16 00:47:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29f4a102-e2a8-3d78-b7dc-69f278bfd16a | -14.9525 | -54.721298 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23c5ed15-5e29-300b-8eb1-671a271719a0 | -11.2653 | -50.4846 | 2025-08-16 00:47:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30c6091d-1a9a-3ae1-aed7-e3d0b8a560b5 | -9.2136 | -59.627399 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7ebfbdf-c4db-3dfe-bb8d-894424b44b69 | -8.9966 | -60.476501 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12828bac-7802-38fb-873e-9923f2e9782a | -9.3879 | -60.5327 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b541d454-862e-3348-9b46-f19905cfa240 | -14.9477 | -54.745399 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d0ec37b-5bb9-3ae6-8a96-f8f40b9dedd3 | -7.8348 | -61.318501 | 2025-08-16 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c641ff80-2823-3d95-85bf-137fd4f1663e | -18.5173 | -50.742699 | 2025-08-16 00:47:00 | METOP-B | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1f5d0ead-736a-32b3-8fb8-4289506706eb | -8.9833 | -60.557899 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6aa7de4a-20dc-36c9-9308-92ebba83f40f | -8.9939 | -60.511902 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a44f276-32ae-33ca-91e4-f3e64e726eec | -8.4669 | -64.019997 | 2025-08-16 00:47:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc8832a2-5148-3c3d-abf9-6891e2e83b4b | -7.911 | -61.721699 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7ce67b-fbb5-3c80-9470-89acd6aff8bb | -13.1192 | -57.1297 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fdaabcb3-ab77-3b5b-9e76-0d5d1c88a2e6 | -13.4502 | -56.669201 | 2025-08-16 00:47:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ea67a3f-3958-353c-8fb7-9f38d81384c6 | -11.2461 | -50.4487 | 2025-08-16 00:47:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d25d0166-feb5-34ba-bdec-9807896ce452 | -8.6658 | -62.434502 | 2025-08-16 00:47:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f143de11-8673-33a0-8e14-d2b81dd537ab | -3.3733 | -52.709599 | 2025-08-16 00:47:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84fb2783-5b3b-3d30-9552-741d8c6c9b02 | -9.5048 | -60.551998 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c26b46a-2b69-3865-99ab-125fff802fb5 | -21.5243 | -49.138599 | 2025-08-16 00:47:00 | METOP-B | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f57a1469-f0f2-3742-a9df-dab65ba25fe8 | -7.4487 | -60.011299 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9520f94-1248-3fa4-b7ea-2b0059462ed8 | -10.935 | -56.837299 | 2025-08-16 00:47:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f92e572-be53-362e-a5b4-3bcec10afad5 | -9.1942 | -59.68 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc35bba-0051-33fc-b459-59272b3ff04c | -8.1512 | -62.755699 | 2025-08-16 00:47:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f3570219-140e-32ac-8d76-ec921c99ae4e | -11.3666 | -55.412102 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac143266-f842-30c2-8cde-33ebd80135c1 | -11.365 | -55.4048 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12bb389e-0606-3be1-a355-9064ff68829b | -14.5832 | -47.905201 | 2025-08-16 00:47:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e3f5f01d-fc7c-37c9-9a23-09cae69dae86 | -7.5373 | -61.317501 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 890c0a9c-971e-356f-a421-ba0c4c419966 | -9.0019 | -60.501499 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b3491ee-a1ca-3e0e-b5fb-4858dc84b282 | -8.7484 | -55.0103 | 2025-08-16 00:47:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2551e0de-1406-3890-9971-48291fbc2ac1 | -6.1436 | -57.927399 | 2025-08-16 00:47:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3c7791f-a796-3dec-8072-1ea3da796a2d | -11.3535 | -55.399799 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba826426-c9e8-3980-852d-1407f0c44a1e | -7.1002 | -59.220001 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5f6c8f4-5647-3af9-b04d-4b5c55839681 | -9.0091 | -60.534901 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e4609de-059b-3658-828e-17aaa1363c8a | -6.9548 | -59.5401 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11184e63-0c19-34fb-84fa-813511edb4e2 | -13.1176 | -57.122601 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77a19676-546f-3400-9976-32c8de042d0c | -17.6068 | -46.676998 | 2025-08-16 00:47:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3486a126-fa12-3e6e-af8a-c7bb5d6f34c8 | -7.5336 | -61.2999 | 2025-08-16 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
