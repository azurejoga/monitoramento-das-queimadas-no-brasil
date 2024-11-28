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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad6886a6-f036-3a95-853f-ef1da6d6c198 | -1.83731 | -44.79472 | 2024-11-28 04:23:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3853ca8-1fb9-3255-97fc-13be4fe8268b | -0.89834 | -51.65048 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f77ddf7-477d-3523-99a6-3e1e205fe6e8 | -2.10815 | -47.89375 | 2024-11-28 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb6c5aba-e2ec-34e1-a448-c717ff4aae2e | -1.08898 | -53.36949 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e14358d-3066-3607-8267-6f0a3b453534 | -1.68413 | -52.49631 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b82efb1-ee4c-3d90-94ef-9f3fa38d316c | -0.19837 | -51.41085 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63da46ce-2f4d-3083-a288-30aaf0e86ed8 | -8.50199 | -43.28178 | 2024-11-28 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e95706dc-db6d-3903-a236-a8b47ab0eef2 | -0.0241 | -49.64053 | 2024-11-28 04:23:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55fa75ab-3f79-356b-9dc1-4f46de1fe846 | -6.08711 | -48.04234 | 2024-11-28 04:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16cc1ef3-5464-3dba-b715-5e3cd8bc4a8b | -1.68965 | -52.49205 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d0331da7-9443-37cf-9375-5d1fac348219 | -6.16469 | -42.62477 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 63c567aa-68ad-3ed0-8771-25d9dc05ad09 | -1.27182 | -52.16288 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c5386bd-0b04-36c8-9b27-183c85b1b9c1 | -1.03897 | -52.42151 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79c4d75c-222b-353f-8f6a-6a01a32a8467 | -2.72068 | -46.26095 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50d8f205-96a0-318b-ae3d-b5caed4cd43d | -1.32898 | -51.95235 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7d2a1430-84eb-32ef-b370-ab5055ce0516 | -2.09815 | -46.57161 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5c1c05d-d3a7-3ad5-acbb-dacee94a25b7 | -1.1558 | -53.55857 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54e7a554-8cb9-3fb9-87e4-4d21f42d3664 | -1.53578 | -46.06469 | 2024-11-28 04:23:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f473c8c5-94a0-32a2-bfcd-28b49882bf4a | -2.56035 | -46.41869 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67d4cb3d-e709-33a9-b6c9-822ce763426d | -2.73998 | -46.1177 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 363284a7-012a-3370-8557-db9cee4be962 | -2.17392 | -47.13928 | 2024-11-28 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c43c90c-00a7-32ec-a13f-256a05898ea0 | -1.9885 | -45.90709 | 2024-11-28 04:23:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e87273a0-d7b7-3526-9a29-b32787fc8445 | -1.89986 | -50.58434 | 2024-11-28 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f294173-ca8e-3874-ba66-a1ecf637d5c6 | -1.7559 | -46.23909 | 2024-11-28 04:23:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c1a1e23-2142-3fd9-8bc5-3c18af6d7ac0 | -6.66735 | -47.87709 | 2024-11-28 04:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca10b729-c8ff-32be-bc54-b90ca3c4e506 | -7.69221 | -42.97489 | 2024-11-28 04:23:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7c7e1265-c410-3461-8bc8-b6ab25d2974a | -1.67405 | -52.43805 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99d08ce0-5285-3831-abdc-02f8bcd28d4f | -1.44148 | -52.60427 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79ef92c5-9a04-3a80-b2ee-b66286bf8445 | -8.12295 | -47.99018 | 2024-11-28 04:23:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9808f99e-53f9-3229-8cd8-5d4c39b3cea1 | -1.4696 | -51.54483 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ee12e04-574b-33e0-b8c0-b5a40c9d673c | -1.12197 | -48.33739 | 2024-11-28 04:23:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3a48d02-1825-32eb-99cc-22bae431da8d | -2.55247 | -46.33829 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8440787-90ca-3af0-8dea-b9e72981d7e0 | -1.57961 | -52.26317 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ed69a6e0-45e2-3b1f-b6e7-7a232aed3eae | -1.20732 | -51.74501 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 773879de-3032-3876-983e-2b93bfdae971 | -1.09998 | -54.14494 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09fc5197-904d-3d81-98a3-448ad0f1b4b1 | -7.83438 | -48.19341 | 2024-11-28 04:23:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60fb0a33-f03e-3e19-b598-ba53213172f7 | -2.71514 | -46.29588 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 410c39d3-236b-3961-8ea9-a40faefeb0b2 | -1.12831 | -53.59831 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ca96224-9112-3423-a9e8-76b48efaf9b6 | -6.16902 | -42.621 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 443550cd-1150-343f-b508-6951fcb7d3d1 | -2.56703 | -46.41975 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e120da52-3b56-39ee-bc5a-f8d0a02ee05e | -2.60001 | -46.8367 | 2024-11-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a7c7390e-2895-34e8-b693-6dd5b86b9492 | -1.35471 | -51.96712 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b042d95-2596-314f-b220-ee44ec3a6ef0 | -2.73721 | -46.11371 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cf78a6a-7b71-3222-a0a1-8b5a0d1760f2 | -1.3228 | -51.93217 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7141ee6e-a446-3bfa-8f55-c6816e5a4446 | -6.36683 | -45.69397 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16d8d759-c01d-3dca-a435-42911449d0d5 | -5.60226 | -49.70643 | 2024-11-28 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 810bbe5f-21cc-35a6-b7f3-e45f513a8cef | 0.94436 | -50.74121 | 2024-11-28 04:23:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a614be16-0948-3b44-b11b-14fd15c7e1eb | -2.60225 | -46.86648 | 2024-11-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42e3c1dc-66bf-3288-9a9b-9214722695bb | -1.57495 | -52.26242 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fba7e9ac-8ec1-33f6-a4d8-1fece6cc1a6f | -1.31145 | -51.74159 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcb56c99-ca75-33a6-a20d-1cb54e078f32 | -5.50158 | -47.17013 | 2024-11-28 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6d8d38e-7e45-3028-a6fd-6f5a794d758d | -5.6732 | -46.4981 | 2024-11-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53605bf2-e151-3340-b444-e2e7971db3dc | -1.38482 | -53.63724 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97f822f1-e398-30cc-829e-1813f0c4fae1 | -1.64028 | -52.43768 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fa99ba3-2c5b-3977-9f6c-5b5a23573774 | -2.68053 | -46.1511 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 945d6b6a-9aec-327f-80a8-0c661069697d | -1.71273 | -52.477 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45db2e8c-2682-3295-8f61-1c0d6384bf73 | -1.0886 | -54.04474 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2bdb42c-feee-3be5-9e8e-1f8eac2d52a9 | -1.35738 | -54.66008 | 2024-11-28 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72c9b66d-e1fb-39bc-a250-2d38b7b5dd6c | -4.52754 | -50.45845 | 2024-11-28 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a75e4072-0074-3b53-a941-f65e661d1f8c | -2.56424 | -46.41571 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81e148c2-9710-3cfd-8372-f539d08ab020 | -0.67916 | -52.37206 | 2024-11-28 04:23:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53e5fb97-301b-3002-aafb-e36c902abc47 | -2.57181 | -46.42801 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14e7331f-3c9d-369b-ba03-db1e37a76c6b | -2.70888 | -46.20908 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3ad2026-fbc2-3c0f-848c-95a0aeedd2bc | -1.27104 | -52.16773 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a24f0af-4c76-35a2-a81f-864e0cd61830 | -7.44218 | -46.63348 | 2024-11-28 04:23:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb956074-6180-3584-86be-4a7041babb55 | -0.02465 | -49.63707 | 2024-11-28 04:23:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 180f7c22-3f64-3c4b-acd2-2aa0df28a5de | -8.08421 | -47.06291 | 2024-11-28 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f16818e2-661e-38f9-916c-55a562dc07bd | -5.97446 | -45.35828 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5fe64d74-867e-3498-9ae0-708e775a305a | -6.10285 | -43.97074 | 2024-11-28 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a7762c5a-f885-3cdf-9df6-1d9eb14d6429 | -1.70537 | -45.82764 | 2024-11-28 04:23:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 20dce040-06e1-37ba-aa4a-c9cd7b04a23e | -1.15753 | -53.6799 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d692274e-4ad2-3eef-94e0-8e45a26362e3 | 0.04716 | -49.53531 | 2024-11-28 04:23:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b381d66b-e7ef-3290-aeeb-bfdc08981bbc | -2.67666 | -46.15407 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 736cb36b-47ea-32a8-aea4-4344dcc54595 | -1.34985 | -54.63699 | 2024-11-28 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 243a4b92-dceb-39d8-9168-c2627ac111f2 | -2.53311 | -47.32745 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a893dac3-46a2-3b3d-ae7e-e3e04d90daa5 | -1.06194 | -52.43041 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6815dd71-c994-3f42-9320-e1019b931fc0 | -1.04453 | -52.41714 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88984681-51a6-3892-a095-d2c557a631e8 | -7.94323 | -49.75714 | 2024-11-28 04:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0212d842-c113-3dbb-b345-4b0712d07ebd | -2.52995 | -47.32748 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b491b00-117e-3d2b-94c0-3c9db0d80763 | -0.3812 | -48.45734 | 2024-11-28 04:23:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 144d277d-4124-3058-92ed-d28d8b9dea12 | -2.09141 | -46.43962 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb72a63d-599e-3890-aeac-20349cf7a860 | -1.88854 | -45.46387 | 2024-11-28 04:23:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab4a44ef-4914-371e-8e34-c01d3377a00c | -8.12631 | -47.99072 | 2024-11-28 04:23:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8f1ed03-88df-3c42-9958-8a354cef06e2 | -5.98497 | -45.35635 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d479c38-280b-3726-94da-5cca8e9d7578 | -1.46681 | -52.35382 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a0d55ca-be2c-3fc9-aeab-28a97e37569e | -0.2725 | -51.62605 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d29959ab-e72a-3fa8-9151-37f918636eda | -0.15036 | -51.35064 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6977974f-2e2d-3bf5-a108-c048f78c149a | -2.48064 | -45.86747 | 2024-11-28 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0473a1b3-eda6-36f6-8d51-230002a611a4 | -4.87146 | -48.48709 | 2024-11-28 04:23:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbd8bed6-9b29-3351-8ac3-0a352787d797 | -2.56647 | -46.42327 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4367df6-5d18-3db0-9f8e-73adf17dd8b9 | -2.23755 | -48.52502 | 2024-11-28 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 684fc90f-ce45-3e4c-a764-793d347eadf9 | -5.7025 | -47.94706 | 2024-11-28 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01b1f953-215b-3c0c-862c-53146112b056 | -2.12655 | -46.41254 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f87f7d18-bb08-32e0-81c1-95c01b61fa6d | -6.86729 | -44.76176 | 2024-11-28 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e339aeed-8375-3ac4-8371-b005e85b202e | -2.55143 | -46.41008 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05524607-5b1c-3556-b351-af1d9d78a63d | -1.04287 | -51.74136 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6e3867ff-4129-3f08-8e9e-5f2541cdf028 | -2.72345 | -46.26496 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3655481-7f52-35d4-b882-657ab295ada9 | -2.03945 | -48.57292 | 2024-11-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb41a410-bc30-300e-8ad6-dc94d209784f | -6.23858 | -46.18734 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| beee6559-6fd4-3cad-94d8-81d6ad9d79eb | -1.15391 | -53.57032 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README46.md)
