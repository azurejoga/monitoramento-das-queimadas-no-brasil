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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f08079c-d650-3644-b9b5-87cba71af7e3 | -3.59321 | -42.55514 | 2024-11-08 12:21:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| def57df1-ecf1-3b3d-bb2e-a3b2761afa49 | -9.62939 | -43.10181 | 2024-11-08 12:21:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0cc2b295-8e7d-337f-b4f6-3094a470b204 | -5.44563 | -43.26307 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| be7bf2e6-61e3-3b56-b051-10a9d0f3e982 | -7.48549 | -43.56722 | 2024-11-08 12:21:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 319f7a31-61a2-3506-8310-e5da2c9baf7e | -7.76026 | -39.85656 | 2024-11-08 12:21:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| c0ea6d94-8cb5-31c6-bc5f-0735d229d0e0 | -7.58916 | -41.78003 | 2024-11-08 12:21:00 | TERRA_M-T | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| c50b39de-1402-3b0e-910d-ec73b1c613eb | -5.48096 | -42.07612 | 2024-11-08 12:21:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 93c761df-eefb-308b-b7e0-e5586511a459 | -3.58632 | -42.85741 | 2024-11-08 12:21:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| a5976114-5c48-30d4-89cb-4971ab9549de | -7.63701 | -39.05097 | 2024-11-08 12:21:00 | TERRA_M-T | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| ef9584fa-11c1-37fe-ae2f-e0e68a3770f2 | -5.57367 | -43.14438 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 9cea5ab3-a509-3139-950c-03ac17c5358b | -8.28056 | -37.63226 | 2024-11-08 12:21:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 51.9 |
| 56ff2729-07b7-3c5e-97af-2af7e7afc6a1 | -3.52857 | -42.17827 | 2024-11-08 12:21:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| a6664bf7-b4db-30c8-b482-e9d84e938d6d | -7.75884 | -39.86679 | 2024-11-08 12:21:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 14.9 |
| a9d13f3c-8417-37f7-a070-0160dfcf0b11 | -3.71652 | -42.78342 | 2024-11-08 12:21:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a8559f22-8827-3934-bd2b-1e34e41b67b8 | -9.15243 | -43.14794 | 2024-11-08 12:21:00 | TERRA_M-T | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| fffdfe58-e7cf-3780-a335-66a94395519d | -7.58788 | -41.78892 | 2024-11-08 12:21:00 | TERRA_M-T | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 819d1c36-4835-3dee-aa56-d612707a8664 | -10.44713 | -40.46253 | 2024-11-08 12:21:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e9f8cc69-3f2f-3c1a-9305-6807eb25361a | -10.73094 | -40.26366 | 2024-11-08 12:21:00 | TERRA_M-T | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| c0cb5509-fc6f-3c95-a5e4-cf7151f385d8 | -9.15475 | -41.40719 | 2024-11-08 12:21:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 40d5ea91-f994-3dcb-9355-2fcb88794cd9 | -4.53213 | -44.06181 | 2024-11-08 12:21:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3079bc8b-e354-37ea-8497-0211e1a5c91e | -3.7694 | -43.243 | 2024-11-08 12:21:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7f27a7ce-6831-3bdb-a4d6-675b3abe214c | -9.94662 | -42.12067 | 2024-11-08 12:21:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 918156d7-fb8c-33d6-ad7e-997b173380e0 | -5.64127 | -44.24413 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| bee11bec-8770-3c61-8ebd-3d83711d11b8 | -3.59187 | -42.5643 | 2024-11-08 12:21:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| d6457e6a-cc92-3be2-a7a0-860aa33b11a9 | -6.26245 | -41.65073 | 2024-11-08 12:21:00 | TERRA_M-T | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 043866f7-46f5-3ec1-b857-8da07338931f | -3.47336 | -42.17373 | 2024-11-08 12:21:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 50.7 |
| 55f9360b-cd17-3cf1-8b38-0271135bc8f4 | -8.02127 | -43.43844 | 2024-11-08 12:21:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| f7a04c01-ab11-3c31-96ed-d52e8fdaae9d | -7.47501 | -43.57531 | 2024-11-08 12:21:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 7b695cd0-8c04-3aaf-99a2-5e6cea51e292 | -10.21097 | -39.34566 | 2024-11-08 12:21:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| a1a98452-c3b9-31c7-8a48-3e302c6618ba | -10.72948 | -40.27444 | 2024-11-08 12:21:00 | TERRA_M-T | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 13e79be8-0394-36b8-8cf7-30df0636739e | -3.68382 | -42.37843 | 2024-11-08 12:21:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2109f736-ed3c-3adb-a69a-a9486553f51c | -8.46638 | -42.91654 | 2024-11-08 12:21:00 | TERRA_M-T | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 51403047-9e58-3099-a5be-cf6887866c40 | -4.13937 | -44.41981 | 2024-11-08 12:21:00 | TERRA_M-T | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6ec60bda-81e7-3b96-963b-adf640100add | -4.10457 | -42.4628 | 2024-11-08 12:21:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 90de466e-50ff-3579-b852-add388851082 | -4.74119 | -44.09391 | 2024-11-08 12:21:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d30401c5-8390-3641-aa12-b6650a733fb5 | -3.53886 | -43.62321 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0d93bf0b-dad0-381f-9afd-8fef04aec027 | -3.59518 | -42.85515 | 2024-11-08 12:21:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 8c5510ba-d44d-31e6-bd4a-168047676f55 | -8.2917 | -37.63366 | 2024-11-08 12:21:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 18.8 |
| be645bd6-d912-38c6-8cca-c622341b0af6 | -8.65646 | -37.21602 | 2024-11-08 12:21:00 | TERRA_M-T | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 2d19d9ed-e252-3d21-bbaf-fb0c890f7a97 | -8.96528 | -41.05017 | 2024-11-08 12:21:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| dce050a6-216b-3342-b9fd-542e6a2b576d | -3.36309 | -41.47547 | 2024-11-08 12:21:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 7311d3fa-bed1-3577-8146-6d1e321db660 | -6.81476 | -41.72069 | 2024-11-08 12:21:00 | TERRA_M-T | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| a0d4830a-2b7d-399e-b0fd-c1dbeb13a146 | -4.14102 | -44.40872 | 2024-11-08 12:21:00 | TERRA_M-T | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f3ea3dd8-ca6a-3600-b5c1-7f991a09da72 | -4.73964 | -44.10437 | 2024-11-08 12:21:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6a9b0f3a-54e9-3b24-9e75-46761cdfcb34 | -5.43928 | -43.24282 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 18ab945e-c5c5-3189-80e7-743cfee9edea | -3.36216 | -42.1791 | 2024-11-08 12:21:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 10.4 |
| e45f9947-40da-3361-97a9-5c5134899a5b | -3.14455 | -44.49719 | 2024-11-08 12:21:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 31014e74-1f6a-385f-b5a1-13120d1951ad | -10.8033 | -43.84283 | 2024-11-08 12:21:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2421c6fc-1c60-3e73-ae09-bd9998967e97 | -8.28273 | -37.62424 | 2024-11-08 12:21:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 20.5 |
| c50872cd-a2a8-34bf-bae3-ca4706c5e580 | -10.50343 | -44.85529 | 2024-11-08 12:21:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 578138cb-49dc-3d5d-bb00-7917ca1ebed8 | -7.50364 | -43.56987 | 2024-11-08 12:21:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 23eb9c93-acb7-36d3-b3de-f787d9fea0b7 | -3.42049 | -42.2859 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ea68715c-31c0-3b75-a0c5-0ca7549eeae3 | -5.54738 | -41.68024 | 2024-11-08 12:21:00 | TERRA_M-T | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| db74bfa1-639c-3925-bc76-183fe0abd3ee | -5.46525 | -43.25621 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 5d00e9a2-01c8-3c75-b0ec-8d53b237f18c | -7.98901 | -40.2643 | 2024-11-08 12:21:00 | TERRA_M-T | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 615c8b4b-1225-3c47-8366-272caa24c9c9 | -9.75373 | -43.57599 | 2024-11-08 12:21:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c037bec3-2abf-368a-a078-f59e06e03926 | -7.85828 | -38.84701 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 0300f243-98cc-350e-bdc0-55f101133b56 | -5.20254 | -43.89836 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ca945046-b379-39f0-8940-993e185ed142 | -8.28087 | -37.63876 | 2024-11-08 12:21:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 31.7 |
| a198bbb4-80a9-316f-ab9c-06692d329c57 | -8.77087 | -40.39684 | 2024-11-08 12:21:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 00f85321-f4c6-3b67-b0af-7a175ec5148b | -7.48688 | -43.55782 | 2024-11-08 12:21:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c752131a-6b85-33aa-8250-1c43358a2bfe | -8.95621 | -41.04893 | 2024-11-08 12:21:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ef888590-adc6-3786-bc57-370e875f82cb | -2.64034 | -46.77443 | 2024-11-08 12:21:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a038f8e0-6fc0-3e67-8b1c-5440bb5d47f6 | -5.46388 | -43.26566 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 2683db4b-b505-3ac3-955c-0c3219c6476c | -9.74478 | -43.57468 | 2024-11-08 12:21:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 50b992ef-82f4-3c9a-a743-e64a12bdec5f | -3.60223 | -42.55639 | 2024-11-08 12:21:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 1b95888e-cd9b-38c0-95a5-506557b3aaf3 | -3.67352 | -42.38625 | 2024-11-08 12:21:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| df05c56d-300c-35df-ba83-9c5534a49f26 | -3.96897 | -48.16842 | 2024-11-08 12:21:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 52424662-3fb7-361b-a5cf-444ed7b21cdc | -8.75431 | -41.49712 | 2024-11-08 12:21:00 | TERRA_M-T | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| a5298e77-b986-3ab9-b4e5-07aa3722a623 | -5.41902 | -43.3173 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ec0799a1-d5a2-3d0a-a369-a8adcf4b99a1 | -7.49596 | -43.55914 | 2024-11-08 12:21:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 83a4a917-1a8b-39ac-8035-4ddd4345e646 | -5.22819 | -43.29671 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e0d7b956-b019-302d-aa7e-a288b76740f6 | -5.57502 | -43.13506 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 309bee45-d81b-31d4-a6ed-e40bc98d4098 | -7.72975 | -37.73296 | 2024-11-08 12:21:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 4c2e192c-2130-3251-a3ad-962df0a62b6e | -7.98822 | -38.63912 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 26.1 |
| dc0bbdb8-ce17-3bd1-af6f-7c84640e8ba0 | -9.56391 | -40.65218 | 2024-11-08 12:21:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9721cb28-0ea2-37da-abd0-aef6379dd536 | -5.36905 | -43.33917 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7911ddad-fbc1-3310-96c4-7cc5761228e7 | -3.67485 | -42.37717 | 2024-11-08 12:21:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| 2c4deabc-cb80-3904-83ff-3c1ac02b5580 | -5.47967 | -42.08497 | 2024-11-08 12:21:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 5e6b8862-7e4d-3e13-963c-1cc11ef008be | -3.53538 | -42.06945 | 2024-11-08 12:21:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 42f7a034-2f55-313f-ae7a-14deffe8db08 | -9.74075 | -43.60212 | 2024-11-08 12:21:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4c484bcf-025a-3860-941a-d2ab98306af7 | -4.43272 | -38.94098 | 2024-11-08 12:21:00 | TERRA_M-T | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| cbca11e9-c618-3d23-a75d-9e60fbca7f20 | -3.65934 | -42.60815 | 2024-11-08 12:21:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 97d83bbe-b867-38df-93c9-6cbac41edfab | -5.50748 | -44.03342 | 2024-11-08 12:21:00 | TERRA_M-T | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| ecee3dc8-7cc3-3cbf-8d4a-9ea2725717f7 | -3.54035 | -43.613 | 2024-11-08 12:21:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 791c0abc-a355-3b3f-9182-bdea3d3f19c2 | -5.44839 | -43.24414 | 2024-11-08 12:21:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 95368e64-917c-3d4e-885a-5d9e7eb6f865 | -11.13606 | -44.9438 | 2024-11-08 12:23:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 622a9225-e312-3cf9-a0b9-6b62a456e237 | -11.76756 | -44.61819 | 2024-11-08 12:23:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| eaea17ac-a00d-3a96-ac5c-8d2dc1425021 | -11.83597 | -37.94887 | 2024-11-08 12:23:00 | TERRA_M-T | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 67d16273-dbad-3306-94ba-9c7ca233219f | 0.0277 | -49.4311 | 2024-11-08 12:30:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 32a6f7e2-abb7-37e3-97ae-cd7ff0780f93 | -2.6388 | -46.7597 | 2024-11-08 12:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9b3dba73-2003-356a-ae4b-9b2721ddc13f | -1.5164 | -52.1696 | 2024-11-08 12:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 90ca37d8-62d1-3b2d-8093-b497b4f68155 | -2.6387 | -46.7817 | 2024-11-08 12:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 00c2dd0e-796a-3b45-9a70-b8e8fbb1958d | -3.0865 | -50.5625 | 2024-11-08 12:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| eed74630-9254-35c8-b8bf-575d650a2e29 | -3.9669 | -48.1716 | 2024-11-08 12:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 24cc5512-f48c-354e-9806-9a64a4668ae7 | -3.665 | -42.3911 | 2024-11-08 12:30:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 64537e63-2209-3fc2-8f97-49d7bfe9e3c1 | -2.8016 | -52.9414 | 2024-11-08 12:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| e16a5ecd-55fe-3092-8498-733dc5227c19 | -3.068 | -50.5631 | 2024-11-08 12:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 4f12fe6a-0d65-3ade-b918-e6676a7b5b49 | -2.6764 | -51.8189 | 2024-11-08 12:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 4de730bf-e8a9-35dd-91e5-93d5206d565a | -5.4359 | -43.2673 | 2024-11-08 12:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 186.1 |


[Clique aqui para ver as próximas entradas](README40.md)
