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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bcfd206-d688-3a1a-8160-b15071ba09a2 | -2.92914 | -48.30012 | 2025-10-15 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c30c395d-17ff-371e-bb3d-0d64cf301c93 | -4.77551 | -45.73118 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17c89ad4-c1f3-3a11-9e09-d52fac680239 | -4.15123 | -43.13124 | 2025-10-15 04:55:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b425cdd3-a06a-3d66-96cb-7a3e9706cbe3 | -4.28457 | -48.57224 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd01bb09-7592-3971-85f0-a3ec880e9253 | 1.86111 | -55.6988 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 06ee1b13-b4f2-39bb-b561-6a1d8402a42f | -4.12553 | -50.71967 | 2025-10-15 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d66244d-95d0-3994-85f1-0f705e34eec2 | -3.22373 | -48.93008 | 2025-10-15 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1456ac7-6fbe-31aa-93ad-88f9b1e38413 | -4.77357 | -45.7364 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 337c7d9a-81ba-3cef-a086-624cf1c2d223 | -4.23399 | -44.43247 | 2025-10-15 04:55:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8dbdb1a-df35-36d1-9c78-96d90cbecc65 | -4.64879 | -47.95262 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 185f83f3-9e3e-3db9-ba6a-465bb47691e6 | -3.56518 | -51.11429 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| fc2c6bb2-852e-3ff4-bfb2-a682e6f3944a | 1.30691 | -50.72206 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dee20b1e-ceb3-366e-ba99-dee92c44aa62 | -2.81863 | -49.20787 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cafc7651-098a-3ccc-99ab-7f83ab9dcb03 | -3.07887 | -49.50937 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 552b6b44-de2a-31bc-86fc-b32eed5e1cc2 | 1.85918 | -55.73388 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4c0dd53-99c2-3a3d-becf-b4ab3b90df4c | -4.2578 | -45.58308 | 2025-10-15 04:55:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1b1031d-9c1f-3606-810d-e1d81d2a4c08 | -3.56968 | -49.44423 | 2025-10-15 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ecbe8b23-70e7-314b-80e6-731157c1d84c | 1.43824 | -50.84198 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe3380a3-3e31-3e7a-a02a-42b4cfae7b7f | -5.42659 | -40.985 | 2025-10-15 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 68bd6ba2-0a7f-3bdf-b27b-d11acdd61606 | -3.22335 | -48.92744 | 2025-10-15 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06059902-f48a-31a2-a0f5-9aaa08763055 | -4.28755 | -48.58007 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b070d01d-8186-3276-bd2a-22d5c2bc6f33 | -2.80017 | -48.9416 | 2025-10-15 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7d509220-0dde-33c4-8e15-181596cf1909 | -3.02204 | -50.44631 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7b3321a-96e9-34da-b1b0-00bb28dd1fe6 | -4.27668 | -44.36528 | 2025-10-15 04:55:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c581f41e-f7be-33da-8171-bb3e76fda1f5 | -5.00911 | -44.492 | 2025-10-15 04:55:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b430fbdf-5022-3c4f-89ba-3a222b6a359b | -3.09703 | -50.38688 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b4a0ecf-ebd4-3cd6-a7b9-ad0fc8566813 | -1.53355 | -48.70786 | 2025-10-15 04:55:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0a98bcc-39cf-3eaf-9055-30821e49d675 | 1.30972 | -50.7179 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cff09deb-cd1b-375a-a3fa-33eb3e7f0b72 | -4.9007 | -43.4548 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9ddf92ca-1ef2-316e-bf63-47140f704913 | 1.33118 | -50.722 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d2799bc-f4aa-3fcb-b9e1-96b7ef4a4946 | -1.89361 | -51.01083 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0739203-eeeb-3bb1-a61e-1ad81dc6faf2 | -3.29957 | -50.17258 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27c6e10a-3774-3ae8-933f-ac21fcd51c57 | -4.90426 | -43.47173 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| aa144f53-0196-3dda-bafd-a4c931d52ce2 | -5.40592 | -42.65375 | 2025-10-15 04:55:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9a2be16f-e24e-30ac-9432-3b9af91b2005 | -4.90015 | -43.45881 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 912.8 |
| fd26888a-b5a6-3a3e-9af2-6fc941293f3d | -2.26253 | -49.5274 | 2025-10-15 04:55:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf206a60-c22e-37ff-9ddc-b7f5e352305c | -2.53204 | -47.80714 | 2025-10-15 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5befbdd5-501e-3f76-9ac7-06986fefff5d | -4.02106 | -48.96806 | 2025-10-15 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a8b45e7-3b30-387a-8444-36f508aab9bc | 1.00771 | -51.08471 | 2025-10-15 04:55:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a39cd92a-5435-36c1-b1e3-3b95076fb007 | -3.46021 | -51.0902 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb674bca-c0b7-3afb-b8a2-4d339f55b780 | -3.56171 | -51.11375 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 4bee1a8a-3537-3f32-8a2a-acc9f3c65fb1 | -1.75656 | -54.51705 | 2025-10-15 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 926e8eb4-cbaa-34db-85ed-70742b31f324 | -3.14026 | -50.21407 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 482329de-bda4-3dce-80fe-a712133b8da0 | -4.72054 | -44.82034 | 2025-10-15 04:55:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f823b20f-e3d3-3237-8eb4-2f72ff6cf0b2 | -3.67554 | -45.22084 | 2025-10-15 04:55:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28d3a8be-0123-3808-8770-ff117cebce09 | -4.91116 | -43.46463 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3181f8be-9231-3b38-bb62-de34961e0ec8 | -3.07511 | -49.5088 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9372e9d4-19f9-3b30-bada-5209526c9edb | -2.87704 | -50.73103 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09e91524-18e1-3f45-b915-13847cdbc983 | 1.33742 | -50.7396 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63c1debc-dfa5-36f4-a408-03a9971fa17e | 1.85984 | -55.73813 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecdcbf9e-eed0-367e-9bb9-4c501ad83f7e | -3.73312 | -48.35867 | 2025-10-15 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec579c17-15c2-36f3-a1ff-a975e2c7c488 | -4.11483 | -48.02442 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 784465c5-531f-3ae1-bb6b-7e6ca9f41703 | 1.85717 | -55.72112 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 69a88170-2edd-3742-b9d0-be1555076231 | 1.85619 | -55.73867 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ec2f10b-be0c-3eea-a99e-1156697f0eae | -3.43319 | -50.25222 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3937643-9aad-31c2-8da4-647e6373b945 | 1.87929 | -55.6664 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcd0ef6e-ac8d-3963-95eb-4a9191e275cb | -4.76972 | -45.73637 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 510e1e2a-6321-3763-9c86-6355712e6599 | -2.71896 | -48.33782 | 2025-10-15 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fdd139b-2dec-33a6-9ccf-82636e552391 | -3.42298 | -50.24635 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13e1e48a-dc6c-3f8f-97fb-6f86eb765cc9 | -4.66356 | -43.1174 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4ce51d92-a836-378b-a521-0834f7803ea5 | 1.81143 | -55.76292 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b71f2a4-033a-3688-8acc-b96068e969be | -3.99802 | -48.34153 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da9d928f-85cb-3161-8c56-6ad54c226259 | 1.85948 | -55.71209 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58ca9779-7adb-3e35-b888-666dd2e8bc5e | -3.72857 | -44.13866 | 2025-10-15 04:55:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32521928-f96f-3806-8561-1035f29c6bb6 | -2.96364 | -48.60147 | 2025-10-15 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3934450f-9b4c-3f65-8260-ec06f4250c23 | -3.12835 | -50.20967 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00c188ec-6e8c-3f70-8aed-0c9e675eea7d | -3.16729 | -48.60744 | 2025-10-15 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7bd9aa8-0ac1-3378-a96b-3f8cd697f0b6 | -2.94925 | -49.34216 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef8f4c5c-7eab-36dc-8959-46afd564892e | -3.06707 | -49.40944 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3e50d89-dbe0-3a08-a9e2-9637d9544cdd | -3.9378 | -48.90744 | 2025-10-15 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 587e7645-3759-3b9e-8754-cff443e1ba89 | -2.92456 | -48.30305 | 2025-10-15 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 65948776-5fa9-3f51-bf0e-dfaa3746946b | -4.11344 | -48.02558 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fef3e981-9943-3ea4-be86-7666b43c9651 | -2.9251 | -48.29948 | 2025-10-15 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 400ca6a3-6c54-35af-ac13-afbe5743109d | 1.87695 | -55.67542 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7011b15e-136c-32ec-80a2-18888b8d0da8 | -2.26084 | -47.84401 | 2025-10-15 04:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7771eb54-cc57-3be3-b767-3435f942414f | -2.44654 | -48.99902 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 748eaf4d-29f1-398f-9d2e-9e6ef89d6bd5 | -4.88792 | -43.45948 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b78ac200-ca4e-3553-91a1-23bc92222140 | -3.46493 | -48.9804 | 2025-10-15 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22ca87d0-6da4-3f60-bcb9-a17741ca1f85 | -3.56111 | -51.11769 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f82f8f51-b3d5-37dc-9bac-13f6e3cafa04 | -4.91059 | -43.46866 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 776816b7-defa-3c31-862b-22d054ced0c1 | -4.49792 | -44.72486 | 2025-10-15 04:55:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2f8c59a-eaad-35a2-ae63-5f30de7f8f51 | 1.3306 | -50.71837 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c21f7100-57ba-3b72-b77e-9c39c813ad5c | -4.7823 | -46.61368 | 2025-10-15 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b577c79e-a55a-3534-821a-d5fab6e73b0b | -2.62844 | -48.05627 | 2025-10-15 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb423380-37dc-3e22-b737-5a81830a825f | 1.29806 | -51.24654 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9e69762-4015-3352-ba81-f10c1f541564 | -3.59472 | -49.43097 | 2025-10-15 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43ebd39d-088d-3ca8-80f1-8323dd94caa2 | -4.89312 | -43.46436 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fdf2eadd-9a23-3a6a-b27b-0a62c9a01f2e | -2.86284 | -49.16923 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30cacb70-454c-3a03-8134-131664d5fd7c | 1.85963 | -55.70847 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 46a17347-1ac6-3897-9f0f-42c0a773eee9 | -3.57365 | -49.44204 | 2025-10-15 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| baf4d61c-e2a1-35b5-a13f-5e4a407da0a9 | -4.25345 | -45.58524 | 2025-10-15 04:55:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caaf3169-f35e-3e8f-a383-98ef2abfd89a | -4.59591 | -47.02916 | 2025-10-15 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5987aca0-8181-34b0-b713-7fa1d874fbcc | 1.8763 | -55.6712 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e433ede-b2e8-3e0d-9c56-f39f9adaac8e | -3.56866 | -51.1148 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ee099c6b-ddbe-3651-8858-aa7a676a7937 | -0.9013 | -47.54736 | 2025-10-15 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0be507be-1996-32dd-bfa3-e9f01723daa6 | 1.85835 | -55.69996 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c1a71e27-be30-3ea2-b220-8e7f8dbd692a | 1.75816 | -55.78271 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0e8fa3ab-8472-3f00-b69e-22be5f809285 | 0.12568 | -51.38869 | 2025-10-15 04:55:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f24e196-f929-3099-8f9a-a96641e77267 | -5.0145 | -44.49295 | 2025-10-15 04:55:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca14dc44-f07f-3810-a790-714a5380feb6 | -4.91229 | -43.45651 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README41.md)
