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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaf4b0c4-3069-333e-bc18-f16c7548be35 | -5.2236 | -43.8036 | 2024-10-09 00:41:32 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e2b28bb-065e-3b22-9469-52c8f4809dcd | -5.2255 | -43.811901 | 2024-10-09 00:41:32 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70cca371-96c5-3bbf-980d-d1ca9e5c43cf | -5.2275 | -43.820202 | 2024-10-09 00:41:32 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f67bfa5-24f1-3d7f-9aa3-113483bfefe5 | -5.4959 | -45.369598 | 2024-10-09 00:41:34 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f067aa5-a199-3a07-be42-8a66506158c4 | -5.4976 | -45.376801 | 2024-10-09 00:41:34 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9611f931-d0ab-3b3a-97af-fba857f34633 | -5.7629 | -46.572201 | 2024-10-09 00:41:34 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 175c28e8-d734-3ada-94bb-3602231810ec | -6.4841 | -49.9002 | 2024-10-09 00:41:35 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50694cb4-0132-3fa8-b0d9-6ed0b7ba0a0f | -6.486 | -49.908501 | 2024-10-09 00:41:35 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12f6dcb8-6951-34c5-8aa7-cdd610b9d525 | -6.4878 | -49.916801 | 2024-10-09 00:41:35 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4a9972f-5b8b-3a6d-8663-215103f32b22 | -5.4768 | -45.509499 | 2024-10-09 00:41:35 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb2d54cb-0591-3255-b593-c347d7c4c650 | -5.4506 | -45.485401 | 2024-10-09 00:41:35 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c80b02a3-daac-3d42-9c85-266af07269e0 | -5.4522 | -45.492599 | 2024-10-09 00:41:35 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f18daa2-0ea7-35a9-946a-226692ab3152 | -6.445 | -49.908699 | 2024-10-09 00:41:35 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17c7aab9-8842-3f45-ad8a-b5556b95b44a | -6.4468 | -49.917099 | 2024-10-09 00:41:35 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d7e39ee-7790-3e39-babf-ca6d9ce2e387 | -5.5774 | -46.303299 | 2024-10-09 00:41:36 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b691b57-953b-377a-813d-b92f56c71ecc | -5.579 | -46.3102 | 2024-10-09 00:41:36 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80628cbf-74cc-330b-ab2c-57eee27ff1d6 | -5.5916 | -46.3652 | 2024-10-09 00:41:36 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a8cc783-0934-3b2d-9443-cac5c54787e1 | -5.5932 | -46.372101 | 2024-10-09 00:41:36 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9caba11e-d0d5-3f6d-9ee7-c275e44e6027 | -4.9435 | -43.665298 | 2024-10-09 00:41:36 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd633286-a390-38ad-b7e1-99a0df30d60d | -4.9455 | -43.673801 | 2024-10-09 00:41:36 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d5534c4-0fc8-3d37-a912-d232aa8a4027 | -4.7278 | -42.968102 | 2024-10-09 00:41:37 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f853522-4ac0-306a-80fc-9cc7d04af969 | -4.73 | -42.977402 | 2024-10-09 00:41:37 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac0a8a9f-b987-3f6b-adc2-4c4a17dc0359 | -4.7322 | -42.986698 | 2024-10-09 00:41:37 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5aefb675-69c0-33d6-87d5-e2503c1ba2e4 | -5.8545 | -48.1493 | 2024-10-09 00:41:38 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9620e2df-3d6e-31a5-a959-e9bb37984637 | -5.8561 | -48.1563 | 2024-10-09 00:41:38 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 406488a0-bcf6-3372-a3e9-62fbb3d008eb | -5.8577 | -48.163399 | 2024-10-09 00:41:38 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| cad3b81a-b8b7-3712-b7cf-d6dfaf7c809f | -5.8447 | -48.151402 | 2024-10-09 00:41:39 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| abbc7259-3977-30f1-877a-dd36adaf70c0 | -5.8463 | -48.158501 | 2024-10-09 00:41:39 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| fe17be3e-4218-3df6-b26e-44ee62d69bf9 | -5.5566 | -47.021702 | 2024-10-09 00:41:39 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e15e133-dfc3-3d55-86ab-a809a5e2c12b | -5.5581 | -47.0285 | 2024-10-09 00:41:39 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 878cad11-365f-3584-8d4e-f2ce4fc1d4b2 | -5.5597 | -47.035301 | 2024-10-09 00:41:39 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52101e33-74bf-3085-a86f-1a2820c7ce4c | -5.2602 | -46.134998 | 2024-10-09 00:41:41 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8fbfce99-51ac-3796-a313-7444049e09b3 | -5.2617 | -46.141899 | 2024-10-09 00:41:41 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12acf791-d55c-3cd3-8bb9-44751139a16f | -5.2633 | -46.148899 | 2024-10-09 00:41:41 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce2d5535-ce56-3245-977e-58ea638b870c | -5.5525 | -47.455101 | 2024-10-09 00:41:41 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37393955-ef31-395e-b088-569ab33fda15 | -5.5541 | -47.462002 | 2024-10-09 00:41:41 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e17ec261-28e7-3791-9186-7dcf5d2537d6 | -4.2515 | -41.913898 | 2024-10-09 00:41:41 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d2631852-4c07-3fa3-ad3b-e2d97dc36930 | -4.2541 | -41.924801 | 2024-10-09 00:41:41 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 610394a6-58db-3835-afb9-021ba30cc765 | -4.2417 | -41.916199 | 2024-10-09 00:41:41 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b1fe1d3-3d75-3e31-85e8-74e15de37957 | -4.2443 | -41.927101 | 2024-10-09 00:41:41 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2c416524-f420-383e-bbda-a1e50be39be7 | -4.8702 | -44.807701 | 2024-10-09 00:41:42 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bae682a5-0341-34e0-b96f-6aab2c1031ac | -4.872 | -44.815201 | 2024-10-09 00:41:42 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01552da3-6a3d-3c3a-a9ab-05a9cafbeddc | -6.4084 | -51.693298 | 2024-10-09 00:41:42 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f343efb-f6f5-3b36-b044-229638843b8a | -6.4107 | -51.7038 | 2024-10-09 00:41:42 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d18d13d-5687-39e2-8c7b-a902c8a44ea9 | -6.3986 | -51.6954 | 2024-10-09 00:41:42 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e2d9fbe-7c80-3e0f-8d20-6b84a666f951 | -6.4009 | -51.705898 | 2024-10-09 00:41:42 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 886f6912-9d0e-3813-aaa2-0b1403b9a55c | -4.4406 | -42.886398 | 2024-10-09 00:41:42 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64cf5f4f-f9d3-3db6-97a5-fe9e940e8f05 | -4.4428 | -42.895901 | 2024-10-09 00:41:42 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d882deb8-8897-3be7-96f6-82890e7286e1 | -5.0602 | -45.8941 | 2024-10-09 00:41:43 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0e9dedd-10c7-37a3-8c9f-7c2906dac8fb | -5.0113 | -45.816502 | 2024-10-09 00:41:43 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e43b1b50-f547-3c09-a8a9-cbd60a16ddb0 | -5.013 | -45.823502 | 2024-10-09 00:41:43 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2c09b7f-9ae8-34b2-990c-98420154a8af | -4.6545 | -44.369099 | 2024-10-09 00:41:44 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4395f95d-df11-30d5-a2e4-958fd3028a58 | -4.6429 | -44.3633 | 2024-10-09 00:41:44 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59957af7-73b2-3b2b-9778-aa31d1431e0b | -4.6447 | -44.3713 | 2024-10-09 00:41:44 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67e69db5-a250-3720-afb8-79efb1f54c22 | -4.6466 | -44.3792 | 2024-10-09 00:41:44 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b1a27d0-4b39-3b01-aee1-37a7cfdbbb93 | -4.9247 | -45.664902 | 2024-10-09 00:41:44 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba821a6-715d-3e32-9bb8-39e795508627 | -4.9264 | -45.672001 | 2024-10-09 00:41:44 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1600d0f0-d00a-37f4-b933-71a39e87a275 | -5.5256 | -48.334301 | 2024-10-09 00:41:44 | METOP-C | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13d6b3bd-1245-32d2-9b48-4cee15147127 | -5.5272 | -48.3414 | 2024-10-09 00:41:44 | METOP-C | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aab7a971-6b0a-32a9-87cc-a05a62d5113e | -5.5305 | -48.355701 | 2024-10-09 00:41:44 | METOP-C | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f16f38b5-ffe3-36b8-87c8-0cfe13a185cd | -5.8504 | -49.823299 | 2024-10-09 00:41:45 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40e041b5-3daf-3ee6-b0d7-3eb29b97416b | -5.7153 | -49.266399 | 2024-10-09 00:41:45 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e75962ab-2891-3a50-b914-37a678538557 | -5.8406 | -49.8255 | 2024-10-09 00:41:45 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73b2839e-c06a-3987-94b9-886a00ec4a13 | -5.8425 | -49.833698 | 2024-10-09 00:41:45 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a138161-a93a-32bb-b838-c5ea30b7a4b5 | -5.3481 | -47.689098 | 2024-10-09 00:41:45 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48224788-9275-37f6-b8f5-9f0a573432c3 | -5.7055 | -49.2686 | 2024-10-09 00:41:45 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7027b7e8-e080-3252-9f24-c8e9271014de | -5.7072 | -49.276299 | 2024-10-09 00:41:45 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6e4fa17-9c2d-35b2-854a-d31dca539e58 | -5.4605 | -48.273998 | 2024-10-09 00:41:45 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| be761ef3-7921-3261-9770-e25b64f93d8a | -5.4621 | -48.281101 | 2024-10-09 00:41:45 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a3eb6560-0209-3946-a2a2-5b5b3fee7c7e | -5.4293 | -48.318199 | 2024-10-09 00:41:46 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2fb0e914-0ba2-392f-91bb-33cc8bcc0ede | -5.4309 | -48.325298 | 2024-10-09 00:41:46 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 73db5947-ff33-3c81-86d1-83a1f61e2408 | -5.4325 | -48.332401 | 2024-10-09 00:41:46 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2a0aec52-31c4-3cb1-af8d-7f876a7a327c | -5.3804 | -48.284302 | 2024-10-09 00:41:47 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e30d3fc7-9bdc-3584-b8b8-db94e5642c57 | -5.7113 | -49.9823 | 2024-10-09 00:41:47 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b11bfbbc-dc30-3fb5-ade5-a846f3c2c9d3 | -3.8263 | -41.597599 | 2024-10-09 00:41:47 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e0983969-75c0-37d7-b69c-a86414458188 | -3.8139 | -41.588299 | 2024-10-09 00:41:47 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ca64b9fe-cd5e-3092-af0c-c0cc178baf40 | -3.8166 | -41.599899 | 2024-10-09 00:41:47 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d5a78dd0-ea58-3e42-b787-e8bb33b66e23 | -3.8194 | -41.6115 | 2024-10-09 00:41:47 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ffa425c6-292b-3c14-a872-8cf445d662ad | -3.8041 | -41.590599 | 2024-10-09 00:41:47 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c619055f-b579-3ca7-add4-dcda696d0af1 | -3.8068 | -41.6022 | 2024-10-09 00:41:47 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f1788eca-c081-3f5c-b77b-eb05d8bacb9d | -3.8096 | -41.6138 | 2024-10-09 00:41:47 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f759bf09-de63-35fb-a765-9ffc5dbb330b | -3.7943 | -41.592899 | 2024-10-09 00:41:47 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9799823c-5d78-3db6-94ba-2c9313a3f04c | -3.7971 | -41.6045 | 2024-10-09 00:41:47 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9efdcc94-1613-3ecf-b169-b1e327dc932e | -3.7998 | -41.6161 | 2024-10-09 00:41:47 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cab097de-af2b-3c7e-9435-5f4ec0232d11 | -5.7134 | -50.1297 | 2024-10-09 00:41:48 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7272f934-4451-3180-a579-14cb7b4fe03b | -4.6814 | -45.817001 | 2024-10-09 00:41:49 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a269f13-075b-35f9-9c1a-18993b545869 | -4.6928 | -45.866402 | 2024-10-09 00:41:49 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f5621864-b81d-3b31-8d8c-2eabb03f00b1 | -4.6814 | -45.8615 | 2024-10-09 00:41:49 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5b7e1e11-44b6-36c6-b7ff-e7fee38cc8dc | -4.683 | -45.868599 | 2024-10-09 00:41:49 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3203bf3d-c726-3185-835b-cdb22a6c0c20 | -4.6847 | -45.875599 | 2024-10-09 00:41:49 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa0e2e71-59a0-348c-a712-46ee41300f8c | -5.0187 | -47.329201 | 2024-10-09 00:41:49 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 77aeff2c-1636-3402-b048-d27ebe78ba26 | -5.0203 | -47.336102 | 2024-10-09 00:41:49 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d30ed29c-c6d0-3a60-aa12-0526e50e98cd | -5.2608 | -48.393002 | 2024-10-09 00:41:49 | METOP-C | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 52f18fb1-0d00-340e-8909-721fbca32ecd | -4.6125 | -45.6082 | 2024-10-09 00:41:49 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07b4739f-0c52-309c-93d5-282ea1081d38 | -4.3705 | -44.434101 | 2024-10-09 00:41:49 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b005bf6e-4d0c-317c-9d36-e5e88cd8cd7c | -4.2872 | -44.386398 | 2024-10-09 00:41:50 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 313d3bd7-3222-3a06-8633-42bb2a1416dc | -4.2891 | -44.394299 | 2024-10-09 00:41:50 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 782fbf6f-8e5b-3696-8852-039b1d2da306 | -4.2774 | -44.388599 | 2024-10-09 00:41:50 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1eeabe5c-c946-3a8e-955a-ead3b020379e | -4.2793 | -44.3965 | 2024-10-09 00:41:50 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7ab1918-aa0e-3885-85d6-e48990af3dd0 | -4.226 | -44.256901 | 2024-10-09 00:41:50 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README18.md)
