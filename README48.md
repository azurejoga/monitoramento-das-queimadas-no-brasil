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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f39babbb-9094-3374-90ad-0c1b27d75a68 | -2.96396 | -48.72526 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79878dd2-d38a-35e1-bf9b-6cb8da853b8b | -3.12656 | -51.10556 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 074dc7be-ffde-3732-abc2-86c9f691b49b | -2.74223 | -54.1224 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0da1ff9e-86bf-3611-bbfd-767dd1cc3693 | -3.24154 | -50.44683 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba893e10-056e-3481-86ed-268467bfda96 | -4.18461 | -49.77842 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0b704626-0687-3cd5-b7ba-f2d1e6c90ee6 | -1.46725 | -54.38016 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e17b61f-d33a-31a8-83c9-a225435a4e01 | -2.75744 | -53.22337 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c0e299f-e4e8-37aa-bc47-0f8420c70b89 | -2.06524 | -53.26889 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d345e934-60e0-3abe-89c9-3a6fa655253a | -3.03791 | -53.2748 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e248379f-4b58-3087-9497-d8c433829af1 | -3.68905 | -51.34225 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e148007-dd40-398d-9b21-4a42d5a1e400 | -3.15188 | -50.20704 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bdc3e39-0e79-364f-8c9c-f402af147bad | -2.87484 | -51.30453 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0e69bd4-f4d8-3447-8e79-82287474c216 | -3.1428 | -51.20439 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5322a994-9ee4-3e27-a7b4-1269205b5599 | -2.83582 | -52.91029 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec27a981-8e70-3c9c-a4e1-74d14768aaf1 | -3.03128 | -54.08415 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38aa1cfb-05a6-35d6-9bcc-56a0e8043862 | -5.20594 | -46.18594 | 2024-11-07 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f3eabbf-08a9-3884-a8bf-bc8febf6d354 | -3.64255 | -50.14098 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ba68c7e-6de2-3f65-ac7b-f4663fcb5e21 | -2.93534 | -51.05809 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7e33dad-f145-3bae-982f-52e853a4d80e | -1.54005 | -52.01009 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2b4eb2f-604f-314c-aa22-7f7a78f73148 | -2.84525 | -51.36022 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 902ecc27-4427-3f39-a2d3-b1bcf3905e63 | -1.14824 | -53.74389 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 260ecbfb-6afa-3ce1-a3d9-39d03541acd0 | -3.02888 | -53.26017 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3a6780f-1afd-3986-8f85-9a144ae1acd1 | -2.23949 | -53.67063 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4f3f922d-69ff-3072-b4a8-4ecd9a94ea8d | -2.17521 | -46.44365 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19b2f47c-ec11-38f2-8ce2-c4d42a30f2a3 | -3.34999 | -50.25758 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 875b0eb0-2943-3e17-ab79-b7bb995ca2f0 | -3.24407 | -50.4601 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8affaf84-1b83-342d-9ddf-30ac85082ab8 | -1.17697 | -53.62809 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45afada4-4b55-37e5-8832-ea38337a1177 | -2.81482 | -52.94781 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 37fee912-9c79-36c6-a4a6-59a6f03de1b5 | -1.60461 | -54.64448 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91a918d8-744a-304a-bd4a-1e8d98273236 | -2.82595 | -52.94953 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdda9e6a-54f0-31ba-9af5-e4627d22e1de | -2.80793 | -51.49544 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d053d72f-b6d1-350d-a654-57e37289b2f2 | -1.52709 | -52.14464 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 340fd9ba-44fe-31ca-9c74-c85dd67aea21 | -3.22893 | -50.37897 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0fdda9f7-d637-3e60-8c3a-f8125716cef5 | -2.16838 | -46.45041 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 32f4bd22-f49c-3e4d-bf82-01d9edd6c327 | -3.83294 | -51.90964 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b030e6ca-8dd3-31f6-8b68-5a958f17eb44 | 0.6184 | -51.84753 | 2024-11-07 05:10:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b96bf90-25ff-39b3-895a-9fe6ec637ea5 | -2.19099 | -53.2532 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b75f821f-676c-3501-829f-5d6bef80cd20 | -2.8417 | -51.35595 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c8364b5-4865-3010-9d1f-0bb732a4a13b | -2.85322 | -51.77587 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2060091d-0bae-3bdf-b556-cf9ab4b7fabf | -2.82977 | -52.90013 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34d1678a-3f92-3050-b440-18f3fb068b38 | -1.12249 | -53.60771 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1368d5cd-4f70-34fd-a430-37220a60f8f2 | -1.41154 | -54.49272 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de48f2f1-fb6c-3318-b0ca-c887f14f8f23 | -3.03092 | -54.20384 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e03cdb7b-7d51-3d11-ac3a-d1f61f7bbfe7 | -2.93508 | -52.54063 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33aec3f4-9ce2-3280-b5eb-def0a8274a4e | -2.95028 | -53.28484 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f5b6f11-bae3-356c-9c3c-ee29dd599cc8 | -3.02742 | -54.2033 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 885b711b-0627-34e7-8fb0-4e5611e1ee64 | -3.70361 | -51.38663 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf5bb50e-2d93-30d9-9927-5b941e28cf91 | -1.68415 | -51.26479 | 2024-11-07 05:10:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec1c4851-4a7b-31d8-8e73-94a1e9ec99df | -2.79401 | -54.02602 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 745109ca-88a6-3084-bf48-d4917c3c1f32 | -3.72618 | -52.27166 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7aa236b4-6d00-3774-a04c-26c2a0041c6a | -2.68113 | -51.82922 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a53ff38b-a574-3800-86cb-ca95a6ceb374 | -2.85722 | -51.77649 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be520153-8f67-3b16-8100-80a383182bcb | -2.67638 | -51.83371 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f479f3f-73dd-3331-bc9d-12627efc544c | -4.34507 | -48.62744 | 2024-11-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13bc483c-6ec1-3d4e-a5eb-24f927d943f6 | -2.58197 | -51.92278 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17385c91-e875-34db-8bd3-c907b8467955 | -3.24739 | -53.39955 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afea6825-685c-3b87-ba3b-31ef946d2d7d | -2.16064 | -53.68833 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6031c905-a89c-37d8-94b9-ece51a9652b4 | -4.67281 | -46.33899 | 2024-11-07 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34a0d86b-c4e8-3e78-9eef-1031d9ec7d54 | -3.8071 | -52.16103 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0510168-37ef-35af-bc1e-c976b10324e8 | -2.06162 | -53.26833 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9366ae7-f9a0-3288-a333-56c55644ea2f | -2.71533 | -52.96187 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67eefb02-02f0-35fd-8890-0e89b9eb01f6 | -2.81316 | -52.93385 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 402d056b-9721-38c3-aaeb-6da207b74342 | -4.05073 | -49.26634 | 2024-11-07 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8904729-84de-32f1-9bf3-e75926da0781 | -3.22337 | -50.44826 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d271f661-6aa5-303b-9fe7-d3371553a9a6 | -2.73096 | -51.73269 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8661c09-45d4-3c26-b57f-3ffd8eff5285 | -3.24092 | -50.45102 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 9f1410c8-dcda-3c37-a82a-cf25fceaf1f1 | -2.92866 | -51.0452 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3125f05a-1a82-35dc-8581-e839f26ebcf1 | -3.04457 | -53.28024 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e022a236-d3e8-37b1-b398-fe53a0a24f74 | -4.35014 | -48.62818 | 2024-11-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c4da841-69df-3c64-ad11-9e663d645aaa | -1.52798 | -52.16409 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3c07873-1d21-387b-baa9-b6f6d180d5a9 | -2.55266 | -54.01177 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f0e2333-b6b9-308e-9c2b-2cb60031f244 | -3.1128 | -51.29236 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f701a762-4ab2-33e1-a3c2-dcaf979fb0d8 | -3.66754 | -50.2508 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| a54dd950-c741-37ec-9862-c75f29b17b36 | -1.15218 | -53.64878 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| baa4dedd-f9f3-3cd4-96ae-ffbd92519600 | -1.6748 | -53.80753 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7848473a-acfd-34aa-9dde-794ad7b53a29 | -3.63803 | -50.14032 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 545cea14-e0c5-3581-81c1-dec486a2e179 | -2.73814 | -54.12574 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db1ca0b7-2ecc-3a75-9ae2-4dfb4bbf3f32 | -2.93058 | -52.54466 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c51f95f-6f37-368c-8ff0-57cf87c8e231 | 0.69497 | -51.44098 | 2024-11-07 05:10:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c1a5653b-15f7-353f-b56d-4d07fbfd871a | -1.19933 | -53.62331 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfae9fc3-e97c-3d2c-b375-a4a73bddb8f0 | -3.45228 | -52.00818 | 2024-11-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39e2fe1f-f7c6-3f85-a9f1-b93841a18aa3 | -3.45126 | -51.11086 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f52f58b-0b18-3a6b-b3bc-21800979e626 | 1.35298 | -50.94172 | 2024-11-07 05:10:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6b9777d-c592-3a3e-9519-ed8c7b077a53 | -1.4013 | -54.1021 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fb3e937-0aca-3865-a62f-c8c4718c507f | -1.53957 | -54.25355 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6de625e0-8070-3de2-92fa-c781109b3b3a | -0.11603 | -51.39453 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1ffd0bf-1044-3825-a51e-fa5d0dbd3072 | -2.79085 | -51.35935 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f47a673-3acf-371b-b785-9c7e316069b3 | -4.22153 | -49.67425 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 651e5da9-3d87-32db-b770-6c71665cc0e4 | -2.60483 | -51.76939 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 679d9580-0c46-33dd-8e16-bf394a14d17a | -3.17612 | -50.5813 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4061bbd-8e15-3560-b6f1-0fed4dd382fd | -1.15586 | -53.74091 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74de4b68-432e-3766-b61d-7a52cba77096 | -3.45114 | -50.37177 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 05f7ea72-7fe7-3494-9a09-ab788f487cca | -3.58757 | -50.234 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 382da5ab-2601-3645-bf09-94c8c14cf592 | -2.75873 | -53.21495 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88c32ec9-8287-381f-8ae6-1c45b8f4d253 | -0.84493 | -52.84571 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7f82d5a-e009-3fab-ad6a-a1cba4fc65a3 | -0.8838 | -47.30341 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 090fe3e0-fea0-34ee-8e3f-069fd10268ae | -2.93576 | -52.53607 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9505236-e823-3c2a-ae63-c5b26166e673 | -1.20726 | -54.20066 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d24be68b-e0f8-3d4a-b3ff-3b1da7f091dd | -2.82089 | -52.95773 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c608e9a8-7630-3856-9dfc-87c57f5a030e | -2.91494 | -51.05101 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README49.md)
