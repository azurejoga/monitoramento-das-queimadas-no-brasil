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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa60f679-2c39-3fc6-a783-9a985a75c983 | -13.02234 | -51.23407 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 76ba3d9f-9a5a-31e5-ad69-ff3aeab450d3 | -13.02079 | -51.24516 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 31562d58-abac-3285-bd8c-896334ed088e | -13.01968 | -51.32368 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c73438e2-a984-3966-9ecf-9cc412c2ffda | -13.01924 | -51.25623 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 5cf9f6e7-d39b-3487-be30-0ce6e7f435b9 | -13.01878 | -51.18819 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.3 |
| c1c7f940-15ef-3e24-bb36-e2ba065a9683 | -13.01769 | -51.26728 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 196.0 |
| ed88d452-465e-3e6e-a938-cc01580c824f | -13.01722 | -51.19934 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 1d786d93-a04e-3ae7-af35-480c0742923e | -13.01614 | -51.27832 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 1bf1a3c1-fb86-372c-895d-653d0a52863f | -13.01567 | -51.21048 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 5d11e165-e2d0-3bf8-afaa-4dd2fc03842d | -13.01459 | -51.28934 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d6af70a8-0475-3005-89a1-edbd8638e00c | -13.01412 | -51.2216 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6f3df3c5-b244-34e3-b4d4-3f41d9facfd9 | -13.01305 | -51.30035 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 341a9392-3926-3426-845e-415c181d3b7a | -13.01257 | -51.2327 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9b047f02-546f-34b3-92e9-e4ed463bf378 | -13.01103 | -51.24379 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1f089ab3-f211-3395-96f7-d4e046d80cd1 | -13.00997 | -51.32232 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6745b8fe-dbe7-30d7-99e1-bebad30fb1bf | -13.00794 | -51.26591 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| ac2271e7-f053-3518-988a-ec4dabb257e0 | -13.0064 | -51.27695 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 159.2 |
| f2297ad0-0595-3d1b-a8c6-38abc26ac64b | -13.00589 | -51.20911 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 4fc6ce43-a336-3995-aba5-a37e2e0f6ce7 | -13.00486 | -51.28798 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 275.5 |
| 0f84a9b6-4d77-3a41-9db7-5ccad42a39a2 | -13.00434 | -51.22023 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 61207177-81f3-3990-9d80-3397ce4e5387 | -13.00332 | -51.29898 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b1a72992-6221-36ab-8492-ce2dd460d3cc | -13.00179 | -51.30997 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 0e8833e5-16b4-3062-a70b-f00863b1222e | -12.99973 | -51.25349 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bbb799f4-4cf2-309a-872f-9e516153b36e | -12.99566 | -51.35378 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c31f51ac-279c-344c-bdd6-50a033084ce3 | -12.99512 | -51.28661 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6a310156-fd1a-3e8b-9720-d1f05ab01ca9 | -12.99457 | -51.21886 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 26faf36c-245b-3401-93bd-5a2e789b3f8e | -12.99359 | -51.29762 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 2c69d23b-48e1-3ac0-bc2a-947acd8fb02f | -12.99303 | -51.22997 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| fc228ff1-fa92-37b5-ab5f-683f4f07808f | -12.99206 | -51.30861 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 89d69c8a-5065-379f-b93e-a955e273d65d | -12.98844 | -51.26317 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 45174b44-4d0c-32ba-bdc8-fdb39807efeb | -12.98234 | -51.30724 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 0adfb7ce-9f33-36c7-b7f0-e27857d3ad8b | -12.98082 | -51.31821 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 6fb200bf-44e2-3ed4-ac9b-a060d6bb63eb | -12.9793 | -51.32917 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 919b8238-81fe-3255-8233-e4f4d6ebb103 | -12.97654 | -51.20499 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6233c841-e17e-3c9b-90cb-3739a3528751 | -12.97502 | -51.21613 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 6f1149bb-9b89-3105-a6ae-27ff28b02437 | -12.9735 | -51.22722 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 24cb0cd7-ad16-3b69-8794-c4af7d0198ba | -12.96959 | -51.3278 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8421dae9-a6d4-3c14-9da1-4d3072c329d3 | -12.96721 | -51.41629 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 3740d41b-92ae-31ee-a512-7712cca25cf6 | -12.96676 | -51.20362 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 00cf30b8-c7b0-3c0c-937c-780df14e6769 | -12.96571 | -51.4271 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| abfbe7e3-6824-3250-86a2-f3dca4e3ff47 | -12.96524 | -51.21474 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| aaf7edb8-09f1-3f91-83ef-4d4e32613149 | -12.96373 | -51.22584 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 496bf42f-4fb2-3b4b-87c6-efbd32f6cd55 | -12.96222 | -51.23693 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b458b564-e460-3204-bbbc-e96624776c3b | -12.95905 | -51.4041 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 04b9e2b0-59f6-39d6-9f86-be9b55f12316 | -12.95755 | -51.41492 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| d58cc520-d705-336f-93d9-879e8f9db478 | -12.95698 | -51.20223 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a3a744d8-34b1-3be9-92e9-add3f6c8aa8b | -12.95606 | -51.42574 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 93120d7e-bb53-3687-a5ae-cea004427f6a | -12.95547 | -51.21336 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dd089cf6-298d-3464-8983-ac12421528d8 | -12.9479 | -51.41356 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ec65840a-c289-3cdf-bc56-a039d1b4b35a | -12.93527 | -51.43382 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 07cec241-0cc7-3b3b-b46c-985e8178f761 | -12.92568 | -51.19229 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6d8f9d6b-d23b-310f-bc7c-5cddb05156cc | -12.9159 | -51.19091 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| cdea5c2e-12eb-30ae-8060-b7cc73fe8880 | -12.91436 | -51.20202 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 907ab861-676d-37ff-96a7-c1082a80d056 | -12.90458 | -51.20065 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 90a28750-f89e-3fdc-8503-6a47f9d48100 | -12.71352 | -51.91281 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 13add8e4-e598-30fe-ac6a-8a1a071faa8a | -13.03994 | -51.17976 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9e9394b6-50bd-3f21-8b85-c79246fbc0e6 | -13.03014 | -51.17839 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 49463726-167d-33e7-a967-3a6ea9b4c949 | -12.91744 | -51.17978 | 2024-10-01 05:46:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7cc73aad-bcd7-3e56-a78d-71cf96c9218e | -13.79808 | -52.43701 | 2024-10-01 05:46:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d47fabb5-4150-35e6-b693-ba1e24ca75ca | -12.90674 | -53.87926 | 2024-10-01 05:46:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 59a2e5f8-9bcf-3403-9268-855e050d5218 | -12.86885 | -54.01195 | 2024-10-01 05:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32b86e6d-6508-3ac5-b752-70e5965aff0e | -12.76246 | -53.98898 | 2024-10-01 05:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cba1acb6-43de-3533-b1f0-a208e2421e9c | -12.76112 | -53.99799 | 2024-10-01 05:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1cd049de-c991-307e-bb89-c9220c16551f | -12.71704 | -54.1111 | 2024-10-01 05:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed1890ca-1de1-3db2-9d7c-47d6fcc8591f | -12.68349 | -54.0173 | 2024-10-01 05:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dd55099e-c6c9-3dfc-a427-e0a9acf04440 | -12.6679 | -54.061 | 2024-10-01 05:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13507d54-aa5d-38ac-95c1-d987385c7d6a | -16.45095 | -53.92784 | 2024-10-01 05:46:00 | AQUA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f397f838-7ea6-3bdd-98a1-2a422f2cddbd | -16.08215 | -53.54118 | 2024-10-01 05:46:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67c28ce9-82d7-3eb7-99c3-3be5e7fa2330 | -15.68627 | -53.91833 | 2024-10-01 05:46:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c06537b8-62d4-32f6-b01a-c6ca08fd0577 | -15.24721 | -53.77256 | 2024-10-01 05:46:00 | AQUA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 588a2b02-6cf1-36e3-aee6-18f364a0f5fb | -16.14528 | -55.42239 | 2024-10-01 05:46:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 19b6e62a-a578-3efe-a040-e5fc00db670f | -16.13635 | -55.42111 | 2024-10-01 05:46:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a09a66b7-5603-3781-8d45-cf4d8d93f166 | -15.89789 | -57.18147 | 2024-10-01 05:46:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5a6214c8-3e78-3516-8971-31e592c60e27 | -15.61969 | -57.45415 | 2024-10-01 05:46:00 | AQUA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 81dd16b4-fbb3-3226-9389-009d18e56ebb | -14.88247 | -58.00045 | 2024-10-01 05:46:00 | AQUA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dbc977c6-7a54-3830-9a1e-b6fd89f418bc | -14.88053 | -58.01208 | 2024-10-01 05:46:00 | AQUA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ee198804-a414-329d-9a6c-fb2f936865a0 | -17.69576 | -53.20475 | 2024-10-01 05:48:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ad17f90a-0a88-3286-8773-1949fe1e6c18 | -21.85311 | -48.21181 | 2024-10-01 05:48:00 | AQUA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 97166428-6f6f-3534-b6db-179ce87d767d | -21.59237 | -47.8175 | 2024-10-01 05:48:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5842c1ed-516b-3267-af3b-5d66aeae254c | -21.5898 | -47.84392 | 2024-10-01 05:48:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 8a42ef19-7c2e-36be-b94a-fde3e8a169d5 | -21.5891 | -47.8122 | 2024-10-01 05:48:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 64.7 |
| cf71f013-884b-3c7d-b314-d94d5fc85319 | -21.58719 | -47.87073 | 2024-10-01 05:48:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 36.7 |
| f0d350ff-d8cd-37fa-88dc-1bff7b40ce8c | -21.58635 | -47.83866 | 2024-10-01 05:48:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 07cfc208-60bd-39ac-b4ab-8880a70a3ca3 | -21.58358 | -47.86525 | 2024-10-01 05:48:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e00534a2-c446-3b6d-8925-fe4032c11f1e | -21.58061 | -47.78851 | 2024-10-01 05:48:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 37.2 |
| c1cdf9bc-39e7-3067-a01c-8bfc179efc25 | -21.57793 | -47.81646 | 2024-10-01 05:48:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 13d9e8f5-be5d-3ef1-b79c-cbdb9b72bb82 | -18.03704 | -48.58232 | 2024-10-01 05:48:00 | AQUA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 283597e3-745a-39c7-89df-1127f5f08922 | -18.03675 | -48.58745 | 2024-10-01 05:48:00 | AQUA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| 968e6edc-5421-3ca0-b7dd-cac343f79619 | -18.03465 | -48.60261 | 2024-10-01 05:48:00 | AQUA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| f1939680-a907-3726-811d-1d37c9feec1f | -22.37726 | -49.2911 | 2024-10-01 05:48:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.4 |
| ecc8cd67-f450-3679-bb32-a200608c0611 | -22.37493 | -49.31308 | 2024-10-01 05:48:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| 3e441035-561e-3059-b198-49cbc1ffe289 | -22.37262 | -49.33487 | 2024-10-01 05:48:00 | AQUA_M-M | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| 94be2104-e120-3a47-887a-8ca00ffe2c4c | -22.36427 | -49.28936 | 2024-10-01 05:48:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| b6533cf9-3ccf-3d8e-86ea-eb765812c224 | -22.36195 | -49.31149 | 2024-10-01 05:48:00 | AQUA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 148.9 |
| 212cb1e5-eb61-335f-ad26-44ec1c068bb5 | -22.35964 | -49.33351 | 2024-10-01 05:48:00 | AQUA_M-M | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 168.5 |
| 56fbd7bf-0782-33c1-be13-fe20216bb038 | -19.15827 | -57.48005 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| dca60c8a-7239-3b3a-b503-7f6fa317d599 | -19.1321 | -57.46531 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.2 |
| bf882207-e3d5-39f0-940f-e0b58d3a9f3c | -19.13048 | -57.47536 | 2024-10-01 05:48:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 008e1f43-266d-3db3-b244-fd2f27bf0015 | -20.80197 | -53.13161 | 2024-10-01 05:48:00 | AQUA_M-M | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 432b6e0a-dbbb-3dc6-999d-5e2b4a52b7ef | -18.87422 | -54.49866 | 2024-10-01 05:48:00 | AQUA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README153.md)
