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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1585112-5343-3b20-88ad-2744ca96594c | -22.5238 | -46.868999 | 2025-08-16 00:47:00 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7b8332f8-8eca-36c2-bd58-82bf64b0e853 | -13.1274 | -57.1203 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7e18095-dc09-364f-8828-694ee658b867 | -9.5037 | -60.499001 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1dd7e1fe-f23f-368f-8eea-32fb1bac0a3d | -18.0431 | -47.702202 | 2025-08-16 00:47:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce5370c-41dd-3732-b798-7e5efb7ec362 | -16.228901 | -51.124699 | 2025-08-16 00:47:00 | METOP-B | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df2f74e7-c809-384c-9ace-96a1f73dacea | -13.1161 | -57.115501 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86723e1e-4974-3477-bf51-e5e6be778862 | -7.1326 | -59.6474 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98ab37c8-f59a-3045-96ff-4796533a88a5 | -13.1156 | -57.160198 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0dd980d8-88b8-3130-b2ef-b9ca02b98b3c | -14.9721 | -54.716702 | 2025-08-16 00:47:00 | METOP-B | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5fffe645-e9ca-3a00-8285-f1ddaa34596b | -10.1122 | -57.767799 | 2025-08-16 00:47:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30021ef6-70d8-31aa-b590-8c8da42118da | -10.1106 | -57.760799 | 2025-08-16 00:47:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e35eddfe-de59-34b9-a06d-1e778102066b | -8.9957 | -60.520302 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ee801c8-57d6-3838-9c9d-aa38a6ce33d5 | -7.6744 | -63.3022 | 2025-08-16 00:47:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af242895-c9c3-3507-ba8e-a28c0cad9099 | -9.5153 | -60.505299 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f54d1d2-25b6-3594-87df-8df968d873fc | -12.5453 | -46.944099 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8875df00-5f1b-3423-865c-36b6fca9ddc0 | -7.3022 | -60.6105 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee2fa80-0ee1-3a1f-aa0b-77d5d9b89ad4 | -7.9562 | -61.741501 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 045e955d-b863-3930-b5c1-bfb0161270e2 | -14.9581 | -56.227299 | 2025-08-16 00:47:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d749388-9e24-3612-bf32-d45864a4a056 | -12.5645 | -46.938801 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57505fde-c86f-3986-8d10-b7a68f532238 | -7.6256 | -63.3125 | 2025-08-16 00:47:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09e6d838-8958-30cc-a995-48bbf8b77a51 | -9.1858 | -59.641499 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9bd74e1-64e8-3bb6-a93f-e318fe4d8c2c | -7.9347 | -61.736301 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0d3fd5b-b8ed-365c-8463-30b2d154e1ad | -9.1612 | -59.6227 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c79a89a1-96d5-36c1-bc64-7a7937692d2e | -7.5275 | -61.319599 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d3809e6-eaff-30f0-a817-03c55a58e25d | -7.9188 | -61.710201 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3988fad2-e088-315d-a687-dcdfabd4c175 | -9.1646 | -59.6381 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7c1cc50-b4f8-3b98-b213-7a732b6404fa | -7.4615 | -59.9286 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6112a93e-d0fd-337d-875d-48d7fc077cf3 | -7.8329 | -61.3097 | 2025-08-16 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c36d849e-384c-3ff4-a388-4331568c4e2f | -7.6067 | -61.210999 | 2025-08-16 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8c3e224-7a08-38a7-ac59-c2b335d25d51 | -12.5507 | -46.965 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23441e8a-a331-3004-a74a-2d5255ef73e1 | -22.527599 | -46.883499 | 2025-08-16 00:47:00 | METOP-B | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 102b7bae-1339-3296-b8cd-e9478f83effc | -8.9877 | -60.530701 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b52e7299-8f4a-3ec3-becc-eeb34c77962a | -9.0073 | -60.526501 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45c7ad29-b3d7-3a54-8248-d89c57896ed2 | -8.9776 | -61.6838 | 2025-08-16 00:47:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a350efe3-1259-36d9-a328-80504a114b93 | -18.5271 | -50.740101 | 2025-08-16 00:47:00 | METOP-B | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df6ca02b-7eae-3cbe-a4fd-44848735111c | -8.9064 | -60.724899 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33e39c22-331e-31a4-9864-d7e944ba44e7 | -7.0723 | -59.233601 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd02024c-a976-3f87-a59d-da6369be5cb6 | -14.9557 | -54.689899 | 2025-08-16 00:47:00 | METOP-B | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98bcf76a-3d78-3e1a-afaa-ff8ea5d4d5a5 | -11.3552 | -55.407101 | 2025-08-16 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cef518b8-8212-335a-8449-fae925e847b5 | -13.129 | -57.127399 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8c346a-8ba4-3d32-878b-7230d44acaff | -9.2119 | -59.619701 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a626c79-2a02-38b5-a674-2a79ec529457 | -9.0314 | -67.4011 | 2025-08-16 00:47:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6904b515-c17f-3228-a2ea-392a61396252 | -14.9476 | -54.699501 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1c15117-6301-36f8-82eb-a27f8ff02560 | -9.5073 | -60.5159 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 450108a2-2166-392a-b4c1-b0f0b3d73f44 | -12.5549 | -46.941502 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| edb79576-1f59-34c0-ba11-ce3e631f28da | -8.9637 | -61.666599 | 2025-08-16 00:47:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fb590319-cae0-3bb1-8aaf-b8610ff30496 | -8.1536 | -62.766602 | 2025-08-16 00:47:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a8e9c9f4-9a2a-374d-9cf3-f55d12de609b | -14.9541 | -54.7286 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b5af3dec-22f8-39db-bedf-349f4e38ce3c | -14.9459 | -54.6922 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b6dfcc5-e3f4-3c24-b0b4-87b714f32bf5 | -18.047001 | -47.7173 | 2025-08-16 00:47:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 94a632f2-ad2e-36e3-8fa4-9ca6b1bba53f | -9.2038 | -59.629601 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b71392dd-1f3b-3ee7-8c86-03815ec7089a | -8.9815 | -60.549599 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55300e52-d677-373d-879a-373c47235282 | -24.923201 | -52.361801 | 2025-08-16 00:47:00 | METOP-B | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05dc8a04-7899-314e-b4bb-4f94286f7ea8 | -13.0098 | -56.865501 | 2025-08-16 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3cdd1383-232d-3f7c-86ff-55cfbd458e8e | -9.1614 | -59.671001 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e76794b7-255b-3a0a-8a91-f977f8685dc1 | -7.2451 | -60.631199 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbfe132d-c2e7-330d-ab83-93c35571d5bc | -7.6231 | -63.3009 | 2025-08-16 00:47:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0736345-f0e9-3fd8-a7e0-3b345324ee99 | -23.9918 | -53.144699 | 2025-08-16 00:47:00 | METOP-B | MARILUZ | PARANÁ | Brasil | 4115101 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ccf6fd5-e787-3ff7-b025-ad571d4fc2d9 | -8.9144 | -60.714298 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0841fdcf-5d98-35c1-a26c-7221f38d2f5c | -7.0429 | -59.612999 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 615dc397-5cc9-37d4-80f5-714b0f1cd846 | -9.1744 | -59.635899 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be1edf9a-f228-3b8d-9d74-d1ec1fdb782d | -7.4373 | -60.005798 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb3f3570-8135-3a0e-b468-6d0ec627ff87 | -13.4148 | -43.678902 | 2025-08-16 00:47:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b52a6ab1-5870-3daa-bb1d-9a6b9ea18ced | -9.5146 | -60.5499 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9aad2905-d5db-32f7-a56f-3b3c5be4165b | -13.4404 | -56.671398 | 2025-08-16 00:47:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0cb3ce0b-47ff-38fe-992f-2d47be754ecf | -7.4291 | -60.015598 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 952113e9-0cf8-38a4-a1a6-df42198dca0d | -8.9816 | -61.703098 | 2025-08-16 00:47:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d82900be-13cf-32d0-964f-f57dcb03da78 | -7.0707 | -59.226398 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d32fd0ed-0016-3298-a775-f54b804fa9a8 | -7.312 | -60.608398 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dae968ac-7f5d-3464-b55b-5fbc2d86691f | -9.0037 | -60.5098 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b48f173-ec48-3338-bc9d-97f2bd986dfb | -15.6617 | -56.1992 | 2025-08-16 00:47:00 | METOP-B | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 383388fa-ee25-393b-8e52-ab9bfcb1ccf5 | -3.8158 | -47.706501 | 2025-08-16 00:47:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f93cf5c-8066-33b1-acfc-63e72b499dd7 | -9.7983 | -48.526901 | 2025-08-16 00:47:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5ab6cc2-3aef-313a-853a-d57afa89e8e7 | -13.442 | -56.678501 | 2025-08-16 00:47:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 307332a6-5b30-34c9-b383-0a7e1774c54f | -14.9395 | -54.709099 | 2025-08-16 00:47:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd70b30-b249-36f0-950d-1cf11a2510ff | -7.0413 | -59.605598 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65ed7c4c-62fa-3fb8-9c20-6cee8a44857d | -12.5357 | -46.946701 | 2025-08-16 00:47:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7347e91e-c4f2-35d4-beb4-bedf6704afa8 | -7.0806 | -59.2243 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d930324f-43b3-3ef5-90ca-91b0d7b30552 | -9.0268 | -67.377899 | 2025-08-16 00:47:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fcf1664-d9dc-3b1b-976d-7c305aa6c676 | -7.2924 | -60.612598 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae83d8cb-a4da-31c4-90eb-acadf0fa4bea | -8.9162 | -60.722801 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 806ce63e-0bbf-38f1-b3da-59f5ceb7ed8d | -10.122 | -57.765598 | 2025-08-16 00:47:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e32d05bb-0a47-3fe6-b1c4-6adec247ae8f | -9.5128 | -60.541401 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26762906-aaee-35a4-b5eb-45618ab3b776 | -10.1189 | -57.751701 | 2025-08-16 00:47:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25a8bd0d-b50d-35b5-9c87-b2a69008b837 | -7.5238 | -61.301998 | 2025-08-16 00:47:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ccdb538-c746-3470-a677-562d8de8fd27 | -8.9841 | -60.514 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| daf2ae4b-56b9-3e55-b392-ee77083e8614 | -7.6158 | -63.314499 | 2025-08-16 00:47:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3ce5095-de04-3c1b-9865-32415cb3935d | -9.9279 | -60.4701 | 2025-08-16 00:47:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a314890d-7983-35df-89b2-2d3de216dfa8 | -8.9904 | -60.495201 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 491a63c7-65d1-30cd-8e5c-01a16cef5f3d | -6.4908 | -62.9268 | 2025-08-16 00:47:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c02c27b9-4abd-339c-9483-f8400c447306 | -9.2054 | -59.637299 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53c4fafa-a11a-34e9-8106-3b0f1d468696 | -7.0822 | -59.231499 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac678c10-35b9-3e33-9e88-b4b677af7164 | -6.9464 | -59.6418 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76d93f49-f527-3857-99c1-538f37ac5818 | -9.2284 | -59.648399 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 137115d6-b9a3-39ba-aade-d4856fc3187c | -14.2788 | -53.0061 | 2025-08-16 00:47:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a36e3b3-36b5-366f-ae3c-88bb930662ee | -9.0411 | -67.399101 | 2025-08-16 00:47:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e942758-3381-306b-9f8a-df6017950c59 | -9.1662 | -59.645802 | 2025-08-16 00:47:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32d28525-4a21-36be-acbb-fe4ae6a31420 | -9.0639 | -58.940201 | 2025-08-16 00:47:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6f1b792-4f4a-3a88-b976-fce63b7afb04 | -7.0791 | -59.217201 | 2025-08-16 00:47:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1b833cd-c7a0-3718-8955-c7878c48b79c | -11.2621 | -50.471802 | 2025-08-16 00:47:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
