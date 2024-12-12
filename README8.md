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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6a08c24-a448-3b08-803c-a5edb0fe16a4 | -6.9349 | -43.4934 | 2024-12-12 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 018c6ce8-b07f-3314-8af6-088d8d725936 | -18.035999 | -52.924999 | 2024-12-12 01:50:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bb11e3a1-b511-3eac-bcdf-639a11473bd3 | -18.049 | -52.970901 | 2024-12-12 01:50:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 71e0bb0c-9cae-3dac-a400-37d61d2c7a02 | -15.0845 | -59.6301 | 2024-12-12 01:50:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc7596de-c1af-3fdb-948f-f6c589a56b9a | -18.055201 | -52.918999 | 2024-12-12 01:50:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5b7db321-f6a6-3e4c-a9c1-9570d5bbff78 | -18.061701 | -52.942001 | 2024-12-12 01:50:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 385a119f-9e5a-39d1-aa62-3d18d016df55 | -18.052099 | -52.945 | 2024-12-12 01:50:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b2e45941-dcf3-3bf6-951c-1e62c2d10be6 | -18.0425 | -52.948002 | 2024-12-12 01:50:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 66ca0c67-bdc1-3d28-b264-fc377e7635ec | -18.0329 | -52.950901 | 2024-12-12 01:50:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f94ca55-305b-39de-9571-831bb29d8420 | -18.045601 | -52.922001 | 2024-12-12 01:50:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8a6eac54-bb62-3711-844d-86325c054eaf | -12.1215 | -64.155701 | 2024-12-12 01:50:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc757a2d-db75-396f-95aa-d9e853ef8361 | -13.694 | -54.748402 | 2024-12-12 01:50:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 808d6107-a1fe-37fa-8815-389aba80b8a4 | -18.023399 | -52.953899 | 2024-12-12 01:50:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6db4b8a1-8721-3876-8565-5597b4b27cb9 | -15.0821 | -59.620399 | 2024-12-12 01:50:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f6029cf-2e1c-35e7-b2a4-6b0d54ebcedb | -18.0299 | -52.976799 | 2024-12-12 01:50:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b340353-1fab-3a40-babe-75a876a9e0ec | -12.1231 | -64.162697 | 2024-12-12 01:50:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e58364ec-ad84-337d-9607-ff7904e5dcc4 | -15.0869 | -59.639801 | 2024-12-12 01:50:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5071ee76-c5f3-3845-8f29-d1449739afc7 | -18.0585 | -52.967899 | 2024-12-12 01:50:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd6d4a52-f438-33c6-9006-969ea62c8c3f | -18.0663 | -52.955 | 2024-12-12 02:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 81f57154-142f-31bb-b4b4-8bc8d3a1ca8f | -18.046 | -52.9798 | 2024-12-12 02:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 9ff13d2c-ab94-3e1a-9d63-6248b381902d | -5.9183 | -48.0667 | 2024-12-12 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e58ae6bd-0886-36e9-8982-8cf89cff64ad | -6.9344 | -43.5401 | 2024-12-12 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 90e6f1b3-5ad6-37d0-b71e-e67b19016df1 | -14.7457 | -52.6683 | 2024-12-12 02:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 08d25785-7db1-3cd9-87e8-9f9bf7e60f28 | -10.1195 | -36.4686 | 2024-12-12 02:00:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 5011de99-61a9-3fe8-8cb3-179a5d57b27c | -6.9346 | -43.5168 | 2024-12-12 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 580.0 |
| 28105255-d9f7-37f1-9116-d84771c7a5b2 | -18.0659 | -52.9766 | 2024-12-12 02:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 9a3ce91a-c686-326c-a47b-3811879cad22 | -6.9161 | -43.4952 | 2024-12-12 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 21d184d8-5984-3e3a-8625-0ec2dedce8c3 | -5.9369 | -48.0654 | 2024-12-12 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| e3e7babf-a36a-357a-9a9c-bcfe67229771 | -18.0668 | -52.9335 | 2024-12-12 02:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| fad7495c-5306-32a7-9774-d503d6bd0d06 | -6.9158 | -43.5185 | 2024-12-12 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 311.5 |
| 6167b56f-ed8f-3d99-b50f-af4a8ce4d20b | -1.8788 | -54.6908 | 2024-12-12 02:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 2485e7dc-1789-3b9f-b5ca-824ed0576656 | -3.2316 | -46.8936 | 2024-12-12 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8534e941-8959-3ce1-aea7-dece75455b5f | -14.7655 | -52.6446 | 2024-12-12 02:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 351223e0-0349-3ca9-9d03-74164d804324 | -3.2502 | -46.8929 | 2024-12-12 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 96796705-b762-37cb-b10a-6696449cab60 | -5.9185 | -48.0449 | 2024-12-12 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 46a43bf8-0b78-3e35-99d2-2f50bf47b2b0 | -11.2148 | -53.833 | 2024-12-12 02:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| cda0cead-ce96-3bff-9396-26aa22729279 | -11.2151 | -53.8125 | 2024-12-12 02:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ea0d0f74-d384-39ed-a869-2d697ea5b2ba | -3.2503 | -46.8709 | 2024-12-12 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| bfc5e28f-f4e0-3dcf-a838-a345e4fc09b0 | -14.7461 | -52.6471 | 2024-12-12 02:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 012c9ace-6703-3850-89e3-af209f71050d | -18.0464 | -52.9582 | 2024-12-12 02:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 90295140-cc3a-3b8b-a4d7-62206a53b9e0 | -5.9371 | -48.0437 | 2024-12-12 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 4ff5af7e-4254-3bc8-95d8-d1221ce01636 | -14.7651 | -52.6658 | 2024-12-12 02:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 633850aa-4aa5-3afc-af79-c1ea27cd2a85 | -18.0469 | -52.9366 | 2024-12-12 02:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 3d6d116f-d198-3711-a687-e8c1ba1f59fb | -6.9156 | -43.5418 | 2024-12-12 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 86759fab-ee42-3548-a7d9-2a86ba6ff319 | -6.9349 | -43.4934 | 2024-12-12 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 7440e00d-0c5d-3956-90fa-b2a445e784d3 | -11.1959 | -53.8348 | 2024-12-12 02:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| dd7e3ae5-cd67-3c6d-9b88-4eed91471885 | -3.2317 | -46.8716 | 2024-12-12 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7eeb172d-221b-30ff-9767-51a9e1e2f58b | -18.05 | -52.97 | 2024-12-12 02:00:00 | MSG-03 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 63931cf4-ae53-38cb-a0e8-4c2a1ed50c9c | -6.92 | -43.52 | 2024-12-12 02:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7586e8b0-903b-31c2-be12-2681884a9789 | -6.9 | -43.51 | 2024-12-12 02:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7015e166-c8be-3e6f-a62d-d32206355367 | -18.02 | -52.95 | 2024-12-12 02:00:00 | MSG-03 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8deb6209-b91e-36b6-a6a9-6f29e72a5fc4 | -18.02 | -53.01 | 2024-12-12 02:00:00 | MSG-03 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| da5d63bc-2d9e-3cf6-8893-d45f2851163e | -6.92 | -43.47 | 2024-12-12 02:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 825500de-7889-3aa6-9d86-36f3c56e42bc | -6.9346 | -43.5168 | 2024-12-12 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 480.5 |
| dddeb96d-4664-3076-8bb6-afa3e75d49e2 | -6.9344 | -43.5401 | 2024-12-12 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 168.5 |
| b7bdfa02-c21b-3be7-9914-1ec6e06a980f | -6.9349 | -43.4934 | 2024-12-12 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 1a43f4dd-7ceb-336f-8fe7-ce639282ac43 | -5.9369 | -48.0654 | 2024-12-12 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| fe9df8f9-13f3-33f2-a60d-d182e9070ce1 | -3.2316 | -46.8936 | 2024-12-12 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 0421b043-a933-385c-a0a9-f509eec3da6e | -5.9185 | -48.0449 | 2024-12-12 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 21d63043-e4f2-3f63-91e3-c59db8ddbadc | -3.2502 | -46.8929 | 2024-12-12 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| c131e490-6eda-319e-b87a-3ec81fbf6dfb | -3.2317 | -46.8716 | 2024-12-12 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| fcd15f3a-e76f-3888-8a7f-ea6326bd37ea | -18.0464 | -52.9582 | 2024-12-12 02:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| c047a6aa-8fe9-30c8-8eb8-9e196ebf19ae | -11.1959 | -53.8348 | 2024-12-12 02:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c2f74165-a660-3da6-a456-f12cd3ec7e8e | -18.046 | -52.9798 | 2024-12-12 02:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| cc9e2b4b-f845-3afb-a239-6efe902b4ecb | -6.9158 | -43.5185 | 2024-12-12 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 270.9 |
| 3f31b7dc-ea1e-38d7-94d8-7fe11ea5ab06 | -11.2148 | -53.833 | 2024-12-12 02:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| cebf96a4-9fd9-3379-8ffb-69866387016e | -18.0659 | -52.9766 | 2024-12-12 02:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| b9ccd124-c325-32bc-9864-b2fa2bcedbe5 | -11.2151 | -53.8125 | 2024-12-12 02:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 25a56a3c-4b87-3f40-9526-1b74db3adabd | -5.9371 | -48.0437 | 2024-12-12 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 60014284-9e77-3d96-8607-badbfba3f06b | -18.0663 | -52.955 | 2024-12-12 02:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| beb31a2e-d5ef-31b9-b878-858162522ac3 | -6.9156 | -43.5418 | 2024-12-12 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 01b1c160-93d6-33b1-8571-bca45c7ee6d4 | -10.1195 | -36.4686 | 2024-12-12 02:10:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 123.1 |
| a95ac5cd-0196-3cde-84a8-47abca91721d | -10.1201 | -36.4417 | 2024-12-12 02:10:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 4a3c1600-3b86-3f44-81b6-63f0476c7e84 | -14.7461 | -52.6471 | 2024-12-12 02:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 917f58ea-b02c-3912-9445-a24650fbdb5c | -14.7655 | -52.6446 | 2024-12-12 02:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c0cd16de-cff1-3913-8fca-c4750bd8b993 | -5.9183 | -48.0667 | 2024-12-12 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 83fddd60-ec7d-3bc2-8aee-8c0bdd851784 | -18.0668 | -52.9335 | 2024-12-12 02:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| bcf5bab5-ca7e-3d29-b67e-bc806cea675b | -6.9161 | -43.4952 | 2024-12-12 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 876afbb1-6971-3b8c-9aee-049441cdfa27 | -3.2503 | -46.8709 | 2024-12-12 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| e50c154c-078f-345b-adea-a937a30d5f62 | -18.046 | -52.9798 | 2024-12-12 02:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 251.0 |
| 7d2a9124-895c-3c1d-ba05-d2ae336bb7a8 | -3.2502 | -46.8929 | 2024-12-12 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 86e4878d-4ae1-3277-a4c9-2b719b402591 | -6.9156 | -43.5418 | 2024-12-12 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 0eecdff6-36a1-3142-950a-67a7241e3eb7 | -6.9161 | -43.4952 | 2024-12-12 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 5a6820c2-ecf1-3523-aaa1-f13bb05dd00c | -14.7457 | -52.6683 | 2024-12-12 02:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 060ed317-de1e-3642-98f4-233f9b5337ac | -11.2148 | -53.833 | 2024-12-12 02:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 40e87056-0333-315f-b9f3-6d46938af68c | -6.9344 | -43.5401 | 2024-12-12 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 166.9 |
| e981ee8e-f87e-366d-9aa8-c42f69fabe5e | -3.2503 | -46.8709 | 2024-12-12 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 28c01f4c-0247-35d3-88fa-db41eda8c0af | -18.0659 | -52.9766 | 2024-12-12 02:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 26e7fe3e-57a0-3715-b2e5-56960563ace2 | -3.2317 | -46.8716 | 2024-12-12 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d5faeb2e-c285-3ded-97a6-5f058ad81552 | -18.0456 | -53.0013 | 2024-12-12 02:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7ba3617b-919e-3b04-9e4e-7c455c580e4f | -6.9349 | -43.4934 | 2024-12-12 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 420e8062-19ab-3880-add8-214504602713 | -11.1959 | -53.8348 | 2024-12-12 02:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| bde41190-0a2b-3bd9-9ab1-4ceb9a5521e5 | -18.0663 | -52.955 | 2024-12-12 02:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| aec72247-e89b-36e4-8df3-550aab4f9a02 | -2.9666 | -53.1201 | 2024-12-12 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c73f3385-e61a-30e1-b922-6f6e9adb40dd | -6.9158 | -43.5185 | 2024-12-12 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 314.0 |
| bdc5cd45-bc2a-35c0-b6ef-37952d1181dc | -14.7461 | -52.6471 | 2024-12-12 02:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 9f6798a4-775f-3f3d-9e42-934e4b4d55d4 | -18.0464 | -52.9582 | 2024-12-12 02:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 17b1df42-998f-3322-85cb-eb4e1c6a606e | -11.2151 | -53.8125 | 2024-12-12 02:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 5b055a4d-40f6-3223-a40b-56ecd30f0a5e | -6.9346 | -43.5168 | 2024-12-12 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 547.6 |
| e88c3902-c692-345d-bd5d-34975ad37dba | -18.0261 | -52.9829 | 2024-12-12 02:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |


[Clique aqui para ver as próximas entradas](README9.md)
