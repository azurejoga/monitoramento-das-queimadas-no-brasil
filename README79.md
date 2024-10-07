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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 116c99c6-8708-3412-990a-625982749425 | -4.26659 | -43.74733 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09cc1d3d-e2fd-3341-97c2-322d052e00af | -4.26329 | -43.73439 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 59940cb2-13bc-3efa-8376-b0c8c1b2d850 | -4.26285 | -43.73745 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 36f494c1-05f9-36eb-93ba-fcde9e0cafa0 | -4.26241 | -43.74046 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a0c2e2bd-f516-3d8a-8a15-1201ec47ab96 | -4.04444 | -43.24186 | 2024-10-07 04:51:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 698bddce-8f3d-3538-ad16-d3af4d7bbf05 | -4.04397 | -43.24507 | 2024-10-07 04:51:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3607e828-0987-3465-8579-a36a3879d349 | -4.0435 | -43.24826 | 2024-10-07 04:51:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d855868-430d-34c6-a8a9-db17c6720621 | -4.04303 | -43.25145 | 2024-10-07 04:51:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d591a38-9c30-3c5f-b4fd-c3237516764d | -4.01833 | -43.2379 | 2024-10-07 04:51:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17d006ea-5176-3777-a096-9489819f571b | -4.01786 | -43.24112 | 2024-10-07 04:51:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49bdca2c-bab8-33e2-9b90-8c1fdcc322b8 | -7.24082 | -44.93932 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 139bc7e4-91a1-368e-bc42-30c3076877ca | -8.15253 | -44.41156 | 2024-10-07 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c980b40-fa16-3c06-bf66-d36d2e91ae5a | -8.1474 | -44.41085 | 2024-10-07 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64c1136c-50df-34dd-b70b-9821e3dfc608 | -8.14699 | -44.41386 | 2024-10-07 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b60c229-5843-3a2c-b8b9-fb160cd18f88 | -8.14659 | -44.41687 | 2024-10-07 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85f23da1-8ca0-3236-a31b-fd60fe0926eb | -8.14618 | -44.41989 | 2024-10-07 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddf4ba5d-9a4b-3f53-8adf-6814be4f98e0 | -10.27182 | -45.48985 | 2024-10-07 04:51:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f5a11212-db71-36d2-8ff1-ff45b290c064 | -10.271 | -45.49606 | 2024-10-07 04:51:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2e5fc2e8-023b-3389-802b-943b3e50a69b | -10.27025 | -45.50177 | 2024-10-07 04:51:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c252dffb-a229-3971-9a85-4ed73037c5eb | -10.2678 | -45.48238 | 2024-10-07 04:51:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c47805ef-f59f-32f9-af71-bcbf1f123823 | -10.26703 | -45.48827 | 2024-10-07 04:51:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 205cceab-2da5-3e17-9534-bbe0d1e1c4a7 | -10.26617 | -45.49478 | 2024-10-07 04:51:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 284168ea-4033-3cd2-9f39-358c8a526739 | -4.2806 | -60.01636 | 2024-10-07 04:51:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aebad19-94b7-37a6-ad78-049ed75df6c2 | -3.74736 | -59.33144 | 2024-10-07 04:51:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e65a0960-b37d-3924-9d85-f4cdd1389321 | -3.74516 | -59.3325 | 2024-10-07 04:51:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d5814307-8ce0-31f8-b628-96e291571aa8 | -3.74266 | -59.33068 | 2024-10-07 04:51:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b3db7f30-0585-3e8d-a138-75706318051e | -3.74046 | -59.33173 | 2024-10-07 04:51:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39497071-213e-3a94-8154-fc156754966b | -9.32018 | -46.72075 | 2024-10-07 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b567a32-4c12-36d2-88e3-664cc5222d56 | -9.31957 | -46.72516 | 2024-10-07 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 105e03b2-10ff-3810-9eb2-010c42caa730 | -9.31633 | -46.71569 | 2024-10-07 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e05283d-4a34-3288-aa96-e872699c7fd9 | -9.31513 | -46.72451 | 2024-10-07 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f626a6f0-9386-341c-8169-d7ff05a57926 | -9.31128 | -46.71946 | 2024-10-07 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4785989d-68bb-3cd1-ab09-c6bc186279ef | -9.31068 | -46.72387 | 2024-10-07 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 75be44c9-5223-3735-ab5a-241a3a80063f | -9.30683 | -46.71885 | 2024-10-07 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96d3e83b-0f8b-3cd3-a7b8-7bb9596a8b3c | -9.30623 | -46.72326 | 2024-10-07 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d44e8011-69a2-3416-8e7e-81e11b75e503 | -2.95599 | -47.36132 | 2024-10-07 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51d6bfe4-50c6-39b3-a3e1-53508163b4f8 | -3.95474 | -46.45139 | 2024-10-07 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d2b9da99-4501-3979-ab31-5fdff52f1c5d | -3.94268 | -46.44625 | 2024-10-07 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21d2a738-7728-30cf-a54e-5375d26e8b4f | -3.9385 | -46.44562 | 2024-10-07 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 155f83a6-dab9-333d-bfec-4fb8a96a3969 | -3.93794 | -46.44945 | 2024-10-07 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bf14d147-d3f8-3a63-8d42-16d6741e4d54 | -3.93488 | -46.44112 | 2024-10-07 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ac8fadf-21c3-318b-b3c7-a14874683c4b | -3.93432 | -46.44498 | 2024-10-07 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ce81abf-b864-3f4d-92e8-07e5f21ad336 | -3.85294 | -46.46521 | 2024-10-07 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aabc510c-e76e-3b5f-b9b1-eaa29ebf8848 | -3.84876 | -46.46468 | 2024-10-07 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eefe97e-b3a1-3951-9efa-f16b3f1edabd | -3.8482 | -46.46846 | 2024-10-07 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31d7c58b-8a17-35fd-9313-7ed54b89905e | -4.83543 | -46.86451 | 2024-10-07 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73319c0c-62ec-3929-bf6b-1bd6bbacb54b | -4.83425 | -46.86338 | 2024-10-07 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cb370a2-94d5-3a50-9a7f-4cf27597c9a2 | -5.62191 | -47.40311 | 2024-10-07 04:51:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50b1d3fa-2536-3fb5-aa25-4dcb7bfc8f36 | -5.62066 | -47.40258 | 2024-10-07 04:51:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7141e04f-8ce2-350a-ae80-cfa77fa1fa22 | -6.35362 | -47.34962 | 2024-10-07 04:51:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dce90666-beb5-363f-ba72-b456ad485622 | -5.37601 | -47.71778 | 2024-10-07 04:51:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 707a966a-e08c-3440-a590-4b7ccb7b05e7 | -6.63338 | -46.73845 | 2024-10-07 04:51:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24d8ff68-4bbd-3cee-8bfb-06cc50353d8a | -6.61691 | -46.73171 | 2024-10-07 04:51:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e609923d-83a4-3e79-a50d-9815350ed88f | -9.74036 | -47.80349 | 2024-10-07 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c622a377-8ddc-3290-8378-ff30aa1de5d4 | -9.69191 | -47.84721 | 2024-10-07 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94ac0ca3-a7dd-34a0-a332-0ace8f6121bb | -9.66907 | -47.81399 | 2024-10-07 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac6346a5-a446-37de-a58f-f1c43cdb5506 | -9.66548 | -47.80948 | 2024-10-07 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79afa123-a61c-3172-83c7-dab6945cff84 | -9.66439 | -47.81707 | 2024-10-07 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a3ccc5b-3d68-3ceb-b05f-db2a39e5f4ec | -9.66384 | -47.8209 | 2024-10-07 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d25dc7f-13d8-3353-9551-8c5f094b1eed | -10.15177 | -48.07084 | 2024-10-07 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cac7af2f-8342-37cf-9ad9-622c50368d86 | -10.03931 | -48.42979 | 2024-10-07 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1393e97e-4b69-363e-a8fb-905babf060bd | -3.49805 | -48.91722 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26e796bb-be93-3ec1-b47f-e71fe7513a73 | -3.49761 | -48.89621 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de60428f-b6ef-391d-876d-cff1bf72b2d1 | -3.4951 | -48.91259 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ebdb945-0edf-33a2-ba9d-8c138bd95511 | -3.49447 | -48.91668 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c36b24d8-cb36-3091-b198-c5ec503e1b50 | -3.49402 | -48.89567 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc29353b-ba36-3508-ab55-1de0de80eed8 | -3.49384 | -48.92077 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 460f5af6-18a9-3dbf-af0f-d7913ceeead3 | -3.49089 | -48.91613 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a9a6583-4ed1-3ae0-8220-3a6a51e64fe5 | -3.49044 | -48.89512 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d7326c9-4191-3427-ac40-cb7468fd84be | -3.49027 | -48.92022 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2332740-e4f0-3759-91e9-5f4566588cd2 | -3.48981 | -48.89922 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99abe14a-a287-3e2c-8976-53f4529a290f | -3.48964 | -48.92429 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d448fac7-52e1-31ee-8255-340b26ca2856 | -3.48919 | -48.90332 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e897f851-d69c-35a7-bf5c-761cc68f1cc1 | -3.48731 | -48.91558 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ab04ded-3d5e-35f3-a983-5884fa9092db | -3.48669 | -48.91966 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7924ed47-300b-31ee-8c3b-67cc4e0a1c86 | -3.46476 | -47.66139 | 2024-10-07 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28585595-f817-32a8-8491-945c4c8b293a | -3.46403 | -47.6662 | 2024-10-07 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f3ed689-559f-3d11-85f4-5fade555d605 | -3.22563 | -48.9248 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61216449-8419-3d9d-a0e0-d5efddcacadc | -3.22499 | -48.92884 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a6153c5-7573-3702-b5d0-bd4ebe921c00 | -3.22434 | -48.92734 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0428e9b4-e342-3ebc-9212-cb94d11cce52 | -3.22206 | -48.92426 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9104cec7-a81a-37a8-bf5e-4f950eaa233f | -3.22143 | -48.92831 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2c8c3f9-d1a1-32ac-80ca-65eba91c460b | -3.22077 | -48.9268 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 369eb349-ce60-3cc7-937b-5cf98e1a75dc | -3.21866 | -48.96926 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7a39659-f5c1-37e9-ad7b-9c77dd73ae95 | -3.21762 | -48.97184 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfe11a75-ba68-3c1d-b6d8-fc89c6e88296 | -3.12612 | -48.62884 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1b00ec1-2fcb-3679-8463-5d164defc00e | -3.12573 | -48.60736 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 002260cd-1e1c-3fff-ada9-796df817366c | -3.12547 | -48.633 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20e837e8-4a7c-39ec-a3df-5a2e01168e29 | -3.12509 | -48.61153 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dae1169e-53fe-3606-b655-22075a08c471 | -3.12275 | -48.60263 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdefd90f-22ee-3fea-a6b7-2ec0d51d6e9d | -3.1225 | -48.62826 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 064aa0d1-43f1-3f13-9b90-bfb83810137e | -3.12211 | -48.60681 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7c75566-4d6b-3628-8710-ec879cc94f27 | -3.12186 | -48.63244 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d9bfd7b-7b68-3de7-9235-1ed9255bb56c | -3.12147 | -48.61099 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9fb6afc-a2e0-332e-b5bc-c3fa3af1c481 | -3.12122 | -48.6366 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b7a7922-58a6-35e4-8777-11b53dd02132 | -3.11889 | -48.6277 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38905605-33ee-34ed-b41c-22c2fefae13c | -3.11785 | -48.61043 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e95a4c3b-5053-3356-a4dc-cc6ffaf6a9a3 | -2.96814 | -48.99426 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 022ba07b-f6d8-3ab6-8fda-f460fcc049dc | -2.93725 | -47.84126 | 2024-10-07 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b69427f5-a711-3c97-8253-1848230a9a00 | -2.8125 | -48.69084 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README80.md)
