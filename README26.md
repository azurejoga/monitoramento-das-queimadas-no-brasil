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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02790d3b-231f-3501-8851-a832bef4c3b6 | -1.61412 | -52.58773 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01fa38d0-b719-349d-bea0-63f9b7c11b27 | -2.68457 | -46.17039 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 563b0a74-59e4-35a1-9d22-e8073ab4c402 | -2.52762 | -46.39451 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3eff981-505a-3c95-9cc9-ae18a8c92f1e | -3.8552 | -52.35018 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef42126f-9667-3e32-a145-09f0d7bc41f2 | -3.62327 | -45.76971 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1773a6fc-bbd2-3767-a54b-74905296b4a2 | -4.15951 | -42.01881 | 2024-11-22 04:12:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67e42724-3631-34e0-9ef6-f28c0ddd77a0 | -0.9539 | -51.72086 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e2a544a-c39f-36f4-8da0-c8d254b62a30 | -2.20109 | -53.65648 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f8a9d39-5cfc-3475-8056-b605cb27e0da | -4.43969 | -45.84509 | 2024-11-22 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51942000-e08b-3f12-9c2c-a0d3b98dc61e | -4.73596 | -46.67026 | 2024-11-22 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6464336f-ec56-315d-a34d-608113198376 | -5.95715 | -48.05187 | 2024-11-22 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d1f1b22-ea68-324f-b3f2-a18df4562c0d | -4.22937 | -48.6354 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0f2cfbd2-a6f6-377f-a90d-b4ce586ae8a3 | -3.19532 | -54.33236 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66cd3dec-3468-3e34-8fff-8c9ef8e79bce | -4.37737 | -46.2827 | 2024-11-22 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b2f4fdf-e3e5-3f14-a83d-f6574ecf1825 | -1.05113 | -51.74288 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bd9ff3f-6295-3511-9677-8b81a8ebdff6 | -4.1369 | -54.65613 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 361cb0d5-5cd3-3550-873a-46122ef79660 | -2.55805 | -47.32709 | 2024-11-22 04:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cacb1f7-4ae2-388d-b2ad-692ba18b4cd4 | -5.0957 | -45.73197 | 2024-11-22 04:12:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6aa46bd5-d483-34db-95f5-c84e6975e37d | -2.70116 | -46.09259 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51625efe-78d4-3d82-904b-24e004a22412 | -1.72554 | -52.71208 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a0fe19bb-ffdd-37c8-89b4-b00dd1a74e8d | -2.52656 | -46.39661 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15499166-7bc3-3198-8d00-4c99ddf35602 | -2.79013 | -48.09988 | 2024-11-22 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a2d507d-f6ee-3014-a323-219b3b958841 | -3.80837 | -51.99492 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2af52034-75ee-3986-ae44-9cdcd3200e3b | -0.81122 | -51.79 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e22a332d-6988-3b4b-96d6-550590b193ab | -2.6114 | -46.19432 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 420a286d-f0a5-3e3a-a338-aec7d4bb008e | -3.28964 | -53.85786 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 286bc287-e5f1-37dd-b4f4-d3b562001581 | -4.11722 | -51.05837 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39f87e27-1777-33e8-9762-63aa7b8ab2d5 | -1.64495 | -52.62415 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1dea60c-896a-3e1f-87c0-c94d47436c63 | -6.56024 | -41.35534 | 2024-11-22 04:12:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d4ed0c7-08b0-3a3a-b165-b20f4eb4b90d | -1.28954 | -52.46701 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de6a5d91-69e0-38a7-b04f-6ba5299c376a | -1.26221 | -53.36965 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4a8d199-b9fa-35a7-b95f-d2cc3b780a7c | -2.69587 | -46.07984 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7af24f0-31ac-3eca-b8a8-a1400870ab70 | -2.44346 | -46.54277 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70d59693-7f82-371f-aca3-35eac88eb5e7 | -2.92746 | -48.05428 | 2024-11-22 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cdf358b-6492-350e-b4c6-a36dc8f75afd | -2.50868 | -54.15276 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 81d7027f-bbf0-369f-8f8f-09cf491fb018 | -1.51695 | -47.06178 | 2024-11-22 04:12:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4cf3fd6d-db19-3ab1-95a4-553894e7faf3 | -6.62267 | -42.38612 | 2024-11-22 04:12:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 30f8c4af-3b4e-3100-aae7-1f91f90fc028 | -3.17859 | -54.31355 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c113949-f554-3d69-a5fc-cececa0d8573 | -3.66037 | -51.57076 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7df8b3e6-ba8a-3c41-aadf-6efb0f1ded1c | -4.81416 | -49.72247 | 2024-11-22 04:12:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bba2ff7f-38f8-3812-939f-775fb6594dff | -1.6521 | -45.45647 | 2024-11-22 04:12:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bfe8ced-d793-3ac9-b68d-059f141dcf85 | -1.74623 | -52.39485 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 39c26d2a-9610-33e5-9092-36c4211ce157 | -3.23947 | -54.22936 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5f090e14-441d-3b1a-afb1-959719d19e1a | -3.28191 | -43.1164 | 2024-11-22 04:12:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d02a1fe-2be2-3f4b-9823-1d49c43210e8 | -3.64547 | -41.91054 | 2024-11-22 04:12:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6fa1e668-ef41-3d30-801f-081127dc5bfc | -2.56619 | -46.54984 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84580156-b62c-33bd-bc57-4190b25d17d4 | -1.13926 | -51.68194 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c1b0822-0818-3288-a475-f75aad85dbaa | -1.24435 | -51.75016 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8cb5fde-6ac2-3013-a1e7-e2fa4e94fd44 | -6.81997 | -46.77869 | 2024-11-22 04:12:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94603f4d-ece9-3611-84f7-0bb5f2d42d3a | -3.65457 | -42.2586 | 2024-11-22 04:12:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 38833e9e-8951-3d9b-9a58-8b390e162de6 | -1.96232 | -52.99109 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f31b9aec-70ad-3f76-a3b2-faa32f265949 | -4.70711 | -44.25403 | 2024-11-22 04:12:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67410fe7-3c1a-3a78-8ff0-7847fcd928a7 | -3.17782 | -54.32174 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0efdad3f-1462-3511-b34f-6cf1e4929a3d | -3.27962 | -53.84093 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b88e3c8e-c0e4-3a3b-9070-6bbd1f027793 | -3.18882 | -54.33146 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ed414865-16df-331f-8550-5e3fa572d0fc | -2.69759 | -46.23467 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc1cc55c-2339-3be2-bbab-ee4b7c22c12c | -2.30501 | -53.59716 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 432b636c-628c-34d1-aad8-75fc84ed0648 | -2.56712 | -46.15383 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41236a44-46e4-359e-bbd9-be4365fafc95 | -1.52047 | -47.06612 | 2024-11-22 04:12:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ea9ee10-01ef-362c-bc3b-860f9c2cc8dd | -3.28505 | -53.84693 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b44dead0-2f9f-38f3-9ae5-5c17b0596c6b | -1.58927 | -53.81087 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 1bf53ef7-43fc-34ac-9544-7dc2599d14bc | -3.08465 | -45.77579 | 2024-11-22 04:12:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b4fdd51-bd68-38eb-9ea0-893a14e96aac | -4.94707 | -47.80336 | 2024-11-22 04:12:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a588a1c9-d391-377e-b19b-db1347ba2d30 | -2.68213 | -46.16751 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e42c070-8cbf-3c9a-b5d4-7814d4b97945 | -4.28734 | -48.24435 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38b45104-9960-3625-8ec7-89875aeb29f8 | -0.92587 | -51.73698 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cf73109-e732-3395-b885-69575e47138b | -4.22977 | -40.38539 | 2024-11-22 04:12:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bed92f61-0661-3521-ab78-d82fae030de2 | -4.95176 | -47.80037 | 2024-11-22 04:12:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed14203d-309b-3f47-8867-ac6034b9c628 | -2.30415 | -53.60216 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfcaa076-17d7-3e4a-ba29-fcce3d096bff | -3.97158 | -43.72086 | 2024-11-22 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38a86792-a449-3db8-b70a-70d9a9550d36 | -2.69371 | -46.09364 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8cf3644-a730-37c5-a9de-b975ad2efdd6 | -2.28313 | -47.91587 | 2024-11-22 04:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f72fdb96-4090-3c5b-b694-a62ba059cde4 | -2.68003 | -46.24622 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2eefe2f-260c-31ca-a1e2-20d4e310b2ad | -5.83431 | -44.01677 | 2024-11-22 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e460176e-021f-33af-affb-f837ccaade2d | -4.35898 | -48.61189 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 71f5355a-925b-321b-820e-26172456ed0f | -4.54424 | -49.54838 | 2024-11-22 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c54d866c-07d6-38f7-94ff-7962c2018c24 | -2.95215 | -53.71543 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6c5e9d1-a864-3928-8ad5-d2d9f0cbff1c | -2.8405 | -46.68584 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 933cbd8c-df7e-3513-854d-f2e8bd44c26d | -4.14124 | -54.66354 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b2bca8f-d76f-3d6c-9c12-06ecb0068368 | -3.83014 | -52.25973 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 56d11055-b30a-36fb-a431-08a450500dff | -2.69508 | -46.08223 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa90be63-705a-3b2b-a177-211ccc29aa26 | -6.84092 | -44.38924 | 2024-11-22 04:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 600a5f97-9057-310d-adf6-5502537bfd9d | -1.63764 | -52.61232 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f5a8509-58a6-34bd-a2ea-3a81ed631d76 | -1.74375 | -52.37305 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36710ecd-ac7e-336b-a415-f4f9d249aba6 | -6.19961 | -37.43534 | 2024-11-22 04:12:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b90b285f-0659-373e-80f1-1d81094fb714 | -4.29216 | -48.23602 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15657291-7099-35ac-a3d5-47d9a5bf1d32 | -0.94822 | -51.7199 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81659c08-a061-3602-821e-af2f25af9ecb | -3.10799 | -53.99503 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f1d5ab9-a6d4-3092-8c7c-38b62a2caa26 | -1.09307 | -53.16758 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8716427-edde-3a7b-8074-3a5ca0a89ba1 | -1.39195 | -52.34299 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 327f2f32-789f-3414-bbf2-16f2e122107d | -2.72611 | -46.08251 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f2cb4ab-f218-3b4d-8eee-e9f245d35273 | -2.68153 | -46.1651 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa3a96d0-3475-3caf-8816-52d24b459fe0 | -5.244 | -42.63217 | 2024-11-22 04:12:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c27890eb-0974-363c-89c8-afe6db82bb40 | -3.06256 | -45.68967 | 2024-11-22 04:12:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11f4bb2d-f14a-3105-a744-b9dc9fdcf42d | -4.23375 | -48.63603 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1b776825-57c9-3dcc-be91-57646221eb0f | -3.51204 | -53.803 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dbecc3a-4856-334c-94a2-97e426f07f25 | -2.56451 | -46.15535 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7be18c5b-8a1d-340c-a64b-3f569176edbc | -3.33413 | -53.33957 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 285990b8-7e16-38a2-9f1e-08bda4088039 | -1.01485 | -48.07264 | 2024-11-22 04:12:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea719a10-7eab-3478-88f8-e31b4e6ecf00 | -2.63367 | -46.22659 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README27.md)
