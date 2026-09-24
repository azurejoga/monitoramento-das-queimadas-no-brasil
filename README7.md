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
| 03e93446-8cc1-3bc4-8010-1d13ea00cbff | -6.3407 | -57.740101 | 2026-09-24 00:16:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa08d4d9-59ed-3498-98f6-7dc5eb8e706f | -11.9884 | -52.449902 | 2026-09-24 00:16:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4d41cc5-c945-392e-8030-60b36c9ff4e9 | -12.0886 | -50.7384 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a91b3ecc-8da7-3342-a339-2b70ec7ee253 | -11.9499 | -50.762402 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b8897bc8-cd45-38fd-8b64-0f7268c533b2 | -4.0643 | -56.2169 | 2026-09-24 00:16:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45967e4c-077f-378d-9a4b-c605604f5342 | -5.2219 | -49.2257 | 2026-09-24 00:16:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b996aed2-bd56-35e5-9d03-151422693ba6 | -9.9966 | -45.179501 | 2026-09-24 00:16:00 | METOP-B | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 321f6045-b339-3201-8b38-3bc4a129a560 | -4.2903 | -49.119598 | 2026-09-24 00:16:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa9c97b-e9c6-30fd-a687-7d94ad5a6ac2 | -12.6905 | -46.990398 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 110d3520-864e-3e06-8675-09ea279614f8 | -4.7191 | -55.975601 | 2026-09-24 00:16:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bd1d7f8-43ca-3bd8-b754-3f071a582f0e | -15.4718 | -47.899601 | 2026-09-24 00:16:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c0fa44c9-3a68-32eb-a7bb-56c3834dae49 | -12.1521 | -50.746201 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97fcd794-7083-3ca5-8e68-da5b0b143b79 | -8.4552 | -51.482101 | 2026-09-24 00:16:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8b9eb7e-2eee-3c95-8005-8143bc668dac | -8.5173 | -50.154701 | 2026-09-24 00:16:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61c15003-ad6a-3dd2-a96b-1fd609a30ae0 | -5.8442 | -49.8713 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dd6e2e7-5d2a-31cf-abac-b4f9c7a5a21e | -10.7449 | -44.816002 | 2026-09-24 00:16:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f9b9c3d-6a5b-3c2b-8466-900219db5b31 | -3.1113 | -51.044601 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57d1f4f7-52fe-3601-865f-ebe8b29d2024 | 0.6066 | -51.5564 | 2026-09-24 00:16:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 93dfc36e-159b-3a0b-8aaa-ab4dd5f5a0bb | -11.2458 | -51.396 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5d94fa6-4e65-356a-839e-57b642e3df51 | -4.6696 | -45.966 | 2026-09-24 00:16:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d3311404-abe3-3e33-a5f3-de8f9d90d688 | -5.7576 | -45.0853 | 2026-09-24 00:16:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a02d9af6-b629-30cc-a7eb-6fe8524a722b | -9.8531 | -48.507702 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 688f8253-62d8-3f29-a843-1a45748e772c | -4.9896 | -45.534599 | 2026-09-24 00:16:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f881c35f-cabc-35b3-9d02-b703d046a48d | -1.2755 | -57.0182 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d957f664-16ce-3fba-902e-cf1154fd5f52 | -3.2296 | -54.312199 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2765ee26-07a4-3553-b836-8023a8d2e875 | -15.9508 | -42.946999 | 2026-09-24 00:16:00 | METOP-B | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2a93c894-b639-3211-a368-99b9bb925c10 | -11.9726 | -50.771999 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c2be4b81-0604-32a6-b4d0-ffa79b4641e3 | -5.8411 | -53.843201 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a106ab08-bf45-3749-892b-09fbd1136342 | -1.6215 | -54.897598 | 2026-09-24 00:16:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0768f61b-bae1-3a80-b821-1b46406dd828 | -10.4174 | -49.349701 | 2026-09-24 00:16:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88fc3dc4-feeb-39d3-9c5f-577504ed0bd0 | -6.1223 | -44.588902 | 2026-09-24 00:16:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34705e61-21ee-360b-8381-a6c1888df489 | -11.9982 | -52.447701 | 2026-09-24 00:16:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a32adcba-fa32-33f0-b57c-d390c1c44dce | -3.0714 | -54.3866 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23393267-6e43-3c6c-8c0f-94c0ee949563 | -6.2125 | -47.492298 | 2026-09-24 00:16:00 | METOP-B | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 081c1889-b9e3-337e-aece-360a9b21efde | -11.953 | -50.776501 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 829120b4-7b0b-360e-8d43-c8a7d0fea003 | -2.8883 | -54.0751 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af784ef2-a30c-3d23-9d5e-4c0d7aab0297 | -5.7606 | -45.098202 | 2026-09-24 00:16:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 022d64b6-7e28-3b17-b27f-a7604ede9451 | -3.8083 | -58.870899 | 2026-09-24 00:16:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f7afbba-7be0-3e42-a404-c4ad7945fafe | -12.4231 | -46.951199 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71c492f1-208c-3dd7-a890-ac5cf518899b | -10.6134 | -48.942699 | 2026-09-24 00:16:00 | METOP-B | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48d37b6b-846c-3fee-b04c-834c85c4b8cb | -5.7851 | -50.200001 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f85905c3-416a-384d-812c-38587da2a5b5 | -8.4493 | -48.6838 | 2026-09-24 00:16:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 0df877f6-30e4-362b-bce0-f63bbb171e9e | -12.1439 | -50.755501 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82eae23b-a657-33b3-9b18-dd9ce2a0ea9c | -1.4272 | -54.583401 | 2026-09-24 00:16:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4ae3599-4768-3f9a-9439-3d8c779e8289 | -3.4574 | -50.074402 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c798f715-8bc3-35b3-8e74-e359feed7d8d | -3.4378 | -50.0788 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 634dd2f8-8090-3294-b612-6d072c5f67d3 | -11.2442 | -51.388901 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c24ff226-b32d-305b-8306-513fdc031003 | -3.2089 | -53.392899 | 2026-09-24 00:16:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6ce855e-c253-367f-b650-8156a37555af | -6.2646 | -43.264999 | 2026-09-24 00:16:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 097a2260-45e0-3a04-82f8-12466ec2570d | -6.3463 | -57.766102 | 2026-09-24 00:16:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 264f9c03-e31e-360b-a90a-bf142c9fcae2 | -12.165 | -50.757999 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8733607a-be41-3c32-b58e-697d2a8226dc | -9.8416 | -48.502499 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00385de1-2f47-3d45-a1f4-3ec6863c7cba | -6.3015 | -51.112202 | 2026-09-24 00:16:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 165d6ded-302d-3e9a-89ab-50b3a7857530 | -3.9564 | -59.314602 | 2026-09-24 00:16:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21f747dc-a5e6-391f-b107-ab368e9668d8 | -8.0483 | -48.510899 | 2026-09-24 00:16:00 | METOP-B | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1d23117-660f-345f-8953-9434163f4623 | -5.7734 | -45.1087 | 2026-09-24 00:16:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4413d16-7284-3a12-bbd9-902f0f0b6e96 | -3.1706 | -51.351501 | 2026-09-24 00:16:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2805049a-f475-3ee2-8aee-85fcb62fbeb1 | -3.1503 | -54.601799 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f667b90e-1727-31a7-bac6-2b3f82660bf7 | -6.4343 | -59.9091 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8665177d-bc97-350b-9be7-be1a3185c525 | -12.6807 | -46.992802 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ed999da-2d7b-32e8-aab6-7f44b10b05e9 | -12.0984 | -50.736198 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5586e74a-306b-3c32-8d8f-f6b6f5a1eb3a | 1.2842 | -50.836899 | 2026-09-24 00:16:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6c9789f6-f4b0-3e30-babe-a56936171d89 | -10.4512 | -44.924999 | 2026-09-24 00:16:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df8e4d25-fcd2-32d1-9dff-8e38938c16a5 | -15.2345 | -43.271198 | 2026-09-24 00:16:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 0c641477-0b6d-3f47-bd10-c1c1396fa643 | -5.1001 | -60.224998 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83f6b0e5-7593-3d3f-abf8-29d986e4accf | 1.6057 | -55.882301 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4268b05c-dbb9-3811-afe5-232a744f5e4c | -8.124 | -54.798801 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb92e3cc-7c7c-3a3d-8721-d28d50b8a2b0 | -8.4582 | -50.212101 | 2026-09-24 00:16:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5ea4cfc-6b04-317e-bbc9-4e3cc18cce5d | -13.2104 | -51.544399 | 2026-09-24 00:16:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 461942c7-2de5-3622-b119-487588e39953 | 1.2859 | -50.829399 | 2026-09-24 00:16:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1078500a-e054-3d1d-9ab1-f3322c5454b5 | -4.6724 | -45.977699 | 2026-09-24 00:16:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1412967d-47ea-32c9-a645-48968a918fc6 | -6.6411 | -50.927799 | 2026-09-24 00:16:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a589922-82be-3949-a2ab-492c8d6a1636 | -12.1666 | -47.3559 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fd243bf-e966-3043-9710-9fec5394ab84 | -12.0286 | -50.281502 | 2026-09-24 00:16:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 114a9c24-87a9-3de2-b535-e5c13be7dc2a | -13.6933 | -43.069599 | 2026-09-24 00:16:00 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a90111f3-96e7-3269-b09d-0a491d2443b6 | -6.1373 | -53.1381 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03374664-cf33-354a-b528-1797c0aeaabd | -11.2462 | -51.351101 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e7ea5161-8c95-3c6a-9d3c-c08a1d479869 | -9.1518 | -49.9515 | 2026-09-24 00:16:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34fdb91e-9257-3050-afce-8475bd905923 | -10.6545 | -51.3274 | 2026-09-24 00:16:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3e654f-4139-3555-a888-44a263d0d682 | -5.7593 | -49.951099 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0080546-c764-3a66-9736-059bc46905e5 | -7.2628 | -45.5229 | 2026-09-24 00:16:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 543865e3-e3c2-3d24-851c-b32f2d87028f | -10.91 | -53.9314 | 2026-09-24 00:16:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa1b509-d7e3-3916-880c-543dce36c710 | -9.5663 | -40.329399 | 2026-09-24 00:16:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cbfc4e7d-2a40-394f-9640-343e146e5828 | -11.2575 | -51.355999 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8db56d4-d151-3579-a566-b2de9f5b8354 | -4.6668 | -45.9543 | 2026-09-24 00:16:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10f86d54-039c-352a-b8dc-a9fbba204a80 | -7.4747 | -44.5611 | 2026-09-24 00:16:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8fee0fd8-38b6-3647-af1c-8effebaefd04 | -3.2012 | -49.089901 | 2026-09-24 00:16:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 453649f1-95fb-371c-b5a0-64a73b84c0de | -15.462 | -47.901901 | 2026-09-24 00:16:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 832cb9b5-9b6f-33e4-be7e-888afd3fd6cf | 1.5673 | -55.824299 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66091b9c-7779-3a25-9aba-457416a9d0de | -8.8998 | -46.810902 | 2026-09-24 00:16:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29cf1743-efe9-36ee-98eb-1d73cbddef30 | -5.191 | -44.694199 | 2026-09-24 00:16:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee7e5920-6227-3e8f-a0d7-c1172571f05c | -8.2545 | -48.1987 | 2026-09-24 00:16:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 489f084f-e172-3b82-8c17-7671822f8194 | -11.7911 | -50.9758 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f29321ae-6c29-35ac-ae2c-12c8c3201c5f | -7.6157 | -46.791599 | 2026-09-24 00:16:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e048a2e9-bc8e-3104-8505-6adda697ff14 | -10.2638 | -49.9464 | 2026-09-24 00:16:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b0d0f2a-6087-3d48-8991-ab70237b538c | -3.4149 | -53.990101 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 272d9c86-9fc7-39cb-a1da-9eb5d7f30e67 | -3.1469 | -54.5863 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66ff44c1-beba-3394-8c5a-d6d1e24d543a | -5.6506 | -60.187302 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d7ac020c-e1c6-39a7-adc7-500064e9f02f | -7.4273 | -49.849499 | 2026-09-24 00:16:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a28df394-74d3-3346-900c-775af1ed6de3 | -0.4579 | -51.7528 | 2026-09-24 00:16:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
