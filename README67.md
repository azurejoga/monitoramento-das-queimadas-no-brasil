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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baecdd70-a750-3de7-b70a-507723e2ad53 | -3.44356 | -50.08968 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 073e7d67-0460-3b41-a8e0-4e52fe900e72 | -6.67729 | -58.55208 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c810cdf-86a9-3b99-a089-ce8abd5fa557 | -6.61986 | -57.98338 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5794b0c-26d7-3776-b0bc-42232dfea951 | -6.11506 | -59.88914 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65d86137-6987-3f77-87be-32d9da6b8e9d | -10.14475 | -45.54182 | 2026-09-24 05:04:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68a90de2-e63f-3ee8-8791-26ef361de735 | -4.11034 | -51.08132 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 35a3bc67-4e5f-30a7-a7b5-a3e488fa73ce | -8.76408 | -45.82973 | 2026-09-24 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69eea3ee-0dc1-3388-a232-bea8c2e39a96 | -3.21057 | -53.40144 | 2026-09-24 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 784464f4-8b8f-329c-840b-01a0a7812ea4 | -7.20012 | -47.45556 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fe92bbb8-174a-3eba-9ff2-3dea60a6b7b6 | -5.59805 | -60.2014 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98d9f209-1a90-316f-ac57-ae209e8c08bf | -2.92853 | -56.58289 | 2026-09-24 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8e86b13-0598-3c30-8ff7-562f88e4bef1 | -8.20766 | -54.73208 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74863f6d-63b8-3253-9039-39742121c8a9 | -1.68686 | -55.02423 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e862fabb-f237-3250-878e-a95eb1c1a5d9 | -5.876 | -51.93877 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 243d758b-72fe-34dd-939a-a2462263a6a2 | -6.45863 | -55.00702 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c60394dd-a1d6-3e16-84fd-fb1d526999b3 | -6.89812 | -55.57414 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ceb31abe-cec2-38d9-aecd-972fc5e53963 | -1.21672 | -54.55996 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce66b577-afb7-329b-a5bb-1e7eca2d3004 | -5.81724 | -57.7384 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcd833d7-2dcf-3dd1-9675-50ac73132504 | -3.45069 | -50.07914 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f0aab837-1be9-3d26-b947-71e3d16a0702 | -10.13954 | -45.54115 | 2026-09-24 05:04:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d398472-4c9b-364f-8b22-8449f3efd803 | -6.41223 | -44.49574 | 2026-09-24 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7253ca63-5326-35cc-a296-ddc90a3fd6e3 | -6.31561 | -52.67027 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d97b6443-e75a-348c-a66f-9cbf0453e506 | -3.77063 | -60.72271 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cf8caee-ace8-31e8-8544-d97f3a7842df | -7.47427 | -44.57601 | 2026-09-24 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca3756d2-ea1e-32bc-b67e-7ee940fe0724 | -4.54115 | -54.96996 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21b43965-0b44-3a00-949f-877b3b2d67cd | -2.97161 | -50.39242 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b2c0d6e-c586-30fd-a84a-89f99ec57dec | -2.56543 | -57.49489 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92d49949-59c7-3cd9-b79d-730cc4dd8551 | -8.45704 | -51.48087 | 2026-09-24 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af67578a-7752-3067-a952-2dacc690a98c | -8.14717 | -49.54725 | 2026-09-24 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ce6c063-b3da-37aa-9d73-4caf3e10ee53 | -4.99514 | -45.54886 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 31ddcddf-4271-3669-b334-df3ce1355033 | -3.44993 | -50.07256 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d0227506-2175-3bb7-a370-d6b2ae81b573 | -6.61912 | -59.92972 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51d1ff0e-d4de-30e6-8ebf-3f0e69b47aca | -8.89946 | -46.81807 | 2026-09-24 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec61de10-a3b0-38f1-9aa0-80743eab88b8 | -8.20986 | -54.71819 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 260836cf-91f9-3b1a-a33e-64281ff9b66d | -2.24722 | -48.74897 | 2026-09-24 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 364b774d-92b8-3e98-ab02-c160eaaf8e4a | -3.71146 | -54.20733 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfb7c9e8-aad2-3ff5-8988-0f02cb56f0ba | -6.88589 | -55.56492 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30c7ab44-5395-3217-8593-8fbb0d89bbd1 | -5.87439 | -51.93818 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7cf2d8e-322d-38ea-ab9c-8badec1bc84f | -3.41293 | -50.75055 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceaa9228-ca32-3a6e-91cd-b2df1f1514f1 | -3.81943 | -54.55511 | 2026-09-24 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a985024e-7a05-3d0b-82cf-0452d7015e97 | -6.14871 | -52.74954 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ba37d4f-ba76-3546-bbc5-6fbe95102949 | -2.95964 | -54.08539 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ee8ce10-f0ed-36be-b98f-474e59cff3aa | -7.04294 | -62.93594 | 2026-09-24 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0924bfd6-e5f3-3d1f-a80e-1419c199f43a | -8.29498 | -50.84679 | 2026-09-24 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0edf999-9101-3518-b6c9-1d7351ac8898 | -3.01016 | -51.5319 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e618969-7d41-316d-886b-583057c4be5b | -6.88927 | -43.75018 | 2026-09-24 05:04:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f736cf1f-a8fe-33d6-8ed4-b00445fd2f6c | -9.26433 | -46.24099 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e165638c-e1fa-37c3-844b-c01b7d33217a | -3.44259 | -50.08239 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dac6078-52fb-310e-a1a5-be4e98434c5d | -5.84015 | -53.85156 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9abc31d9-cffa-3db3-ac66-198a8c273d45 | -6.03932 | -57.77535 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c0e8a03-d0e5-3cbf-8ad0-43725ab6d3fb | -2.94584 | -54.08676 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a037c794-a336-34e9-b368-f0d059b61653 | -6.65458 | -55.05645 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be6de125-0d2d-3f1a-b9e4-3a41bab0c025 | -9.23963 | -47.37364 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| ceb5d3ac-8774-3a31-a935-4565d29fcd31 | -7.04398 | -62.93006 | 2026-09-24 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc515515-d9ce-3d6b-9dfe-e78af2371e42 | -5.9916 | -57.72458 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8ab7a58-2d30-355a-8d21-78eecbb151b9 | -3.15933 | -54.60447 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bfe030f4-bfd0-3a99-9567-3fba602f2f5a | -6.09036 | -57.62627 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4414b85-29e0-391d-a1a6-bc316786104a | -5.49722 | -49.0336 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 604817e1-26eb-3146-87e7-ca130bdd75ac | -6.87984 | -59.86171 | 2026-09-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22a207d9-4ab6-30ea-bb47-29035c83b84f | -7.46341 | -44.57092 | 2026-09-24 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dd8213a-ed09-363f-876d-fddde8d6be71 | -7.19706 | -47.46753 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a5e16e8-715f-3b23-b8fa-4d2186103a63 | -7.4439 | -49.83712 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d40622cd-06f9-3427-a317-a6833f70504a | -3.45 | -50.08355 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eeb0ba49-4fd7-3555-bd29-d79b2e0ad267 | -5.99972 | -44.1062 | 2026-09-24 05:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 150f1e85-8926-3aac-9f8e-a123eb9d53ca | -6.7839 | -48.6862 | 2026-09-24 05:04:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0a3650c8-eb89-3bbd-8b8c-177f565b832a | -8.26299 | -54.7697 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b32f611-a2f3-3abf-acdd-697a4bfc06f4 | -6.34026 | -43.36643 | 2026-09-24 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 160d59ff-2f70-3c7f-8c88-7407a10005c5 | -2.45016 | -49.22282 | 2026-09-24 05:04:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3534859-3aaa-3bb7-8b81-1550bb82e708 | -3.64784 | -60.61359 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1eb0f45-1b57-3cc2-92ba-7f8f5a39cc01 | -6.6689 | -58.55548 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8d4061f-c1ac-3c4e-97c4-aeeb5eb2aa02 | -7.58513 | -57.65845 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f20e05e-abda-3f60-ac3a-03e277e55e6f | -6.02628 | -53.89894 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dff64417-c443-388f-8e49-790ac801fbd3 | -5.78567 | -50.20361 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45e5c5da-87df-3498-8eaf-6f9992f8d130 | -4.25822 | -55.76595 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8876ad1a-8fb9-3e88-94db-04e506512981 | -6.88984 | -43.74598 | 2026-09-24 05:04:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2bcdf3e-58d5-322d-9a0c-d5fc29570440 | -6.3285 | -59.96022 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5af8a1d-430e-3216-9145-de26513c78c6 | -6.16763 | -57.7025 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e9da0f2-48df-3f55-a55f-007c3bc1670a | -3.45209 | -50.07028 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5e1890f-322f-317d-88cd-a7c5bd4b5f52 | -4.35961 | -56.22336 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f5b6804-0001-3269-9a88-72f517fdf163 | -8.30902 | -50.38133 | 2026-09-24 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eba97ff8-4e75-3fe1-a692-ce63a1c2bb1e | -6.01498 | -59.93951 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 024f3ee5-f9eb-363b-9097-95b0327394e1 | -5.9583 | -49.97408 | 2026-09-24 05:04:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3a09543-968c-37b4-ab94-7bc140b182eb | -4.49836 | -54.96354 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 087abcab-0215-3c2e-b51d-ae3071b23aea | -5.59512 | -60.19257 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25c7c814-1ae1-36e1-aeb1-753476c4cf9c | -4.25881 | -55.76225 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cca57f7-2fb8-3355-9d74-f675ec6cb65f | -6.63155 | -59.93186 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54037c09-0e15-3acd-856f-6385aa2d97c9 | -3.68429 | -60.56287 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e084a21f-ce7d-34e4-b7ea-174c1c971091 | -2.71452 | -57.50777 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 45ff707b-f5b8-3816-9b70-9450d8e6be50 | -3.82275 | -54.55564 | 2026-09-24 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4057d4b0-21da-3c5b-aa76-d38eb52240d7 | -5.95606 | -49.97634 | 2026-09-24 05:04:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48a25581-0621-3b3a-bafa-8589c04e4185 | -2.38787 | -48.52764 | 2026-09-24 05:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 308c5667-2211-3860-be09-9b3e7cd7641f | -7.03038 | -44.65614 | 2026-09-24 05:04:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a1eda11-6b16-3335-b947-72c72f7b559b | -8.2707 | -54.76381 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5570374c-4b1c-3dcb-b34a-e3fd97a422a6 | -6.43999 | -48.46932 | 2026-09-24 05:04:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 290f40c5-0fec-312f-8973-e805cb13a5e7 | -3.6858 | -60.55375 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e6d459d-7dcb-3691-a6da-8841ea7244af | -8.08357 | -54.76566 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8eb8a52d-78eb-31d9-9e65-adf3720876c8 | -3.68127 | -60.55295 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 064eb823-87f1-3fe3-9874-b42be3583f6b | -6.09589 | -57.68335 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e14d0fb3-1a4e-3c18-8eb3-bd5d2d2895cb | -3.5001 | -59.17529 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b82daa5-d5d2-3c2e-b549-7bf9b11e41ad | -6.0437 | -57.77165 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README68.md)
