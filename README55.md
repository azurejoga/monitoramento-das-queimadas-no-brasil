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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02f54fb4-79d5-3be0-a97d-46c529bf545c | -3.01931 | -47.80167 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7310925e-1414-3d07-822e-a7fa9c2b5f89 | -4.07024 | -46.82267 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d15125c-a0f4-3ecf-96be-f69cbfb0cfd5 | -3.22312 | -54.17881 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 714515d2-130a-306d-8804-d75bd1aba3b5 | -1.71377 | -52.49265 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 6442eed8-2a75-3850-aa30-a8b95b9a8180 | -3.09996 | -54.03267 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eac45f99-03d7-37d3-bf07-1d03d6235e9d | -1.59282 | -52.28738 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f2ccb35c-145c-3615-860b-504b4b30e955 | -3.45128 | -52.00723 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ba571fa-335e-3e77-94cf-03184908b7f3 | -4.22702 | -46.53619 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f05b331e-3df6-39fa-9675-5303bc9c6a4a | -1.31506 | -51.75375 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87c3202f-79b0-35d9-bbb7-4cb6fa60405a | -4.79165 | -46.12559 | 2024-11-29 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 47fae8af-1855-366b-aaa2-02c2c2a18f90 | -3.44514 | -50.00605 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4be1b40-a891-345f-a4de-6009283429a5 | -2.57745 | -50.00132 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8e621a1b-78b5-356d-9cf9-9a3788b6d5b0 | -2.17158 | -53.65754 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdeba91c-88a3-3eae-9e00-2305d504eaf0 | -1.94963 | -52.96519 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91382dbb-f589-3a05-a15a-05921fbeed18 | -2.46275 | -55.28105 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6087e321-ad4a-3d7f-b017-5b890e812abd | -2.98178 | -53.89404 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76aed917-5340-3bf0-a9ea-197b64fb7297 | -1.32665 | -52.79385 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f588b26-04df-3796-85b4-7ba3ac91d0ef | -3.14838 | -50.86182 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 557bafd1-6ea0-34d9-ac2c-09b09575f4d7 | -1.92012 | -52.89358 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39f02b2e-7b8a-33b8-a943-302ba8edb533 | -2.80501 | -53.04222 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08e01d3f-6cfc-3426-a135-379d60f5f074 | -1.40284 | -53.3969 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0943ac9-03e2-3701-b67c-92a0b4b883cc | -3.46918 | -50.53806 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1f67a843-c7d7-3192-bca3-c88c5b4845b3 | -1.08702 | -53.37193 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3dca02a3-298c-3df8-94a5-d98444142d3a | -2.01378 | -51.43261 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3f5d345-fd3b-3621-9944-f8b2009e5128 | -5.03707 | -43.62039 | 2024-11-29 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8fda9f79-1859-3635-974b-ec8657f71f5c | -1.35664 | -51.37196 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d889e77-8991-315b-b4e0-26557dc93c67 | -2.00957 | -51.19042 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c8ee2ca-2725-3874-bece-5d5da526484f | -1.59671 | -52.28439 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b7342ad7-741f-37ee-a1ab-e041ae457743 | -2.60895 | -54.27697 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f1519d8-4c60-3a66-bfae-610bc37e234a | -0.0547 | -50.82965 | 2024-11-29 04:57:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7808ec6e-04ac-3af0-b093-63b1c0890e16 | -2.52271 | -54.13253 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98f42af1-7bcb-3aeb-b45f-0867d8c0982c | -1.20809 | -51.74138 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55cec923-bb34-328b-b9ad-8a147ea331ec | -1.1403 | -53.61911 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52468201-a868-3276-ac33-43d8a12e2529 | -4.05114 | -48.33622 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4864c90f-62bf-3f7c-a648-bd8d9e1e3572 | -1.76317 | -53.63959 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6a96efd-d9d8-3140-9798-a14f5b941856 | -4.15861 | -53.47944 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fafe218-4940-3e8c-b3c6-7f3e69d7b2c9 | -0.2696 | -51.6345 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dee0d68e-7ea1-3764-92bf-5a470322d1ed | -2.4506 | -53.70152 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c226556-4cb3-31c8-a8ba-89b88b2ec5f7 | -2.64129 | -54.06968 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa5b5ed7-5892-3549-9971-72345c5d1a93 | -2.8579 | -54.03329 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca1b4b12-cec7-315f-85df-4281a2fc9bd5 | -2.88854 | -51.71962 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 592699d4-e3ae-3829-a280-7ef0fa879927 | -1.89445 | -50.95728 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 495fb7fc-143e-3b17-82ba-246d03614bf6 | -1.6933 | -52.62484 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b603cd5d-2ca4-3929-8f78-53f4b6b843d3 | -3.13874 | -54.26107 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4250e28d-3df9-3593-a8a0-2b7e4cfc8ac9 | -1.21871 | -53.55452 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bba2aab-0ca2-30c7-8b36-da50f6689950 | 1.67436 | -50.66447 | 2024-11-29 04:57:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a41e8a1-f0f9-350a-a666-1721d101e6f2 | 1.2126 | -55.95726 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ac2b29f-550e-3d3c-bc99-c8c015da0a34 | -1.28351 | -51.73414 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74f08018-de05-3110-b284-89a940a7761a | -1.32162 | -54.6354 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cbf4d378-2fdf-30e4-9558-ac397e64d6d5 | -1.12344 | -53.81377 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5518747-87a9-3b58-8a40-41f60fbd7d46 | -0.87904 | -53.68088 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4db1447-b066-384a-b881-614b68992b0d | -2.59557 | -54.08029 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59de3e35-b5c9-3221-b6b7-9ee959746df8 | -0.96074 | -51.6558 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| db5bca6e-9ab3-397b-bcb4-a1ab773f9506 | -3.53494 | -54.48993 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfe4abf8-811e-3734-82fc-a041265f4132 | -1.70882 | -52.63434 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 92c74618-e995-326f-a960-c5894f3364c3 | -2.78527 | -52.92922 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b138e6c-9630-36ea-a944-59c4960fd9f1 | -2.89214 | -51.58315 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4007950b-8d30-3aa3-a02c-830dcf8d53a8 | -1.25648 | -51.78561 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4645d582-9049-359e-ae52-edece915cef5 | -2.80353 | -51.58881 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91e2934e-d8ad-30c2-a82c-cc6f46459905 | -2.8631 | -45.54126 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 933c77d4-772f-30cb-9121-eb0e053f433d | -2.62308 | -51.80364 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdc0fa9a-72f5-3da5-b238-ecf3d36ded36 | -1.59392 | -52.28036 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8fab461d-4527-3c1b-ad29-ecc93669b3ec | -1.29009 | -51.36992 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 652f422c-f067-32ed-a49e-183998bc3c0c | -1.94301 | -52.96417 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a6a4dbc-a00b-3607-868a-24a2e5736f81 | -1.20078 | -51.74394 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e638ae2e-84e2-322d-973e-bf78de72e948 | -4.02585 | -48.89269 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c0093b7-7362-34c6-ad40-396645e959ca | -3.11383 | -53.26714 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9fb28909-4681-3a22-92e6-61e46df98c1c | -0.23757 | -51.59661 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46f21780-1b0e-3b9e-8160-6a746ae394c3 | -5.76391 | -43.39254 | 2024-11-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4eab905-6d95-3622-9d8b-9bd795aa5fe9 | -2.84448 | -46.86652 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3f131ff-eecf-305e-953b-edad1f9bf953 | -1.9033 | -48.51825 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28c2d362-4688-38f4-9be3-48d97c56d446 | -2.01016 | -51.18663 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d848c85c-afbe-332e-82dd-dacc5f862019 | -1.15826 | -53.5691 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30ea99e8-bb1e-32af-ad50-3fc345d56a07 | -3.49898 | -53.80668 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0afbd0d-31ec-3277-832f-fa0f59f7d0ba | 1.22807 | -55.93787 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9992e346-5713-31d9-a0b0-a8ec5787132a | -1.3339 | -51.42885 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2837d889-2eea-3117-9a4c-cd01f7280a9d | -1.7621 | -50.85461 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3308812-689a-3639-a5ad-15ef9f1aa722 | -2.6497 | -49.21586 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8217574-a357-3ece-a6c9-ae52a787fd2d | -2.13011 | -54.90069 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e39613ec-fda4-310c-85df-f6d46ec4b363 | -2.04387 | -54.69091 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 646fdd34-759f-30a8-b45f-ff3e76846439 | -1.64459 | -52.74087 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 204b3d01-7009-3b8e-b8db-66b554cbdbe1 | -2.38235 | -53.6803 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac1abda0-ca31-3962-8f6f-38b286af8b87 | -2.23482 | -53.68916 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb50381b-7573-3761-9aea-a47ab94b2730 | -1.11493 | -53.21479 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8844c57f-79dc-3e97-bf0d-e7d7f500632c | -0.56878 | -51.69865 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d6118ef-ce88-33c0-9c9c-1c48b71cc620 | -4.01719 | -46.99764 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c6004d6-e22f-38a3-a1cb-a1c599171178 | -2.05836 | -51.16587 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27ca0a78-9dd6-3942-ae3f-5bfd153714ba | -2.8336 | -54.01545 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02b238fd-0526-3ca6-b7fb-9ee1a3f96d48 | -2.64978 | -48.78777 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 940eeb25-88e4-3e54-8133-e0a45e5f32bc | -1.5846 | -53.84417 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2df01b9f-2c49-3ffa-93bf-fc16502b5fec | -1.4619 | -52.69155 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2fc3487-d431-3cdc-a716-70b5a2268068 | -3.26805 | -54.10814 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb4a3fb1-abdf-3f53-a5fb-d4614ae51f3f | -2.73072 | -54.12937 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45b1b24c-26d0-3d27-9052-4e347a56356c | -3.11135 | -53.98158 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b1168a2-7b5d-3540-bb6b-4993abb80962 | -2.32396 | -50.68571 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6695aba-019f-38d2-b9fe-087f4b54b4e8 | -3.37701 | -50.11459 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b491e574-0811-3cb9-b41b-59719d0a2163 | -2.74074 | -54.15211 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1e8e64cc-3e02-3972-8e6f-e0f2c42a65e9 | -1.09202 | -53.38323 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2dff2bc1-8ec9-33ec-a641-14833d97a234 | -1.26266 | -51.74611 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1cf60aa-4ac0-3c53-b73f-31677a9346fc | -2.69789 | -51.6828 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README56.md)
