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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 409b21cc-7c53-3684-a63e-c78517ee81f7 | -0.4126 | -52.04768 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6d07902-b808-3fdf-8d65-fce96c440093 | -0.41205 | -52.05116 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd8505a6-4151-31c5-b8c6-b24f51645150 | -0.40983 | -52.0437 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 164d9ddb-beb7-3757-9822-0602060f7b8a | -0.40538 | -52.02881 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ac2217ad-5339-3de3-a12a-11c2ceb666b4 | -0.40261 | -52.02483 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bf42174-6ba3-36a2-9fc9-e44abb745a65 | -0.39929 | -52.02432 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 910aa3a6-9887-39e6-9472-358121a61f03 | -0.39598 | -52.02381 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d73cb7b3-60cb-3265-b859-25600704d279 | -0.12729 | -51.56708 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 265d9bb6-db2d-3346-ab21-b87a676722ad | -0.12674 | -51.5706 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 480b4615-0e90-323a-9877-ae75c8360d54 | -0.10795 | -51.64697 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9cc39be-8164-31ee-b8c6-02404063bd98 | -0.10462 | -51.64645 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 562cbeca-e4fa-31c0-a3ef-ca57fde49d5e | -0.10297 | -51.65699 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32bd152b-25cc-3809-8c93-808b14c87be6 | -0.89931 | -51.74452 | 2024-10-12 04:55:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94309940-8574-3940-bff5-223338268bf4 | -0.89875 | -51.74804 | 2024-10-12 04:55:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe2ab065-c7fd-3a0f-8794-cc667b86718a | -0.89597 | -51.744 | 2024-10-12 04:55:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ca8aa5a-b44f-3550-9889-194f3dae8777 | -0.89541 | -51.74753 | 2024-10-12 04:55:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c8063d99-d236-379b-8b76-c031c5363ea2 | 0.83129 | -60.57624 | 2024-10-12 04:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d0d17fb-d671-3438-a145-ed676d955b50 | 0.94822 | -50.20642 | 2024-10-12 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a0cfc51-445d-38f8-828a-c34f6a7bf23e | 0.75234 | -50.79286 | 2024-10-12 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0ddf056-1a5d-32ed-bb90-d15d7cca336b | 3.52242 | -51.46055 | 2024-10-12 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6d6880e3-fb71-390e-9c03-9b093e6d8dbc | 3.44543 | -51.46976 | 2024-10-12 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9a6e239-e8cb-313f-8377-ed4b2181fb7e | 3.38019 | -51.3351 | 2024-10-12 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e68c5744-e234-33f6-a8da-4593ed9e9caf | 3.34215 | -51.31268 | 2024-10-12 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6662684f-bdea-3080-b95a-618c0ab6307e | 3.30683 | -51.34656 | 2024-10-12 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52a96ebb-2034-3192-8825-a0de02a561c6 | 3.30352 | -51.34707 | 2024-10-12 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46bf9d20-3adc-36d3-b29e-5541bed193f2 | 2.82393 | -51.11283 | 2024-10-12 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a40bfd74-91c1-3ff8-b888-5f86873fde6f | 2.58489 | -51.66885 | 2024-10-12 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26a07e69-7d7c-38c7-8218-a84e4acec4e2 | -1.63745 | -46.25648 | 2024-10-12 04:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be4f9726-7fc2-31dd-8283-5ce7c616f0d2 | -1.44743 | -48.15044 | 2024-10-12 04:55:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22fb5588-5cf8-3781-8029-4d23d0074b1a | -1.44343 | -48.14981 | 2024-10-12 04:55:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 250d78e8-3d96-30b4-8a4c-ea7f69d13cc5 | -1.05728 | -48.00082 | 2024-10-12 04:55:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c4deb10-19db-3146-8f65-5cd9a46c5e62 | -0.25574 | -48.60214 | 2024-10-12 04:55:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb6b170f-cc8f-3b46-ab0d-ded3f1e17184 | -0.08058 | -51.38905 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8fbae46-fc9a-3d76-a158-80f64eaa2780 | -2.8254 | -51.3401 | 2024-10-12 04:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 0b27955f-aebd-3294-9c96-2d6d4ddcbe8f | -2.7701 | -51.3622 | 2024-10-12 04:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 2e3ba187-0987-3b3d-8dc5-cb3777e02979 | -2.7885 | -51.3618 | 2024-10-12 04:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 3dafb8d5-45a1-3091-b67f-ba295a53461c | -2.807 | -51.3406 | 2024-10-12 04:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| a2e834c3-c3ff-3fca-99ad-ff828d56c01f | -3.1426 | -50.3724 | 2024-10-12 04:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 57e655c2-5e52-3e80-81ea-7bb90d68c699 | -3.1427 | -50.3514 | 2024-10-12 04:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 00e59c21-f973-385e-ae1c-4624a0b477ea | -3.161 | -50.3718 | 2024-10-12 04:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 91330b9b-780b-3e4b-8a9f-45f0d01e0b14 | -3.1611 | -50.3508 | 2024-10-12 04:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| e03af707-82b8-3231-b8c2-a4acc4a19cb3 | -3.6978 | -50.1225 | 2024-10-12 04:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| da5a8962-b6c0-37bb-ab55-0e3f1a00ee39 | -3.7845 | -51.3104 | 2024-10-12 04:55:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| cba18c2e-7d04-30ae-8552-c42d4cd84cbc | -3.9394 | -46.445 | 2024-10-12 04:55:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 946ca934-0526-3ac6-9607-14e66ec6ab27 | -3.9396 | -46.4229 | 2024-10-12 04:55:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 26dba08b-e4a8-3319-9f63-39b414633e13 | -6.747 | -59.3259 | 2024-10-12 04:55:43 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 83cd4563-f9cc-3041-94eb-6145eba3aee2 | -7.8717 | -54.6814 | 2024-10-12 04:55:49 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 08d065b5-bd09-3654-9988-551b221e8a41 | -7.8529 | -54.7027 | 2024-10-12 04:55:49 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 39fc4444-71ca-3fb3-8cb8-766c03454386 | -7.8715 | -54.7016 | 2024-10-12 04:55:49 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 3f31f881-c399-3422-bb77-b685cb13dc16 | -7.8713 | -54.7217 | 2024-10-12 04:55:49 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 853e8568-2c50-3cc9-bce2-890dda1639ec | -7.8901 | -54.7004 | 2024-10-12 04:55:49 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| b2c10dc2-adfa-3d23-a21f-fb3b2b595495 | -14.23563 | -39.74964 | 2024-10-12 04:57:00 | AQUA_M-M | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 963b9828-71d0-3965-9d44-52bc467cc164 | -14.23423 | -39.75959 | 2024-10-12 04:57:00 | AQUA_M-M | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| d41ec455-dcdb-3246-b107-43fb61f56834 | -13.47072 | -40.83952 | 2024-10-12 04:57:00 | AQUA_M-M | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e41839a0-d1f6-3992-9a1f-05d8618b74d6 | -12.78594 | -44.86477 | 2024-10-12 04:57:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 08e79e74-c66e-342b-8db7-2a034bbf991a | -10.96483 | -44.64758 | 2024-10-12 04:57:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1e4f9615-bce6-3e3a-bfec-d91f71f661aa | -10.96374 | -44.6402 | 2024-10-12 04:57:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f7d495cc-7504-3990-9166-339bb4908684 | -10.96168 | -44.65266 | 2024-10-12 04:57:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| ded5cf42-1ff0-3503-b90a-83e310ed8a52 | -10.9545 | -44.64585 | 2024-10-12 04:57:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 4ec947ec-c669-379a-971b-777e7d0b4d40 | -10.94417 | -44.64412 | 2024-10-12 04:57:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0c707c9d-2006-3ae2-8b4b-d70f08a2a798 | -9.32254 | -45.8997 | 2024-10-12 04:57:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bf37c1ee-2986-303e-9f8e-51dc0a9af8ba | -11.33501 | -50.89872 | 2024-10-12 04:57:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 41.7 |
| c6cfcbe6-b072-309b-9313-759c2f8a222b | -11.32478 | -50.9018 | 2024-10-12 04:57:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| c58dbe9f-7ea4-3793-bd19-7b7e3c525c2e | -10.47469 | -47.66479 | 2024-10-12 04:57:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 39339bcc-c4fe-363f-bc61-e05afed575ff | -1.89898 | -52.4894 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c11f6240-fec2-38d4-ad38-11007e8f1217 | -1.89844 | -52.49286 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b460908-5916-33da-9358-00c95282c834 | -1.71629 | -52.5036 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49140d83-cf78-3b7f-bf29-2e363e26ff27 | -1.71576 | -52.50706 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 704bbc26-52b6-33e3-8f0e-57638fe9c590 | -1.71414 | -52.51741 | 2024-10-12 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20bff5c6-fc96-3ab5-939c-3da6b54b2642 | -1.34408 | -52.79385 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09d52f27-07f5-387b-b6a2-fe3ce15709f2 | -1.59776 | -53.34585 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8bd28653-c946-3b7f-9d2f-76f7598b677e | -1.59447 | -53.34534 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 810f2452-1e30-3b51-a669-8f21939cb029 | -1.59117 | -53.34483 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 790810b9-f137-3740-8e3e-bae78dd0561b | -3.53847 | -53.51522 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16b86c6a-7492-3791-b8d6-a37a1e9c5cf7 | -2.84029 | -53.3203 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47f0ddc9-5a22-344b-8b2e-3f63882139cd | -2.68037 | -53.34454 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2eb6cfcb-1c4d-3840-8bc2-03ed9cb8acaf | -2.67707 | -53.34403 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41b62af8-9441-343d-9d5f-e533af301765 | -2.67653 | -53.34746 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98f1d0a2-d19e-3ad7-8a91-e9c0c9d9db58 | -2.676 | -53.35088 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55d7c3b7-e6c1-3669-9d1e-35276ae6d6e7 | -2.67431 | -53.3401 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40f8ae16-642c-38d1-8fed-975624fc4cd7 | -2.67378 | -53.34352 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1aab3a40-900e-36b8-a432-42c0590e7202 | -2.67324 | -53.34695 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 729d221b-1ba7-36d6-8fef-bd76bd49cea7 | -2.67048 | -53.34301 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59cc6138-4ffc-34ea-a87c-7d842e0c65e8 | -2.66994 | -53.34644 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c123698-7437-3327-a173-2c8c78b69fdf | -2.6694 | -53.34986 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84fa85f8-6a84-386a-b2bd-2f7da0d99180 | -2.66665 | -53.34592 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19568a3f-51fb-39f8-a2ee-31e0e88dd35c | -2.66611 | -53.34935 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdadecbc-b1f0-3d73-b9a5-c6ee17078953 | -2.66557 | -53.35278 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79feb64d-4062-32bc-99ff-1f3885adb000 | -2.66335 | -53.34542 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 399cc84c-7663-3917-92f8-d918e3ba8ea4 | -2.66281 | -53.34884 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7c6967c-c934-3834-a383-66549db347ae | -2.66227 | -53.35226 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bd58e55-ea46-35b2-8a0c-7fdcd67342b8 | -2.66174 | -53.35569 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd1ace71-8627-3fbe-8602-2b66eb694599 | -2.66005 | -53.34491 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82f2b960-93d0-3723-bf73-d26b83a95f52 | -2.65952 | -53.34833 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c63ff25f-0e02-335d-8022-e0cc8d7cae0a | -2.65898 | -53.35175 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ae4065a-d762-3cfd-ade9-2caa84ee85ff | -2.65844 | -53.35518 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b78f094f-eee8-3875-8aed-7b73c29439d5 | -2.65622 | -53.34782 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9d94403-6898-3cdd-963c-5a2da6a9577a | -2.65568 | -53.35124 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8a07e49-fc0b-3465-9684-5042adca1894 | -2.65292 | -53.34731 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13562733-6dcb-3a6f-a2c3-8343ab69518b | -2.65239 | -53.35073 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README58.md)
