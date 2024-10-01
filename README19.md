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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc53022e-ed00-3866-b9a5-13aa843a3335 | -10.9276 | -50.09 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9db7ec29-3d71-34f8-8603-348cdd4eff39 | -10.9144 | -50.077599 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55a18037-030c-3686-9057-ff97b95992bb | -10.9161 | -50.084999 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb0eaa3b-9904-3d29-91bd-6fb1d5eedaa5 | -10.9178 | -50.0923 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d38b7e70-3c51-31ff-ae4a-2b89ab752902 | -10.4561 | -48.196602 | 2024-10-01 00:52:03 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6323acd8-a59d-3387-a448-e007530d1129 | -10.4582 | -48.205502 | 2024-10-01 00:52:03 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 084167ef-2d24-3dd3-aaa1-7506ba153086 | -10.4442 | -48.190102 | 2024-10-01 00:52:03 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abfa65f9-26ad-3962-82f9-6232564d1c2e | -10.4463 | -48.199001 | 2024-10-01 00:52:03 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6692e869-94dc-3adf-91b3-4adf74751470 | -10.4484 | -48.207901 | 2024-10-01 00:52:03 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96984ae9-ec72-3f90-865f-01d858afc135 | -10.4505 | -48.216801 | 2024-10-01 00:52:03 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dff65483-7a58-3f9e-98fd-c87f03d47c8a | -10.4526 | -48.2257 | 2024-10-01 00:52:03 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50a219d6-9dd5-3ea2-8b91-8e1b885a0099 | -10.3988 | -48.1726 | 2024-10-01 00:52:03 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b316df2-7eb0-387a-b664-64a24cbe984e | -10.4394 | -50.7976 | 2024-10-01 00:52:13 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 550c78ff-357a-30cd-aaa5-2f12e78eadee | -9.6331 | -48.515202 | 2024-10-01 00:52:17 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9db50377-ceb5-3638-ae28-89564a402c57 | -10.043 | -50.2808 | 2024-10-01 00:52:17 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 444b0834-e88e-3924-8a9a-6f486620726e | -10.0447 | -50.2882 | 2024-10-01 00:52:17 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a8b1bb8-b1fc-39a7-ad78-d5260f21f824 | -10.0464 | -50.295502 | 2024-10-01 00:52:17 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 595a5b61-fad5-3328-9bd7-22943258afbb | -9.5806 | -48.9077 | 2024-10-01 00:52:19 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 208856c2-507e-3417-988a-a37bf0b82160 | -8.5171 | -44.698601 | 2024-10-01 00:52:20 | METOP-B | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eadd2c1f-20c6-3321-b7fb-d1d66e17071f | -9.5803 | -50.106998 | 2024-10-01 00:52:24 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d9e14e4-5933-38e9-b5de-f5250147398a | -9.582 | -50.114498 | 2024-10-01 00:52:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0137e66d-567f-366c-a866-7f90e9d4dcb7 | -9.5705 | -50.109299 | 2024-10-01 00:52:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0af81ca3-dd5c-3f05-a665-19c5734c6202 | -9.5877 | -50.184101 | 2024-10-01 00:52:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be1ddc8e-e876-3f08-9ac3-9269b380e037 | -9.5715 | -50.2034 | 2024-10-01 00:52:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74315a99-362e-3bd8-ac0e-b97cf8453af7 | -7.8332 | -43.067101 | 2024-10-01 00:52:25 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0b4bf979-7708-359d-b875-a2d31dc2339e | -8.7614 | -46.802299 | 2024-10-01 00:52:25 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63847e34-1e04-3927-9f79-8888fef3d53f | -9.1974 | -48.637299 | 2024-10-01 00:52:25 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e85f90d-4cd7-3ef1-953e-203ba0c28b1a | -9.1994 | -48.646 | 2024-10-01 00:52:25 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19ffa3a6-6104-3a14-8510-201ee21a2ca5 | -9.2015 | -48.6548 | 2024-10-01 00:52:25 | METOP-B | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 094fa101-b0be-35de-8794-6fd07f4c500d | -9.6608 | -50.909801 | 2024-10-01 00:52:26 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c54f283b-40f4-3891-a283-50449ec665d8 | -9.6624 | -50.916901 | 2024-10-01 00:52:26 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24b627be-2211-35fe-ba9e-87a479d15eb0 | -8.7427 | -47.111198 | 2024-10-01 00:52:26 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56dd8c61-3a1f-34fc-a42d-c1380de5e802 | -8.733 | -47.113499 | 2024-10-01 00:52:26 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9291188-e534-3c61-aa88-09e73dfda083 | -8.7356 | -47.124401 | 2024-10-01 00:52:26 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82e18045-7515-3c6a-8aad-613809d7ad41 | -7.676 | -42.972401 | 2024-10-01 00:52:27 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fdd5c9a2-f37b-35a2-80a6-2411760b5bd1 | -9.1366 | -48.9506 | 2024-10-01 00:52:27 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 669e2a47-d8b0-369f-b076-fd63d8f3ddc0 | -9.1386 | -48.959 | 2024-10-01 00:52:27 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee7da42d-8ae3-3b23-94fb-1a409e76f8fa | -8.8019 | -48.931198 | 2024-10-01 00:52:32 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 912da16d-b198-35d7-9571-071963bc8e14 | -8.8039 | -48.9398 | 2024-10-01 00:52:32 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca9603f9-87af-3aaa-9cee-7eb1cd83b39b | -8.6543 | -49.404499 | 2024-10-01 00:52:36 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f95573df-50cc-34a4-b69c-877448d3d9e1 | -8.6562 | -49.412601 | 2024-10-01 00:52:36 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dce364b1-9373-323f-b0fb-7526eb7e9b45 | -8.6581 | -49.4207 | 2024-10-01 00:52:36 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 572a08eb-7c0e-38e4-a264-fc440f8253b2 | -8.5529 | -49.5896 | 2024-10-01 00:52:39 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd87a132-b9fa-3921-a1e7-07c2553e734a | -8.5548 | -49.597599 | 2024-10-01 00:52:39 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 142fd19c-007a-300f-aa50-a87fb0155dbe | -8.5431 | -49.591801 | 2024-10-01 00:52:39 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c0adbd9-b920-372a-96f4-c4f3f48935e9 | -8.545 | -49.5998 | 2024-10-01 00:52:39 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 520c3343-af6f-3a6d-a742-912323a6a08d | -7.7143 | -46.135399 | 2024-10-01 00:52:39 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5257adc8-8c20-36dc-b98f-0271bedff494 | -7.7174 | -46.1483 | 2024-10-01 00:52:39 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3aca8d20-b4b5-3c87-890b-7e2fe597e745 | -7.5724 | -46.0172 | 2024-10-01 00:52:41 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86c33e66-ea4a-307a-a3c5-20ddb21e0973 | -7.5756 | -46.030399 | 2024-10-01 00:52:41 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7d2707c-d444-30a0-9571-6f7b4494c0aa | -6.6817 | -43.015999 | 2024-10-01 00:52:43 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7e14aa3-9efa-32ee-a4ff-45ffb4475557 | -6.6872 | -43.037998 | 2024-10-01 00:52:43 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a37c7d41-2f41-362a-933d-8ab3439ac4f0 | -6.6721 | -43.018398 | 2024-10-01 00:52:43 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c9b791e-d919-30f7-bd99-fc890293a3b0 | -8.0059 | -48.308601 | 2024-10-01 00:52:43 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63aa8ef0-220f-3fcf-9dec-dbec52a67fec | -6.5261 | -43.008099 | 2024-10-01 00:52:46 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62a3e978-94e7-3cfc-9b77-d7b30c6c9f0a | -7.0508 | -46.847099 | 2024-10-01 00:52:52 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9400104d-1bee-3736-83b4-54e4abb4dcb6 | -7.0536 | -46.858898 | 2024-10-01 00:52:52 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8dc3dbe9-8671-3ff1-910a-1f59b7484577 | -7.6303 | -49.702999 | 2024-10-01 00:52:54 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a99a86ae-b842-311b-aadf-0e3a782c2f65 | -6.2358 | -44.1175 | 2024-10-01 00:52:55 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5846582d-756d-3db0-a844-50230b4b9c9e | -6.2404 | -44.1362 | 2024-10-01 00:52:55 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05322af0-2f98-37cd-a35a-5bb21746848a | -6.2216 | -44.101002 | 2024-10-01 00:52:55 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a43e5158-fe49-3b54-9e1c-fb6be16fbb39 | -6.2262 | -44.119801 | 2024-10-01 00:52:55 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e8ff8ac-fd61-367c-8b12-e038310244f4 | -6.2308 | -44.138599 | 2024-10-01 00:52:55 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1f2cd32-583e-3269-be74-ce761577df85 | -6.9732 | -47.603401 | 2024-10-01 00:52:57 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a81c8b0-fe74-38b4-bd1d-d8806b4ef950 | -6.9608 | -47.595001 | 2024-10-01 00:52:57 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 636f6330-bfa2-3ce0-8e62-33fa0a5afa1f | -6.9634 | -47.605701 | 2024-10-01 00:52:57 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 943bce11-f692-32db-9d0f-46744841f1ea | -6.9659 | -47.616299 | 2024-10-01 00:52:57 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4636bd09-fc76-3846-a663-c94d9927771a | -9.198 | -58.175999 | 2024-10-01 00:52:59 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9372560-0794-3f8c-b434-11c0d87111cc | -9.2005 | -58.188099 | 2024-10-01 00:52:59 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f858bcb6-a371-3a1e-9df0-bfd33556b8a3 | -9.1883 | -58.178001 | 2024-10-01 00:52:59 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93fc737d-1c36-34ec-8fb7-dbe38f96caf4 | -5.7313 | -44.32 | 2024-10-01 00:53:04 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba1cb90-5e15-3bea-ac0c-e7e23d6ae1f8 | -5.9687 | -45.3414 | 2024-10-01 00:53:04 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f6ae70b-5531-366d-a3ac-6f4679cfc519 | -5.9725 | -45.356998 | 2024-10-01 00:53:04 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc0778b5-14d0-351f-bcfd-4a946e829f4d | -5.959 | -45.3438 | 2024-10-01 00:53:04 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c84a744-6f93-3b2d-b719-dfffc4717d02 | -5.9628 | -45.359402 | 2024-10-01 00:53:04 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62419187-dea4-3149-a55d-db4d49a5a419 | -5.7558 | -45.523602 | 2024-10-01 00:53:08 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 303fcd76-3120-3368-8a37-a3800ec44f3f | -5.7594 | -45.538799 | 2024-10-01 00:53:08 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02cb4e94-1619-36c5-881a-006ed288dc23 | -6.0139 | -47.4245 | 2024-10-01 00:53:11 | METOP-B | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f519fb7-6ae7-3463-9f44-2ca812613564 | -5.3673 | -47.694801 | 2024-10-01 00:53:23 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cfea625-80fc-3599-a945-8b0704d4deb4 | -5.3699 | -47.705898 | 2024-10-01 00:53:23 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8480697-b10f-33c2-9bed-48cb394838b0 | -4.7027 | -49.7934 | 2024-10-01 00:53:42 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7e44f54-ccbe-376a-902b-0b330b208024 | -4.6909 | -49.786999 | 2024-10-01 00:53:42 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25edb9b2-895b-3976-97a7-4f9067879349 | -4.6929 | -49.795601 | 2024-10-01 00:53:42 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e89fcbb6-17f1-3f9a-94ad-e38bd27e778f | -4.6949 | -49.8041 | 2024-10-01 00:53:42 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e92c84df-24da-3ff4-9175-90c3417e039e | -4.6453 | -50.978199 | 2024-10-01 00:53:47 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c5d8773-83cb-3fae-85a7-3dd1e20f3fd7 | -4.647 | -50.985699 | 2024-10-01 00:53:47 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d766363-ca87-393c-9d30-eaedbe846c2d | -4.6355 | -50.9804 | 2024-10-01 00:53:47 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e526a8e4-9de8-308e-8d15-97a5b0610374 | -4.0867 | -51.1045 | 2024-10-01 00:53:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9cea1b1-526a-3e01-9464-1b71422695f6 | -4.0884 | -51.112099 | 2024-10-01 00:53:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b986c9b3-80c5-3271-8a1f-905040c56ee0 | -4.0902 | -51.119598 | 2024-10-01 00:53:56 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22b615cd-caef-3696-be7d-844b40dfb001 | -4.1624 | -53.8479 | 2024-10-01 00:54:05 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2568c6c0-dd50-3390-8443-c6caff9497e7 | -4.1634 | -53.898201 | 2024-10-01 00:54:05 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 042c00f5-287c-3cf2-bd0b-b4713c9ea645 | -4.1649 | -53.904999 | 2024-10-01 00:54:05 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2ef80b8-fa62-3b92-82b9-0e5af561a30e | -4.1665 | -53.9119 | 2024-10-01 00:54:05 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 673e2e93-d793-3e13-8a5f-ad8306b324e0 | -3.105 | -49.3862 | 2024-10-01 00:54:06 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 118d101f-03cd-36fb-83b5-a6a6dddf576e | -3.1072 | -49.395599 | 2024-10-01 00:54:06 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 463f2360-ff2f-31ca-9323-3d611fe37284 | -4.0071 | -53.752899 | 2024-10-01 00:54:07 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f52558c-0949-31f1-a229-3eb667fc3dc9 | -4.0086 | -53.759701 | 2024-10-01 00:54:07 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81ea0735-0880-3263-b0a4-fb52d2050b6b | -3.2117 | -50.432499 | 2024-10-01 00:54:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd1bd87-a60f-32ce-a1ad-44e443bc89c2 | -3.2136 | -50.440701 | 2024-10-01 00:54:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README20.md)
