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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db7125da-5f8e-3acf-b972-bfda6c09f9ad | -19.7668 | -56.709 | 2025-12-02 03:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |
| bf95fef3-87e9-31e0-ab4f-baf37c4d3c78 | -1.4923 | -45.7903 | 2025-12-02 03:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 6b18b9c3-1eb5-371f-a889-50427a02aa92 | -8.0703 | -43.0981 | 2025-12-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 837c5a30-f8b7-3505-8fbc-9424c73f698d | -9.80096 | -37.64775 | 2025-12-02 03:17:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8e5851b1-ee58-33f6-8f7b-79ec0ead61a8 | -6.74496 | -35.04244 | 2025-12-02 03:17:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 37.1 |
| d9452421-f7de-3d8e-9ed1-44411208a567 | -6.24089 | -40.29718 | 2025-12-02 03:17:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ceadea92-d7e3-3c3a-a538-dee334523b0c | -6.28265 | -39.68813 | 2025-12-02 03:17:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a93c8f54-17e5-3b3c-81e2-9c18bfd0d1e4 | -6.2835 | -39.68345 | 2025-12-02 03:17:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1abb629d-9d10-30e7-b931-29aff65c2de4 | -6.74265 | -35.0408 | 2025-12-02 03:17:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| 6b516476-89cd-3b43-a5c5-97f4f12c02a5 | -6.74193 | -35.04498 | 2025-12-02 03:17:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| 563d1dca-a84c-3b4f-b534-c4a7b27c149b | -6.23998 | -40.30206 | 2025-12-02 03:17:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8373c8b1-078a-3cad-bce9-f75c105d4562 | -9.80586 | -37.64862 | 2025-12-02 03:17:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0855e3bd-7ad7-3a80-93c9-2f6971c18e71 | -6.74696 | -35.04162 | 2025-12-02 03:17:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c0a58cc2-509d-3fc4-9343-93f6529fa231 | -9.68005 | -37.3092 | 2025-12-02 03:17:00 | NOAA-21 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1f3de0ed-4089-310f-ae52-ded4efe6ad7d | -8.05252 | -43.10347 | 2025-12-02 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 1a01fb05-1d59-3a8c-8b0f-719a798d5a99 | -9.71303 | -36.24961 | 2025-12-02 03:19:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b4dbd409-e8be-37f7-919f-d2e49750e5d9 | -8.0489 | -43.09945 | 2025-12-02 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 7c2ba8b9-258e-3853-beed-e09e291306ce | -8.1725 | -43.22091 | 2025-12-02 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 04553c37-2b9f-3b3f-b134-91ffd4f32780 | -8.16542 | -43.21948 | 2025-12-02 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 1fd4f0ce-c405-37c2-8289-9ee243f56855 | -8.04761 | -43.10611 | 2025-12-02 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 2dd55859-2348-3483-975c-1ec6bfae2ca3 | -7.80702 | -35.22152 | 2025-12-02 03:19:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c5d987b7-da6b-3946-a3e2-bb53f44ab117 | -17.73994 | -39.71755 | 2025-12-02 03:19:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d98a1849-1ff1-318f-986b-650e2e44e762 | -8.0596 | -43.10474 | 2025-12-02 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c01b32bc-de86-3914-b82d-364128912b3c | -9.71751 | -36.25031 | 2025-12-02 03:19:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 26569712-3cfb-3e5e-b7e6-145dc3ecdfa5 | -9.72119 | -36.25552 | 2025-12-02 03:19:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6644e59e-10b8-3534-86e5-852d809273fc | -7.72321 | -35.12902 | 2025-12-02 03:19:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 96614a07-3a78-3a9c-805d-85e8b0b57162 | -8.05386 | -43.09679 | 2025-12-02 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| e68c2616-d094-381f-b516-745548c4aaea | -9.71222 | -36.25412 | 2025-12-02 03:19:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 52cb5971-5a74-3cde-b435-b5d0e3eba073 | -8.056 | -43.10059 | 2025-12-02 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| af7d04d9-9334-3042-b63a-7858c7b049bd | -8.05114 | -43.11034 | 2025-12-02 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 574098e6-b9db-3d6d-8803-e2e7dfe8f38a | -17.25629 | -41.19618 | 2025-12-02 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c3a1c334-f174-30b9-ad4f-c3a791e32cbe | -8.16923 | -43.21986 | 2025-12-02 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| baa018b2-4e25-3907-9af6-2457967bbbd3 | -8.05468 | -43.10742 | 2025-12-02 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 248e0afd-7b63-3e8a-9eb3-ebcbc62e7c79 | -17.03283 | -40.3244 | 2025-12-02 03:19:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c76c400f-4afe-3bb4-9c4e-33e7aee40b68 | -7.72391 | -35.12496 | 2025-12-02 03:19:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9ee769b9-d463-3448-9289-f8ce3867c5ff | -17.03348 | -40.32117 | 2025-12-02 03:19:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d51027aa-c63d-32f9-b05a-1d5f6959fd70 | -9.71671 | -36.25481 | 2025-12-02 03:19:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 0dec8d1d-4e7c-3d61-812f-eeef72eaf289 | -8.051 | -43.1237 | 2025-12-02 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| e6f94ca3-eb01-3da1-a9d3-bd4a9277939c | -11.1379 | -53.9429 | 2025-12-02 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e2f60d57-83a0-3af4-ad39-e162dbfbab37 | -8.0703 | -43.0981 | 2025-12-02 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| fb20bbe8-e728-333b-aa42-ceff010f7fb1 | -19.7873 | -56.6851 | 2025-12-02 03:20:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| dd71510c-f8c3-35e9-946e-56ea1df19fa6 | -8.0513 | -43.1001 | 2025-12-02 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 334.1 |
| b132d440-eafc-326c-a2c5-175ba552e7c5 | -8.0516 | -43.0765 | 2025-12-02 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 0dab5895-642f-3411-b0d3-fb012ee9c844 | -1.4737 | -45.7907 | 2025-12-02 03:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 3450ef7a-185f-3213-b2ab-ee2bb57eed6a | -8.163 | -43.229 | 2025-12-02 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| efcb7ef0-4e35-39cc-b378-c8c8754c9b71 | -8.0324 | -43.1022 | 2025-12-02 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| c66ff25d-c749-3080-9c0a-b7756a2b4756 | -8.1633 | -43.2055 | 2025-12-02 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 614f2721-0cec-3007-99c9-11c548e515e3 | -1.4923 | -45.7903 | 2025-12-02 03:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 6d1a3ebb-1fcc-3c4f-b523-ccb259e44ecd | -1.4737 | -45.7907 | 2025-12-02 03:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 4653a04c-c0f6-3b35-90ce-63d314045823 | -8.0324 | -43.1022 | 2025-12-02 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| f60d8402-61f7-362e-8ed7-2fdd1258e4c9 | -8.163 | -43.229 | 2025-12-02 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 9e2edb37-2178-364c-a2f1-48b28e18a992 | -8.1633 | -43.2055 | 2025-12-02 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| b3273198-9652-3411-98ec-5db99d53a36c | -8.051 | -43.1237 | 2025-12-02 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| ae882c87-13bd-3a10-915f-9f89f75b2e22 | -8.0516 | -43.0765 | 2025-12-02 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 2738fe30-caac-3ba4-b282-09fa9006ab62 | -8.0703 | -43.0981 | 2025-12-02 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 40c4cd95-cd00-3f36-b553-d5969134e55a | -11.1382 | -53.9223 | 2025-12-02 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| de6d33e1-da92-3d5a-ad13-309c23ed8147 | -8.0513 | -43.1001 | 2025-12-02 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 238.4 |
| 6e0274b8-a9a8-3043-97c4-0db050e5499d | -11.1379 | -53.9429 | 2025-12-02 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| fa39979d-4ea7-32a5-9e27-92962942acd9 | -3.2565 | -45.5607 | 2025-12-02 03:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 76e26996-1c74-3c7f-996a-616cb60c4d41 | -8.163 | -43.229 | 2025-12-02 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 9f3985e9-a30f-3688-be11-0108eb829fda | -8.051 | -43.1237 | 2025-12-02 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 0542ca0c-12cc-3d80-b8d3-aa3ca9c0685f | -8.0513 | -43.1001 | 2025-12-02 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 309.8 |
| c1b496e2-dab2-30d7-8f67-0cad976eab55 | -3.2379 | -45.5615 | 2025-12-02 03:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 3a372670-d15a-36cc-89f3-443b40013559 | -11.1379 | -53.9429 | 2025-12-02 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 375e57ed-3844-359c-a469-f1cddf0417c1 | -8.0703 | -43.0981 | 2025-12-02 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| da6862ec-d288-3096-a42a-f50300acbb1d | -1.4923 | -45.7903 | 2025-12-02 03:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8d6eb8f9-6ef4-3576-bdae-f5525adfa496 | -8.0324 | -43.1022 | 2025-12-02 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| e9086bf9-2a64-3558-8661-0d37e52fbc2a | -1.4737 | -45.7907 | 2025-12-02 03:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 0a6bfe60-9192-3860-b08b-0f7791ec4789 | -8.0516 | -43.0765 | 2025-12-02 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 3eb99feb-b646-31b5-b65e-408d8db5dc22 | -3.23717 | -45.57722 | 2025-12-02 03:46:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f73eacaa-2694-36e2-8062-924aa5c52f50 | -3.3208 | -42.50206 | 2025-12-02 03:46:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2edc377-f388-3e86-b8b5-0d0824227f26 | -1.48346 | -45.78761 | 2025-12-02 03:46:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| b4a468dc-a387-35d1-9f14-57f17ae25d80 | -4.02322 | -40.21493 | 2025-12-02 03:46:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 01a6e3e8-1376-355a-a56b-6b06fbc07957 | -7.44164 | -42.5461 | 2025-12-02 03:46:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 123d3a9f-6a03-3e60-8370-4a0a25b5ddcc | -9.80465 | -37.64678 | 2025-12-02 03:46:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9f2ffa5e-8af8-3f62-975c-c486a4b6be6c | -4.37426 | -43.15374 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 888b8391-382c-3dc2-9d49-6fecf722f374 | -8.04092 | -43.1011 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 740a7936-a868-326d-80f4-7f49491077d6 | -8.05996 | -43.10446 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 08dc3c13-f4b0-313c-a377-6814c05f857d | -6.68672 | -43.54826 | 2025-12-02 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 575daed0-0b74-362b-ae88-54adba6e604b | -1.47992 | -45.79676 | 2025-12-02 03:46:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 7d9ae46c-be78-3714-b6cf-c930938910a2 | -4.37782 | -43.1509 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37550d9d-a4fc-3bf3-bf5b-69a78c3768b9 | -8.03919 | -43.13797 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bef036cd-2366-3768-bd5b-d63b87bf4aeb | -8.04895 | -43.11112 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 898e0a36-ddfd-3ef1-95ba-9ebf921223a3 | -7.34651 | -34.89436 | 2025-12-02 03:46:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc9f0b6c-edfd-3dd5-b016-2605c8153eef | -8.73535 | -39.6802 | 2025-12-02 03:46:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1b5af66b-01a8-3bae-bb78-8091a71e7289 | -3.32668 | -42.49735 | 2025-12-02 03:46:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e01d598-18d0-3925-9492-d37751a67d9a | -4.3834 | -43.14883 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 752e8b58-e26f-348d-87d9-5dc6d178947f | -6.24185 | -40.29935 | 2025-12-02 03:46:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 69949fd3-81db-3446-8639-87496effcd5b | -1.47716 | -45.78645 | 2025-12-02 03:46:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bda47fc9-7d59-3fea-b186-bd72b7af3cbc | -8.04507 | -43.10513 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| b3cc06f8-7586-3243-986e-92c5722c76bb | -1.48623 | -45.79789 | 2025-12-02 03:46:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5cd62aa5-9f0a-3b46-b993-64c0f129e756 | -8.0486 | -43.11303 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 57bbf9c2-73ed-398b-885f-20f417d6146a | -8.16644 | -43.22134 | 2025-12-02 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 9453cba2-5ab1-365a-834a-b0580351c7ba | -5.09135 | -40.23926 | 2025-12-02 03:46:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c585cbb6-9be0-343d-b7a9-bb93a22de2dc | -5.1299 | -36.42856 | 2025-12-02 03:46:00 | NPP-375D | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d1b6b60-dd62-3a55-b570-22ee19919437 | -4.37883 | -43.14501 | 2025-12-02 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 818c4910-315e-3072-a349-beec963096d6 | -7.91621 | -43.78844 | 2025-12-02 03:46:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b80a26d6-c4b2-3379-8d3d-ab123df26102 | -7.44083 | -42.55076 | 2025-12-02 03:46:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d397dc37-1ce9-39b0-bdf5-c889c3013496 | -1.68848 | -45.79603 | 2025-12-02 03:46:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 789cf145-7798-3149-8726-27d9b967d2cc | -3.23796 | -45.57264 | 2025-12-02 03:46:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |


[Clique aqui para ver as próximas entradas](README7.md)
