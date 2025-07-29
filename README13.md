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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5c49a97-4bbf-31e7-828b-b0053d4d3b54 | -8.95714 | -46.75281 | 2025-07-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b749bcf4-e887-3911-8966-c44ddce700c7 | -14.32189 | -54.15757 | 2025-07-29 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b52792be-4c76-3964-af1f-d590b50d39c6 | -15.12254 | -45.33591 | 2025-07-29 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53a43be0-c70c-33f4-be75-83dd8ae1a863 | -11.42845 | -45.13055 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| fd6ede7d-4414-39cc-825b-a59b8dc3f06b | -11.98924 | -46.70383 | 2025-07-29 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d58fcc6c-7d55-352f-b0ac-bd3e4fa0661b | -9.36492 | -45.74568 | 2025-07-29 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 812f118d-70a7-35cf-a419-3b12ae14235c | -14.13155 | -45.28835 | 2025-07-29 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3d83052-0be0-3745-8c94-842d8fb13da1 | -11.55986 | -47.32565 | 2025-07-29 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ad25c99-0954-304c-8d76-6593dfc4c792 | -10.42995 | -47.22596 | 2025-07-29 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| beec3f41-d56c-3330-bfa2-499252a95bce | -10.44646 | -49.34594 | 2025-07-29 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8740f8d0-aa97-3b71-aee7-2854c14cd043 | -13.52071 | -45.62224 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 186f9c9b-6b62-338b-a389-985186374612 | -13.08995 | -47.31182 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0891e8ba-8f4c-334c-88ef-c3b4d037a186 | -11.17317 | -48.62617 | 2025-07-29 04:21:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a454972-c98c-3ef0-a30b-4124e2228875 | -8.88746 | -47.34292 | 2025-07-29 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccdc4081-a7ea-3ad0-acb5-3413eec3d889 | -10.55104 | -50.24466 | 2025-07-29 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3cc7631c-e290-3b6a-80ba-b326ee3b9820 | -10.6279 | -45.23237 | 2025-07-29 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69931b9a-85c4-3314-a047-0c5af4b4fda7 | -14.48319 | -50.28915 | 2025-07-29 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1fa8c1b-36a8-315e-b570-6fc604708568 | -9.3649 | -45.72427 | 2025-07-29 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7c14825-3c1e-32f0-b011-a262ba3c80b7 | -14.2259 | -43.95298 | 2025-07-29 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 246fafcd-8bc7-38df-84ac-4830afca9f44 | -14.35218 | -47.09756 | 2025-07-29 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fcb9422-3a2f-3144-9dc5-a5e48165931b | -9.57648 | -44.44339 | 2025-07-29 04:21:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 58997326-9217-382e-8a71-34a0bbb326f7 | -12.71013 | -47.79271 | 2025-07-29 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6425ac92-b37d-38c0-82c1-c707aea6704d | -13.09385 | -47.30879 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12281c13-7004-328b-84ad-97c1b4adfb7b | -10.72663 | -51.58278 | 2025-07-29 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c08c5454-6fdd-3941-a158-ec8ed0c4de27 | -12.99913 | -44.89473 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c55282dc-7800-3115-9aa6-5488d81baf5b | -10.52209 | -42.55236 | 2025-07-29 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| e3b796ae-5a86-314f-baf6-43ca4bebaa8c | -9.709 | -48.61202 | 2025-07-29 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7dab4688-0e6b-3e4b-84c1-b9bb0366b3f5 | -14.37474 | -50.33039 | 2025-07-29 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 380bd09f-00e4-38cf-a133-4b02f6d8fb67 | -14.13491 | -45.28888 | 2025-07-29 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a2f23e6-526b-38ea-af70-2412d56c511d | -9.31736 | -44.84924 | 2025-07-29 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2d33275-8e7f-3929-bdd6-2488b19068c2 | -14.48685 | -50.28981 | 2025-07-29 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb41c13c-fee6-3913-8bc0-6dfe2afa2042 | -11.51953 | -54.68316 | 2025-07-29 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd63380d-c4bb-36fd-932c-ba6a5c69bd68 | -10.96418 | -49.57241 | 2025-07-29 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 624356a2-e437-323a-84e3-b691259b9e2e | -13.10903 | -47.3851 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a83cde0-ebbd-3822-b848-dc300394bed8 | -9.59103 | -44.46033 | 2025-07-29 04:21:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25ecd029-bfd2-30df-9754-a02dba760929 | -13.48889 | -45.56602 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 049c611c-0657-3d68-91d3-83a1f3320fed | -9.1192 | -47.64659 | 2025-07-29 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9633c30b-2b96-3ce1-860a-f7c6bb9f8a67 | -10.63074 | -48.09036 | 2025-07-29 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df0dc23e-79d2-3faf-9d24-dedce9658e5c | -13.2506 | -50.13203 | 2025-07-29 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa145aa1-55d0-3fc5-b23e-6bca46e24cd3 | -14.48394 | -50.28469 | 2025-07-29 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4de9078-2c76-3086-9590-3fd5d30f794b | -13.49675 | -45.62607 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87b9f631-ad5a-3792-b70f-a54631b6fa20 | -13.00533 | -44.89945 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17a0a4f0-e63b-3a3a-bd3a-782a23e8838c | -13.76525 | -56.12603 | 2025-07-29 04:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb1bed29-cf28-3a5c-9619-b990e992254e | -11.37615 | -49.00048 | 2025-07-29 04:21:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bd66c7c-9a48-352a-8aa7-a9f7aa997d66 | -13.48834 | -45.5696 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df152368-1ee6-307f-9275-0c681b9a58df | -14.88213 | -48.39576 | 2025-07-29 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98f7687d-7c46-3865-8c40-6c202d5121f2 | -8.37059 | -51.07437 | 2025-07-29 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88616431-2ee9-304b-b6e4-adb8b9ce23cb | -12.99521 | -44.89789 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8d2cfba-9ea2-375a-9e37-b8c2426960e6 | -9.23035 | -43.15429 | 2025-07-29 04:21:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 65310767-cc3b-349d-8785-01dd0555a1b9 | -14.35605 | -47.09456 | 2025-07-29 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87eb42f1-dc1b-3d27-be12-848aeacb688c | -13.4973 | -45.62248 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 908033d3-7b92-3ad3-a4df-1caed4a0f9a9 | -12.00105 | -46.94919 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd9bead6-8bfc-3f21-9547-005c7681b8a7 | -14.74112 | -46.30542 | 2025-07-29 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d2cea34-d160-3583-aa02-bdcb5339e74b | -13.06738 | -47.36724 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddee8a6f-e74d-3040-887f-e5c4f2f9d274 | -11.43287 | -45.12397 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 2cc9adc1-7dca-3d3c-8f0a-93427e8c3f64 | -14.74166 | -46.30186 | 2025-07-29 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1915ebbb-ad18-3ba8-8182-0ced48625f56 | -12.99858 | -44.89841 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24939014-2d25-3c72-a5c5-e270fe102397 | -8.94372 | -46.7506 | 2025-07-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 26f0844a-0111-3fd3-b347-96ec6bbf7d81 | -14.3483 | -47.10057 | 2025-07-29 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13b1c768-e376-371d-bec5-d6cbe7f8e53a | -12.77059 | -47.85604 | 2025-07-29 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2f482a5-8d2b-3d3a-8c92-b481cf492b1c | -11.42791 | -45.13408 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 8eb32d86-d4a7-34b5-aadc-58f107c93723 | -13.24094 | -49.83747 | 2025-07-29 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d72e8b6-77d6-30bb-8386-f37a99d8447b | -11.74403 | -48.18237 | 2025-07-29 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b4e97617-ae79-3e95-9351-6f9dcfe353d7 | -13.00809 | -44.88104 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5997ea67-b463-39dc-a6cc-19c089d7ff90 | -9.73135 | -48.32337 | 2025-07-29 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 485a6553-ba27-3388-8f30-c4e303d71fea | -11.57334 | -47.89396 | 2025-07-29 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96b6db4e-8cc6-31cc-b835-10d9f2a2f2a3 | -12.00048 | -46.95274 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f17aaab1-5ee3-3b5b-ad8e-5636e5a7682d | -8.95379 | -46.75226 | 2025-07-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 8e4f8ce1-ec58-35ab-93a8-7196a7e3f191 | -13.00306 | -44.89158 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 104296c1-6c85-3871-8329-f8cfc544f9c3 | -9.99615 | -48.12627 | 2025-07-29 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d294a2cc-8f93-3f34-87f8-007fecea2165 | -14.50755 | -46.54051 | 2025-07-29 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0912e561-4d1b-3204-a009-8782b160efe8 | -11.69018 | -47.42879 | 2025-07-29 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0325573c-d0b7-3b01-b351-8c1e88c1bba2 | -13.01036 | -44.88892 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39e45d86-f0c8-3986-b800-f03a58f55c34 | -10.71686 | -49.48433 | 2025-07-29 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f4252c3-31fb-3280-97f7-11a1f2d827ec | -14.50038 | -46.54298 | 2025-07-29 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e176ebc0-26a5-39b3-8053-1dcd894f7119 | -10.41647 | -47.22379 | 2025-07-29 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 341b9a45-585f-3a5d-9824-c973062c1b99 | -9.39778 | -45.49054 | 2025-07-29 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bfa9a029-bc92-3f8b-be75-371d1dd3a307 | -14.13265 | -45.281 | 2025-07-29 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57dafb35-33ca-3f9c-9c3e-4e8439e436c4 | -13.13751 | -47.35335 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c8d1054-fd9d-3bd5-bc33-ff4b20f69eaa | -14.48976 | -50.29494 | 2025-07-29 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e437b7e-7198-3e49-8ab0-e3b9457e2c08 | -14.22001 | -43.94378 | 2025-07-29 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1dc1b41-3db2-379a-87fc-072048656d0e | -13.48504 | -45.59115 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89356692-2f0a-3b31-aa4d-c3ca47daea1b | -9.84925 | -44.70431 | 2025-07-29 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0e48fdc-8632-3df6-a245-75d45a12e763 | -11.5227 | -54.68356 | 2025-07-29 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13b32a2b-1722-34ca-9a2f-862921111a8e | -9.74446 | -48.66445 | 2025-07-29 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 508d5b92-7714-3653-9929-d9cb51bb7027 | -13.48556 | -45.56549 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa83ff63-5365-39ae-957b-3a3c8d981058 | -14.12819 | -45.28781 | 2025-07-29 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf894019-53a2-346b-9616-ccd58cb5068b | -11.99991 | -46.9563 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39b19f43-f50a-3215-b405-fe2e4ef87ef4 | -12.99238 | -44.8937 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfced605-a9db-3aa5-88ce-6fb7fc018de0 | -10.51294 | -50.25823 | 2025-07-29 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c78878ca-14a6-31b8-8268-55b96a644908 | -12.67198 | -44.02848 | 2025-07-29 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84f9b73b-c842-30b3-a5dc-f43002a3bb03 | -11.42954 | -45.12345 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| bdb2c18d-6556-3556-a0e4-7f5b42b116c7 | -14.8309 | -47.23191 | 2025-07-29 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc02da59-bdc7-3463-8caf-10740a8cf8c2 | -10.52147 | -42.55663 | 2025-07-29 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 6b631d74-efdc-30ef-8248-81218494dde6 | -12.00096 | -46.97108 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81922a4f-cb91-3eb1-a505-9968dcfd5644 | -11.99763 | -46.97053 | 2025-07-29 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7a66303-5626-3f62-9f75-ed3ce67410da | -14.22648 | -43.94893 | 2025-07-29 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05180dea-9bee-37e3-96e5-fbb14f8d42f1 | -13.09328 | -47.31234 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 040086cf-e2c9-3745-be2d-e93b5f72eec2 | -14.50466 | -42.23544 | 2025-07-29 04:21:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0cc795b7-edaa-362f-a354-58c36609da15 | -11.6896 | -47.43243 | 2025-07-29 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README14.md)
