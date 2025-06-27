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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b135ca2-85d9-31ec-9a86-2597a0d28844 | -6.9698 | -42.88728 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c6eb12b7-7095-37c5-b673-13b545665345 | -5.92334 | -43.47425 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d3e5ca3-2a04-30c2-b0a3-40ea3cd91029 | -2.28747 | -48.57478 | 2025-06-27 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e38c340-1726-37a3-b448-d01bb55f83cc | -6.77312 | -46.33075 | 2025-06-27 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc79e08a-5c7a-316e-87cc-2d34c05562cb | -8.67739 | -49.95555 | 2025-06-27 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 665ce858-1929-32e1-a13c-70de5f7f25ce | -8.67745 | -49.95329 | 2025-06-27 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efff323c-d467-39eb-9eff-f6ef7bf6d716 | -7.26277 | -46.94417 | 2025-06-27 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c6573d72-0ecd-314f-a269-444e6bb39ef1 | -7.5485 | -45.83825 | 2025-06-27 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f0488d39-dd96-373f-bda6-fc05313ffa91 | -5.91946 | -43.47728 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0b6df8bc-c12e-3ab9-9005-0c6eb5d08564 | -6.17627 | -48.08569 | 2025-06-27 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 762630da-10ef-3869-b588-cf552c164925 | -8.62883 | -47.4507 | 2025-06-27 04:19:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51c1f9df-5d85-3459-b53d-42199775aa6a | -7.09901 | -49.17699 | 2025-06-27 04:19:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 432215c5-1838-330d-bea1-7999a42b0fdf | -8.4892 | -48.26629 | 2025-06-27 04:19:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c25de621-2a69-3d4f-bd9d-a6caf811c891 | -6.36838 | -43.65531 | 2025-06-27 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6154d7f-37c9-3110-a15a-0e89a07f1b28 | -8.22736 | -47.2164 | 2025-06-27 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e5f7cd0-71c2-3929-bc2c-23c4325f0b9c | -6.77369 | -46.32715 | 2025-06-27 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d128feed-3418-36f7-afdb-ce571e7a5c12 | -7.53634 | -45.82917 | 2025-06-27 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ed77660e-1be3-3e7e-9d18-30c742785b4d | -8.67663 | -49.95827 | 2025-06-27 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6710d080-8fd1-344d-bb3c-8262e8b26c76 | -7.00455 | -44.59809 | 2025-06-27 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92e7a783-0b36-3a3e-b15d-920a2cdc3d60 | -3.02886 | -49.43176 | 2025-06-27 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0dc7c7b0-e303-3bcb-a1f7-c9c0fa7eaa78 | -2.28687 | -48.57692 | 2025-06-27 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5501a049-0c84-3a11-8b3b-07aa306c4d88 | -4.54408 | -38.3886 | 2025-06-27 04:19:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46d77a60-34b7-3c5b-8314-d457fd1da4e6 | -6.1806 | -48.08202 | 2025-06-27 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b1ee5108-3ea8-3b75-9005-750b56d32c8e | -6.77515 | -46.33137 | 2025-06-27 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd5fd1f9-d88f-37d5-a83d-53d70a3591ca | -9.07006 | -46.9101 | 2025-06-27 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46d5c981-2cfe-39ef-855b-283fec7ca5c0 | -7.54905 | -45.83475 | 2025-06-27 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bef12aa6-2681-35a6-b3ce-c03e9c8b3354 | -6.96865 | -42.8948 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 4181418b-350e-385f-bfe6-9f9bdcc2f2c2 | -2.54976 | -47.69833 | 2025-06-27 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cef5156-3130-32a8-8c17-a122ee5c5a2a | -8.37314 | -51.07345 | 2025-06-27 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b4707b8-4f48-33e3-855e-eebb2028c011 | -8.47783 | -48.26865 | 2025-06-27 04:19:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c11fa143-8f9e-302b-8959-71a707106f07 | -6.22322 | -43.36296 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0fe37dc-491a-363e-a4dc-97790eb695ff | -5.18009 | -46.10871 | 2025-06-27 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56197d86-0322-3ccc-a1c1-53913faa427d | -6.96179 | -42.89376 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| d8b873f9-22d5-3cd2-b268-eb06761b2375 | -3.03297 | -49.43241 | 2025-06-27 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5fb22a8f-2612-3530-952b-39c912b03080 | -5.90008 | -43.45223 | 2025-06-27 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df8d756f-a7e3-342d-ae2d-5794659ae1ac | -6.95836 | -42.89324 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| bb1ef949-e16f-3dc0-8bc5-751e28ac4cf5 | -7.15237 | -44.06185 | 2025-06-27 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9af9f275-b647-308a-8663-099ee1cf8b24 | -6.47596 | -43.75148 | 2025-06-27 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 62c598a9-3578-32c6-902e-c00f36ed22f5 | -8.22676 | -47.22012 | 2025-06-27 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d83d7cb0-5891-3486-b4ff-8215487b3a89 | -7.22031 | -43.08454 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a65ef6d3-8203-39a9-8ef0-2411ad7f6475 | -6.96407 | -42.90179 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 368b1e65-c476-3913-a4bc-421b880181a4 | -7.2169 | -43.08401 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a4a995ed-aeee-3b3e-8d68-f4e61af16bb7 | -8.48207 | -48.26511 | 2025-06-27 04:19:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ad3acde-5e8d-3647-bf01-7a08ea98c488 | -6.9658 | -42.89052 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| b88323a6-f33c-3aad-bfaa-497197d5fbed | -6.47316 | -43.74746 | 2025-06-27 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8154c79-c9ae-3be2-862e-8a8e1a337295 | -2.44154 | -47.46369 | 2025-06-27 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd98bb0e-8ac4-313b-8e12-1e6e12e8fac7 | -8.44191 | -46.97731 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a144fa1-b919-39e8-8b49-3f365e75ff0d | -8.47851 | -48.26452 | 2025-06-27 04:19:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38bf48b2-ecd4-3ab3-b493-6155daba9b3b | -6.4765 | -43.74796 | 2025-06-27 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f05df5fa-bb8f-3d65-bb99-75474a9174c6 | -8.16992 | -46.87372 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89d874c3-5abb-3d06-a14a-cd9f105d10f0 | -8.48987 | -48.26215 | 2025-06-27 04:19:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d08ba75-b303-33ad-9038-7bde73d01a07 | -5.02429 | -47.65977 | 2025-06-27 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 836602f4-ed87-304c-a04e-12d527606cc0 | -8.68477 | -48.31309 | 2025-06-27 04:19:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f819739-c0dc-3bd2-b555-b6ae1b22ef08 | -8.48631 | -48.26157 | 2025-06-27 04:19:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 106f8390-5e60-34f4-83d9-71713ba29216 | -4.81655 | -47.32289 | 2025-06-27 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32510109-034e-384c-b585-7c132ed3c115 | -8.73535 | -47.98271 | 2025-06-27 04:19:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b1a187e-40b0-34cd-947b-40b880158eab | -7.76997 | -44.44495 | 2025-06-27 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bcc6f9e-103c-3fce-b303-e0b973508c3d | -8.38084 | -46.96028 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4d992a9-6312-35a5-af8f-1bb9bb063d56 | -6.17264 | -48.08513 | 2025-06-27 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5fcd06db-00db-3f92-931d-8a1a8ef68d91 | -5.97593 | -43.75325 | 2025-06-27 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0058ec83-3a5b-36d1-b9d7-5962ad79bf08 | -8.55836 | -47.75403 | 2025-06-27 04:19:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f0b0554-a4d2-33b0-9869-fb5f591408b5 | -8.045 | -45.66745 | 2025-06-27 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adc1232f-013e-3482-90d2-129b8c338989 | -6.77793 | -46.33551 | 2025-06-27 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35a70ea5-4410-3d8c-9074-439d869a8e74 | -6.57537 | -54.99755 | 2025-06-27 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e4a7179-b12b-33b6-9f63-3ec2f811c204 | -6.34091 | -43.74503 | 2025-06-27 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7233eecd-c009-30a2-8b78-04f10c171596 | -7.21348 | -43.08348 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 40d04f2b-2856-3bbc-b021-b64cc100156d | -9.78916 | -36.99632 | 2025-06-27 04:19:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec265847-b6eb-3c86-830c-b87c9236c9e0 | -7.20062 | -43.19122 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0ec806b5-9e4f-3d3c-9fca-f23a9f7461d0 | -9.06949 | -46.91375 | 2025-06-27 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b13ed48-323a-3ee0-9f12-a9640e083402 | -8.48563 | -48.2657 | 2025-06-27 04:19:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 814d29eb-bfba-32c0-92fe-3a29e5559967 | -6.96637 | -42.88677 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 36d138ef-db6e-3a42-a510-a6728140c507 | -7.15183 | -44.06534 | 2025-06-27 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5084c9db-0383-321a-8848-3559fe5c7636 | -5.91837 | -43.48437 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c300b15-1fb3-3ea3-8ed5-19c379188000 | -6.97208 | -42.89532 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 61efc09a-10d8-335d-9fce-c150cacb911a | -6.95894 | -42.88949 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 11294c4c-8f60-3f4a-beef-161877949410 | -6.6578 | -47.58503 | 2025-06-27 04:19:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0619aa9-cb2a-3e13-88ed-a58b2f61d2f6 | -6.9715 | -42.89907 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.0 |
| aeb6bb10-f036-32cb-bc55-58ba1e4dd001 | -8.22334 | -47.21956 | 2025-06-27 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 19eeddd2-4fec-3ae8-972e-f929b71795a4 | -6.21986 | -43.36244 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd163815-f8ad-3d8b-9383-1bf3d99c88f0 | -6.96425 | -38.58007 | 2025-06-27 04:19:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5b9e734b-c4ce-3fba-8759-f66918a1cc0e | -6.77256 | -46.33435 | 2025-06-27 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca9418f9-fa02-32f3-a6bb-26e5472ac112 | -6.95493 | -42.89272 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 94654fbb-0375-3777-ad05-2fcafe9bb49e | -5.92054 | -43.4702 | 2025-06-27 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b1f9bf9c-3b39-3af4-b898-7e56495a0ff4 | -8.39745 | -46.92155 | 2025-06-27 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23aba1fc-834f-3b93-a4eb-6c2ca1e4f693 | -4.8172 | -47.31883 | 2025-06-27 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aed88a65-24dc-31a4-8910-3035a3456898 | -6.1799 | -48.08627 | 2025-06-27 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 7e51d00d-f59e-3e8e-a798-18cb193c27d7 | -7.21063 | -43.07923 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a301d705-6c90-30f2-a3c8-99ecf8e036f6 | -6.95436 | -42.89646 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| ddaeefe7-3270-33af-a58b-86c8d4ab1174 | -7.21633 | -43.08773 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 57d63467-e014-3454-8fc1-28802fcace58 | -6.9675 | -42.90231 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 3736bfda-cc4b-3955-94e4-4f5f56409c81 | -7.70393 | -47.80484 | 2025-06-27 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a967fd55-e1ac-394b-af66-c35ac345c9a6 | -6.96122 | -42.89751 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 315d2dfe-bc45-3f28-a5b1-2f914c1e445a | -5.97539 | -43.75676 | 2025-06-27 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcb1914a-6b5c-3418-b09b-00c1681e547d | -8.48442 | -45.49231 | 2025-06-27 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7d0a808e-edb5-37a6-bfec-e859a4a2cafa | -6.26609 | -40.62309 | 2025-06-27 04:19:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 69c60875-821c-372a-9e3f-194d556b0ffe | -8.22394 | -47.21584 | 2025-06-27 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbc17978-1b70-3bc3-969e-001181f7dc54 | -7.20778 | -43.07498 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 7b4309d8-b017-34ac-b25a-51f74240478c | -7.21405 | -43.07975 | 2025-06-27 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| ea0808ae-ae1f-37df-8a7b-1dd2a7f3d570 | -6.77573 | -46.32777 | 2025-06-27 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de2183c7-d868-3271-af79-7c5209b2b34f | -8.37736 | -51.07417 | 2025-06-27 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README11.md)
