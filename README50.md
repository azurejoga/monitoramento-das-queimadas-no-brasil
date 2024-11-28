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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbd1606d-4815-37b6-9481-cf2d2d0229b9 | -2.40858 | -46.17254 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71757b62-efa8-34f8-baa1-7eb1db3e95a6 | -2.50929 | -45.18814 | 2024-11-28 04:23:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40c21a18-abd2-35b0-a87d-df0d948e0b1e | -6.49058 | -47.89022 | 2024-11-28 04:23:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4ba7979-22b2-37d2-9b45-a8e876296ebe | -1.14975 | -53.56347 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4852fceb-7428-36ba-aca7-83cd8c47dc0b | -1.71485 | -52.48584 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f9735ce3-2204-31c5-99d1-cd7ac4603095 | -1.71745 | -52.47776 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a6d8e96e-98be-33b4-8751-4db2a4d87219 | -5.98387 | -45.36333 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 241e4964-69b7-30f9-b351-e80f5b1dc1df | -6.71011 | -47.26395 | 2024-11-28 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6f6148e-cd9c-3391-a3a9-20796ec59909 | -2.74053 | -46.11423 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 400d6d20-e939-357f-ad9e-fe9422759b4c | -7.70499 | -42.9901 | 2024-11-28 04:23:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c65bb4dc-1395-379c-a7ab-0ef0ec4cec36 | -1.34674 | -51.98886 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55a30012-56e4-38e3-8fc0-7c7b8834bf3a | -2.54975 | -46.39902 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 502818ae-a4f1-307a-b7d8-f9080cfeaeb6 | -2.04371 | -46.65459 | 2024-11-28 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1cc07e2-44df-3d5c-a961-586f00264b64 | -0.95153 | -51.63585 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee9fd17c-f678-3f0e-bb87-a7f24f648089 | -2.71623 | -46.2245 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de7b930e-15a5-3ca5-a5ea-f85a9922097d | -2.26069 | -46.44034 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 350108d6-6962-389b-bac1-a7bf7da80d3d | -1.14928 | -53.56642 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c19d7779-349d-3a62-89f8-47bf3b50ec7a | -4.08954 | -54.77069 | 2024-11-28 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c20613e4-6067-324f-905e-9daa492756a1 | -1.53766 | -47.19491 | 2024-11-28 04:23:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36580713-5191-34d0-8253-59e9b8eafc37 | -6.1727 | -42.62157 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| b6b854f5-f29a-3614-a6a5-d8489326f90e | -6.5217 | -47.01763 | 2024-11-28 04:23:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6479f6ea-4179-3d73-8c00-efc6d8d76be1 | -6.31666 | -46.23181 | 2024-11-28 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4fa7ec3a-3150-3430-84ad-0ea1923b9131 | -2.62518 | -46.19952 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dc85947-0dab-3409-9345-8b5cee12cb2c | 0.94 | -50.74191 | 2024-11-28 04:23:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33441732-8ff3-3a15-90e3-4fe28a1bca81 | -1.64557 | -45.23577 | 2024-11-28 04:23:00 | NOAA-20 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12e50fd0-1d69-3b1d-bada-e7509f7f2c13 | -1.28248 | -51.73852 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d677f8ae-136a-3517-9e01-563cc763b19f | -6.64189 | -46.53785 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a4601a8-1bb9-3b3a-b2c5-44257b046893 | -1.6248 | -52.37134 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a13c220-a017-31c4-814e-5659aa6269ba | -1.72483 | -46.22376 | 2024-11-28 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc804fda-2c0e-33ad-a2bf-f0c9c2de0237 | -2.28651 | -47.11531 | 2024-11-28 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4f488ed-75b5-3821-920d-0e5b6a4621c5 | -9.18012 | -44.72197 | 2024-11-28 04:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61901e64-f7b8-3297-b38f-c36fabe59c52 | -5.7145 | -44.67094 | 2024-11-28 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cf6a400-f1d1-3e44-b031-06304ec5262a | -1.36606 | -52.12949 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22783eee-0aa2-34aa-9d01-10dba2f49e2d | -1.28364 | -51.74176 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b227e79-4787-3989-9959-ca9a5b1c752c | -1.70333 | -48.82657 | 2024-11-28 04:23:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afab2bc0-d4dc-351e-a36a-8d2f6ea6cb2d | -1.14084 | -48.33607 | 2024-11-28 04:23:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b51f6bb0-2c3e-356f-9d42-d42d13d9ea5f | -0.87754 | -51.72197 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41e20016-fd60-3713-b51d-eca9e29c9aaa | -6.26919 | -43.88659 | 2024-11-28 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b7b8054-e523-3f60-aa21-ae126e4bf922 | -6.47371 | -54.91525 | 2024-11-28 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9399803a-bacf-3b8e-8123-64d9cc97b8f3 | -1.68805 | -52.50213 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec00255c-82c6-34cb-82a7-d384731b8170 | -5.97723 | -45.36229 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ec4a3d42-2f9e-3567-be1f-1db650fb6b44 | 1.23247 | -51.03609 | 2024-11-28 04:23:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d2e8b63-295a-348c-a8b5-b1ac88cda73c | -0.93729 | -47.559 | 2024-11-28 04:23:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80ab5435-77d2-3c00-9bdb-eb4217c93b55 | -2.09871 | -46.56805 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d68f5e96-92ca-36f2-aef0-ac04182a2d49 | -1.1581 | -53.57705 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33a11982-4416-3c83-9e1b-47a2b6458700 | -1.66577 | -52.73196 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d7cf147d-1c8d-3bf5-87e9-f6df1abee4da | -2.53338 | -47.32799 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d74ba620-1616-31f3-8545-0d97b66fa8a0 | -2.71513 | -46.25294 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8006e294-4796-3f3d-939f-06a8cbdce617 | -7.69157 | -42.97925 | 2024-11-28 04:23:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e2832765-ab92-3ee1-a95f-c05eb0dde7f0 | -6.08625 | -41.94329 | 2024-11-28 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3126b826-6aba-343e-81cf-484b50c88112 | -2.71512 | -46.23148 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd252b84-828f-39a3-8979-3eb5a885677e | -1.19607 | -51.75721 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 993b60f2-226c-3f6c-ba33-50242863c268 | -6.58581 | -47.90873 | 2024-11-28 04:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb3d5d9c-a461-3e6b-b80c-90606e34d8bf | -1.12594 | -53.64566 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f39ebad9-10e4-3a6c-ac5a-622fc60a5a58 | -6.37345 | -45.695 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7aa5278-c1d7-3505-845e-0c6fe7089096 | -1.15875 | -54.07461 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d25697d-f9d0-3c1a-a617-39ef922b4bed | -6.54436 | -44.65388 | 2024-11-28 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c33ba3e-e31a-3edd-a848-45279938c80b | -2.38728 | -47.16469 | 2024-11-28 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c65e4d75-1aa4-3e77-9240-6c3588c2e82f | -6.38185 | -45.68596 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58f977f2-7c26-3749-b14f-aa24b3e24ce5 | -6.66218 | -39.23894 | 2024-11-28 04:23:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ab4b0a5f-c3a6-34c6-92f0-a12a1b50246d | -1.52033 | -46.11969 | 2024-11-28 04:23:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a35f439-b355-3037-b34b-59d2abca9ef8 | -6.58555 | -44.17688 | 2024-11-28 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3f1706f-fd99-3b98-be6d-e5649ce471ba | -1.64484 | -52.46924 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5dc90e08-63e8-35d8-9771-e199eefde95f | -1.64956 | -52.47001 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fa201bc8-a4cd-390f-8c38-7dffa362e58a | -1.65428 | -52.47079 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c1e46eb-ca4d-3d71-a86e-142b4aebb15e | -5.80972 | -47.05262 | 2024-11-28 04:23:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 412f8e1f-9834-32b7-af36-4a1ca70f2166 | -5.49255 | -47.65865 | 2024-11-28 04:23:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1dfa7bc-1613-3bdd-bdd3-df562a4d6a28 | -6.0877 | -48.03866 | 2024-11-28 04:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 596c479b-67bb-3fe0-9ce0-0372199a4cd2 | -5.12341 | -46.90063 | 2024-11-28 04:23:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 676c3b40-03eb-3cb9-aea9-c46b1f277327 | -6.17769 | -42.61349 | 2024-11-28 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5465a091-93f4-3c1c-9153-0b24a7ca3afb | -7.30721 | -42.098 | 2024-11-28 04:23:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c5495f8-4ec8-3ce2-8d33-70402c4ba690 | -6.16968 | -42.61666 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| f2299676-b2b0-3737-a056-f59e7b99ea9f | -5.65634 | -47.05323 | 2024-11-28 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f012a42-70df-353a-85c4-4e72cbc34fed | -0.26801 | -51.50806 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9bec391b-68d5-390a-84ce-776f4af61396 | -6.82864 | -44.39566 | 2024-11-28 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ec6eb97-cad5-3d1a-81b9-2798a052edaf | -1.66764 | -52.47812 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5c4821d-9e53-3194-afbe-dc9ad746e2be | -9.17323 | -44.7209 | 2024-11-28 04:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0c47586-d52d-334e-af9c-e2e2477f16f0 | -6.2736 | -45.46556 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87aeff61-dae8-3ff5-98d2-0c29fe76de49 | -5.98442 | -45.35985 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0930e742-25c0-38d1-aa0f-8b646bb3d459 | -2.71035 | -46.11304 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1f8c1a0-52f1-3e5a-8c0c-d6d4c6c9a339 | -1.15858 | -53.57409 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abc9baed-d4be-3766-b6ca-b2d34d966791 | -7.79775 | -50.00095 | 2024-11-28 04:23:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74571fb3-1e9a-37c0-9f36-4e351e567530 | -5.50707 | -46.25896 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a94a62e-6b5b-353a-94ee-217fc83feae2 | -2.70442 | -46.1941 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f360b4d0-5fdc-365a-bd16-41405a108f8d | -2.39069 | -47.16526 | 2024-11-28 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cdc87bb8-ae08-3779-93c8-fe5336fe6631 | -1.35609 | -54.63378 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24f8a38a-dfa8-3be3-a4df-4cabb7d32002 | -6.27286 | -46.24936 | 2024-11-28 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b914e4d-d710-3ac3-a153-aef1d5477d9c | -2.10263 | -46.56502 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8772302d-5e99-31b2-ab72-1667e16db26c | -1.57755 | -52.01295 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0dcf0ada-1d09-3ea4-9c0a-b2777002e1ba | -5.64908 | -51.4691 | 2024-11-28 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d1c2193-eb68-3b1b-920b-ed0e82d74ea3 | -2.89288 | -45.25582 | 2024-11-28 04:23:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e819bffb-24f3-37c7-82db-bbf224b4d309 | -5.64049 | -46.38308 | 2024-11-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68b2f127-3d93-3061-863d-cff7e7277757 | -1.18858 | -51.7747 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bacc9400-a45d-3e1b-adb1-fbe65ddf2140 | -2.70387 | -46.19758 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 148ce1b1-0893-3c85-affa-d0058b3e3fc7 | -1.53353 | -47.22113 | 2024-11-28 04:23:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc2f33ca-4030-3b8b-9181-e3476c5376f5 | -6.64063 | -47.91386 | 2024-11-28 04:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8b84f654-0bc3-38a7-acda-7b5e4144d794 | -2.10039 | -46.55737 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 156b09e7-b428-3789-b7a5-4afa5b92b8de | -2.65099 | -46.5779 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0fc8262-8f62-3661-857f-0977d1846efb | -10.03224 | -36.27293 | 2024-11-28 04:23:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| de5921ec-475e-3d15-aecf-8b13d315d644 | -1.08685 | -53.64853 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README51.md)
