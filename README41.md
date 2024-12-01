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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60630e27-f87e-39fe-994b-28dcf72b79b2 | -2.12278 | -50.34306 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cb43af9-ee4c-31df-8011-f8447732a02d | -3.38447 | -50.113 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff3dca80-5893-36ce-a3fb-05bc533dc234 | -3.24803 | -53.92261 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 98e424b9-8bc2-35fd-a822-884637b61c7b | -1.71764 | -52.62438 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4a0984b-e981-3364-9cc5-2ecb588b2ba9 | -1.14046 | -53.6718 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a991712-d1b1-3582-ade7-ebbefd3c9dd8 | -1.07718 | -53.39487 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0c0bab6-537c-3232-8065-4a05f2f860ed | -4.01051 | -49.95903 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 832bd951-dac5-3b83-9305-3b531dbdeee5 | -2.59069 | -53.97137 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21a66d48-2659-33ff-8e55-c1d8822340cf | -3.49412 | -53.79821 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d11477b4-b0a9-3d60-8066-0466af489ffc | -3.39219 | -50.30152 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e600763e-6702-3806-a2de-a3a3a4e4f165 | -2.53142 | -54.07736 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3321ca7e-24f5-3d2e-80af-11445586c83c | -2.88345 | -50.73855 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a00bab10-ddb7-311d-ab48-d657e5b90441 | -3.41114 | -51.97598 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f210eb07-08f9-3095-a795-c22a0ffb558d | -1.71765 | -52.77541 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b58d950-23a5-3e2a-8287-fd28e34ed95c | -3.99171 | -49.97031 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b5aaa06-f71e-3256-8f3c-c80594e35ec5 | -3.99199 | -46.65492 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0eb72272-f790-3d58-8294-325314393cc1 | -3.25678 | -53.86937 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec81ae45-5764-3df4-804d-51992a56c06a | -1.27996 | -47.90351 | 2024-12-01 04:44:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 81b8eca4-8819-3376-bac6-ce72f4ba1cfe | -3.77553 | -51.61883 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90649171-879a-3305-bcb8-9081e5c11974 | -3.3323 | -50.05536 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bab7daf5-a61d-323a-9983-98a6d0999f10 | -2.47983 | -54.01394 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b427074-2687-3368-94af-48d7ad076dc3 | -4.50038 | -49.6385 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e9a31b6-5be1-396b-9896-0d9088f66564 | -0.98457 | -51.75518 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3b6b284-275c-3af5-a5d2-09e79c3993f6 | -1.90988 | -52.8709 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c329f8d8-a4e5-3e61-910b-9e761629f644 | -2.96111 | -53.72634 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df365b20-93f7-3659-ab01-920fdc8f53a5 | -3.72943 | -49.94036 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92d26e1e-21d5-3ef9-9d7b-b343888b4c59 | -3.39334 | -50.31583 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 025430bc-5db8-39bf-ae92-a268b105eb8d | -1.62197 | -52.69928 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c5b0b89-4083-395f-853f-74602f61c6ab | -1.73039 | -52.49695 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de79ec09-ea30-3e97-a078-4883927e4165 | -1.60795 | -46.23176 | 2024-12-01 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01f88229-d724-39a1-8ca2-3f1938ce8db0 | -3.60419 | -49.98485 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c4a67ff-d504-3371-8e3d-d33a79b72412 | -2.86769 | -54.00186 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 595320f5-41df-3b3b-8b99-95e39edbe8d5 | -1.48004 | -55.19825 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d1d618c-43a2-3211-a393-280f9d025ef9 | -4.26432 | -50.84177 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c891e3c4-b219-3689-bb8e-3c675d42b8da | -2.47561 | -50.40509 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acaa4903-d095-3978-a84e-f1f9af033024 | -2.31767 | -50.65343 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a06cad8-6cbc-329f-ba57-e6951de503c4 | -3.26807 | -50.09835 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d475d57-bdb2-368b-9899-9ff743427b0a | -4.69649 | -46.80934 | 2024-12-01 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a4acabd-1331-3e83-9e27-4031fd529e94 | -3.12635 | -53.27084 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27c07e36-70c5-333b-8471-d1bdde2c3807 | -2.94848 | -49.44129 | 2024-12-01 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bb8d559-9b57-32ea-b02c-e69c4b47bec0 | -3.29586 | -53.83968 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8077a50-3276-3d8d-9b21-e2b3c5de0fc8 | -3.18403 | -45.35342 | 2024-12-01 04:44:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a8ad7f20-f950-3804-b2ac-03ffe18c6955 | -1.74511 | -52.31203 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96fee90a-e20f-324f-b907-5979931bf073 | -3.05579 | -51.06217 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0db48745-cc7a-30d3-ad0e-6a95c4c43a40 | -2.83693 | -46.86001 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 051bcccd-9e57-35d1-9bd2-ba7a9a7a88ca | -3.25342 | -53.93038 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e65f16bf-b79d-3f28-9e27-8b1f2231f21d | -1.46433 | -54.36733 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7ef759c2-73a1-3f57-b350-a6e9d5cd068e | -1.5224 | -45.91204 | 2024-12-01 04:44:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17421411-d661-399c-bd45-548ea83d4c59 | -3.48467 | -53.81014 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f6a4231-da16-3861-a054-4ad9fd10a36f | -0.76256 | -52.45823 | 2024-12-01 04:44:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9306a3f5-a774-3f3b-8907-bf77eceb983a | -1.09505 | -53.40219 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ca94c6c-22a2-3d05-bc8b-1fa5c34a8c4c | -2.88355 | -54.21365 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 410d52e8-5077-3acd-af84-78132ac15ca8 | 1.07602 | -60.3211 | 2024-12-01 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8443357f-bdde-32cd-afcc-1081c05f1000 | -3.69535 | -51.81192 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0113f903-644c-3614-a90d-f90361fac58e | -2.8792 | -46.79921 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28de5de7-79ac-37ee-8888-cdd34c1e8bea | -1.00645 | -51.72805 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81944364-ac1e-318b-bf4b-9f36c6cea569 | -3.06429 | -53.81625 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19b3f3c7-8d6d-328a-861f-4fbc71506edc | -2.86712 | -54.02953 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d7f808d-d5e3-3429-86c9-1d1fc653e2f3 | -3.09459 | -53.26161 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ffd8a6e0-032e-3ecd-9db5-342b137df19f | -4.47534 | -50.76899 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd9506bc-92d0-313b-a1f6-5774e6f38940 | -3.10702 | -53.18389 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3cd3e71-5097-3373-ad50-776e05bfd656 | -3.14815 | -45.37289 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bbf5094d-f229-3388-ab49-2a40cf329d00 | -2.33389 | -51.30308 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5cb5697-d08a-347a-a297-e71d5d4a3d38 | -1.25135 | -54.54977 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4a8c867-07f2-3790-8a4e-f4037ac0e230 | -2.99059 | -53.88729 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 540bfaff-cb29-38f4-8458-43c682bf1546 | -3.66447 | -51.72237 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 677054c8-76e9-3c92-8fdd-533a4bda929e | -2.1426 | -54.87502 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 338f29cc-f461-3a58-a65b-52ce0bfdf5ec | -3.56033 | -50.307 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 491aa979-6579-33cf-8c73-817db43fb496 | -2.63002 | -51.75027 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98f6b171-684e-3ac3-8326-f3359cd89eba | -2.09866 | -50.73344 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb0962ad-b75b-3f86-a9e5-baf1ddbc602f | -1.44848 | -47.11197 | 2024-12-01 04:44:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14f1feed-1098-3e2d-bf8a-305755871e5b | -1.70529 | -52.47292 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82ee71c0-80b6-3e5c-87a0-164edf8752a5 | -2.83575 | -52.91652 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acb5dbab-5555-3f3b-aaec-058fc7321444 | -0.59209 | -51.69106 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0be09875-f15e-356a-805d-6d3e4a9bb572 | -2.41988 | -50.47781 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85417a7a-0e0a-33f7-911a-0db9cbf10589 | -2.87073 | -54.00695 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9cffd1c5-b1b9-38be-8b70-3d0b36ffc9f2 | -3.29614 | -50.24408 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c6d3ef0-2f68-3e49-866a-ff60c9b96080 | -2.79528 | -51.89555 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25f04d32-6a45-3ecb-a90e-bfdae212d1cd | -2.28892 | -45.60691 | 2024-12-01 04:44:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 097d0f5d-577f-3405-b488-13ddf095841b | -3.14009 | -53.84182 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acbd8652-1371-3fff-9ef7-7d76e8f74f90 | -1.32604 | -51.66995 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b964cb06-2735-3222-8baf-5aa6abf367f9 | -1.20609 | -53.87074 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bba28276-83bf-39cc-80cb-4b0b28002484 | -4.06897 | -46.68375 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0a7da1a-577e-3cae-a379-34e08f18d2fb | -2.12283 | -50.60187 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81dcecec-b172-329d-9e35-ab9393b32dc5 | -2.07201 | -50.75069 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c845442d-bbc6-3f69-bbac-06a400adb2f7 | -3.28054 | -50.53507 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 211f2aad-49f7-36ad-8b49-8187e4a8ff9d | -2.60374 | -54.08133 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 596a5a52-3cb0-3b17-bc27-3e5037b014fa | -3.49877 | -53.82893 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be4ccdce-56fd-32ff-a830-4d137a39a76c | -5.62968 | -45.95724 | 2024-12-01 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd0d5b7e-5c82-3f2b-88a0-353a8b231da5 | -0.82245 | -51.60408 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61405551-abb8-30e3-acf0-b2f2b8e4d460 | -2.12281 | -46.41843 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 867f6499-95c1-3060-8740-3770ba554011 | -2.60451 | -46.57695 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c28472f-7785-389f-87ab-5abf24181ece | -3.7915 | -51.2595 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68591b01-364a-3869-80ea-d12628421df1 | -2.59673 | -53.98161 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2560b91-bb8e-32ae-80a5-ebcf69bc2c9c | -4.55899 | -45.72182 | 2024-12-01 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 845513cd-ab19-31b0-b800-6880fdd2f108 | -3.48723 | -50.31973 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0936244b-4eaa-34ce-b45b-50e812721ed3 | -2.9815 | -53.29084 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8fea5c1-3acf-3fec-9dbc-e3a7aed63ee9 | -3.31063 | -50.08731 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4d23dcc-24a7-3a82-afd8-60fe61d3db26 | -3.19391 | -46.57645 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee934b32-0e00-3437-9b2e-2fa8317e3400 | -1.5491 | -47.15869 | 2024-12-01 04:44:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README42.md)
