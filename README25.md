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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94ca99e8-685d-31bd-9875-9026f736d541 | -13.2824 | -45.1776 | 2026-07-08 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 390.8 |
| f61d4d9a-7b6b-3fcc-9898-877bff23a2d8 | -13.2966 | -54.4068 | 2026-07-08 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 175.7 |
| 611e34cd-e41a-3b6e-8d89-990166a7ca31 | -13.9594 | -45.2018 | 2026-07-08 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 5e42add5-8d95-3d91-8936-25b67318d2a6 | -13.282 | -45.2009 | 2026-07-08 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 08250385-ce07-370c-8983-1fe11a84a87c | -13.2772 | -54.4295 | 2026-07-08 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 9208b65c-363e-3d7d-b0c1-b9d246af5d2c | -17.5311 | -54.0186 | 2026-07-08 14:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 897c942b-98cc-366d-a356-6985fa1d5deb | -14.1445 | -52.8715 | 2026-07-08 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 6e13e6c5-fb6e-3b08-8c90-ced970f039d5 | -13.2774 | -54.4088 | 2026-07-08 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 136.0 |
| b9975e3c-1efc-34a3-ba23-e362b64eae1e | -5.9177 | -43.8584 | 2026-07-08 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1a0cec27-6adc-3cef-839a-422a478c1c4b | -10.421 | -46.8603 | 2026-07-08 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 8f2b51bd-41ae-3c09-99fc-5027edc51919 | -10.4397 | -46.8804 | 2026-07-08 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 2db313c7-8afd-32da-b62c-c66e81845aad | -6.4973 | -42.2142 | 2026-07-08 14:40:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 107.3 |
| 263a0bb0-3728-3622-9e42-8856450a4dfd | -10.4207 | -46.8827 | 2026-07-08 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| fbd7466e-34c8-3a49-a614-66bb9c07c8c8 | -13.2631 | -45.1808 | 2026-07-08 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 52346e58-6878-3cbc-9489-cf2f8f05820f | -13.2963 | -54.4275 | 2026-07-08 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 194.0 |
| a816ef0b-c9ee-3dae-ade6-8de7f617faf0 | -14.1442 | -52.8926 | 2026-07-08 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 137.3 |
| cf23bbe9-c94a-35bd-93df-7b914908619a | -10.4397 | -46.8804 | 2026-07-08 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 1b957b41-269a-31e8-9c8d-3cbf34766bcf | -6.4973 | -42.2142 | 2026-07-08 14:50:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| 026876f9-5059-3963-a5a4-2b58a891acd4 | -13.2772 | -54.4295 | 2026-07-08 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| e66b610e-7de2-3ac1-ba4d-6aec3a85c18f | -13.2824 | -45.1776 | 2026-07-08 14:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 289.5 |
| a873b532-eb18-3ed6-9880-c8fee4e88019 | -14.1445 | -52.8715 | 2026-07-08 14:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 71ad4bbb-0173-3cca-9958-a7db5a81e6a3 | -13.2963 | -54.4275 | 2026-07-08 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| f53b372c-8d2d-3ec1-90f1-25dc7173ee8d | -13.282 | -45.2009 | 2026-07-08 14:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 068c0e33-9266-34c8-b4dd-f0bbf31a45c8 | -5.9177 | -43.8584 | 2026-07-08 14:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 26367a9f-ac63-3d12-8ee8-4fa02a7e77fd | -14.1442 | -52.8926 | 2026-07-08 14:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 150.0 |
| ddc0403e-1a71-3eb4-9c7e-8ac2afd53fbc | -10.421 | -46.8603 | 2026-07-08 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 18e907e8-4ad9-347c-b83e-79219137a695 | -13.2774 | -54.4088 | 2026-07-08 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 9d25436f-2c21-3cad-94ed-a7c9f6087570 | -13.9594 | -45.2018 | 2026-07-08 14:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 33ef84bf-6f55-3064-afe2-2ec8f86d7e20 | -13.2966 | -54.4068 | 2026-07-08 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 9c39965a-2137-3e79-bce7-67f427d75f15 | -10.4207 | -46.8827 | 2026-07-08 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 49373c7f-7f7c-3227-a6f1-7ec3df1f5804 | -13.2824 | -45.1776 | 2026-07-08 15:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 240.7 |
| d4d45a4c-f608-3c48-be4e-34ed6f0612fb | -13.2966 | -54.4068 | 2026-07-08 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 7feb0725-986e-377b-95cb-8b9cd02c040a | -13.2774 | -54.4088 | 2026-07-08 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 8d99c626-59cf-32a1-9e45-f1a03aef9a86 | -10.4397 | -46.8804 | 2026-07-08 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e1905bed-7b6f-3ae9-b3b6-c4f687204ede | -13.2772 | -54.4295 | 2026-07-08 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| d4e29b67-9bcc-3c4c-b043-24ee26065b1c | -5.9177 | -43.8584 | 2026-07-08 15:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| a8f45bfb-fe6b-3793-adc8-586290715f73 | -13.2963 | -54.4275 | 2026-07-08 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 8ae9444d-903e-3d0d-b862-9bc3f5468d0f | -6.4973 | -42.2142 | 2026-07-08 15:00:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 6917c932-12ef-3436-8758-1a846fc790fb | -14.1445 | -52.8715 | 2026-07-08 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 0fb7f990-f87f-3fea-b540-dfe2e78eebc6 | -13.282 | -45.2009 | 2026-07-08 15:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 58c59809-b022-37e3-8cc0-e72e66faee8f | -13.3543 | -54.38 | 2026-07-08 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| d1e44ca4-51d7-3809-a608-56503c951a62 | -13.2824 | -45.1776 | 2026-07-08 15:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 215.5 |
| e24b7dbc-aae4-3228-9e1a-6885ee98522e | -13.3352 | -54.382 | 2026-07-08 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 628b7f1d-2407-3c35-91e2-7331752feb28 | -13.3355 | -54.3614 | 2026-07-08 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 7b165f04-1949-39ea-8964-1331c25184fd | -5.9177 | -43.8584 | 2026-07-08 15:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 44d91599-ff0b-3294-b54a-49db60731acd | -13.2966 | -54.4068 | 2026-07-08 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 226.1 |
| c1794322-d064-3ebf-a6b5-8000e502a288 | -13.2772 | -54.4295 | 2026-07-08 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 49197783-df5f-3402-9803-a21153225b6e | -14.1445 | -52.8715 | 2026-07-08 15:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 16ab1590-46b6-3c99-9b44-8890dcfcbbb5 | -13.282 | -45.2009 | 2026-07-08 15:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 97919cfd-aac3-3261-8aef-0f3c5db6a81f | -13.2963 | -54.4275 | 2026-07-08 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 09076be0-e654-3471-8f13-ba0f2fcc061f | -6.4973 | -42.2142 | 2026-07-08 15:10:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| dc89a4a1-6573-301e-b784-6d7366cc2d4b | -13.2774 | -54.4088 | 2026-07-08 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 234.4 |
| 4782f295-7d04-31cf-abf5-806c2f96ffe4 | -13.9594 | -45.2018 | 2026-07-08 15:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 1f11d64e-4ebc-30fb-9c62-0594fb06a037 | -13.3543 | -54.38 | 2026-07-08 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 251.0 |
| a12cd595-9d90-359f-9379-881c1146db38 | -13.3355 | -54.3614 | 2026-07-08 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 135.1 |
| e06b2de4-b36a-376f-97eb-0f02425af1db | -13.2631 | -45.1808 | 2026-07-08 15:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f528d85b-ff7e-3e0c-8244-2a8635facd82 | -6.4973 | -42.2142 | 2026-07-08 15:20:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 8c34eccb-06fd-3eeb-9216-f70e88d834e0 | -13.2774 | -54.4088 | 2026-07-08 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 44fc613d-fb66-3669-9978-5ffde411f6cb | -6.9514 | -43.7015 | 2026-07-08 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 10dbe8a5-5243-3b6e-af31-c52eef4a8fa4 | -13.3543 | -54.38 | 2026-07-08 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 363.5 |
| 434f6ded-8f75-3607-a7fc-71ca65083ad2 | -13.3352 | -54.382 | 2026-07-08 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 155.9 |
| 18c033a4-fda3-3a12-9c9d-0b8da2d65116 | -10.4207 | -46.8827 | 2026-07-08 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 94f93237-7d37-3a80-803b-cc90a70df8be | -13.2772 | -54.4295 | 2026-07-08 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| e2df447d-acaf-38ac-8fc8-e15116ecd6f2 | -5.9177 | -43.8584 | 2026-07-08 15:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| da63ef91-e823-3a49-9a12-140b86c874ad | -13.2824 | -45.1776 | 2026-07-08 15:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 192.5 |
| df3f8209-45b9-3fc3-a902-53259d304203 | -8.1154 | -47.1058 | 2026-07-08 15:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 434640f9-cc22-3654-8d57-8d299199ae49 | -13.2963 | -54.4275 | 2026-07-08 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 18938dec-5305-34fe-9b58-57332aa26bd0 | -14.1445 | -52.8715 | 2026-07-08 15:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 473fd879-e841-357a-8fd8-c502c97da9f0 | -10.4397 | -46.8804 | 2026-07-08 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 8b13d262-a17a-3831-a8ae-4497dbd27236 | -14.1638 | -52.8691 | 2026-07-08 15:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 428a241d-e28f-3dac-89f5-677fa861b0d9 | -13.282 | -45.2009 | 2026-07-08 15:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 36001ff5-8680-36f7-a6df-612bb6a5d352 | -13.9594 | -45.2018 | 2026-07-08 15:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 441155b2-b6bb-3c77-bfab-dd251d3ade2c | -13.2966 | -54.4068 | 2026-07-08 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 185.2 |
| 8847a12d-993e-39ef-ad1f-fce20a611984 | -5.9177 | -43.8584 | 2026-07-08 15:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 790b0e44-0d97-352a-9bc5-b637bfeedd98 | -13.3352 | -54.382 | 2026-07-08 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 153.4 |
| b9e0581e-7012-36df-9f8c-5ce466c5d6b8 | -13.2966 | -54.4068 | 2026-07-08 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 210.1 |
| 89c1bcd8-1fcb-3d4c-849f-13b0b3c722bd | -13.2963 | -54.4275 | 2026-07-08 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 516b7c17-08b9-3308-b28c-ba29591b2449 | -13.2824 | -45.1776 | 2026-07-08 15:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 59d5e658-6d1d-3c76-aedc-e182bf7032e3 | -8.2442 | -47.3368 | 2026-07-08 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 80b33a0e-e7de-3177-84e9-093c266ce6a7 | -14.1445 | -52.8715 | 2026-07-08 15:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| a52df1d6-37cc-3438-8182-ec8c19899cd7 | -13.282 | -45.2009 | 2026-07-08 15:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 506bfd41-d2f1-3175-8571-f8fd063664a8 | -13.3355 | -54.3614 | 2026-07-08 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 39d79e20-41c7-3689-8e8c-d1f33566df04 | -13.3543 | -54.38 | 2026-07-08 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 310.9 |
| a1df7632-c65e-3e5a-a97c-0cc345be5779 | -14.1638 | -52.8691 | 2026-07-08 15:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| dcfa98b4-36a7-309c-911e-85873149926d | -8.1154 | -47.1058 | 2026-07-08 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| a6b06ff4-0aaf-3752-a9ae-14baa97cac03 | -10.4397 | -46.8804 | 2026-07-08 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| c2e4c491-75ce-3967-9b44-55706362abe6 | -6.4973 | -42.2142 | 2026-07-08 15:30:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| 6b835df5-ccc2-332f-9d51-084535f2aae1 | -13.2772 | -54.4295 | 2026-07-08 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| bea8b7bf-e536-3af3-aa5c-175295288437 | -13.2774 | -54.4088 | 2026-07-08 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 178.7 |
| bc021b09-1f2d-3d04-a27a-2ddd78958d09 | -14.6014 | -52.0719 | 2026-07-08 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 0dbef528-372c-39ba-88de-33f6de38fc81 | -13.282 | -45.2009 | 2026-07-08 15:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ce2271b0-545e-3a10-a878-d0049d493ad6 | -6.4973 | -42.2142 | 2026-07-08 15:40:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 008b311a-218e-345c-b75b-c999fd26dd64 | -13.3352 | -54.382 | 2026-07-08 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 244.2 |
| 9f942901-0aa0-37bc-a8eb-35f1666e829f | -13.3543 | -54.38 | 2026-07-08 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 251.1 |
| 0c389ada-b31e-328d-86c9-d3775a6ffad0 | -5.5907 | -42.7164 | 2026-07-08 15:40:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 8b148747-c4e4-39ad-96af-343c5103bcf7 | -13.2772 | -54.4295 | 2026-07-08 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| a0b5e2b6-69dd-35d3-bb3a-915dcfc478d2 | -6.9326 | -43.7032 | 2026-07-08 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| f3e63fc3-c27a-3c8f-93c7-b3227bd18707 | -15.5886 | -48.231 | 2026-07-08 15:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 266e64e4-3d04-3148-9d23-806486e47eda | -14.1445 | -52.8715 | 2026-07-08 15:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| fcfd645a-b9a0-3d24-b7b8-7e9a9775bb76 | -13.2824 | -45.1776 | 2026-07-08 15:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 164.1 |


[Clique aqui para ver as próximas entradas](README26.md)
