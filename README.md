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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34fcdf9a-4e0c-31a8-8898-126c31b406a8 | -4.0974 | -48.0361 | 2025-10-16 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 914055f9-5a9a-3ca3-a3cc-b3c1d60c027d | -11.456 | -44.1613 | 2025-10-16 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| c3010a31-13fc-38c9-9d0a-ebe3ce6d02aa | -7.9442 | -44.115 | 2025-10-16 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 48133e1e-600c-3313-90dc-17ce3b76c030 | -7.4894 | -42.7586 | 2025-10-16 00:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 4416f7d7-67ff-3e29-b767-98a39f42afc0 | -7.9628 | -44.1362 | 2025-10-16 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 276.7 |
| a8b70416-4cae-38f5-b751-87738c5cc903 | -3.0157 | -45.3903 | 2025-10-16 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 2c3f22f4-395a-37d6-b847-1c048361e3b8 | -10.8666 | -48.7945 | 2025-10-16 00:00:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0d5c812d-a018-3160-be61-9e20699bdebe | -4.3872 | -43.406 | 2025-10-16 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| e8907727-bb48-3ee9-8c3e-6c019014cbe4 | 1.8401 | -55.7429 | 2025-10-16 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d08a95ff-69f0-333d-98c7-2489a3a91e57 | -11.4368 | -44.1641 | 2025-10-16 00:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 7e13b23b-e197-34aa-8ff0-ac0ec04b2e42 | -9.2255 | -48.6 | 2025-10-16 00:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| c76f927c-3ffe-35ab-a192-c7b77c521c19 | -9.2398 | -63.2489 | 2025-10-16 00:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 96.5 |
| a127d9ae-10d1-381f-aa12-0acf0f4371d7 | -4.5041 | -45.4118 | 2025-10-16 00:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 85978230-2f7c-3114-a4cb-b7bf56646074 | -7.9817 | -44.1342 | 2025-10-16 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 62fb4a8c-e98a-38ce-a2ff-a42f984622f7 | -4.116 | -48.0352 | 2025-10-16 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| f53ac5d7-ae02-36ef-ad11-f154c9724f87 | -5.9221 | -45.434 | 2025-10-16 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6e77514f-05eb-35f1-9f8c-4bd8dc5a4cc1 | -8.4528 | -44.1767 | 2025-10-16 00:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| c03f9f1c-28fb-382c-b490-a65aa8126945 | -4.5042 | -45.3893 | 2025-10-16 00:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 4ddbabf0-0849-3b6b-b846-05f815ef4b66 | -4.5698 | -43.9967 | 2025-10-16 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 8e8463c4-fd49-3022-988b-46d5017b3b97 | -9.2397 | -63.2678 | 2025-10-16 00:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 93d60d35-9b49-3109-b16d-f15d39469856 | -7.9439 | -44.1381 | 2025-10-16 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 09d0064f-c048-344b-8aea-11392ad87752 | -9.2584 | -63.2482 | 2025-10-16 00:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b58d2df8-3a82-37df-a216-87cddc801206 | -7.982 | -44.1111 | 2025-10-16 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f998be7a-dbda-3bd1-a815-955f6a06e5a2 | -8.4714 | -44.1978 | 2025-10-16 00:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 45412dfc-6721-3392-8cfd-b85a710268ec | -4.3687 | -43.3838 | 2025-10-16 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 325.7 |
| 7a6ead3c-c447-311c-84a8-5cadae3f73e5 | -4.1161 | -48.0136 | 2025-10-16 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 35d967cc-7b4e-3435-8080-e76fdf92cebc | -4.3498 | -43.4082 | 2025-10-16 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 2d0496e0-d242-3858-a000-b03e9ab48cd9 | -12.681 | -43.3997 | 2025-10-16 00:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| c215b88c-3c99-35af-8773-6c72c403e232 | 1.84 | -55.7824 | 2025-10-16 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a52f5015-e6b5-3dc1-9d0a-230aa44c6fa1 | 1.84 | -55.7626 | 2025-10-16 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 34bedacf-8be8-3564-8ccb-0f4b9f847451 | -4.3874 | -43.3827 | 2025-10-16 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 30fc5e26-53a6-30d6-ba51-289c36cb7876 | -12.6612 | -43.4268 | 2025-10-16 00:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 1e0fce22-6330-30a6-8300-549ec9ab82e7 | -8.4717 | -44.1746 | 2025-10-16 00:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 150.1 |
| fd2ec36f-e439-371e-98dd-3d2100eaa0be | -3.2737 | -45.8509 | 2025-10-16 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 15be4344-f26f-3212-a8e3-e1597222ca04 | -11.4556 | -44.1847 | 2025-10-16 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b4550509-6b06-31e8-856e-a0b1d3a27488 | -5.4762 | -42.9367 | 2025-10-16 00:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 06df99f4-648f-3eee-bc58-41eb9b4fd97b | -12.6805 | -43.4235 | 2025-10-16 00:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 76538605-52d0-38ab-b0dc-33cd88a9e927 | -7.9631 | -44.113 | 2025-10-16 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 9b2d56bd-85fa-36fa-b75f-ad11d9082faf | -4.0976 | -48.0144 | 2025-10-16 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 6845c2ce-032b-32d3-ad50-df2b7b9674c9 | -12.6801 | -43.4474 | 2025-10-16 00:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| b6b3f1d5-8fb6-3c5a-8e85-36850f48e233 | -4.3685 | -43.4071 | 2025-10-16 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 287.0 |
| 5de4b14e-6772-347f-a0e4-251488ef01c7 | 1.8401 | -55.7232 | 2025-10-16 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| dcb9c73c-3cbe-3090-b064-4e6055a75f76 | -5.6819 | -45.112 | 2025-10-16 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ce56fb8f-9c58-3965-afa8-29ffdb63b67c | -9.0832 | -47.9374 | 2025-10-16 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ad0ae17e-834c-3053-9ffc-62b3f4860f05 | -10.133 | -44.5777 | 2025-10-16 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| d36058ef-df15-3c2e-8fe7-e495b85322af | -10.8856 | -48.7923 | 2025-10-16 00:00:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c391c4be-411c-33eb-8ebe-654d6084a9fc | -9.0829 | -47.9594 | 2025-10-16 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 82cb5f01-9da0-3196-9611-e26e7f0df438 | -5.4764 | -42.9132 | 2025-10-16 00:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| 4a99a3d0-7dbb-3dce-b7f7-e33ba300b5ee | -4.8644 | -44.5748 | 2025-10-16 00:00:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1a38269a-7b75-3edf-9706-809ac9d2ee12 | -4.35 | -43.3849 | 2025-10-16 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 6255894a-77de-3f11-b53f-fc6409559105 | -5.656 | -45.9692 | 2025-10-16 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 7e61d05c-896c-3e5b-ab38-e6f213f7d9f6 | -3.6916 | -47.6411 | 2025-10-16 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7ce1b4e8-abb3-3784-a47b-6f9723deb752 | -5.6821 | -45.0893 | 2025-10-16 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| cf34af14-a8fa-3598-a9d4-a3eceb0893b0 | -7.4706 | -42.7605 | 2025-10-16 00:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 138.7 |
| b58e8347-21d4-3b34-863f-875ad436de6e | -9.2397 | -63.2678 | 2025-10-16 00:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| f70bca93-02a4-3982-b0d0-a06a8a93fce8 | -4.0974 | -48.0361 | 2025-10-16 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 5c94d0b7-0420-3d23-a0ec-a42a57ec2546 | -10.655 | -45.2462 | 2025-10-16 00:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| bd2c7778-f692-3cd7-be4e-d6836c9362d0 | -12.6607 | -43.4507 | 2025-10-16 00:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 2e2f7f8b-1520-3bba-b596-fda38ee2791c | -11.456 | -44.1613 | 2025-10-16 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 26073a5c-3732-38e7-a4d4-5645708cb0bf | -15.1943 | -49.3862 | 2025-10-16 00:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 8397fa3e-27d6-385c-ba51-852b06fe359b | -8.4714 | -44.1978 | 2025-10-16 00:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 8c32f308-5b36-3f25-a46c-095eaac1793f | -4.5041 | -45.4118 | 2025-10-16 00:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 47fa01a4-c66d-3194-93b2-d61da6c85e09 | -12.6801 | -43.4474 | 2025-10-16 00:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 1f76471e-3ffc-3742-a576-44563ee9eccc | -7.9631 | -44.113 | 2025-10-16 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 8da04ada-c9c9-386e-a5f3-f4ad4b8c6644 | -9.0829 | -47.9594 | 2025-10-16 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| f2dfa53b-3efa-3db5-8f17-5674e8148e5a | -4.35 | -43.3849 | 2025-10-16 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 4ebdf777-8792-3ce4-b8e5-1e0d7439d834 | -3.0157 | -45.3903 | 2025-10-16 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| be8429e5-cf8e-3d67-8ac7-4fa78f0d782e | -4.5042 | -45.3893 | 2025-10-16 00:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 713f08ff-5a05-310b-b917-b562ff9fba19 | -4.3498 | -43.4082 | 2025-10-16 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| b9f4883b-407c-3155-acd9-00df5667273b | -7.4894 | -42.7586 | 2025-10-16 00:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 8d819144-808b-3c6c-bd70-97773cdb7081 | -4.3872 | -43.406 | 2025-10-16 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 695af58a-1991-3dca-b69e-4f8725cd5622 | -8.4528 | -44.1767 | 2025-10-16 00:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 6b83941f-9406-3764-9fa5-87af55b5cfd3 | -4.1161 | -48.0136 | 2025-10-16 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 5588db48-a84e-3cb8-99ee-2a78d48a4200 | -10.133 | -44.5777 | 2025-10-16 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e47afad6-1316-3eb8-bf3b-9f3a4cdcc9f5 | -4.0976 | -48.0144 | 2025-10-16 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| aec106d2-52bd-3a52-83ab-3bcea7c1a365 | -4.116 | -48.0352 | 2025-10-16 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 8fe05657-812c-3bbf-a1a3-319d6dc2b782 | -4.3684 | -43.4303 | 2025-10-16 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| cb06f62d-fede-34e2-bf48-07923223706a | -10.8853 | -48.8142 | 2025-10-16 00:10:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 5459aaf6-7672-3c96-87b0-079e027762c3 | -7.4708 | -42.7368 | 2025-10-16 00:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| bd719a2f-4f7b-3911-96c4-5e4cdb163f97 | -3.2737 | -45.8509 | 2025-10-16 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 26dc0708-7709-3b56-a4ee-aa6b1d808c22 | -9.2255 | -48.6 | 2025-10-16 00:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 62af592f-7e2a-34cd-90ed-b386ebd32c6f | -5.4762 | -42.9367 | 2025-10-16 00:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| e0faef0f-b553-339a-9009-2a8abe972250 | -8.247 | -44.0368 | 2025-10-16 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 54bf3897-c9c0-39cf-b924-ee1522483b38 | -8.4717 | -44.1746 | 2025-10-16 00:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 13b6e34b-729b-3751-a5b9-5809b0c21516 | -15.1748 | -49.3893 | 2025-10-16 00:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d820482d-7b6f-3743-8922-23a592a648f6 | -3.2738 | -45.8286 | 2025-10-16 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 35.0 |
| d5ba9428-0c37-384f-9e58-dde0c224b254 | -4.3874 | -43.3827 | 2025-10-16 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 7cb858f5-c9d7-3633-8cbe-94838ffa98c7 | -10.8666 | -48.7945 | 2025-10-16 00:10:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 420d7cd4-6906-3334-811d-e27870052814 | 1.84 | -55.7824 | 2025-10-16 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 57f54b76-c6a8-37fe-b799-18916a19d1cf | -12.6612 | -43.4268 | 2025-10-16 00:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 3828141e-cbde-37ec-a73b-ab32d9727eb2 | -26.8188 | -50.5512 | 2025-10-16 00:10:00 | GOES-19 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| 94430472-bc0b-3532-baa6-3dea09901db2 | -4.3687 | -43.3838 | 2025-10-16 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 310.1 |
| a91b2021-c85d-36c9-b44b-49a9e62f53c3 | -9.0832 | -47.9374 | 2025-10-16 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 7b9010f1-2521-3c18-911d-525a8c044034 | -15.1744 | -49.4114 | 2025-10-16 00:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 66d67820-26d3-317e-a84e-62f49a20a572 | -9.2398 | -63.2489 | 2025-10-16 00:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 92.0 |
| b298f742-1086-3759-bda0-08a2d4c52409 | -7.9442 | -44.115 | 2025-10-16 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| fdb41314-65b8-369d-bc17-ec6a5b804592 | -7.9439 | -44.1381 | 2025-10-16 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 3df23fd8-93f0-3da4-8c3c-47557009b18f | -11.7601 | -61.0743 | 2025-10-16 00:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c667f6ec-c4ad-36c4-8f1a-b9f690465975 | -4.4856 | -45.3903 | 2025-10-16 00:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| eab58bd1-6564-36fe-b8eb-5fa396d33f39 | -4.3685 | -43.4071 | 2025-10-16 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 259.8 |


[Clique aqui para ver as próximas entradas](README2.md)
