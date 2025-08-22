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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e249114-7108-34ae-8606-2454b4e91b26 | -3.23039 | -46.78869 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e5c76ad-2111-35dc-a045-d6e304c808f5 | -4.77961 | -45.32036 | 2025-08-22 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| be7c4d8e-9bdb-3812-9850-cb5fddb1bce3 | -3.98577 | -43.24382 | 2025-08-22 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e5c7b7a-4703-3ce5-8020-5451ed801df3 | -3.98158 | -42.52719 | 2025-08-22 04:17:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| b1e4910e-3920-32fe-b74f-0c76d9278d2a | -4.40443 | -44.08419 | 2025-08-22 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96de79fd-cfb9-359c-bba4-9f45320fc182 | -5.48822 | -42.15837 | 2025-08-22 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ec7c5ba9-df1d-3c52-a756-e6cb83aa861c | -3.04024 | -49.44331 | 2025-08-22 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d61af81f-22c7-38ac-922a-6aaaabee35d4 | -3.98243 | -43.2433 | 2025-08-22 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c5c6748-a4ca-31f9-872e-81bc8156970a | -5.38612 | -42.34687 | 2025-08-22 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 103a32dc-dba2-37a6-aa4c-f4d54b9f311b | -4.4782 | -47.67105 | 2025-08-22 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4efa4ae9-dc32-371a-af88-1c62bbf62b99 | -2.46849 | -47.76488 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eaefe410-89a5-3dec-9a69-ec5ead2e124f | -4.66406 | -46.39607 | 2025-08-22 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d47c322-0280-32d1-bc41-e6fa5b2bec0c | -4.65546 | -41.41397 | 2025-08-22 04:17:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 895c0ad0-f458-374b-8a1d-e10c3c2e7497 | -3.17306 | -49.47661 | 2025-08-22 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8571cd5-0ebd-3d14-883e-74977f7c7a64 | -2.93124 | -53.69904 | 2025-08-22 04:17:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8fe64409-e3a2-3e65-a522-7ba9104c2ea7 | -4.07671 | -46.93161 | 2025-08-22 04:17:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2736df96-f15b-349b-9687-84b4203e7eaf | -3.98916 | -47.88788 | 2025-08-22 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c36a2dd6-31dd-3078-9725-43b1d955e1f7 | -4.40058 | -44.08713 | 2025-08-22 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90dd3f7b-d78c-319a-87b0-86edc5680475 | -3.23392 | -46.78926 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db0285fa-7c49-34e9-92b5-5209b5f17498 | -5.37752 | -41.22094 | 2025-08-22 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 198f5c19-55c9-33be-a4a7-4130ea9a37ef | -3.83097 | -47.73514 | 2025-08-22 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 525c83c3-78ea-3407-9840-d0c7dace6339 | -3.26339 | -46.91972 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86eb20ee-6b06-3c4a-9ee7-a0e9a23bd1aa | -2.38785 | -47.66169 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf0db627-bc5c-3dc3-bfc6-ab8c63567355 | -3.42755 | -43.33969 | 2025-08-22 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 748e4d0b-657b-3bc8-a032-616b38adfede | -4.65187 | -41.41354 | 2025-08-22 04:17:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97cb48af-63f9-33e2-ba29-b5663462efcd | -2.11374 | -47.11885 | 2025-08-22 04:17:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9c76996-5c3e-34ce-b9af-e3e5fb44789d | -5.48762 | -42.16224 | 2025-08-22 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4aeda12b-4459-3ac5-a29d-b8dd0bae15b6 | -4.31122 | -48.09739 | 2025-08-22 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0552ef8a-a27e-3b5c-ae8a-2b7605c44fbc | -2.45187 | -47.74817 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 871ff77a-0212-3ca6-83e6-99a04de2a510 | -4.39396 | -44.08609 | 2025-08-22 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aef3246-0b8b-3afa-afcf-41f77e006263 | -3.59452 | -49.44436 | 2025-08-22 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3206ac2f-b2dd-3d1f-a962-37a3e125b5b5 | -2.47152 | -47.77008 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| edd72c0f-70a0-3f11-a263-236a7a5bc0d1 | -3.96531 | -47.88109 | 2025-08-22 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4392cf1f-6a99-372c-9b73-20ee4af613cf | -3.42477 | -43.33569 | 2025-08-22 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29c466d2-f6e5-3207-9713-5cda35b18e4f | -5.48881 | -42.1545 | 2025-08-22 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6aaf733b-30c9-317e-b7b4-2d1bb4086636 | -2.69242 | -48.20832 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf68c5ec-79b8-3cb3-93bb-38fe67441c1c | -4.77572 | -45.32333 | 2025-08-22 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a580042a-5763-38f2-bca1-f5224e040421 | -5.42032 | -42.89049 | 2025-08-22 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 95ca0463-103b-33b2-8807-6707f04432f6 | -5.38179 | -41.2173 | 2025-08-22 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 062cafee-3688-3314-b19d-85526ced495d | -3.04266 | -49.42832 | 2025-08-22 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d171954e-7a6c-3a22-9f1c-1c92f29375d1 | -5.3848 | -41.22203 | 2025-08-22 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4a09941c-dccf-3446-b694-e0e4e353724d | -3.81618 | -41.57746 | 2025-08-22 04:17:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e91b021e-ce74-39f5-b9de-7819469a1760 | -4.39129 | -47.76772 | 2025-08-22 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc2d5a49-f0ac-3f53-8449-7c340a99e729 | -2.46777 | -47.76941 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b78589a6-c232-38e3-b62d-336fc8508d3c | -4.14333 | -46.45069 | 2025-08-22 04:17:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2e0225b-c885-3ae4-a527-42de72622899 | -4.77239 | -45.3228 | 2025-08-22 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68d58e9b-147d-3de2-8bb6-8487439e3405 | -5.4917 | -42.1589 | 2025-08-22 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de21dee4-5af7-3062-b4fa-b5dd4fd6f9b6 | -2.38551 | -47.65915 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bda31cf-5cbf-32cd-98a6-b97edbef8e7a | -5.25284 | -40.73458 | 2025-08-22 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cce7e605-15ea-33b3-bdb2-7d8c9b6bd306 | -3.4785 | -48.93259 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b2996f2-e56b-3327-bf79-7bc8ccd5e31e | -4.39727 | -44.08661 | 2025-08-22 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a9890ce-68ca-3917-a264-dca1d981cd2d | -2.45937 | -47.74947 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 650db091-cb01-36df-853b-15f61e6bc947 | -4.93997 | -42.89555 | 2025-08-22 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc901046-062a-348b-acac-1664af677987 | -3.59332 | -49.45178 | 2025-08-22 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c08788b-605c-32ae-abe0-55a121aa1b02 | -5.42019 | -42.37067 | 2025-08-22 04:17:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9af564ac-dbb8-3bc1-b18c-432032d53d68 | -2.47224 | -47.76551 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 67e6c3af-80cc-3b67-80a5-96a3eec69b8c | -3.81919 | -41.55786 | 2025-08-22 04:17:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| afb45b43-c18b-31dc-94d0-f85a79be6459 | -3.81738 | -41.56964 | 2025-08-22 04:17:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 69f7cb52-92fb-3a82-96af-47000eb4050a | -2.47248 | -47.76845 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| b24d35d0-8a43-31e3-987f-b0442173db4f | -2.30522 | -48.1493 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5105a8d-9db0-3424-b02b-7e10c03478db | -5.1844 | -42.85447 | 2025-08-22 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c57a399-f471-3cba-8024-90e1c744bd55 | -5.13196 | -42.94665 | 2025-08-22 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccf705f2-567a-3047-8c85-2eac6fb44e2c | -3.23102 | -46.78472 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6d8c614f-cd7b-31b6-8c30-e9893cd69a95 | -2.47173 | -47.77303 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f2c8bee8-b718-335b-8f0a-0c0dc423dd83 | -4.39673 | -44.09006 | 2025-08-22 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37352ac2-5039-3165-928f-86003bc2cf42 | -2.84538 | -48.78574 | 2025-08-22 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3acbdc7d-9873-3185-8062-bd626fdf3670 | -5.13931 | -45.17378 | 2025-08-22 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbab2347-dbe3-338c-bc7f-4ee9be79f71c | -3.7297 | -49.68465 | 2025-08-22 04:17:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 486417f2-7b90-3162-b406-33dc73043b91 | -2.94107 | -49.46661 | 2025-08-22 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93bb1abf-eed1-38e1-bc0a-2f29831448dc | -3.45564 | -39.59669 | 2025-08-22 04:17:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a5d77514-84d8-3f2e-8326-b1e6aa9b5ebf | -2.30216 | -48.14389 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b081674-f3dc-374a-b68c-d24db49f41f6 | -2.93752 | -49.46216 | 2025-08-22 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06ee8994-a59a-3761-b1de-b6af1e342eca | -3.2352 | -46.78131 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 958772b8-e207-38a5-8e3e-5338b2fac331 | -3.23166 | -46.78075 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| da7640e1-912b-361d-8738-90e5187bbeec | -2.69318 | -48.20356 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fe1f8c7-a461-35b7-bb4b-ccf9068b1977 | -4.42767 | -47.75182 | 2025-08-22 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96f5bc6f-29a4-3be3-85f7-ada467f11c84 | -5.38266 | -42.34636 | 2025-08-22 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9789fd5c-f793-3525-91c3-2edda63aa31a | -5.24234 | -37.69598 | 2025-08-22 04:17:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84d4dbd2-508e-3af4-adb6-85a90780cf12 | -2.90627 | -48.25247 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4912f511-d05e-3377-9734-f46f70fec9c1 | -3.73878 | -53.98352 | 2025-08-22 04:17:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c2d8875-5d71-3a98-aa52-d3f53e37d640 | -4.72316 | -38.39631 | 2025-08-22 04:17:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 47376d56-16b3-394b-9e70-b5b7cbbcb491 | -4.29467 | -48.05806 | 2025-08-22 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e06820e2-e500-37f0-ba5e-141f287f49a2 | -3.47154 | -47.69346 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 560fa569-83e3-3578-8860-51b47ca2c1ca | -2.30391 | -48.14697 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8470c841-46cd-331d-939f-c04dc933910b | -3.38618 | -47.61257 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 392382e1-6c58-3b1f-92d8-66dc3aa44675 | -5.14208 | -45.17781 | 2025-08-22 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bcfc8591-94ec-3082-89d1-40fb0a4f8f1c | -3.81628 | -41.55338 | 2025-08-22 04:17:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d0a2152-8dd3-36eb-b04d-2b2459ef07f7 | -3.81799 | -41.56572 | 2025-08-22 04:17:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8a43f6cb-d631-3a5e-ae43-5ca8df2aa98d | -4.82209 | -44.90249 | 2025-08-22 04:17:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9508bb0d-819c-3a21-a0dc-57ff6a9ad896 | -4.11221 | -44.45127 | 2025-08-22 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0202cc0a-3d67-3707-8439-919b6f2b813d | -4.13988 | -46.45014 | 2025-08-22 04:17:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a136a855-1459-3b35-8b89-54ca92aca024 | -3.62967 | -43.54553 | 2025-08-22 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 24b4612a-9fe2-3a44-8114-89e52bcd5919 | -2.47081 | -47.77465 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 749e1a9f-2751-3816-abd7-68aec20e97f2 | -4.6561 | -41.40982 | 2025-08-22 04:17:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f1bda28-94ea-385b-a375-e0f89477b432 | -3.36249 | -43.36477 | 2025-08-22 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2df9af7e-f07b-3c22-a627-fa3160ccc961 | -2.87371 | -40.09355 | 2025-08-22 04:17:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f7f05982-4dc2-348e-a214-abd3887586ee | -0.48706 | -50.35923 | 2025-08-22 04:17:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a2ec024-e5dc-3d83-8a4b-946a49edb70f | -3.26405 | -46.9157 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 964ceb38-d0f0-3d7a-80a5-1bf016240b70 | -3.26388 | -46.92125 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d116f82f-00b3-3700-b92d-ae341dc77ec8 | -3.43774 | -47.55029 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README24.md)
