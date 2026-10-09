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
| a3f982cc-cb39-34a1-bc72-688578048ecd | -7.64001 | -35.01562 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 2ad98b6a-00d0-39d3-88cc-9a6a28e3954a | -6.00566 | -40.9586 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 54.5 |
| adb1012a-f865-3e36-9e24-0d23b887c062 | -6.16182 | -35.2951 | 2026-10-09 03:21:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c37ccc2c-a7d5-3c97-a3fe-78c64cfce05e | -6.83048 | -39.39346 | 2026-10-09 03:21:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7683204a-d702-3a72-a43f-2c160054d522 | -7.6405 | -35.0064 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| d54e30dc-139d-3f2b-bddb-1f4a4c65012a | -7.64343 | -35.01756 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dd9cebbb-7f30-3c3f-9960-6390bc8a711d | -7.40402 | -35.19263 | 2026-10-09 03:21:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 4c40d8de-0246-31f0-905b-bcc0a20709ef | -7.64479 | -35.01657 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| ca43fec2-62e5-35d3-b136-a4a79c5ae65a | -6.00295 | -40.97274 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| a46c20b1-95e9-36c1-8491-cb33c7d34eb9 | -5.99001 | -40.96299 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 5ea9eb6e-eea6-382c-908a-85974127f748 | -6.0002 | -40.98704 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 2fe78832-1676-3c88-aaa5-365efcdd303f | -7.63958 | -35.01148 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| a0a837a5-4497-3997-9932-283d7867fc35 | -6.01315 | -40.9833 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 21559700-b7a7-35f7-99d4-8bcf5732de39 | -5.99051 | -40.98561 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e7337f43-be1d-3a3f-9165-34ada7a115a7 | -6.00609 | -40.98143 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| cefdecd1-b09a-3a36-90d1-ebd4b0c43045 | -7.40574 | -35.19397 | 2026-10-09 03:21:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| c81e85f2-e9a7-32a6-afba-c826fdcaaad3 | -7.64436 | -35.01242 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| 226ddc12-84db-3a2f-812d-163ef976152a | -5.99996 | -40.94977 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 646e8973-c09c-3d4a-b28a-c0a067669e1d | -6.00165 | -40.96546 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| d8eae02c-385b-3786-a11d-08dc359a7e3f | -5.99425 | -40.94101 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ec321260-ff05-34a1-964c-96a89de13540 | -6.01 | -40.97459 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 35bcaa7d-42fe-3b11-aa60-20944c867c13 | -7.64568 | -35.01143 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 4939b62a-352f-31db-9c98-02564eb66f4f | -7.637 | -35.00447 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e68b45c1-df23-30d6-b456-aa09fb8d1f53 | -6.0074 | -40.97436 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| f3c8a09a-674a-38eb-92af-7ac7d4e0d03c | -6.16779 | -39.4494 | 2026-10-09 03:21:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 1cfeb362-bc96-3685-880f-12b99650ab63 | -6.00865 | -40.98161 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| bca30b02-1c1f-3be0-9451-3c83b3e454ce | -6.00298 | -40.95832 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| ea8c5b4f-9c55-37fd-82e9-0923687e0c27 | -5.99444 | -40.97845 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 484c3777-f722-332a-9df1-185554340978 | -6.01134 | -40.96755 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 895f183d-c12c-3559-93b9-2853bd20ae26 | -7.64528 | -35.00731 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| d8853a5e-d763-3a89-ae7f-0160eb298628 | -5.99766 | -40.98701 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| fb7148a1-aeb0-3968-bafc-a279cf98f33c | -6.00157 | -40.97991 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| f486a641-c307-3498-8a26-85654e9e07c3 | -6.00479 | -40.98849 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 2a3cf898-6ad1-3284-bdb2-cd7654a9cf6d | -6.16685 | -35.29586 | 2026-10-09 03:21:00 | NPP-375D | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 34e5b0cb-13d1-332b-9cb9-6f813f65ae54 | -6.00165 | -40.96545 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| bc19b455-05ee-3f3f-903c-48c78b1945e1 | -6.00032 | -40.97263 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| be22a653-20ef-35f8-b9ce-b443c9a3d966 | -6.16779 | -39.44941 | 2026-10-09 03:21:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 3f13e2c8-208b-3a38-935a-8484ad7372dc | -7.64001 | -35.01561 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 390ac437-00da-36f0-9351-deee85755887 | -5.99855 | -40.94238 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ed063c15-99e7-388a-9ee3-6ad9c39374c4 | -6.00871 | -40.96728 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| c9e55a0b-7bd8-3f38-bf45-3acfc589594c | -6.00432 | -40.96561 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 3322a1bd-e7e4-366b-b52d-51610a28bfe3 | -6.0061 | -40.98143 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 52775d52-d57a-3cbe-9193-ec8c9f0ba71d | -5.99185 | -40.97843 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| e3908230-86cc-3a0a-9a54-9e549c482eb7 | -7.40887 | -35.19368 | 2026-10-09 03:21:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 3b7dceaa-17ff-3371-af2d-a06dcc8bb308 | -5.99766 | -40.987 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 38544949-8121-3d2d-aa83-c3996b84ed3a | -7.637 | -35.00446 | 2026-10-09 03:21:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 03f9f122-1c26-321e-bf3f-0ff5b2350b5d | -7.40575 | -35.19397 | 2026-10-09 03:21:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| a7f1c271-83f1-30f8-bce8-dff15e76faf0 | -6.00479 | -40.98848 | 2026-10-09 03:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 68192d4b-c35a-373a-898d-ec957f3c38e6 | -6.89635 | -39.54179 | 2026-10-09 03:23:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ab589b11-e48b-3919-9518-a9b5b799c3ae | -10.19312 | -36.3275 | 2026-10-09 03:23:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 2d7fda02-f4ea-35e9-ad64-19866b0a58a0 | -6.89736 | -39.53635 | 2026-10-09 03:23:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d0eade95-8619-3b47-9bf0-c6948f94f776 | -9.84966 | -36.04352 | 2026-10-09 03:23:00 | NPP-375D | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d6dad478-b3a5-3d51-ab81-c3e3b6d0ae58 | -10.5925 | -36.685 | 2026-10-09 03:23:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3069bc82-026f-33c5-8d70-6266d20a9223 | -6.89084 | -39.53526 | 2026-10-09 03:23:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 61326b02-41a0-3d7f-adcb-d213be891ab9 | -10.16809 | -36.32264 | 2026-10-09 03:23:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b6744d84-f53a-34cc-b9b3-3c01a5bc3c88 | -10.19184 | -36.32766 | 2026-10-09 03:23:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 5c39dd5a-d871-3a9b-80ab-0131f4b22644 | -10.59193 | -36.68801 | 2026-10-09 03:23:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 695b87db-6246-3dd3-8ed6-f1dcaeebadcf | -6.8898 | -39.54084 | 2026-10-09 03:23:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9e8b4285-5c2f-3b06-a2f4-dbdabd221099 | -10.19418 | -36.32168 | 2026-10-09 03:23:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 6c4c3ae6-d4a9-3f62-be42-55183d2a71ef | -10.19295 | -36.32183 | 2026-10-09 03:23:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| f5080881-46a3-30f3-b1a8-d86a59111721 | -10.5925 | -36.68499 | 2026-10-09 03:23:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2f541b6c-b9c9-3c13-9017-f740ca6f4348 | -10.19418 | -36.32167 | 2026-10-09 03:23:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| bd5e9727-00f1-32ba-8cde-3eea83f5ff24 | -9.84966 | -36.04351 | 2026-10-09 03:23:00 | NPP-375D | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8486dec4-87ea-3556-8109-632d1ff66728 | -16.97055 | -41.2342 | 2026-10-09 03:25:00 | NPP-375D | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f9f0858f-9ebc-377e-805b-6530704af01e | -18.64208 | -41.35505 | 2026-10-09 03:25:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 18f041ca-f93b-31e9-a4ad-9005f6aa62c9 | -13.25998 | -42.25675 | 2026-10-09 03:25:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 567f20f4-ab32-37e6-a50c-6f45a194e611 | -13.25333 | -42.25439 | 2026-10-09 03:25:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 0b96eaef-f4be-3528-99b9-d15e84acb953 | -18.32901 | -42.38253 | 2026-10-09 03:25:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| d4a10f4a-baa4-3e31-822f-64114d463826 | -18.33132 | -42.37233 | 2026-10-09 03:25:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 56adc416-9afc-3ea7-ad85-5d00b1c3ba4e | -18.08657 | -42.2655 | 2026-10-09 03:25:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 875471a7-599d-3169-ad39-80acd8dc2204 | -18.63135 | -41.34769 | 2026-10-09 03:25:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| fc47abf8-daf0-3731-b644-60f335022825 | -18.0855 | -42.2702 | 2026-10-09 03:25:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| abf864d3-5259-366c-a7af-be4f527d4d3f | -18.63025 | -41.35261 | 2026-10-09 03:25:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b894faa6-a0a5-3f14-b406-1e8dcd2ed26a | -18.47626 | -42.25191 | 2026-10-09 03:25:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7e224eb5-0e05-3496-9753-33e16ac5103a | -18.63828 | -41.34435 | 2026-10-09 03:25:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3252bf31-961a-3cd3-a3a0-a3f0484572ff | -17.00388 | -41.1707 | 2026-10-09 03:25:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 35b6cceb-52bb-3b51-abd2-e4d1f26e2f99 | -16.96453 | -41.2328 | 2026-10-09 03:25:00 | NPP-375D | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c06a425b-1bdb-3b6b-907a-a069fd548a53 | -18.33218 | -42.37931 | 2026-10-09 03:25:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 94f7fd9f-b2c5-3d54-86b3-dbab9b6179f6 | -16.99035 | -41.17186 | 2026-10-09 03:25:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b3225d35-222d-307a-8e77-565e04727d1d | -16.98959 | -41.17828 | 2026-10-09 03:25:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8c056e0b-1ae2-3dbe-8c05-e3aced48de2c | -18.47943 | -42.25347 | 2026-10-09 03:25:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 206da7af-dfb4-3d9a-8ead-75c9e1a3eb71 | -15.25382 | -42.3656 | 2026-10-09 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 00136cd7-ba1e-385b-a907-6ad18d39da0f | -15.94817 | -41.08707 | 2026-10-09 03:25:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e8fcc6eb-a2f5-3075-8aab-955ea0bcbf98 | -18.32371 | -42.37675 | 2026-10-09 03:25:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c990ffd-465a-30c7-8f48-4ded231dc5bc | -16.99635 | -41.17327 | 2026-10-09 03:25:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 83ab7cc2-2479-3fe9-a7c7-dba8b139852e | -18.33331 | -42.37448 | 2026-10-09 03:25:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5a06c795-00f1-349b-ab33-d5292bea98fe | -17.25418 | -39.472 | 2026-10-09 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 908126a3-0f2b-3c6c-8353-4234f38482da | -17.25285 | -39.47186 | 2026-10-09 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 10a0192a-1e88-31b6-a037-4c590526eaa7 | -17.25359 | -39.46825 | 2026-10-09 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| af54fab0-be6d-349b-b0ee-c8eee6e62f84 | -16.85012 | -40.56366 | 2026-10-09 03:25:00 | NPP-375D | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b1b894f0-3ae3-302e-8307-2e80e74e4854 | -15.94839 | -41.09069 | 2026-10-09 03:25:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8ba22e64-d0b2-3ab6-ba76-a2ffb2a59b8d | -18.33026 | -42.37699 | 2026-10-09 03:25:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| ca62d432-07ab-33d0-9778-2f446fc664e5 | -17.25495 | -39.46841 | 2026-10-09 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c7314f67-db48-3747-975d-ce4461e709f8 | -15.103 | -43.63645 | 2026-10-09 03:25:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f8493377-bca5-33fd-9a37-29de41a9466a | -18.04733 | -44.56231 | 2026-10-09 03:25:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0beb09d8-ec2c-3f1c-99e1-0b77abd1edaf | -18.63731 | -41.34869 | 2026-10-09 03:25:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 7ef97e9f-7007-3306-acc7-2ed620765790 | -16.98928 | -41.17682 | 2026-10-09 03:25:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 2486225e-27c3-3716-b0c6-7dc6585326f8 | -15.95557 | -41.08687 | 2026-10-09 03:25:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ae93c777-2a30-361a-ad8f-2a086f46d5a6 | -17.00949 | -41.17068 | 2026-10-09 03:25:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9dbd21e7-8635-360f-a8a3-46b1b9292e0e | -15.10135 | -43.64367 | 2026-10-09 03:25:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README57.md)
