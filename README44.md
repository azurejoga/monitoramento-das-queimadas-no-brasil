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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bab49b1-72d5-39b9-8b41-413c65ed9dda | -4.86914 | -49.97887 | 2024-11-10 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3029fcc0-fd73-33bc-b23c-ab4a7ceeeb78 | -1.05133 | -47.89261 | 2024-11-10 04:14:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f07352ca-698a-39e0-84e8-3375b4c0d132 | -4.17904 | -46.57697 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 054060b1-d19c-33ff-915d-e37def85d009 | -3.08939 | -51.11723 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 210b559a-96e1-36f4-abed-c6a2a16caf2d | -2.30031 | -46.1834 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30f07463-c073-359f-b0c2-4724856450be | -5.81521 | -44.12225 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0aea19d6-3c58-38e1-9109-c59c3ebd0efa | -3.44751 | -51.46603 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 421ad8df-1755-340a-a541-034edf43d65b | -0.9462 | -52.4446 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cef38c8f-7382-3619-acaf-b383138aff79 | -2.89416 | -48.30287 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a5338ee-845d-39bd-bcdd-327a285796e3 | -2.30164 | -46.72622 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30001e47-ac69-370b-98ed-dd41e7d0ca2c | -3.55772 | -43.57257 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2b1ac26-14da-36b4-9eeb-aa51b1944acb | -4.10123 | -49.10925 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 501fa0de-f47e-3263-9615-bce40c352b3b | -3.80699 | -52.20761 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d484bcf-a373-315a-b630-578cfc8e551c | -4.28112 | -48.18432 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fa2076d-f004-3952-bf5f-f40e4ffb644a | -4.09117 | -38.65686 | 2024-11-10 04:14:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2b9783b8-3133-30f3-b1cf-2715e53ead51 | -3.05366 | -48.03694 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 045c10f8-93f5-3dbc-8f50-399e3b619376 | -3.59467 | -50.27351 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4fccf1d-0934-3d4a-9fe2-5fcbed94ea62 | -4.05637 | -48.30816 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7703931-cd36-3b5e-b504-0c91947ac69a | -4.09845 | -49.12662 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb6e3ff9-04c3-37a2-b333-64c7cdf3da4e | -3.96175 | -43.68609 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 005d04de-91e5-3823-a7a9-09a78156fbb0 | -4.51447 | -45.6816 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1767a3b4-d86b-35f3-abc4-f2a22ff00d80 | -5.38198 | -42.76218 | 2024-11-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4deab04c-024c-31e4-bc4f-afd6ef8e5ba4 | -4.71362 | -50.84537 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3aa2302d-c7e8-3858-b4d3-9d09b12c09a2 | -2.95348 | -49.57485 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 311394b7-e238-3164-9d85-7f68ecbfb41c | -2.58643 | -48.16651 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02793962-680a-37fd-8d85-54959315e947 | -3.12884 | -50.14969 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8895f586-17b4-3bdc-8961-1c366be1a29c | -5.30333 | -47.89017 | 2024-11-10 04:14:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dec565b-42b0-30ef-bbd0-62f1e31e4138 | -3.69203 | -45.81016 | 2024-11-10 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 134e635d-fa78-3283-859e-d7b8ee99a061 | -2.2273 | -51.99285 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5de743a-b5a6-352e-bead-66614a9e04e0 | -5.08514 | -47.79607 | 2024-11-10 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ec9533e0-f711-3d6c-ba93-4f887dd93bab | -2.80406 | -46.64919 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5df2d22-0acc-3028-bf4c-2961f3f23e8e | -2.21073 | -48.37274 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 71ae353a-2753-350a-bcf4-cd90ace6c2a0 | -3.23557 | -50.31012 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 4ce52c11-d4c0-3be6-a73d-34b466c0d079 | -2.46683 | -48.44446 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c8d37de2-1310-3890-8941-910cb86d16f8 | -4.61395 | -45.98407 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 189058f4-8cc3-34fa-9c84-797668c75262 | -1.31287 | -54.66868 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c59c338-20d0-33ce-9f00-c4464dd4d8db | -3.20954 | -50.317 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a4ab8f2-b739-35d2-8762-6a00feaf098e | -4.8555 | -46.97734 | 2024-11-10 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d343e0f8-1a6c-3efc-af3b-76c9dd428f63 | -3.09849 | -48.0605 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b109309f-2197-35f2-b94d-6f7921d803f6 | -5.68613 | -47.62099 | 2024-11-10 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e7e72d2-ebe0-311e-bed6-d987da1d61da | -5.30811 | -46.23308 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1625b09-de5a-3476-8ed9-0231cd493e6c | -2.46691 | -50.3993 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6b73f472-2221-37a0-babd-621996de8263 | -2.55902 | -50.68003 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2d71200-d5d5-336b-9102-2de8ed0dcd6b | -2.8539 | -48.44465 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7846d690-7d9e-3344-a0c4-6ab05b697141 | -2.17533 | -48.87981 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87e4793e-bb39-358a-ad3b-472b498aa668 | -3.10211 | -45.95707 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b928eae-8cf7-39d3-bdcc-1460b5d5665d | -3.42215 | -53.05573 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4d14ed8-0fb5-3df7-970d-0330a4abdac8 | -1.53379 | -52.21293 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b8f3af2a-978b-3de7-b956-f0ad31a3070f | -3.03395 | -48.0533 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2ef0a56-d72c-333a-aade-0b9bd1acf8ba | -4.51384 | -45.6856 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9c052e4-19a1-3767-a8a1-877b9a4af5b7 | -2.39499 | -47.71484 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c65290ff-36f3-37e1-82c3-ee1b54a6cb19 | -2.1673 | -46.8298 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c170492f-cc18-3ac8-9e98-0023f94bea96 | -4.12038 | -48.50059 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e7f92d7-fbe8-3f97-a88a-aeab6f733cda | -4.644 | -46.02674 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 251957fb-7e4d-36fc-b1b7-0aa70ff5f27d | -5.8041 | -44.04139 | 2024-11-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a054f94-1168-31ac-8459-2c0747e1c02d | -4.56764 | -45.41416 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a46b9fd2-4232-30d1-a0ad-afd5d4f2e0cf | -3.89173 | -50.08366 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f472a03-887b-3a5f-8941-a5c657a96704 | -3.02919 | -51.09822 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fce5b81f-b36a-39b9-92c3-c05b040b76f4 | -4.89669 | -48.61072 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0687a50d-bf25-36c7-815d-5c33a02c4aba | -2.81337 | -51.80956 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c216e6b2-c369-33cc-a3f9-35855cd156d0 | -4.49442 | -48.49533 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed2c13bd-bbcc-31f1-be06-6017bc54f5b2 | -3.05704 | -51.38158 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a41968b-4ab1-3caa-a8eb-bd39b3fdbc0a | -4.72434 | -45.63922 | 2024-11-10 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8871e0ac-d1a2-3ca9-bd50-cc665760af8c | -3.35762 | -53.40729 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5d273af9-c6cc-3a36-b565-45b4a5f6ff30 | -1.18716 | -52.16713 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50b39199-2690-35e7-8a7d-e29c6e9e95ae | -3.72944 | -54.73988 | 2024-11-10 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d8b29d9-72fd-3d35-bab6-91debd4b5e05 | -2.20707 | -48.36798 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1b58f19-7ee9-3258-8e89-f996392c9315 | -4.61234 | -45.97128 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6c00579-a796-319b-8eab-a35f87e86af5 | -3.14322 | -50.44577 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc6377cd-3cbf-3a2a-bde8-3f48ca6d3313 | -2.23871 | -50.72056 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc20bec6-8cd3-3fa5-aa31-baa9544b3183 | -2.445 | -46.32058 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f4bcfb0-2f92-3423-a8bb-12ae9fc7517a | -2.35189 | -46.66025 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e45e45d5-6d3f-37c4-9f2f-2ea0781d0cb8 | -4.32091 | -49.76324 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c41467f-9168-3369-b60f-d39214e90158 | -2.64811 | -51.87806 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e02f256c-5f23-3d2a-a04a-98ee59ebf05d | -3.97325 | -48.17787 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5451bca-89d3-3124-84ff-0ee1af92ecbf | -3.8776 | -46.61312 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18efbd46-7d82-3eee-8727-e2eae3f46ce5 | -2.7681 | -49.52968 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf485723-b0b8-3212-8db0-a374099375fa | -5.05591 | -44.27786 | 2024-11-10 04:14:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 809bd9fe-26c8-344c-a3b9-4b18f0a09647 | -5.46109 | -41.6569 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f5de3711-4994-3e4e-9f59-66f1102aabf4 | -4.11541 | -46.92185 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e643eec-acab-379f-baf4-53b3d5331670 | -4.10661 | -49.13076 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66523860-160d-3d16-8d32-97aa51baab73 | -3.95806 | -48.14092 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4409ad3-892b-35da-9cb8-d01d6755c07e | -3.02973 | -51.09499 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3327191a-729d-3dfa-ad0d-8e0a3500bc62 | -2.40841 | -48.49136 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4156a223-61d6-3707-b52e-00a569235e7c | -5.55613 | -41.65718 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 469baf53-0338-3c31-a699-5311abdedabe | -3.00201 | -49.04037 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e27183f-d495-3af0-94e9-332b134365d8 | -4.11924 | -46.92237 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b458b097-774b-35d7-9e59-eb6eddcc0022 | -3.11538 | -45.9679 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4ce8ed3-c456-3cd0-8a12-9d4bd9fb4571 | -2.81172 | -46.65034 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d54eb5a8-4c57-33bd-af5c-86850439a1f6 | -3.97315 | -46.16219 | 2024-11-10 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 503cb5e5-8417-33a5-894a-9d65bc55d757 | -5.69019 | -38.0373 | 2024-11-10 04:14:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6cd17509-679d-398d-a2f4-a76774bd059e | -3.2211 | -50.38721 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df0702e4-581a-322c-9f2f-3f1eb9c433e1 | -3.59656 | -44.93385 | 2024-11-10 04:14:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 320cbc12-db2e-3e7c-99ae-67de5c41a5b1 | -3.22751 | -50.45372 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 69dc2697-eec2-3bd9-9c0e-5bb8ddea390d | -5.29434 | -46.22642 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 258d637c-b368-3f2f-9e57-1b88e4a1aea7 | -2.87517 | -51.30691 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f739043d-7091-373b-85a5-5872982f5e5a | -3.0766 | -50.5643 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5194edb-b73b-3f31-bedc-ecf8af74ae7c | -3.12761 | -50.4357 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 2b49bf09-1a4c-3255-a9f3-12b9f291fd08 | -2.21201 | -47.74004 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a10a2240-d76d-3843-90f3-d50612932b4a | -4.2569 | -48.54189 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README45.md)
