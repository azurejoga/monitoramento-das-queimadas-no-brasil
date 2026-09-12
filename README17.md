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
| c23897e9-2b8f-3fa2-90f7-5ba2c47b8b0c | -3.81325 | -55.89111 | 2026-09-12 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d57990ac-7be7-33b6-acb3-3ca041ad0e33 | -2.94304 | -50.40609 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45d085ad-966f-3d67-adf7-5ef56bb0d91c | -2.22773 | -51.93145 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84ca59d4-b211-3742-80d8-43ee6180df46 | -2.97125 | -50.41471 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9a93e566-1b5c-3f83-b80d-0aee8387ebd9 | -2.93894 | -50.47802 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cf55d83-776d-3fa5-ab4e-5704aa41f4bb | -3.37776 | -50.75896 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d19a99c-2c5b-3318-903b-22cf38169578 | -3.24839 | -47.24979 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f91c22ff-a353-30e4-996b-cb01b401da24 | -2.94551 | -50.48333 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdb9c7a2-1c75-3881-b959-d26b2d3df531 | -2.94894 | -50.41549 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 98cf7670-c7ae-3f3a-a28e-f39152fbfa3e | -2.9719 | -50.41057 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c058868e-b5ef-3239-8f04-f1abc751478b | -2.71794 | -57.61794 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a0ce6fca-51a5-3e85-b1d1-756f4c24ef8a | -2.9421 | -50.38894 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e108899-2510-3f0d-8997-a9745cb969e4 | -0.16548 | -50.40736 | 2026-09-12 04:32:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa14a5c6-1748-3386-86c4-85da9e3e6ede | -1.84186 | -46.14698 | 2026-09-12 04:32:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b55d2534-b37c-3357-918f-7bf4df9bf9a4 | -5.61141 | -44.84945 | 2026-09-12 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ccda741a-3a36-3fa8-8837-a02259ff94dc | -5.47777 | -45.13025 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f9c49af-08a8-3028-8032-a82e8eb30651 | -4.92752 | -47.54139 | 2026-09-12 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 82b5166d-a568-321a-be46-eaa36773d9f2 | -3.36612 | -50.76152 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 022ebe87-d53d-36a3-8737-26c4a6555b97 | -4.91851 | -40.65907 | 2026-09-12 04:32:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9717eb4f-8d01-30b7-a9cf-7951223a7f63 | -2.72097 | -57.63523 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0d2502f6-2804-3db4-b871-5747c870e31d | -3.73731 | -40.42911 | 2026-09-12 04:32:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 821eb2f9-8810-35bc-b2dc-338246b10d96 | -3.54577 | -48.17581 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 892bd067-d19d-3e99-9e06-b79e84759e07 | 2.51021 | -50.85065 | 2026-09-12 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e43ba5d7-de6e-3cfb-b9e6-7960fee1b958 | -2.30134 | -48.58507 | 2026-09-12 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 853272af-24ce-367a-a7b2-96037ba3f566 | -3.95295 | -47.61719 | 2026-09-12 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ddb30893-6e7e-3cc7-b084-539cbc84fe83 | -4.36283 | -47.78019 | 2026-09-12 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 252ad15e-d01c-3b8a-a58c-c20e35c97cdc | -5.12382 | -41.08962 | 2026-09-12 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c95fc36f-695d-36fd-9e00-14a9af9532dc | -3.53803 | -48.18175 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bcb8a481-1562-382e-8594-413142499c0b | -2.9621 | -50.37935 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| afd04805-1ec8-3d02-8f3f-da95f5514e0d | -5.62917 | -43.54885 | 2026-09-12 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 209ea822-a147-305c-94cb-fd7bda583e8a | -3.16136 | -48.60916 | 2026-09-12 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d8da0b7c-0408-3ec4-ba84-2fd5c57f4259 | -4.30066 | -49.11036 | 2026-09-12 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a401145a-181f-3b70-95b3-80381895245d | -6.27365 | -41.95333 | 2026-09-12 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e956a38b-a0f3-3039-a458-60edfc795301 | -5.77242 | -45.09916 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 65b69119-8c76-3b48-818d-29e2168d54ad | -2.96962 | -50.40169 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| d748c3b7-1939-399c-b510-2d9c18596304 | -3.86208 | -49.22038 | 2026-09-12 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71b80ffa-e414-3e50-8027-46ada396be25 | -2.97256 | -50.40641 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| ffda382e-c1ea-3db3-b0b7-98dedd56865c | -3.97477 | -53.44086 | 2026-09-12 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94d01625-f571-3fd8-9ddb-7ef11ef55848 | -2.78614 | -47.61676 | 2026-09-12 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4ae0c3f-3a85-3869-b0ce-a8e37d266d7a | -2.25975 | -47.0036 | 2026-09-12 04:32:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ccf5800-fa6f-3181-9848-4749acbcd683 | -2.96504 | -50.38404 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9afdbad3-1da6-330b-b7cf-547ef59ba03c | -4.08375 | -43.35016 | 2026-09-12 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7bde540-f495-3400-ad14-1ffe2e208152 | -2.9439 | -50.47021 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b9465da-bb52-392b-87c5-935b09b804c6 | -5.51409 | -47.44242 | 2026-09-12 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3c653c6-42ab-3d57-b45d-5d17d496da3a | -3.38142 | -50.75954 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0c243c8-f723-3b1d-9b36-bf67858ccf89 | -2.95717 | -50.38706 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcbde001-50f3-3ea5-a8fb-5de0c671a69b | -4.92287 | -49.2404 | 2026-09-12 04:32:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0315f145-a300-3731-b761-03683d3da28a | -2.95255 | -50.41604 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e6f76a76-471a-31ad-a7f1-e1af0b764a8e | 2.51367 | -50.8466 | 2026-09-12 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f55c1a09-444c-3939-b20b-d8b7cded3911 | -3.09608 | -51.28934 | 2026-09-12 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4be1f299-5829-31ed-87d7-5f07cbcfa182 | -5.00441 | -42.77761 | 2026-09-12 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef28af6b-d6a2-3639-9334-8a3a3ef801ae | -2.72674 | -57.63717 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7cc50b42-6634-33ad-aed1-77dc2cc50bd0 | -2.73702 | -57.64624 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 678055bc-8d99-3a7a-acb9-92762601a00e | -4.3656 | -47.78413 | 2026-09-12 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8586555d-083c-3767-9a0f-fc99be7b376c | -2.96241 | -50.40057 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 153.9 |
| b84dfcc3-8a6d-339b-9280-9066e88b7c6a | -2.94798 | -50.39834 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 04696c81-0a3d-3093-ba8b-15adbac67bce | -2.90122 | -51.93956 | 2026-09-12 04:32:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1db56901-1db7-3f0f-907c-994a4e7d43b2 | 2.5147 | -50.85344 | 2026-09-12 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0f89194-0584-3376-b874-7432183b5be6 | -2.95387 | -50.40775 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 576c23a9-588a-3933-b94a-58c0250e7759 | -3.89634 | -55.82206 | 2026-09-12 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a2b113c-d674-3070-87af-086b9b9e3f9d | -2.73771 | -57.64215 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c510e69-98d5-3acb-9628-1f2d25bea4a8 | -2.96698 | -50.41829 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a982bebc-95e1-3d13-9104-bd8d19256128 | -5.48203 | -45.12965 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16466600-24f1-3dec-b019-dc5bb2d5f901 | -2.97028 | -50.39754 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2571ef2b-4f36-32e3-a6f0-8240841ede49 | -2.95976 | -50.41717 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 254f769f-9161-3fcf-b7c7-4a5b02a8f012 | -3.23448 | -46.94438 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 17b6601c-5a61-318b-93eb-a0a629ea1b6e | -3.53857 | -48.17827 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8962fb0b-bb50-3c4e-b4ff-c275b63e395a | -0.29317 | -48.567 | 2026-09-12 04:32:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 882d031a-f175-3b2d-afc2-d38c3d89f551 | -2.93599 | -50.47325 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de067c21-295d-3102-9900-129b75c0f49b | -5.61561 | -44.84589 | 2026-09-12 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 60d58f47-91b4-3467-b6f9-05c9bc2968c4 | -3.80863 | -49.42752 | 2026-09-12 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b60fbabe-a174-3525-bc54-1a5f0f5718b8 | -4.96484 | -45.14892 | 2026-09-12 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd704f98-4059-33e8-a0f3-7e60b97bf35d | -2.94533 | -50.41494 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| ee983171-ef4c-32d3-a062-3c2e963c6938 | -2.94599 | -50.4108 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e63ff515-5496-3f4a-82e1-68a8b4668f25 | -2.94931 | -50.39006 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d68da4a7-d002-3d8a-8482-ec5161752bfb | -2.72027 | -57.64034 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df990361-7e78-375c-85b2-f5f9aee2d60e | -2.95519 | -50.39948 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| f40e1ba8-b36f-3bf9-a1ba-71962c2335d7 | -5.5516 | -44.17954 | 2026-09-12 04:32:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6091ed6-62e6-3c59-95dd-b7696ec252cb | -3.2132 | -53.94531 | 2026-09-12 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64d10fd2-1b2f-3182-b554-33d5045f6b1c | -5.76655 | -45.09011 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 2d17401a-56f3-3a36-ae8a-322452d58ad6 | -2.96438 | -50.38818 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2ed2da3-4a29-3994-95e0-0654f5f17bf8 | -5.76301 | -45.08954 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| d770317b-d06d-38f3-b132-5011ff039727 | 2.51073 | -50.85406 | 2026-09-12 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24f7026c-e9ef-3fb7-a1ba-f3d94c57a3e2 | -2.47108 | -48.04338 | 2026-09-12 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9bfe0d56-d341-3eb1-b2a5-0646da5611e9 | -2.72093 | -57.63622 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 047e5f23-bd8d-3ca1-9cd9-0e0b553327fc | -6.29548 | -41.69884 | 2026-09-12 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ac4d7f65-09aa-3410-99ab-224c882bb51d | -2.67087 | -57.50708 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d0a11c0-1d20-3a68-8f49-729191809de5 | -2.72608 | -57.64128 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d875980-28a9-3c30-905d-1b4ef1d63c99 | -5.62086 | -45.23927 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16fcf70b-ec78-3107-b109-9935ca017333 | -2.73259 | -57.6371 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8dfd09ee-d3e5-3f96-98da-6175b0f688a4 | -3.54522 | -48.17929 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a157d80-a10a-37be-a8a8-607dac8b8dbb | -2.96109 | -50.40887 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 30a5b0aa-6cd1-34e6-ac43-84e9d317178e | -2.64039 | -48.57155 | 2026-09-12 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5729d11-7adb-3137-8533-de24f287dfc3 | -2.7254 | -57.64435 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1cc98463-19ef-38c7-b380-39ac730f51a2 | -5.54994 | -43.43175 | 2026-09-12 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e648c86-cdb8-318e-ab4c-37174ac06409 | -1.77915 | -55.50428 | 2026-09-12 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1dde117-7193-378e-aa6e-296e0749bf03 | -2.96372 | -50.3923 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 19b349ab-37c1-3b7d-81ed-7c9ebb116820 | -2.95357 | -50.3865 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b325c14-a0a7-31fc-98a9-3ab155f1eccb | 1.22921 | -50.72292 | 2026-09-12 04:32:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db31bb4e-cee1-39dc-9a03-1e136e40a0cd | -2.48747 | -49.41385 | 2026-09-12 04:32:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README18.md)
