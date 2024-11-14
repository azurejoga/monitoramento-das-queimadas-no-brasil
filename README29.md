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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf2ee8c4-1790-348b-9e00-83bf112f5f44 | -5.8584 | -46.42391 | 2024-11-14 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02f05149-1c70-35f2-a297-c83e246bbf06 | -3.80381 | -47.46046 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7d955fd-5215-3b3c-badd-e1ced6310fca | -2.69754 | -51.87423 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2882dbcb-5ed5-37d3-a908-08982f8570cc | -4.44635 | -45.36733 | 2024-11-14 04:40:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d348245-e4b4-35e7-8432-09347501f2af | -4.45399 | -44.93247 | 2024-11-14 04:40:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e0edd13-d8af-3166-b63b-59e59843ee03 | -3.27991 | -50.05652 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da9fd10c-a51e-37b9-a950-f204871431c0 | -3.03584 | -50.32694 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cacf38c5-647d-3836-b007-f5ccd9a25d11 | -1.66498 | -46.22871 | 2024-11-14 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7149c6f5-9828-3b6e-86b8-097d656d7da7 | -1.22779 | -51.74932 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8022f5b-e115-39fa-94fa-2e5783b9e53f | -4.26801 | -48.19065 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e3a7a7f-9136-342a-ad9d-7a34627da1c5 | -4.50959 | -48.6949 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 571776c7-3267-3e5a-ad46-3ed9b08e0e15 | -1.59967 | -47.3288 | 2024-11-14 04:40:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b959522-59d1-389d-8dfb-c7d562b80a8c | -2.9514 | -48.01932 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98d05200-11c3-34ee-9cd2-668e50254af2 | -3.30523 | -51.28637 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19ad7b1a-efe7-34d5-a2d0-7958f88b9fdf | -3.03807 | -50.33461 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7c8f593-91f0-3152-adbb-df8ab108ccbe | -0.93529 | -51.72472 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac0af10b-641e-327e-967a-b0ae1f3ad2e6 | -3.05122 | -45.52667 | 2024-11-14 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c6a30af5-810a-3c20-a6f0-592e745df856 | -2.8926 | -46.86596 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e3dd7a30-6a87-377f-b181-6fc9268a8aab | -2.63141 | -49.50463 | 2024-11-14 04:40:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a25e801d-3000-319e-805d-9ad67c08ac62 | -5.60544 | -45.26064 | 2024-11-14 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3763782e-5248-3d96-ad5a-cb6c95e8ea44 | -2.74892 | -51.6215 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7be87f25-7968-36d9-84d8-bfba5c7c9a19 | -2.64916 | -46.82934 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3f12776-fef3-3fd8-9285-2271d2dbe243 | -5.35331 | -44.36991 | 2024-11-14 04:40:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34da3214-0b01-327c-9b04-2dd41b1dc705 | -2.25803 | -48.73702 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cc87710-86de-309b-905a-eb428e5e60c6 | -2.09075 | -47.73586 | 2024-11-14 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2525a56a-8a8d-3ecd-904f-d6d8dc079a8a | -3.02408 | -48.0553 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fd9c642-e541-342c-a74d-a68defd2de03 | -2.36374 | -48.51817 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd43b070-deb3-3249-b398-fd75fd6d67c3 | -4.42658 | -49.68359 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e7b51a9e-f6c7-3d8e-8784-27d945ffd249 | -1.57503 | -52.01999 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aee4d264-9eaa-37bd-8718-1d366f5af566 | -4.15843 | -46.24858 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69491203-7d9e-3985-b758-c3c3dd89f8d0 | -4.75582 | -46.01184 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 085f7524-41f7-3e53-9b3b-802506f01574 | -4.21247 | -50.69808 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf3bd579-5505-3459-8ce6-bd66d09f3d1f | -2.29807 | -48.58868 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97a8e986-47c1-39ec-8869-b069cec2d9a1 | -4.11552 | -48.49479 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd8e999e-269b-396e-a3bf-feee36e7b9f5 | -2.37695 | -48.52021 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f49b14f3-321d-35df-93c6-6042f8459c80 | -4.17651 | -46.10561 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14c1051e-28fe-3289-89de-1c38bf74ea2f | -2.21998 | -48.36925 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f34374a9-4177-3ba3-a362-aa77c033f459 | -1.22548 | -51.78766 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28e56c77-8371-3dca-988c-ba6415a21af2 | -3.13416 | -51.12006 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d30ae634-ce06-3b6d-b5c1-af0ce629163a | -1.33949 | -51.42948 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75c4df92-3d1a-39e0-8ee5-fa1e4cdf38ca | -2.22284 | -48.39431 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec8ccd36-3b55-371c-9751-40c582458e0a | -3.93211 | -47.33463 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7750daf9-9cf5-3c47-9f05-821a2e3d757a | -2.64032 | -46.15708 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8ef9a70-a14f-38fa-98e9-ddeb079d90c6 | -4.85496 | -46.97139 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b68e4256-3928-3ebe-b0f3-b283d187763b | -2.41949 | -46.27243 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 39d946da-9c45-35b4-9a56-d8ba717cad45 | -3.27641 | -51.26622 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95a8b9d7-876d-3f99-98ce-709b43bde756 | -2.36564 | -46.9866 | 2024-11-14 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 068f2167-1af3-341c-ba08-9d1a5b362e69 | -1.13594 | -51.68929 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2b5a3fb-2a1d-3994-ae27-6384036483ff | -5.19727 | -44.35801 | 2024-11-14 04:40:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b905f718-a8cb-3b1c-ad8c-a5e657e11219 | -1.49492 | -51.1598 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 987e083c-029f-3538-a882-2a0621c0f08d | -1.14021 | -51.68569 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b25afa5-daec-356d-b903-6c275a7d7837 | -2.35342 | -51.98479 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88abca5d-132d-316a-854a-f81c78a19b19 | -4.26413 | -48.19365 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40c8fac0-86b8-3486-ae3f-ad48f1db772f | -2.63318 | -46.18018 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4f2c4a0-42d4-3fde-8f64-5b8a6e50095d | -3.40892 | -50.3156 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bdd9bfb-f732-30a6-8c9a-5cdabdbe8974 | -1.38978 | -52.0775 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e981988-569f-3569-960d-e1198521fe13 | -0.90128 | -51.72812 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf0fab74-edb7-3810-a2f3-5cf869a909cc | -2.17605 | -48.39064 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c02c5cf4-9878-364f-b69a-46635528a06d | -1.84509 | -46.28661 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d53c6161-dafe-3e98-8cdf-63b00b971837 | -1.56001 | -51.85309 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e0eb661-49ed-3941-8142-bb605c19f479 | -3.09956 | -51.27893 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f4c59f7-4446-3aeb-b9a1-e42943567a47 | -0.66377 | -51.68998 | 2024-11-14 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c99768ce-d9da-3545-8cc0-5e5b123ca340 | -4.04761 | -47.22443 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84f8bfbb-268e-31fb-8b5f-f04d797ba0ba | -1.81686 | -48.00964 | 2024-11-14 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b405c326-1b13-3c90-b839-5d3ba25d02e6 | -4.59366 | -47.07239 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4409b7a-8130-32a6-a985-e6ba04661cb7 | -1.64262 | -53.2765 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55cd710b-ef48-36d6-af07-cdec134c31da | -2.95912 | -48.01322 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f17ca02-4e3f-3a95-9bfb-41841fddac55 | -4.30071 | -48.17768 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 967d7383-6a16-3245-b7e3-0a62b00a2d1c | -2.27925 | -45.45827 | 2024-11-14 04:40:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91736af2-bc11-39e1-b942-3f76ca75376c | -5.75347 | -44.34106 | 2024-11-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea2bd282-b6de-31ef-8549-a53452139f64 | -1.35295 | -49.15128 | 2024-11-14 04:40:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76918b7b-e6f9-3dec-aced-ce420bf3c682 | -1.64478 | -47.25957 | 2024-11-14 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c505cf5-9d25-331f-a56b-4d9d94c3d439 | -1.41526 | -51.11221 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b8bb5e5-f701-37e2-8100-c2d7931df0f6 | -1.3861 | -52.07695 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd1afbdf-3782-390d-aea8-7f91300d7692 | -2.17798 | -48.9249 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c0f5757-39e4-3706-b7bb-15ccb220f1b0 | -1.39133 | -51.10454 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f1aa196-baea-32ce-bccd-7c3356bb635e | -2.65031 | -46.82192 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f03a6ad-8c06-3189-bdc5-afc7fd5b9e42 | -4.85728 | -46.97073 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 776ae7fa-4153-357e-ab19-ef561d11cf1b | -5.60515 | -44.88383 | 2024-11-14 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 180e0a2e-b4bd-3912-bea5-3d550d1285d4 | -6.26866 | -44.54506 | 2024-11-14 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b9616923-f14d-37c9-9870-33d30c536fbf | -3.45777 | -51.20461 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4259ee71-61fc-356e-bb07-6b8dc6ce9914 | -2.34123 | -46.09778 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c84b7bf3-5073-3d14-a7ea-e545bd5521c0 | -1.23207 | -51.74569 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d2e302c-f1c8-3e08-8706-0fd56d38391e | -3.76834 | -47.48832 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1eb511a-7408-3627-a358-10227aa07e5f | -2.219 | -48.39724 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47bd2c3f-1199-32b4-979a-b982f1852cae | -2.30359 | -49.12035 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 820c9a53-cb67-3940-947b-8f1f4432a2db | -2.43821 | -48.93416 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d9a0411-a10c-3e57-b5dd-f6ee443a9a62 | -4.44297 | -45.95177 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0bb6ff8-9467-3876-b4ab-8682546e6057 | -3.89306 | -46.09113 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5501bc8f-b2a3-3daa-bb56-38aa3c5d249b | -1.33543 | -51.41264 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edd21c07-cdd6-3f69-9f82-133d6ebd332a | -5.15627 | -46.08844 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 320c4362-760b-32ac-a77f-54438b4d726f | -5.07302 | -46.14164 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 810070e6-2578-391f-826d-d656e54d6641 | -1.45207 | -52.2512 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b367fe03-4ccc-379d-8459-fe8c1c15f901 | -3.46877 | -50.30665 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47413fc9-1e2c-30d4-abfd-04a690bb83f8 | -0.82165 | -51.75625 | 2024-11-14 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a82af38-bc11-3a8c-9efd-62dca3e250a6 | -4.53473 | -48.64208 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a91830b6-7b9c-34b4-b014-e6fe70d30907 | -2.89445 | -51.68802 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6984e5b0-7541-396b-b982-bc4f793ac726 | -2.72682 | -51.73712 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89b4421f-8e27-3d1e-a6a1-1f63ff38af29 | -3.03322 | -47.97459 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6c6f851-71b2-3f32-a4e0-57eee19b4be2 | -2.27324 | -50.8158 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README30.md)
