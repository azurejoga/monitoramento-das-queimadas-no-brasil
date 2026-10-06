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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff2f2ae7-a41a-3ce1-a09a-074472041e6c | -2.91956 | -54.12409 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76929510-61f8-37b3-b472-d6fe428f26b6 | -7.45533 | -46.83427 | 2026-10-06 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7897575b-328d-3460-bc36-f1022ec6ce98 | -2.80017 | -54.14452 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ae1175c-13a1-392e-82b9-ee37cf395b26 | -5.43791 | -43.44818 | 2026-10-06 04:19:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2f14e582-af9b-3eb8-90e0-db16dcc42b9b | -4.23205 | -49.97986 | 2026-10-06 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 057c11fc-a1c8-33fc-8b94-d29e3666b767 | -11.27001 | -45.49667 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 67f75958-c7b0-3a16-8052-c82125f5ea9f | -3.07252 | -54.27452 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0be9ec8a-1321-33a1-9ef5-a5bc173bddc3 | -3.16289 | -50.4371 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd7380ea-22ae-3ba8-8ca2-50fd169aeeab | -4.35682 | -47.77519 | 2026-10-06 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 288373ce-5706-3303-8adf-6553ebf23577 | -5.67391 | -42.587 | 2026-10-06 04:19:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2368abbe-2eee-30a6-b76a-2afda2137c04 | -3.27316 | -54.19003 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9cafebe6-fb4e-3d5b-b187-9cc9abb7f2f8 | -11.26588 | -45.5215 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 424d9b4a-8113-3256-a2d8-7ea1d4af714c | -7.02682 | -43.4242 | 2026-10-06 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9d616e5d-ca40-361c-a3d5-10ac0b539835 | -9.80544 | -44.79197 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97ff4fd2-c7b7-3242-bfb2-bfdbc22fc2bf | -3.06419 | -54.17645 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb2200c3-caf4-3348-bc38-7c3e5ddbd6b7 | -11.27452 | -45.52143 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| a5cd3ec5-499e-3566-aecd-a6240140e1a0 | -6.35163 | -42.54798 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3e99a64d-0350-372c-a10e-9e3312a241f4 | -9.8612 | -44.80543 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab3fd2df-e65d-385d-9f1d-082e85a1f58b | -11.28296 | -45.50746 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 40baac6e-1d78-3b8e-b0ce-367e945efa68 | -7.82785 | -45.29796 | 2026-10-06 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1553e4a-4bd9-3e2d-9d2b-27c30a116a72 | -8.32241 | -45.46318 | 2026-10-06 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98276432-5db0-3b76-9058-b609bda517b4 | -3.0737 | -54.24758 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 99fe8992-2a73-3461-b0ab-927acbaf279f | -7.337 | -44.37795 | 2026-10-06 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fd48c32-345a-3a5e-b6e8-da0e48e07674 | -11.28364 | -45.50336 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 19bf8e98-b7c4-3ca9-8eef-5aa6f07897af | -3.32892 | -53.3914 | 2026-10-06 04:19:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 894209dc-e3e8-3df9-8313-21a8d15c3fd9 | -7.47261 | -42.80416 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d4a00ac8-5dba-3579-8a52-32a1819584f9 | -5.95131 | -41.37529 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 141685f7-cdf4-3973-bd19-96f607e7a351 | -3.10603 | -53.77043 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2f36124f-277a-389f-a3eb-7fb47f254b3d | -3.06322 | -54.24506 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c2dcf8b-b1ff-3114-9411-d4011548ea6f | -9.80259 | -44.78737 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd04f414-72c6-3eb1-ac3d-3ab53e4697d0 | -6.71474 | -45.97258 | 2026-10-06 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad3f0159-75ca-3d6e-8e03-3a2690eab821 | -7.14902 | -39.53952 | 2026-10-06 04:19:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| da95ed24-a93d-33b5-b1c3-956782799cb2 | -11.29313 | -45.52042 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 0dd6a4f0-8643-36a3-800b-98de258fcd6a | -3.09892 | -53.73031 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 25b62c4f-3b51-3563-bd47-16dd8cff18ee | -2.98577 | -54.12855 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a36dfe58-f4be-3064-95fa-adc0d4e62d41 | -6.89618 | -43.6688 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e9ec0c4-e9f2-3142-86d4-aec87231b173 | -11.28163 | -45.50145 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 722d75f8-b93d-3715-bdb2-f71071fc4589 | -4.25526 | -50.80236 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc27e7a7-5cfc-3926-ae8d-02521e08bb53 | -4.05389 | -54.04714 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce36370a-acd0-3662-92bd-b6cfb81f5510 | -11.27806 | -45.50079 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 95d52bb9-318c-3fdc-a3c5-3bdc28ae5f51 | -2.98815 | -54.12811 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 97eeefb7-8053-3a9c-b7ad-4d8dada506a5 | -5.126 | -43.99659 | 2026-10-06 04:19:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eb105bf-462c-3d1a-8cfe-4f93db64019b | -3.58833 | -54.31248 | 2026-10-06 04:19:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9bdf2bbc-8dfe-3083-b3e5-25b7202d8677 | -2.94145 | -54.14725 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36fc045b-0c7b-3054-824b-0508ec31ae94 | 3.31635 | -51.34093 | 2026-10-06 04:19:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 369a0917-4c1b-3918-9418-fdcc3fe21240 | 2.46203 | -50.84765 | 2026-10-06 04:19:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2122a46b-0d06-3110-bf9c-0b97641bb21e | -11.26657 | -45.51736 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 63a4a553-34b4-353a-bba1-180f42646c70 | -3.73141 | -48.87733 | 2026-10-06 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3ccada2e-2f4b-3a95-a08e-7b2f5929cfbb | -3.28235 | -54.17872 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d85d35d8-fe73-3c34-ad77-8ac360f67382 | -10.96847 | -45.40969 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dad9606d-9de3-3f15-9922-02225bbc766c | -9.87464 | -44.81186 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ca22675-990b-31c3-aea2-a4b679439859 | -6.72189 | -44.27778 | 2026-10-06 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdf6fa59-255b-3940-8487-71a008767d43 | -2.97749 | -54.1344 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 44b41e9e-acdc-302a-92b1-f7f35e9aff2e | -4.79292 | -40.04274 | 2026-10-06 04:19:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e733e36f-5f12-3a85-bdcf-fdb4061948ba | -4.3357 | -50.40266 | 2026-10-06 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 096bd71d-2f50-3d7e-b276-8223620f4e1d | -3.16172 | -50.44405 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e54aff71-f4b4-30f6-9003-234df0f268e0 | -5.94736 | -41.31419 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc230a7e-ee49-373e-81e4-a78ab7690a51 | -5.68552 | -53.49389 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 227da8f1-75b0-33cd-8ed7-53ee55d7ebe0 | -3.17464 | -50.43545 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e079f5b-e641-33d2-a840-5eb050103d6c | -4.4632 | -54.97667 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 01f5e6c2-cfa8-3714-834d-e788e473d492 | -7.38127 | -46.22372 | 2026-10-06 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30adc190-5456-39f3-8c27-46c8fd9eda0e | -2.86871 | -54.14884 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5b3e55b2-f18f-39f0-9958-13c30087efa3 | -11.26367 | -45.51261 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7351fada-e2c9-3c95-b338-d5a563ef2310 | -5.73263 | -41.62479 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d32d3da4-8754-3ce0-af6c-556b5224e302 | -6.60615 | -37.88465 | 2026-10-06 04:19:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f7f40ce6-4abf-30f2-ad97-3b42957068c9 | -3.80467 | -51.03357 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b00668b6-7e39-333d-bdf5-1ac153a6b2be | -3.09453 | -54.16835 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a932c1bd-2f55-352d-9723-8cde0f1969e2 | -7.57239 | -46.63499 | 2026-10-06 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39b65004-7059-39bd-a3e2-7cc58f4f57b9 | -6.42507 | -43.46653 | 2026-10-06 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 097aa876-6da9-3bc9-bbeb-ab8643811ea7 | -6.66907 | -43.82195 | 2026-10-06 04:19:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4a2f380-1bde-37f4-aeab-d9156ecf1e6b | -5.09269 | -42.22425 | 2026-10-06 04:19:00 | NPP-375D | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2ed4a838-caa9-3311-b7ee-84714dfbfb7f | -6.3623 | -42.54604 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 614ae0f7-6f64-33d7-ad5b-5dae23c46c3a | -3.07505 | -54.26029 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 53d7ee5a-d18a-329e-b219-e740e5510196 | -5.67698 | -53.50377 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa3ffb7c-43d7-3707-842d-1d99df9eacf9 | -11.28955 | -45.51979 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 3d3128f0-784e-3cae-8369-89af9993d209 | -3.0797 | -54.27508 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| adf40366-24b4-3410-b4a6-91c1071c68ea | -5.74867 | -46.68051 | 2026-10-06 04:19:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d14381d-d7e8-3079-ac8b-78e707b2157f | -5.58351 | -47.27118 | 2026-10-06 04:19:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ce0bce4-fc55-36b3-a800-3de517abef55 | -4.05282 | -54.05394 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7be4368-3bce-3e83-af07-642485fc0372 | -8.27511 | -47.91577 | 2026-10-06 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43aa981f-17bb-3c1c-b009-d3a8453fe252 | -7.01288 | -43.4449 | 2026-10-06 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4906c5a2-7d15-3610-882f-6859413ff53f | -4.05392 | -54.04789 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3af8b44-3dc6-3ab4-8a25-acc44601118b | -3.72051 | -48.88129 | 2026-10-06 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5137db66-8570-323f-982b-56bb35a43307 | -2.90527 | -54.08046 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b95a8ad4-599f-3659-8f6f-6fbc26f9c99e | -7.33409 | -44.3734 | 2026-10-06 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4681c746-8255-3cb2-9483-e04c676e13ab | -5.84496 | -45.02124 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a4595f82-9869-3c04-8351-d5eb65599bbe | -2.7966 | -54.13995 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8876e498-56b7-3f93-9cd6-fba1889c459e | -4.02395 | -44.82344 | 2026-10-06 04:19:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 219dbc1b-575e-3afc-b7a0-9b2dcdc06890 | -3.16112 | -50.4476 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0929821-b934-3bbd-87b8-1e3f385c1a31 | -3.46108 | -50.10431 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7878f6cc-0504-3852-b4e8-e27f67e33aa8 | -6.90281 | -45.02452 | 2026-10-06 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e11b6ebb-186e-3bc2-8edc-48c52843f70b | -11.28022 | -45.50966 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 0a6ba627-81d4-35da-afe2-72f1cb1804e9 | -2.78033 | -54.09268 | 2026-10-06 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5c50f14c-27f2-341d-9079-67187de8a414 | -2.87335 | -54.16356 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 85a39584-4841-3a8c-a237-b7b4247e2d55 | -3.23677 | -53.87031 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea986635-248a-3e0f-89fd-9ea74eb36e09 | -3.09181 | -53.728 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cff06c13-b600-3711-aa9f-4531fca8bdd0 | -10.35125 | -45.02744 | 2026-10-06 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a374d4f3-36e8-3dd9-9440-0208e6cfab1c | -6.18686 | -44.85393 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6275b23-90a7-3945-a9f4-459ddfc9d3a2 | -3.07122 | -54.17767 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b50d35c-0c1e-3db3-a713-be5aa2b9c030 | -2.87633 | -54.1655 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README30.md)
