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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 271ea1b1-3775-3d57-b5d2-ab6f609864ee | -9.62953 | -46.11728 | 2025-09-03 03:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcef9f70-6b19-3d74-8430-bad5f47943a7 | -6.86087 | -45.5442 | 2025-09-03 03:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff811d8b-4a0f-3497-971a-5863916aa41b | -8.02076 | -44.10397 | 2025-09-03 03:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21226121-a5f4-3c78-a408-e60b9eb6daf5 | -8.87576 | -45.83102 | 2025-09-03 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| db086dfc-a857-3cbf-a03e-c12609fe016a | -6.7075 | -44.18561 | 2025-09-03 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d07fa3d-3d07-3142-b7b0-059c0bca9ea9 | -6.78141 | -44.48634 | 2025-09-03 03:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40cc6080-8c36-3d09-9030-392214a63243 | -6.35818 | -45.65498 | 2025-09-03 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 715b8430-0bed-32dc-bc2f-8647629a0225 | -5.80689 | -43.23069 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3917f90f-f7e3-3a74-b454-5224275b8209 | -5.79469 | -43.23303 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e44db316-8cb8-3a54-868c-45e81cf89730 | -6.98051 | -43.28351 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 54918be7-bd63-3be3-86ce-608274dc7a89 | -7.1148 | -44.75724 | 2025-09-03 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 591d15ff-0a69-3e70-9cf4-c2813f88ed5f | -9.19769 | -45.19276 | 2025-09-03 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 731aae40-0d34-390d-bbe1-4358fd31e5fa | -8.06394 | -45.36706 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7e83fc87-cdf0-3cbd-9f4e-3ffe17feeee6 | -9.63542 | -46.1174 | 2025-09-03 03:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d150a54-0136-3b85-92df-828aebd7e918 | -5.53404 | -36.84798 | 2025-09-03 03:32:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 2a04fae2-5bc8-391f-b02e-f8256a5d884b | -6.95743 | -42.98126 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0ccb0495-c574-315a-9b3e-fa5f8b521842 | -6.19678 | -43.34262 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37a36179-8b99-363e-ac03-b5602a5afb15 | -8.87024 | -45.82286 | 2025-09-03 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c69f6252-867c-37f0-ba69-23d320a6e03e | -8.02352 | -44.08895 | 2025-09-03 03:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7085efc3-1104-3c1a-bdcf-c667511b2741 | -8.02276 | -44.05772 | 2025-09-03 03:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b0e57eb-ef79-3a70-98c5-82fa7c89da6d | -6.70371 | -44.18709 | 2025-09-03 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43cfec4d-a0e7-300e-9547-451e4154808a | -4.89715 | -43.21009 | 2025-09-03 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e584ee39-55fa-3d01-b094-0de67ed950fc | -5.8095 | -43.22147 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b09a3ec6-06e4-32f8-886a-0bb3995de756 | -5.80089 | -43.23408 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20665ebd-c4db-33f0-9259-82698b78745a | -9.61294 | -40.61871 | 2025-09-03 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 735d1692-1674-3de3-8080-b61244bd4606 | -4.67861 | -42.92863 | 2025-09-03 03:32:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c82ff06-e85f-3dba-bdf3-05557bd9868b | -6.69353 | -44.18874 | 2025-09-03 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4cc0d70-8c9b-3e4b-a4cb-ac01f30cef8d | -8.8877 | -45.80671 | 2025-09-03 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 141757eb-5de3-3b84-9313-d1ecfc6fcfbb | -7.13357 | -44.57005 | 2025-09-03 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c62d36f1-71dd-3ca8-9d6e-7b8931983e2a | -6.97964 | -43.28814 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8823b090-6b26-3160-b986-37d92c8898c3 | -5.52937 | -36.8509 | 2025-09-03 03:32:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 90037b4d-abb8-3b42-ac85-a9229c35583f | -5.89405 | -43.35161 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cb680d3-bb9e-36d6-8159-6c5d45cca8aa | -6.22708 | -43.38364 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a2e8bd4-efbe-383f-935c-fa323f91a7f6 | -6.99699 | -43.26259 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9c2ed8bf-458e-3a75-aceb-2da65adcf02b | -5.79984 | -43.23422 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d133bf3-6f0c-3e89-8e83-5292059ac75c | -6.02643 | -45.99877 | 2025-09-03 03:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d101b95-86ff-3b8b-9306-e034c003b363 | -5.80329 | -43.22051 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c08dadb-3a9c-3c85-b367-a34c4276b5a5 | -9.19418 | -45.19542 | 2025-09-03 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f20267be-575f-31e5-9d1d-6eef27556158 | -8.02059 | -44.0518 | 2025-09-03 03:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5743d357-7574-3d53-901b-28a72b37dc9e | -5.92728 | -43.36249 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 64aadfe2-a9af-3827-a639-4c21f23d70c2 | -7.00565 | -43.24983 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06f2237b-02ff-3d3c-b336-e840e8206167 | -9.6121 | -40.61599 | 2025-09-03 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 46d045c2-dde8-3085-ae05-7551efe926a1 | -6.46884 | -45.40613 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f5fe71b-6181-3207-8936-ff6b13c23f35 | -5.64331 | -43.67525 | 2025-09-03 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ff0092c-077e-3dfe-a37d-bf9612d45a34 | -5.87871 | -43.01088 | 2025-09-03 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3436d910-86b1-35bb-8d1c-6fd02b214f9f | -6.53893 | -42.9524 | 2025-09-03 03:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6808d8e6-98b2-38f0-8501-396c96e1ca49 | -6.58453 | -44.57864 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e78feb73-465c-3bea-8fe9-d43ddfaa4900 | -8.43485 | -45.08159 | 2025-09-03 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e399705-0c62-3ec5-be66-587542ea1a3c | -7.48234 | -44.83897 | 2025-09-03 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5ea70ca0-a431-322e-bcf1-c89e33f565de | -6.2209 | -43.38241 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ab66b611-f0dc-30d6-9d7a-878d478515df | -6.41115 | -43.75673 | 2025-09-03 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 68b5d0fc-dc06-39c4-a4a6-d783f1adf682 | -9.63414 | -46.12366 | 2025-09-03 03:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 877e59bb-5124-3d6e-b6d5-076f7430d018 | -6.28482 | -43.58178 | 2025-09-03 03:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67e5920e-199a-31f9-b8ad-cac2b5ad5f4a | -7.48691 | -44.81485 | 2025-09-03 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecaf0d3f-6a01-387b-bba5-63812ce848c3 | -4.89266 | -43.199 | 2025-09-03 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e22ed61-d182-3a7d-b798-ec898650c4fc | -8.86895 | -45.82931 | 2025-09-03 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 71104d41-05cb-3b3e-acc6-d1084d0f07a2 | -5.96196 | -44.28234 | 2025-09-03 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b3d2c63-8c6c-34fb-b949-b9c97466a828 | -7.01591 | -43.53899 | 2025-09-03 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fddd1592-fdf4-3660-b996-96ea793f3dd5 | -6.46526 | -44.68385 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60a30cac-fc03-35d9-8c1a-616bd3bf4ef1 | -7.00652 | -43.24517 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 160de3bf-f687-3701-b8b6-052b037c3455 | -7.93336 | -46.55964 | 2025-09-03 03:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6be5a6eb-ed7f-360f-af53-838a02c8fb15 | -6.73544 | -42.25785 | 2025-09-03 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6db6cd6e-6377-3c99-b8ea-d867daec332e | -6.09322 | -43.28845 | 2025-09-03 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a3977211-6df8-3b4b-8d9d-88be6ff35627 | -5.7945 | -43.22854 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a249c68-4919-392c-9291-3b459cfd3edb | -6.23236 | -43.38983 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42be0d53-9a52-3ba0-b0a2-6541abfd2f2e | -8.02026 | -44.08756 | 2025-09-03 03:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fea29a52-2ccf-3110-a390-ee3931fa4735 | -4.89539 | -43.21999 | 2025-09-03 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 0b708607-8699-3f0e-8d2d-f183e8c9ddd6 | -5.74191 | -39.75798 | 2025-09-03 03:32:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3ca270a4-8d87-3e42-8e8a-3ad6cf0f9f8b | -6.35566 | -45.6688 | 2025-09-03 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f39e7b79-c9be-38fa-8b68-82011353e800 | -6.19595 | -43.34722 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 00dd2f77-3c71-3c27-ad67-df1e437b8d93 | -8.05159 | -45.36233 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02928dfa-a506-37b0-9600-1b4fd69b0465 | -9.63465 | -47.04752 | 2025-09-03 03:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18cdc9ec-8f8f-36f9-bdfe-ff599fed6601 | -6.85246 | -45.55058 | 2025-09-03 03:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2b96ebea-1b27-3df0-9e07-607c8df994f1 | -6.19512 | -43.35187 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 89013b80-d07e-3184-a2b8-902a03997ccb | -6.99785 | -43.25797 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9761bb40-9fd1-369d-9934-64929d40247f | -5.5009 | -42.63372 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ab98f25e-ed23-339b-a81f-336b5a960367 | -8.86974 | -45.83015 | 2025-09-03 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 910d1a31-5087-3215-aa24-e9041eee5c67 | -5.80772 | -43.22617 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22377e46-6fe5-33e3-b4dd-bb0b31d45873 | -4.68479 | -42.92974 | 2025-09-03 03:32:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcbfd631-4b63-3faa-bbaa-fccf752fa101 | -6.54413 | -42.95792 | 2025-09-03 03:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dca03724-b928-3f4e-8255-2323cfbeda39 | -7.49347 | -44.81648 | 2025-09-03 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f372942-437f-3e64-aa05-b53fba259935 | -5.80606 | -43.2352 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 830edca8-f4f9-305c-844c-0acd28a7aad2 | -6.26724 | -44.50352 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ae86a15-2a81-3e0a-9bd6-7f487246029d | -6.41203 | -43.75192 | 2025-09-03 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b4c5738-df4c-3228-8591-4ac578da270e | -5.89694 | -43.35258 | 2025-09-03 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62cf6d94-13fd-3bd3-97c4-e4663c512cbd | -6.12879 | -44.13434 | 2025-09-03 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70502e0e-7be5-3d7e-8587-63eec04ef922 | -6.22187 | -43.38139 | 2025-09-03 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 22a3471f-7ae0-3c8c-9dc1-e3755e9850ec | -6.9763 | -43.28926 | 2025-09-03 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aeed7cca-6a52-3165-b3e0-3f60f90b4c9b | -8.05733 | -45.36489 | 2025-09-03 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad817747-4731-3ead-8fdf-ed256155c55d | -3.81466 | -41.06364 | 2025-09-03 03:32:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 480b1951-241f-3821-9789-ed9ae0ba4e3b | -7.48344 | -44.83316 | 2025-09-03 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f111b63a-108b-37fd-ba09-486de68aa523 | -7.9293 | -46.54713 | 2025-09-03 03:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| db551c8b-a2bd-323f-939b-0ec4a3f73f81 | -6.47322 | -45.42097 | 2025-09-03 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6299ca3f-2c5d-324c-bbc5-8943edfa8ecc | -7.94206 | -46.55365 | 2025-09-03 03:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9399948b-2db5-3b04-b08a-7d124238d746 | -9.16552 | -45.20176 | 2025-09-03 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b72a4d4-2cc9-3092-a0fd-0b42b1ed9fcc | -9.85711 | -44.68351 | 2025-09-03 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fcf2b45-10a9-31d6-8234-13aa45e14780 | -5.76437 | -37.92814 | 2025-09-03 03:32:00 | NPP-375D | SEVERIANO MELO | RIO GRANDE DO NORTE | Brasil | 2413607 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cad97ea4-565f-35fd-9b4c-1dd8523356c0 | -4.90431 | -43.20618 | 2025-09-03 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eda583ab-9498-3c8b-a091-4fba59608387 | -6.25322 | -42.59669 | 2025-09-03 03:32:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cbfc7342-4ea2-32c8-b0d0-f35d9554b5be | -7.11593 | -44.75132 | 2025-09-03 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README24.md)
