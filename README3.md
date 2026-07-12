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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd44f089-2a2a-3a4c-a145-53cc90a2d645 | -3.13359 | -48.97992 | 2026-07-12 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1730b068-2bd8-357d-ac87-7d0e77d07ebb | -4.02517 | -44.1309 | 2026-07-12 04:49:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f974144f-93e0-3078-bbe3-64f9345182c5 | -2.8056 | -48.59255 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a256866b-92fa-3f51-a1bd-16be8ee9982a | 0.0823 | -51.09053 | 2026-07-12 04:49:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1231d8f-6966-3ca0-bf84-1c1e0b726dd2 | -3.30912 | -49.4634 | 2026-07-12 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50cd2047-ac0c-35b0-9bcc-0d5d57106337 | -4.02582 | -44.12645 | 2026-07-12 04:49:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1fa39bc2-9816-3269-ae9b-c701f5f40f1a | -0.99523 | -48.08541 | 2026-07-12 04:49:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8a7ff5b-31e6-376d-9be8-1d04c3527d05 | -2.96126 | -48.98966 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f4563163-8bca-3788-a491-d3700cf31ed4 | -3.73272 | -45.46915 | 2026-07-12 04:49:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1dcbc1ac-939d-3c81-af53-f9c9144da2ce | -2.96071 | -48.99323 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f6fe0d7c-80b4-3636-bca1-5d7189115e04 | -4.02962 | -44.13155 | 2026-07-12 04:49:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 29bd169d-b08c-3a40-a6f5-15e7c7c6479e | -2.96407 | -48.99376 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e28012ef-b26a-3903-95b4-5edeea9aba33 | -3.49158 | -48.03548 | 2026-07-12 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9f31ef1f-98c5-3372-8f4d-ee4d6bd1a9cf | -3.12188 | -40.10429 | 2026-07-12 04:49:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 587e14ab-3749-3030-a983-792e57269725 | -2.96462 | -48.99019 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e05552ac-bd7b-3292-ae98-f1489e99c45e | -3.13303 | -48.98351 | 2026-07-12 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbac8fe5-459e-3ede-819a-c0a28776077d | -3.27296 | -48.82809 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a5bd791-5815-30b4-83b1-174d6c5f7f0f | -3.12112 | -40.10447 | 2026-07-12 04:49:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f4d437b-b74c-3d1d-bbcc-e6f4c5a50bce | -2.95944 | -48.9896 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad4a32ad-dd7d-3efc-8849-45e2e75ba7fe | -3.49507 | -48.03606 | 2026-07-12 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1fbb60f0-d474-37a1-95d9-467a28ca356e | -4.03027 | -44.12713 | 2026-07-12 04:49:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 966d0154-5528-3ade-baf8-51b520fa40f4 | -3.49099 | -48.03931 | 2026-07-12 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 410b3ee9-c4f9-3f4f-9437-29a71a5a0aed | -2.43149 | -47.03027 | 2026-07-12 04:49:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4efea86-67d6-334d-afe9-672b416a123d | -0.16569 | -50.40727 | 2026-07-12 04:49:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9eec76c-7f53-32ea-a462-39805ff311d2 | -4.02661 | -44.1291 | 2026-07-12 04:49:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 5093a8a6-0d61-31b8-b042-33a6a88009ab | -3.1213 | -40.10829 | 2026-07-12 04:49:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 990dfb9a-9d8d-3849-995e-466a9040323a | -2.96799 | -48.99071 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 616dfe6f-0a3b-3746-a255-41fb9a548c1d | -3.49447 | -48.0399 | 2026-07-12 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a0d5a32-3ce3-3468-b571-5904acdd34de | -2.61973 | -49.1119 | 2026-07-12 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 967b4bf1-332d-337f-838e-0bb9b991cf67 | -2.8048 | -48.59337 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 601d3e43-05c3-331a-a225-98a713a7ffcf | -2.81013 | -48.71981 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1050bb35-33f8-323f-9057-b634b9805b32 | -2.96743 | -48.99428 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2cda26a-e47b-3cbe-9c30-0e5ea87ad81a | -2.95888 | -48.99317 | 2026-07-12 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6097d877-7b9f-3062-a6b1-abf7cbd45930 | -3.12051 | -40.10847 | 2026-07-12 04:49:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c95c7685-d39c-381a-88ea-930552368251 | -5.12261 | -43.23869 | 2026-07-12 04:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4cf4d369-33c6-3870-8796-f7edefaf13de | -10.47769 | -42.42424 | 2026-07-12 04:51:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f289ee46-bac3-3667-afe2-0694be41ea9b | -5.12715 | -43.2358 | 2026-07-12 04:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67f8ba04-ef88-3859-893b-75bc26de0586 | -10.12786 | -50.15067 | 2026-07-12 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46361e00-1a42-3f0f-9d84-787af9a0c4af | -10.12274 | -50.16132 | 2026-07-12 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e0d3e40-64d6-3397-8e64-a695905144eb | -4.34618 | -47.77173 | 2026-07-12 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6085d105-c665-38c9-83dd-64743896d107 | -8.25968 | -48.21478 | 2026-07-12 04:51:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 616125b9-5c01-3f2f-9bcb-b8de9184ad02 | -8.05428 | -46.93464 | 2026-07-12 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e4b78b1-b835-3c76-bc85-a9155a85e048 | -7.64285 | -50.02401 | 2026-07-12 04:51:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5bf2db1-c2d1-3b4e-869c-15144e0f2192 | -7.03696 | -55.49768 | 2026-07-12 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f91ccfa-21a0-307d-a2ab-da4928585acd | -10.84922 | -45.04 | 2026-07-12 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f12e8ec3-622a-3efd-83d9-b8be67597d3c | -4.2059 | -50.26184 | 2026-07-12 04:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9e759b4-3528-3067-aedb-8f19f11b81e3 | -4.34035 | -47.76746 | 2026-07-12 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d38064b7-4c7d-3f5c-be6d-afda1d521319 | -4.61607 | -49.05092 | 2026-07-12 04:51:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a9774c0-1229-3d42-8acd-98cf83b37ee4 | -10.8446 | -45.03926 | 2026-07-12 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a52fcac6-7464-33ae-a22b-39885bfe86b3 | -5.1216 | -43.2402 | 2026-07-12 04:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 508b9db3-7887-3b93-b106-374c5e72ba6f | -4.34262 | -47.77117 | 2026-07-12 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 409ce851-fae3-318a-95d7-bafbce4481f0 | -4.80641 | -45.76937 | 2026-07-12 04:51:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f7dabc8-fe91-3be7-a2c0-0e2fbf9cada8 | -8.10271 | -47.09357 | 2026-07-12 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2db5c7d9-6fa9-3c15-b71e-413e219c2fa7 | -4.61268 | -49.05041 | 2026-07-12 04:51:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 42929434-4665-3f94-aa0a-704d69588519 | -10.13127 | -50.1512 | 2026-07-12 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 615320be-dd2d-3048-a228-de227203b8dd | -4.34328 | -47.77207 | 2026-07-12 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4f06e40c-5745-3a82-8940-64742c32fd16 | -4.60928 | -49.0499 | 2026-07-12 04:51:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e29a4d2-79fc-3cca-9429-817e7c0a999f | -4.66488 | -43.22362 | 2026-07-12 04:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2294f3cc-d142-39f7-b418-64a0cdba9dc0 | -8.7288 | -47.82339 | 2026-07-12 04:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 010e53a7-237f-3483-be35-39a20b3fe9f8 | -7.90948 | -48.25709 | 2026-07-12 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a6d5e25-61b7-33b3-a020-c8b9373e9790 | -4.61664 | -49.04727 | 2026-07-12 04:51:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6e5377c-cea9-30d8-9d69-40313bfd14f0 | -6.49631 | -42.22075 | 2026-07-12 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 46be8491-8ad5-3437-a6f8-e6955da7c781 | -8.10734 | -47.08916 | 2026-07-12 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92fe95dc-8acb-3ba2-aa58-a2ca3f750b12 | -8.09884 | -47.09294 | 2026-07-12 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 837d7cfb-b6a4-3c21-b726-ed676ab9797a | -8.05455 | -46.93275 | 2026-07-12 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6f42898-80f9-34e1-9c7e-34ae0fa01366 | -6.94434 | -43.71978 | 2026-07-12 04:51:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdb6b8c6-4071-3dbb-b7d6-f05dbb24ad3d | -8.25604 | -48.21419 | 2026-07-12 04:51:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 284a1253-ece6-3033-a39e-fb2c178bc122 | -8.72438 | -47.82737 | 2026-07-12 04:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9a8b310-b898-3261-8e9f-8f3557c993b3 | -4.34323 | -47.76711 | 2026-07-12 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a8ab8613-e683-3c45-b0ac-8e941df5f55f | -9.00367 | -45.71303 | 2026-07-12 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8f0de54-aa0b-3c7c-890a-8fbde8811689 | -7.91074 | -48.24869 | 2026-07-12 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d0dd930-09a7-3064-a1c2-915e527aa567 | -7.75574 | -44.82221 | 2026-07-12 04:51:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 444ef783-b7c9-3edc-be5c-48d3c80ae0ef | -4.61211 | -49.05407 | 2026-07-12 04:51:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 082ebef9-63f6-341e-88c4-36f3b2650ab8 | -4.66967 | -43.22431 | 2026-07-12 04:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fce6d4c8-23fc-3aa9-b0cc-5a5209feb150 | -6.99783 | -42.90952 | 2026-07-12 04:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 78e2ee14-5aff-34d6-8ae8-be05f219249f | -8.50928 | -49.49454 | 2026-07-12 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68c02e38-5906-31e4-962d-8c039ba16267 | -5.12641 | -43.24096 | 2026-07-12 04:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6a04003e-6313-38d5-adcb-8ece50246399 | -8.13958 | -47.17577 | 2026-07-12 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d130ed0-6f1b-3613-9ba7-39313eb49a25 | -10.13013 | -50.15865 | 2026-07-12 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dae2a85d-2bc5-3d20-aad7-0df7a578fd87 | -10.1307 | -50.15493 | 2026-07-12 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6302fc48-1ca3-3478-84c1-bf4ed46f3ab3 | -7.91373 | -48.25346 | 2026-07-12 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffe8a5c7-3274-3500-ba45-8683e3fe73df | -8.72678 | -47.83702 | 2026-07-12 04:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ee5d95f-81be-3241-8f89-2c7ca5607952 | -8.25904 | -48.21904 | 2026-07-12 04:51:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 937cc635-caaa-35cf-ba10-4749e8d11cca | -10.28703 | -44.94559 | 2026-07-12 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a833ac7-eb26-3830-8486-3a38ee798898 | -4.34099 | -47.76342 | 2026-07-12 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b130a5c4-2236-3a40-abba-f40022388036 | -5.97673 | -43.61693 | 2026-07-12 04:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c42b49b-ad02-32be-9106-ba369cbfbff6 | -8.02597 | -46.88267 | 2026-07-12 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0c6b4c5-25fe-3cfc-b31b-55d56a56a0ee | -8.09812 | -47.09782 | 2026-07-12 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c53183d8-c402-3ab6-806e-40a1f036421a | -7.91011 | -48.2529 | 2026-07-12 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7ada52bf-3111-324e-8376-afa96b0559c2 | -5.67831 | -49.81664 | 2026-07-12 04:51:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fbebc76-694b-3578-952e-075ba47e485e | -8.72371 | -47.83191 | 2026-07-12 04:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d273d9f-9af7-3338-9ea8-47e9ca2c30c1 | -4.34391 | -47.76801 | 2026-07-12 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3da7be09-7bea-388d-b61f-dc0dc2eb7c33 | -10.05575 | -48.21218 | 2026-07-12 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f435092-17b4-36c8-b64d-d56164a61776 | -7.26964 | -49.51563 | 2026-07-12 04:51:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ba3135c-c76e-3d3e-92a0-3fdad34a4b12 | -4.66411 | -43.22881 | 2026-07-12 04:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 653edacb-d337-37a3-a9a5-699dfc5ecd33 | -8.10659 | -47.09417 | 2026-07-12 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e75c9607-9b03-3032-87f4-1e143ec8cd9a | -7.63948 | -50.02349 | 2026-07-12 04:51:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4d4a30a6-e623-3b86-97c0-e9253376c886 | -5.12234 | -43.23501 | 2026-07-12 04:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c6d30fa0-756d-3b97-b4e4-defa719e26f4 | -8.72812 | -47.82795 | 2026-07-12 04:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 787c3311-c7c8-3578-b9ac-2030cc452eb8 | -5.64638 | -49.04813 | 2026-07-12 04:51:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README4.md)
