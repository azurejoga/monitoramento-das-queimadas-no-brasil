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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a56e3af9-5ac3-35a8-8c11-f54efb1aa9ce | -20.78557 | -47.75546 | 2024-10-05 04:17:00 | NPP-375D | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1830c69c-8675-3e1b-9ec4-6250ca418db3 | -20.66807 | -47.08663 | 2024-10-05 04:17:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| d837e9fd-be29-3280-9702-195b06ea4c60 | -20.66746 | -47.09035 | 2024-10-05 04:17:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a95364f8-5e9c-3210-92e2-99a3406bf819 | -20.66686 | -47.09407 | 2024-10-05 04:17:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9e346c40-8851-3ba2-9a39-90fee6407020 | -20.66473 | -47.08603 | 2024-10-05 04:17:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7df19f37-c83d-3335-b865-4e8c052243f0 | -20.66412 | -47.08975 | 2024-10-05 04:17:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1f0d28a-42b0-37fb-bd38-8d2ef08e400e | -20.66352 | -47.09348 | 2024-10-05 04:17:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef70e29a-28d5-393d-8aa1-57d3f8f0a928 | -20.66138 | -47.08543 | 2024-10-05 04:17:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad25dcce-e408-3c07-b771-c800be70cc74 | -20.66078 | -47.08915 | 2024-10-05 04:17:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6fbe586-e8f6-3cd0-82bb-8b6b624a9ba0 | -20.65804 | -47.08482 | 2024-10-05 04:17:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d97d9b85-dd04-38fb-b2c7-c33e530d30a4 | -20.3776 | -45.60436 | 2024-10-05 04:17:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9e813f4-eba0-3d03-877b-32fea74f5ee1 | -20.31093 | -45.58144 | 2024-10-05 04:17:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87e3d7d6-f49d-3a23-a1cd-dc0aff391e69 | -20.28255 | -46.87698 | 2024-10-05 04:17:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbeb4732-5276-367c-adbc-03fcb575240b | -20.28196 | -46.8807 | 2024-10-05 04:17:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f816c188-eca1-32ed-b265-4b2121e9885c | -20.27922 | -46.87636 | 2024-10-05 04:17:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 399d3c0f-3ac6-3b6b-8588-d624dc9722c6 | -20.23767 | -47.09055 | 2024-10-05 04:17:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 326e7162-d3b8-3857-bcaa-f8a907dff025 | -20.23371 | -47.09372 | 2024-10-05 04:17:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6fb6923d-cb11-3e8a-b0f9-91724506011c | -20.19428 | -47.46129 | 2024-10-05 04:17:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36584366-69b4-3750-9ead-ce4a07e621c5 | -20.09199 | -47.54908 | 2024-10-05 04:17:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99d6c094-113f-37bb-9b2c-d5d18dd2e8a1 | -20.08924 | -47.54465 | 2024-10-05 04:17:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f93193e-6c07-30ec-b9bf-9e087d931d03 | -20.0761 | -45.78908 | 2024-10-05 04:17:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87c607e7-6a1b-3349-8f05-b7509a166dad | -19.83763 | -46.7565 | 2024-10-05 04:17:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85dc3edd-1c96-3c7b-b2ec-e8edf0efb65c | -19.83755 | -45.88807 | 2024-10-05 04:17:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57bbd77f-9ecd-3573-9d7e-2776f80e9526 | -19.80593 | -46.44841 | 2024-10-05 04:17:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a91f2ce-a827-32b0-8633-31e03046f1a5 | -19.80261 | -46.44782 | 2024-10-05 04:17:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d72b340-8c8f-3f31-9979-6e05254e1155 | -19.75004 | -46.6693 | 2024-10-05 04:17:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1cfe69c-5cad-324b-8e3a-b6fe143739c8 | -19.61205 | -46.26359 | 2024-10-05 04:17:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 929a0464-db56-305f-8449-1d1d83cb96f0 | -19.61189 | -46.28617 | 2024-10-05 04:17:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a48d705-9dc5-3323-bffc-e6407fe977f0 | -19.60873 | -46.26301 | 2024-10-05 04:17:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 521d20b8-c7f9-31ee-b4ad-9dfcb7a77dab | -19.47144 | -46.85241 | 2024-10-05 04:17:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca68ecab-3ad9-3f1e-9c3f-42841fade39f | -19.29613 | -46.2096 | 2024-10-05 04:17:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45150e38-047a-371b-9220-cc336d09f921 | -19.29555 | -46.21326 | 2024-10-05 04:17:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29e2c42c-6576-3d54-ace9-57f6671d2e69 | -19.29497 | -46.21692 | 2024-10-05 04:17:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 48beab5b-14e7-39dd-b183-8b4c7cfcad55 | -19.29281 | -46.20901 | 2024-10-05 04:17:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3004509-9d7b-3786-9522-5bb8d09efc7d | -19.14879 | -46.62451 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cea17507-73b9-339d-bb5d-2d4d97d79de6 | -19.1482 | -46.6282 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75912199-2e65-31ef-8ef1-4c946053e728 | -19.14761 | -46.63189 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66440384-7a99-3242-b4a7-4b36002e3e7f | -19.14701 | -46.63559 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61d2d84d-d8a1-3b6a-8e86-1db231336563 | -19.14487 | -46.62757 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c983910-1ea8-3524-ade9-748d9f1ae7a5 | -19.14428 | -46.63126 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c420d2cc-d21b-3a32-9684-e69466b74bc3 | -19.14368 | -46.63497 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c07b4e61-ed03-3be7-be5e-a04ace87b1d3 | -19.14308 | -46.63866 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6aa170f5-bea5-3937-8e1d-d47e87ad2977 | -19.14034 | -46.63435 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7a260ca9-ea57-352f-9df9-32cecd6fb4f3 | -19.13975 | -46.63805 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 02b55826-6d59-381f-bc6a-a50fa0fb75c0 | -19.05897 | -46.4469 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a356065-a168-3689-b83c-8df29802df06 | -19.05563 | -46.44632 | 2024-10-05 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f1df07e-6d30-3dfe-9bf0-7c70f1ccb05a | -18.92319 | -46.93557 | 2024-10-05 04:17:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54869398-d98c-394d-b352-4ade442866be | -18.10332 | -45.60233 | 2024-10-05 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac76d02a-95db-36a0-a023-1ee8d2752261 | -18.10114 | -45.5945 | 2024-10-05 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5d002cb-fbff-3e07-bf27-844c73174854 | -18.10057 | -45.59813 | 2024-10-05 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 297929d4-2f50-3e9e-b80a-191b81e50227 | -18.09943 | -45.60539 | 2024-10-05 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e7fb4a6-676a-3b23-b748-b4f089b8196f | -18.09448 | -45.59336 | 2024-10-05 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 184915e0-f8ba-3d2f-87e9-d0462625a213 | -18.08888 | -45.60732 | 2024-10-05 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7258d0ad-60ac-39d0-8b4a-650acc78e269 | -17.62774 | -46.99715 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68d149d9-0d7d-371e-8278-a027e48787e7 | -17.62749 | -46.97769 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1c74f09-856a-3132-9614-280545a2611d | -17.62687 | -46.98143 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19d1353b-ac0a-3c31-aa6a-092cceec1fab | -17.62436 | -46.99656 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4fb5a7c4-8464-3079-b2f6-41032da0c282 | -17.62373 | -47.00034 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98ea68b0-29aa-38a2-92d8-1da5752b9b8c | -17.62351 | -46.98077 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76e99ca6-dd76-39d1-ab33-8c08ec6586c2 | -17.62269 | -46.98115 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cd31f70-aa9f-3575-a8a3-012ea4c0e12f | -17.62162 | -46.99213 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20c6f3e3-c248-3aed-a6e2-10c6548d2c18 | -17.62113 | -46.9694 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e98c5626-9a55-376a-822e-1ebc203fd641 | -17.62083 | -46.99255 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e719c636-1947-3c26-b594-b77d8d9191d5 | -17.61775 | -46.96881 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c25113dc-3369-359a-8c62-805b084805a0 | -17.6107 | -46.99073 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 395b4b1e-81d5-3399-a321-1c1d180b6db1 | -17.60794 | -46.98633 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 331d5c25-8f5d-31a6-ae5b-dbc26b42e642 | -17.60732 | -46.99014 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c7a5a6c-8225-3fc0-bfe9-6d2408aac561 | -17.58429 | -46.93972 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eff6a88c-be03-3bdd-8656-272808bc83f5 | -17.58093 | -46.93904 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 803499a2-4bc9-3a8e-b1d3-196f92393962 | -17.58031 | -46.94281 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1872d1c-2517-33a5-b683-22494b3073bd | -17.57756 | -46.9384 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b6c6311-723d-3d99-b259-e4ca9c6dc3e2 | -17.57694 | -46.94218 | 2024-10-05 04:17:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d2a80053-d41b-35f3-8e58-34e9f636ec79 | -17.41385 | -46.31791 | 2024-10-05 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88b2e2de-7f45-3721-8594-dd529cf7ca0e | -17.20991 | -46.38799 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86c1b264-85c9-3d32-97e1-50c512eda930 | -17.18646 | -46.59578 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 241a95b5-0304-33a6-9061-8d1a8a7c3197 | -17.12169 | -47.13844 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2de73451-a113-3a50-a34a-f3d7f1140b09 | -17.00006 | -45.8219 | 2024-10-05 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5df71adc-c8ca-36d9-aa40-db69718168bb | -16.94996 | -47.12012 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 348522c3-4584-3616-88f3-243aa04656a3 | -16.94983 | -47.12078 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 523816ed-369d-3296-b13c-336333e0f080 | -16.94932 | -47.12394 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 258c4a9f-fe75-3708-ac64-8998a5ae7c84 | -16.94642 | -47.12016 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 7aa9f9f4-615b-3e60-a3a1-668e77ad47e3 | -16.94302 | -47.11955 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 44d0dcae-30a5-3eca-9af1-43f82dff9983 | -16.9424 | -47.12337 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 212d9de3-26a1-3798-bc4a-e9ef1ad13719 | -16.93899 | -47.12275 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 287ee733-f523-3769-be02-b328c578307d | -16.93677 | -47.15762 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b437ae68-b717-3f41-93e7-c5e6b107ce4e | -16.93336 | -47.15697 | 2024-10-05 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64e30187-8573-34b1-846d-be19c1b4d69c | -19.87447 | -44.4063 | 2024-10-05 04:17:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24dca005-723b-34b4-aeea-fca3c0b39986 | -19.86709 | -44.40897 | 2024-10-05 04:17:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cd5c5a1-0614-3c95-b725-e87f436bb5f9 | -19.86418 | -44.40955 | 2024-10-05 04:17:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 89b50913-91d5-3e30-a6ba-3fc99711780d | -19.46608 | -44.13655 | 2024-10-05 04:17:00 | NPP-375D | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3b5a4d1-878c-37b0-be14-a154aef4d320 | -19.23787 | -43.36007 | 2024-10-05 04:17:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd1a014c-f116-39b7-8af3-dd84dc94d823 | -19.23316 | -43.36777 | 2024-10-05 04:17:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95273fbc-ebde-35c1-b07f-132081f41f73 | -18.95539 | -44.21973 | 2024-10-05 04:17:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ba38caf-17d6-32ed-ba65-dd45584497e4 | -18.59476 | -43.95142 | 2024-10-05 04:17:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e07642b-4a25-32db-8364-e0089c8de2ae | -18.57644 | -43.83659 | 2024-10-05 04:17:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa2dca51-0789-3184-921a-d758c8ff74c6 | -18.34317 | -44.00313 | 2024-10-05 04:17:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a3faf21-503a-3e81-b2cf-f3daa6318a4d | -18.34151 | -44.01439 | 2024-10-05 04:17:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f653e05-bbf1-31b9-ac7e-6763b439dc2a | -18.32617 | -44.02351 | 2024-10-05 04:17:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a43d26ac-14d6-3c00-9734-2729206fb2aa | -18.32337 | -44.04245 | 2024-10-05 04:17:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a60ca90b-400f-3088-850a-f5603bc0dc8f | -18.09588 | -43.9579 | 2024-10-05 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README79.md)
