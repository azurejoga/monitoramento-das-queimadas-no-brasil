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
| 499ebaed-0065-3598-afa6-cdd686ca81a8 | -2.7605 | -49.305302 | 2024-10-20 01:00:17 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c99382da-11be-38d2-92f8-3c67609d1b3a | -2.7634 | -49.3176 | 2024-10-20 01:00:17 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80e97178-9177-3753-9eec-9671a09c3fc4 | -2.7479 | -49.2952 | 2024-10-20 01:00:18 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31d43f76-6014-3fad-b614-d43abf58aebe | -2.7507 | -49.307499 | 2024-10-20 01:00:18 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa216c5e-cd09-36f8-924c-db3486c68589 | -2.7536 | -49.319801 | 2024-10-20 01:00:18 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6bd4e70-35da-318e-9b78-08a0139b0e0a | -3.8158 | -53.9884 | 2024-10-20 01:00:18 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f87ba9a7-c278-3a65-9be7-47b86c94c2b9 | -3.8173 | -53.995399 | 2024-10-20 01:00:18 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea58625c-4d1f-3c83-a496-c291c713388b | -2.7442 | -49.411999 | 2024-10-20 01:00:18 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dde1400-e961-3e4e-b073-ea605417c2cc | -2.7344 | -49.4142 | 2024-10-20 01:00:18 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cd5cbe6-fe73-3dcc-a7a4-ac67c8155831 | -2.7373 | -49.4263 | 2024-10-20 01:00:18 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5f73618-c9bd-3291-9630-7babccecd1f0 | -3.2432 | -51.616699 | 2024-10-20 01:00:18 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6afe2303-2966-38bf-a46b-6484854d7d50 | -3.2452 | -51.625401 | 2024-10-20 01:00:18 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e47cd5d8-21bb-3bb2-93fa-c5bc1beb3044 | -2.7717 | -49.619202 | 2024-10-20 01:00:18 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc8249a-211a-3aea-996e-107f3ac788c9 | -3.1489 | -51.251301 | 2024-10-20 01:00:18 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af019465-1e83-3434-97f1-b72af058756a | -3.151 | -51.260502 | 2024-10-20 01:00:18 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae8de87f-9408-3a9b-9457-db8d416bec83 | -3.0993 | -51.348999 | 2024-10-20 01:00:20 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc440858-0923-37d7-ad32-1441e915b398 | -3.0124 | -51.016499 | 2024-10-20 01:00:20 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7c8f258-186c-3399-95b8-b9e84a1ebb13 | -3.0146 | -51.026001 | 2024-10-20 01:00:20 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99d50f3b-a522-3b5c-8cb8-c4d32d5c8e27 | -3.0168 | -51.0355 | 2024-10-20 01:00:20 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65312241-4b07-301a-b0bc-be41369ab624 | -3.0599 | -51.2229 | 2024-10-20 01:00:20 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 961f7c66-2128-38fa-9680-84e015c64ba1 | -3.5457 | -53.5257 | 2024-10-20 01:00:20 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a17809a-9572-3a42-a567-82f1239680eb | -3.5474 | -53.532902 | 2024-10-20 01:00:20 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5df9e4c2-4842-3e57-a81b-03fb5192888b | -3.549 | -53.5401 | 2024-10-20 01:00:20 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8fa5b46-f54f-3dda-a879-99b5f2fde370 | -3.544 | -53.744701 | 2024-10-20 01:00:21 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0455c694-fba0-3fee-9fba-775b48f2162e | -3.5457 | -53.7519 | 2024-10-20 01:00:21 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f281bdb7-ac6a-3356-9418-a6731ff2ab9f | -3.5473 | -53.758999 | 2024-10-20 01:00:21 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b724729b-eaa1-373c-8088-8946f118fa54 | -2.4457 | -49.0993 | 2024-10-20 01:00:22 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bdaa78b-793a-39fa-9ea2-c00a0c638a21 | -2.2722 | -48.5732 | 2024-10-20 01:00:23 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 669a39f3-1a80-3402-9782-d42352a1304b | -2.2754 | -48.5872 | 2024-10-20 01:00:23 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e770d0ea-e01f-36c6-83a9-87d6fa4039aa | -2.2787 | -48.6012 | 2024-10-20 01:00:23 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e841211-0563-3028-9c07-c9884ba047b7 | -2.2624 | -48.5755 | 2024-10-20 01:00:23 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ca8a64b-c3ab-3f44-8059-f81e12949c58 | -2.2656 | -48.5895 | 2024-10-20 01:00:23 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e88e22d-a11b-3b93-abf4-853f2abb8143 | -2.2689 | -48.6035 | 2024-10-20 01:00:23 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7cfb9a6-a985-3e67-a983-bc51042fb3b3 | -2.2559 | -48.591702 | 2024-10-20 01:00:23 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48865f23-103d-33a9-9f52-e3f208c4f531 | -2.2592 | -48.605701 | 2024-10-20 01:00:23 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 755d2c1c-81af-3415-848b-a8be89ec71bc | -3.2599 | -53.039902 | 2024-10-20 01:00:23 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b2eb806-909d-3ce1-b337-3ccb0b4c19e5 | -3.2616 | -53.047501 | 2024-10-20 01:00:23 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9d65c7-7c2a-36eb-a30b-c52e052e4159 | -4.7823 | -59.895802 | 2024-10-20 01:00:23 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9fde576-d1ed-385c-a642-f146d538b15d | -2.8056 | -51.280701 | 2024-10-20 01:00:24 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 531b7927-4f18-38de-a2fd-f05bfcd2a834 | -2.812 | -51.308399 | 2024-10-20 01:00:24 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27c0e906-bbe2-371a-af38-5f1472eeb63d | -2.7889 | -51.342602 | 2024-10-20 01:00:25 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f06ed6f7-2ce6-3823-824a-ebe01e5de764 | -2.791 | -51.351799 | 2024-10-20 01:00:25 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afb9681e-3f88-3e48-9dfd-8286062a9f6c | -2.7714 | -51.3563 | 2024-10-20 01:00:25 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95ab9ba8-d507-3e28-abb7-4fd66a0b3358 | -2.7736 | -51.365398 | 2024-10-20 01:00:25 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 126635e9-252e-3900-9f51-415c28e35ca2 | -2.7617 | -51.358501 | 2024-10-20 01:00:25 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4893005-3e1a-3550-8e4c-10a85946fbb9 | -2.7638 | -51.367699 | 2024-10-20 01:00:25 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f161bf7-42e0-3b37-8b7c-9e6f41f8c2e9 | -3.4677 | -54.4534 | 2024-10-20 01:00:25 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7551f3f3-f052-30a9-8579-5d18b3d25577 | -3.4782 | -54.682301 | 2024-10-20 01:00:26 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2e94cb4-dd3b-32af-b6ad-f4eaf8c2e001 | -3.4798 | -54.689098 | 2024-10-20 01:00:26 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdbdb978-b771-3908-b9be-257488973f05 | -3.2467 | -53.7062 | 2024-10-20 01:00:26 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bee15d9a-9ac4-36ab-9f61-5849ed38a7a8 | -3.2483 | -53.713402 | 2024-10-20 01:00:26 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7fdeb38-65c0-3f37-bf93-ab225b745a17 | -2.9575 | -52.8437 | 2024-10-20 01:00:27 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ea49e71-f4f2-342d-8999-7075eef2e506 | -2.9593 | -52.851398 | 2024-10-20 01:00:27 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 118c04bf-e061-3c78-83fe-f99cc2f396dc | -3.2548 | -54.1506 | 2024-10-20 01:00:27 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e6b7067-f731-382b-bb1a-336bf97d5dc0 | -3.2564 | -54.1576 | 2024-10-20 01:00:27 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63e000ca-f03c-35db-81e2-2fc37fb6fa47 | -2.7484 | -51.973701 | 2024-10-20 01:00:28 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eafbc3e9-9791-32e5-92a6-bdbb1c577b22 | -2.9495 | -52.8536 | 2024-10-20 01:00:28 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33431c31-ebe0-315e-a85e-8d56817c1b96 | -3.0375 | -53.239399 | 2024-10-20 01:00:28 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85c24eb1-1e81-3db2-b8b9-41f75a7a8ad7 | -3.0392 | -53.246799 | 2024-10-20 01:00:28 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec0d1a9e-1287-3fa5-8bdb-fea0eae300ba | -3.2434 | -54.145802 | 2024-10-20 01:00:28 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f94e2c59-4e12-3f1e-97fe-39e77813a382 | -3.245 | -54.152802 | 2024-10-20 01:00:28 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| def913e2-2eb4-31b9-93e7-35ae20eb87fc | -3.0277 | -53.2416 | 2024-10-20 01:00:28 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da54ebc7-ff2c-3dcd-b3a0-1e908758c267 | -3.2301 | -54.178101 | 2024-10-20 01:00:28 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7415f445-6eff-3f37-ba71-1ea6a35c47e0 | -2.9289 | -52.898602 | 2024-10-20 01:00:28 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d4dd75d-3a46-3f7d-85b8-76d57bdd41c2 | -2.9306 | -52.9063 | 2024-10-20 01:00:28 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f79d16f9-8649-3018-b5d1-0683278956ac | -2.9324 | -52.914001 | 2024-10-20 01:00:28 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff4e65fc-8ac1-3c93-9fe1-71bc16abe947 | -3.3275 | -54.744701 | 2024-10-20 01:00:28 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97a8b979-dc42-364b-9771-6c05bb44e95b | -3.4619 | -55.431599 | 2024-10-20 01:00:29 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c33ecf8-2a97-3328-ad7f-13d3fba8bdb6 | -2.666 | -52.063499 | 2024-10-20 01:00:29 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df208cba-1f6b-342c-8604-bef2c10af78f | -2.6679 | -52.071899 | 2024-10-20 01:00:29 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ba05a3f-032f-31f6-a365-bde95c5ac60b | -3.1244 | -54.348099 | 2024-10-20 01:00:30 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8526de70-5224-35c0-8660-4e0b0487edce | -3.126 | -54.355099 | 2024-10-20 01:00:30 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d055d43-6b02-30a1-9594-dc42dce78bec | -3.1276 | -54.362 | 2024-10-20 01:00:30 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96736e44-89bd-3f34-92c9-8ee750072dbb | -3.1291 | -54.368999 | 2024-10-20 01:00:30 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9732500-7c03-3bc1-9f7f-4d329023257a | -3.1146 | -54.3503 | 2024-10-20 01:00:30 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac86ef9b-499a-3f53-a900-807a4bdb12cd | -3.1162 | -54.3573 | 2024-10-20 01:00:30 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f73e24e4-bd75-3d5a-be25-f929255664d9 | -3.1177 | -54.364201 | 2024-10-20 01:00:30 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 439f5233-bc85-35d9-977f-d0e69a2f7ba6 | -3.1047 | -54.352501 | 2024-10-20 01:00:31 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02499358-21ed-34c1-b9e8-d86a04a38951 | -3.1063 | -54.359501 | 2024-10-20 01:00:31 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0c0eeab-dfcd-3d93-bf71-9670ee0a1d33 | -2.2033 | -50.451698 | 2024-10-20 01:00:31 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d327052-a300-37e2-8180-d82cdaf71d03 | -2.1959 | -50.4645 | 2024-10-20 01:00:31 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ceea526-3347-39f6-bf4c-dd614ec2aeb3 | -2.1838 | -50.4561 | 2024-10-20 01:00:31 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dab8bbe-1f2d-354f-87b7-ea869b33a118 | -2.1862 | -50.466702 | 2024-10-20 01:00:31 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b902a3e-60bb-3466-a032-d124deb3a165 | -2.9263 | -53.7024 | 2024-10-20 01:00:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7849fbdb-cc79-3453-b1e4-385fb17c88be | -2.174 | -50.458401 | 2024-10-20 01:00:31 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba12dac7-c593-31a4-8a82-bfbba706c566 | -2.1764 | -50.469002 | 2024-10-20 01:00:31 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e5d6605-c875-3110-bb86-c8c5de8b572c | -2.8285 | -53.317501 | 2024-10-20 01:00:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40b6446a-f669-3e8b-ab80-4bd633ba7249 | -2.8302 | -53.324902 | 2024-10-20 01:00:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83413ada-5d9e-31fb-9d0d-103cff8760f5 | -2.8319 | -53.332298 | 2024-10-20 01:00:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f129fda-a174-3f96-baef-a84d464714f7 | -2.8336 | -53.339699 | 2024-10-20 01:00:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c7e3265-4d84-34c3-9b2c-eecee4668ce3 | -2.9925 | -54.039398 | 2024-10-20 01:00:31 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d29fe33a-f625-39ed-b8a7-002c0ee40b37 | -2.9941 | -54.046501 | 2024-10-20 01:00:31 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0593a5e-7b97-3f91-9185-206d3c05652c | -2.8221 | -53.334499 | 2024-10-20 01:00:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed2de040-2f36-3f29-9414-c81464723830 | -2.8238 | -53.3419 | 2024-10-20 01:00:31 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59db9f2d-bb51-3977-9d25-bc807b444673 | -3.06 | -54.428101 | 2024-10-20 01:00:32 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4123f1b0-3cdd-32a7-86c7-5e13a3120702 | -3.0616 | -54.435001 | 2024-10-20 01:00:32 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58fab440-b9f4-3603-b927-6fa99e00404c | -3.0632 | -54.441898 | 2024-10-20 01:00:32 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd5356e-a2c7-3838-8419-d3f3b09ba24e | -2.9266 | -54.1576 | 2024-10-20 01:00:33 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c8ffb66-e3c5-3779-934e-23123aa0e080 | -2.7345 | -54.037701 | 2024-10-20 01:00:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa1847eb-88e0-30cb-92f6-2d7805de8823 | -2.6922 | -53.987598 | 2024-10-20 01:00:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
