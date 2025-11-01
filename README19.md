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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 409509cc-5cb7-315c-a03f-55957261e0ab | -5.29093 | -44.98951 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38e9aef8-9722-30bd-9f02-9d9dbf3d006f | -3.2224 | -50.58068 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 45149a6a-74a3-3e98-a4f1-bfc06253e4e3 | -6.80334 | -47.04594 | 2025-11-01 04:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76018233-5f26-3861-bf07-0dd368d7235e | -8.82408 | -39.83002 | 2025-11-01 04:38:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2473b6f0-333f-34c3-a480-f25916b08234 | -6.05102 | -47.97464 | 2025-11-01 04:38:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b51b81ac-69e7-3409-bbc6-57fe0793820b | -6.40858 | -49.17547 | 2025-11-01 04:38:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 109dff5b-9295-39d4-92d0-1a1cd18cbb73 | -5.46791 | -48.59954 | 2025-11-01 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fba041ae-b2d2-364e-afc5-c788cdc50ddd | -5.19028 | -43.41505 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5399c9f3-e367-31dd-af5e-4c6484c47762 | -4.92643 | -45.96991 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a7a910e-b8ec-3812-9371-8c5929450013 | -7.13767 | -47.73426 | 2025-11-01 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c30b3630-b166-3ca5-b383-03ffb639c84c | -3.04008 | -53.79378 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3529d32f-204c-3772-9942-c249542dd7a6 | -4.87491 | -47.52768 | 2025-11-01 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd53ec23-f8cf-31bc-9bbb-22030cc3c257 | -2.52878 | -45.84839 | 2025-11-01 04:38:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57839773-c964-3001-86af-4f7f386037b7 | -9.07809 | -49.77046 | 2025-11-01 04:38:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87a107a6-a702-3f19-a3f0-395028a4a3e0 | -4.75832 | -44.4641 | 2025-11-01 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56456362-dce0-3fca-873f-c3425c4c785d | -8.56444 | -40.91167 | 2025-11-01 04:38:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5a9af4aa-8d16-39bb-b951-0b716a59abe3 | -5.1151 | -43.39365 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdb09fe9-5bde-3800-a28e-b91401612c0c | -1.8083 | -51.02973 | 2025-11-01 04:38:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44c8dbd1-8df0-39fe-85bc-61e9c377ec8e | -2.65166 | -48.50532 | 2025-11-01 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2ed1d52-f1f9-3f13-8308-91f27fe6d5d3 | -4.91801 | -47.95526 | 2025-11-01 04:38:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44020e15-f045-3713-a66c-1d37c38685d5 | -3.47754 | -53.49853 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65fe94f8-0e15-353b-b2d1-c5126b22b707 | -3.10538 | -45.23276 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cb36fa00-8acb-331e-9a42-9d2f1c5363d0 | -3.4916 | -50.2135 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd26f35f-4369-3733-8fcc-88b3b638e201 | -6.39784 | -47.548 | 2025-11-01 04:38:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e643cd7-dab1-35d5-bb8f-29b2cc20f87e | -3.07694 | -51.24389 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aaedc4c6-25b0-342c-8ce0-b2b1c64dd8d9 | -9.17775 | -43.23338 | 2025-11-01 04:38:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 07cb2bd3-14a1-324d-a116-cb988a5ee7e8 | -5.01256 | -46.85579 | 2025-11-01 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06082817-5334-3286-ae8a-be66f4ae15da | -3.41376 | -49.99578 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc4ba810-619d-359f-9602-714149c8870b | -6.61898 | -47.17799 | 2025-11-01 04:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f83a8251-8675-35ba-ad02-6c0afca6254b | -2.88832 | -40.46769 | 2025-11-01 04:38:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b77084a7-f330-384b-8a91-67722ffa222d | -4.61731 | -46.59637 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 370a6496-82e5-393f-b875-093c295e43d5 | -8.97525 | -47.77737 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f8bb2aa-4512-3147-903d-e31f27d25f78 | -3.57453 | -50.26767 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0333f8c0-a509-34f9-b61e-b24f00a7bce4 | -3.11395 | -45.2254 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c58a5762-6819-3f27-925b-095cff1b0e95 | -4.70654 | -46.44418 | 2025-11-01 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 938c6b3f-fbe6-300b-a550-ea6d4d7b3781 | -1.92903 | -54.0608 | 2025-11-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a592b78-64b4-3763-bcaf-8ee7efc5e12f | -4.96075 | -40.55116 | 2025-11-01 04:38:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 02ca94b9-ed26-3d37-8bec-f170e4910d1c | -4.45474 | -44.21548 | 2025-11-01 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e469acca-3936-3fb4-94af-3cb39774ac69 | -7.32004 | -39.37364 | 2025-11-01 04:38:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 99ed00fa-41b0-3841-94c7-4c3a57b10f80 | -2.95608 | -51.52114 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa62159a-3d93-30b8-a233-2cfa59a18f65 | -7.35412 | -46.21249 | 2025-11-01 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69f8ec50-c86a-323d-9492-cbcd61d5acb8 | -4.64756 | -45.38659 | 2025-11-01 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f038668d-d10e-3530-899b-f12f7dcd7fe1 | -1.96356 | -54.06179 | 2025-11-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a4eba59-2071-34bf-b2a1-595db68ea614 | -2.91156 | -54.29216 | 2025-11-01 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e67019ad-5e1d-3e12-bd4b-83b5554784a7 | -3.42816 | -50.10059 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c3feffb-e62f-3109-9f89-9136b8c62adf | -8.82358 | -39.83385 | 2025-11-01 04:38:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cccf6fb3-d074-3d77-970c-d3e200ac1c06 | -4.67717 | -50.44371 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08be1859-4355-3ca5-a584-13d7f340dbec | -5.06821 | -43.95769 | 2025-11-01 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7482174e-0b5e-32ae-9d30-e2e309c6efdc | -4.95158 | -43.45181 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 373d6e78-10b7-3073-afb7-c0b3b68876ad | -5.64294 | -43.99121 | 2025-11-01 04:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbba05e5-9c12-336d-9e93-bcf0e153c3f6 | -5.45133 | -50.90055 | 2025-11-01 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| af73f0f4-3170-3dcb-b599-1ec0308811b5 | -8.71444 | -41.58646 | 2025-11-01 04:38:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3a34ad2-1072-3a8d-b733-7f497b5454db | -3.22948 | -50.64669 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f250d7a-64d3-3613-ae6b-4e3af3123521 | -4.18272 | -47.65425 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 534cf362-73f4-3e68-aa19-1294d2148c79 | -3.23609 | -50.58282 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 00154544-0c64-3fcb-ada2-e593fda6ccee | -7.12098 | -47.00564 | 2025-11-01 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ca01b5c-9ea0-3c69-be78-4ac4b1727ee3 | -7.07705 | -48.3105 | 2025-11-01 04:38:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd32ed6e-0919-3969-b165-0038c45989c0 | -3.10668 | -45.22431 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a61a1b5-6efc-305f-aaed-0b91689af70f | -5.66878 | -44.23257 | 2025-11-01 04:38:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 061bbcd9-5ac0-301d-8aeb-566c4be00482 | -5.82282 | -47.5396 | 2025-11-01 04:38:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed9c1f99-12fb-3486-9096-590a63f3cb98 | -4.81339 | -45.75599 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54c74692-89d1-3a8f-8dfc-bc79e0544536 | -7.03256 | -37.24748 | 2025-11-01 04:38:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 445e498a-35ea-3b14-830d-3e1ac1433869 | -2.91138 | -54.2927 | 2025-11-01 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfafac87-1e54-3e3c-a4ae-f3087dcf45dc | -4.96582 | -40.55199 | 2025-11-01 04:38:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8444323e-97cf-376d-991a-2b6e91f0d3bf | -6.88759 | -42.84544 | 2025-11-01 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 6b36c6da-5219-3db8-8271-12fe0b9b6d78 | -5.10135 | -44.2677 | 2025-11-01 04:38:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6d74655-5cd3-33f4-a9ac-89f7be147caf | -3.60162 | -50.62429 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2678513-86b9-319a-b274-4d88e63e7f27 | -3.38005 | -51.06972 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f887f8f3-7554-3ad5-8bbc-81abbc0fe74f | -4.29645 | -46.25785 | 2025-11-01 04:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e16eb87-4de6-324e-9365-a4f6cd91cfc5 | -3.41542 | -50.007 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a98d099-be9d-30c0-9f2c-28ca37ef0bea | -3.04301 | -45.82401 | 2025-11-01 04:38:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21897486-6c8b-32e3-8122-729f9276e0a1 | -3.57172 | -50.26355 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d06e4f91-a58e-30c0-90ec-58c7e305a155 | -6.61956 | -47.1742 | 2025-11-01 04:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 70d25dba-9cc7-3bff-9c07-29bb7205211b | -3.01979 | -53.97126 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a606a145-2905-35cf-bc3e-4906c58d61e0 | -7.12572 | -47.2571 | 2025-11-01 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2531bc7c-f5ff-37cf-abe2-5e0cdd9a5488 | -4.80553 | -45.75928 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb92a34d-5aa3-3e46-bd0a-9c0f6776137a | -4.21578 | -48.09538 | 2025-11-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48240f4e-8368-328c-8453-00733c989a69 | -3.49544 | -51.55192 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fa1eed0-1e49-3e8b-8e1a-d6fd8363f1e6 | -5.77403 | -47.65418 | 2025-11-01 04:38:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51c3f5aa-c7df-385f-bedc-884385dd6b0f | -3.87942 | -52.26758 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 359d5616-7e9f-30ae-b2fc-374fc79b2e3c | -5.88576 | -44.52558 | 2025-11-01 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6714ac8c-19fe-3aeb-a4e2-089ce0432118 | -3.26749 | -45.32698 | 2025-11-01 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d40bf127-41c8-3ccd-964f-74e9d13d20f8 | -6.53774 | -48.03445 | 2025-11-01 04:38:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd0cc88e-54e3-3a8f-bc54-6ff52438e8dd | -4.8096 | -48.71896 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba192d53-16ec-35c8-917d-f1833aee58f7 | -3.58632 | -50.8089 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3ee7b8b-c23b-3ec2-9b50-12dcbe117dca | -2.79563 | -50.2838 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de199729-711a-37eb-a80c-cd4d76b114dc | -3.43814 | -42.54385 | 2025-11-01 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e359fab-fad1-38f2-b6cd-0f981615b066 | -4.03166 | -47.77119 | 2025-11-01 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1913cd77-2041-3327-8a47-50a1d1575aa1 | -6.88313 | -42.84485 | 2025-11-01 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 2be483aa-cba3-349b-8f41-a984d15d7020 | -4.96118 | -40.54817 | 2025-11-01 04:38:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 284d8e1a-d0d6-3f2d-8c97-442f579a84cb | -2.59583 | -51.34793 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 755ee295-9fe6-3466-8f68-ce92741e8634 | -5.73465 | -47.36162 | 2025-11-01 04:38:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faf991e0-47d6-3ab2-a46e-d394b338c241 | -3.2355 | -50.58654 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a62a583f-e411-334e-8ad6-ef820b813788 | -5.12041 | -43.38665 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d8fd351-cdd1-3fdc-9b34-9605aad00afb | -5.88028 | -48.15399 | 2025-11-01 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95db7a6b-620b-300b-8636-8935170e0750 | -5.56767 | -47.33281 | 2025-11-01 04:38:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d13be57b-2152-38f0-af78-dddaccda8a03 | -3.32594 | -52.62584 | 2025-11-01 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1b040fa-195e-3870-b067-65f1c95db756 | -9.09594 | -47.79123 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce6afc4c-92ab-3f2c-ae89-09bc9e17c404 | -5.13623 | -48.32437 | 2025-11-01 04:38:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e23cd9ec-93dd-375d-84ba-fd747d155be0 | -3.4888 | -50.20937 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
