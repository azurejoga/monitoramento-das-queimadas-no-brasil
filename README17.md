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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d4ca743-65de-3e38-94d7-952f8524f7f0 | -3.27079 | -45.56077 | 2025-12-12 04:21:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b010625b-2ffa-321b-9f93-38b2dfa6b365 | -3.19135 | -45.09739 | 2025-12-12 04:21:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef10ba44-4a79-3b39-b7f7-edefb4cda5ce | -2.30068 | -45.66278 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e5b1d4c-25b6-3d1a-9a5f-0049be8662c6 | -4.11214 | -47.30075 | 2025-12-12 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 006d0d5e-7341-3da9-be90-78badf73b6c7 | -6.79504 | -47.59844 | 2025-12-12 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc2da194-62ef-3f85-989e-2d1e35e0e352 | -6.51936 | -55.04394 | 2025-12-12 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 167ece80-aeba-32a3-969a-c44eb0388404 | -3.82438 | -51.14158 | 2025-12-12 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 37452fe4-4168-3442-adb7-7fd64823cf2e | -2.09406 | -47.39311 | 2025-12-12 04:21:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 061c676e-3fac-3e94-bb3a-f2d82eda9fb4 | -3.30692 | -42.53365 | 2025-12-12 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 727bacf0-47f5-3f1e-b3be-86e56ba87920 | -1.11499 | -53.69534 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2945a6f3-cc7a-3dcc-b6f8-8f17e4f05709 | -4.93683 | -43.96611 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6dd331cf-5062-3770-8ed2-297a5646b318 | -1.49041 | -45.6429 | 2025-12-12 04:21:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79a31195-c0e4-333c-9a5b-1463dc0f0898 | -3.02343 | -49.0545 | 2025-12-12 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1453b3b-ef26-3fd6-ae9f-42f9341f6b0b | -2.90981 | -51.93985 | 2025-12-12 04:21:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c868e828-d372-346c-b5fa-f7fb6a9e76c6 | -8.02506 | -43.10067 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 21d33bfc-4c18-3601-a035-efc5a136a88f | -2.49968 | -51.80891 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b00f63cc-c1a6-357b-8d1b-0b4ac3cb7437 | -6.11414 | -41.29067 | 2025-12-12 04:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb34c9d0-8caf-358e-a329-00034f0b16de | -5.9827 | -44.59414 | 2025-12-12 04:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89b74afd-d635-3308-9a10-9ad14133a7ae | -2.92204 | -48.05408 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a383f167-e612-3281-b4f0-45f13ba37bba | -2.88898 | -47.80357 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e7f875e-1c9e-30e9-a6ff-c6f4210b32ec | -2.02029 | -46.3848 | 2025-12-12 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15b10965-5417-3690-9634-25a0a8018092 | -6.60696 | -47.61761 | 2025-12-12 04:21:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6c7a9a0-e7e6-37fb-b33a-7df185f954fd | -4.63374 | -44.40242 | 2025-12-12 04:21:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3afe4f1d-2312-32b8-ade5-42cb5b87da4d | -1.84452 | -46.39536 | 2025-12-12 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a817f7c-74d9-3bcb-86ac-9ab9453edfa2 | -2.33801 | -45.78126 | 2025-12-12 04:21:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb4c1b1c-50af-3070-9649-e9538130e29c | -2.22965 | -45.40207 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 979c45e1-0ed4-3383-b966-49095107ef38 | -3.0123 | -52.83182 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88aa040a-80d7-3644-b9f2-72133ff58545 | -2.68208 | -51.9207 | 2025-12-12 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36d56f02-b76e-3213-a5de-6e91bec74b4e | -6.51248 | -55.03868 | 2025-12-12 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99c914ab-92fa-3e2a-9625-a5e08d4461a4 | -3.04622 | -53.01532 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 654a1f33-b3ef-327a-9732-468e022c8991 | -8.04343 | -43.09572 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7eef4104-e52b-3f55-8a3c-9f295f576e7f | -3.17095 | -52.87897 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0d1b73b-f416-3824-9acb-84b7e5f6544a | -2.49567 | -51.8026 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| af0f97d7-6fcf-3204-868f-af3be2eb31ca | -3.01746 | -52.83295 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a612e5f-bc05-3ab1-abd4-afd3b3b701db | -2.37955 | -45.65235 | 2025-12-12 04:21:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3deff53c-0efc-3e3b-a3f0-63f740ca4457 | -3.01904 | -52.82365 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06eee532-b805-312a-baf1-8f2b5bf44a63 | -3.3103 | -42.53417 | 2025-12-12 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6986bc8c-1e82-3d3b-8693-febad870dde5 | -2.90489 | -51.93911 | 2025-12-12 04:21:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fb626ae5-26f2-3b05-8b43-3691f530cdb8 | -3.34953 | -46.85992 | 2025-12-12 04:21:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b8e1574-fd5e-3778-a442-2b68b363a070 | -4.3039 | -43.21622 | 2025-12-12 04:21:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 730155f2-79f6-3ad3-bf28-f2a2b176c80b | -3.95205 | -41.52658 | 2025-12-12 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 38418391-b512-34d1-9955-47c6ec4c28e3 | -3.23903 | -47.47013 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22866e10-8aca-31a2-aab9-4c75b4fd15e7 | -8.04284 | -43.09951 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 98121429-b757-348b-bd16-a4fa8837ee4f | -4.76882 | -43.60842 | 2025-12-12 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cf36630-2b51-3f09-ad01-558804ff6e01 | -1.50464 | -45.88649 | 2025-12-12 04:21:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c478c459-4e7a-3bf1-99e4-ad57be22d3f1 | -2.74582 | -52.97732 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a036254f-6ca1-38bc-b08d-5ddbecf4dea4 | -4.99596 | -38.05644 | 2025-12-12 04:21:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6c9bc020-e262-349a-bb33-2f327862dff6 | -6.1191 | -41.28268 | 2025-12-12 04:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3317a26d-b2fa-3027-b55c-7c97af438ff5 | -3.85886 | -45.3036 | 2025-12-12 04:21:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17e438a0-f9a6-3fe1-95fc-469ecaadecc6 | -8.03596 | -43.09848 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 54d2946e-3884-394c-86ef-c0248e2d8f9b | -8.04167 | -43.10707 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d397250f-88aa-3a39-af7b-f79e0854bef5 | -0.97088 | -53.18404 | 2025-12-12 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1949f234-0b9d-3660-8506-aab3e9849b7e | -3.1275 | -54.18485 | 2025-12-12 04:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 757143f7-185f-3b5e-9ec0-170c2a6d2f8f | -4.73647 | -43.07555 | 2025-12-12 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 87923ea5-182f-3311-93c8-27eb216c7125 | -4.38862 | -43.62774 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f8a276a-5567-3c30-b1ac-7ff7741cf13d | -3.39444 | -42.10776 | 2025-12-12 04:21:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| bcd264b2-0af5-329a-9cff-5f3f0261c088 | -3.65009 | -47.15194 | 2025-12-12 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9809ec65-e191-3453-9300-44c268861853 | -6.23701 | -43.96967 | 2025-12-12 04:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12d438f4-97a8-3d8e-b661-b6a122ded586 | -1.84804 | -46.39592 | 2025-12-12 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dd34c81-b870-3093-a51b-c4f5db3332fb | -3.62423 | -45.39011 | 2025-12-12 04:21:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f249fef7-5b35-3c93-9fc1-9e499559fe6e | -6.86985 | -48.84021 | 2025-12-12 04:21:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d8a5f36-cce5-364f-8724-a223e83e1f6e | -4.39472 | -43.63224 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8afca86d-e4e2-30b5-8322-1c7bb7259492 | -6.56946 | -47.24929 | 2025-12-12 04:21:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b9c8281-1ac8-311b-af5b-caaec9c52bd9 | -2.26519 | -45.73238 | 2025-12-12 04:21:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e22a0e92-6de1-33f6-91f0-c012614447db | -3.1819 | -48.03051 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a5a90f3-ebf0-3cdc-9d95-69c4875d6741 | -2.77574 | -45.56838 | 2025-12-12 04:21:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 600af0d7-0dc8-3ed2-938a-c6f5cfd98aed | -3.65366 | -47.1525 | 2025-12-12 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5046fda4-1af7-3230-a2b2-d6c3556fa9e9 | -2.21556 | -45.40354 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a543c94-ab16-32fc-bf0c-6b8c5a86211e | -3.43705 | -41.65197 | 2025-12-12 04:21:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 99eafa53-1c40-34e5-ac7f-db389e1c86ee | -4.7445 | -49.79947 | 2025-12-12 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61ce1997-f61b-34c5-8449-70ff13dd011d | -3.65943 | -44.69692 | 2025-12-12 04:21:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36f47fcf-7613-39de-82b0-84bb2ad2ae9a | -2.65788 | -51.64394 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b9b9089-28ba-3bb4-ad70-dd010ebd6990 | -3.23407 | -42.07977 | 2025-12-12 04:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ad8a306-2971-3027-a530-a20d311f8d7e | -3.01158 | -52.83191 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ba47803-411a-3d94-80a0-085226a63a2b | -4.99531 | -38.06083 | 2025-12-12 04:21:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10a45e52-8af3-3164-a0da-c5a26b8eedec | -1.02537 | -53.74271 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f80757f-b847-333d-9e99-672ea1332a8e | -3.66589 | -45.78872 | 2025-12-12 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db850bcf-9401-3fbc-b8eb-1772ee1f0065 | -4.37894 | -43.62622 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 088311d9-6fe0-3959-ad33-0ff5ca007560 | -4.3872 | -46.67039 | 2025-12-12 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53a73cfc-0612-3801-a682-79bd55647676 | -8.03765 | -43.11032 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cd0a341d-10c8-3670-b981-236d414cb151 | -1.79407 | -45.76213 | 2025-12-12 04:21:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e107740-3f42-3e3c-90a8-301fcb0061fb | -3.43356 | -41.65142 | 2025-12-12 04:21:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 02f574e4-828d-324c-8b73-55ecce643a65 | -2.25542 | -53.76144 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbbc4c46-c5d6-3cc6-8a45-384e31aad3a1 | -3.06138 | -52.39547 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bd2f81c-5f46-3ebb-b59b-4da4147c6d3b | -2.83656 | -46.73786 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d8fe6c7-6215-39f9-abde-e9da8ba38da0 | -2.66319 | -47.78556 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3ef53bc0-4853-35a4-971d-b5dfa823f12c | -3.27153 | -45.70872 | 2025-12-12 04:21:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2568d899-7b15-3f21-b22e-ea2f1a808d59 | -8.02448 | -43.10443 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b5dcdb92-975c-34d9-9913-99ded2c7c882 | -3.17147 | -52.87589 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86fae4b1-e256-32df-bfab-cce00a22ec75 | -8.03998 | -43.09522 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17337d86-1a51-3c49-b87f-7952e13a049d | -3.76829 | -47.16158 | 2025-12-12 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b379c8a-66e5-3e0f-b050-0ceab8a12e62 | -3.42392 | -42.27906 | 2025-12-12 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dee6f4e4-ce5a-3237-9f5c-7bbd8b83c2ca | -3.12253 | -54.17966 | 2025-12-12 04:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44dc60ab-8c80-3a2b-8b13-406d8791cdc6 | -2.09115 | -53.42105 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7980371-2a46-3ff5-bc32-ae9ce0cdc043 | -3.26741 | -45.56024 | 2025-12-12 04:21:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a8109a7-9243-318e-afdf-35a865209eae | -3.38388 | -47.19314 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91f54593-92d4-3769-aef2-27e2578c7a65 | -3.95991 | -41.52316 | 2025-12-12 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c1726857-dc20-3f09-962e-5fac9badd990 | -3.39502 | -42.10405 | 2025-12-12 04:21:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 96f78b0e-ca52-3c21-ae82-648179a72760 | -3.68891 | -52.00845 | 2025-12-12 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e98ad5f8-fa01-3efc-8e2c-d02c42671e86 | -6.02705 | -43.70373 | 2025-12-12 04:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
