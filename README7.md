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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54235ad7-8ade-3f5c-a651-e6c78c90b934 | -6.94174 | -43.53653 | 2024-12-23 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 784b0ba3-ef70-3e4f-8857-9fe4ef86049a | -1.63262 | -45.85069 | 2024-12-23 04:08:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6807e846-9c46-39d0-9290-f51228de1663 | -4.17726 | -43.65647 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73c04c2b-9f6b-3b08-8ec3-7f9ee2150292 | -5.93233 | -45.48639 | 2024-12-23 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c8ce206-48f7-33ed-b000-b54289cae976 | -1.6367 | -45.85131 | 2024-12-23 04:08:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48711af7-8d89-3b8d-9ce0-08d00aa99026 | -5.24561 | -36.18486 | 2024-12-23 04:08:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d2535d0f-5155-340b-a3e8-1d2c42d6830a | -4.08736 | -46.80545 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10ab4443-506d-338b-8569-c753083de526 | -7.91997 | -35.19559 | 2024-12-23 04:08:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 04708371-825a-3c37-992e-d6b9cc2d0c4f | -2.94097 | -45.73728 | 2024-12-23 04:08:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee018b57-921a-39e4-a629-a40343ea28a4 | -5.24594 | -36.18506 | 2024-12-23 04:08:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8b86d4fc-c00a-3c81-81f9-e49e3092735f | -1.82833 | -45.72449 | 2024-12-23 04:08:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9ac542e-9874-3fdf-90f8-0506c1cd91ec | -5.38538 | -37.72528 | 2024-12-23 04:08:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4220003e-dd16-31d3-9e76-444b4f4c7e53 | -4.01469 | -47.06333 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2cd76771-9881-3fb9-9301-16920b444ff2 | -4.91983 | -44.05302 | 2024-12-23 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ad0c7db-55b3-37b8-8d32-3683f1939cfe | -2.42865 | -48.59468 | 2024-12-23 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 590339ca-5a24-3768-abec-dcfa5b8eae6f | -1.63376 | -45.84348 | 2024-12-23 04:08:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b8020c1-a59d-3fbe-8d74-14b3ad6f61b1 | -3.90393 | -46.99703 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0aa8b574-d6ba-3fd0-9b93-680c477bc849 | -3.99372 | -46.7398 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13ee9892-1863-3888-a5a8-fb32dcb9944f | -4.14688 | -43.66758 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 43f21cd1-c8b2-372f-b54c-6bd913ce5517 | -2.5627 | -45.56442 | 2024-12-23 04:08:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a610789c-0264-3d02-8afd-673dff910384 | -7.38964 | -35.2673 | 2024-12-23 04:08:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 64154d0d-acfa-3107-bf3e-82da31fdd630 | -4.01178 | -47.05452 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a16e855-f922-3bbf-8dff-d2b64d4414a3 | -6.90606 | -43.54209 | 2024-12-23 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 01e6793d-1b29-3327-8f1d-29ca8ae38c6a | -4.00396 | -46.99646 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb390fc8-f599-39e9-9d21-6a236bffaafe | -4.0596 | -47.08311 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f2ec7ad-cc58-39a0-a5bf-746311d5de44 | -2.63948 | -45.68713 | 2024-12-23 04:08:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8e52ad9-ee5f-383e-b74d-78ccdd3abd2b | -3.92199 | -46.3587 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87ae6dd9-19b6-30cf-bb44-1bd2d56687d8 | -2.40558 | -53.74432 | 2024-12-23 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dcd78fe0-cb30-3f41-8049-82df08dc352d | -3.01801 | -46.9977 | 2024-12-23 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0826431-933a-3772-8298-4c1aed6c50d4 | -2.40662 | -53.73814 | 2024-12-23 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fcc03a0d-ba3d-337e-9ee0-bf31cc62dd9a | -4.00821 | -46.99711 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94ae3587-cbff-35f8-9575-2e201bed6cbb | -6.93272 | -43.52758 | 2024-12-23 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eb297c4a-9506-321e-8b95-034f8c5a7a04 | -3.64164 | -40.48016 | 2024-12-23 04:08:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 214215df-f9f0-3976-bfa7-761d07a8a7e3 | -4.32633 | -48.94667 | 2024-12-23 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 680f527c-e059-3553-b1b4-6c27a983d863 | -4.17909 | -43.64491 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12cc6d4d-4cd8-3947-b0bc-72751a2836a0 | -1.66738 | -52.05936 | 2024-12-23 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e67315a1-30a6-308e-92d3-7aecd2a37dab | -3.09868 | -54.55011 | 2024-12-23 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dd1f8669-0778-3a67-93b3-057a2775f90a | -3.79708 | -46.7203 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c0dd1e41-4184-3f67-b9c5-be2ed1bfc383 | -5.35285 | -46.22261 | 2024-12-23 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b214b31-b920-355a-8bc7-18b21cd376e5 | -3.00551 | -48.12533 | 2024-12-23 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 706bc112-41d8-3376-bd83-17b78b8fa61f | -4.3252 | -48.94832 | 2024-12-23 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf1be51b-999b-35fb-90d7-6e127cbc8dd2 | -4.03245 | -50.05518 | 2024-12-23 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d4708c5-7ea1-3948-b0e1-8bd92157c08e | -4.01535 | -47.05934 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ec61f63-f42f-331b-bf3b-c7869244c97d | -4.05766 | -47.0951 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aedb76c9-07a4-3eed-b6f5-d635f9617523 | -3.35628 | -47.10856 | 2024-12-23 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6518516-a493-3ad6-b969-f34622add928 | -3.77599 | -46.8245 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8c774ff-0519-3635-87aa-f4f4d10a8a26 | -2.40455 | -53.75049 | 2024-12-23 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8fedf991-834a-3d79-856f-788b97fb9ad1 | -2.46627 | -45.80877 | 2024-12-23 04:08:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 914f59ac-0678-35d2-bf00-b4f5e3c8d716 | -4.03155 | -50.05894 | 2024-12-23 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da13ced2-9baa-3fd2-982a-0f223ee2bb17 | -5.4532 | -44.81102 | 2024-12-23 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f2bcd3d-7be7-3422-b55f-7f334fc63da5 | -4.17848 | -43.64876 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5a4c3e3-ba7d-3500-80e3-597e306ce6c2 | -4.37607 | -44.00369 | 2024-12-23 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1c120b42-3217-3ea1-a2fe-cae67527c323 | -2.73985 | -46.87205 | 2024-12-23 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ce7f33b-33ff-3421-9685-48053639685f | -6.00647 | -45.41769 | 2024-12-23 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf0b1b2d-0b35-3883-bc82-026bb1f552ac | -5.24613 | -36.1812 | 2024-12-23 04:08:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e226b662-02a6-3a6e-b057-c1443e31502d | -2.44305 | -51.79159 | 2024-12-23 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87200e95-2fd4-3954-ab54-f78e46b4fc7f | -3.9353 | -46.35397 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92faaf9a-b0fc-305e-ae2e-c5462dbdce1b | -2.70961 | -42.72205 | 2024-12-23 04:08:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09dc8625-3edc-3514-aafc-8628aa8a2c83 | -4.10697 | -46.81695 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 648100af-cbd8-31b6-b597-74da54acc7ef | -3.38647 | -40.45789 | 2024-12-23 04:08:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9a717aa8-f2c7-3d5b-a33c-fea9cabaf3cd | -4.48084 | -45.43023 | 2024-12-23 04:08:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28818b15-f1ba-3594-ac18-8a3eb1b05bc2 | -5.24649 | -36.18142 | 2024-12-23 04:08:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 5a1da3e1-4a59-355e-980b-b48925a5aed6 | -3.64495 | -40.48067 | 2024-12-23 04:08:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf3f597f-6fa4-3f40-90da-3be9cbdd796e | -4.15222 | -43.65653 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4633aa34-60ae-351a-af8b-1e57971d9763 | -3.98953 | -46.73922 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07ccb6ca-c612-3d0a-a575-b691708a45ad | -4.04677 | -47.02766 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f93e80d-91f4-3412-bbe6-3951317e6e27 | -4.1803 | -43.63723 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b5d9564-4ec7-3c3d-adb8-d4204329d084 | -4.1475 | -43.66371 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5c511d72-de79-3da2-a4c2-730b81d845b0 | -6.9429 | -43.52919 | 2024-12-23 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5bdcb1c-f7cf-3f29-8373-b6912f7126a4 | -4.04316 | -46.40921 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6eeb655e-3512-36e2-b181-5e36a3a2bc84 | -2.46226 | -45.80814 | 2024-12-23 04:08:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a431130-c5cc-3e4a-972f-1438cce25f54 | -4.18257 | -43.64547 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63c27b7c-8f89-33fb-9ed8-45925083e722 | -2.50251 | -49.06548 | 2024-12-23 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d68af40b-a4df-3e80-99f1-269d4f1f9ced | -1.93908 | -45.63427 | 2024-12-23 04:08:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbf403f4-da8b-3044-aefc-05a93d4ae203 | -6.05381 | -39.43642 | 2024-12-23 04:08:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bd45562d-949a-3488-b728-19d4840f141d | -4.17787 | -43.65262 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcfa50b3-d848-33fb-9587-9200b09d4e95 | -3.73027 | -43.43821 | 2024-12-23 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 693049bc-ee6d-3fde-b19e-e6cb99852508 | -3.93006 | -46.36049 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1601bd9-7ef6-3694-8d3f-d4a1c28567f2 | -4.04256 | -46.4129 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fbd0476-b19d-3fa8-93f2-7575e94a0c54 | -4.0281 | -46.79261 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8c458cb-c4d9-38c5-b004-2c83914f6bbc | -0.20575 | -51.60096 | 2024-12-23 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4656f84f-3eca-3d8e-90ab-4806cdbe3b85 | -4.18196 | -43.64931 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbe35723-f917-3cc3-aee9-cb7b1dbcee3b | -3.0063 | -48.12046 | 2024-12-23 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8284c6b4-555e-38b0-9014-de5c50d8b516 | -4.15284 | -43.65268 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7e7f9fc9-f561-3f2a-aa0e-cfa26ff9b1a8 | -2.2663 | -46.39579 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e3b9dbc7-8a5f-3b27-97e5-423b25bf3e0e | -2.71302 | -42.72258 | 2024-12-23 04:08:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c02355cc-25b5-3cbe-a0aa-de8bdfcfa258 | -4.15571 | -43.65707 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2ebc389-0e6b-3ce7-826c-f10056fa4a1a | -11.76002 | -37.58673 | 2024-12-23 04:10:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2f67276c-0e2f-3ea2-895a-fb9f36443da4 | -12.47618 | -44.60375 | 2024-12-23 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 25b85048-1c9d-32a5-aef9-72744524b1e2 | -10.69661 | -37.04855 | 2024-12-23 04:10:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3c42140b-5c4e-380d-a452-d968a8c1b6b3 | -15.96004 | -43.01888 | 2024-12-23 04:10:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32523c87-effc-3a29-a122-6ba5f6de25b7 | -11.96622 | -44.23994 | 2024-12-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c81817e-6b86-38e9-97be-a8c64b493365 | -12.87384 | -43.75845 | 2024-12-23 04:10:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8419519e-bd5a-3fda-aaa7-7d2b0cf548a1 | -12.85104 | -43.81652 | 2024-12-23 04:10:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a5cbba5-dc98-3b16-bfe0-b0d88615ee9b | -9.09345 | -40.88522 | 2024-12-23 04:10:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4d280b62-edb4-3a26-b8cc-41cb23e474d9 | -10.43106 | -44.88599 | 2024-12-23 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f912765-ec63-35cc-bd4c-09ba5db8e069 | -9.18793 | -43.12121 | 2024-12-23 04:10:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be56cd63-65a0-3cd6-9e55-0a4185244604 | -11.96957 | -44.24049 | 2024-12-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4184d5ce-3772-3b6d-b94e-4dc55fd55929 | -10.4276 | -44.88541 | 2024-12-23 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c1d349f-b94c-3f93-b188-5d9f2061ecb1 | -10.20719 | -42.43694 | 2024-12-23 04:10:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README8.md)
