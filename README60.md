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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ea0143e-513a-346f-953a-a1105278fc7b | -3.2954 | -53.68008 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1947770c-f28c-32e2-ab23-3fd0d0cf1dcb | -2.04493 | -54.67149 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e0bd123d-85ce-3aa8-b07f-e77598053f37 | -2.6171 | -51.7634 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88f2e773-a3bd-3a76-a40b-462d4186be64 | -2.46814 | -53.96536 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84799017-5089-3575-82e0-48ddcbed066b | -4.59346 | -45.57294 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 620f7280-c68b-394b-802f-f69bbc2cfca0 | -2.81469 | -53.04897 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48730564-97b6-3bf3-8ae0-f1a80ff05eda | -3.65632 | -50.70741 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4a4a1c8-d25b-3dbd-95b3-b3e198d7545c | -3.98445 | -49.93368 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3eddfb86-cabb-3b34-ab32-41fd9ede52f2 | -1.00417 | -51.72005 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85b5b915-799e-3fe5-a31c-d59ea869c546 | -2.77783 | -55.33889 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 565c36c8-3af5-3773-89fa-72127f069b40 | -6.75855 | -46.52544 | 2024-12-01 04:44:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 629cac56-cf12-37cc-8333-fbbbbef2b7cd | -1.34975 | -51.38564 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b492bf5e-7063-3d0f-87ed-0e9bad00c82b | -0.59494 | -51.69535 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e10f5e9-d584-3035-8f0f-da3105e6163f | -4.25822 | -50.83727 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c821d87-3318-36ff-8a68-084b638a1289 | -3.32041 | -53.29473 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dca2596-7ff1-30b1-9a38-c12371db3e5b | -1.6197 | -52.69071 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a0934e9-2b76-31db-9624-cb019a1a7708 | -1.24721 | -51.79051 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37e73704-96b8-3a12-9c0b-2de8dcc7f73c | -4.20107 | -50.68679 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4641ec21-9053-311f-b9a7-b35a4cd60a80 | -3.03683 | -51.47459 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf02200a-a31b-342b-bf09-70ad821cb1ef | -1.14423 | -53.67239 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10c9cd5f-72fd-36c1-b202-7d6ee1719307 | -6.92302 | -43.53713 | 2024-12-01 04:44:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 348f7d17-b25c-3d1b-86bc-a9d4641518e1 | -3.83718 | -50.03156 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adb46466-4b5f-3a1c-b8ff-95280088ac09 | -3.4653 | -53.78931 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab197b6f-3321-3d2e-bf19-aa04d52c7065 | -3.95681 | -50.51717 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fad1845a-4f57-3218-9d70-abd94db898b8 | -2.26844 | -50.77042 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c23b8076-3582-3471-af61-ce93ec9be015 | -4.0143 | -47.00436 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07f1a141-2ec7-3e63-998f-66ba3810f79b | -1.2007 | -52.56392 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c89ff775-00bf-3b4c-9e48-c8f89b8e8e2c | -2.36337 | -50.515 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3c5d8c9-0ce6-39c3-9591-5fe0ff23d869 | -1.09316 | -53.60669 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90d6fdb8-14a6-3e9b-8564-ac9da0ba9241 | -2.10426 | -47.624 | 2024-12-01 04:44:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d811ff2-5b44-392c-b94d-22bbb1c49f21 | -3.24297 | -53.92401 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c7869bf-559c-3490-ad0f-6a082a68ca82 | -3.82211 | -52.24664 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5ee9ac8-ecf5-3e1a-96a8-c350a4665535 | -4.01119 | -48.40714 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e7a2d32-09d1-3ee5-8c55-a760901f65ca | -3.28987 | -53.82978 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbb67f67-bb1b-3485-a07e-1d346117b83d | -3.11465 | -53.81055 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f6a2307-b777-3498-994c-722ba21b5418 | -1.24737 | -54.54921 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 041fd747-2a00-345a-aa7b-d6c1f5ab951c | -3.25245 | -53.62683 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1f06734-32a4-3f2e-bfef-c644107008a8 | -3.32161 | -54.18081 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04a99d65-7a09-34e7-97f6-ad9607c123d1 | -1.64564 | -53.86867 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44850b4e-0049-359c-98a5-9b82f4a82cd0 | -2.60589 | -54.28618 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b4ddd0e-3637-37f4-840e-6c5079bfc55a | -3.37955 | -53.50742 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| be83f27c-5216-3d90-a1e9-54ccb7ae7dd5 | -3.26046 | -53.62368 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 708a190d-a8e5-3f76-ba28-afedafe97683 | -3.31455 | -53.86509 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bdd03daf-3ff0-389c-998a-8254766dc3ec | -3.82634 | -46.60222 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd628119-2538-37af-8231-d304fbbb46ea | -2.84938 | -53.94832 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83df12f4-330d-3f37-ba2e-5119cd6b79df | -3.75509 | -52.27007 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 043559ad-9097-3615-92ee-136df96777aa | -2.85072 | -54.05947 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e417f148-998f-39f0-8cb5-c7bbde2c0896 | -3.53912 | -51.50561 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5307e02a-4459-39f9-b92d-9f8cbd629794 | -3.86142 | -47.0527 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05b9ef01-72db-3d28-ae4d-cb565e009b84 | -4.78906 | -44.74354 | 2024-12-01 04:44:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 368bc220-0dd7-34d1-878b-f2d281f4500d | -4.52921 | -49.80445 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af140e3a-d697-35c9-8b85-c827d4ab8d8a | -2.98686 | -53.88671 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 471842df-562b-3d5c-bc8b-f49df1e23af3 | -3.72509 | -54.52586 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c369c0dc-df98-3fd7-803b-2e054f32ad96 | -2.98154 | -53.87228 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58f11481-e925-35d9-a077-295fad961fc8 | -1.4524 | -48.2037 | 2024-12-01 04:44:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36e6a73f-cade-3af8-88af-570858eb2639 | -4.1695 | -48.62069 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bed7e22-9366-36e2-bde5-7658e531f88b | -2.44433 | -50.51705 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 481cde54-4733-3fb9-979e-fef6aab467b4 | -3.31987 | -50.02863 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab6854b3-5f9d-3ff2-83f1-01170deacd19 | -3.65578 | -50.71086 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 814466b0-cc51-3dae-a527-4c972d942f81 | -1.1813 | -51.76941 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6641a0b4-a1b6-3277-9a07-f2c6e17fe29e | -2.61652 | -51.76705 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56487503-2a08-3a59-aac8-7a48e958c59d | -3.71404 | -51.06478 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d5b9411-146c-35d5-b1b5-1e1b99530611 | -2.74915 | -51.6576 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14e9e68c-f2ce-3302-9bc4-5b1c86e42baf | -1.40353 | -53.40576 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5a722f6-1ac7-3a9a-8432-4eb02bd61cca | -1.40273 | -53.3872 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01e917a2-2899-3c1f-bce1-8a47aacef717 | -2.26372 | -53.4621 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b5b349c-5b75-37b5-95e3-93cf7fd19d6d | -2.90462 | -51.58249 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66ce91e5-3c5d-3c9e-bbec-13c25308a492 | -3.8928 | -45.00871 | 2024-12-01 04:44:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4527c744-173f-3402-8e6c-f45b1aebb5df | -4.55672 | -43.29849 | 2024-12-01 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 16d9e547-4694-31fa-90b4-841618b17b19 | -1.29559 | -51.72955 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b483666d-7fe3-3485-949e-3ce101dfb832 | -1.72334 | -52.49584 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4403db0-4bbc-3847-a440-37be645b8a15 | -3.48984 | -53.8141 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ac0cdea-6f41-331d-8d92-e27a51f62aa9 | -2.03203 | -52.07836 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 344141f5-47d6-3aeb-8c88-df16c3ad87a6 | -1.32359 | -51.75293 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2ad93da-82de-3cc8-bee1-6787ffa5156f | -3.95124 | -49.94982 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07ed34da-82fe-39bd-b0ea-ea28a397dfdb | -3.15275 | -50.14418 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c86b88e-f909-3198-86b4-b39ba16519f3 | -3.59702 | -50.37634 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea1f05a8-e6a2-3847-990a-bf17143a8838 | -2.80451 | -49.77831 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13da3122-2708-3d90-b5d8-0a11cc5cff5e | -2.06861 | -51.19652 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 374719d9-4044-3d22-b7ba-b1d16c86c5c8 | -2.46315 | -46.5705 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fdd1e40-2bc2-3c95-a4e4-82de73b5eeea | -2.88129 | -54.01323 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86345c17-a5db-3661-b295-ce7f6dc33b7f | -1.5988 | -47.32759 | 2024-12-01 04:44:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfe4e282-6948-3bdc-94cc-676b7b1f1427 | -4.04835 | -46.82153 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03cb6ab4-d7a3-30eb-bab7-03686ee1368e | -1.94654 | -51.2101 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c40cf9a-9fab-35c0-86b5-16f92b90c11a | -2.43695 | -50.43444 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7177e59d-05da-336d-9f64-d432e817c928 | -3.42402 | -50.01303 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fd2f5bb-4cbd-3adf-b77d-ae1d4391778b | -2.59657 | -53.98404 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 123c397f-5dc5-338a-a50d-e8759b46918e | -3.71294 | -51.07174 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d949a90-dcd7-3b17-bdf7-76da8fb96d72 | -3.22198 | -51.71602 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daa1f7cf-f6bc-3fd8-98d5-1e9c9e151d96 | -4.43569 | -48.2998 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0343e96c-f7a8-3c49-ab20-46bb8eea798a | -3.54125 | -50.40652 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cbe9db51-a0e9-3804-9d65-7713411693c7 | -3.33893 | -53.36824 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc8cab24-b1fb-3306-be4e-86e7e2a5b0de | -3.26458 | -45.37252 | 2024-12-01 04:44:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03758e20-c334-3e98-9a59-2a1136a5ebca | -2.77258 | -55.34551 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88be70b9-be23-3c99-a1ce-e97b9fef8680 | -2.03701 | -54.67021 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe53c49a-987b-3e03-b396-de55b077faa3 | -2.36859 | -50.39542 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0be7aee7-aa7c-3b28-be08-64057ae54b72 | -4.31361 | -48.20739 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6b1d49e-dafd-3861-885e-dd0ea928f76a | -2.81881 | -51.79066 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f712d7f9-e5ce-3a95-9b60-d15626b69ec0 | -3.26141 | -53.64129 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4f077f98-c50b-3536-9e4c-04d8800f9ce7 | -2.87951 | -53.32294 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README61.md)
