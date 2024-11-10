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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 533ba5f6-4a5f-3737-87fc-77828d2ef01d | -4.48945 | -44.48475 | 2024-11-10 04:14:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58c61fe3-6f12-3698-9080-dbcde232ca4e | -3.88498 | -49.94925 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16776a2b-8ae1-361f-a0ad-728abec9a3df | -2.91715 | -51.68237 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee90c8c7-6572-3fc9-823e-a1da08fa5067 | -3.59712 | -47.34986 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 28a67781-4227-305d-a4c8-1be76d7d0e25 | -1.54254 | -52.21464 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| aa792aed-fa6e-3a9c-bc06-3be7320b1b1b | -3.21275 | -50.38948 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 41bbb578-76d8-3cd5-a2cc-5e5956c74931 | -1.65781 | -51.91179 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6b4e32e4-37e7-3cf3-b573-b05c228fb2ba | -3.92564 | -45.00766 | 2024-11-10 04:14:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29fd696d-8429-3bd9-a112-d488a362bf6a | -5.5691 | -43.979 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3edde13-5e46-3e92-ad45-85678777918e | -3.21789 | -50.2963 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73647ea5-a9fc-37ad-9e76-162951a78b65 | -3.38187 | -50.22665 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 022304d6-053f-3f25-bb7c-84f9e6410686 | -3.04532 | -48.03564 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c67834b-1c06-313b-90b6-8f591e746b2b | -5.81854 | -44.12277 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e7c3b13-47d4-396b-810e-d2d1e5f1ef17 | -2.75779 | -49.36248 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f8e8a282-d870-399f-a793-525052921221 | -5.38475 | -42.76613 | 2024-11-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b200d54a-f375-3271-8391-0af3f8d85b9d | -4.1041 | -45.70333 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4710759-0355-3c4a-b71c-7f129cfa63f9 | -2.16222 | -48.53577 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ff151bb-01d4-31ac-9bc2-5b15651f00c0 | -3.24536 | -50.30275 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9495d85c-2171-3c5e-be83-2e06a1fe0c3a | -3.30166 | -50.14391 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45fd69e5-0914-3657-b519-0285e7004ce2 | -2.56627 | -47.35218 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1052e935-5824-3f42-b738-a615e6bb6975 | -1.4838 | -55.44456 | 2024-11-10 04:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 306ab6be-c47c-3e80-a4f8-8d1efbcc2767 | -3.05037 | -49.52891 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 019dd796-01f5-3b61-a6ec-e217ab379c8a | -3.44203 | -50.43154 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 249caf19-9b97-313f-aeae-a2de696b250a | -3.5352 | -49.26401 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb18beba-775c-34de-ba49-6ae22151a544 | -2.42071 | -53.66005 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fcdfb215-ba6d-37f2-955f-83c2bf1f7bf4 | -0.04193 | -50.77332 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e86b346f-5f93-3d15-abf0-0664976fac99 | -2.93928 | -52.77016 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e49e702f-8d97-3d5c-b988-a6f93c7d1f46 | -3.80645 | -49.94414 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1926de15-56ce-31c8-9f77-c12aef961955 | -3.69563 | -54.62119 | 2024-11-10 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c988238c-48f0-34d2-82ed-1c32362a6516 | -2.46604 | -53.69104 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb02d998-e0ba-3e16-a958-0b09d841632c | -3.18661 | -54.31378 | 2024-11-10 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3597902a-7dfa-3e1f-9e8e-ce51b6896613 | -3.98605 | -46.4139 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db650fd3-a26a-3272-b418-e8095feec467 | -3.24128 | -50.30557 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 215bd6d2-3915-3e52-a7e5-059c4069942b | -3.0355 | -50.35379 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89a77fe8-bab1-39fb-a32d-ce7dc768fe6a | -2.21266 | -46.4155 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa4c5b19-dd3f-3f05-ba5c-7bbe9f839f50 | -2.22712 | -46.42263 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 379399b3-5abc-31e8-8332-9d42e1fab981 | -2.63504 | -46.76822 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8f64f081-1b8a-3e3e-809c-383f54a8246c | -5.14344 | -48.24983 | 2024-11-10 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6ef21f0-bd30-31c6-8520-612e8254e429 | -2.64459 | -46.79283 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03d07f27-0c2a-399e-9af9-ae1eb4afd5c7 | -2.67517 | -48.65953 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97b1f5dd-8a16-3065-885b-a592384acb26 | -4.36306 | -48.14805 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 24c89399-b799-3c62-8aef-51b1904ac7d7 | -2.67954 | -48.66021 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da8bfde6-fe6f-370e-baa8-2a184921f781 | -3.0283 | -50.34963 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a65488c-f554-3db7-9964-21c0b8f7061a | -3.24298 | -48.74849 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db3ef1b0-a890-35e2-93a1-eeaa60cc3cd6 | -3.21851 | -50.38485 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7c93ca00-bb44-36f7-a84e-be178566d9dd | -3.17374 | -50.59886 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4754e7d0-e703-3bae-bd42-cbd0b2e05f7d | -3.49648 | -44.87906 | 2024-11-10 04:14:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dc0a087-a743-354a-be0f-2b4146d1ab8b | -2.14378 | -49.14003 | 2024-11-10 04:14:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65e8edcd-4508-3366-aecd-5b3a53c76e7e | -1.2453 | -51.76717 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8634dc96-709a-39fe-8ae0-2e9f2891b0d6 | -4.88308 | -48.58854 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 816a462d-40b4-3c96-b3eb-7b0df052d408 | -2.70452 | -49.34175 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1da6dfe-baeb-3e15-8feb-c69b5c2aeede | -3.10708 | -48.61695 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 755ebccd-9378-3ba3-9d24-f27593d67cbd | -2.55034 | -47.45074 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a08700e8-8408-3b68-b62e-1195dbe291fa | -3.6771 | -50.22214 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d1616a7-bf56-339d-9658-4339fca1ce60 | -4.57937 | -45.40812 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e258c8e3-e933-3901-a8c6-384d075141cf | -5.22096 | -48.28522 | 2024-11-10 04:14:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 61793782-9b51-3671-ad80-ac42ac3a088d | -3.03994 | -49.53936 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d196a98a-6e88-35e0-8c18-f12e27dc8055 | -4.93375 | -43.73528 | 2024-11-10 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbea7276-e7aa-37a7-b54e-05f4834c9824 | -2.76255 | -49.36073 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 68d4d4b2-ec01-35d2-a075-b8021e4ed1d4 | -2.92393 | -49.49899 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79262394-fdeb-34f4-a893-a5ba1666475e | -3.60079 | -50.23703 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b41c775-6b9f-3abd-b380-d046a05fb910 | -1.94599 | -46.40664 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d41977d-9373-33f9-8b72-af89abd56db0 | -3.3098 | -44.39497 | 2024-11-10 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e6c8e39f-5ab6-3309-89d6-5ace2e80cd00 | -3.13434 | -50.43865 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 203.7 |
| a4911839-4296-3afe-b3b8-4e24370de9d6 | -2.1017 | -46.55475 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da854728-f56a-3671-bfc5-e5534983ec9b | -3.62034 | -41.57798 | 2024-11-10 04:14:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d65f5e39-19ff-3c75-887d-8ee6678b777d | -3.35466 | -50.12049 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db8dc03d-c407-3204-a583-7d6981d5af2e | -2.53606 | -46.30955 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27915a3b-9685-35d3-b186-5ef1238a2a55 | -3.12042 | -45.95991 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f1ac01b-4354-32c6-90d5-2c9b241b459b | -2.61817 | -54.39737 | 2024-11-10 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b4f8cd77-0da4-34e2-85d5-342fcbb2078b | -6.15288 | -43.07738 | 2024-11-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4635628-7d14-3535-b214-4f4dd1aeaf5b | -2.24417 | -53.77212 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b04110f9-0332-3b04-836a-f12153828ce2 | -5.46891 | -41.65082 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0fae63b7-388b-3f3e-bc38-a50e14d4b072 | -5.21174 | -48.34029 | 2024-11-10 04:14:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c8a417f-93ba-3a28-83f4-edd20b0666eb | -5.56633 | -43.97497 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2ae1d9da-8122-3cc6-98fb-1ec67f9a579a | -1.1521 | -53.78613 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3f48fe50-e5c8-385d-b1f8-a07c4d7c8398 | -2.35188 | -46.63578 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d2b96c0-2394-3196-9226-1b3e3b5ba83f | -0.1471 | -51.5621 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6920335a-cfe3-33b6-9de6-e2a4c792ccf5 | -3.94793 | -48.15089 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f08e6f98-eac5-3c69-b007-4774d5d0eb65 | -3.90163 | -46.44137 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 71b20a0b-db84-3ce6-8a2d-6cea8b5f295c | -3.0625 | -51.38341 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6abbc5b8-494c-3776-97ca-9a6a0beee036 | -2.11418 | -46.22827 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| facedeb0-d068-37f8-983e-891ccfb66f97 | -4.11859 | -43.59647 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 74a69c9f-f5f6-309a-8678-9f206d92c876 | -0.04721 | -50.7741 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05ab7ba9-edb7-3279-8e33-0c76f5bae228 | -1.20496 | -53.62321 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fcb4afe-1318-3722-b125-f203b39ff7b7 | -3.23738 | -46.53734 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db8eeef4-076d-3df3-bba9-e21483772d92 | -4.12192 | -43.59698 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ab6011d4-7d04-3738-a345-cb1f0ec051d7 | -2.67462 | -51.81765 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c79a654-6aaa-30ab-98ee-548fdfcadcca | -2.67011 | -46.78193 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0d2854d-b389-37eb-9b0b-5425f0801da9 | -1.15133 | -53.79073 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 98636cde-caeb-37c4-a044-c2fdbb7ab5b8 | -5.23752 | -48.16134 | 2024-11-10 04:14:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3548b1d-8fdd-3bdc-b10e-9ed7bdec63a7 | -2.87704 | -51.65867 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e3d76ac-5a24-30bf-b617-9ecca5068f6d | -2.31412 | -50.67179 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 647055c7-bfec-3b72-a315-57384aa2281f | -3.01792 | -51.0399 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c136e6c6-81a0-31ba-89ee-1b51cbf87025 | -2.37204 | -46.73228 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94458299-d56a-3136-929a-7f70540dbac1 | -2.52064 | -46.38208 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a515560-e74b-3c1d-b5b4-59e7be6359e0 | -2.69353 | -51.70021 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c524f53-0e5b-33b6-955d-55989a358a01 | -5.44824 | -43.27336 | 2024-11-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 642d8046-8479-313e-b7ae-47dd34c6ef0a | -2.60026 | -48.18879 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bdbfdd2-855e-358f-a7ec-3aa56799a1ff | -3.31321 | -44.39549 | 2024-11-10 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README38.md)
