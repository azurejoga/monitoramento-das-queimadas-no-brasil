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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d21bfe06-93a5-3914-a4e2-5c2af99d2456 | -5.91168 | -43.48326 | 2024-12-28 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc3450a5-2078-30c8-9b13-c01dd6215f28 | -3.94644 | -49.44731 | 2024-12-28 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 056a4b95-0ba5-3eff-8072-bb4d3a54643c | -4.0423 | -47.0469 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9815822f-d37f-37ea-b47f-40a669ab2689 | -3.73908 | -47.19053 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83354c38-e7f1-3ce6-a3c6-6348c8cd5b6d | -4.06068 | -46.99138 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d427d49b-d52e-38b7-8ac2-3ca4ad2b75be | -3.03865 | -53.91034 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe5a9679-4efe-3dca-adbe-8ff0134af4ef | -3.02414 | -53.89368 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2159b51-cfa8-345a-9f13-a2470870979f | -4.04272 | -47.04408 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85d38726-1000-36a2-a491-79316c84ff0c | -3.89711 | -46.99091 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 62706e7a-67c8-3e32-847c-24a7fbb69982 | -4.03607 | -47.05459 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8115e2a6-1f91-34f9-b55d-a9aa4120f812 | -4.08071 | -47.09774 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 50907975-e749-3a76-b25e-9ab32cb6f262 | -2.16859 | -54.43311 | 2024-12-28 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3d6ecdeb-8b66-3253-a6d3-824e516b4194 | -3.7243 | -47.1883 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e08958cc-fa1c-32bc-91cb-f3dbd049cfb9 | -10.60086 | -44.98914 | 2024-12-28 05:01:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2c045f9-a63c-3e7f-abe7-c310c21cdd76 | -3.75869 | -47.22729 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d42c96c3-5816-3419-8d47-1cb86c6dc168 | -5.31578 | -46.06913 | 2024-12-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdfe853d-244c-3426-9bbe-07e6d00a0932 | -3.72922 | -47.18906 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec45bcd0-127b-3d47-9cc3-d0e9095a11ef | -2.21991 | -53.65375 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 38cfab7c-b1c8-3371-98e7-9095f2d69418 | -3.57425 | -50.67769 | 2024-12-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27d4756e-c51f-3f25-b831-6565aa10c638 | -2.39586 | -51.79509 | 2024-12-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa64ba25-760c-37bd-a0f6-6b8ef979b7cc | -3.73568 | -47.3459 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75179d5c-4043-31a8-a704-09ee92ad689e | -3.94636 | -46.76796 | 2024-12-28 05:01:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa58192f-e6a3-31f3-868b-5ae4ed50b3a8 | -3.58825 | -53.71515 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cf4aa9e-a620-3da7-9925-32373442a0e4 | -3.57368 | -50.67544 | 2024-12-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dd4666a-f4e4-3922-af61-595cf7afa07d | -4.08142 | -46.8145 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 051743d3-5e12-3664-b375-f335f6dd13d0 | -3.7636 | -47.22808 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92a3bce5-7a7c-3fdf-aff1-1940118a97fb | -3.72513 | -47.18273 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34522ec6-6630-3c7b-8eeb-4193e1359cb0 | -3.53405 | -53.79797 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40efe301-e105-369d-a8dc-d925a79c2b17 | -2.48158 | -54.17059 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 907df257-5313-37e6-ba93-626a0387ebd3 | -3.14911 | -53.89831 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90db8793-7707-311f-a155-b50c9c078c55 | -2.48858 | -54.16846 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1f658c7-b206-3653-b573-fceeeff9bac1 | -4.12681 | -46.68329 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8f0e630-ff21-311e-a33b-f2c34d4917aa | -10.60147 | -44.98409 | 2024-12-28 05:01:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a97967e-0778-3128-9204-2171f9b0e691 | -4.00099 | -46.94562 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fab11e31-5b52-39e3-aa7d-1681340303d8 | -4.06025 | -46.99428 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 255571e6-c1b4-3ec2-a687-02cf40fd7996 | -2.21768 | -53.64617 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f2e7a61f-f1a1-3c43-8e91-c9f61175ba7b | -3.7284 | -47.19458 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85354c89-fbdd-3561-84be-c8b271f702dc | -3.8984 | -46.98236 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6dafbe9d-89d8-3c12-b6d6-2b1ae453039a | -3.0208 | -53.89317 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f095ccdf-60ea-3b36-9ede-c875eaaeeb9d | -1.95287 | -54.09918 | 2024-12-28 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ee7ba582-5f09-3674-b6b6-a05a26b0fc0f | -2.84173 | -48.10722 | 2024-12-28 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 364eb2cf-f547-3598-a36d-ccb0e9bf40a9 | -3.95068 | -49.44794 | 2024-12-28 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88a31b17-2ec8-32f6-a9e0-1e1142d77744 | -4.13155 | -46.68667 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fb28084-1f7c-344f-9d8d-7abdab06f487 | -4.56142 | -45.98804 | 2024-12-28 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 43b941d8-d86d-3319-8355-34e86cde7b1a | -3.94214 | -46.76142 | 2024-12-28 05:01:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4752dfc-999e-313f-87b6-65169d53b307 | -3.5335 | -53.80152 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca13209f-d940-3c67-b866-c08433f05162 | -2.82451 | -54.02063 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46f99774-cea9-3e27-a429-e8e7f20d4026 | -2.68346 | -54.03057 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b385255-2b2d-39b8-b1ed-2e669be0da58 | -2.47771 | -54.17355 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d712929f-d8db-3fb3-b1ea-07e87320c59f | -3.99676 | -46.69431 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a2945d4-fad3-3926-be1a-1a820cc792f8 | -4.33728 | -46.49412 | 2024-12-28 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20c831d2-4bc0-3316-96f3-7af295aa493a | -3.74319 | -47.19673 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e8f6b10-d002-36bd-94e3-2aed730a4399 | -2.44183 | -54.207 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56b39d5b-4228-3d7c-b38e-e933b6fd37b2 | -6.21175 | -46.22308 | 2024-12-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e27825e1-07d9-35db-8675-a246cf40a7f4 | -2.84516 | -51.87445 | 2024-12-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 137b691c-7abc-31d7-b267-d2b552a6afb5 | -3.43972 | -53.29599 | 2024-12-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62b1780c-0d6b-3d6a-96d0-dae7942735db | -2.44847 | -53.99088 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9014f36-dc2f-313d-a4b9-cc560e9c1f78 | -4.10269 | -46.81119 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a663e44b-6d6a-342b-928e-dfb545c61743 | -4.50439 | -44.23223 | 2024-12-28 05:01:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bd9f979-07ea-3a06-9a21-0313ae8d0555 | -3.03531 | -53.90982 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af873ae4-b045-3eca-9e27-85c9e698c9bf | -3.19504 | -46.12915 | 2024-12-28 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45953222-b31d-30a0-8f6b-baea739489d8 | -5.90525 | -43.48201 | 2024-12-28 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4306e075-2290-353c-9830-f4601656d8b9 | -2.68291 | -54.03406 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ff3803a-a4a1-3dc3-ac59-b41ec2ecd2db | -5.31632 | -46.06546 | 2024-12-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4c305a8-2067-35ef-81e9-28b23f82b567 | -3.7481 | -47.19752 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be865476-4704-39f7-9bca-1f4e83fd3a38 | -3.9235 | -46.98378 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88c85f70-e43d-36f1-bb5c-4c90c2542d7c | -2.4788 | -54.1666 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c694c76c-e0bd-363e-b5b1-d5ba21a13653 | -5.5773 | -46.13341 | 2024-12-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d5fe2568-0503-32ee-bc03-12c1a947d520 | -3.94 | -46.76196 | 2024-12-28 05:01:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c56d965a-2833-304b-8a67-3fc2c169a30c | -5.57234 | -46.12917 | 2024-12-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47c24ec4-e2d8-3eef-adaa-6df2d6b9822a | -2.53169 | -53.95766 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9beb8b02-3163-3678-9a98-be76ce4fafab | -2.9038 | -54.48833 | 2024-12-28 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6419dad-a7c7-3651-ba42-d0507f06a64b | -2.16582 | -54.42915 | 2024-12-28 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d170e3bf-dab1-36fb-9ff2-a73608831936 | -5.48095 | -46.44302 | 2024-12-28 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dadab3b-07c5-34fe-86ac-3e67852e4d26 | -3.74056 | -47.34658 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f29af246-60bf-3ebc-a9df-5fadc5bdd7d8 | -3.99644 | -46.94162 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13a28779-71e8-3c4b-9988-96dadd407420 | -2.85702 | -48.32129 | 2024-12-28 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5484ec7d-b165-3ad5-a6b6-2d11134e871f | -4.08611 | -46.81798 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c172177c-594d-356b-ab69-2b51433bd330 | -2.57739 | -54.03628 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7e67d7b-582c-351d-8cbe-b47adb1b0d46 | -3.44313 | -53.2965 | 2024-12-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adf7474f-7c88-33aa-a7d8-d60b935cb4c3 | -5.57187 | -46.13253 | 2024-12-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e06efe7-5478-3bee-92de-bfef42206559 | -2.21823 | -53.64264 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1832fde0-244c-3ba4-a227-35649fa90481 | -3.96657 | -46.68608 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f12cb2ad-c9af-34e5-af64-bdcbc5196ca2 | -2.87021 | -51.80668 | 2024-12-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec88ca41-7741-358d-8b67-ec145a7de610 | -6.11904 | -43.94921 | 2024-12-28 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e875b435-790b-33c1-934e-893396c09669 | -3.73826 | -47.196 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8bbbc58-6d42-39be-9c3c-5019f1242ff0 | -3.18932 | -46.13156 | 2024-12-28 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cf0015c-4364-3a1d-9855-cc720486bf6a | -3.87396 | -46.6941 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e3bc769-4b55-3ee5-9633-9a00d2145a78 | -3.93395 | -46.98244 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23bca4fe-86a6-374c-80fd-ce1e4c077c79 | -4.56089 | -45.99168 | 2024-12-28 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 474bd74e-60ca-3bc8-b0b9-fa1b333cc24f | -4.12638 | -46.6862 | 2024-12-28 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dda830e6-c3d7-3cbd-a3ae-24878cb26da7 | -2.48544 | -54.16763 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 208d06b1-d0e2-361e-be3f-1c2cadcf7277 | -3.744 | -47.19129 | 2024-12-28 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36c0b330-ad52-3de1-bed1-8fda818501b6 | -4.55653 | -44.12587 | 2024-12-28 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fba90de7-ff13-302b-ae86-eab7b67e61a8 | -2.91381 | -54.0129 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f349482-94b6-30e5-9007-543326cdea75 | -5.91093 | -43.48858 | 2024-12-28 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1209d1ad-f739-34fe-818a-682bd7cea3ff | -5.58138 | -46.14386 | 2024-12-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6e5a322d-8f8f-3a9b-ad22-a184f4e5eea6 | -4.00145 | -46.94254 | 2024-12-28 05:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a09dea8a-9137-354d-af23-4afb81d740fd | -3.0381 | -53.91386 | 2024-12-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48d79d3a-7615-32fb-991a-816cf5cbde31 | -2.41811 | -54.22816 | 2024-12-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README22.md)
