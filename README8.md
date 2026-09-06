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
| d3770a07-d31b-3356-a615-afa7210d096c | -9.1508 | -67.815903 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1d279bf-8851-3d91-bf69-a0503375222b | -9.3677 | -67.818001 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3622d08f-4c6f-3fb5-98a9-914a7e18c2d5 | -9.3683 | -70.494202 | 2026-09-06 01:28:00 | METOP-B | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b758eb47-54d5-3169-9b4d-4aab17f66d96 | -10.743 | -60.698299 | 2026-09-06 01:28:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62569263-ee36-3845-9f5e-2042f34293c7 | -9.1524 | -67.822899 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a034cd3f-2d0a-3b2c-bc46-de91821878cc | -9.1246 | -67.8367 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d0bb596-4e53-315a-bc1c-8234a97f3c12 | -6.9814 | -70.073898 | 2026-09-06 01:28:00 | METOP-B | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e946143-1c0e-3d68-a7b1-6f84d261e096 | -9.1262 | -67.843697 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ccea219-4a30-34bb-b209-f71c6fd204fe | -9.1426 | -67.825203 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7add3fe9-06f9-3e4b-8815-6b2e72c86854 | -10.7509 | -60.729801 | 2026-09-06 01:28:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9e8dfbe-8dc3-341b-b7fb-7cb278ee8855 | -9.0576 | -67.859398 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5a782c5-71bc-3517-9131-1c3a60fbeff3 | -9.1394 | -67.811096 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19e1569a-3b5d-37bc-9d97-86662c73692e | -9.1492 | -67.8088 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98b00e8b-d925-350b-9075-b87c9f7493c9 | -9.123 | -67.829697 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66c1bd80-bfcf-35e2-94b1-9c6b1728a587 | -13.3423 | -61.1362 | 2026-09-06 01:28:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4dcbfb8-26a0-3177-b78d-4c6e461b6ff9 | -9.1344 | -70.8806 | 2026-09-06 01:28:00 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1139f109-669a-37b0-9188-9f2a6e535955 | -9.1328 | -67.8274 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70747bec-2a56-3229-b7f4-4f60a6556734 | -9.141 | -67.8181 | 2026-09-06 01:28:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2aee734f-9bb7-3cab-96a6-a3f7a3591e65 | -6.6699 | -59.9251 | 2026-09-06 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 270f1273-03ae-367e-bb96-844bd54ece6b | -6.6514 | -59.945 | 2026-09-06 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| aae7da87-eeac-3fb4-b8f3-c748627aaae9 | -10.7013 | -45.9244 | 2026-09-06 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 4b2ca667-ed4a-3043-bd78-1ab469a626d9 | -9.1442 | -67.8317 | 2026-09-06 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d0e1a028-f4cb-361e-b376-83ed74cfc666 | -9.1256 | -67.8507 | 2026-09-06 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| c7853dbb-01a9-31b4-bdcb-b232df8c460f | -6.6698 | -59.9443 | 2026-09-06 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 458cb409-7bc9-3fa5-a4d3-07bc263c54f1 | -6.6513 | -59.9642 | 2026-09-06 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b9c3cabb-b9f7-3c07-b2fd-417422e0fa80 | -14.9246 | -44.6744 | 2026-09-06 01:30:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 3761419e-3a8d-3156-a805-ef9d57437c2f | -5.3645 | -56.0447 | 2026-09-06 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| ddd5122a-4515-326e-a7f0-52872825a680 | -10.7492 | -60.7097 | 2026-09-06 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9a99afd1-17c8-3901-9d51-0ae9ac8076ea | -3.5591 | -48.1882 | 2026-09-06 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 8dedf34f-40ed-3e27-986a-44f5d7035847 | -13.7993 | -51.6445 | 2026-09-06 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 2461cc29-95d6-3a30-9d27-45d0f160937e | -6.6515 | -59.9258 | 2026-09-06 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 8805bc63-2bd0-32e2-93e5-d1b4dc5079dc | -5.3462 | -56.0256 | 2026-09-06 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 7bd56b52-927a-3a96-92ca-4bbdc92022bc | -9.1443 | -67.8132 | 2026-09-06 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 1e6d4efa-dfee-3322-86c4-634e49d3fc2d | -5.3647 | -56.0051 | 2026-09-06 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 83020fad-b5b5-3706-bb6e-e7c39c654aee | -13.7801 | -51.647 | 2026-09-06 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 730e9763-83f9-34fd-963c-2d1ba2c7ea3d | -6.8813 | -55.619 | 2026-09-06 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 4a2dafd5-b6d4-3525-a6e2-1dd379fb9b29 | -5.1438 | -55.9741 | 2026-09-06 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| b6c4a8c3-5e92-36fe-a7c6-6eb5fb39b4c9 | -5.3646 | -56.0249 | 2026-09-06 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 223.0 |
| 6d7edfcc-7777-3ced-a155-0c977771254e | -9.1257 | -67.8322 | 2026-09-06 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 94f5289d-84ba-3f5a-80d3-b988d6c1f749 | -10.7017 | -45.9016 | 2026-09-06 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 80614cd3-0055-3dec-b91f-b4149e8e0cc0 | -5.1439 | -55.9543 | 2026-09-06 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 95898f99-bf2f-3ba5-982c-d0fc14a07d46 | -5.383 | -56.0242 | 2026-09-06 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7a048924-0086-374f-973d-f7d5ed3cdbed | -13.7997 | -51.6232 | 2026-09-06 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 068f455a-bd29-35db-9f9a-54dcbd32df6d | -6.6513 | -59.9642 | 2026-09-06 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 9e082f57-1346-3250-ab0c-c6e4b670b700 | -5.3462 | -56.0256 | 2026-09-06 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 461471c1-070e-3ed2-a97c-623f545a6c4f | -20.4384 | -57.3893 | 2026-09-06 01:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 37cadd7a-b034-3d20-9724-e3771d632223 | -10.7017 | -45.9016 | 2026-09-06 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 2e296d1e-50c2-3b00-b540-eaf115cbf01f | -9.1442 | -67.8317 | 2026-09-06 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ce44955d-ff7f-31fe-a7d5-68ca7c599694 | -5.1438 | -55.9741 | 2026-09-06 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8cd7982b-196f-369b-a37e-17db6576dc00 | -13.8186 | -51.6421 | 2026-09-06 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 89e47ec7-e21c-3057-b969-0b68ee0b5142 | -13.7801 | -51.647 | 2026-09-06 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 8245bc0b-2d3d-3c17-b611-b963053a6fe2 | -13.8375 | -51.6609 | 2026-09-06 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 4808e9c4-09af-32e7-b712-1b254e1d71d9 | -5.383 | -56.0242 | 2026-09-06 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d890175c-3451-3e0a-b21f-e4bc56075fbf | -10.7013 | -45.9244 | 2026-09-06 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| cfd09b7a-a179-36df-874a-699b0741c144 | -5.3829 | -56.044 | 2026-09-06 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d0a6760c-d384-39c4-8316-875ab0028151 | -6.6698 | -59.9443 | 2026-09-06 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1687b66b-1e5e-3098-b8b5-4212111ec111 | -5.3645 | -56.0447 | 2026-09-06 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 816d9f9c-34de-3fa9-ad3f-fa20a41c6e42 | -5.1439 | -55.9543 | 2026-09-06 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0934874a-0623-3d9e-846d-af72498c3a7d | -14.9246 | -44.6744 | 2026-09-06 01:40:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 498a1de9-687d-388e-9f47-ee4a10f0d920 | -6.6514 | -59.945 | 2026-09-06 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 09a71f54-4c9b-3051-a5f5-8dcdf44afacd | -6.8813 | -55.619 | 2026-09-06 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 91b70149-29fd-3007-a34d-1c4082836361 | -11.3443 | -45.0828 | 2026-09-06 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 86ad6f08-5a20-3e22-858f-2fd59e299f3c | -9.1443 | -67.8132 | 2026-09-06 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 43675642-8eae-3fdc-b546-cec9668d299e | -11.3255 | -45.0624 | 2026-09-06 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 4906bfad-8d50-3d3b-bf81-0a608713a2f7 | -13.8183 | -51.6634 | 2026-09-06 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 1d5e2933-9cdc-315d-ae30-649ad7b078c4 | -13.7993 | -51.6445 | 2026-09-06 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 5651554e-4358-3935-97ef-0ae3335730cf | -11.3447 | -45.0597 | 2026-09-06 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 4ac88067-693b-3fc6-8d32-a2a5451058a2 | -13.7997 | -51.6232 | 2026-09-06 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c40f9f67-c48a-3613-9e39-af45965e193f | -5.3646 | -56.0249 | 2026-09-06 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 134ef559-e83e-3b8d-8dee-6fe787ec4e8a | -5.3646 | -56.0249 | 2026-09-06 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 187.6 |
| 34d9c760-3f78-3e0c-a0e2-b573c3722b33 | -6.6514 | -59.945 | 2026-09-06 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 96760b70-e970-309b-ac83-c206e124b662 | -5.3462 | -56.0256 | 2026-09-06 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 65ae419c-555e-32d8-8324-d135fc83b257 | -6.1304 | -47.2224 | 2026-09-06 01:50:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 282fc7f6-8959-33a6-864c-89cbb6adf59f | -5.1423 | -56.2703 | 2026-09-06 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 98f34b26-4564-3ed3-9bb1-5d82a23c095e | -14.9246 | -44.6744 | 2026-09-06 01:50:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 384737c1-a89d-3bb6-9291-9e5105e4c9f9 | -10.749 | -60.729 | 2026-09-06 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 80fb0553-dae3-3d94-b861-2c03751c9593 | -11.3447 | -45.0597 | 2026-09-06 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 7b91844c-bbd7-31f6-b66e-e6c0c39ec739 | -5.3647 | -56.0051 | 2026-09-06 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| f9acec7d-de48-3dfb-b9cd-6561374f64b8 | -13.4291 | -41.8882 | 2026-09-06 01:50:00 | GOES-19 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 55.4 |
| 82b1d789-536e-3504-a962-eb3fafe37106 | -11.3255 | -45.0624 | 2026-09-06 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ef6f4490-778d-3857-9e43-305fa7db9e40 | -6.6513 | -59.9642 | 2026-09-06 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 3ebdd187-016d-3ef2-8da1-f845c5603d7a | -5.3645 | -56.0447 | 2026-09-06 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 7cace15d-035c-303a-85c8-8915c14b2e14 | -5.1438 | -55.9741 | 2026-09-06 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2af83cc3-8c8b-368b-9dad-9f2249527740 | -6.6697 | -59.9635 | 2026-09-06 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 80b9cedb-ed90-38f6-b0b7-3dd43d8dcd07 | -3.5591 | -48.1882 | 2026-09-06 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6d5c6742-f05d-31c1-abbf-f24e5dee9269 | -6.6698 | -59.9443 | 2026-09-06 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9e73bc27-3f5b-34de-9696-0cddfa3b5d7e | -6.8813 | -55.619 | 2026-09-06 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 27739472-a0b0-3c14-bbb4-24530fcbdeec | -10.7492 | -60.7097 | 2026-09-06 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 97f6bc10-43f3-3621-8443-fdeb0648e0a1 | -6.1302 | -47.2444 | 2026-09-06 01:50:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 13d25c15-49b4-3966-be61-0957d261c539 | -6.1118 | -47.2237 | 2026-09-06 01:50:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 9f252d0b-37fe-301a-92f5-a43df8e0a096 | -6.1116 | -47.2457 | 2026-09-06 01:50:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d7df1356-70ed-3ca8-a553-18cb3ac0df1b | -5.1439 | -55.9543 | 2026-09-06 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d082541c-9c26-31f4-8aee-bb90eec826e9 | -5.383 | -56.0242 | 2026-09-06 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 16f63c64-3c1d-3c75-8302-5e3c30023d45 | -20.630199 | -57.989399 | 2026-09-06 01:50:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 51ba5643-d498-3735-9c0b-1e5005172fbb | -20.4501 | -57.408798 | 2026-09-06 01:50:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 61afc63d-7c61-3a64-9b0d-da4f6673e419 | -5.1579 | -55.970501 | 2026-09-06 01:50:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1b8605f-5f79-344b-a756-68eced11ed03 | -6.6601 | -59.953999 | 2026-09-06 01:50:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 324893a8-7ac1-32e1-843b-2ce583c908d1 | -9.1356 | -67.834396 | 2026-09-06 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57523d21-2028-30db-89fa-6c5333603692 | -3.7692 | -61.764099 | 2026-09-06 01:50:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4388fcb4-e3a5-3aeb-ba28-2376a142b98d | -20.447001 | -57.3965 | 2026-09-06 01:50:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README9.md)
