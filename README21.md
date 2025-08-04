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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1599bbe-547a-3219-b49f-3eeea1fc92d8 | -6.32477 | -45.65589 | 2025-08-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e130d19e-e43d-355e-bf07-e0ff80ff744a | -6.31962 | -45.65507 | 2025-08-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b960cb24-fa5e-371c-94a5-cdc8911a91fc | -11.22168 | -48.43704 | 2025-08-04 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 398f1539-6f3c-3e92-be17-8e8a25dd51dd | -7.51698 | -61.32009 | 2025-08-04 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79c114ea-835e-33f2-83bb-c793175acbab | -10.24522 | -50.16816 | 2025-08-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7211471f-eede-32a6-bb35-74082291769a | -6.62496 | -59.97304 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3ed24abe-3cec-3ac6-a0bd-730c3aff813e | -7.01045 | -59.83072 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f05ace5-f241-3d0c-9bf4-93c4e75f22c2 | -9.46012 | -57.83849 | 2025-08-04 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97b24da7-b1a5-3e8d-a879-2e739a285d51 | -10.7805 | -48.80243 | 2025-08-04 04:57:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30fe01e6-ae34-3cb1-86ba-dd7aec3ccf01 | -11.92438 | -44.96547 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e9f5b26-1832-3a2e-b019-21464ad698ab | -7.0133 | -59.83879 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87390845-811a-333b-b007-3763d07fd779 | -6.61789 | -59.9639 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b319002d-6edf-35c5-9eea-bd4dc0503721 | -8.74441 | -46.41369 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8f67afa-c20c-3a7d-9750-91cdee71ed22 | -6.65102 | -59.10708 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6b462b52-1192-3762-8dda-a8999dd9898b | -8.36053 | -46.91421 | 2025-08-04 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb155060-71a4-3b9f-b508-72eee0456156 | -11.22688 | -48.43316 | 2025-08-04 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e1bbf82-b118-392e-89b5-9d7a2fd67c9e | -9.39229 | -45.50936 | 2025-08-04 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f293da3-ee0c-3718-9330-1671f213abcd | -7.65286 | -49.84239 | 2025-08-04 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c778d71-87b2-358a-a7c6-9b5dff282e49 | -10.59569 | -45.25982 | 2025-08-04 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b4c6fbb-3a74-33fd-b770-3d928fa62e0f | -11.75432 | -45.00677 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88baf68b-6bbc-32b8-a40b-094faab36151 | -9.26961 | -50.25538 | 2025-08-04 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72f8c09f-0a0b-3387-a4af-7e252f4b1dd3 | -7.40063 | -45.2694 | 2025-08-04 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee9449b3-2c97-3974-930c-22b2e82c7eb0 | -6.64976 | -45.88939 | 2025-08-04 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d6de108-9590-3187-a6c1-0be757654c64 | -8.00767 | -43.13986 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 31ada6bf-500f-3a6c-996e-a79e075037e9 | -7.96288 | -45.10196 | 2025-08-04 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf153402-cbba-3ac6-8318-dc4aea036011 | -8.01698 | -43.16579 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4e618470-5ad7-332b-ba56-d6682c1aa667 | -8.0214 | -43.13184 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5129ec0a-1490-38df-a515-efb01584de3d | -8.51377 | -44.74891 | 2025-08-04 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70c4cda3-e840-3eac-bb93-fa437649a6ba | -7.00982 | -59.83442 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dc29567-8b1a-3809-816b-2be2e4007135 | -7.40016 | -45.27285 | 2025-08-04 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92c05093-9985-39a6-9a1f-f82d684dbd4a | -8.13062 | -49.58856 | 2025-08-04 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2af4faa0-e41d-3c1b-aa87-7eb8794fced6 | -8.02956 | -43.11791 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 07244e6f-8443-3258-b827-08ed1d2dbae1 | -11.22256 | -48.42992 | 2025-08-04 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 510be8d0-f951-3268-81d1-b7b8bb1ed81f | -8.25893 | -47.33876 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5973a66-ea57-3be8-9aa3-e37be632c34e | -8.00391 | -43.16892 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cb1a9723-0fc7-3d14-81f9-271ad5342aab | -8.05714 | -43.10149 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8b406315-a8cb-34a7-adcd-89fb3dbbc87c | -10.2922 | -45.18014 | 2025-08-04 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3767e62e-7705-3a12-8c7a-2e666712e76a | -7.99772 | -43.21686 | 2025-08-04 04:57:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| cb72815b-7b1e-3788-bf10-1443b3387d91 | -10.24621 | -50.16106 | 2025-08-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0daa3f8d-d86c-333f-9795-35850eea971e | -7.13366 | -48.19251 | 2025-08-04 04:57:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89c349fd-2b6f-3a64-8ab5-5197a3cc6839 | -12.44033 | -44.85144 | 2025-08-04 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63924466-9363-3383-88cf-eca830d36cb3 | -7.77279 | -45.21588 | 2025-08-04 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 159f0c64-6cca-335d-a205-e97299cafb81 | -7.0152 | -59.82767 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e640434-4d91-389e-8107-70c006e508cb | -8.26309 | -47.3333 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a45b2be8-945a-3faa-8824-26948c097698 | -8.00017 | -43.14885 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| cd95387f-22f1-38ff-addb-81152f610309 | -8.26967 | -47.36626 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| abc0f9c9-1fe9-33b7-ab3c-73bbb28a172c | -9.4852 | -63.26781 | 2025-08-04 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47fcf8f4-2277-3bc1-bec2-784eba1a01d4 | -10.24974 | -50.1652 | 2025-08-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e1b4a389-1fe2-3e2e-bb61-b4b351f8cb15 | -7.77133 | -45.22647 | 2025-08-04 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90f2332a-ff58-3433-9f86-d9849880ea5d | -6.64708 | -59.1064 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77fa2bfb-9b87-383a-bda1-e7e43de4d26f | -7.77773 | -45.22015 | 2025-08-04 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcd81796-0797-3ccd-8d4d-70d98d1e043b | -8.74402 | -46.4166 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b0ab1b7-e907-3be8-a7bc-8a68f727b215 | -7.99711 | -43.17262 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| c5caa9c8-5078-3c3f-9984-86e0644bef32 | -7.56408 | -44.89166 | 2025-08-04 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 351d339b-af26-32a1-a387-0c95fa4e6d38 | -8.27223 | -47.3705 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b3d8929f-373a-36ab-9c49-4f80347608ca | -11.74952 | -44.99781 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 639248c0-42bf-3ffe-b1f2-822b451c18a8 | -11.93027 | -44.96578 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93f4bdb9-4dbc-33b6-8e4a-eefb4f8ba5db | -6.61853 | -59.96004 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac7127aa-de16-33e1-8f3f-2618bed4980c | -6.64625 | -59.11144 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d29ce048-3113-3477-8d27-f2e05080d790 | -8.05648 | -43.10649 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4de0ba39-355a-35c1-9228-f659196a5b39 | -8.37028 | -46.91563 | 2025-08-04 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5712fa7-d44f-3b87-93b9-3ac8c488e464 | -8.13115 | -49.58495 | 2025-08-04 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e84e1427-fe9e-334a-aac2-87e36231aee8 | -11.92353 | -44.97253 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc5cdae7-d93a-3221-a9ad-0e905d376002 | -7.99273 | -43.1574 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 4da0601e-1d9f-30ef-8f4f-5ed2522d3dbb | -8.72962 | -46.40819 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8265850a-fd38-335c-9a53-8bfa9d5e845f | -7.26828 | -46.1641 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1306f890-6faa-38bb-89f0-8d75f32eb76f | -11.22654 | -48.43523 | 2025-08-04 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1c0c2fc-92ea-3cd1-948b-7c1dab33383d | -7.99712 | -43.22151 | 2025-08-04 04:57:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6311b68a-05f6-3fe6-a0ce-db03070ea7ae | -6.65185 | -59.10206 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c68593d3-8525-3ae1-a0bb-5a4c1e3c6302 | -11.22716 | -48.43043 | 2025-08-04 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9be7d6d0-b296-3de7-9344-673171cf4cca | -7.99954 | -43.15372 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 7bad895b-d3d3-3ef3-902e-50a78126f1e2 | -6.62043 | -59.9486 | 2025-08-04 04:57:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8011cf56-df4d-3674-8e44-3e7f43a2c6fd | -8.25768 | -47.33742 | 2025-08-04 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5755cd0f-6b0f-35ce-b66c-fec7ab700628 | -10.25072 | -50.1581 | 2025-08-04 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97c2a755-289c-3a0f-b3ed-646574313aa4 | -11.22569 | -51.5328 | 2025-08-04 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4487f7b-77eb-3829-8c6f-cb8e7cd04fb7 | -8.38677 | -46.94027 | 2025-08-04 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ceca5cd1-769f-3071-8fb7-b2412d00a1f4 | -8.01389 | -43.1408 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| bb805708-4e08-355d-98bd-5e41e07d4a45 | -7.94966 | -43.91056 | 2025-08-04 04:57:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b715a569-75be-383c-a0dc-d3212c5b15ed | -7.54342 | -44.87748 | 2025-08-04 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03beacb8-4083-31d8-b2a1-7be849911634 | -11.75481 | -45.00275 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66de1fb9-e00f-3a7d-b21a-e66ea59e6ffb | -6.6688 | -59.16469 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60ec27bb-8293-3e60-a604-37d4d46ae40f | -7.99834 | -43.16305 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 0b0a95ed-1892-3eb8-a793-b14b69aa3d3c | -6.62432 | -59.97689 | 2025-08-04 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a74f4d1a-ab14-3319-8e4b-2de5f2923429 | -7.77678 | -45.22709 | 2025-08-04 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47d15c8c-c265-347f-8d6e-b6afac4ad11b | -8.38117 | -46.94479 | 2025-08-04 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f51c137-419e-32bc-a5a9-e2e6d4f6c2b1 | -11.92644 | -44.94813 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2aa50361-af93-3b97-abfb-20177a66b420 | -7.99832 | -43.21218 | 2025-08-04 04:57:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| bf789e4c-937f-340b-b572-7eca5958f7ef | -8.01448 | -43.18506 | 2025-08-04 04:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e05c82fb-1aaa-3b75-8e53-431fa2957c2d | -6.64704 | -45.89268 | 2025-08-04 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 790397af-7aa3-30ae-92b1-9d455568c3f8 | -12.48213 | -51.76641 | 2025-08-04 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa89bb6f-8bd3-3150-88a1-1ebd731756db | -6.64396 | -59.10072 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a79c36e6-d702-363c-98df-b41671b8ed01 | -11.74852 | -45.00593 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4663c5d2-d424-3c27-ae76-e5fbc4fd788f | -6.65019 | -59.1121 | 2025-08-04 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e270fe44-1224-36b1-bbfd-cccd37b56671 | -11.22138 | -48.43901 | 2025-08-04 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f558f345-3892-34e8-8007-abf693cc99db | -11.92395 | -44.96904 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40bb921e-d9d2-36bb-bdd1-c0ca6d567d0c | -7.08101 | -44.37172 | 2025-08-04 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 301a9911-cf94-35e8-85ec-089a7cc854f7 | -8.73629 | -46.3969 | 2025-08-04 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19060797-86f4-33fe-9fdf-3f1ee6636b3c | -11.99429 | -57.21538 | 2025-08-04 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 157a1c35-4ff8-3911-932c-acf997946559 | -11.7645 | -44.97213 | 2025-08-04 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7fdd749-2931-3d06-814b-e3bd982f0f03 | -7.56359 | -44.89535 | 2025-08-04 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README22.md)
