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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa91f72e-bfac-39d9-be8a-63c6c7bde8de | -19.56785 | -56.68961 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 01a15667-6562-310f-900a-1e9c70819973 | -19.56782 | -56.64476 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| dcadefc8-ceed-3bed-8299-b469655b6ecc | -19.56771 | -56.55594 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 813ab94d-0258-33cb-82a0-57a6c46418ec | -19.56629 | -56.60798 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| da134e59-c32e-3c32-86d0-ee0592a807d5 | -19.56556 | -56.61187 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 161a6136-1f62-3c72-bec0-9363bc093cd2 | -19.56523 | -56.6809 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e617bf21-cc24-3434-882d-91eae21fc2f0 | -19.56516 | -56.5916 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e7cb714b-aaad-3bd1-8d4b-68ee97e938de | -19.56481 | -56.61576 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 070c729b-2808-311d-98d3-83227080198d | -19.56448 | -56.68481 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 00c0f831-6ce5-3f9b-bd59-a077fab36e9a | -19.56446 | -56.64001 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f729b1d4-e0b9-350f-95c4-6db4f38e6d17 | -19.56436 | -56.55122 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 284f8680-47cf-3f40-bc92-80cba72acf96 | -19.5641 | -56.66434 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7fed4a0e-7af9-30ac-b9b1-dece19014eda | -19.56407 | -56.61965 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0d69a8b0-1e52-377a-a2d2-e0672fff1212 | -19.56374 | -56.68874 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 747cd468-3fe6-3a60-a10a-96d7c432185b | -19.56372 | -56.64391 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 04d38dab-2f80-3f33-b329-6158b872fdf1 | -19.56363 | -56.55508 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0e5e8a4f-0b57-30c3-bfc8-cf1fc760dbdc | -19.56335 | -56.66827 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a95a35b3-3bfb-3ab9-bd2c-bf42c7c34748 | -19.56328 | -56.57913 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2ccacbe3-d0e5-3cb7-a5ec-fd66189ac476 | -19.56297 | -56.64782 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 12c16309-6073-3ea6-bc48-1055551e7522 | -19.56294 | -56.60324 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 2ef934e2-1fcd-31a7-8e8c-7e00acacedbb | -19.56261 | -56.67219 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| fa59e01f-2691-363e-8634-0d67d34da6bf | -19.56223 | -56.65174 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2b072e50-d974-3b43-8ba5-c909f8626882 | -19.5622 | -56.60713 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 8c70f9e1-2f9d-3952-a6b2-e17c2f9ae69f | -19.56186 | -56.67611 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| fc80db7a-6c31-35c3-bef5-c54fdc73d032 | -19.56148 | -56.65565 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 26356e93-37d7-3548-b8d8-c13d9a4632b0 | -19.56146 | -56.61102 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| b7fe605f-1f74-3fda-8a53-206288757d8a | -19.56141 | -56.56667 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d563c82a-1bf4-3ed9-923d-e7190bcc8b14 | -19.56111 | -56.68003 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c165e283-5f56-3790-90bd-1d83dfc4ac44 | -19.5611 | -56.63525 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7e0ceb52-b43f-3b14-a3a6-0088cda25ef2 | -19.56073 | -56.65957 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e75c018b-8c8c-35cd-81c2-e4228f8e79ba | -19.56072 | -56.6149 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 244bdeb1-968c-3fa7-81b4-c1adcd23c2bc | -19.56035 | -56.63916 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| adbf1cc7-b364-3a08-9c5a-2023e744069d | -19.55999 | -56.66349 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3c0aea6a-ef6b-3d68-8cc1-7ebc9583af77 | -19.55997 | -56.61879 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 647e28c6-ea45-3f61-bdf0-b133407002c7 | -19.55961 | -56.64306 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 47de4d2c-04f0-3812-bdbb-f6273782adb7 | -19.55954 | -56.55424 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ebe39253-cea9-3f86-885a-f0a993cba098 | -19.55924 | -56.6674 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c591bcfd-a444-3505-a9eb-58d4c7486fc9 | -19.55923 | -56.62269 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0c0fb10e-82bd-3d48-98df-f126aece4df4 | -19.55886 | -56.64697 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 876e3454-22b9-3b40-8642-c312487abeb5 | -19.55881 | -56.55809 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| bfd87f9a-51a3-3886-a3ac-272e565ed44c | -19.55849 | -56.67133 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 2d170bed-9794-3bcf-ab66-e0d9fb2035f4 | -19.55849 | -56.62659 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7209887b-6ec5-3fe6-80e7-3afdd0d739b7 | -19.55812 | -56.65089 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8ccfe004-f749-3f0a-bc3f-de817cc0348f | -19.5581 | -56.60627 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 626f2e72-3fde-3af6-ba18-1c4c27303d0d | -19.55807 | -56.56196 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b1b8babc-1ee5-3972-b1f4-adbb9d7afb7d | -19.55775 | -56.67525 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4e9a7f7b-a1b6-318f-9b43-6c466162c7df | -19.55774 | -56.63049 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| afd2582c-9921-3b6b-a916-e9c083528a3a | -19.55737 | -56.6548 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| de2e0aae-ded1-35f8-813f-1ccf48438c2f | -19.55736 | -56.61016 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 55d5a8e1-1c96-31b3-b44e-abc38ca79b09 | -19.557 | -56.67917 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 057b8afb-bd90-38b6-a5e6-8028b2decd34 | -19.55662 | -56.61405 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 47095172-0eb3-31c6-967c-0d70475d195c | -19.55625 | -56.6383 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b0504218-8b40-3286-ad3c-7f640cacd80c | -19.55587 | -56.61794 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9f741c8a-3f60-368f-be32-cedc40497a60 | -19.55551 | -56.6422 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1bcce6ce-5456-3f73-8825-1b9e0990a01b | -19.5555 | -56.68703 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9643893f-a6f4-37cb-b7f6-84e29ef34e12 | -19.55513 | -56.66655 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b03b2058-3548-39b9-81cd-3a53fbdb60d6 | -19.55475 | -56.69096 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0a808835-16ce-3c5d-8b90-2a70e224d722 | -19.55472 | -56.55725 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5d1f21d8-111d-30e1-9b32-dd7f3c1c53ad | -19.55438 | -56.67047 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 56fbf70c-326a-3fb8-91d0-c97e303c1e30 | -19.55401 | -56.60542 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4b0532fa-3df2-3352-944b-4602eaade338 | -19.554 | -56.69489 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1f27262b-7041-34e8-ac70-60671d1cc2fb | -19.55363 | -56.67439 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 2392d8c5-bc40-317a-95d1-dbc8684cc6ff | -19.55326 | -56.60931 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 61301906-a208-3d88-b281-0c03ac763009 | -19.55289 | -56.67832 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5549b361-cb1a-32e6-9663-87bc20cf9d68 | -19.55252 | -56.61319 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c1f97f7d-2bd8-3732-9998-77adf65fece3 | -19.55214 | -56.68224 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7daa0614-646a-33f4-9497-bdf9b185f745 | -19.55177 | -56.61708 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c2ec0b1b-8dc4-34b4-8194-52782dbf8902 | -19.55139 | -56.68616 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fa524a1f-7074-3c4b-ab2f-7f386c5ab7fd | -19.69061 | -56.77713 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 776d7ad9-8ddb-3e80-a512-14a74ad9b342 | -19.68648 | -56.77626 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0ba940c0-3df6-3199-b534-4195f38f2b76 | -19.68307 | -56.72624 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b5fc5891-f6cd-30eb-aa94-acbab3f2d1a3 | -19.6816 | -56.77935 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 248311ad-74fb-3c86-b5a5-8783b411f4ce | -19.6782 | -56.72931 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 80937695-21cf-32ec-afdc-4591ba42a83f | -19.66996 | -56.72759 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c1566c9b-9639-3022-82d8-f6e80f960482 | -19.6651 | -56.73067 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8088ad0e-73c8-3c31-90ff-7e50cbd8e293 | -19.66508 | -56.77588 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 806823d8-428a-3d04-a8d5-bfe9c8582bea | -19.66435 | -56.73462 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 1bd244ff-f5d6-31ca-a0e8-6c81a29c568a | -19.66433 | -56.77984 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a693aad8-6a06-30f5-b17f-d9e4b909ca88 | -19.6636 | -56.73856 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ddeb0f08-4b56-3650-9d6e-8692ebf7d222 | -19.66284 | -56.7425 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c0373611-15d8-3e7d-a7ea-f292e2fd22db | -19.66098 | -56.7298 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 61dd9b14-8885-34cb-806a-be0178b84322 | -19.66095 | -56.77501 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f8ffae8c-2196-3b41-9a5d-91e481e65347 | -19.66023 | -56.73375 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 989727ce-eff6-3779-9638-bd5849a3c80f | -19.66019 | -56.77898 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b5a2ad72-bc06-3f82-85c0-ae4ff28ce66c | -19.65908 | -56.76227 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d2055ee9-54ef-3a56-91d8-e53f28c02ce6 | -19.65872 | -56.74164 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| be2ae231-65fe-3a99-bf25-ceb4dbd0d2ba | -19.65833 | -56.76622 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 959fd748-0ebd-3de1-8468-12c6f2fd0bd4 | -19.65797 | -56.74559 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 80a4a2a4-4823-32b3-af80-d8e88a771148 | -19.65758 | -56.77018 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 02ed6df3-06d7-3cfa-b7e0-2b850d8be2ae | -19.65682 | -56.77414 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 46293d5b-18d9-3fe2-b116-2c53440e2853 | -19.65611 | -56.73289 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 27.8 |
| 2505408c-d4c8-3e88-a96a-3426d2eb9a36 | -19.65606 | -56.77811 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| fdd3e981-0ac7-3f88-924c-11ce7a577502 | -19.65571 | -56.75745 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 5acc45fe-5721-354a-9679-c43724a7e805 | -19.65536 | -56.73683 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 27423b9c-edf8-3d9c-8272-603c1ae763db | -19.65531 | -56.78207 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 49cc384a-7f02-3592-9cf2-6ada0a73bbde | -19.65495 | -56.7614 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 378c275b-cef4-355d-a59b-fbb4547ad705 | -19.6546 | -56.74078 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 56b5304d-3a4e-3937-aca0-3bf8b3d99966 | -19.6542 | -56.76536 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| cc91918e-ab6e-33e4-9754-c9bd3900b533 | -19.65385 | -56.74472 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4ea04990-7212-3b72-869e-f1061b8cefe0 | -19.65344 | -56.76931 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |


[Clique aqui para ver as próximas entradas](README57.md)
