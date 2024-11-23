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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebf35f90-6a0d-3715-91db-ec0970211664 | -2.7149 | -46.2713 | 2024-11-23 03:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 49.0 |
| bc51d5b6-b8d4-38ab-a439-416e96e1ed0c | -2.7719 | -45.936 | 2024-11-23 03:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 68c6a202-acfa-3bd0-87a4-2f9af9de200b | -1.7175 | -52.7184 | 2024-11-23 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 70a23e47-0b18-3679-bcfd-f2eb62abaa19 | -3.2584 | -53.8204 | 2024-11-23 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ee49a03c-fd0b-3b5f-b6df-03490c26881e | -2.7534 | -45.9366 | 2024-11-23 03:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 4fe72b79-bc64-39bd-81ae-7ad23c90a22b | -4.53071 | -42.91022 | 2024-11-23 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 505cd57e-c041-3ebe-ae0d-35e4230c7950 | -3.14552 | -44.48482 | 2024-11-23 03:29:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4577cf93-ba6d-3ccd-83b7-9c113c864cf4 | -4.57081 | -37.98544 | 2024-11-23 03:29:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 77c09407-1be6-307b-baf9-ea2e07750a01 | -4.01206 | -44.33818 | 2024-11-23 03:29:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 748d2b55-15f0-398c-ad91-7b0864182691 | -4.1218 | -43.23514 | 2024-11-23 03:29:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e279b2e-e8f7-3ea0-a1c7-35abb823e8fa | -4.53595 | -42.91582 | 2024-11-23 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 3cdf4147-c14e-331b-8fa2-a51b5739be6d | -3.95412 | -41.49438 | 2024-11-23 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5bd302f-80dd-39bc-8308-f375deba1940 | -4.4199 | -44.11589 | 2024-11-23 03:29:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eb65f959-bce0-3e10-93b1-86ac45a5debe | -3.60699 | -41.67676 | 2024-11-23 03:29:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 11425470-b8f7-3838-aca0-af297ade92d0 | -4.42092 | -44.11012 | 2024-11-23 03:29:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1e9b1a2c-f8a6-3aab-b7ee-fc98c208d4bc | -3.26396 | -45.44006 | 2024-11-23 03:29:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10ecf438-a351-3e98-a29a-37414db7327e | -2.82141 | -45.16119 | 2024-11-23 03:29:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d5f50e54-ba1d-3047-8121-ab5515b39389 | -4.11171 | -42.47554 | 2024-11-23 03:29:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e85a97b8-4d8b-30c9-87b1-1f58fb15d9d5 | -4.41339 | -44.11473 | 2024-11-23 03:29:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0269c89a-c576-3da4-9bdd-314bc968ee3e | -4.12099 | -43.23997 | 2024-11-23 03:29:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dcd70d11-28df-3577-a717-6d7c37d7a593 | -3.16617 | -44.40657 | 2024-11-23 03:29:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6faf441a-5c56-3e71-b9ac-f669e7627fe0 | -2.82848 | -45.16246 | 2024-11-23 03:29:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e80261d3-e0c5-32d8-9ac1-a2ce95cc4a60 | -4.1058 | -42.47452 | 2024-11-23 03:29:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8ee0c23c-d1f0-3370-b807-cb0ce3f504ae | -4.57014 | -38.48165 | 2024-11-23 03:29:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 21aa230b-d896-3d08-90e5-998805a639a1 | -2.82451 | -45.16142 | 2024-11-23 03:29:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 23e1c045-b3f0-3c59-8494-124eb0a456b2 | -4.52993 | -42.91468 | 2024-11-23 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 4e86b101-e587-3c59-89b9-4a4773f17e07 | -4.12816 | -43.22825 | 2024-11-23 03:29:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d6e930f7-a2ba-3baa-896a-577b7af9c218 | -4.03074 | -41.79975 | 2024-11-23 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c2fb4c27-11c8-3838-a99f-e42232cce3f1 | -4.53518 | -42.9203 | 2024-11-23 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 59b0be33-35fd-3793-a870-6a59c3d85a4a | -3.38881 | -45.29143 | 2024-11-23 03:29:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f383761d-b0a6-3626-93d3-5338a197d478 | -4.10653 | -42.47018 | 2024-11-23 03:29:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8e75c75d-490f-3154-86c6-18c9cbe606bf | -4.56941 | -38.48611 | 2024-11-23 03:29:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c376d572-5fbf-39e4-ac05-b11f50e8d5ed | -4.12803 | -43.23599 | 2024-11-23 03:29:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d8a82dd-3c7b-3061-b663-b413e9d700d4 | -4.41886 | -44.12175 | 2024-11-23 03:29:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 372946e4-30fe-3ee1-9694-fec896ceac23 | -4.38908 | -40.76162 | 2024-11-23 03:29:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 94692484-0cf7-33e7-b328-86d8c2d3dace | -4.02755 | -41.80354 | 2024-11-23 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c4e66b9d-952f-3a86-8ee2-e137734937f3 | -2.81743 | -45.16021 | 2024-11-23 03:29:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b00a3f37-267f-366d-90a9-819c30a3589c | -3.60199 | -41.67185 | 2024-11-23 03:29:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aef73d12-24d7-342f-8259-e1b26ab076b7 | -4.12733 | -43.23298 | 2024-11-23 03:29:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29ff2a9b-0d29-3241-9710-7dc471339ced | -4.42639 | -44.1171 | 2024-11-23 03:29:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16013eba-81fb-3d38-8b35-9c338cc6641d | -4.12109 | -43.23213 | 2024-11-23 03:29:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b70949c1-e548-3344-8c96-01800835673f | -4.12026 | -43.23684 | 2024-11-23 03:29:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b25bac1-ec92-3f41-9320-cccf6c076c29 | -4.0282 | -41.79967 | 2024-11-23 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5795e3a1-c613-320a-909b-ee1538a4c6c1 | -4.03007 | -41.8036 | 2024-11-23 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6740961c-dd8d-3829-8587-2cf288546de2 | -4.56923 | -37.98535 | 2024-11-23 03:29:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11521484-c1df-3721-a1fc-05cfe1151bad | -4.11244 | -42.47121 | 2024-11-23 03:29:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f60813cc-3c4f-3e44-ba7a-2ebeea061be0 | -4.12259 | -43.23044 | 2024-11-23 03:29:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7242b02a-d9e5-348c-b909-0ccd965b9e18 | -3.1435 | -44.48649 | 2024-11-23 03:29:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f273f11a-f535-3043-8a30-60d04838b9f8 | -3.60134 | -41.67576 | 2024-11-23 03:29:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2faab71d-2b1b-3f8d-8f01-03f09738987e | -4.12651 | -43.23764 | 2024-11-23 03:29:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f86f922b-37d2-316f-a9d9-2fe5ed448ccb | -4.42191 | -44.1045 | 2024-11-23 03:29:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e82a59d-1fbc-3662-b8c5-4e91551429b3 | -3.27112 | -45.44122 | 2024-11-23 03:29:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98f2d81c-dcc9-3a0a-b328-8160242e1b70 | -4.12194 | -43.2273 | 2024-11-23 03:29:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4fbf1777-9ff2-3e0a-9c72-b71726f1e791 | -4.12882 | -43.23133 | 2024-11-23 03:29:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c2a45a3b-a218-38d1-8eb3-4f156acd8468 | -5.55359 | -38.00401 | 2024-11-23 03:29:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c45e62bd-1564-37db-a51e-4a32fd88e64d | -4.52916 | -42.91913 | 2024-11-23 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| c1baa480-aa6b-304e-8b6b-478aa67ba466 | -4.38862 | -40.76432 | 2024-11-23 03:29:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 94af7de3-cc95-3aa4-9f49-0e007c426881 | -4.6086 | -46.478 | 2024-11-23 03:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 705152ca-9711-36cf-9ba9-0f0d26f189f7 | -3.5159 | -53.8132 | 2024-11-23 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| eca584cd-15f8-33e6-9cae-c72885b39120 | -4.6085 | -46.5002 | 2024-11-23 03:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 284.6 |
| 65a9d93f-3462-379a-9591-3ea613c6cf18 | -4.6083 | -46.5223 | 2024-11-23 03:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 943765d3-b5c2-3c8b-8891-b33a296be10f | -2.7719 | -45.936 | 2024-11-23 03:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 8739adb6-3549-3c82-a2fe-3497166aaf5b | -1.7359 | -52.7181 | 2024-11-23 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 736241a3-e732-3d2a-94b8-39dfaecfa235 | -2.7534 | -45.9366 | 2024-11-23 03:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1d49d44f-dbf3-3bc2-a8bb-b95d8e00f255 | -2.772 | -45.9137 | 2024-11-23 03:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4faf5b81-21c6-3bb5-8794-7346fe2b5a14 | -1.7359 | -52.7385 | 2024-11-23 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| d5179c7e-f00f-326d-a851-e48748471ccb | -4.6271 | -46.4992 | 2024-11-23 03:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 44a16b20-6f98-3a25-bbb1-671b406865e3 | -3.2768 | -53.8199 | 2024-11-23 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 06f9f26b-3e17-3f71-9497-937c1e8f6570 | -1.6075 | -52.5977 | 2024-11-23 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 507c7e48-936e-3cfa-bdd3-2d631978738a | -4.5216 | -42.9078 | 2024-11-23 03:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 743d8a5e-4cf4-3fe7-816b-11698702a48a | -5.2902 | -44.86137 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72d36093-a6b2-38ad-84b2-0f1d15969bbf | -10.1401 | -36.19184 | 2024-11-23 03:32:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5250ec92-ef1a-38d0-b454-c77f07fd2e6c | -9.13131 | -43.10701 | 2024-11-23 03:32:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84da68a5-b0ee-311a-a288-4d5bb5e23ece | -8.34483 | -37.28861 | 2024-11-23 03:32:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f81e8c6e-82f3-3a24-b295-b0f0a49347aa | -4.65984 | -45.67547 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c65680c5-dc43-3438-87bd-0438099a76ef | -6.14208 | -38.20472 | 2024-11-23 03:32:00 | NOAA-21 | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e54fdfa2-f0a3-3f88-bb4d-91f80488f4b5 | -8.15089 | -38.24326 | 2024-11-23 03:32:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b57a72fb-232a-34c3-a128-6c45bf44fcc9 | -7.24393 | -35.14984 | 2024-11-23 03:32:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 61e5aa1b-10b4-368f-b819-c311f86571c0 | -8.52499 | -37.06162 | 2024-11-23 03:32:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da44edec-a054-3d75-8a91-093d57606a98 | -6.03695 | -42.23007 | 2024-11-23 03:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a15fcecc-4fb4-3683-8652-bd9b297a5a50 | -7.831 | -37.39593 | 2024-11-23 03:32:00 | NOAA-21 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9e3c036-d310-3750-bd32-beb1dbab1ea9 | -7.68998 | -42.99062 | 2024-11-23 03:32:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3467fbae-b03d-32b1-bbd3-4dc6289125ef | -4.67552 | -45.6698 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d4034a3a-2e04-39af-8903-ae1366c164d2 | -5.2235 | -44.90976 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94c987ed-47a1-3dc2-97f6-f6b4f79836b4 | -6.62999 | -37.9824 | 2024-11-23 03:32:00 | NOAA-21 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 46d56f5c-cc6a-370d-ab62-584383da7a45 | -7.58466 | -40.00465 | 2024-11-23 03:32:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| af6bd1ef-4af0-36d8-bd87-2d7e18739940 | -5.22563 | -44.91143 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a90c3a9-24fe-3401-8d32-2ebe21d227ae | -5.58422 | -45.21033 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80f9cf55-1a05-3d8b-9381-b2eef9a6e2f0 | -5.4634 | -43.24412 | 2024-11-23 03:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7d4374a-b15d-3a02-bdb4-f2d78ba4d374 | -6.18003 | -45.45489 | 2024-11-23 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1909be7b-da4c-37bc-9bb3-0e7f25e5498c | -7.69073 | -42.98643 | 2024-11-23 03:32:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| be030028-b34b-3193-a5ac-8e55b2419f90 | -9.72452 | -37.03027 | 2024-11-23 03:32:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 6.9 |
| afeaf3d7-37d8-3262-a15c-8a1c4b5df8c7 | -7.95717 | -37.90614 | 2024-11-23 03:32:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a31989c2-5c9f-3dcd-b08d-3d5b27e66d92 | -9.81975 | -39.15136 | 2024-11-23 03:32:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2718e1e-c73f-344e-b73b-5ae9bc1b1eba | -5.10606 | -43.15972 | 2024-11-23 03:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e12efdfb-8f47-3800-a372-939d84fba171 | -6.56271 | -39.76536 | 2024-11-23 03:32:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 12e7b703-03ba-3ccc-98f5-4687dcf245e8 | -8.71397 | -44.00709 | 2024-11-23 03:32:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6ce332c-7c54-399e-8434-5a735b064ca4 | -7.01499 | -39.22382 | 2024-11-23 03:32:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 76be8557-6625-3fe3-9a87-5f827e2d1d77 | -9.13061 | -43.11076 | 2024-11-23 03:32:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5c308dd0-92f4-3c30-9b55-74689f3c2d3c | -4.72026 | -45.50257 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README20.md)
