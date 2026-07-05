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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bb0e273-f981-3a4d-96b4-e21cdc79825f | -6.59123 | -51.69909 | 2026-07-05 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| eac47e31-2c5f-3e7b-9034-be823350c805 | -5.8691 | -51.73961 | 2026-07-05 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e1e947b2-6add-3cbe-aa54-6bdf1f899014 | -8.67524 | -54.56318 | 2026-07-05 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 91114aa6-b73f-3faf-acb7-71ac3d9d6fd4 | -6.99097 | -55.89811 | 2026-07-05 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d875c7c2-e9d1-3430-841e-9ccca6411794 | -5.72043 | -51.72956 | 2026-07-05 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a94c17cd-0c74-3d2e-b7f9-c8bd7fe569df | -6.89971 | -43.69908 | 2026-07-05 00:22:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| d9c32601-5eeb-3905-ae22-4205189e4ac5 | -3.21947 | -53.02238 | 2026-07-05 00:22:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7589d987-ca2e-3cba-8a18-c0f02435e2f4 | -8.72217 | -54.55671 | 2026-07-05 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 7b1c082e-e168-340d-a6e2-2ebaf25209f8 | -8.67656 | -54.57329 | 2026-07-05 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 25ab412f-e19c-33c8-b049-1d7adcd0d16d | -8.72082 | -54.54662 | 2026-07-05 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 59e56fc1-87d0-3558-b779-c2a079ecde38 | -8.67909 | -54.66597 | 2026-07-05 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9c7f85e7-deed-3584-896a-9514f3958916 | -6.88999 | -43.70579 | 2026-07-05 00:22:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 097f4d96-bc87-3395-a717-f6216a8f3b1d | -8.32578 | -45.37906 | 2026-07-05 00:22:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d5e7c93e-47d5-3c9d-adbc-27c1966402ac | -7.40804 | -46.8337 | 2026-07-05 00:22:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 44faa01d-73ec-39c0-8eae-3e53da70ead0 | -6.42533 | -55.79403 | 2026-07-05 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f35717db-6234-3c24-82d1-ee7ccf0a8d31 | -9.38997 | -48.91761 | 2026-07-05 00:22:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 61b444f8-ea44-3dc6-87e5-191a11834601 | -7.26137 | -49.55059 | 2026-07-05 00:22:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d33f83b1-1e1c-3040-bf36-2496be480a7d | -8.68462 | -54.56184 | 2026-07-05 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 1de41db9-d6d2-3d3a-a7dd-05f9c8fe8c70 | -9.45515 | -51.82394 | 2026-07-05 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 70a86855-a8b3-3e61-ac45-6b93ebc9318c | -1.6964 | -53.67723 | 2026-07-05 00:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cda51c48-1435-3800-9522-44d0c2e73e93 | -10.9397 | -43.0593 | 2026-07-05 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 304.0 |
| 275a4c54-14a5-320a-90d7-ab4172b58547 | -11.4334 | -46.5969 | 2026-07-05 00:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 5a8a4882-38f4-396e-9b95-6aea5f84fc76 | -10.9405 | -43.0117 | 2026-07-05 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 1dda4fa6-8c4c-336c-9306-e7f3d2ad48d8 | -10.9205 | -43.0622 | 2026-07-05 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 01afd02c-ba03-3785-b192-c20b8ea0b07a | -10.9209 | -43.0384 | 2026-07-05 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 47a1116f-4678-30de-ba0e-14145d0e44d7 | -10.9401 | -43.0355 | 2026-07-05 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 508.4 |
| b7e67e5c-0ab3-3f78-8616-5afbd8e82524 | -10.9397 | -43.0593 | 2026-07-05 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 197.6 |
| 32181e07-cd3e-3e48-8b34-42bb88269f69 | -10.9205 | -43.0622 | 2026-07-05 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 2d0e41ac-7776-3675-ad90-3ecdede8d46f | -10.9401 | -43.0355 | 2026-07-05 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 422.6 |
| 6970d43c-9392-3eb4-b3f4-22901819a9f7 | -10.9209 | -43.0384 | 2026-07-05 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 375.8 |
| 972f6cb6-a2c3-3dfd-a65f-5096ae5d6c97 | -10.9401 | -43.0355 | 2026-07-05 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 398.2 |
| a3b3a285-ec6a-31de-94a7-6111401e5420 | -10.9209 | -43.0384 | 2026-07-05 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 278.6 |
| 470e90cf-f204-3889-84be-90ad5be88aef | -10.9205 | -43.0622 | 2026-07-05 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 1903bcdb-da31-3819-a6c4-caa72552b354 | -10.9397 | -43.0593 | 2026-07-05 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 3927f371-1ba4-3566-ac99-c173cadbdbdb | -10.9593 | -43.0326 | 2026-07-05 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ddf917ed-9428-30aa-b84d-e792a92c63b7 | -11.4334 | -46.5969 | 2026-07-05 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| d531bae3-d827-3492-8d5b-0e62d1947da2 | -10.9209 | -43.0384 | 2026-07-05 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.8 |
| f37fb4df-b810-318d-9d5b-0b33600578d0 | -10.9205 | -43.0622 | 2026-07-05 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| e0907884-cfdb-307a-a5bd-038a296ad893 | -10.9401 | -43.0355 | 2026-07-05 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 312.7 |
| 93ff4701-6c97-31be-b6d9-7ce7a4cd601f | -10.9397 | -43.0593 | 2026-07-05 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 30047e97-d292-3f5e-9226-a4bb3cbdddc4 | -10.9209 | -43.0384 | 2026-07-05 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 7cc86d6c-b251-3607-a054-c58a27120cc4 | -10.9205 | -43.0622 | 2026-07-05 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| ceb12d94-4405-3648-a1fd-34d7e1c5c7f5 | -10.9397 | -43.0593 | 2026-07-05 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 9676bba4-1f81-34c3-b5b8-501b1e95fd27 | -10.9401 | -43.0355 | 2026-07-05 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 254.6 |
| b0c86b3a-7b8c-3ff9-82f5-36ae0fc62229 | -10.9401 | -43.0355 | 2026-07-05 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 243.1 |
| 68612287-f066-3046-8f41-1e473aee2efa | -10.9205 | -43.0622 | 2026-07-05 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3bda15d6-7481-3708-9f28-896e7e87e59e | -10.9397 | -43.0593 | 2026-07-05 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 5997964f-f4fc-3d47-957e-a1e5f9dc0f2f | -10.9209 | -43.0384 | 2026-07-05 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| db6b8329-518c-32ba-890a-980204ef6f67 | -8.6085 | -63.8265 | 2026-07-05 01:29:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba1c3891-c335-352b-98ae-8ce03799343b | -8.8578 | -62.209801 | 2026-07-05 01:29:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54405d12-f491-316a-a476-4aef60755753 | -8.611 | -63.8368 | 2026-07-05 01:29:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0e8cd666-f9ed-302e-bef8-819e0c7e96e0 | -10.9205 | -43.0622 | 2026-07-05 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d720b6b3-7ade-3b72-a8aa-7e46997dd761 | -10.9401 | -43.0355 | 2026-07-05 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 400.4 |
| 15f6f887-5cde-31c3-8fb2-a18517964622 | -22.1213 | -47.2765 | 2026-07-05 01:30:00 | GOES-19 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| bef186a9-5c07-3b9c-bff7-94e4fc7d3d5d | -13.2595 | -54.3283 | 2026-07-05 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| e2b9fa2e-b4f0-3275-9d45-ff9c6258388a | -10.9209 | -43.0384 | 2026-07-05 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 6e0df84d-5e34-3f67-a034-b084569361d5 | -10.9397 | -43.0593 | 2026-07-05 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 197.0 |
| aeee895d-bacf-333e-be2a-db900de323fe | -13.2404 | -54.3303 | 2026-07-05 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 5c2028e2-80e1-3bc3-b551-c75c17abadae | -13.2595 | -54.3283 | 2026-07-05 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e7850ebe-bdab-305e-bb16-c1b0f3ef7025 | -10.9397 | -43.0593 | 2026-07-05 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 253.8 |
| 2c715ce9-25c4-3d61-a2b8-63ee60d2b4a6 | -10.9401 | -43.0355 | 2026-07-05 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 347.4 |
| 02894768-1e3b-3671-b68f-e162b79ffa93 | -13.2404 | -54.3303 | 2026-07-05 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| b7d276fa-f8db-39f4-8f5d-a01206abf68f | -10.9205 | -43.0622 | 2026-07-05 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| cb9ff1ba-f4f3-3951-808e-39351a77c131 | -10.9209 | -43.0384 | 2026-07-05 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 8ebfc832-3a6d-30dc-a800-3d547bb350e2 | -10.9593 | -43.0326 | 2026-07-05 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 9fd658f3-79ea-3b65-a7a3-68fa6e8f9145 | -10.9209 | -43.0384 | 2026-07-05 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 213.2 |
| 45b2f3fc-87f6-3e64-9d25-24fdd165b95c | -10.9593 | -43.0326 | 2026-07-05 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 65972dc5-8afe-35fc-97f5-b4a1c1a77aef | -10.9405 | -43.0117 | 2026-07-05 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ce689319-5e62-3fe9-9c51-b546ac2e61f1 | -10.9205 | -43.0622 | 2026-07-05 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 0441f456-74be-39fe-887d-ae63449f003e | -10.9401 | -43.0355 | 2026-07-05 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 497.0 |
| fba73f56-a583-3282-b8d0-9e2b54519a84 | -10.9397 | -43.0593 | 2026-07-05 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 247.6 |
| 3ecab569-8d2a-3959-b471-66cc38c89b68 | -13.2404 | -54.3303 | 2026-07-05 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8bc56e18-1976-3e30-aaa5-90957c0a1cf0 | -13.2351 | -54.2939 | 2026-07-05 01:54:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 069625d3-f22d-3763-8265-d244c581ca37 | -13.2609 | -54.349602 | 2026-07-05 01:54:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c9832b2-6286-35cd-86f9-f8eb30ddec58 | -13.2432 | -54.3232 | 2026-07-05 01:54:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3373b0cd-3f81-31a6-852c-788501aa092a | -13.2337 | -54.326 | 2026-07-05 01:54:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a816c2f-c624-324f-b85c-f507b41af0b5 | -13.2514 | -54.352402 | 2026-07-05 01:54:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd48f85c-2a36-3502-b825-c98e2bc9a3e2 | -13.2528 | -54.3204 | 2026-07-05 01:54:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7eb36f96-0c6a-3206-ad4c-9f118a7d9fa1 | -8.8624 | -62.219501 | 2026-07-05 01:55:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 72fef058-a539-380b-b922-240f88c6ece6 | -8.6184 | -63.833 | 2026-07-05 01:55:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 534ea3a3-c860-3905-92a1-179122e2e592 | -8.8599 | -62.209099 | 2026-07-05 01:55:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65b57ec3-7d6b-33b5-ace0-7385a0ad46a2 | -8.6204 | -63.841499 | 2026-07-05 01:55:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a0fdba1a-ec3d-3027-a05a-4a0841ffd20b | -8.6086 | -63.8353 | 2026-07-05 01:55:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa364b0c-c3a0-32ff-83b1-d0ffab59417e | -13.2404 | -54.3303 | 2026-07-05 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| fc291cfb-9703-3e87-bb44-97a99b834c32 | -13.2404 | -54.3303 | 2026-07-05 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 55b76db6-f4a2-365c-a5f1-d4f0d306a44a | -10.9397 | -43.0593 | 2026-07-05 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 06f77aca-94d4-3fe5-8652-c0cdfc28ffc4 | -10.9209 | -43.0384 | 2026-07-05 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 7a802fc3-c998-39f9-a8b8-4b4e6d4a4bad | -10.9405 | -43.0117 | 2026-07-05 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| b6a452c5-eecf-325d-8837-1a2133352638 | -10.9401 | -43.0355 | 2026-07-05 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 583.2 |
| 081a8104-ea10-3089-9742-9a4360d58d84 | -10.9593 | -43.0326 | 2026-07-05 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 694d2e4a-485d-3c4b-8be1-c7624509d9cc | -10.9205 | -43.0622 | 2026-07-05 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| ad55f55e-2f45-3ced-abbd-63c9329f8565 | -13.2404 | -54.3303 | 2026-07-05 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 375358b4-8ad2-3a7c-91b2-8bbef169362a | -13.2407 | -54.3096 | 2026-07-05 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 007b28f0-f320-38be-a6b7-f4063f3deacf | -13.2407 | -54.3096 | 2026-07-05 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0a9d5141-ce7f-3ffc-908f-4f282ac9f288 | -10.9205 | -43.0622 | 2026-07-05 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 827aeee8-657b-3c4e-8caa-fdc3fcb35050 | -10.9401 | -43.0355 | 2026-07-05 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 884.4 |
| 224e3809-ebb3-3bb6-9a3a-8bb3562e34cb | -22.1213 | -47.2765 | 2026-07-05 02:40:00 | GOES-19 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.0 |
| 63006dd7-1bfe-38fd-839b-2f0dcac8abb8 | -10.9397 | -43.0593 | 2026-07-05 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 315.1 |
| 9a678e9d-82cb-34e2-98bf-07b9138d6718 | -10.9405 | -43.0117 | 2026-07-05 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 7784fb00-e468-38d1-8207-daea3ed96271 | -10.9209 | -43.0384 | 2026-07-05 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 277.4 |


[Clique aqui para ver as próximas entradas](README3.md)
