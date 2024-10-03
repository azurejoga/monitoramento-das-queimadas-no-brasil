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

## Dados Diários - Página 191

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33d93b24-1eb5-3c27-8580-5bd23afde223 | -7.43776 | -72.78114 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6844aea6-927c-3aaf-9b84-3ad8a3837e70 | -7.43837 | -72.58387 | 2024-10-03 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b36d844-12a0-3147-9e88-63b669442d24 | -7.66446 | -72.31746 | 2024-10-03 06:08:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d28a045b-c992-329a-a00c-48431d852cdf | -7.67577 | -72.9966 | 2024-10-03 06:08:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08402f2f-e4fa-3c44-ae66-18e3b8af2b3a | -7.77976 | -72.98416 | 2024-10-03 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db8fb6bf-3ea4-374e-b12a-84b92df5f021 | -7.78033 | -72.98063 | 2024-10-03 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dadc30e8-d8fc-3d34-838b-51dc63b0c6ef | -7.78366 | -72.98116 | 2024-10-03 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3004bb49-022a-3a67-a846-60d598c53ee8 | -7.79083 | -73.00042 | 2024-10-03 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 140c0b72-5549-37d0-b20d-2b43f2abbfc3 | -7.80468 | -73.02077 | 2024-10-03 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69e5d66e-c61a-35bd-83d0-312cf2a1c1f5 | -7.82907 | -73.06096 | 2024-10-03 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1135a64f-3d3e-3c55-86f1-045a502e8291 | -7.87425 | -72.79722 | 2024-10-03 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0c4e407-fcba-3555-b6c7-af1800372dbc | -7.88364 | -72.80284 | 2024-10-03 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cf131a0-1c6b-3716-b4e6-7be64dcd3e28 | -7.88476 | -72.79584 | 2024-10-03 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 244d5c67-553c-36d8-8568-04d1aed8a591 | -8.10687 | -70.2092 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6410a08e-f269-3271-8084-7260441c20a5 | -8.12523 | -70.49642 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8d68d33-78b3-31a6-b4f5-75981745b3c5 | -8.16806 | -70.24128 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a828c7b3-f00e-3be0-b16a-f187ba02c75a | -8.16893 | -70.24089 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dc4c61f-df66-3a70-8f2f-461d10c84976 | -8.34556 | -70.38851 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84ce4af6-c323-3fde-84e2-325664a3881c | -8.47158 | -70.36623 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4580208-f618-3cf8-89d1-a5bf2ca952fc | -8.49018 | -70.52567 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68575593-681b-3fbd-aa53-8b186838a7de | -8.52761 | -70.34793 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8577bed-c5c3-3882-a953-cc86ebe991a8 | -8.61599 | -70.52675 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 148d0c27-bf52-382e-9d06-6cc2cfb08d46 | -8.45462 | -70.87057 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2463fc8-044a-3087-8173-53975738058e | -8.46309 | -70.33101 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34328451-1858-31e2-9a17-4392006574c3 | -8.46536 | -70.3615 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3786bfb9-9d45-30c7-8f5d-2561f124b1f0 | -8.46691 | -70.87979 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15ca5a9c-a673-313d-8ef1-ce053f2650a9 | -8.46819 | -70.36569 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff9e1267-84fe-38ae-92d3-e827da03bf66 | -8.5344 | -70.34898 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b022740a-f9f4-33dc-bbf7-69654a364570 | -8.5467 | -70.84503 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b48960a-ac33-33de-b3d1-382058b8b112 | -8.54677 | -71.44167 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58969413-e9ca-3b39-83ac-cfa0922989c5 | -8.59923 | -71.45348 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a883a84-442d-39eb-b1d6-ee531af45496 | -8.61543 | -70.53039 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 009ad8b2-2503-3663-b72d-f1005366c8f7 | -8.64176 | -71.57448 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2efda24a-99e4-3dc3-aae6-cf8223e70f3c | -8.73202 | -70.59266 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f207d0b8-2aa2-336b-9b37-bf6ac7b0a819 | -8.74242 | -71.01002 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f00b7596-8ff5-3dc9-9bca-2b8a1ebf8ff2 | -8.74576 | -71.01054 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05cf2ab6-1532-3be0-98f7-1546c1ca17ae | -8.76466 | -70.79727 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3d6337d-b757-3189-8639-bbc65e685fa1 | -8.79618 | -71.27979 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf504ee8-f6b1-3a59-8fa4-6900b30f2b8f | -8.83329 | -71.28196 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a88d856a-65df-39fc-9414-85c8373c7a88 | -8.84781 | -70.56902 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59e5b60f-8f0b-3721-a95e-84fb4387f7b9 | -8.85118 | -70.56954 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d138162-e62c-337d-9e11-5ab15d1deb0f | -8.86912 | -71.44588 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d85fe9a-6a2a-3f99-b789-1879a5d891dd | -8.87217 | -70.85099 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 113732dd-b92d-3192-9e0f-09daac793138 | -8.87271 | -70.8474 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2853a3ea-878f-335c-a5d1-7645ba57e0ca | -8.87311 | -70.61784 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f06f9142-392e-3e4d-b1b9-790c025727d6 | -8.87552 | -70.85151 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8762170-c23b-370e-bfc7-609d9794846f | -8.87607 | -70.84793 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fce8d7aa-1ac5-3dcd-b570-8e85c1247e99 | -8.87662 | -70.84435 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc72cc83-8513-30a8-870a-947701fd12c3 | -8.88211 | -71.36162 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33a1fe59-6157-36ee-826d-839f7c79115f | -8.88713 | -71.37321 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1437a8b9-7bc7-3845-bb55-aaa9c433af00 | -8.88892 | -71.25083 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea872645-7d15-362b-80fd-398cd33b917e | -8.89225 | -71.25135 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53efae40-ff67-3661-9609-19eb7aed8281 | -8.94161 | -71.2627 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60e73010-91b6-3cbb-beb1-101495c4f860 | -8.94493 | -71.26322 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9907772-c002-3f3a-9186-69ab794952b2 | -9.19265 | -71.83693 | 2024-10-03 06:08:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b9fb26c-abea-31d1-ab60-0bf23c01d459 | -9.19862 | -71.79862 | 2024-10-03 06:08:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f140250d-af1c-3890-8aa9-bc8fe465b2c4 | -9.20138 | -71.80263 | 2024-10-03 06:08:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc8b3b18-10be-39b6-bfd1-07a600ea0dc9 | -9.20193 | -71.79915 | 2024-10-03 06:08:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0db7690d-f1bd-3487-9f89-77503df67765 | -9.24181 | -71.93741 | 2024-10-03 06:08:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a385d007-97a8-3757-96e1-0adc5b4ae09b | -9.24457 | -71.94142 | 2024-10-03 06:08:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66a0764b-45d0-3b84-8fdd-3f90ca93ea0e | -7.92627 | -71.47217 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d253569-e4c6-3298-9ffe-0521bf044e99 | -7.92958 | -71.47269 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cbbd9f9-1751-3ded-93ea-0781cabb1fe1 | -7.93012 | -71.46921 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee95d795-973e-3559-baa5-9c68e847b497 | -7.96427 | -71.46744 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5998a1ea-21d2-3c8c-a5fc-8a9a157cb662 | -7.96507 | -71.35351 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19c16fdf-d8a5-302f-b6c8-753c856ea396 | -7.96561 | -71.35003 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da5cbccc-2d1e-3e98-af25-66ea58f36f58 | -7.96892 | -71.35055 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a91f87b1-6ec8-3a37-b3ab-5b5ea9c8581a | -7.99963 | -71.39458 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9226b5c3-f8bb-3846-acd2-22e2d93c2de2 | -8.00703 | -71.30291 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d53f51fb-8028-3780-9f53-80c4e0d85c2d | -8.0163 | -71.06747 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d17c7df-a680-3eea-a992-786db3cb5314 | -8.04534 | -71.57979 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49bbd9fe-0535-3af7-ad67-acc8dd7ed431 | -8.04584 | -71.18352 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9127efc3-659f-3599-a008-628d1ee44504 | -8.04666 | -71.26613 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ad00b73-c507-3f10-90c1-951b1edaca37 | -8.04865 | -71.58031 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60dc3259-752d-333d-9986-be385f312eca | -8.04919 | -71.57684 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0380c8bf-4418-3c02-9ecc-5b0a90b229e2 | -8.06571 | -71.57942 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5b3bb09-1a79-3fd4-9531-8da591b595bc | -8.07264 | -71.27378 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9d4e9ec-d861-37b6-b6be-f5a034c1b699 | -8.07318 | -71.27028 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e819b0be-b6a5-3b02-a463-5260a5c9fe99 | -8.07801 | -71.21725 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9842c46b-218e-3dfa-bc38-3a895ac2e595 | -8.08876 | -70.9268 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b3075ed-0d83-3ab3-938a-405f4ec7a49a | -8.09155 | -70.93086 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d97552e0-f9d8-3fef-9fe7-537536be79ed | -8.10293 | -70.64068 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7473bd98-2925-38a5-9fbf-cccf0d971c52 | -8.12499 | -70.20446 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c73f05b-fee6-390b-a09f-80cd190d75ca | -8.16523 | -70.23705 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3fe13b8-c59b-3676-9545-0e023e6adc24 | -8.19469 | -71.01244 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dea9c53-d080-300f-9c89-fe754efc409d | -8.19796 | -70.99121 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22840a08-5ef1-3ce6-9c83-bdb410de9b24 | -8.22633 | -70.80643 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ee3525c-2d67-33d8-9cd9-f590b74b3d24 | -8.23706 | -71.68152 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2404103e-cf26-371f-8ab3-3d2bc5a025ca | -8.25531 | -71.14815 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02ef15e2-0d57-3492-a687-2ca573c96906 | -8.25585 | -71.14462 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a607ab4-48ef-3cb7-8c15-7ca1ee5eb354 | -8.2625 | -71.14566 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6fb0268-52ce-3e50-8ac3-b4971964b864 | -8.27117 | -70.9373 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3324c12a-5caa-36d4-a48a-5499b6bc2027 | -8.28052 | -70.56472 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7a75252-0e31-36b0-a0e4-7c32a3cfd371 | -8.28107 | -70.5611 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a64bd3b-1ec9-3851-bfbd-516939ba42e7 | -8.29451 | -70.9371 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef578b09-634b-377f-8da4-d3822ed50c7a | -8.30111 | -70.91629 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62ab2bcc-5b43-31c1-a851-0eef704feb9d | -8.30656 | -71.05865 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3997404-f088-3ece-bf3a-fdfa2703d8b5 | -8.33866 | -70.25198 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 018e4640-de5d-3803-b115-7e0b9036d954 | -8.37123 | -71.21286 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa3a2a0e-4bd1-3da9-a9d4-1b5120cdd5fb | -8.37177 | -71.20935 | 2024-10-03 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README192.md)
