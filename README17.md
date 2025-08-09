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
| 484aa24e-fa88-305e-bf01-ec7c9bb494e7 | -6.25035 | -44.83275 | 2025-08-09 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0d1e3cc-4566-32fc-9ebc-c494119aeef8 | -8.07983 | -46.8488 | 2025-08-09 04:40:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ededb9fd-c33a-37b9-b387-ef2e63c50598 | -6.14299 | -44.53845 | 2025-08-09 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32d8321e-ea1a-39a7-a13b-89e4e1126c56 | -7.0821 | -44.51912 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d7ddf6b-c2c7-37a4-93bb-58d98a8f0588 | -3.9872 | -47.88743 | 2025-08-09 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f79c9a9b-dc66-39df-a880-5137048cdaa6 | -9.08059 | -40.00571 | 2025-08-09 04:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1728fa8e-8086-3571-943b-7debe8b2843e | -8.05812 | -46.32996 | 2025-08-09 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0707c99-86f4-3276-9207-9676142c2d8c | -7.17375 | -44.40137 | 2025-08-09 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4e7be91-3f16-32ee-8d7b-4614350d1c29 | -7.25257 | -44.62926 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96237d47-8ca7-39d1-80f9-d2747cfbb154 | -7.96224 | -49.39951 | 2025-08-09 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1840f991-591a-39b2-ae61-559ff0d1b15c | -6.57681 | -44.5744 | 2025-08-09 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 638541ed-d63b-30a1-ab42-e9d5b56f3807 | -6.29096 | -44.99042 | 2025-08-09 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df97a5d9-43d4-326e-b2c9-038b1c3a7f30 | -6.02935 | -47.77892 | 2025-08-09 04:40:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ddbd28f8-c9ad-319d-b5ef-7b704a978e2e | -7.26043 | -44.6601 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9ab56c55-d0fa-350a-b629-897f9c0c483a | -7.10897 | -46.10582 | 2025-08-09 04:40:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 46a4a21a-fce1-3018-94e8-92a8e39a8f8b | -3.82097 | -41.56152 | 2025-08-09 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5bbf4975-8d30-3759-accf-a2843c126d78 | -7.96278 | -49.39603 | 2025-08-09 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78d56580-3517-395e-9854-72614a796814 | -6.12645 | -42.95189 | 2025-08-09 04:40:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9ed850ce-0aef-397e-aea4-26a026142750 | -5.8882 | -57.74999 | 2025-08-09 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d044abb8-f1bb-36af-a29e-8184f090c6da | -5.27153 | -44.94808 | 2025-08-09 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81d4224d-3402-378f-9854-4c1a9941c2f3 | -6.06994 | -44.89371 | 2025-08-09 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a071766c-02e5-35cc-b7e5-7495fff742f7 | -6.59501 | -43.3949 | 2025-08-09 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3ab0cb96-9930-393a-bc07-82a111dbb653 | -6.25111 | -44.82967 | 2025-08-09 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddf5265a-16fc-3e82-ba09-0d43b9e217de | -6.13344 | -42.96593 | 2025-08-09 04:40:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 791d39e3-adf2-3603-8eb1-5bf81250bfdb | -4.17357 | -48.5758 | 2025-08-09 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d01628e8-fada-3afc-befd-49c2c66b8312 | -6.4135 | -44.56287 | 2025-08-09 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73cc329e-df4e-3f2e-b72c-2befb3a04aaa | -3.64865 | -48.32348 | 2025-08-09 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53949f32-0343-31b5-b28d-3fc194d60265 | -6.05336 | -43.75074 | 2025-08-09 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6bda7ab-5610-31e3-adf8-4b79dfc5ffd7 | -3.42683 | -49.0415 | 2025-08-09 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bee6698-d6df-3099-815f-50cbc2c3230b | -6.68146 | -43.32671 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c57a12da-dfce-3d69-819a-aeb442a35819 | -5.42236 | -44.00654 | 2025-08-09 04:40:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e77ffbe6-4ca5-3c84-a4dc-a8c9e16db968 | -7.47712 | -44.87466 | 2025-08-09 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c699267-4e14-3401-8123-5e171214bb00 | -6.17178 | -46.14889 | 2025-08-09 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd88493f-6afa-3ca2-9cfc-a463becb7342 | -7.41875 | -43.97355 | 2025-08-09 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db94bb07-7465-3081-a649-3c9adb92fef7 | -6.59007 | -43.3986 | 2025-08-09 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 17792d5a-270d-3f8b-ba7d-2cb8926c67b3 | -6.59848 | -43.37067 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f1595fa6-c9c3-3183-a3ea-28e8c4e14820 | -5.21501 | -46.07516 | 2025-08-09 04:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 173459cb-27cf-31cc-8071-52a4612f7c02 | -6.68173 | -43.35617 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| da298a12-07f9-3f62-ac40-bb58aa06c7cc | -5.08378 | -48.31611 | 2025-08-09 04:40:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 349d1f25-7dad-328d-a233-e368dca21120 | -8.05444 | -46.3295 | 2025-08-09 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04e56ba5-ed20-3c62-8ad1-6cfc544fa8fc | -3.82172 | -41.55657 | 2025-08-09 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2a6c97b5-451a-3600-b0a5-7804c47f5e83 | -4.29971 | -48.07632 | 2025-08-09 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39eab17d-b2f1-3f79-a683-5b4c18fb3dac | -5.20843 | -46.07009 | 2025-08-09 04:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 878d202c-fffc-3a61-b4b7-ce247b178ea7 | -5.00415 | -56.03983 | 2025-08-09 04:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 3d98ac78-c7d2-3097-84d7-c7998b9007ad | -6.58081 | -44.57492 | 2025-08-09 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 2cfb196b-f297-39af-9750-4b366b2d962d | -9.07781 | -40.00281 | 2025-08-09 04:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 048a7c04-e175-380a-b0f0-c04ef2d2731c | -6.62497 | -47.29055 | 2025-08-09 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0395955e-25f9-31be-a976-7c3d73f7c3a1 | -8.15913 | -42.42385 | 2025-08-09 04:40:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 63e26549-2aa0-3c86-831d-6696baf3b63a | -7.40521 | -47.13773 | 2025-08-09 04:40:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10c1fc0a-2e6b-354e-abcd-e7bb16bf36d9 | -5.73369 | -44.50117 | 2025-08-09 04:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52f5f4dc-9d79-364a-9476-8690d98125e8 | -4.00679 | -47.93719 | 2025-08-09 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3fcb326-db5f-39f4-a904-77f5898d0b0b | -8.0775 | -46.84004 | 2025-08-09 04:40:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b62d3d8-3457-354e-95e3-ba674fbdd58d | -4.10795 | -38.1764 | 2025-08-09 04:40:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 662201f7-a6ac-3e7d-b3d8-9d28a07a8472 | -3.83589 | -48.95732 | 2025-08-09 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c67ca79-27bd-36a0-9b92-43035e4e307e | -9.07495 | -40.00486 | 2025-08-09 04:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 37513e3e-a9ab-330d-a7e8-97db45c26e92 | -3.84024 | -47.74982 | 2025-08-09 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 51f6e792-001d-3ae2-b9ee-ec42750511cd | -5.27535 | -44.94868 | 2025-08-09 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14a9bd3e-4a69-3950-947e-5e7e7863b84b | -4.70066 | -48.58401 | 2025-08-09 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6939f41c-14f3-3f94-845d-eca9488305d3 | -5.84825 | -42.95662 | 2025-08-09 04:40:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6ee85acc-87bf-3d37-917f-de60049e05ed | -7.24219 | -44.67321 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11a950c8-6056-36da-9a8e-d3fa398bbc0a | -7.25606 | -44.63353 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf94940c-6abf-35a7-a8d2-3455f106cd58 | -7.29766 | -39.64079 | 2025-08-09 04:40:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 517620f1-a56e-3360-99f8-3192dd7836eb | -4.10856 | -38.17206 | 2025-08-09 04:40:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b0a99fa9-d455-3ae4-af8d-9279c27c7cde | -6.2326 | -44.97491 | 2025-08-09 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e69e959c-4403-38a9-83b6-e4560327c157 | -5.6018 | -47.15401 | 2025-08-09 04:40:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18da1b0b-1ad6-3848-a23f-497f1802c684 | -6.13283 | -42.97017 | 2025-08-09 04:40:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| c68ca323-7933-3932-9c93-4eff3948b607 | -6.68607 | -43.35672 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 893095c4-2bd1-34f0-8c00-e72640de9ac2 | -5.21202 | -46.07063 | 2025-08-09 04:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c29cdbdc-2ab9-3807-bb62-260e6ef5e540 | -3.82274 | -41.55843 | 2025-08-09 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7ff7be22-88dc-3bf8-a808-04912578158e | -7.3981 | -39.68053 | 2025-08-09 04:40:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 68956aed-7b63-3c09-b68b-2bf1c2b52b51 | -6.58158 | -44.56977 | 2025-08-09 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 99030646-4a34-3fe6-be0b-2da39b3d087f | -6.13904 | -44.53774 | 2025-08-09 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6aece19-7dd1-3cc5-8888-0964eb6ed1ea | -7.08262 | -44.51554 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4564f5e9-0d18-387a-b99e-c6ace0370b1c | -5.22757 | -43.19378 | 2025-08-09 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11f32357-a9e9-355d-835a-4d56865528a8 | -7.17037 | -44.39763 | 2025-08-09 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4839da7-879e-3b0e-acae-2f36cf65ddb4 | -7.39247 | -39.67973 | 2025-08-09 04:40:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af11f8ed-0b7f-38aa-83cf-09187c2f08fd | -3.27664 | -48.8129 | 2025-08-09 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c4a72ad-dd3a-3654-acd2-c3365c935ff9 | -5.90284 | -57.71228 | 2025-08-09 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0917995e-3eb7-3278-88c6-c0b5a15aa9fe | -5.21563 | -46.07105 | 2025-08-09 04:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 98e5d879-24ef-3795-af71-702dd810922a | -9.07516 | -40.48058 | 2025-08-09 04:40:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2a723237-0d59-30d9-99e7-d0da734e7075 | -6.62151 | -47.29 | 2025-08-09 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c46f802-7620-3026-b69f-f3f5842891b6 | -6.57758 | -44.56924 | 2025-08-09 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 64738497-f573-38a3-b9c9-e3b442397c2a | -6.6823 | -43.35212 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f0d0d84b-3680-3dec-b264-5ed02ad4ab72 | -6.60539 | -43.38405 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 64948b52-ad81-3f89-9fd1-029fbf6456b2 | -6.96239 | -44.4909 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9d780a5-9d5e-3248-9cf4-83907839057f | -6.92595 | -44.69842 | 2025-08-09 04:40:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c227eb3-e462-3ee8-92c1-fd883872265b | -6.34513 | -55.5608 | 2025-08-09 04:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9e72c97-4a1f-3d9f-b656-0e87c4e00c1c | -4.33836 | -49.35628 | 2025-08-09 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 515ec8a8-ba99-3ed0-92df-ff792f9faa6d | -6.24648 | -44.83413 | 2025-08-09 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06a824e4-bb5a-3f2d-b4b0-78d87de01c90 | -7.32067 | -44.69556 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b06b9f0-c41a-341d-98bb-1eaabad5eccb | -6.42429 | -42.36995 | 2025-08-09 04:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce96ff17-324f-3399-98a9-c39e49d8c60d | -4.14919 | -48.21356 | 2025-08-09 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ef12ec1-3423-3387-9365-bb2413b74aa2 | -6.66953 | -43.33838 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cee816c2-49cd-3850-b53c-8ff97808df22 | -7.24135 | -44.67157 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72f4e905-e115-3a03-9996-09f5a225bcfc | -7.20622 | -44.66029 | 2025-08-09 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce5cf7ad-3068-3892-83b9-695426b85402 | -6.60483 | -43.3879 | 2025-08-09 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 684fad6b-d0a1-3f0a-8c68-3a648d179c8d | -7.57901 | -44.40521 | 2025-08-09 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 357876cb-6d7e-3eff-abeb-7274410b7b1a | -7.26355 | -44.52372 | 2025-08-09 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad298a71-a763-344b-9c1b-8524a2fe7b2a | -6.83889 | -44.31651 | 2025-08-09 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a29e3e5-df21-3dea-bf0a-d02eb506650b | -6.59065 | -43.39453 | 2025-08-09 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README18.md)
