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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c02e0d26-6a83-33e9-bfea-11acc8a8f9c2 | -3.96939 | -46.4832 | 2025-11-24 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1abbb0d2-8ad0-3de8-92c9-890162b47cda | -5.0729 | -49.99637 | 2025-11-24 04:36:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89fd310c-7fc2-3f83-ad3e-3b87b0b090cd | -5.63267 | -49.13147 | 2025-11-24 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3f492dd-02d2-3894-8463-75bf641833e2 | -6.04664 | -45.83562 | 2025-11-24 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2adb981-e089-36fc-8be4-2e7afd3e616b | -1.72726 | -46.19063 | 2025-11-24 04:36:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eec5fe9a-e8bc-3830-9e63-634a1de8c65f | -3.02818 | -51.03534 | 2025-11-24 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b50c4c4-e788-3437-85a1-93c65f628525 | -3.71312 | -44.00815 | 2025-11-24 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f9da388-9ee4-3162-9bc4-0316f3e7e5cb | -3.81084 | -43.36041 | 2025-11-24 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2830f5f-2bb4-38dd-8889-8001c6b1033c | -2.19363 | -46.17078 | 2025-11-24 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ad7c24c-08de-33db-914f-f794748b3e48 | -3.91785 | -43.18997 | 2025-11-24 04:36:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57d7a745-8e97-3d17-9da7-bd1f9e943a19 | -3.3771 | -46.05309 | 2025-11-24 04:36:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4695de8f-87b0-37c0-8d57-073f729f75b7 | -4.52504 | -45.61569 | 2025-11-24 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9cdbd314-3c7e-3ef8-8b83-86bf7dec3f42 | -4.71116 | -46.45415 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9b526948-23c0-3a88-8006-764cd5a41014 | -2.70276 | -49.51504 | 2025-11-24 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24594269-4fd8-3e20-b6a6-c7f0b7b5dcf7 | -4.81899 | -43.83041 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5afd0d09-bee7-3447-a9f9-15883c59d34e | -4.21681 | -48.69843 | 2025-11-24 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7f82f65-9e7a-3eb7-b4a5-44d8a8bcfb11 | -2.98003 | -44.42771 | 2025-11-24 04:36:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2fc4dbf9-7015-3083-8b51-939a28834863 | -4.7095 | -46.46469 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0f0db2ca-eb9d-33d1-b2fd-6eab8b34bb7b | -4.71061 | -46.45766 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9478d19f-d6ee-3a17-903d-2faa2b8f1838 | -3.21568 | -45.92956 | 2025-11-24 04:36:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a926706-288b-3d71-8934-b38972a8e35f | -3.49159 | -46.01239 | 2025-11-24 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a3bc0ec-9eda-33f2-88c6-3257659c098e | -1.14539 | -54.14516 | 2025-11-24 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65d9ae37-2d45-3b8f-964b-b368d4b5821f | -4.16638 | -44.47147 | 2025-11-24 04:36:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8f5a899-808a-3986-a1a1-088d8c9330f0 | -5.63209 | -49.13507 | 2025-11-24 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 441d8304-75fd-3c57-8b73-7b6bbb1d9ec6 | -4.39551 | -40.67675 | 2025-11-24 04:36:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| df1d6398-a31d-3685-b273-5e687d42d11c | -4.40278 | -50.59961 | 2025-11-24 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad06efd9-7b1b-35c5-a4d8-8ef2c19b6be5 | -5.97054 | -43.06599 | 2025-11-24 04:36:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 203116e9-25ea-3903-a5ef-44dfb8cabfdf | -2.26202 | -47.85493 | 2025-11-24 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7137e04-350f-3825-b631-f13e83f5ebc7 | -2.46829 | -48.11428 | 2025-11-24 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72bfcd71-0371-309a-b426-0af82600f4b9 | -1.86722 | -54.06374 | 2025-11-24 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| beeceb43-0bb7-3c11-96fd-005674470bf4 | -2.92727 | -48.23339 | 2025-11-24 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81b58cba-9cb4-3d4a-8c3d-ef4221f604fa | -3.76487 | -47.47618 | 2025-11-24 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 049d5091-25cd-3ef5-bc1a-e9a88830fb43 | -4.8271 | -43.82714 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7bcbb9d4-2799-3be0-8674-79c67e889aab | -2.93286 | -52.33949 | 2025-11-24 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b3f5157-3ebb-3c3d-9e38-02bca571af13 | -2.88188 | -51.80244 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5264e181-556a-377d-a967-dba1690f7582 | -3.49495 | -46.01292 | 2025-11-24 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a367a84-3f86-31a3-876f-ad7e2d53685a | -4.51615 | -47.64745 | 2025-11-24 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 133b9dc1-1794-3585-b2ef-78912d5643e8 | -3.60492 | -55.4646 | 2025-11-24 04:36:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46d612a0-daaf-31a4-9821-155dab3e3f2f | -1.1459 | -54.14335 | 2025-11-24 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fe7e514-7d9d-38e1-9eaa-d9e9b2903e4f | -4.52446 | -45.61938 | 2025-11-24 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c03e0861-3da1-3908-ac2c-dba3585004bc | -2.87312 | -51.80626 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 89615d9f-66a0-3a92-9508-de37713bff03 | -3.26826 | -51.17117 | 2025-11-24 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c17dc982-46b3-3f00-8721-077c29300aad | -6.92132 | -45.08112 | 2025-11-24 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1568f3cc-03ea-3558-aa59-eab0ce35d096 | -2.95612 | -52.94178 | 2025-11-24 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99189a1d-020c-38ef-8af1-82529abe78ea | -2.12823 | -53.43607 | 2025-11-24 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8974c61-b2dd-3135-ad11-385ec462ea2f | -4.52103 | -45.61891 | 2025-11-24 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a6a0b4f-1b28-3710-8862-20065e8185dc | -1.75146 | -47.08508 | 2025-11-24 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b4eacb4-b323-372b-80a8-22c6f44fce2b | -4.41088 | -45.74106 | 2025-11-24 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c68c73fc-54a5-3cae-abee-49a831eb3089 | -2.87476 | -51.7961 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0535d719-f10e-3877-b736-ae4024b216bf | -3.39473 | -47.56617 | 2025-11-24 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba38d5f4-0462-3438-9b72-873eff5dbaac | -4.45898 | -45.77039 | 2025-11-24 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fc7e75a-4388-3e5b-bbd6-ab40dbceeec3 | -5.0764 | -49.99696 | 2025-11-24 04:36:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64b0fe10-4086-3741-87a3-33a76905516f | -5.73724 | -42.37839 | 2025-11-24 04:36:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69d12431-7a59-3318-9cb7-e956df4b5f5b | -4.20067 | -38.12282 | 2025-11-24 04:36:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2f806a83-957b-3754-8395-4c3edbc97c7b | -3.27345 | -46.04384 | 2025-11-24 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba89157c-e338-320f-9020-057286a7e79b | -2.88025 | -51.81262 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8ee402b7-a5b6-3218-9245-a24fd7f85be2 | -4.83082 | -43.82772 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79fe9c4d-dee6-34aa-a13a-cf541608dd31 | -2.03999 | -50.78915 | 2025-11-24 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9774bd6-47e7-38d1-957d-28db8756387c | -3.81069 | -43.35783 | 2025-11-24 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c820d67-fab9-3a25-8ead-45669b58f651 | -2.80162 | -45.36195 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85c1e483-d420-3198-88e9-800d463efe7b | -3.83828 | -50.74718 | 2025-11-24 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 719bfef4-14c6-377c-85d9-cc0438721759 | -5.31392 | -47.48342 | 2025-11-24 04:36:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af8aa546-1418-3126-8ae6-86cce6ba0db5 | -5.76743 | -46.59969 | 2025-11-24 04:36:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e23084c-813d-35d6-baa8-25cc82833f6b | -2.88504 | -51.80818 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf936303-9ca4-3207-89d4-853ff660e7ec | -6.85324 | -46.28622 | 2025-11-24 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eac4c692-8b0d-31ea-aaa4-ec487949cce3 | -4.26505 | -40.85858 | 2025-11-24 04:36:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a343ab50-b266-3180-8c02-095e9942b04a | -2.88819 | -51.81393 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3759292a-95fb-3930-b495-ed2471cc5b03 | -1.71535 | -46.47924 | 2025-11-24 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf996145-6f64-3d53-9302-147317c45220 | -3.71381 | -44.00207 | 2025-11-24 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77b48764-2551-3685-bc92-c63fb374257a | -3.39418 | -47.56962 | 2025-11-24 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a7560dd-cd99-312a-a0af-97aa55091885 | -4.0008 | -47.65468 | 2025-11-24 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30fae1f1-58b5-3fcb-98c7-fe567fea0d22 | -4.21624 | -48.702 | 2025-11-24 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21f80b72-c42f-3c3e-b651-f3680af3da67 | -2.79537 | -45.35726 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a45cb6c-c2cc-3049-841a-4b6244936ec6 | -4.71285 | -46.46522 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 650d93db-e7d9-375c-9ecd-4bc714c970bd | -3.21775 | -44.36088 | 2025-11-24 04:36:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 298f0c00-bdc5-3f00-a248-212d7a6aadae | -2.79878 | -45.35778 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62aa40dd-1157-3a2b-a19b-40ccd91bd896 | -3.59728 | -40.97897 | 2025-11-24 04:36:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bbcfe84f-b3ca-3b75-9170-14ea9df98a73 | -4.71005 | -46.46118 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 97eb2714-723c-3b63-8035-519364d10dde | -3.21849 | -45.93362 | 2025-11-24 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 266214b3-1c72-31fd-9b90-8c9a900367d5 | -4.53613 | -45.49986 | 2025-11-24 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fdbbd95-bf65-32f5-956e-1ed7e82741af | -2.1085 | -47.09851 | 2025-11-24 04:36:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f62f0e3-78c8-3a93-8009-26943331f4b0 | -3.21512 | -45.93311 | 2025-11-24 04:36:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 30dd9db9-0800-3dcf-b043-a2fe45584a35 | -3.37374 | -46.05256 | 2025-11-24 04:36:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f063d0a-3a2e-3ae0-9700-0504f7a57178 | -3.71254 | -44.01053 | 2025-11-24 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eaf69df-b67a-30a3-a779-4ae8d8c70219 | -3.71378 | -44.00393 | 2025-11-24 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3fdf3d6-e5cd-381c-9bfb-dc7b15ff3d89 | -2.7948 | -45.36092 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 855f76aa-b248-3abf-a4f0-adb6b7d687ba | -2.92447 | -48.22932 | 2025-11-24 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 37eb475a-b128-33fc-b140-4e1eb96dd392 | -1.86795 | -54.05919 | 2025-11-24 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46801e1d-81ff-3e81-95bb-56a0f6ed0f56 | -4.77753 | -42.72405 | 2025-11-24 04:36:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0f0aeae-9bbb-3342-bf79-9f50b052920c | -4.16687 | -43.9868 | 2025-11-24 04:36:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c24d956-60f1-3e2a-abad-5982315c33b4 | -3.82347 | -48.99302 | 2025-11-24 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03202c12-a848-32ab-a76e-06c675fadbd8 | -4.53958 | -45.50036 | 2025-11-24 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2cf22d0-32ec-3fac-9b1a-7d02b9385c62 | -4.54016 | -45.49664 | 2025-11-24 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5267ad2e-3eb0-3391-be77-cdb6d6bd3925 | -4.82271 | -43.83099 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e6f17c87-d73e-3b82-82b3-57b255b5f561 | -3.20327 | -45.76001 | 2025-11-24 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 908b2f85-2aee-3b79-b984-4a1192587c39 | -2.1354 | -46.41412 | 2025-11-24 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 257d8172-8cd7-3ded-85ea-e64581555397 | -3.2729 | -46.04737 | 2025-11-24 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76d06c88-12f7-30f4-9e1b-ab805e9510a8 | -3.76819 | -47.4767 | 2025-11-24 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12a26f93-a7cd-394c-a76b-f18aa5e2de15 | -5.93731 | -45.57719 | 2025-11-24 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd2ac151-1aca-321a-9edd-3cde3192d4f4 | -4.70726 | -46.45714 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README10.md)
