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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4743257-c343-39ec-94e2-e6fca262295f | -16.88667 | -45.32349 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 179382b5-f05d-34ae-88dc-56e7484ad392 | -16.88611 | -45.32728 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23d143f4-17e8-30e4-9b4c-ddbd954c4afa | -16.88384 | -45.31915 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a755e4a0-c47b-349c-bd26-8aa6e7ed2ffe | -16.88328 | -45.32294 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cc2693f6-56e7-3e0e-a362-eda900de47f3 | -16.88272 | -45.32674 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc425cb8-e6b8-3c5d-8c36-b61cf6e4e870 | -16.87989 | -45.3224 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 671e900d-1079-301f-be71-c42ef65bf42c | -16.87933 | -45.32619 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 789eec9d-5df7-37b6-9eb0-6a6e2f2c8b7a | -16.8765 | -45.32186 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ce295b9-891c-3fa9-a50c-b53c7fb6dbee | -16.87593 | -45.32565 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d0ed7336-fa6d-3d9c-8e77-c6ae170c3721 | -16.83947 | -45.63953 | 2024-09-28 04:21:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 368d35cc-62b0-34dd-b3e6-7cc15a6519be | -16.79689 | -45.31319 | 2024-09-28 04:21:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 661041e9-4a3a-3d12-9a73-79d41f9e82c3 | -15.11123 | -47.16135 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0723bcb1-0e56-3ab7-bb52-8947bd8b4add | -10.69855 | -45.8639 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6af4bd13-7709-33ac-b38a-8c3992098c99 | -10.6958 | -45.85989 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 415e6043-7659-32af-9a6b-9873286d1b41 | -10.69525 | -45.86338 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0cfd3d76-9297-30c7-bdd0-1c800ceda8f0 | -10.69469 | -45.86687 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c3263849-b56c-3d57-a68c-10aadb6c27a7 | -10.6925 | -45.85936 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fd5f446-72e4-32bb-82c4-aca2cbb985b8 | -10.6892 | -45.85883 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3aa153d-b5ff-322a-a43f-2cf655b118db | -10.68645 | -45.8548 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e2d5a81-9832-3192-8524-ddf9b34e87ac | -10.6749 | -45.88512 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 738b6694-6afc-3cda-ab61-f08d4981b49e | -10.6694 | -45.87708 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8a89287-2ca7-3659-87f3-f64c98ed0b1d | -10.66885 | -45.88057 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6aa83b2-ed15-391c-9c03-0bbd3208fba0 | -10.6661 | -45.87655 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 616adb7f-093d-3971-8dc9-3fd0cfe347d3 | -10.66441 | -45.97291 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec99b7eb-0c0e-3dae-b9ed-3080e75b4326 | -10.6584 | -45.86103 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3c4c3e1-7213-350b-9806-82edaf575054 | -10.50342 | -45.13173 | 2024-09-28 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b16ee35-b0e8-34ae-bd91-b07f3ff57836 | -10.43216 | -45.8027 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 919c2759-7a9f-3ee1-b4c9-9ea23a1104a6 | -10.32638 | -45.17886 | 2024-09-28 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae50369d-46b9-3a28-8c68-60e5f2ab5d86 | -10.32362 | -45.17484 | 2024-09-28 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df95e68e-b342-3ab0-a991-169c6a40f577 | -10.32308 | -45.17834 | 2024-09-28 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57b595e8-1cf6-3824-81a3-ec9d0b9085be | -10.32253 | -45.18183 | 2024-09-28 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 339cc099-f38d-3416-be33-14bc03e24f85 | -10.31977 | -45.17781 | 2024-09-28 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21d28d90-30ca-34b1-a15d-f32a51514dff | -10.23916 | -45.38653 | 2024-09-28 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 537b1b30-45ee-3e2f-aa71-68c69eebb46a | -10.86437 | -44.80008 | 2024-09-28 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28967301-8b4d-3f5e-bb9f-d804a850af4f | -10.86104 | -44.79955 | 2024-09-28 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efee0348-87cd-3f36-bcfd-8b8390aad0af | -10.85827 | -44.79548 | 2024-09-28 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e53ff855-4a0e-34d1-9399-d18a9a77d17b | -10.85772 | -44.79902 | 2024-09-28 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e5556064-04c2-3f9b-a3df-d93f6c9349dd | -10.8544 | -44.7985 | 2024-09-28 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72646fd7-21c8-33ba-bf47-dae28a264408 | -9.58749 | -45.1821 | 2024-09-28 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e4f2d63-968f-31fc-bb79-26d0b18f6600 | -9.58694 | -45.18557 | 2024-09-28 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41b22c70-2f79-344a-8f7d-9beee9838b98 | -9.58364 | -45.18505 | 2024-09-28 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68b3b338-d0d5-346d-b900-0c2a6df16974 | -9.58093 | -45.65468 | 2024-09-28 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f77c475e-970a-3c07-a657-d784fd4acb7c | -11.13949 | -45.57099 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ec518d8-ecfa-36a3-b5b3-45ec802059d1 | -11.13895 | -45.57449 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43c14483-4d4a-3939-af88-8cbb6d111926 | -11.13831 | -45.5135 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ff608af-1244-39db-b06f-dc35562529ac | -11.12617 | -45.52183 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba4b8621-1f05-3dad-a18d-f98b235d4db7 | -11.11963 | -45.58524 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c9830b5-85c8-349f-ad6d-7760f626e4ba | -11.1163 | -45.54173 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f766541c-e101-324d-8fe2-679f855bc8db | -11.11578 | -45.5882 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 385e9388-ccce-37c1-9f5d-0b7ea66e2f5c | -11.11194 | -45.59116 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c278d5f5-17f5-348e-ad01-28d770f3a8ff | -11.10919 | -45.58714 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6f32b31-2773-3fef-a5e7-eae99c7c2a81 | -11.10864 | -45.59063 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 868ec4ae-4d05-3243-a018-cb181e91f163 | -11.10589 | -45.58662 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b23d1801-563c-3444-abe8-60fff119cf45 | -11.10534 | -45.59011 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cdce8501-626e-318c-a884-434ba5a55374 | -11.06369 | -46.09579 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49429b8f-ca0c-379f-9667-abb642ac28ab | -11.0499 | -45.70642 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7eef3c5-07d7-3e63-bcf5-1e456255d7b2 | -11.04716 | -45.72388 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e500687d-f0c5-3da4-ada9-f4c527f2ee4a | -11.04661 | -45.72738 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a052736d-56fe-3139-b909-6d6dcc79898e | -11.04606 | -45.73087 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b6e3fce3-4517-371c-9567-6dd87dabfa92 | -11.04605 | -45.70938 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaa28753-915c-356d-aaa8-7dc4fed0d926 | -11.04552 | -45.73436 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ddcb2dab-a6e6-30a0-9d4b-b242d048d53b | -11.0455 | -45.71288 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcd27aa7-8974-3a32-81ea-85bbaeb9fc40 | -11.04495 | -45.71637 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8993aba8-b548-3743-910f-d8f8bc5e0e20 | -11.04441 | -45.71986 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d5a82e0-83dd-3cca-a7bf-9e7b1afbef06 | -11.04221 | -45.73383 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4c286e3-628b-3c93-80c6-b095cb2b1df1 | -11.03285 | -45.70726 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 884a7788-dacc-3770-935f-cc8943e45875 | -11.02955 | -45.70673 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb8c1d7a-7bb6-3b96-a587-19a0d0a16ee4 | -11.029 | -45.71023 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f8762817-410b-3d45-90f9-317e0bde743d | -11.02845 | -45.71372 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2f938e0d-046b-3274-a235-b45263b265e6 | -11.0279 | -45.71721 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a896111-a446-3b9f-8647-3e59585a3301 | -11.02625 | -45.7062 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91fbd3d8-3877-35d5-ba3c-f0ab529c8288 | -11.0257 | -45.70969 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7ada58f4-4987-35f0-b29f-87858cbf795a | -11.02515 | -45.71319 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3b78a78c-da58-3bd9-beed-2f62d932808f | -11.0246 | -45.71668 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b683925d-b7d6-3625-b5a1-bb42604106a2 | -11.02294 | -45.70567 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b2f72ce-d428-3c43-b174-69d6d1e2e00f | -11.0224 | -45.70917 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 10b51872-1ed3-3a77-8d05-be8398cda86e | -11.01909 | -45.70864 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29096c13-4aec-35b8-9edb-75d5815931ca | -10.87474 | -45.52103 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7dc8e0d8-6f4e-3e80-b13d-a187cc6f2caf | -10.87144 | -45.5205 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4e7c4aeb-68bb-3c19-97e0-fff70436a55b | -10.87092 | -45.54541 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c4f3f0b-234a-35b1-81d0-d4ff8722d939 | -10.87038 | -45.5489 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5b6a332-e326-3ddc-93a6-ecb832de8b8d | -10.85882 | -45.53634 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68a61e02-800f-3dec-b092-bce1b3df2d14 | -10.85443 | -45.54279 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70d14c1d-e867-3c33-8cc9-c00e81a2daa3 | -10.85058 | -45.54575 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b691be21-1553-32a7-b3aa-4fd781c39c77 | -10.85004 | -45.54923 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c86812de-0a82-3ebf-8b8c-c5041f6f41a9 | -10.84895 | -45.5562 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae1b254d-cb6b-3e25-bda5-c6bebf06cd5e | -10.84674 | -45.54871 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| d051bf43-7612-32dc-a0df-8d0509f2f563 | -10.84619 | -45.55219 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 900e5cc3-8565-39db-ab87-baa2bc4fa24b | -10.8393 | -46.03033 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7340e67e-b2b4-3d16-ad24-a4fa00a6b601 | -10.83374 | -45.9757 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb4b8509-7899-3bd5-9b77-115d5b55ea69 | -10.83044 | -45.97517 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d62d1522-30a8-3c26-92f3-3cba7ec3c136 | -12.02036 | -44.95324 | 2024-09-28 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af5adb0d-12c1-3706-bbf1-e2a653850ae0 | -11.96416 | -44.96661 | 2024-09-28 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5d0fcc3-bc17-30d2-a582-da01ef7ffdda | -11.29368 | -46.14726 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 367faae5-f14b-3a50-923d-9897908b4125 | -11.29038 | -46.14674 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 776a04ba-3943-3e87-a111-f5e7e4191117 | -11.25091 | -45.39895 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f0cff41-1671-319c-ac5c-2387a44972a6 | -11.25037 | -45.40244 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23499a43-d6ac-3032-828f-692a53123264 | -11.21867 | -45.58369 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4c93eb2-5662-3f7b-93d9-40d8d033087d | -11.21428 | -45.59013 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c578b708-8f54-3fce-8eac-623b43fbc881 | -11.21044 | -45.59309 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README50.md)
