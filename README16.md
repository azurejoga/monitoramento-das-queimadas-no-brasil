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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a3359c6-ec25-381a-82b1-a87dd3ed5b76 | -10.5579 | -52.0289 | 2025-06-29 04:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f2d38ca0-0a84-3d35-9222-abb247bd54c4 | -11.5309 | -52.7887 | 2025-06-29 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 402dfb5c-1fdf-35f6-8d07-59fea0858158 | -10.9811 | -45.1104 | 2025-06-29 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| f4257dac-75fb-39f7-84ed-033cc4be728e | -11.5502 | -52.7659 | 2025-06-29 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 620dea99-8f50-3485-914a-3653b789b05d | -10.5576 | -52.0499 | 2025-06-29 04:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| c6e24589-d7c1-3c67-82ec-0b50489e1b5f | -11.5499 | -52.7867 | 2025-06-29 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 5bc2936a-cba2-3290-9359-c937d453691e | -2.54714 | -47.70185 | 2025-06-29 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c63df16-e712-3152-b4d5-689ffa6a8ccb | -3.62508 | -47.54657 | 2025-06-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 881fa769-4c0e-3b5e-a6bf-9bf011855e68 | -3.94698 | -48.08922 | 2025-06-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1be4bf84-c5b7-3ab0-8579-e44a51598a21 | -3.62839 | -47.54708 | 2025-06-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26f0625d-8fac-3ecc-9f5e-410a56e99917 | -4.17199 | -42.03058 | 2025-06-29 04:29:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| eaf08032-3e24-3314-9d40-7bd9bb680fd4 | -2.75055 | -54.59361 | 2025-06-29 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 39abdd26-22a2-3ff4-be15-4830a1beb2dd | -3.58459 | -49.43655 | 2025-06-29 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d276c02c-a070-3030-8b42-a4c881d1a345 | -3.59149 | -49.43765 | 2025-06-29 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc43fcdf-2d9b-36df-a09c-ef1d05283f5a | -3.67711 | -47.43142 | 2025-06-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d1bd828-5640-35b0-8f45-9b5845587e46 | -2.75077 | -54.59481 | 2025-06-29 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7bb2df87-b13b-3477-b1c2-923825d3a99c | -3.78003 | -41.67927 | 2025-06-29 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af1fb318-f78a-31c2-90b7-548e2b621b33 | -3.42196 | -47.60592 | 2025-06-29 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9fec347-0d82-3ffe-9ad9-4ce8d5ed6ffb | -3.62893 | -47.54364 | 2025-06-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad224f84-a629-320e-9fdf-3acc71ad48fb | -3.62563 | -47.54313 | 2025-06-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53021792-9868-365c-b4e2-f8e2a64a3f01 | -4.38444 | -41.91485 | 2025-06-29 04:29:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ef64ac60-0cfa-3b78-9901-ebfe86a59145 | -3.77584 | -41.67859 | 2025-06-29 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b734c1e-0319-3ab6-b166-d7871b000884 | -10.5576 | -52.0499 | 2025-06-29 04:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 68770700-329a-3b16-a014-a7c8608f41fa | -10.5579 | -52.0289 | 2025-06-29 04:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f759069e-8cc4-323f-82f4-e3a76014d668 | -11.5312 | -52.7678 | 2025-06-29 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 42443bca-b923-3be5-91fa-bb7f75e0155c | -10.9811 | -45.1104 | 2025-06-29 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 7c90f503-f4cc-332e-a4bf-dc3dea35d10b | -11.5309 | -52.7887 | 2025-06-29 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 828edb8d-0d47-35c4-8e11-bac1b2aa3dbd | -11.5499 | -52.7867 | 2025-06-29 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 4f57d531-f07f-31a2-9d0c-887eaee19d07 | -11.5502 | -52.7659 | 2025-06-29 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 129.9 |
| a08e2406-37e9-3189-a85f-12287d89f0e8 | -7.09929 | -44.36364 | 2025-06-29 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 586f0a25-fd43-3133-983b-60146c4b2d50 | -10.29358 | -57.13324 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 904493be-7773-3e8f-b43c-4f12354278f5 | -10.56569 | -52.03423 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a425d74-c2e2-366a-90ff-d64f758bef84 | -7.40438 | -44.57624 | 2025-06-29 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e374562-3a90-3746-8b3f-f8980ba4a3bf | -6.62234 | -47.28226 | 2025-06-29 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 77eda0b0-7d5b-354b-878b-54f5fc4e2189 | -10.27442 | -46.29172 | 2025-06-29 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd609d28-75b1-3a51-85a1-d87532de2f50 | -9.98062 | -47.80414 | 2025-06-29 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94d1fb72-8fc5-34f6-a3cd-6421330b83a1 | -8.1228 | -55.08971 | 2025-06-29 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13f0c97b-7699-3a1a-a61a-39f4bb1deb92 | -9.42416 | -47.95502 | 2025-06-29 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0f091d1-119f-368e-8518-92ccdd2414ef | -10.5664 | -52.03006 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e5be127-717e-3b78-b24e-e35599d18581 | -10.87683 | -53.74849 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68ebe2eb-4f30-3c6a-b534-b8d26f252c38 | -9.11149 | -59.05381 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81afadd4-e6c2-36d0-b8de-3fd1437330f3 | -9.11224 | -59.04967 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5674aefa-e30f-32f6-a49e-bcb10536bb05 | -10.55472 | -52.04638 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3ec47f48-88c9-3b09-9bb1-98bec66bfefd | -6.62512 | -47.28626 | 2025-06-29 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6fda1d05-93bf-3e00-b272-4edd62310725 | -8.36493 | -51.07854 | 2025-06-29 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 056fd71d-1e5d-3ddc-9847-a018897ae451 | -7.18999 | -43.43341 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 89d3e811-2fcf-3692-946e-5c71ce1dc0c7 | -10.55402 | -52.0506 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 79a6be43-7b1c-3707-b086-713db72f604a | -10.82115 | -51.29329 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0891ea9-f38a-3da3-9ae0-5cf1fc255ccb | -5.74905 | -46.25579 | 2025-06-29 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 123b2a76-f131-377f-8722-f0ad48d51abb | -10.92762 | -44.15389 | 2025-06-29 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d8ffe9f-bc14-35a3-970e-26957ce61c3c | -10.85534 | -53.75508 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d855043c-371d-3144-b65b-cfecfd37fb0d | -10.56261 | -52.04341 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e511ae89-2377-3d8b-ab64-c47d71f1db3d | -7.19388 | -43.70169 | 2025-06-29 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7ccaca8-75e9-3609-b95b-2c36c3d35f45 | -5.57216 | -45.21176 | 2025-06-29 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e696da2a-517f-374b-ab8d-dbc1a41cd925 | -8.86908 | -50.16488 | 2025-06-29 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 995b1c83-febf-334f-8a26-87388ee81c13 | -6.62621 | -47.27929 | 2025-06-29 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f301d59c-5ffe-3616-a664-1917db482c7c | -11.83705 | -47.52819 | 2025-06-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ef4d5e8-2e00-33f7-b449-95dccd604f9b | -4.55518 | -48.00428 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3039cc66-70c5-39c3-9721-f63e3cc4a514 | -11.83819 | -43.80308 | 2025-06-29 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8cb99aa-e1d3-3df8-84a0-1c3ee9fbfbd5 | -6.62898 | -47.2833 | 2025-06-29 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c0a5ca72-28d5-324c-b8af-a607e720ee34 | -6.89598 | -43.98318 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b616297-dc1e-30d7-b584-3fc6bf3d65d7 | -9.70589 | -56.18763 | 2025-06-29 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1754ec1b-78ba-3d85-89d2-938d7c10e91b | -10.03219 | -54.33001 | 2025-06-29 04:32:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d43ba4f-eb0c-3d08-bac5-ee0d5caf24eb | -4.54582 | -48.02053 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74acca4a-fac6-3986-956e-ed310e81b956 | -4.53866 | -48.02295 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 468879e2-6266-3ab9-8d23-28bd7383c9f5 | -9.14312 | -46.38687 | 2025-06-29 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b505345b-6d76-3518-acd6-d38f5f6ac1e2 | -7.40794 | -46.33133 | 2025-06-29 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 664f7235-197f-345c-a418-61701af5277d | -9.42857 | -47.94853 | 2025-06-29 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 270c2660-4601-3087-96fa-70a47b7c8d56 | -11.88018 | -46.50425 | 2025-06-29 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a438f9da-0a35-3306-8b9b-04d2de5f3a8b | -9.70115 | -56.18681 | 2025-06-29 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4426cc90-7ba9-3890-920f-202057548da6 | -11.59146 | -44.66282 | 2025-06-29 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 078b1b9f-1989-3d5e-87fc-39a072653b4d | -10.56426 | -52.04261 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3ea0f5d-cb8c-3f87-9db6-d0652ca055ae | -9.08059 | -59.47334 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7537a3db-3539-3a52-a16e-cd4c2c1534aa | -7.55361 | -45.83228 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 189e532f-7fd8-32a2-a3ca-991a29d9b593 | -10.55749 | -52.02958 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ccd4937-d925-3980-ae24-191cbdf59b18 | -11.78924 | -48.29147 | 2025-06-29 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25f4292d-ec73-30bc-896d-e29e22de098c | -5.69142 | -50.04903 | 2025-06-29 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49f38fcb-804d-3a5f-a85f-e5483a1591b9 | -10.9269 | -44.15909 | 2025-06-29 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a002dbe2-3cc7-3cba-b972-afdf8a439596 | -9.11275 | -59.04926 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5822bd10-13ef-30a3-8b8b-a7a971dbc41a | -4.03596 | -48.06441 | 2025-06-29 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd1cd9f1-fc68-3257-a74f-a6c3fcff24bc | -5.74512 | -46.25888 | 2025-06-29 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b853fda-2974-3255-8b6f-220891ff66ae | -8.70969 | -48.22422 | 2025-06-29 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7dda733-8622-30a8-a8ba-ce2bfe561130 | -6.33029 | -43.75418 | 2025-06-29 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df1329f5-13cb-3358-8978-0befac63153a | -7.54955 | -45.83559 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e01b45f3-637a-3817-a14d-c483bfbbbe0f | -7.55072 | -45.82787 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01ebf344-7929-3cb2-8953-24728ed354d5 | -9.46615 | -40.34603 | 2025-06-29 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0c217d6f-5dcd-343c-9ca5-8bcc1f6ba16b | -10.79637 | -47.99387 | 2025-06-29 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf593846-adde-34bf-9a6a-88c7a7f0454e | -9.08736 | -59.47001 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69c08664-77a9-3671-8ac6-360414fb9774 | -10.52688 | -53.62822 | 2025-06-29 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77c599dc-574a-3af0-98dd-db3565b46705 | -10.86806 | -53.75216 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5df06ba8-108e-34e6-badc-2560ff695b2e | -6.62953 | -47.27981 | 2025-06-29 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f7b0f194-e462-3b26-a2ee-28f3fb22bff1 | -7.55476 | -45.84822 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d6d0b9d-c6c4-3588-b844-7a9ac24fc94b | -10.62067 | -51.79696 | 2025-06-29 04:32:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7ecb92e-a310-3e64-b778-2970fc4e82d9 | -10.95588 | -48.14936 | 2025-06-29 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85aa306f-f82e-3709-b564-933967710a61 | -10.5532 | -52.03315 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3e2205fe-90d5-3840-b5d7-d074d8c0fba5 | -10.55611 | -52.03797 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c0c8ae3d-ec21-36cc-b3ab-11bdf289bb89 | -5.16065 | -46.09246 | 2025-06-29 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 038624c1-d72c-33f8-9c95-1dfc5bf27165 | -8.37681 | -51.07237 | 2025-06-29 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0870f019-5523-30e4-a901-940d3754339f | -10.6529 | -44.49072 | 2025-06-29 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf87dbd4-2a59-3509-af80-eeda449a2828 | -4.45496 | -48.99451 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README17.md)
