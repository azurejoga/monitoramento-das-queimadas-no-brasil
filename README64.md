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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba22fbc9-5752-39ac-b558-6558935ae49e | -6.19315 | -43.42347 | 2024-10-03 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f43e78a-9848-33a2-b7b2-25824c7861fc | -6.19251 | -43.42712 | 2024-10-03 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4c1bb99-edd3-3172-988a-c4e56c885783 | -6.17422 | -43.21231 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4bf4ba44-0bcc-390b-ac1c-7476b0b3cd86 | -6.17356 | -43.21619 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8b75e1ec-c176-35ca-aedc-87766cc579aa | -6.17282 | -43.21518 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 333ee91a-3c99-3c7c-a4f8-de80836deb2d | -5.88062 | -43.43184 | 2024-10-03 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb245989-b78d-341f-8ba1-ab7b062a650c | -5.875 | -43.43069 | 2024-10-03 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dacf89f2-9e51-3116-a0ad-15142934d06a | -5.87431 | -43.43461 | 2024-10-03 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebd00a7d-fb8e-321e-86d8-d27bf5e31fd1 | -5.71661 | -43.78795 | 2024-10-03 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ad50684-846a-3ae2-aeb1-5b7a93ef3a52 | -5.71588 | -43.79212 | 2024-10-03 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ba959dd-464f-3746-820e-1eedacf03d8b | -5.70863 | -43.93157 | 2024-10-03 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3959e617-fd53-3562-bb4a-3dd876e19feb | -5.56761 | -43.11271 | 2024-10-03 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 0ddd4ec8-604f-39fa-aee3-d86bc163d974 | -5.56208 | -43.11159 | 2024-10-03 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d4d5a9a3-f78b-31fd-844a-a4aac57a90ae | -5.56144 | -43.11521 | 2024-10-03 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d1423fa4-b05f-3cee-a149-2550cecc0a9a | -5.53593 | -42.77744 | 2024-10-03 03:34:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 20bbc15e-1368-384d-8cac-f5ce6cfb0eb2 | -5.52987 | -42.78008 | 2024-10-03 03:34:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 77229eb8-ce6d-3298-ae9b-b9f490417f76 | -5.5244 | -42.77928 | 2024-10-03 03:34:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4cf8fc56-e77e-3a88-a52d-5f9d3dd071c0 | -5.408 | -42.9251 | 2024-10-03 03:34:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b419c266-6151-3656-a086-63d181379243 | -5.4025 | -42.9241 | 2024-10-03 03:34:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 74d3a251-5de0-3f51-b010-8586ef93d98c | -5.39862 | -43.11035 | 2024-10-03 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13cb0620-3bd2-37ce-986a-5692c59b44d4 | -5.39799 | -43.11403 | 2024-10-03 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23f6c6aa-4ed2-3196-805b-8a623393f7b9 | -5.39369 | -43.10575 | 2024-10-03 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8d5d77c-29ff-3392-b121-4f0d438f0b40 | -5.39304 | -43.10945 | 2024-10-03 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbb70377-677e-3377-ac02-8111099155c4 | -5.39241 | -43.11312 | 2024-10-03 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b26ed228-8378-39c5-9eab-063a80af34cc | -5.38033 | -36.82168 | 2024-10-03 03:34:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8788a3e-1ddd-338e-b07f-1f02044f0474 | -5.32076 | -42.97194 | 2024-10-03 03:34:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bebfb9c5-eb0b-3759-929a-7f39c237b9e0 | -5.31585 | -42.9674 | 2024-10-03 03:34:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 33b5928d-23ff-3bd3-8859-65938f4dd93f | -5.24665 | -43.81231 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6afdd51-a684-3afd-826e-e5e1d4fc80a4 | -5.24228 | -43.80297 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7229860d-a9ef-30bb-a768-780daf3602a0 | -5.24154 | -43.80714 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b7cbb48-866b-3e6c-8939-7643719470cb | -5.24081 | -43.81129 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 368c7973-c6bd-360d-b1ca-8ecad9bfc9c3 | -5.23644 | -43.80196 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b41b0546-6ed2-31ae-a8e7-1d0d5394e1d5 | -5.23569 | -43.80616 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a10b787-92fc-30aa-ad50-06d3cb7eb8a3 | -5.23496 | -43.81031 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a93d43f5-260b-323d-945a-244860cdf248 | -5.17013 | -36.56954 | 2024-10-03 03:34:00 | NOAA-20 | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 149493b4-4848-3f24-89e7-43d235fe0afb | -5.10526 | -43.32634 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 956ddd2b-706f-33ed-9448-d207a3d2f5d9 | -5.10457 | -43.33023 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bd4c5ed-ced1-37ac-9bb3-40415f0617aa | -4.94095 | -43.68427 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcc2db9e-0c73-3ca2-ae51-2bf6e56cbbb8 | -4.93075 | -43.77679 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 398b4c5f-15ff-3db2-ad12-4cb8af66c28c | -4.48737 | -42.88068 | 2024-10-03 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| ff6d1dc7-1f94-36c7-8033-5ca68d222833 | -9.70164 | -36.65295 | 2024-10-03 03:34:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 07ea2041-1435-3ac3-8bc7-4fe2444fdcc9 | -9.49027 | -36.06086 | 2024-10-03 03:34:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd04ba2d-9e36-3ef7-95da-965a5f63ca06 | -9.2517 | -43.4978 | 2024-10-03 03:34:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 00daa4b2-c475-3832-bb9a-7ce5ca3bea78 | -9.01847 | -40.26549 | 2024-10-03 03:34:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 41f04129-3952-38ab-ab2a-4679c65f78b1 | -8.92474 | -45.64448 | 2024-10-03 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 16096d6c-95cf-3d05-a5cd-6d7f929edc9e | -8.85661 | -35.16444 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| f51b7d43-0399-3eb8-a03d-b423c1e1751a | -8.85502 | -45.50994 | 2024-10-03 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 744d60a0-7bf9-3e21-a83b-12c6ca8a81ae | -8.85492 | -45.51133 | 2024-10-03 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| adf0fb74-277d-3510-bf9c-1d53f194b8a6 | -8.8541 | -45.5147 | 2024-10-03 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 15b11dd4-40dc-321b-b23b-2e1aabe008a8 | -8.85403 | -45.5161 | 2024-10-03 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c6a835b7-c931-3b56-a0fa-70b092866451 | -8.85327 | -35.16389 | 2024-10-03 03:34:00 | NOAA-20 | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a857e1d5-9734-358e-a6f6-209ca90060d9 | -8.85317 | -45.51945 | 2024-10-03 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6ca06fb1-7e2d-3e03-9afa-c8d0be4b3523 | -8.85314 | -45.52086 | 2024-10-03 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b545915a-fc7d-30ab-a16d-d3b4c1d3ce46 | -8.84881 | -45.51011 | 2024-10-03 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 5bc1e503-f238-3a4c-8aa6-6f4241574b7a | -8.84792 | -45.51487 | 2024-10-03 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| de7e9fad-cb4e-3114-930d-3c79c88b19f8 | -8.84702 | -45.51963 | 2024-10-03 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 149f7843-38a6-367a-9705-d906f1dd0936 | -8.48484 | -39.89042 | 2024-10-03 03:34:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 41749ce7-ad25-3b50-9103-d294716f15f1 | -8.48393 | -39.88897 | 2024-10-03 03:34:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b57bc1ca-1811-3f42-a2aa-0789b364e434 | -8.48322 | -39.89301 | 2024-10-03 03:34:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2550a61a-ee54-395d-8c08-89963161d892 | -8.43783 | -41.93375 | 2024-10-03 03:34:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f40b0c6f-e74f-37f7-8608-63247d02e3c4 | -8.435 | -41.93648 | 2024-10-03 03:34:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c873677b-f6c1-3e9f-a300-a546cdccf09b | -8.42921 | -41.94069 | 2024-10-03 03:34:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fa056170-82a3-38cb-b6fa-33ef25303369 | -8.3105 | -42.83012 | 2024-10-03 03:34:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1bb167a9-a210-37ab-b12b-4bc0865cd889 | -8.30992 | -42.83332 | 2024-10-03 03:34:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33e1a036-f56d-3bdf-b196-98eb22d8ea33 | -8.21327 | -41.4067 | 2024-10-03 03:34:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eca1e509-4783-3994-b94b-4a5a7a9626ea | -8.18724 | -44.37114 | 2024-10-03 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 10a58918-6037-3c84-bfb1-fa801556ffb0 | -8.18648 | -44.37528 | 2024-10-03 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fbd6cda8-2da7-3421-abaa-612ddaf267a0 | -8.18149 | -44.37001 | 2024-10-03 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3a694ba-7c70-34f7-a12d-4c27793a3751 | -8.18117 | -43.68911 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01aa7130-d9b3-394f-b0b3-f44ceca65ec7 | -8.18049 | -43.69283 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 512fe242-2994-3624-87b5-16d9af662979 | -8.17981 | -43.69651 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0854773-932d-3ad9-9693-408d85bdc274 | -8.17916 | -43.70009 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b28093b8-9e93-3b6a-b588-3c34f8204ace | -8.1785 | -43.70368 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 218b2b69-ff19-304d-9f23-692792ba096f | -7.68831 | -42.98805 | 2024-10-03 03:34:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 97ff7e5c-d886-3032-8765-9bcb912634f5 | -8.1592 | -43.71545 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e2ac9af-55e9-311e-95fc-fd19031d3712 | -8.15852 | -43.71914 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 65fbc2f2-b522-3a8a-a7ca-25ebbdf9615b | -8.15783 | -43.72286 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b640742d-f454-32c1-9de8-d6365ec15661 | -8.08387 | -42.88729 | 2024-10-03 03:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b54ef520-d80c-38bb-b21b-4b1a8bc7f83d | -8.07984 | -42.87971 | 2024-10-03 03:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7a2bacfc-b336-39dd-9ed2-37ce9cb21b92 | -8.07506 | -34.97668 | 2024-10-03 03:34:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 78ee3cf2-f4ef-31c1-8106-46a14d599aae | -8.07172 | -34.97614 | 2024-10-03 03:34:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b0bc3ea7-87ef-310a-a198-cacf2fa3e49f | -7.87444 | -44.97041 | 2024-10-03 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c124722-8f08-3b18-bd22-bdc42b8ed0cb | -7.86175 | -43.10197 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 372fc067-79b6-3a8a-912e-afad8b70f66f | -7.85961 | -43.08327 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f236afe9-e4a2-3b96-802e-1308f8cf984b | -7.85899 | -43.0867 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d7a8944f-2ba3-39ac-a05d-0ab82ca2fd42 | -7.85709 | -43.09724 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 40efc5d1-f541-3ca0-9ce4-02373927fe21 | -7.85646 | -43.10074 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb675873-ba7e-3ea0-8682-652db76387a6 | -7.81445 | -43.08906 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2b204660-a30b-3953-962b-a4ad3b9c765e | -7.81147 | -43.08754 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a175710-faa5-3d01-954c-06be46bc64cc | -7.80914 | -43.08793 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fbe33cdb-80bb-3542-9834-c1e9d09b56f7 | -7.80614 | -43.08645 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e594cec9-bd40-3fec-b45b-9e04008045e2 | -7.80552 | -43.08997 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 013100f4-9ed1-320d-932f-9cadc2e3e80e | -7.80381 | -43.08689 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e282dec-c9f7-3b03-aae0-6d131fe55a93 | -7.80316 | -43.09044 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 801f077e-00fb-3a07-acd7-ae788e36eb78 | -7.75526 | -43.06271 | 2024-10-03 03:34:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e0946aeb-fa12-3b3b-814a-89c48a7a4ed4 | -7.75249 | -44.03899 | 2024-10-03 03:34:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 679985e1-94fc-318d-93e3-fbadeb006866 | -7.75047 | -44.04026 | 2024-10-03 03:34:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80df5acf-10b6-3e36-ba3d-912b87432f0c | -7.74675 | -44.03825 | 2024-10-03 03:34:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe0c13ca-44d5-3f81-9721-19575ddeafd5 | -7.74474 | -44.03947 | 2024-10-03 03:34:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f553dd2b-0526-3aff-a0c7-a5d10613d987 | -7.70483 | -42.98772 | 2024-10-03 03:34:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |


[Clique aqui para ver as próximas entradas](README65.md)
