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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 090a3c7c-e1ab-3d77-8c4d-a18c218be062 | -4.26536 | -48.19109 | 2026-08-08 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| c67bfcf2-c4ec-364e-a61b-d94ebcd42744 | -9.38339 | -47.09195 | 2026-08-08 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7dff96ba-c05c-3e98-8680-033004118cc6 | -6.60658 | -56.35596 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 622b756b-92f4-31c8-84f8-a687210fdf9c | -6.65354 | -56.40636 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f597bf5b-7888-3ab6-9bcf-b2f890144b0e | -4.45778 | -47.92091 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 65012356-5696-3776-aced-18ce753fcc6d | -7.31542 | -48.09504 | 2026-08-08 04:44:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00c65e1d-8789-3a4d-ac5a-618461a515ee | -4.36868 | -55.77357 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d737c9b-0113-376c-a415-d10c9e32a891 | -3.75813 | -49.10317 | 2026-08-08 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50f20f88-c548-3e49-beb2-f51c9559ed80 | -2.48687 | -47.08207 | 2026-08-08 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d8b9a055-c772-3162-92d3-f1b3ea70a8ac | -7.77453 | -49.48423 | 2026-08-08 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 557948e7-5dc9-3784-8f41-d0984f9442f4 | -8.623 | -50.02883 | 2026-08-08 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f270946c-44c7-36fa-a3cb-929c47ded92b | -2.76216 | -49.46846 | 2026-08-08 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71696db0-b8f3-38d8-bfaf-22d3050434c8 | -3.02526 | -54.52843 | 2026-08-08 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2a0e98c-8ff5-3eee-9472-efe113f33524 | -4.65413 | -42.43673 | 2026-08-08 04:44:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| de925b32-ef77-3239-91d8-ce966e90148c | -2.7522 | -49.4669 | 2026-08-08 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7938920c-3c01-3b03-b85a-47f10356f23b | -5.6035 | -44.27053 | 2026-08-08 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a113687-bf58-3f36-816a-7bad1890028f | -4.45984 | -47.92109 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa1071ce-b6ad-3d2d-a80e-2f2da66f5c20 | -6.65111 | -56.40419 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cf4f31c-a453-3032-b131-4de1334c9197 | -6.5467 | -55.1775 | 2026-08-08 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bab870ce-1619-36b4-920e-980a5a39c4cd | -2.48969 | -47.08622 | 2026-08-08 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 525b63b4-9f33-3214-9665-e3fbdce8190b | -2.78711 | -49.5257 | 2026-08-08 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23f31d60-93f8-3a0c-b728-ebbfd93da5fc | -3.96384 | -48.12233 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1dfedb1b-08de-3a84-9023-d152c969a11c | -6.88765 | -59.89314 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2b9e222-30d5-38eb-b3c5-221a94e1ddf4 | -1.58803 | -50.4374 | 2026-08-08 04:44:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 051bc24d-34db-32b3-95a1-91e38442d598 | -2.79043 | -49.52623 | 2026-08-08 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91d1ba23-d0e6-3d78-a548-74f40e1936b0 | -3.99958 | -56.23902 | 2026-08-08 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 898c60c8-acef-31fd-b30b-382ec254028b | -5.87741 | -57.6512 | 2026-08-08 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb03aef8-eed4-3b4b-bbfc-bb70d9500b86 | -4.90601 | -43.46957 | 2026-08-08 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a3dd6b6-0dfb-3f2a-b7bb-63840af56e30 | -1.58685 | -50.44478 | 2026-08-08 04:44:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33017984-161e-362a-829e-bb3393066c06 | -2.82716 | -46.72279 | 2026-08-08 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d855dbe-6df2-3e79-bada-ed1eb12108ce | -6.91291 | -41.95952 | 2026-08-08 04:44:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9151444b-0e99-39a8-8f19-5f0015d19d7b | -3.9533 | -48.12424 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e50d87ce-d4e2-3c51-b686-6d2596846acb | -2.50551 | -51.81198 | 2026-08-08 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 36710c85-2536-3f5f-b250-aec3571c8c00 | -2.69535 | -47.35758 | 2026-08-08 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17978106-9b34-3e20-aba4-3a99a2a76a16 | -9.38039 | -47.0872 | 2026-08-08 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e8359bb-41e7-34ee-91a8-86f90b6c67e3 | -2.76602 | -49.46552 | 2026-08-08 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aeaf8653-6397-3863-ab5d-d8a21548d7d3 | -4.59992 | -45.58685 | 2026-08-08 04:44:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e63f74f-bc1d-345c-9655-e308434f6600 | -8.28121 | -50.40485 | 2026-08-08 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d8d4a8fc-ca1e-3908-887c-241efa19c535 | -6.98329 | -42.91151 | 2026-08-08 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4190670d-d436-39b1-9041-c8cf5b11f898 | -2.69478 | -47.36117 | 2026-08-08 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fb27138-f4f6-357a-be80-fd5a82c0b408 | -6.88625 | -59.90103 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93af9376-db29-3f1d-bcbb-1dd072b43c90 | -3.81907 | -50.63433 | 2026-08-08 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac4a606b-52ec-3cd7-a0c7-d9ef25bb5b2f | -2.41862 | -48.63468 | 2026-08-08 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| def3cd7d-3f0b-3204-86ba-2f00b4f2291f | -6.98785 | -42.91212 | 2026-08-08 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e2cdf7bd-d01e-39a2-ba84-16a956feab65 | -6.30465 | -52.81213 | 2026-08-08 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53f019eb-ae0e-382c-b3ab-efd54bdaa646 | -11.15706 | -54.85213 | 2026-08-08 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 354a5c49-97d1-3c47-99ec-40f140a57b4d | -14.92489 | -48.24892 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1cb90ad-a63f-36a9-a239-061ac3df7cb5 | -14.16394 | -54.0073 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7e199c39-a9a8-319a-8899-84cdb0fbd3b1 | -13.77949 | -48.50075 | 2026-08-08 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c5e4f6d-324b-3ef6-8dc0-8d9460f53501 | -15.93788 | -48.31204 | 2026-08-08 04:46:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abcb633b-226a-3240-b5e7-f1074900da94 | -14.93425 | -48.26638 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 40ee49dc-fdde-3d70-b746-cd007faa9ba8 | -7.54899 | -61.16606 | 2026-08-08 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f783face-03f0-3407-9a95-4b52838cb776 | -15.16473 | -52.74289 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 22853c63-ff49-34b2-9f45-f6c19c73ecb1 | -14.41858 | -45.66266 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2dca0465-4295-383e-85c4-7fd6f24290c7 | -14.93215 | -48.24998 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ce72a06-48d4-3866-bac7-56eaca0a6d7d | -10.78326 | -47.70928 | 2026-08-08 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06506e17-3fd2-3dc6-8caa-c7fd7663f2fa | -10.50167 | -46.62843 | 2026-08-08 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0aa760e7-ada9-33e2-8af0-a0c183d0892c | -12.33268 | -53.16206 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7958fcc-3def-3c72-8602-44937465ba1d | -10.26137 | -45.81073 | 2026-08-08 04:46:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69fb9fda-9d53-35d3-92a5-c1295493b88a | -17.30574 | -42.67535 | 2026-08-08 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a52d055-3d2a-36b4-91c9-751bd1ed8376 | -14.93849 | -48.26261 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52fba511-882b-3aa5-9e04-19ca5cddcae6 | -12.54613 | -46.94004 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10d58e88-27b3-391b-9b47-12893c53678a | -11.2409 | -54.01981 | 2026-08-08 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33370dc3-915e-3a46-84d2-76d83a9993b0 | -20.27087 | -41.78014 | 2026-08-08 04:46:00 | NOAA-20 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0f3c77e3-eba1-3c2d-a1c6-441f7fa7a985 | -10.24255 | -45.80185 | 2026-08-08 04:46:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1404e2a8-ded1-3363-9b4a-2f2005440d94 | -16.7191 | -46.40195 | 2026-08-08 04:46:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7035d54d-f6e9-3d37-b508-164ea4000067 | -21.36724 | -45.1375 | 2026-08-08 04:46:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4995156d-b73c-3650-8a7f-32930d234324 | -15.09834 | -52.73522 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16fc1046-7ec7-3502-a575-3ac0a471de24 | -9.68251 | -56.49184 | 2026-08-08 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44e7b2f5-514d-3f5f-b4de-a5758a2ee42c | -15.11074 | -52.72236 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3721dc61-b866-3d48-ba54-2579681b9d4e | -14.42334 | -45.65925 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bca1955b-7e97-33ea-88b4-7d50215d8700 | -12.54034 | -46.95366 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f03ab4f4-5cd1-31ee-a465-b23ea5dcb7ce | -20.39243 | -49.3126 | 2026-08-08 04:46:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 95d19a9e-8f92-3185-b80e-f78e09c15a24 | -14.41912 | -45.65867 | 2026-08-08 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9281662-2403-3ec7-bddf-37ce856ac59c | -15.85523 | -48.07822 | 2026-08-08 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c488cb1-dffa-3569-ade8-6a082f2d9c44 | -12.33806 | -53.15113 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68f7c488-fa6b-396f-899b-ce293443bf94 | -12.32923 | -53.16146 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba6f6f96-3fc5-3c6a-be60-b9a30d8b5cc3 | -14.37443 | -54.96607 | 2026-08-08 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| db78827b-c7c2-3741-96ee-66a5b48d7598 | -15.15625 | -52.75272 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a6434fc-05c3-3980-81e0-f3144d9e2449 | -11.61605 | -54.5736 | 2026-08-08 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 215714ac-117f-3e93-b0b8-40f7730971d5 | -15.67871 | -56.15939 | 2026-08-08 04:46:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58e3d8ea-7a49-3956-9b69-f93c192648b9 | -12.33741 | -53.15497 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84ece362-87af-3bc3-ba37-9abe7ed34ddb | -9.14546 | -49.66554 | 2026-08-08 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bddcac22-b10d-3b37-ba9a-d4d57c5ee769 | -15.16199 | -52.73863 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c480340-e9a4-331f-8d94-ffb2bf075be3 | -11.03986 | -44.27259 | 2026-08-08 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f8b16e22-d5a7-3fa3-b6e9-f1ffb5a890cd | -15.15685 | -52.74903 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6f7c52b-8dc6-319a-8c7a-2ffea2b959d2 | -11.77936 | -46.38874 | 2026-08-08 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 30b5890d-e7b7-3648-91ed-cd0e1ba3cd63 | -15.38025 | -53.79452 | 2026-08-08 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c2469622-ed4b-300c-9d10-a5874e0acdbc | -14.92426 | -48.25323 | 2026-08-08 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c8ba6e0-1773-34b3-9502-9c63a17be965 | -12.35053 | -48.20047 | 2026-08-08 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f60a305-c03a-32f8-a2be-10893415960b | -7.54994 | -61.16491 | 2026-08-08 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1188decf-25de-35db-aafe-d3943b4b2641 | -11.27347 | -55.8624 | 2026-08-08 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 22dbd55a-391b-3721-a9ee-e4daf844e3ea | -19.91422 | -45.4356 | 2026-08-08 04:46:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4424417-4bef-3853-9bc7-595572d78982 | -14.15762 | -54.00208 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f3c1f49f-52d3-3ea7-940d-708aefde925a | -12.54302 | -46.93459 | 2026-08-08 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 58181d3e-a1ac-370b-92f2-00a7afe6f238 | -13.83384 | -53.68027 | 2026-08-08 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88b2c747-0409-3e0e-8764-de056a660ea8 | -10.6146 | -46.54362 | 2026-08-08 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c2a9452-4d42-373d-b0bf-0898eb83209e | -14.20281 | -53.31927 | 2026-08-08 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f940ce98-3f5b-3f14-a363-536e30a08503 | -12.33397 | -53.15438 | 2026-08-08 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04ef75b1-1a05-3eee-b675-672a504c47bb | -15.14526 | -52.73586 | 2026-08-08 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
