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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a33cced1-bc8e-3904-a737-bdda72b79f21 | -4.2299 | -50.8983 | 2024-11-27 07:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 209.3 |
| 1dde0f42-155f-3dea-9f9c-0ebc36ce99fa | -3.6973 | -50.2277 | 2024-11-27 07:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| cde0c687-6223-3669-af0f-30006bba2bef | -4.2114 | -50.899 | 2024-11-27 07:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 173.3 |
| 9c128490-9ae9-34dd-983b-52624956f124 | -4.23 | -50.8774 | 2024-11-27 07:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 205.9 |
| 8a462c06-5afb-3c70-aef3-b73345779b5a | -2.7798 | -54.0334 | 2024-11-27 07:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 0dfb0f82-ecab-39ca-b33f-a4f077b9d4df | -2.5956 | -54.2181 | 2024-11-27 07:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 3c65cc05-8069-3211-8d96-3b744ae989e7 | -3.5858 | -50.3577 | 2024-11-27 07:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| fa0a345d-3e35-3d79-991a-79d6fd7cb613 | -3.6043 | -50.3571 | 2024-11-27 07:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7296efb0-1526-3127-b241-8e9cb5ddccba | -4.2114 | -50.899 | 2024-11-27 07:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 2f01b00b-ee73-3faa-8435-2ef0519fd784 | -3.1691 | -48.4394 | 2024-11-27 07:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2a3e46aa-9d24-3c5a-bede-5d9f4811eb81 | -3.1133 | -53.2583 | 2024-11-27 07:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3d8e71fe-9695-38d0-ada3-242e931a4288 | -2.8346 | -54.1326 | 2024-11-27 07:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 462bb78f-d5fa-31e3-859f-4d424c43b6ab | -4.2115 | -50.8782 | 2024-11-27 07:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 7986c7f4-bcee-3afb-9dd7-f233e1377ac6 | -3.6973 | -50.2277 | 2024-11-27 07:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 065918f2-7b4b-3760-b401-046aea8326f5 | -3.0949 | -53.2588 | 2024-11-27 07:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 69aa13d8-7f6a-36cf-887e-ea66c19c543a | -2.8347 | -54.1125 | 2024-11-27 07:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 4cc52766-b285-3e79-82dd-c3c4add9d3eb | -3.0949 | -53.2385 | 2024-11-27 07:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 64735899-e976-39cc-a907-1eda9fe794e9 | -4.2299 | -50.8983 | 2024-11-27 07:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 3d9170f3-3c06-3faf-a6a6-3d22eef812ce | -4.23 | -50.8774 | 2024-11-27 07:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 78d5deb0-68e0-3709-86d4-3a3d3c8a93ad | -4.2299 | -50.8983 | 2024-11-27 07:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 178.8 |
| dc8c65b0-df38-3d15-9581-a9dd755429c9 | -3.1691 | -48.4394 | 2024-11-27 07:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a910b69b-0e3f-33a8-ab1f-356a8f29a228 | -4.2115 | -50.8782 | 2024-11-27 07:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 705c2c4a-36e5-3db3-92b1-99d8518950cb | -3.6043 | -50.3571 | 2024-11-27 07:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 10d6a3e0-f597-37f3-aa50-5c149366896b | -3.6973 | -50.2277 | 2024-11-27 07:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| be90dab2-7376-3797-8901-c315a8119b8b | -2.7798 | -54.0334 | 2024-11-27 07:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 8453ec93-8149-3a09-b2af-bb2b6d25b294 | -3.0949 | -53.2588 | 2024-11-27 07:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 6cd765d3-ea24-3424-bfee-cd7850e86cd4 | -2.8347 | -54.1125 | 2024-11-27 07:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 03e7016b-f419-3632-ad21-c97dcb78e33c | -4.2114 | -50.899 | 2024-11-27 07:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 149.1 |
| a3745a39-6b6d-30fd-820f-c84ab0bfc290 | -5.9788 | -45.3621 | 2024-11-27 07:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| c86bc5f6-0afd-3a5d-887b-12a4869495dd | -3.1133 | -53.2583 | 2024-11-27 07:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| fddd8177-848c-3dda-8289-1dbe45bdfee6 | -5.9975 | -45.3607 | 2024-11-27 07:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| a0ecbe51-18c3-3de9-94ef-2d96a85f67a4 | -3.0949 | -53.2385 | 2024-11-27 07:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 046627c2-9920-3c9d-a9a8-0c191a29d1ad | -4.23 | -50.8774 | 2024-11-27 07:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 203.0 |
| a30e8e1e-3fe1-3919-a118-944ddbcb36e7 | -4.2114 | -50.899 | 2024-11-27 07:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| fa06f04d-129a-3e7d-8525-4426069738e8 | -3.9674 | -48.0851 | 2024-11-27 07:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 2fd1b303-3224-33c9-9961-a2173dd31244 | -3.5858 | -50.3577 | 2024-11-27 07:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 281cf6c4-77f2-3777-967f-bcbccfcce3ad | -3.6043 | -50.3571 | 2024-11-27 07:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e0443528-c635-339c-b749-8a0e5052058b | -3.4975 | -53.8137 | 2024-11-27 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| c8b61387-f2ec-3c56-930e-d78dc7720603 | -3.6973 | -50.2277 | 2024-11-27 07:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 32d010fa-fcb3-3b98-aee4-a5536f668fd3 | -4.2115 | -50.8782 | 2024-11-27 07:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 48e0046b-bd97-3f13-852a-ee6fe8aab12e | -2.7798 | -54.0334 | 2024-11-27 07:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| c3845f7e-6eca-351d-9236-734156603191 | -3.1133 | -53.2583 | 2024-11-27 07:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| a69a0738-f951-369d-a139-2d6cf329cd52 | -4.23 | -50.8774 | 2024-11-27 07:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 185.0 |
| a4fb5ba5-2cc6-3f3f-ab36-f5dc8245b52a | -2.8347 | -54.1125 | 2024-11-27 07:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 42ef58f5-aa8e-38f4-93aa-ff40d9ad5ba1 | -3.0949 | -53.2588 | 2024-11-27 07:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| ec4eaf43-0ac1-3f91-b12a-65159f6a92e2 | -2.8346 | -54.1326 | 2024-11-27 07:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| db684154-4c0f-39f4-8bf8-26fc9f8029ee | -4.2299 | -50.8983 | 2024-11-27 07:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 211.4 |
| ce91d215-3f5c-3d0d-868e-08ec52199625 | -4.2114 | -50.899 | 2024-11-27 07:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 189.3 |
| cc314b00-e402-34e9-a244-f2a54159ac92 | -3.6973 | -50.2277 | 2024-11-27 07:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 9aeb3ef4-a6a6-3bec-a03b-a344a8343b2f | -4.2299 | -50.8983 | 2024-11-27 07:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 181.0 |
| 33c7b44e-7cc8-3a27-9a7d-052767287144 | -3.1691 | -48.4394 | 2024-11-27 07:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 502541a6-c3af-3cbd-9b50-fdb2b6b3db36 | -3.0949 | -53.2588 | 2024-11-27 07:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6fdd34c2-3ebf-395f-9e6a-dd0f4bb5ccfc | -2.8347 | -54.1125 | 2024-11-27 07:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| df0d7b4b-ce2e-31e2-b700-b41eb12219fd | -4.2115 | -50.8782 | 2024-11-27 07:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 1f9581d0-1777-3fb0-ab7d-47bc89c5e325 | -3.5858 | -50.3577 | 2024-11-27 07:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| e7ffc288-5f7f-380a-a89a-3e4450c10fa3 | -3.6043 | -50.3571 | 2024-11-27 07:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 93646bdb-177b-3d00-8691-326c9e5272d5 | -3.9674 | -48.0851 | 2024-11-27 07:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 1032cd98-6623-3e6b-90c3-345a3d1814c1 | -4.23 | -50.8774 | 2024-11-27 07:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| a89859e9-d3ec-3670-bfc1-a455ed2fc7e8 | -2.7798 | -54.0334 | 2024-11-27 07:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 35e91ee3-d335-3575-a3e6-eb1ecc2489b8 | -2.7798 | -54.0334 | 2024-11-27 08:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| dc8a4527-03b4-3cef-828f-cbab5998abe6 | -4.23 | -50.8774 | 2024-11-27 08:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 184.5 |
| 02dfd99b-41f9-39da-80d8-8f4959ca7ec8 | -4.2299 | -50.8983 | 2024-11-27 08:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 184.2 |
| ac519eba-d122-3ac8-a54d-2e77dfc89e7d | -3.0949 | -53.2588 | 2024-11-27 08:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9e3f0e82-dbe2-323e-a4ae-7de508849972 | -3.9674 | -48.0851 | 2024-11-27 08:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 1836af1b-0649-391c-a7fe-bfc28d9f0a93 | -3.5858 | -50.3577 | 2024-11-27 08:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 1a1d4bf2-7165-3028-8383-73d6aff000c1 | -4.2114 | -50.899 | 2024-11-27 08:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 381a52eb-61c5-372e-aad4-df198bf421c7 | -3.6043 | -50.3571 | 2024-11-27 08:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 1dbd5757-149f-345f-b918-30a305e2dfe4 | -4.2115 | -50.8782 | 2024-11-27 08:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 0289506e-70e8-3d52-830c-dbfbba9de80e | -3.6973 | -50.2277 | 2024-11-27 08:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4b240b10-9702-3f8a-9d03-4b9caf742ec2 | -3.1133 | -53.2583 | 2024-11-27 08:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 4bd3e62a-fb6b-3f39-a620-86ad79a88dca | -4.23 | -50.91 | 2024-11-27 08:00:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79134d52-86cf-3eff-bc23-ba8ef3e942f7 | -2.8347 | -54.1125 | 2024-11-27 08:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| ad310a66-7385-374c-afa3-3ce6505a7891 | -3.0949 | -53.2588 | 2024-11-27 08:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9ed1cddb-d236-38df-8fc7-130854287a58 | -3.6043 | -50.3571 | 2024-11-27 08:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 84e0baad-81b5-3a28-998c-99efb77687f7 | -3.1133 | -53.2583 | 2024-11-27 08:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 9d970091-8952-3a93-9fbf-91d92bf48a3a | -2.7798 | -54.0334 | 2024-11-27 08:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 0b619e32-5d5a-300e-86c6-5faddb8a8db1 | -3.6973 | -50.2277 | 2024-11-27 08:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5c943fed-9157-38fb-99d7-045cceb951be | -3.0949 | -53.2588 | 2024-11-27 08:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d5bdcf2d-e327-36e7-a8ee-e2697c4c6626 | -2.8347 | -54.1125 | 2024-11-27 08:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 2fcf15d9-d3aa-3a48-aa69-b36086e3da5a | -2.7798 | -54.0334 | 2024-11-27 08:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 08c5d399-07cb-39db-b8eb-aba505960839 | -3.1133 | -53.2583 | 2024-11-27 08:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| dc797fb9-c516-3272-a572-16b007113644 | -2.7798 | -54.0334 | 2024-11-27 08:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8a1d59cf-7baa-3e7b-93b2-3ef6141278dd | -2.8347 | -54.1125 | 2024-11-27 08:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 9f60eef1-332f-3b5e-9982-71ce09f76a5c | -3.9078 | -42.4256 | 2024-11-27 08:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| dc06dbde-e50f-3ba2-a265-6d72f465fde1 | -3.0949 | -53.2588 | 2024-11-27 08:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 0506a57d-9e95-3f77-bdee-5e5c358c513d | -3.908 | -42.402 | 2024-11-27 08:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 1f75fd4e-6ce2-3cee-8b96-e03de14ca671 | -3.9078 | -42.4256 | 2024-11-27 08:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 156.9 |
| ce2facda-42af-38a1-8fd5-da91e25bf32a | -3.908 | -42.402 | 2024-11-27 08:50:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| 0cc4a337-a4b2-30a5-a0b0-6ac9a710fda2 | -3.9078 | -42.4256 | 2024-11-27 08:50:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 154.1 |
| 83da4cf9-1e67-3cb1-a326-525a61e426d5 | -3.9078 | -42.4256 | 2024-11-27 09:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 124.5 |
| 21bb7cec-839a-3a7c-932c-19b0275c51e7 | -3.9265 | -42.4246 | 2024-11-27 09:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| fc7662c9-add1-32fe-a47f-a5c876eb04c6 | -3.9078 | -42.4256 | 2024-11-27 09:10:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| ee586f1d-3584-3d60-8b7d-53c220f083e7 | -3.9078 | -42.4256 | 2024-11-27 09:20:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 129be6c3-1dd7-3181-9616-5758cc111600 | -3.9078 | -42.4256 | 2024-11-27 09:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| 844de455-be6a-38e6-b2d9-48cd92898961 | -3.9265 | -42.4246 | 2024-11-27 09:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 7bb23cec-4d91-3c60-9bdd-0bf417649126 | -3.9078 | -42.4256 | 2024-11-27 09:50:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 72ff3179-bb46-32da-90c3-7eded7c05042 | -3.9078 | -42.4256 | 2024-11-27 10:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| cfa13595-9360-3610-9390-3a60676d821e | -17.4 | -44.88 | 2024-11-27 10:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cd05ba23-a1b9-39ef-a6c8-089c0a1cf544 | -3.9078 | -42.4256 | 2024-11-27 10:20:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 7b8b8826-b034-3d04-bd7b-dde9713cd814 | -3.9674 | -48.0851 | 2024-11-27 11:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |


[Clique aqui para ver as próximas entradas](README83.md)
