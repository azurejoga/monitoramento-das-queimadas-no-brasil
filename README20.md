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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35744755-8aa6-3013-933a-6025cec5db17 | -6.50999 | -56.20728 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08e8807a-c913-3f63-9dbd-b533e1fc37d7 | -5.06276 | -56.93018 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e978d2d8-15f0-337e-8c56-adca72b7690a | -6.82559 | -59.27089 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 8ff5b3db-43d7-3311-b7f0-e6ce7e4b9f14 | -4.31623 | -48.10198 | 2025-08-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 503bc15f-676b-3a6c-afef-76694fb3a5a6 | -6.66077 | -56.39384 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ce4741b-8806-3f8c-bf03-798abad85da2 | -8.05043 | -43.11317 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 659e1fe1-1894-335b-bd94-45ca4c180b00 | -8.05122 | -43.11095 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| ba84d1a4-e95c-3dbb-be92-9eecd5e72f0a | -5.48248 | -42.15847 | 2025-08-01 05:04:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e6a38607-9de4-3096-8fd5-152231395b1f | -6.74067 | -59.16908 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 94c0b74c-29b3-3d53-9605-efdfc1399c48 | -6.73212 | -59.17624 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 99e4b30b-1595-302a-9a8f-34c223301ba0 | -6.55183 | -56.19965 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1bc7570a-d59c-313e-87d9-4f83ab1fe419 | -6.72988 | -59.16734 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebe6a008-1bcb-3d17-aa1f-09f77e65d8e8 | -4.39921 | -56.21744 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d142005f-58b2-37bf-832b-e9e2d0164244 | -8.0419 | -43.12498 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 42a4cffe-aa4c-3aef-ab52-b32f66498074 | -6.52208 | -56.195 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88f682f0-be1d-3da6-9e76-3f51110892d0 | -6.51107 | -56.20036 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04a72eea-96ea-3f64-a877-1857586441e1 | -6.50831 | -56.19639 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9142131-f475-319f-9f0e-a7f6aa353f31 | -6.74337 | -59.15248 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 65988ad8-2ad1-3cc3-afa2-91c618737973 | -6.73685 | -59.14721 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a6824ea-5968-33a6-b3b6-b407b00dc10e | -3.36347 | -49.16304 | 2025-08-01 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e340873d-6e27-3aed-9c0e-f36cbf2d37d4 | -6.54744 | -56.20605 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33719016-09a8-3989-a53d-1d87185dc29f | -6.7292 | -59.1715 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1a93dab-ffdc-31c1-ba3e-75fc54d66d69 | -8.05201 | -43.1045 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f23c4fac-49ec-3e89-a3ba-f50791e745fe | -6.83057 | -59.26311 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 9d1dff53-a6ac-3e90-a3e9-00ea146d34cd | -6.66467 | -56.4122 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc3688ba-9bcb-3af7-bfd5-4c937e89f2a8 | -6.81835 | -59.26976 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 5fa2dc05-c7c7-3e37-a123-da74a889c9ac | -6.54852 | -56.19914 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3dc1e0f9-f6d1-32e3-aa12-a5f099e16eaa | -6.67346 | -56.39937 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b697dfb2-aa1b-358b-9da5-ab06287561b3 | -6.55898 | -56.19723 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87aa639d-0079-37dc-9711-79faad0cdaea | -6.554 | -56.18583 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 086ed984-19fd-3bfb-948e-407c6222cb80 | -6.62486 | -59.97164 | 2025-08-01 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 4e17f05f-3e03-322b-8937-0f1119ad2134 | -6.51221 | -56.2147 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bbd9022-4c9d-3921-90b3-66149caf7375 | -6.55345 | -56.18929 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca36d455-277e-31a7-833d-df777e0a5e07 | -6.7427 | -59.15663 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 11ba61a6-245f-3403-911e-7179a77b25b1 | -6.55291 | -56.19274 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23fd5afc-d28f-38a9-9861-45b62f4157c6 | -6.56061 | -56.18686 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 924b0030-30a9-3df7-9607-f353992fc78a | -6.73618 | -59.15134 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b512cfc-7273-36a0-8845-5e557d6f3dec | -4.31076 | -48.10632 | 2025-08-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b77bbe99-6cd3-3818-872f-d6bd2ff19002 | -6.56337 | -56.19084 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ebb218e-11c7-30ca-a56f-2a0b373c29a3 | -6.66462 | -56.3909 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a63b89d3-1f53-373e-8e3f-69538beb7835 | -6.66521 | -56.40873 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0de5602c-d13d-300d-ab97-edec84a921f6 | -6.62111 | -59.97097 | 2025-08-01 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b1d8d7ad-01ab-3694-8ac2-5a0599da93d4 | -5.05996 | -56.92611 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41d4da06-70f9-3f13-9f96-a0b70dea800c | -6.50945 | -56.21073 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a58d3c39-e4ae-3be3-ac53-f1579acbc04b | -8.03503 | -43.124 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| cd9d3b74-834f-3703-b5ea-9b3b0411ceca | -6.53422 | -56.20398 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0bce43c-9eb9-39c1-851b-1a50db60c467 | -6.64165 | -59.08648 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3229769f-dd42-3f9b-af1c-01ff0b658fba | -6.74203 | -59.16076 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ccbc84ff-49a0-3360-95bc-412ce5219a6f | -8.04434 | -43.10996 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| b5fb65ff-5b0b-3202-b1e5-cb45b23a3f0f | -6.67569 | -56.4068 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 995370a2-93fd-3f26-aed0-649f4041fb80 | -6.17084 | -58.06854 | 2025-08-01 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10cce0a7-53fb-3afd-bc25-07c5e3eb0fd5 | -2.90817 | -48.29844 | 2025-08-01 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2205da91-e711-3990-bf7e-045f87023c8f | -8.03512 | -43.12815 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| ebeb8903-daab-3de3-8d50-289ffdac1dad | -6.7436 | -59.17378 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 56215622-ef66-3db2-a75e-f924d7743f11 | -7.08214 | -60.04836 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a184be63-25f2-3324-811f-88454b5910f6 | -6.56722 | -56.1879 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cc52e25-b827-3cf7-9e49-dc72e845f559 | -6.62854 | -56.27534 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e66cfd42-bf81-3383-a76d-2c5a3f0ef6d7 | -6.83192 | -59.25484 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e0656b2-5e4d-39ba-b04f-c5d3d841a9f2 | -6.65144 | -58.82487 | 2025-08-01 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 085987da-6904-3a27-b3bb-b10cabf69a7c | -8.03421 | -43.1304 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| e903cedb-e91a-3cfe-bebb-8b29397d007b | -4.58032 | -55.73559 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3679f87-cb29-3822-a793-e41de86d89ad | -2.90611 | -48.25024 | 2025-08-01 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e4ea948-36a1-3867-9080-448252fa2549 | -6.56668 | -56.19136 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea629e7b-6997-3a7b-b9ae-ea15ec8391d3 | -6.64524 | -59.08704 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc8e84b7-b3d5-3839-abcb-759ee5a2af65 | -6.65692 | -56.39678 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18b7d451-aab9-3085-bd21-92bfc90dafc1 | -8.91651 | -47.33611 | 2025-08-01 05:04:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f9a869c-dfc9-3c69-aa22-5e951ec6d7b2 | -8.04199 | -43.12914 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| b46529c9-f77e-3b10-9d5b-4b1453b4ffbc | -6.50357 | -56.20257 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4375098-a10c-30b8-b774-c29a69c4dba2 | -6.53091 | -56.20346 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a58d567-cf11-3ad3-8fd6-08b9732c018b | -6.74135 | -59.16491 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 34ca596c-49cc-34bc-80d1-815f4303ef4e | -6.66684 | -56.39834 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b67f9e8-1b61-3cc5-ba76-cec4b3de6d98 | -6.82334 | -59.26194 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3ea78215-4f78-3ab0-9076-1b685c40b8da | -7.07536 | -60.04259 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f21e581b-eea5-3b2b-8299-6f87218e6596 | -6.7355 | -59.15548 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ffac364-1f52-3bb7-af5e-5b27545a2c02 | -6.67677 | -56.39988 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ae66e73-879c-3b00-8752-58509895aa22 | -6.73842 | -59.16022 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| afaf590f-2fb1-39b7-834c-d7c4dddd035c | -6.54798 | -56.20259 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36c64ea5-3cde-3a0d-a564-71889abba7ea | -6.73932 | -59.17737 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 148395d7-3b91-390e-b53f-7b22cdbf1f67 | -6.62035 | -59.97556 | 2025-08-01 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8978c99f-056d-30ba-9b5c-42c1a8ac79a5 | -10.4248 | -60.27546 | 2025-08-01 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9713a689-2e8c-354a-aae1-b42ea974a32d | -10.60615 | -45.27597 | 2025-08-01 05:06:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c51f3b9c-5c9b-3e0c-9947-e7aa73d9629c | -12.65626 | -48.09286 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 411996c5-acc8-35bf-93a8-a41c37faf942 | -12.63921 | -48.09922 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb3d060c-ad8c-3405-9f2e-16ce7ec8b048 | -10.06137 | -48.32946 | 2025-08-01 05:06:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d3866e3-7eff-3797-ac03-9795998e4c05 | -11.77161 | -45.00691 | 2025-08-01 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f3ecb59-be68-33f0-a33c-4771b0978d0c | -11.81275 | -48.79161 | 2025-08-01 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f60b4ac-41ac-3a8a-bb8a-83b84aa325aa | -9.86515 | -44.70319 | 2025-08-01 05:06:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 864a5d84-1924-3a60-a37c-1d86e5663a7a | -12.65593 | -48.09563 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 068a210f-3da2-3561-b7ee-6a2356acc13e | -11.51955 | -58.00122 | 2025-08-01 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ee0f301-732d-3af4-8289-b179dc39dbfa | -12.65057 | -48.09509 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1739c959-0cd7-3318-8736-7d31ad0b5c42 | -10.60259 | -45.26942 | 2025-08-01 05:06:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5522fb96-3cbb-3796-b97b-63ebcca5683d | -10.43412 | -47.24988 | 2025-08-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e921a559-c5d4-350a-af67-9b94773d9119 | -12.65023 | -48.09792 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98bce8eb-b2f7-3d2f-888c-cc0380b5a369 | -7.32726 | -59.62172 | 2025-08-01 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1cfd5b1-e201-32a8-810f-c9298759fe46 | -10.11112 | -58.22778 | 2025-08-01 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 43447ede-5a52-3b1d-acd4-57097b48909b | -10.08236 | -46.74609 | 2025-08-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9a66fb17-0a02-3c2c-84d1-0dd8849226b9 | -9.43166 | -56.50883 | 2025-08-01 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b65c2e3-804a-3324-9072-d7df82fdedeb | -12.26591 | -45.07545 | 2025-08-01 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa79b711-4140-32f1-a41a-3ea973f5db46 | -12.71412 | -47.79232 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce4e7956-41eb-322d-9c19-0ff1375e7fc3 | -13.09319 | -52.14473 | 2025-08-01 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
