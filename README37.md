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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9428439-3d5e-3b81-b517-091644599bf0 | -6.71226 | -44.39301 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6d5046c-47df-39cd-a7ff-1464968c375f | -7.75621 | -42.47186 | 2025-10-16 03:49:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2b48b091-ddde-3bb1-9942-3d55877d4bf6 | -7.17746 | -42.19526 | 2025-10-16 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7281843d-9f78-3e93-8781-8ac8ea5f868b | -7.00628 | -43.74449 | 2025-10-16 03:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a947045-c886-3a4b-9d41-18126e3019ee | -13.71271 | -40.98563 | 2025-10-16 03:49:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d4dfdeef-33fe-3ac7-a9c7-5b98243414d7 | -20.22824 | -41.87035 | 2025-10-16 03:49:00 | NOAA-20 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7d450b6d-4fc6-306c-9964-9dd3ac725f7d | -6.50354 | -44.46275 | 2025-10-16 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f932b7ce-88b4-3f06-8ae2-9b0fef511b09 | -17.59936 | -46.6919 | 2025-10-16 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ffe15431-eab9-3fa9-8598-5e54eb81b035 | -18.58407 | -47.46522 | 2025-10-16 03:49:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f7d6194-ed77-3e07-9e79-07ed2cd62b2b | -7.47966 | -42.15671 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 743b6d13-e914-3ccc-bc2a-731cde40b6bc | -6.79947 | -45.47554 | 2025-10-16 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba2faa69-8e99-3a12-a9d5-78f877fdd585 | -13.89777 | -42.5113 | 2025-10-16 03:49:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 17b166b9-410e-36b9-b9df-cee1a8c4fbb5 | -7.95199 | -44.135 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e665c6d0-abaf-3564-b554-00a933f7de0d | -20.05122 | -44.75017 | 2025-10-16 03:49:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31263dff-1c83-3756-9889-b50ff8e4d154 | -7.10765 | -44.71804 | 2025-10-16 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f0dbaf94-26ba-377d-bda0-73476da2aa9b | -8.25201 | -44.08384 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd1d2c39-a0c0-362f-8bd2-57a86833003c | -7.48379 | -42.74633 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4831764e-87a2-31c9-b232-3b7cc0876a1e | -8.07323 | -45.42526 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ff48fa1-5efb-3ac7-a452-5de5a6b6bb05 | -8.38721 | -46.25819 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78135ac1-6ecf-398f-8f58-4e4635589503 | -7.34389 | -43.86473 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a4ed5cf2-0426-302b-8d6e-31caec085509 | -8.16341 | -43.31446 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 675358c7-aa40-3aa6-ab5a-9de8817c48f2 | -14.74633 | -42.46264 | 2025-10-16 03:49:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 32a39f74-b7de-3cf8-b9db-7689831ae243 | -7.84981 | -45.40664 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 833dbeb6-f9dd-3de6-a8c0-1a781419a0e4 | -7.11093 | -42.03807 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4e0be084-9b92-340e-a518-dd3a1614cacd | -8.39719 | -46.26393 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c36c6863-cce2-3479-a6ff-f30a9f1f9a2d | -7.90019 | -44.98558 | 2025-10-16 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05d742f1-abca-3d75-887a-abab79e3d180 | -8.27489 | -43.37627 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e44b585-1e54-3736-bf80-7205b0cf944e | -7.47813 | -42.75377 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 818390c8-d13e-3310-bd5b-58fe7fdefea3 | -6.40402 | -45.36019 | 2025-10-16 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6c0c699-78ef-334b-8ebf-c2a064a26a62 | -7.16247 | -42.51712 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31d3133e-7c12-30d7-88bb-e6c757eaa46b | -7.28411 | -42.95984 | 2025-10-16 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bd44ebf8-93e6-31db-a9d3-4413d8a130bc | -8.29436 | -43.41787 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5a90244e-b4b9-35cf-8621-ee93b7d6c1b6 | -15.73479 | -44.62491 | 2025-10-16 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9d18a9a-36b5-376e-ad9a-9024a588979b | -6.79428 | -45.4746 | 2025-10-16 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8c4b96b4-32a8-353f-b47a-d74748f05b7a | -8.28883 | -44.9682 | 2025-10-16 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de017cac-fbfd-31d5-9b87-89ac70a6fc2d | -8.25374 | -43.34142 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 884c74ad-b685-367d-99df-8f5cb74e316a | -7.47852 | -42.6747 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 26ba529c-01f4-33ef-8ba2-b284e17a1c9c | -16.04909 | -43.70196 | 2025-10-16 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99ec7224-5741-369a-9125-2f0b88f88c22 | -8.46874 | -44.19322 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| db37e3fd-c09b-3230-a071-3ee3a7fcc380 | -7.28877 | -41.9518 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4b7b5251-68c1-3843-afe1-910117b73caa | -8.27199 | -43.36679 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 457f34f3-ba3b-3fae-9c28-b9f327cf3622 | -7.39346 | -39.69536 | 2025-10-16 03:49:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 26854398-03f5-3daa-85b8-d0d520840694 | -19.02846 | -47.51971 | 2025-10-16 03:49:00 | NOAA-20 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3414c3e-40ad-36a3-b5a6-c39cd0329b6b | -13.73422 | -44.2347 | 2025-10-16 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb4108b9-2541-3186-a4ad-f54b22927806 | -8.26457 | -43.4366 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1711ccd-7dbb-301a-beed-eb7dfb4aa572 | -6.71581 | -44.38042 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c9487b8-dd3d-350f-82a6-eee352a387b9 | -6.32104 | -46.32303 | 2025-10-16 03:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca1fa85a-0bbb-3a33-b632-8a45a9cc3f2e | -7.47556 | -42.15599 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 63723778-c6a8-39bd-b6aa-50c6dc560373 | -8.18429 | -43.32483 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 9dd826f0-1b5c-3953-8397-19e3b65d223c | -7.95045 | -44.13157 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1b10281a-093c-3872-a396-489d563eebd2 | -8.47242 | -44.19159 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| adc4c8f7-661d-3d76-97f1-901d397ec768 | -13.71555 | -40.99023 | 2025-10-16 03:49:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9f0c568a-d5ae-3ec2-b9c0-628430e4d224 | -7.74941 | -42.48657 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba8625ae-c80e-3c63-b97f-1f92afc6751e | -7.11258 | -44.71887 | 2025-10-16 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c9840b8e-fd66-3ea1-947a-70e16daca642 | -7.48068 | -47.0305 | 2025-10-16 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9aab19a-473e-37c5-af6b-1334495ae3a0 | -16.05242 | -43.69865 | 2025-10-16 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ad9c414-d5ab-329f-820f-24388dac7c48 | -7.96353 | -44.13899 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 64e12bcc-d0b8-30ae-b4e4-d12b1e273785 | -6.74819 | -44.94379 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3718f60-1712-33e5-ace5-b2eba5b8e2cf | -8.18312 | -43.96592 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 269d334f-a8d4-3107-82fe-d3d825f101e8 | -6.22357 | -47.04119 | 2025-10-16 03:49:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62b07c37-8ca3-3c3d-a8c7-a0461b43aad5 | -6.11059 | -47.30072 | 2025-10-16 03:49:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 85167a42-a98a-3ee3-bd97-e99d5094edf3 | -8.58892 | -37.7026 | 2025-10-16 03:49:00 | NOAA-20 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a1f7151e-6cd9-3b6e-9dd3-a6ac2ef7dd1e | -8.21731 | -43.31705 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 50f6f3b5-cc6b-3ad1-866d-8d8c776cbe85 | -6.66649 | -45.031 | 2025-10-16 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a5a4c98-8d1c-3935-82cd-74216cb0b730 | -7.47882 | -42.74969 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 18945d3a-42a3-3975-9378-082e305e636d | -15.0856 | -42.12411 | 2025-10-16 03:49:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f38e9e1b-ab10-31e9-82b7-16430ebbd1ad | -8.19763 | -47.0128 | 2025-10-16 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e678740c-1e3d-31a3-b589-4243b1d3e100 | -13.60641 | -43.57489 | 2025-10-16 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8695bd4-030b-3140-9062-28b6d76576ba | -7.10781 | -42.03753 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 85940b5c-a30a-3527-b165-94783688f628 | -8.21193 | -43.98776 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3e3ec06-4f26-35fe-bc8b-ec18f84f5169 | -6.32169 | -46.31939 | 2025-10-16 03:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b76985e-b6d3-30a7-8e06-abba32d119e6 | -7.34237 | -43.86646 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7996e672-87fa-3d54-a39b-edf46df1f99c | -16.68218 | -42.08401 | 2025-10-16 03:49:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 657bc052-fdfe-3d73-8391-3f698d8b5f2a | -15.57493 | -42.37634 | 2025-10-16 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3e3c70c-de7c-30cd-bab7-2fbda5fa5ab8 | -7.6684 | -42.37447 | 2025-10-16 03:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a609a741-4e4f-3407-a387-b86237a37f57 | -15.31818 | -43.09797 | 2025-10-16 03:49:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 661d0db3-8cde-360f-b784-aa74d5cc59d3 | -8.40647 | -46.24286 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4f6102c-d55c-3593-ad81-f4e0a40d0238 | -6.89336 | -43.05511 | 2025-10-16 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d699aa1-ab44-3920-a963-5856a0c910eb | -7.19765 | -45.48543 | 2025-10-16 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45013d83-9c07-365f-be6a-51fa1137252b | -8.19606 | -43.97313 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cba88fae-3c8e-3d86-aae6-2cf85ef2b2ae | -8.193 | -47.01973 | 2025-10-16 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a5b6911a-1bf5-3c14-85aa-2a5bfcaa71ae | -7.3051 | -41.85512 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7bbde6ab-4017-3804-b7b3-0369751ee591 | -17.21997 | -46.93074 | 2025-10-16 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cc8aed2-e876-396d-892f-51f6b38b84ca | -7.93973 | -44.12259 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2cebaa3-8d9b-3217-bd1a-3514dc1fc233 | -13.41031 | -44.31845 | 2025-10-16 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f3322ca-798b-3239-9000-8c60f9e1c579 | -8.22968 | -43.32382 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 63fb1da9-7a2e-3d9e-a3ae-80dba42aa9eb | -8.39187 | -46.26287 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c5d89d1-7dd0-378c-be7d-e5a41c1bde3b | -7.347 | -43.8672 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 35b9e219-44d4-31e4-a9b2-1dcce59f25fe | -6.74996 | -44.37695 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d0165338-c086-3d4f-8d7b-e5a34b48be97 | -16.19613 | -43.71012 | 2025-10-16 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d99e29ff-1c1b-323b-a2a7-7fdb5bfd9f55 | -6.6373 | -43.42303 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5571bef0-5c95-3185-9469-219c81329e40 | -7.50618 | -46.64419 | 2025-10-16 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12d7e862-2ab7-3d95-93a1-3ae4227fa573 | -8.20337 | -43.31924 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f3062f7a-a9a5-38fd-a12b-1f04b5fbb19c | -7.21923 | -45.16726 | 2025-10-16 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9591e76e-5c80-3f26-82bf-809a89a0ce8e | -7.5726 | -42.68185 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f5c24514-cfdd-3f97-b7da-50e3904bbf0d | -6.11137 | -47.29643 | 2025-10-16 03:49:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ed0a9fc5-0477-3f0a-af55-50ec5375216e | -7.89463 | -42.95883 | 2025-10-16 03:49:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d9aa293a-eca4-3dc0-b18f-0694dfeaf11b | -6.66599 | -45.0339 | 2025-10-16 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59a85353-2f92-3d9f-bce6-250531c0c1ec | -7.05967 | -41.57314 | 2025-10-16 03:49:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 21cd1149-1468-33ae-85c1-147c2b1f2822 | -7.29224 | -41.95605 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README38.md)
