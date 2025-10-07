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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 351b798f-eeed-360f-8379-fc733e89dbf2 | -4.06813 | -44.53887 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 7d9d9289-0806-3d0d-a42e-d49088165ea5 | -6.4889 | -51.70155 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1990a08e-6fe1-3cdb-8cf0-cb422fcf826a | -7.01363 | -49.33527 | 2025-10-07 12:36:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d06f70e3-dcd0-3dd5-8436-9e7f0b95bcb0 | -5.43964 | -43.34712 | 2025-10-07 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| eda79151-2aff-3652-849a-e5eba584f958 | -8.1979 | -44.20645 | 2025-10-07 12:36:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 3316c964-3372-3eff-a9ce-0b9820f58b20 | -5.01804 | -43.66974 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 44490e07-0cc7-38af-85be-4075e262f7e7 | -8.10011 | -44.77914 | 2025-10-07 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 34600f96-180f-3d56-9ece-e31d1b6cd509 | -5.69768 | -49.32179 | 2025-10-07 12:36:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3a7f5348-7c1d-3857-b07b-f9e9ba6ff77a | -8.08763 | -49.5541 | 2025-10-07 12:36:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4787bb9a-4230-3ae7-8416-ca36a2f72076 | -6.15526 | -52.79831 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 722e7bf9-64fb-3a52-9478-7fc57ac07349 | -4.06345 | -44.51003 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 407eb3d2-9b17-3d87-aae9-b988b839a03a | -8.67747 | -47.08401 | 2025-10-07 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 7224823f-56f3-3e9c-912d-8b2ce2e6f5e3 | -4.8837 | -45.18509 | 2025-10-07 12:36:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d6243657-6ff3-3d1b-8954-8bb4df8a801d | -8.13745 | -50.25519 | 2025-10-07 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| aa85dfa0-02a8-3899-87fd-28abbe67b654 | -4.06035 | -44.53227 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| debb95e9-202c-39e8-836b-b5fe81f6a8d5 | -5.77198 | -43.47339 | 2025-10-07 12:36:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| cabdf772-7643-3f1d-84f6-a1e31d8f9f1c | -5.71426 | -44.8411 | 2025-10-07 12:36:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 5a811dda-6a71-3175-a3a5-ba553ebda481 | -4.88553 | -45.17987 | 2025-10-07 12:36:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| aee5df5b-792e-3459-9237-9cbbc7cd3cd6 | -8.87865 | -46.8033 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 1eafb3c9-8d35-3535-8d79-de0e6c18f4b2 | -10.2559 | -44.35098 | 2025-10-07 12:36:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 5a4e2126-c5c1-35cb-84b9-94ac677e62a6 | -8.88976 | -47.66246 | 2025-10-07 12:36:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 8290147b-3082-3cad-b262-7051e7b09265 | -8.53449 | -46.24692 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 557a1709-2660-3345-84b7-4a8c1562a068 | -9.04023 | -50.59266 | 2025-10-07 12:36:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 382ea59c-756a-3b80-8d7a-03c3640064b2 | -3.48794 | -48.94083 | 2025-10-07 12:36:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fdae8020-fa42-323c-a500-7e95f1566f85 | -8.49949 | -46.32092 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 3105f568-cc43-3729-9e62-db8ea56259f6 | -5.20989 | -43.59504 | 2025-10-07 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| bb2077fb-12d0-3b88-b15f-25f81251c208 | -8.87512 | -46.77257 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 4bc0d50f-cf96-361e-a5f0-b7fb71c40c21 | -8.88291 | -46.8094 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 799d422a-dc0f-3e16-b7ea-8fe130dadbdd | -8.54948 | -46.23042 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a24de6cc-0cc8-3a0f-952e-dbe5905fd6f5 | -4.07108 | -44.51665 | 2025-10-07 12:36:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 267.1 |
| a3924fdf-0e0f-3a55-8013-27a3b8dc7a65 | -8.19816 | -44.19963 | 2025-10-07 12:36:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 201.4 |
| c5cbc8fb-a037-30a0-b164-5f34f9c53c6f | -3.7028 | -49.69595 | 2025-10-07 12:36:00 | TERRA_M-T | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ecd0d01f-d702-3909-9df8-f515a5ad9f7b | -3.6499 | -48.44426 | 2025-10-07 12:36:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9a31290d-573a-3561-9ff5-530f5ea6fa46 | -4.05233 | -42.50196 | 2025-10-07 12:36:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 160.0 |
| 61f2227e-73b0-3cc5-8b2c-5fb63726a98b | -9.0416 | -50.5827 | 2025-10-07 12:36:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 4f0da2ab-99cc-3ce1-8d72-01f6bfe714bb | -3.20191 | -51.01385 | 2025-10-07 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 99f99906-9357-3575-959f-89fab1619c7f | -7.89373 | -47.82361 | 2025-10-07 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bc9349dc-4898-393b-9497-32dc36f0ea8d | -7.68958 | -46.21955 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 896b6dcc-d9ce-3eaa-8ebe-04e2b4c98628 | -8.48697 | -46.31884 | 2025-10-07 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 1547e517-5714-37d1-8b92-e728c10dc26e | -8.13608 | -50.26522 | 2025-10-07 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 99e2f70e-6487-31e2-9f37-5e738ecae7f1 | -12.95054 | -46.82445 | 2025-10-07 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| fc4bf9db-9d33-3585-8c9b-57bec7276da9 | -11.15572 | -47.75349 | 2025-10-07 12:38:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d0edbc46-bdd1-3117-a208-1738f987c714 | -13.32775 | -48.03644 | 2025-10-07 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| c902a3ef-3cc9-31a0-b895-36d9f6849026 | -12.90001 | -54.74547 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 218.4 |
| 1824d6cd-8837-3a78-ad23-e6930cafa84c | -10.99843 | -51.21729 | 2025-10-07 12:38:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 28801bce-c1bf-39a2-a70b-229023d9c4ca | -10.46046 | -48.36301 | 2025-10-07 12:38:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 596fd212-d3a3-3a3a-b981-b35aaf2eba1d | -11.71964 | -54.17676 | 2025-10-07 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 51ff8603-4386-3f7d-8774-c0574bdc3f79 | -14.75864 | -46.01547 | 2025-10-07 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 48f55b4b-2870-336f-9575-0fd0c4c768a1 | -10.41687 | -45.39097 | 2025-10-07 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 250.8 |
| 15b9c362-eaad-328d-b655-a09f4920097b | -14.86381 | -51.41932 | 2025-10-07 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| a0b88864-3d75-3278-abfa-2a5ffefdb326 | -12.9014 | -54.73606 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 7becbcc3-2f84-3189-884f-d7fc64a68103 | -12.25393 | -54.49878 | 2025-10-07 12:38:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d4862c0c-5011-33bc-aec7-48ec67d350fd | -11.02989 | -50.91869 | 2025-10-07 12:38:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 75b58853-7bc7-3f64-9a73-8b19cc1502b3 | -14.54384 | -46.63759 | 2025-10-07 12:38:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 4d9af7d2-bbb4-341a-be19-ba5f901e4a15 | -13.66737 | -48.72029 | 2025-10-07 12:38:00 | TERRA_M-T | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 31.9 |
| d33000b9-4ced-333c-a3ef-65b5ee79ca22 | -11.04337 | -50.88972 | 2025-10-07 12:38:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 8af69313-8851-3455-b3b1-6a16fad84b72 | -11.75126 | -51.496 | 2025-10-07 12:38:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1ec50a7f-0cba-3e15-9cc6-0cd907cc38c4 | -11.91465 | -55.90663 | 2025-10-07 12:38:00 | TERRA_M-T | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 6f174c4c-e2bd-3f93-8c91-c59cb7204a82 | -15.26654 | -48.06881 | 2025-10-07 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0d06a5c0-66d3-35d8-a4d2-3a8f530dd49a | -16.29094 | -50.97199 | 2025-10-07 12:38:00 | TERRA_M-T | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| aabba31b-1e58-383f-aabb-fbe915b72721 | -14.49986 | -46.93955 | 2025-10-07 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 20f5978c-1f18-3a7f-a1ea-a34f8ad6725d | -13.03968 | -47.89464 | 2025-10-07 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| c887f308-82de-304a-bab1-1d8ca35a0842 | -11.15485 | -54.8813 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 26ac0b51-cef2-34c2-aab2-d03eb1bdc8c1 | -15.60745 | -47.26039 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 4aa458d7-9c31-387e-8e22-e6c09de9635c | -15.36951 | -47.29738 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a8f546e9-f23a-3c4e-8910-3db830d9406a | -11.69226 | -46.33426 | 2025-10-07 12:38:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 75fb44b2-0724-3475-80eb-5bb73adeca76 | -13.33619 | -47.76228 | 2025-10-07 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 508b3a1a-3b50-3153-b96f-9ebccf90d6f3 | -15.99836 | -50.95079 | 2025-10-07 12:38:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e7bb36ec-1479-30de-aa99-c1f44f064644 | -11.78447 | -54.23951 | 2025-10-07 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| de325de2-6960-33b0-b4be-3d391187040e | -12.99139 | -51.09319 | 2025-10-07 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 36f5df41-a4c6-3fec-9ae3-899db8148beb | -14.29626 | -45.82785 | 2025-10-07 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| b4d4c708-0e72-310d-8879-b45bac50a8ef | -15.61758 | -52.57069 | 2025-10-07 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ed42faf6-5169-3808-8932-286f95d9b17b | -12.96179 | -46.83248 | 2025-10-07 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| a3825075-0a7e-3095-a9d6-cc54b316f139 | -15.61889 | -52.56114 | 2025-10-07 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 0263ebec-2f36-3c62-b800-538f4a54d27a | -12.48765 | -54.72563 | 2025-10-07 12:38:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e8fbe19c-9a65-3fb3-a4b2-a408293f9dc7 | -10.86152 | -47.17277 | 2025-10-07 12:38:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 94da6530-9089-3536-8289-27464e4bb567 | -14.49932 | -46.92331 | 2025-10-07 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 7dcc8c40-0c74-3108-afab-7b77136c57f8 | -12.39952 | -51.13667 | 2025-10-07 12:38:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 41beb6ff-392e-3549-9df3-4fed225c45ee | -15.16629 | -52.77271 | 2025-10-07 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 067ceb3e-6083-3be5-aec6-b37b30b2f033 | -12.96351 | -46.82595 | 2025-10-07 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 02374745-35f3-3e4b-8b3f-ec8a2b0cedd3 | -12.89861 | -54.7549 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| cb217a2e-f377-3397-b4bc-66ea7cc38506 | -11.03263 | -50.89854 | 2025-10-07 12:38:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9520bebd-41d1-3480-a790-dd28d6c06126 | -16.01756 | -51.03514 | 2025-10-07 12:38:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 33c892c8-a55f-378c-913e-5ade5c2e9911 | -14.87331 | -51.42062 | 2025-10-07 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| bc09a6a9-f00e-3fa7-a8a2-1a5f1961be2f | -13.03366 | -47.9013 | 2025-10-07 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| c79545f7-fec1-35bc-9043-78c3db63526a | -12.99448 | -46.78783 | 2025-10-07 12:38:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| b5537ee2-205a-37d6-b038-1f478bc3d218 | -11.71446 | -45.35489 | 2025-10-07 12:38:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 3ec3a5f5-7f5e-3bd4-8a74-f024028b5ece | -13.04558 | -47.90251 | 2025-10-07 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| ae975298-9e66-3157-b569-9b4724da5abd | -11.15629 | -54.87157 | 2025-10-07 12:38:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| c888984c-2bd3-3b4f-b70a-7b28661c75e6 | -15.58258 | -52.55582 | 2025-10-07 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 6cc28434-aa15-3453-a68e-314853a0474d | -13.30211 | -48.05028 | 2025-10-07 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b75c5407-d13d-3569-9525-f548a42f7778 | -16.24955 | -44.05577 | 2025-10-07 12:38:00 | TERRA_M-T | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 02fde74d-7aa5-3797-bf1a-342e5510b9ea | -15.38873 | -48.01688 | 2025-10-07 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 08c84bce-5053-383c-973c-6177ba99c8f0 | -11.04199 | -50.89981 | 2025-10-07 12:38:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 33ff0d75-a3af-3556-b21a-d2956d02818d | -15.20718 | -44.49862 | 2025-10-07 12:38:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 1419930f-0a8d-35a4-8967-21188ef9e1c0 | -11.04774 | -51.65975 | 2025-10-07 12:38:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9599d261-887a-3d3a-8180-4641cc19b7ae | -13.40386 | -47.60897 | 2025-10-07 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 729eaae3-4d90-332d-b132-b2f551c633a1 | -16.00351 | -50.83178 | 2025-10-07 12:38:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9d55ab2f-1003-36a8-a2de-480ac6183245 | -12.40418 | -50.26875 | 2025-10-07 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d1991e66-1fbe-3479-a1d8-e838fb40e5b2 | -11.656 | -46.41609 | 2025-10-07 12:38:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |


[Clique aqui para ver as próximas entradas](README115.md)
