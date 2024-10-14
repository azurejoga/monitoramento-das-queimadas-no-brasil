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
| 491d2a17-031e-3b74-abd8-28e1559b02b5 | -5.0646 | -45.877899 | 2024-10-14 00:38:31 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 03d7af6b-8c75-33e6-a956-9c093e5a0205 | -3.7541 | -40.494499 | 2024-10-14 00:38:32 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d634c628-cfa4-3c29-a7c0-4e03a901f1bd | -3.757 | -40.506599 | 2024-10-14 00:38:32 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| de780c49-f0fd-3de9-a52e-46ff43351faa | -4.9639 | -45.619301 | 2024-10-14 00:38:32 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2cd952ed-0cd8-3605-b66f-e9c60a021c5c | -4.9655 | -45.626099 | 2024-10-14 00:38:32 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dbc43013-678b-3750-a961-e2eed55cdbc8 | -5.4073 | -47.925701 | 2024-10-14 00:38:33 | METOP-C | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 769dea1c-574e-390d-a36e-2e0d929b8121 | -4.0856 | -42.287899 | 2024-10-14 00:38:34 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2f5236d2-5236-372f-9228-2d28687a7332 | -4.4269 | -43.9226 | 2024-10-14 00:38:34 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a89b1a6-d801-33b5-903b-8e3f5c1f1983 | -4.4287 | -43.930199 | 2024-10-14 00:38:34 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7120499-9282-31d3-b5b4-7deef4651ba5 | -5.6067 | -48.949699 | 2024-10-14 00:38:34 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79549de8-9bfd-37f4-b6b2-8ed2ee53885f | -5.5969 | -48.951801 | 2024-10-14 00:38:34 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66b1fd1b-2e03-3029-a1e6-1bc713af79c1 | -4.9069 | -45.999599 | 2024-10-14 00:38:34 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d14adef-48db-3533-a6e9-807f26ad5a0a | -4.9085 | -46.0065 | 2024-10-14 00:38:34 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86da3c7b-4cb4-3d77-bb6c-d7af51e2bcc8 | -4.91 | -46.013302 | 2024-10-14 00:38:34 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 119aa46a-c46f-3974-91bf-4a0c4622e93c | -4.8971 | -46.001801 | 2024-10-14 00:38:34 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26f70a60-557e-3f9b-bfd8-3267fbccc27a | -4.8987 | -46.008701 | 2024-10-14 00:38:34 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1656a90c-3eb8-34a9-88bb-8e66e9de7fde | -4.9002 | -46.015499 | 2024-10-14 00:38:34 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b999cbb-ef84-375d-be06-84c526fb4885 | -4.6221 | -44.852501 | 2024-10-14 00:38:35 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffeca7ac-0245-38a9-8243-bbadf2d5dca3 | -4.6237 | -44.859699 | 2024-10-14 00:38:35 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eeffef16-5d20-371d-963f-aecf48ccfa18 | -4.6254 | -44.866798 | 2024-10-14 00:38:35 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e88983a-27af-3e19-9b64-493b93c5d885 | -4.837 | -45.785 | 2024-10-14 00:38:35 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ad7b003-60e0-3431-b229-4077b46a9d53 | -4.6139 | -44.8619 | 2024-10-14 00:38:35 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 000e6185-cd44-33f6-a318-b8c59ef0695b | -4.8272 | -45.787201 | 2024-10-14 00:38:35 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25d346e2-92a3-3643-a41c-4b16abedcfa8 | -4.8288 | -45.794102 | 2024-10-14 00:38:35 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b87a276e-288f-3405-99bd-10193b1663e2 | -4.8398 | -45.842098 | 2024-10-14 00:38:35 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b19be932-bfef-3958-bfde-9b7cb234d7de | -4.8414 | -45.8489 | 2024-10-14 00:38:35 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b4647be-4238-3e71-99f8-13e8469aaa8d | -4.9886 | -46.491501 | 2024-10-14 00:38:35 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce9de95c-cfa3-37ff-a090-e5eb6b4ff018 | -4.7998 | -45.757401 | 2024-10-14 00:38:35 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98b41116-ef0d-39dc-9c64-32d46546cafa | -4.7766 | -45.791401 | 2024-10-14 00:38:36 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 810280d4-1467-3e59-b18d-d70882ffb005 | -4.0437 | -43.031898 | 2024-10-14 00:38:37 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d46a68d3-485a-377c-bd04-761dda49a0cd | -4.0457 | -43.040401 | 2024-10-14 00:38:37 | METOP-C | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 296b55e4-1ae9-3fe2-ab4f-6721fb712769 | -4.0319 | -43.025799 | 2024-10-14 00:38:37 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 873d0db7-e974-3a0f-941e-89d53f21962d | -4.0339 | -43.034199 | 2024-10-14 00:38:37 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ed072dd-00d3-30c5-9600-20c4c63acd69 | -4.0359 | -43.042702 | 2024-10-14 00:38:37 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 364bdd7a-90ce-3dd4-bb2d-ef6151fe8db9 | -4.0379 | -43.051102 | 2024-10-14 00:38:37 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cecdb195-5abe-3cc7-91f6-8ac70d6c1562 | -4.6533 | -45.703701 | 2024-10-14 00:38:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a66f348e-7b1e-3e75-bc74-7c4078b7d9cb | -4.6549 | -45.710602 | 2024-10-14 00:38:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2597045-a9d1-3427-9133-328dc03e13a9 | -4.6565 | -45.7174 | 2024-10-14 00:38:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b42adc66-f38d-35c0-8320-55335a42add9 | -4.6435 | -45.705898 | 2024-10-14 00:38:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d6d4eba-d433-3568-a496-868a068c68b0 | -4.6451 | -45.712799 | 2024-10-14 00:38:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 630816b1-c4b5-35e6-8e23-49e33ac4349d | -4.6467 | -45.719601 | 2024-10-14 00:38:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7176ee8-39ba-3d44-9053-7886d11b366d | -4.9006 | -46.828602 | 2024-10-14 00:38:37 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cffe3d6e-cb76-389f-ba74-5d9e02b2434b | -4.9022 | -46.835499 | 2024-10-14 00:38:37 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 280cfce5-12d1-3177-8fe9-f1267f8eca69 | -4.6337 | -45.708099 | 2024-10-14 00:38:38 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7baf8b6f-35e2-3f74-80ba-4259379388b2 | -4.6617 | -45.874901 | 2024-10-14 00:38:38 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e9dd5bd8-cddb-37d6-aa22-7ee0996ab8d7 | -4.6633 | -45.881802 | 2024-10-14 00:38:38 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 194837c1-e386-3704-8524-0dd231e28772 | -5.0656 | -47.644699 | 2024-10-14 00:38:38 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e16b504-e7bb-313f-bcee-58b68b39ed3c | -4.7131 | -46.1437 | 2024-10-14 00:38:38 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43400fdd-0422-34f7-93c5-258480703cc4 | -4.7147 | -46.1506 | 2024-10-14 00:38:38 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db2b0198-6534-3839-b4e0-4318a72294e8 | -4.7163 | -46.157398 | 2024-10-14 00:38:38 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62df0bf9-1e8a-35e7-9c14-f7c3cce25577 | -3.9244 | -43.139 | 2024-10-14 00:38:39 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9e39524-33a0-37e9-822a-beafaa04f9c6 | -3.9264 | -43.1474 | 2024-10-14 00:38:39 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2a012dd-3baf-347c-b288-c9ab0e407d53 | -3.9283 | -43.155701 | 2024-10-14 00:38:39 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a9a79bc-c2e8-3dbc-b1e0-0545738c2361 | -4.83 | -46.8806 | 2024-10-14 00:38:39 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad47bfc2-b1fe-32eb-a546-47c230f712bd | -4.8316 | -46.887501 | 2024-10-14 00:38:39 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac26388f-4c85-368c-8673-bd79a5bfe1aa | -5.0561 | -48.057301 | 2024-10-14 00:38:39 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 945efb72-1be5-3273-b912-eb5c8122170f | -5.0577 | -48.064602 | 2024-10-14 00:38:39 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ec295083-b235-31c2-9b09-694f515dece3 | -5.0594 | -48.071999 | 2024-10-14 00:38:39 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c1c255e9-5d46-3135-8a1c-2d083224b0dc | -3.9146 | -43.141201 | 2024-10-14 00:38:40 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27376767-13cd-30c6-9d6d-2023b2fa4dbf | -3.9166 | -43.149601 | 2024-10-14 00:38:40 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 548c0538-ec42-3040-bece-2d4af23dbf73 | -4.6102 | -46.324799 | 2024-10-14 00:38:40 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 448f6ed9-31fc-3a68-842d-85ff381a7c4e | -4.6118 | -46.3316 | 2024-10-14 00:38:40 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06ba56c2-7e36-3403-b20f-e8460e7e2167 | -4.8893 | -47.638901 | 2024-10-14 00:38:41 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ebe5a761-b68e-3014-b212-b2de63d4f946 | -4.8909 | -47.646 | 2024-10-14 00:38:41 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25d1a9a0-5545-367a-94c1-b37ce79dd976 | -4.6562 | -46.796398 | 2024-10-14 00:38:41 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a28482f-cae0-320f-9e38-96471616dbb5 | -4.6578 | -46.803299 | 2024-10-14 00:38:41 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed201ce7-283b-3978-abde-bb58931877d2 | -4.6594 | -46.8102 | 2024-10-14 00:38:41 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 101ce7db-41e3-3b6e-94a1-ff347f3a6d69 | -4.648 | -46.8055 | 2024-10-14 00:38:41 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f71ebd7-e65a-310f-929c-ad08a461abdf | -4.6496 | -46.812401 | 2024-10-14 00:38:41 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7eac3e5d-9a5b-329e-8416-9cda3c84fb59 | -4.7078 | -47.294102 | 2024-10-14 00:38:42 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9f7274e-f01f-3a58-aa79-e9943e685e04 | -4.7094 | -47.300999 | 2024-10-14 00:38:42 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d2ae375-60cd-314c-941c-62dc922f62a4 | -4.0359 | -44.2817 | 2024-10-14 00:38:42 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c701bd7-62e1-3d56-8a0b-eaf3b7203313 | -4.0376 | -44.2892 | 2024-10-14 00:38:42 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac6615f5-8331-3425-8802-3f7a92dfbc44 | -4.2026 | -45.761799 | 2024-10-14 00:38:45 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab0c7947-7c4e-3c4e-8623-ab2c1a8a0810 | -4.2041 | -45.7686 | 2024-10-14 00:38:45 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 095b1014-485e-37ab-8db9-35c9b3ee0a39 | -4.2057 | -45.775501 | 2024-10-14 00:38:45 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7800caee-8181-3560-a7a8-ca4ca4c4ba30 | -3.0184 | -41.167801 | 2024-10-14 00:38:47 | METOP-C | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c02c8c4a-37d5-3195-b2ca-0cfc2ebcf3c9 | -3.0059 | -41.158798 | 2024-10-14 00:38:47 | METOP-C | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 71dc95bc-096b-37cb-83b4-bb0b516dd9cc | -3.0086 | -41.169998 | 2024-10-14 00:38:47 | METOP-C | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 929af8a7-8319-3e7a-8e3b-249d15e5e82a | -3.4307 | -43.056 | 2024-10-14 00:38:47 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 532a573a-c447-3867-9756-ac91e31f2ec6 | -3.4327 | -43.064602 | 2024-10-14 00:38:47 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d79b3107-e866-38e0-ac7c-4f634b580c25 | -3.4347 | -43.073101 | 2024-10-14 00:38:47 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81f68d56-f05a-36a9-afb7-f0feb3c8e505 | -3.4229 | -43.066898 | 2024-10-14 00:38:47 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 184a9d65-c794-321e-82e7-ecdd21ac2d11 | -3.4249 | -43.075401 | 2024-10-14 00:38:47 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 642aec23-5624-3b44-b41f-8ecfb828aae4 | -4.0086 | -45.456699 | 2024-10-14 00:38:47 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c1cb920-0bf5-3f0c-b2d0-f6e1cfdd1f90 | -4.0102 | -45.463699 | 2024-10-14 00:38:47 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 868e30b4-3359-3cc8-9686-59e1b431aaf5 | -3.3034 | -42.819801 | 2024-10-14 00:38:48 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e865b9bd-cc7f-3a01-912d-0617ea26799f | -3.3055 | -42.828602 | 2024-10-14 00:38:48 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00441ae8-7167-34f6-a641-c57aa0600e2b | -3.3075 | -42.837502 | 2024-10-14 00:38:48 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10844c68-a7a1-3ad6-a428-ce2d85aa4b7c | -3.3096 | -42.846298 | 2024-10-14 00:38:48 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b06710e8-3276-3daf-b660-2fb84fcca135 | -3.3116 | -42.855 | 2024-10-14 00:38:48 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c19a0f24-f932-3cd6-be7f-41c05ca72815 | -3.2936 | -42.822102 | 2024-10-14 00:38:48 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 264fc2d5-c68b-3e14-b38d-06c6caeb625f | -3.2957 | -42.830898 | 2024-10-14 00:38:48 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e81205ce-f123-36ec-a784-cee9e7685a68 | -3.2977 | -42.839699 | 2024-10-14 00:38:48 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a18cfc42-a539-3e5e-9587-a26b0694f9d7 | -3.2998 | -42.848499 | 2024-10-14 00:38:48 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4fc3bc2-e2dd-3370-8d76-099d017cdb61 | -3.3833 | -42.9855 | 2024-10-14 00:38:48 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a5ab56d-d68b-32cd-9ed9-16cd5b8b5c52 | -3.3853 | -42.994099 | 2024-10-14 00:38:48 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a40b1a6-9906-373a-8d9c-82496559cbc5 | -3.4152 | -43.343102 | 2024-10-14 00:38:48 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bc568df-5034-3998-9ff1-aa9b2910bd78 | -3.4171 | -43.351299 | 2024-10-14 00:38:48 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a45f14e-1e9f-3b25-8e8e-3d1202bd36ba | -3.9011 | -45.706501 | 2024-10-14 00:38:49 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
