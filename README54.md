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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7873310b-213c-3461-a164-ffc56fe16f57 | -2.88779 | -49.25571 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 93e9c0da-760c-35b6-96fe-36f4177d1434 | -2.88759 | -49.25854 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 8d37bf33-4ec9-3b3b-b2fc-374961f5bbc1 | -2.88524 | -49.24868 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb2efef6-fe71-32f8-8a42-9f634fcd347d | -2.88469 | -49.25048 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 21d06efb-9150-3066-9c7e-30ef81ea7842 | -2.88452 | -49.25332 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 280590fd-2746-3d4d-bda4-02e0efe30e56 | -2.88399 | -49.25512 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| fffa1785-34da-3f2a-bcfa-8f83dab50bfe | -2.88379 | -49.25795 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| edecb37b-3fec-3fb6-8277-982e2d495be9 | -2.8833 | -49.25977 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 628197aa-2c44-3a82-9f7a-87e903905ac7 | -2.88144 | -49.2481 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 959c8428-dcda-3504-9f73-260b6f8e254c | -2.88089 | -49.24989 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a673576e-1fde-3199-97ff-66b4c370752c | -2.88072 | -49.25274 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3b125335-923a-3341-806e-0c4f77cb16a0 | -2.88019 | -49.25453 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 7f681829-f0e0-3a9d-aabf-2d44b01d1049 | -2.87999 | -49.25737 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e3da9127-fca3-3961-84ee-a5273076a272 | -2.8795 | -49.25918 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d069574b-dcb8-3f32-bcfb-874508430214 | -2.87764 | -49.24752 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44856ec6-9acb-37cb-bada-925a57d79a9e | -2.87709 | -49.2493 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 0d3fc9e4-757f-3933-b30a-9fa1ea80c3af | -2.87692 | -49.25215 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e3e91d9b-108c-3ccf-8a61-0c5e31aba7ae | -2.87639 | -49.25394 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a8da4ce8-5e2d-32ed-a766-81fc271d686b | -2.8762 | -49.25678 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 667b43cf-16b2-3743-8861-88a898b5afe6 | -2.8757 | -49.25859 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b31a39de-28b7-34d5-9278-19fe51b99608 | -2.87312 | -49.25155 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4d631cd-dcc6-381a-b00f-936edca3fffc | -2.8724 | -49.25619 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 028832e1-87db-3cd3-932c-eeaf15cfb9d7 | -2.87168 | -49.26084 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd5682e0-1292-3130-8387-a45dea47132c | -2.86932 | -49.25096 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 629baec8-ad89-31ae-a3f7-38810acb95b3 | -2.8686 | -49.2556 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2689392d-a74d-390c-93c1-509507745fa0 | -2.86788 | -49.26026 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19173711-f274-33c4-bb3a-0b967162e5c5 | -2.86697 | -49.2411 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 897df8ba-a460-3a87-88c9-12fb83a31e0b | -2.86625 | -49.24573 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 97af16c8-00bb-318d-a48e-ef149850400c | -2.86553 | -49.25037 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1582cf3-a9e3-39df-980d-9ae703ef8cb3 | -2.86481 | -49.25502 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4c72e27-6378-3e3c-acb3-c56c34e447c6 | -2.86408 | -49.25968 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9aa6c76-a983-3c07-986d-c843de9101dd | -2.86317 | -49.24051 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83b6a9c3-4cc3-3ca9-8f6c-62c2db3afb98 | -2.86245 | -49.24514 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ac0e5d4b-492d-398f-a3cb-b1ba84ddc5f0 | -2.86173 | -49.24978 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8574a5bd-8650-3055-a0d9-b043df31a8cd | -2.86101 | -49.25442 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae5c7a4f-4ce7-3bdc-a2ac-ab120aa43d38 | -2.86029 | -49.25908 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f800198-1d78-32ff-81af-590cb343647e | -2.85865 | -49.24453 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0a1d89a-7968-37f2-ba17-5856e16adae2 | -2.85794 | -49.24916 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42197dfa-7f25-300e-ade8-15ae35d3d4cf | -2.85722 | -49.25381 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 958aafde-d665-3d90-9e2a-5fe774c8c09f | -2.85649 | -49.25849 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 547fbd4b-3f76-335c-82be-6496eefffb50 | -2.85486 | -49.24391 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca74e570-a62d-30b2-9353-7f19219a427a | -2.85414 | -49.24856 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a53de2d-ee52-3aa7-80a1-c06e64b86624 | -2.85342 | -49.25322 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6370707-b739-324e-ab3a-1b56f4367751 | -2.8527 | -49.2579 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 198b4874-a873-3c82-8332-5a8889197a99 | -2.85105 | -49.24335 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b22e15b7-c5e2-31fc-b5eb-57a9cf18940d | -2.85034 | -49.24798 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8aba6c13-967d-3d63-873e-6df5c0ef4487 | -2.84962 | -49.25266 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa92903e-2b5b-3034-820b-28e7d1de8d35 | -2.8489 | -49.25732 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be25b51d-bed0-3097-bfcd-2cd1668a8748 | -2.84725 | -49.24277 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1d7306c9-c1f5-31c9-a1df-78176b2343cd | -2.84654 | -49.24742 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7ff842b-6370-3f17-aafc-f74427986985 | -2.84582 | -49.25208 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 284c975b-4eda-320c-9026-0eaa9504f56e | -2.84345 | -49.2422 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 14fe7c04-147a-3c5a-9e3b-198bbd65e513 | -2.84274 | -49.24685 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c736bc6d-bab7-3c29-9591-8226f16942fe | -2.84202 | -49.2515 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abf694dc-0588-3f39-9f46-9d36a927948a | -2.8413 | -49.25616 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6e4d948-7232-3934-962d-f3cb5b120f57 | -2.83894 | -49.24627 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98cc5eec-8990-3d11-9cdd-7a7e9aeee8ff | -2.83822 | -49.25092 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f1e79f7-80ce-327a-82f1-db15ecd6a733 | -2.83751 | -49.25559 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e725c68-7965-3493-a835-85f1f11b4ccf | -2.83679 | -49.26024 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 372a9131-c95f-306b-91e8-d771e537f633 | -2.83514 | -49.24569 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c74f3dcc-7cc2-305c-9959-a6ae1573c957 | -2.83443 | -49.25034 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b98a843-d949-3963-b22a-45f5d83e6362 | -2.83371 | -49.25499 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 910edbf8-d3d7-35cd-ac5b-8ed86aab3f60 | -2.833 | -49.25964 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab4479d2-9d20-3023-b510-9d00a4d6d9e5 | -2.83205 | -49.24044 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 75522fb3-c6ac-3b83-a012-387d7d87e6fa | -2.83134 | -49.24511 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67c203bf-de31-3302-bff5-7193ac7b8cfc | -2.48384 | -49.23665 | 2024-10-28 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a119db6-2122-389a-9299-2656d34e3a4e | -2.47648 | -49.10932 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebae8b2a-cacf-32e1-b752-e2f856563c93 | -2.47552 | -49.11173 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62506e59-4d44-369c-8703-30bc9f9fc76f | -2.47445 | -49.78845 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58e02ae7-497b-3b65-96bf-cbe3dcc58124 | -2.4744 | -49.79039 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 726318ce-c4f9-3d6d-b36c-fd1c9183789f | -2.47341 | -49.10407 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6f0fc2b-d185-3ef1-974a-d4bff7538915 | -2.47267 | -49.10873 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfaaf40d-fe06-30af-beba-3deb4b284221 | -2.47241 | -49.10647 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44776018-ee6b-3c93-a1a9-e870830af88a | -2.4724 | -49.06062 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adbf760e-d503-3b0b-9750-c556c38a9cac | -2.47079 | -49.7879 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e022d11-af93-3621-8177-2da5ca0758e1 | -2.47073 | -49.78985 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b92c4d13-8869-3fe9-9bc0-fe1e99a28f99 | -2.47014 | -49.79216 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c539bfbe-768b-34cc-ab1e-2fa7d3304494 | -2.46858 | -49.06003 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ac3cf2f-631c-3ccb-a582-730beb9669b9 | -2.46707 | -49.78929 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a3a0139-51f3-3f83-9d99-1e82aadec0e2 | -2.4658 | -49.74938 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c6ba22c-9ef2-37d1-8568-98f839d6a000 | -2.4634 | -49.78873 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c503212c-fa55-31c1-9016-ed3edb986709 | -2.46273 | -49.793 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d3c0a13-c573-3b36-b2c3-0da94dd8cb74 | -2.45667 | -49.87948 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ef44817-fe43-3cc5-b2e4-3277481d7110 | -2.44112 | -49.16113 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22e7614b-de06-3796-b831-e3d5d01ff0d9 | -2.43731 | -49.16057 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8f26f15-8279-373a-8812-541356d87ff4 | -2.43071 | -49.65956 | 2024-10-28 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43373b7c-b9b4-3363-83d8-5da5ead7d7cd | -2.42728 | -49.22519 | 2024-10-28 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 194138c4-c8a0-3c07-ac82-c43bd40ad785 | -2.42571 | -48.95636 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 472a248a-8104-310c-9a0f-750374e2cffc | -2.42426 | -48.96588 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f9a2c2a-69b8-38a1-83a7-b5d7df0e42b9 | -2.42149 | -49.08644 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d21f5893-6c50-3356-8249-853d882981e3 | -2.40619 | -49.8194 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f753ad5a-abd4-3e7f-ac70-fa96af93c985 | -2.40319 | -49.81454 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f89f76f-ecfe-3c62-8131-fdffb2345dbb | -2.40026 | -49.02045 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dce63663-e448-32c9-b3cc-aba1543e7a9f | -2.37354 | -49.02388 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a8d35d2-043d-3698-88b6-5589bc4ed130 | -2.37205 | -49.02575 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd9e5978-b261-3603-a9d4-d9d21c6d17f7 | -2.35461 | -49.54607 | 2024-10-28 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 884a093f-917d-386d-8613-8c4efb4ad5d8 | -2.3509 | -49.54549 | 2024-10-28 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2641a67a-5a4d-3146-b5e8-7ef7ea464680 | -3.51945 | -49.23428 | 2024-10-28 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb41233b-6781-35c5-b908-092dee3548e6 | -3.50032 | -49.93942 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acbf5435-e98a-3f70-9fcd-cc11c1480284 | -3.49965 | -49.9438 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README55.md)
