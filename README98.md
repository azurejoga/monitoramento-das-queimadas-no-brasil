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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a74ffd1f-5473-33bd-a2e0-e0296d51882e | -6.41072 | -43.84021 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25d06301-8132-32a5-96b7-8a39b50213c4 | -8.177 | -47.01182 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d98716f7-9db3-3f13-a153-cb066bc9628c | -7.81421 | -46.96974 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80133a86-fb23-3b5b-8790-354023205b50 | -6.62234 | -46.20718 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e028deb-5021-3a0a-ba83-758616cfc54a | -9.91757 | -43.79459 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9f1e818-3cef-39fd-aab5-97b72504ecfe | -7.31297 | -47.28806 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddda13e6-6bca-37fb-be1c-27a5010353b2 | -6.00619 | -52.38562 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 253804a9-b1fb-39df-b42f-464a362f85c0 | -5.6297 | -43.91899 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| fdfad254-c72c-35cb-b679-83d3a4e65ce9 | -4.97528 | -48.66227 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edae7731-c66d-327c-ba12-0817ce6ff701 | -5.4885 | -52.13887 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48e5aeb5-aef5-34f8-98cf-060bfeb6490c | -5.7882 | -45.75855 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b138a08-1ebe-3b54-9da7-75b16a680604 | -7.90525 | -43.53954 | 2025-10-03 04:32:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3665d246-522d-3742-8c6c-1f5cc03ee31b | -10.94988 | -46.70501 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 838b7602-f0cf-3826-9248-b48035503259 | -7.75029 | -42.59185 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 089e79fc-8e4b-3fd9-a5d8-d2858224228b | -8.81688 | -46.6706 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61f0589a-3530-3e41-bbc4-7aa8b6af5e88 | -10.60692 | -48.71599 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8623fd9f-f4b6-39f2-acc7-cba6b96727fa | -7.75399 | -46.25084 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fb5442d2-1ae3-3ddf-ae4d-9ff7e0f1fb1f | -10.8886 | -46.71942 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| f57b8e0c-ff5e-39c4-96c1-1c2c182feb77 | -10.24839 | -44.94747 | 2025-10-03 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a1626b5-3ac8-3d57-9e27-8136676baba5 | -8.25233 | -47.0345 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a84cd332-e5d8-31be-bf8d-a57a26f95345 | -8.51958 | -50.04027 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a32d2c54-6805-306d-9a7f-fe2783d8b128 | -8.2121 | -49.11991 | 2025-10-03 04:32:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 896a3697-a36f-3fbb-ac54-139705535673 | -11.14429 | -47.20059 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05b9909d-319e-34b7-a00a-7ff35145ac1b | -9.95368 | -43.70274 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e1a2cb3-c0cc-3d35-a82e-7a801b2e53d4 | -10.93159 | -46.7333 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1426902b-0ceb-320c-87d9-2dfdb8f46151 | -6.32072 | -43.89808 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 434aebe3-2222-3655-b9c2-049b92772b0f | -4.66941 | -49.51432 | 2025-10-03 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c16a2501-8e65-30d2-8a6f-4bae8dd5a12e | -10.28074 | -48.06844 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9309bd49-2793-3e85-8195-5cecfd06cf12 | -10.28329 | -50.30669 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e71b4dc-e126-33a7-8033-aaa137ab30f0 | -9.91803 | -43.76341 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eae68bc1-6932-3f8f-b5db-16c473fabaef | -11.9989 | -46.57076 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 104a6735-beba-37b5-982e-e0d90743d3bf | -6.05338 | -44.6315 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fcd8ac6f-cf12-321e-888d-2fe217fa797b | -11.14139 | -43.39236 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a56c324a-81f7-3376-9f92-8d8213de141f | -7.25007 | -49.41319 | 2025-10-03 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87a33322-4745-3a77-b325-c70f1fb4ba58 | -10.91036 | -46.71506 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e79bd192-f7c1-3dcd-b9c7-33544e054ae1 | -6.95762 | -45.3457 | 2025-10-03 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12ee9c44-6449-3df0-9fdd-d2d0db71052a | -9.06295 | -46.66285 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9391385-fc89-3491-94eb-e211564ddbd0 | -11.11281 | -43.18985 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9458fbe9-6660-30d1-bcc0-9d2c8010d084 | -11.84145 | -45.04078 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd0091bc-ef44-3747-8d18-b4c6fb9bcdfd | -6.52266 | -45.73917 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6693be49-c4d3-35d9-a7e7-8e90c7df18c3 | -9.87261 | -47.81232 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7030815b-9634-3606-88fd-9ca91f8e51da | -8.75653 | -49.91973 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbf308c0-e920-36d4-8e4c-244135a15030 | -10.94587 | -46.7083 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a92e91c5-545e-38de-a8eb-85762ebb7a68 | -7.76029 | -46.2781 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 4f105b23-ffd1-3ce4-a308-1f5fbffca654 | -5.64285 | -43.90718 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b32204f4-d7d3-3c51-a826-3e4ee71eba9a | -11.0802 | -47.70711 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71ce3921-b78e-3a3a-b1c8-f76f260d3622 | -7.77269 | -42.50955 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f642882b-3a3d-3e16-9e41-fdd9bd3b5ceb | -10.88116 | -46.72211 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3d06429-9d94-3fdc-8248-a454dadafa66 | -6.04263 | -44.62977 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7475ef25-08f4-3dd7-9a59-14f9ff001a89 | -7.75688 | -46.27763 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| d4a37ac9-cb0d-3535-8609-d6f7b97a6758 | -8.6957 | -47.69534 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23f7925e-36c6-375e-9260-4bcd948e49da | -7.79327 | -42.54408 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1b221cde-9362-3556-a4fa-b31911cb9d48 | -6.55736 | -43.8926 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 139f4575-c930-3248-a937-d4315d7f7d3c | -8.17711 | -49.10336 | 2025-10-03 04:32:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d5e13af-9cef-3f2b-b269-34f8b10f7e8e | -7.56356 | -42.3948 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ebc963c7-85f4-3bef-b8e0-04bfe8cb5f1c | -10.25918 | -48.07585 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 585d70b3-33dd-383a-9e62-85e945b6f668 | -8.42933 | -46.80471 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d0ccf9e-40c4-3950-a3f5-752482dfcf02 | -7.31762 | -42.87651 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3f512ce1-bd8f-3b01-8aed-a95df811fa8c | -11.14812 | -43.40439 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5985ba39-67fa-308d-8fdb-4fb2be9223ac | -11.07962 | -47.86087 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d613edf6-d99c-395e-9494-6f2e4f2ceb49 | -5.40164 | -41.33544 | 2025-10-03 04:32:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| db494f8e-efd9-3db1-acad-2d9277d5d774 | -6.03637 | -44.63427 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 355e461e-05ab-3b32-9be6-ece1b3cdc079 | -9.09677 | -46.72058 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfbfbb79-b03d-3d76-946b-893b17e7bc54 | -8.51566 | -47.26 | 2025-10-03 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ff47bb8-e258-31f1-91ba-497add4b5a70 | -10.9413 | -46.71537 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 85bb063a-9c41-3c07-b15a-b22814290724 | -8.8952 | -46.59592 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52809493-1d46-3a13-b0f8-2790590431c7 | -6.04203 | -44.63383 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6c80f025-fc48-38b4-8271-34a4e09511cf | -7.71222 | -46.20279 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a82b4b57-775c-3c82-b4d2-46c851677d88 | -7.80073 | -42.52171 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 79f9551d-1fbe-3697-b572-15ba0460c9fe | -6.23 | -44.27539 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da1c9f68-80d1-3810-a0cc-fe2a313e8ceb | -10.00217 | -50.2642 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9cce3ae-70e4-3326-aed2-2cb9e8324273 | -6.97361 | -44.39766 | 2025-10-03 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab551299-09c2-34f7-b4bd-f46114d4d3ad | -7.75457 | -46.22392 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3fd84f6e-bde1-3400-aec2-5ef7bbdb7ee8 | -7.75742 | -46.22815 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b25bf63b-f140-37eb-a676-f6eaf0b90b48 | -11.2594 | -47.7977 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf5411e9-bc9b-368c-9007-f8e316c2bb4d | -7.78681 | -42.50002 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7ff0ff85-27a0-3f60-9add-625dcbf5c6c5 | -8.21773 | -45.54691 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 627522f9-35a1-3a17-8492-4e46bcdcd095 | -11.90232 | -46.27308 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 543dc002-af12-3d04-9927-eb990d6383b8 | -7.74725 | -42.58379 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2dbb9d21-9a7e-365a-ab7c-de652b406329 | -9.87926 | -47.81337 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7c82269d-82c3-382d-807f-b807eb2e3663 | -10.88231 | -46.71454 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d55136ec-eae3-310e-8541-3600d9b8ea6e | -11.86505 | -48.00621 | 2025-10-03 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d399a792-a028-35ca-bf34-dbb95b0f798b | -8.30408 | -44.86985 | 2025-10-03 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15cab20c-0048-3ad4-b36b-5f179e4bfa50 | -10.87573 | -53.76853 | 2025-10-03 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07c3d525-6f57-3eb7-b3d8-715bfd969720 | -7.02034 | -46.44201 | 2025-10-03 04:32:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9810186-f92f-3f3e-b78a-eb44bab280a0 | -6.23815 | -44.24595 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c3e26c0-57eb-3d6b-88b9-e44eb5531a2d | -10.8909 | -46.70425 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bbbf50b-05b8-35bb-9898-4e68ad28e98b | -6.67762 | -42.82028 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 57c2203c-3e2b-3586-824e-ec0ee4d5f439 | -9.58694 | -43.32529 | 2025-10-03 04:32:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8ec8ae7-67c4-3a35-a557-71c17aa35a8e | -10.60747 | -48.71249 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74deb1a3-fcdc-3473-97ee-8b08553c39cf | -10.89547 | -46.72049 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 585cc3b8-e17e-3d0e-bf8d-ce2d2988d651 | -11.10013 | -47.83865 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e7b610b-e3dc-3718-baac-57e52033b481 | -6.97056 | -44.39297 | 2025-10-03 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1daf8d17-d3b0-3715-a35b-564c108875d0 | -8.22124 | -45.54745 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 667165da-fd78-370c-aa9e-951612d6f0a7 | -10.86123 | -47.24755 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa21e361-57a6-3049-a664-10b3ef9d5a06 | -5.31832 | -45.28341 | 2025-10-03 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| efa6534b-48be-3566-8a65-e95c1a19b868 | -7.88135 | -47.34472 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c52a10c5-ee98-3176-aa6f-e74b090f73b6 | -7.73151 | -46.23615 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c9fa939-891d-33cf-b305-295cd7ef34bd | -10.85891 | -47.21714 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1838046c-2139-3c78-91a2-b21bb7ab04da | -11.06523 | -47.80381 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README99.md)
