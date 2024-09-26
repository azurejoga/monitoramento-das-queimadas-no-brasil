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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fdf71fe-5778-36e0-b9e5-ba697256b647 | -13.79525 | -48.07082 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45c43a08-a784-39b2-9df0-e23f6a7ce418 | -13.79499 | -48.1185 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2d0a476-1e64-35a8-9cea-8f6c3d7aa469 | -13.79457 | -48.07467 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a167a510-b1bb-3d8f-b5a2-6e37d879e666 | -13.79145 | -48.09212 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 509112f2-b7ad-392a-b695-dec097b8c116 | -13.79092 | -48.11821 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 023ad76d-1cb3-31e6-b595-b8a5815a58ea | -13.78897 | -48.10599 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e45668ab-e43c-3e7f-a2b6-d716f034ce55 | -13.78827 | -48.10991 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a4c85fc-09ea-39a6-920f-a90236afdb0d | -13.78756 | -48.11388 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8ff8d13-af95-3cb8-8d1c-c10322d6c2b0 | -13.7842 | -48.10959 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e22fea44-2b35-3d4c-8d72-82ba2a4406d9 | -13.78351 | -48.11347 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dee56d6-2949-3160-a8a0-fb8361e65ed1 | -13.7828 | -48.09437 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 127a6444-5e3b-3d43-9811-bbd39ca9fab0 | -13.78218 | -48.09784 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7c74514-4a5d-3132-8e80-a60f8dba63e2 | -13.78084 | -48.10534 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7813e82-edfc-3b76-b841-55d0c810a6c0 | -13.77936 | -48.0906 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14a53b4b-36a3-3707-814d-b87a83d5e386 | -13.77748 | -48.10106 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad55c66d-f71e-31e8-bf8f-848798abb3d0 | -13.77681 | -48.1048 | 2024-09-26 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a4c48ff-21c5-311f-80e8-fd10b98af049 | -14.5814 | -47.61123 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6616721a-71eb-31f2-a4a1-ebaccb7c82be | -16.0066 | -48.15097 | 2024-09-26 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c53ae84-e68f-31cf-9792-47811256492c | -16.00358 | -48.14545 | 2024-09-26 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d284e89-fdd2-3672-ad71-31903956c451 | -15.99973 | -48.21268 | 2024-09-26 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba3ec751-d7e2-37be-bd76-dbdbd574816a | -15.52977 | -48.51244 | 2024-09-26 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd10f8e5-ae52-3636-8cb4-004e1184772d | -16.35841 | -47.74244 | 2024-09-26 04:08:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2403bfa2-9ae1-336e-ae85-f2c859ceb0f8 | -16.3484 | -47.7115 | 2024-09-26 04:08:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be9aca7f-a6a6-373c-9d0a-5abe8f6e46ad | -16.34756 | -47.71618 | 2024-09-26 04:08:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eae304a4-f4c5-3b98-b817-e6bfa94f4afd | -16.34549 | -47.70605 | 2024-09-26 04:08:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09935a96-49e1-3d59-88e1-82a6fe9e45a0 | -16.34466 | -47.71073 | 2024-09-26 04:08:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1bd00333-2b37-3122-aeed-993999cb9f67 | -15.56793 | -47.85475 | 2024-09-26 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15036704-3d08-34d5-a6c0-744219dc49b3 | -15.30315 | -48.00544 | 2024-09-26 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8426e87-2a6e-36ab-8a0c-eb02dd3b5863 | -15.23275 | -48.0372 | 2024-09-26 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5537828c-fa18-3baa-9142-2cac14fde150 | -15.22698 | -48.2754 | 2024-09-26 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1886f64-9066-35fc-8d4d-b7032e954360 | -15.22607 | -48.28059 | 2024-09-26 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bf86b8c-62bb-3bda-9199-121512e0d7a2 | -15.20867 | -47.97007 | 2024-09-26 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 038edfab-756e-3267-89d8-875acaaf9b39 | -15.20483 | -47.9692 | 2024-09-26 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aea7e430-baf4-3cd9-9c69-aba1891ac4b8 | -15.57656 | -47.38745 | 2024-09-26 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e4c93bc7-506c-3d30-a472-d781625feda1 | -15.3304 | -47.4617 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7fd682b-1fbc-327f-a5c4-24602fc7a79f | -15.32589 | -47.4653 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| daca6e62-8f39-3ef0-b140-debb99f66c52 | -15.32443 | -47.47358 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ca88b57-0972-367b-956b-acd379da8cd1 | -15.32208 | -47.46491 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b5f628d-fb15-3b3d-8abb-783f2688f39d | -15.32135 | -47.46904 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 75707849-4977-3a88-907e-f4dbb3864a32 | -18.10057 | -47.98746 | 2024-09-26 04:08:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02a1f6a3-1ae0-3f1b-944f-e8f70c1cf1cb | -18.09974 | -47.9922 | 2024-09-26 04:08:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3d2af38-a3b9-38d7-bce7-115201787a97 | -18.09686 | -47.98673 | 2024-09-26 04:08:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dde74cd9-017b-3bb6-939f-3ba87586ebf1 | -18.09603 | -47.99146 | 2024-09-26 04:08:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a32638dd-592f-3c10-a5bf-7ff33315b19a | -18.03757 | -48.59759 | 2024-09-26 04:08:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 5c99fe3c-0bba-39d4-8597-964f771b2116 | -19.27668 | -49.12976 | 2024-09-26 04:08:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4cd83b11-0465-3e15-a177-27e16e2cbde8 | -18.27406 | -47.80793 | 2024-09-26 04:08:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17e73c9b-72e0-3b62-bded-08e0a3ac69de | -18.45012 | -49.21577 | 2024-09-26 04:08:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 927d78bf-060f-3d1f-b04a-1cb211e45b71 | -18.44907 | -49.21208 | 2024-09-26 04:08:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2a8a9a23-c4ec-32a3-96cb-a97965168bd7 | -18.20723 | -49.10509 | 2024-09-26 04:08:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d99446a7-9240-3a8f-84b4-e3ba4282a2ca | -18.1944 | -49.10812 | 2024-09-26 04:08:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| df6e6dc3-560e-394b-80f5-65c3c30a471e | -18.19335 | -49.11387 | 2024-09-26 04:08:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9a09b7d3-a57a-355a-ad6f-d8dfc3f2a3fa | -18.03664 | -48.60268 | 2024-09-26 04:08:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 402abae1-dc78-3f20-8209-29bc94d99116 | -18.04047 | -48.60351 | 2024-09-26 04:08:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 26d82eb9-beb5-31e3-9014-3d1a5c812f00 | -19.27279 | -49.12899 | 2024-09-26 04:08:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1f30e93-691f-3417-925b-b528430bfd9f | -14.81463 | -48.84585 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8994949-54b3-35db-9326-59a7f744d2f9 | -15.15415 | -48.77673 | 2024-09-26 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbfed4b0-7246-390b-84b1-44a19999e426 | -13.1405 | -48.54514 | 2024-09-26 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1a8168d-35d0-3c6f-b708-a0effed1c3c5 | -13.13635 | -48.5444 | 2024-09-26 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1db38b45-219b-3b4d-b649-76f1d9ad7678 | -13.13556 | -48.54874 | 2024-09-26 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b858151-b521-3401-ae55-36c47caee0b5 | -12.71583 | -48.43012 | 2024-09-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27c3d279-3002-3748-b026-7a7c807c9bd3 | -12.71338 | -48.42949 | 2024-09-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da518f03-d5ed-3f1b-8bb3-0f02334ea884 | -12.51126 | -48.92798 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| d3e5ed3c-720f-3198-9f28-cbbb00370085 | -12.51053 | -48.93216 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 8b6c6a4d-cee3-3362-9314-f019a23ebe26 | -12.50989 | -48.9218 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f491b89c-3e87-30a1-a528-0fdbb94705ec | -12.50912 | -48.92599 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0cbc8330-b56d-36e8-b2cc-6d351ca9bc1b | -12.50835 | -48.93017 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 18a5d0d9-7dba-3534-a2df-373a5dfa1a7d | -12.50771 | -48.92296 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 046be213-4ec9-33cb-811f-192706950b85 | -12.50697 | -48.92715 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| a054b1fc-fe0d-393e-a2d5-ffcff6db9ca1 | -12.50623 | -48.93135 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 6b412b14-6932-3da1-9655-a2d0bd19a748 | -14.81185 | -48.83789 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f19306ee-b144-33d8-928b-e71faf87a026 | -12.50415 | -48.91798 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 93710bc9-4496-33a2-b5ca-b0283cfe683a | -12.50341 | -48.92215 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e13e961f-ba96-3bc7-bc35-ac8a6203f33e | -12.50267 | -48.92633 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a1829f31-b2f2-3740-bb45-2b5ff0edd214 | -12.50193 | -48.93051 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0a56f447-a2db-3802-8db6-e2db9eb210e7 | -12.49986 | -48.91717 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8520a38b-6b34-35aa-b8fa-ec0a75bde451 | -12.49911 | -48.92134 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e4f75993-77a4-3860-83f9-fa4c69d1426d | -12.49837 | -48.92551 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 79b35147-004e-3dfa-ae53-9c68618772f3 | -12.49556 | -48.91636 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37f13cda-7f3d-3e3f-863c-184e6d76bc4b | -12.49481 | -48.92054 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6416017e-54f9-3091-8c06-537e12415eeb | -12.49407 | -48.92471 | 2024-09-26 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57197025-06c4-3f96-bbea-7903cc74c323 | -12.27595 | -49.20735 | 2024-09-26 04:08:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| baac4566-9be3-3755-ab03-e260fdb89f77 | -12.27515 | -49.21172 | 2024-09-26 04:08:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8f4fbdc-0468-3f82-a122-f0984cd98c12 | -13.1413 | -48.54074 | 2024-09-26 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bad0fe0f-7c6c-344c-9582-00361eb179da | -13.13716 | -48.53993 | 2024-09-26 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fa01ff9-a14d-3cc9-8e0b-8b933082d0e3 | -13.07995 | -48.51477 | 2024-09-26 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86280b6e-674f-322e-95ee-cdab1dae48a4 | -12.97731 | -49.33508 | 2024-09-26 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e551b5b9-5da1-32aa-902a-0a40e95665ec | -12.97676 | -49.33818 | 2024-09-26 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d09caa65-abd7-3615-82f1-cfc51854b147 | -12.97653 | -49.33941 | 2024-09-26 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a87117d6-3ce6-3e6c-9cf4-c5fc6fc827e8 | -15.17301 | -48.81174 | 2024-09-26 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87a4e51e-79f4-3699-9a7a-335ebc0cc0e0 | -15.15131 | -48.77311 | 2024-09-26 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2118099-eee5-3a40-8c33-56eb207976e2 | -14.84832 | -48.89435 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ac0f5c6-b309-38fd-b8c8-1bb8e9477d5e | -14.84421 | -48.8935 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd49bce7-d8f0-3c82-876a-f89394515381 | -14.84132 | -48.90931 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af9c310d-cdda-37e5-9941-50eb4d7d162a | -14.82898 | -48.90678 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6794506b-a2a4-3818-a09e-1b2d53236d53 | -14.8283 | -48.86403 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e3df084-4b86-31be-af63-0106bfcceafb | -14.82488 | -48.90585 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 351385c0-2594-3134-8d54-5d6b30157d0f | -14.82086 | -48.85818 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bb9b259-c606-3600-8cd8-10e7846faa71 | -14.81679 | -48.85718 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21489972-5ed2-3410-b0b4-ed5d2c2eff47 | -14.81527 | -48.84235 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 751d4052-872f-37c1-8b7e-fd793ef49105 | -14.81121 | -48.84134 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README75.md)
