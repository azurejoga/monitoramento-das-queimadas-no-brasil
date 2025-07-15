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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| feb1dd96-2928-324d-826d-e223085b80dd | -11.85415 | -46.75424 | 2025-07-15 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bc500fa-eaed-314d-a169-afd0e16003df | -11.45039 | -45.13283 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79cd8e6c-9796-32ea-b433-ac4bc71ece0a | -11.46331 | -45.09162 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| fc2d14d5-b0ba-3e0c-986b-0f143e799b7d | -11.44763 | -45.09142 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| c940d01a-21a4-3bf1-9b09-39c83be198ce | -11.45718 | -45.09641 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 91a432a8-c131-3d53-9a02-6336322aaee8 | -8.64918 | -47.75002 | 2025-07-15 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 663e58ee-559e-37d7-8a9c-61b26cca264e | -9.98307 | -48.08714 | 2025-07-15 03:45:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea0abf71-bce5-37ce-b789-4610a5b7c6f8 | -11.46056 | -45.10643 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7724931e-a75f-3122-a61c-77124d218cfa | -11.90028 | -46.75593 | 2025-07-15 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fb3051f-98d0-3a0c-9900-0f23f1a83073 | -13.13099 | -47.27113 | 2025-07-15 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad98097f-55d3-3db0-bca0-99f5c21aad0b | -11.451 | -45.10143 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 372de187-9216-356b-9f65-a8c6f7e41800 | -11.80343 | -44.26534 | 2025-07-15 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 464a36d6-a8ab-3f86-9feb-c5e57e8955ce | -7.30833 | -45.36165 | 2025-07-15 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99f379c2-97d5-3b33-a6c3-04d6dbfd8840 | -11.44026 | -45.13083 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 2301c481-a5f3-3086-bb01-e086e93c01ba | -10.65098 | -44.48605 | 2025-07-15 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec43a4da-e346-3b16-b811-e154d25946fc | -7.65385 | -44.42096 | 2025-07-15 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9d38844-9b9a-3b96-92a7-24bf62894a90 | -6.70705 | -47.79663 | 2025-07-15 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3d8efd3-9d64-394b-b125-2e4c6063c5f7 | -9.44047 | -40.31797 | 2025-07-15 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ffb7e5a6-9362-38c4-b616-711d7a03955f | -11.45213 | -45.09541 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 016627dc-2d62-36f5-bdab-8f2198679eef | -11.4459 | -45.12877 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4c1f9da4-13fd-3928-bfd7-48581316de72 | -9.97779 | -48.08088 | 2025-07-15 03:45:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6a4e805f-d1bb-378d-b10b-d29395b9cc18 | -13.12941 | -47.26536 | 2025-07-15 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2f2ed77-1adb-32b2-8f6c-4bc7659ed86c | -10.57413 | -49.14026 | 2025-07-15 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 34bac200-48e3-3e75-8d40-192d8316dcc7 | -11.44533 | -45.1318 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5c769a32-0e6e-3c5f-bbd1-1cba8e77fd86 | -13.65777 | -45.72732 | 2025-07-15 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60d6c2b6-44c7-3fcf-a7ea-8465c79ce634 | -10.96742 | -49.25409 | 2025-07-15 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b5a9890-fa14-3ced-986c-5bd2d30cdfaa | -9.98407 | -48.08207 | 2025-07-15 03:45:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0a2ebb8-b4ce-3592-9c0d-2bd32be605e0 | -9.7985 | -47.7383 | 2025-07-15 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e45688cc-687c-3439-8983-9f44590ce3f1 | -10.96086 | -49.25254 | 2025-07-15 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3db9b80-1c39-3db5-bd30-1137d5f35dbe | -11.46222 | -45.09746 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 6702cdab-7f17-3e9b-bc69-f261f3ddecd2 | -11.44083 | -45.12779 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2c945f9c-8c03-35f1-9e13-58c85c6cc950 | -7.09119 | -49.17229 | 2025-07-15 03:45:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1567a276-eb2a-3967-a729-fdadbaf8dc8e | -11.45268 | -45.09243 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 76375853-c9fa-3d68-b84c-1f985a7c6d8b | -10.56747 | -49.1392 | 2025-07-15 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 128bf676-236a-3ded-aa9f-3414ff02e7c5 | -9.43664 | -40.31733 | 2025-07-15 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dbeecabb-b84a-331c-90d2-48935d81d69c | -11.80917 | -44.26097 | 2025-07-15 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 780a22f9-63fd-344a-8a43-e84bcda3d8c6 | -11.44476 | -45.13485 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 91658431-cee7-3e9d-8274-5f03af7bd99d | -7.21172 | -45.32986 | 2025-07-15 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d557f92-d802-304e-b73f-cb3b8ec59c27 | -7.89399 | -44.49722 | 2025-07-15 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5171683e-f1e7-3eb9-94ee-abddfa824e3a | -7.88994 | -44.48998 | 2025-07-15 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d213cf1d-5943-38fc-8c3c-a805be2a9932 | -11.85497 | -46.7501 | 2025-07-15 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25590b5c-a679-3aaf-9700-a977180af0bf | -13.65655 | -45.73351 | 2025-07-15 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2da5d71-a4e1-3cee-81c7-115d47e74f76 | -9.79724 | -47.74044 | 2025-07-15 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 392cf910-b707-34c4-b610-e8bb02f499eb | -11.45606 | -45.10241 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2529f28d-0ab4-3c10-b138-070e6c681627 | -10.64286 | -45.22026 | 2025-07-15 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9660ee95-5725-32c3-ae84-5cd7eaddca48 | -11.46112 | -45.10341 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 622a7b76-8557-3cd5-b280-513db5818d1b | -11.46277 | -45.09452 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 753e4175-c11e-311f-884a-38993ef02f0f | -9.49597 | -40.38666 | 2025-07-15 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ed9d53a0-f4a2-3ce4-abc5-21b2124659a4 | -8.60204 | -47.43499 | 2025-07-15 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e07fb017-f384-31a9-8cde-53fb5fad38fc | -7.81531 | -46.56329 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bbcafbb-f4d4-3b0f-a6ba-6fcdfe828c5e | -10.64965 | -46.63125 | 2025-07-15 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 011c1a92-4edf-36f9-b4d9-5665802d12db | -10.70218 | -48.29739 | 2025-07-15 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b66c150-e607-37eb-b14e-73ebc84c3969 | -10.37639 | -47.14899 | 2025-07-15 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e2f8a57-15d3-31e5-b2fb-25d519dbba45 | -11.46956 | -48.52728 | 2025-07-15 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50311c11-f865-3fef-ba4e-c157578dca2f | -12.40332 | -45.37015 | 2025-07-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01b8fbb5-5d0b-3153-8cfd-e7ac2c444cf6 | -7.99087 | -43.38528 | 2025-07-15 03:45:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bd27a69d-d7af-34ac-9ac3-51d018d29826 | -11.8082 | -44.26621 | 2025-07-15 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0d64fa5-e6a3-3f06-9a56-dd1fb0d1dbcc | -13.03999 | -47.81078 | 2025-07-15 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 105a9c7e-52ce-3bc1-bddd-be15e0f5b2df | -12.40894 | -45.36816 | 2025-07-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65eb700e-65ad-34df-86b4-23800c298884 | -11.46675 | -47.31695 | 2025-07-15 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a40f44c1-72ed-3a5e-add7-cbc85a826c07 | -10.89564 | -49.21359 | 2025-07-15 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 92986cb1-c3da-3ed2-9468-3115abeba4c5 | -11.46757 | -47.31275 | 2025-07-15 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96b314b9-e4ef-321d-bd1e-256980d7f25b | -12.69665 | -47.87657 | 2025-07-15 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bda1edc-6688-30a2-bcc0-71b14e196280 | -9.44348 | -40.32338 | 2025-07-15 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 54fa0bc4-420c-37cc-ac01-8dbb3c9a289d | -13.04587 | -47.81178 | 2025-07-15 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fbb9072-e0d5-3f37-83d6-d4a9b7d50218 | -11.44707 | -45.09443 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| ed56be31-c228-3965-bfb1-8b2f1c4080a4 | -12.40217 | -45.37625 | 2025-07-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62175535-1f12-3c1a-aea7-c7a602287eaf | -10.56864 | -49.13335 | 2025-07-15 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 155ffffb-8d64-3cd4-a13e-662e7a91d5e6 | -12.69752 | -47.87214 | 2025-07-15 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bba6af0-e25b-347c-b556-b0a2222f7857 | -7.54121 | -43.92516 | 2025-07-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b60b5e5-39f6-3f1e-a118-7cce9e47d18b | -11.36241 | -48.73322 | 2025-07-15 03:45:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c5c812c-40e7-3532-9bb9-bc8a79d2aec5 | -11.45096 | -45.12978 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2f0d4cc-d87f-33b1-bdad-21a9f560e14c | -13.04402 | -47.81456 | 2025-07-15 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb0f5802-ede5-316d-9903-bafd5b969000 | -11.45323 | -45.08949 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 72aef90a-019d-334d-a8b9-9ae2921506f0 | -12.40837 | -45.3712 | 2025-07-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f75f8f9f-c6b4-3ebc-b102-86622b9d49ba | -11.90585 | -46.75714 | 2025-07-15 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92232dfa-fb1b-3fc8-a676-f89dc65c9a0b | -12.07508 | -43.48099 | 2025-07-15 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5e93cb6b-fb5f-3f33-a92e-2dd5aa510d0b | -9.80369 | -47.74457 | 2025-07-15 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 64b0df12-aeb4-39f2-a2ce-957a2f9dd5c1 | -12.40666 | -45.38036 | 2025-07-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 783f34f2-ba0a-3c8e-91fd-11a09672559c | -11.46647 | -48.52641 | 2025-07-15 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b22eb80d-c01d-3cfc-8764-8eb35cd5f628 | -11.45882 | -45.08763 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4f8e53e0-396d-330d-9d55-81a31e53570a | -12.07589 | -43.47651 | 2025-07-15 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 92980a79-807d-35bd-a6ee-d6e1a2184c6c | -7.89456 | -44.49404 | 2025-07-15 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a99e170-d5ba-3d21-b512-9a2e306abebd | -11.94365 | -45.76704 | 2025-07-15 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17632b03-4f89-3ae2-8627-ea201674d51a | -10.89678 | -49.20787 | 2025-07-15 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5106d4da-ce0f-358a-8c7a-35506e0ffd23 | -13.13159 | -47.26815 | 2025-07-15 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc4a9f16-3b05-3130-9198-d40a100427aa | -13.65817 | -45.73444 | 2025-07-15 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3abe89e4-79ea-399d-a85f-42e5c58b99e4 | -6.71257 | -47.80305 | 2025-07-15 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ea72909-441e-3c86-b07d-3ccf6a2df45f | -13.13214 | -47.26548 | 2025-07-15 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be990077-37b6-3d97-8295-6b9ff6e267cb | -13.65934 | -45.72823 | 2025-07-15 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e7bf970-d5ec-32de-9795-4ffa56010006 | -9.8024 | -47.74669 | 2025-07-15 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ccc2b50-931b-3f2f-9464-b45751c1f8cc | -10.64227 | -45.2234 | 2025-07-15 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7ac762a-84cc-3157-a61e-01176525df06 | -9.43965 | -40.32274 | 2025-07-15 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 91cc0b73-ccbd-300c-a1f4-7d9d69464daa | -12.40274 | -45.3732 | 2025-07-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48751fe1-3e5b-31b0-97db-d81b7eb46a1c | -7.30281 | -45.36057 | 2025-07-15 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c201d229-5e9b-3266-b569-a05b170909e8 | -13.04486 | -47.81049 | 2025-07-15 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68efa34f-fb46-3a5a-b768-a4f9fd48e62e | -10.56634 | -49.14485 | 2025-07-15 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| fab49b61-4a99-363c-b3ec-47027206581a | -7.89512 | -44.49087 | 2025-07-15 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 226a471b-b53a-356a-b4c0-22f1b1b13b58 | -11.44651 | -45.09745 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 274b23db-b335-3f6b-ab0c-59f641aff20a | -10.2785 | -47.61219 | 2025-07-15 03:45:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README8.md)
