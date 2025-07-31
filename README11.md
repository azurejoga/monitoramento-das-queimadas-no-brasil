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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e2c21f8-e4b8-3881-bdea-7982840340de | -9.57728 | -43.8924 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cd75945e-abce-383b-bbbc-57bfe90b68b7 | -9.57408 | -43.86905 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 27a21462-4aa4-305d-b84c-6ee25c5caa87 | -12.55482 | -44.72827 | 2025-07-31 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 077b4dad-9546-308d-9143-b14b37b76142 | -7.75165 | -45.04645 | 2025-07-31 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 306c6ad5-873e-3f5c-a0a7-b3d6992366eb | -9.63332 | -43.84849 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b9549bd-31c2-3645-b042-b564921871bc | -10.61663 | -47.45628 | 2025-07-31 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1bc6849-20dc-3e57-8ddc-78bb25291ca4 | -7.88436 | -45.55016 | 2025-07-31 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 482c39c3-35c2-353d-b757-79e4393cc9f9 | -9.57046 | -43.89132 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1c2dd86c-fc34-34c3-9d64-f7d3d48e5594 | -11.53312 | -44.24522 | 2025-07-31 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca7d67d1-a3e7-3da9-b11d-5fbee4a09f9b | -9.59192 | -43.84531 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 110471fe-8bf4-38bc-82fa-2254929d9794 | -12.80961 | -42.73254 | 2025-07-31 04:10:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 46b6d31e-03c8-3059-91c9-11988a0f4012 | -7.74364 | -51.09087 | 2025-07-31 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8686cb04-1aee-3abd-94fe-5c77fa0fb788 | -13.06641 | -47.3973 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46e2bcc9-31cf-3b33-ab15-195186edaa22 | -7.32003 | -44.6729 | 2025-07-31 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ed08705-b1f2-3bb2-8379-d8fd30bf91d6 | -8.60412 | -45.51834 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30b3fc6d-46cc-3ce1-8d34-c6b2cf89affc | -12.55544 | -44.72451 | 2025-07-31 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebdb76c6-b062-3619-83d5-34f00c05a43f | -8.60215 | -45.52071 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b002986a-911a-3303-bd11-dbee5a8d1395 | -6.37086 | -53.33417 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc900080-0ef0-3de0-a17d-c6e2346cd64d | -11.13165 | -48.64193 | 2025-07-31 04:10:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17f739b8-625a-30da-ae5c-9ab2b7d1a2ef | -10.22659 | -47.98485 | 2025-07-31 04:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bdbb3ec3-a751-3c73-8b0e-19c76843395d | -8.17139 | -45.01524 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84062c72-834e-31c1-95e1-8681902187ff | -7.74584 | -51.08763 | 2025-07-31 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93048f3f-0ff7-355c-8fd0-b628010dd10d | -9.22377 | -48.59795 | 2025-07-31 04:10:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa50a91e-0df8-372b-9347-ba4cc392f1d8 | -7.75061 | -51.09194 | 2025-07-31 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 021f3b12-98b2-3db7-b9a0-0b0d5a586e54 | -12.62974 | -48.09081 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcbf2d5d-20e4-3078-83f3-d20b1dfa006b | -12.73597 | -47.01099 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 169f9caa-8735-3efa-adf8-f05f5c6d7ee1 | -7.646 | -49.80084 | 2025-07-31 04:10:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e904ffb5-be30-305d-88d5-81f767f5b22f | -6.89898 | -52.86247 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd52f544-459b-3eab-907f-c0cd3291b2ea | -8.16778 | -45.01465 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f925cb7-05d9-3e04-bdf5-eb82450feb75 | -12.60811 | -48.09458 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4915b55-fae7-35a5-9a66-407ec2665fef | -9.63327 | -43.84793 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dcb3673e-1e43-3fe9-9094-34d318bbcb89 | -10.60552 | -43.30854 | 2025-07-31 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1b3caaff-0cec-3df6-b811-b560c4a2512d | -7.74528 | -51.09067 | 2025-07-31 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c460d49-ba72-3631-b3d1-5c066a7f9d33 | -7.59252 | -44.81088 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1db871b7-7636-327c-bae2-ff6c4ee2db95 | -8.17571 | -45.01163 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7a63c45-5339-31e7-88ac-cc59e59d2eeb | -13.51026 | -45.64844 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8987ea24-6044-3366-876f-585194fe0fbc | -9.58791 | -43.84846 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b1ebedf5-1c08-3ccf-adfd-ce634ab25cf7 | -7.60038 | -44.80808 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24f73d11-4788-38c5-a5ce-758b2638f305 | -10.60495 | -43.3121 | 2025-07-31 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c99666f-ebf5-31e9-9b43-ac578ab398d5 | -9.39065 | -45.49883 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d4a623a-9d81-3406-a048-3b661fbd430d | -7.87762 | -45.54453 | 2025-07-31 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78eee89e-02f9-3b90-8966-71a33557df34 | -6.39278 | -53.32215 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a44c62b-7d71-337b-a13d-36d14fd1a076 | -12.71158 | -47.79321 | 2025-07-31 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab6c523b-1ab0-33f9-aca3-ad07343097ca | -10.91667 | -41.83937 | 2025-07-31 04:10:00 | NPP-375D | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3f3a9c2c-0c8e-3886-a376-10714d795632 | -11.97247 | -46.67805 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ef471da-a8f0-36ed-b121-95c0e8e4b72c | -8.30487 | -47.34023 | 2025-07-31 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 162a3310-2b41-38c7-a950-5a5fb5169b6d | -7.31157 | -44.67955 | 2025-07-31 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76848d3a-041b-3b6b-9891-bf4251a22ee6 | -8.16486 | -45.00985 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c0919f4-d398-3014-b9b5-ec8eeaeaa0e5 | -8.92218 | -47.33876 | 2025-07-31 04:10:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 571883ce-dd81-3d5d-88da-f16253706f5f | -7.88136 | -45.54514 | 2025-07-31 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f967fbb-42f7-3152-a0a1-2a7292900d92 | -9.57848 | -43.88498 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f423b5c0-13d1-3d4f-a20d-acfb54ffbc23 | -12.73513 | -47.01589 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dc29174-8718-3121-80a6-ab6a75202b3e | -13.15603 | -47.33918 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc0e52b9-fc40-3a98-8534-6298fccfa3fb | -12.5514 | -44.72769 | 2025-07-31 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdc6de0c-697c-3157-831b-c528e8d8a85b | -12.43745 | -44.72008 | 2025-07-31 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fab3a64-ad8f-3245-9065-1508cef15b40 | -10.05607 | -46.5433 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac01e9c6-0866-3c65-b0f5-251d9a8f71fb | -7.61236 | -49.9356 | 2025-07-31 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50f536db-eefd-3d08-b282-005d9f55e1fd | -12.55886 | -44.72509 | 2025-07-31 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46cac8ce-88d0-34de-91d8-a0f4dfe11e8c | -8.59326 | -45.52828 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43394ef8-d0cf-38e0-b865-f82c5c856e2a | -10.70408 | -48.86607 | 2025-07-31 04:10:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56f57f2b-648d-3b02-a09b-4a68ebb2f0eb | -11.97239 | -46.68095 | 2025-07-31 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7edb87ff-46df-3581-93c4-2cdd3a6b412b | -6.37181 | -53.32909 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e6abe56-6825-310f-91fa-cd197c43e024 | -9.64068 | -43.84534 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d38d43a-34d7-312b-8689-9648f33f7d2b | -6.37911 | -53.32511 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75c91d26-0b3f-3cb9-a5d0-cfef7dc38a95 | -13.54481 | -44.14672 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b396e53-6dc9-3583-be32-a61e45fb1a12 | -13.51861 | -45.64177 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3768a360-3945-341c-afe5-5ec46978a8c1 | -8.59671 | -45.51723 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f132b77c-c867-39b0-b5cd-ee68dd9e993a | -10.64662 | -45.23116 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c6ffa98-6e82-3eca-a520-1f6b3899b3aa | -10.61477 | -45.24667 | 2025-07-31 04:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bd311e34-19c6-36f4-8722-c3864859e34b | -8.06176 | -43.10664 | 2025-07-31 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5786dfa8-9b93-34d3-88e9-1bd70878ca72 | -6.37568 | -53.33315 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1218ebb0-2f46-3f5b-bb39-2926d986a0ac | -13.51443 | -45.64511 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a6adab6-a69d-391e-8ff1-a1c7cc3e2760 | -8.73514 | -48.07068 | 2025-07-31 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1731c864-a685-34ca-991a-3cd0760fc1ed | -10.07904 | -53.86718 | 2025-07-31 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d8fab858-6521-3a88-9d56-15f577fa4dc7 | -9.56705 | -43.89077 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1472d2d2-c17b-37af-afcf-5c7051161f79 | -7.12567 | -44.90278 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 472fd49a-bf08-392f-8cce-9a604cac8b58 | -10.51974 | -42.5537 | 2025-07-31 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 98fa9780-f5ef-3439-ad8c-772a2efe19aa | -10.98615 | -43.11287 | 2025-07-31 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb38b8e5-daaf-383a-a023-02baf74e9aa4 | -7.33905 | -44.64651 | 2025-07-31 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a96258d9-8c0c-33f7-8146-9721e76f6425 | -8.62209 | -36.75172 | 2025-07-31 04:10:00 | NPP-375D | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 055aff97-c7ff-33e6-a078-436722f2177f | -11.92391 | -44.54691 | 2025-07-31 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cad8170-06f1-3cb2-b85c-2a2e6c0ed664 | -8.45204 | -45.14861 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84c364de-5745-335b-a291-7cc6983413c2 | -8.80659 | -45.6376 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6a910d0-84d5-33e3-85ec-13cdc21ad887 | -10.60886 | -43.3091 | 2025-07-31 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9233fc53-5172-3a7b-969b-df1824f437bd | -13.53981 | -40.69501 | 2025-07-31 04:10:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 87897dee-cc59-300d-ab0f-348acde5ba8e | -9.19285 | -43.1527 | 2025-07-31 04:10:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 238de23e-197d-3cff-883f-f108df9fbeb2 | -10.52417 | -42.54722 | 2025-07-31 04:10:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| e40fd4cf-d960-3867-a48c-55f1eb369bf6 | -13.36908 | -44.77537 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47706abd-d711-3e06-a5ca-37be4cb9a2a6 | -9.43312 | -43.20999 | 2025-07-31 04:10:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f0f6e15b-ab0d-36b4-8a49-e42dcbb50a68 | -8.16707 | -45.01888 | 2025-07-31 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3454dc14-1ca6-3add-8039-c3f339d8bf7d | -12.43403 | -44.71947 | 2025-07-31 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 878cc28e-2ffd-3713-a9fa-132e648242f2 | -9.59592 | -43.84218 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ded4c6c5-8dd9-31bc-b578-e9f780cf6f06 | -9.59132 | -43.84901 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 6129b568-4e05-3478-8146-e6912536f33e | -8.80213 | -45.64138 | 2025-07-31 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8cfa594-f847-3b1c-80e9-8d488cd45e7f | -9.63545 | -43.85592 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d0608509-a6bc-3996-a784-49d4357ec589 | -6.37817 | -53.33015 | 2025-07-31 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6988142-a308-3ffc-bd3e-e7d9caac9a07 | -9.57166 | -43.8839 | 2025-07-31 04:10:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e31375b-4c0a-355a-bb30-4b98a61ac83f | -13.52813 | -45.69284 | 2025-07-31 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 597cfc32-67d9-3c3b-9b7e-36f5dcc3be0b | -7.12201 | -44.90224 | 2025-07-31 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b1e5bf3-e5a0-3571-91cb-5109f09a33d6 | -12.73863 | -46.99561 | 2025-07-31 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README12.md)
