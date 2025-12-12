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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f85863c-5263-3d97-9aec-5517c18a8d01 | -2.4367 | -51.948 | 2025-12-12 03:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c60ca9fe-ad1d-3c4d-9d63-653a3845394c | -2.4183 | -51.9278 | 2025-12-12 03:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 6588fa6c-2216-38c2-baea-5587b1e2592b | -14.8941 | -58.1282 | 2025-12-12 03:10:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 1862f9e6-64d2-309c-866b-20c78f0b1442 | -2.4367 | -51.9274 | 2025-12-12 03:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 7e10ccde-9d8e-331f-bcbc-f7c4dd44551d | -1.7517 | -54.0323 | 2025-12-12 03:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 6a84deaa-44c8-31f9-9ff1-051f431ec21e | -8.0513 | -43.1001 | 2025-12-12 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 4dd2829a-2d0c-3303-bd15-6ba1e4ca2e79 | -14.9134 | -58.1263 | 2025-12-12 03:10:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ec422908-d895-33f6-9b0f-31c34cd77461 | -2.4183 | -51.9278 | 2025-12-12 03:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 73047650-1c42-38fe-8ce0-de8a1955046b | -10.1994 | -36.3197 | 2025-12-12 03:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 102.6 |
| 502cd9df-0bf0-36dc-beac-9d4533355531 | -14.9134 | -58.1263 | 2025-12-12 03:20:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a7d7f76e-3fd6-3c59-ac4f-1731342cba80 | -2.4367 | -51.9274 | 2025-12-12 03:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 422699fd-508f-3aa3-b426-dea2d0b92fdb | -10.1796 | -36.3503 | 2025-12-12 03:20:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| effc77a5-167d-3a0b-9fd8-0b612a78bfd3 | -8.0327 | -43.0786 | 2025-12-12 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 28abd39a-b972-38ef-ad25-b213bcc30f29 | -8.0324 | -43.1022 | 2025-12-12 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 43cafb7d-5203-30ef-9318-cf24ed42b103 | -14.8941 | -58.1282 | 2025-12-12 03:20:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4c06eb86-dd74-3dec-a044-dd9c6004ded2 | -2.5108 | -51.8023 | 2025-12-12 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 4ca4df43-3306-372e-a639-890c2be2ba5c | -10.1801 | -36.3232 | 2025-12-12 03:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 122.3 |
| f6f32412-06c8-3b8c-b1ae-06e77a873cea | -8.0513 | -43.1001 | 2025-12-12 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 211ad3c6-838e-3a47-8bb4-c7437aece0e4 | -2.4367 | -51.948 | 2025-12-12 03:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 687d6722-4c1e-369a-82c3-b558dd72e424 | -2.4183 | -51.9484 | 2025-12-12 03:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a5840d0d-8427-36d3-8e43-64faa86735f0 | -3.23071 | -42.08168 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1c1b1e1a-94a6-3da9-ac80-f153fc503535 | -3.23212 | -42.07314 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3c4fde3c-bc0a-381a-b6d5-78d519effa28 | -3.23414 | -42.08494 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b35f815-1786-31bc-b903-a2161441c52a | -3.23591 | -42.08703 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ea01880-07d5-3f4f-89f9-1090ad772953 | -3.2356 | -42.07646 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 008ad8e1-a6b2-3875-9cd7-c881c92a9817 | -3.3927 | -42.10519 | 2025-12-12 03:27:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1e98c565-2268-349e-a656-e3c4953b73d1 | -3.23486 | -42.08073 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1fdfe6fb-9898-3d09-a237-9eb855435426 | -3.43394 | -41.65155 | 2025-12-12 03:27:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 71b112aa-9364-3f38-aa32-b1c9d4a20b60 | -3.23633 | -42.07219 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0ee5dad9-2cd8-3888-83d3-cb356911ad98 | -3.30235 | -42.52789 | 2025-12-12 03:27:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ddad993-32f4-37e2-bb2f-5e10a3647cd9 | -3.23044 | -42.07111 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6a04e42-ef4b-32e5-a907-2463c71c6506 | -3.23 | -42.08596 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eeb98d0a-495e-35e3-bab3-8bb942fe38d8 | -3.43969 | -41.65246 | 2025-12-12 03:27:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a1a8d9ab-07bb-37c3-b9d1-15f34c878325 | -3.22971 | -42.07534 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 461ab16d-01a9-3ffe-b890-1e403adc766f | -3.39861 | -42.1062 | 2025-12-12 03:27:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| af7367d4-e050-3f6a-b0d3-0c5deeb539e8 | -3.23731 | -42.07853 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8f64bec-3668-371a-88d8-765a46cd2e3b | -3.2366 | -42.08281 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e176e5f4-3c96-3bb4-bd90-efb5c7cfbaed | -3.22897 | -42.07961 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70f484f5-7b99-341f-a9aa-aae663adfe82 | -3.30764 | -42.53349 | 2025-12-12 03:27:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc3cee37-b675-3b12-9e14-f524e6606f51 | -3.22823 | -42.08389 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3a81e28-c0f4-357f-9aaf-52815cbd3afd | -3.23142 | -42.07739 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 68278a31-2bb3-341d-87e8-b62c682583b0 | -3.44037 | -41.64844 | 2025-12-12 03:27:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e0cd8e44-2b9d-3970-b61b-c7ee09ff6ad4 | -3.23802 | -42.07424 | 2025-12-12 03:27:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fff97085-dc1e-33ec-ae76-504e62c2c162 | -3.22947 | -41.79982 | 2025-12-12 03:27:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 387a7dc2-aaa6-36a8-9554-f6acc2dcdcd2 | -6.95251 | -38.61873 | 2025-12-12 03:29:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7edf65ee-9ef6-3f8d-af2a-6c18814deb4c | -4.16154 | -39.24793 | 2025-12-12 03:29:00 | NOAA-21 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ffe7e3f1-4451-3a4a-a89e-fabfccf94213 | -10.14178 | -36.40588 | 2025-12-12 03:29:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 52ebe912-cb59-3d39-b841-1cd41b80b27b | -9.15756 | -37.18845 | 2025-12-12 03:29:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b74490f-fb8e-3b12-aa5f-81c16b49b078 | -5.89236 | -38.17634 | 2025-12-12 03:29:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 814d5424-e4ac-3a3a-8baa-751ecd22acfe | -9.40949 | -35.65113 | 2025-12-12 03:29:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 51f65df6-1e02-3f92-b68d-387b96911eb9 | -8.79888 | -36.95365 | 2025-12-12 03:29:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1caa9d9a-66f0-3bcd-b6bf-92637107ca11 | -3.97307 | -42.51492 | 2025-12-12 03:29:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8514c913-bd13-37df-a35f-eb779412c13d | -6.47226 | -35.16893 | 2025-12-12 03:29:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 001606be-e81d-3b8a-8496-7ee86f50f7ba | -6.95647 | -38.61887 | 2025-12-12 03:29:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1bcc86d0-c273-33df-becc-b46c95868030 | -5.15986 | -37.69833 | 2025-12-12 03:29:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 52412dd1-ed1b-38fd-9321-d40ce5bf4250 | -8.80273 | -36.95433 | 2025-12-12 03:29:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa8482fa-b8fd-39c4-9b66-7038d5defc84 | -4.73435 | -43.07565 | 2025-12-12 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e29a9b5c-9066-3b6c-b0fe-57ef90cbc74d | -6.11819 | -41.28114 | 2025-12-12 03:29:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| aec6798d-097b-3969-a3d6-fa03d8818bd0 | -3.96442 | -41.52697 | 2025-12-12 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f7735be7-cf29-31ef-8c7c-8797e50e54b7 | -6.11758 | -41.28461 | 2025-12-12 03:29:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4ad6ef9d-1061-3488-ab15-4dd3ea662cbb | -7.91556 | -37.59784 | 2025-12-12 03:29:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 15916d89-c068-3dc8-bc6e-30cfe109238a | -4.33068 | -39.14906 | 2025-12-12 03:29:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f996976d-aa89-3c95-a6c8-a45512ecacda | -10.14545 | -36.40647 | 2025-12-12 03:29:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cf92c695-ac06-3903-95d7-77c7231ac759 | -3.95379 | -41.52135 | 2025-12-12 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3732f0e2-4ba0-324d-9564-4a508081e96e | -6.95625 | -38.62356 | 2025-12-12 03:29:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ef5b759-9ac7-36b0-abf1-0690cffebec9 | -6.95571 | -38.62323 | 2025-12-12 03:29:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 61a179a6-2755-35fc-952d-9119b3f7e806 | -6.11698 | -41.28809 | 2025-12-12 03:29:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5e8beee5-0d13-3581-abda-0548c2bc9546 | -3.97384 | -42.51043 | 2025-12-12 03:29:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1a51c85b-cc4c-3de5-b0db-8a86bd1cc2b8 | -7.46848 | -34.86557 | 2025-12-12 03:29:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2094273d-0d1a-3321-9693-0856d8ca3148 | -7.89537 | -38.44874 | 2025-12-12 03:29:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f4ee8d2c-5eb8-32f4-97ee-8a5b3c2318a7 | -3.95556 | -41.52646 | 2025-12-12 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e4d92a09-3744-3ebb-98fe-5764643343c2 | -8.09013 | -35.01547 | 2025-12-12 03:29:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| cbeccf00-5a4a-3916-a16d-a75f92d6ab44 | -7.33379 | -34.98238 | 2025-12-12 03:29:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 0bf1e406-db45-38a1-b23b-098898b8e2fe | -3.93644 | -40.73208 | 2025-12-12 03:29:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| efc6198f-7949-308b-9341-43d04862235f | -3.96122 | -41.52734 | 2025-12-12 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f3fd2cb1-3c02-3ec2-95a1-2fdee957b555 | -9.66931 | -36.0224 | 2025-12-12 03:29:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 069f5379-7b08-3ffd-8667-bf4fe142aecf | -7.31323 | -35.06512 | 2025-12-12 03:29:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 99403ce0-fbb6-30fa-b910-128bbbeb6016 | -4.99465 | -38.05846 | 2025-12-12 03:29:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6fff2bf6-51f9-3350-a9e1-1c7619349682 | -8.03791 | -43.10283 | 2025-12-12 03:29:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 637a131c-1121-38b4-999e-6b46f2fe5426 | -4.38967 | -43.63379 | 2025-12-12 03:29:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96728081-c349-3f9a-badd-066174a3eaae | -3.9531 | -41.52526 | 2025-12-12 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 921a0f55-d772-36a4-a5b9-c07ebb537331 | -9.03152 | -35.69594 | 2025-12-12 03:29:00 | NOAA-21 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1ec3d77b-15bf-3609-b23f-7c2fb9a5656c | -3.96753 | -41.52431 | 2025-12-12 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 98b15587-58f4-36e2-ad28-adc3af7238d9 | -3.96188 | -41.5234 | 2025-12-12 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2d44277b-d02c-3fa1-99fe-18779b15d870 | -7.47297 | -35.31002 | 2025-12-12 03:29:00 | NOAA-21 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b052fc5c-34ea-3a2b-87f0-acf8cae253ad | -3.96511 | -41.52305 | 2025-12-12 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| cc299a15-7bf6-3125-869e-60503f399667 | -9.40592 | -35.65055 | 2025-12-12 03:29:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d4469657-6906-3880-b2fc-7fd8064c1b40 | -3.30563 | -44.8675 | 2025-12-12 03:29:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c5fa80b-93e6-3d91-9380-f1cc2286d107 | -7.07088 | -35.21913 | 2025-12-12 03:29:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e00486f9-fc12-3b78-8583-1ee6c9674fc8 | -3.30443 | -44.86452 | 2025-12-12 03:29:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f744f7d-3487-335d-b5b2-a6e8bc3fe4c9 | -8.8334 | -35.44342 | 2025-12-12 03:29:00 | NOAA-21 | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9cb91338-bf9a-347a-ba7b-a4d5f9a13db5 | -9.40521 | -35.64946 | 2025-12-12 03:29:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0feada3c-cf3e-3cb5-b0ed-7b8d0ba43b5d | -9.40809 | -35.65411 | 2025-12-12 03:29:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0b5d280b-3b74-3195-8c58-ce0a53b67b0d | -5.16054 | -37.69433 | 2025-12-12 03:29:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1cc6f4da-9cd7-3f3f-8e47-a58d751488fd | -8.91845 | -37.94431 | 2025-12-12 03:29:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d6a1d485-df6d-3f59-a162-a2971e958199 | -6.95274 | -38.61415 | 2025-12-12 03:29:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ba8371c4-1d34-3e0b-9361-3235087a12be | -6.1188 | -41.27767 | 2025-12-12 03:29:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 349bd14c-16bb-3f14-8f5a-b0a2b3210441 | -3.30675 | -44.86084 | 2025-12-12 03:29:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82e4a5ef-fe0b-3660-9855-acae935544cc | -9.39801 | -36.02374 | 2025-12-12 03:29:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0b3fb90d-b9ce-3caa-b6e3-425ec146e497 | -7.46952 | -34.86496 | 2025-12-12 03:29:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
