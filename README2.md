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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dd47036-076a-3756-af93-6ede47f111f0 | -6.7401 | -44.1371 | 2026-10-03 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 798c1ae1-3377-3441-9f12-517886096bfd | -11.6977 | -43.5128 | 2026-10-03 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 25b2b810-38aa-3fad-895c-6966de19beb7 | -5.7378 | -45.1307 | 2026-10-03 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 653b5c4e-180a-3da7-ba8b-16a72c92bb8b | -2.8856 | -45.395 | 2026-10-03 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 76f1b5d9-f9be-3af7-9773-fe1c49d38f07 | -4.3587 | -47.7853 | 2026-10-03 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 32d2fe31-1173-306e-9f3a-cdadfa7cf958 | -5.9569 | -43.67 | 2026-10-03 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d532a193-6807-30f9-b944-88b9aecdc018 | -3.1299 | -53.7431 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 208.9 |
| d2a75b28-0d7f-3004-b815-180d21c8e784 | -2.9082 | -54.0907 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2ab6f4ec-4671-361a-bf19-a1f2b10e7ffa | -13.5365 | -44.1044 | 2026-10-03 00:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 1c5e8ebb-780f-358d-b973-4d94d1836dd8 | -5.9384 | -43.6482 | 2026-10-03 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| ed91de19-67eb-3f26-9858-2edf6b6297be | 1.7671 | -55.6056 | 2026-10-03 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e8ca0473-d151-3e36-95aa-9ff9ef5ac5fc | -2.8898 | -54.1112 | 2026-10-03 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 054446c8-e65b-35fc-995f-70439354dd3f | 1.7854 | -55.6054 | 2026-10-03 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 79933d5e-13b5-3c24-ae82-93c5df382d4c | -2.9266 | -54.0903 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 249b0708-72c0-3df4-a262-6041ea4693de | -3.2768 | -53.8199 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 1679d1ee-9e08-3d50-835a-808274116423 | -2.8897 | -54.1514 | 2026-10-03 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 4a0c5698-72bd-3355-8e1a-5f4baa9c4e9e | -3.1299 | -53.7633 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 00ca2271-a520-3b6a-a9c9-1fe3c6a40d2c | -8.852 | -66.7827 | 2026-10-03 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 8ba27278-7dca-3543-8a06-593d4b43fbb4 | -12.8676 | -44.6878 | 2026-10-03 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 468f08bc-6c19-3a93-8cb3-300dc92221e4 | -3.1483 | -53.7426 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| f04f9ba9-71a7-3df9-b2fe-0876535a5167 | -5.7355 | -43.2916 | 2026-10-03 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d5278a95-1b21-382c-8abe-ffd3bf42bebd | 1.8037 | -55.5854 | 2026-10-03 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| f76aa5ce-c163-33a4-bc98-f1c1e3a0f9f7 | -11.0067 | -59.1381 | 2026-10-03 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 3d2777e5-c51d-3c7a-9f36-42e500d53d2d | 1.7854 | -55.5856 | 2026-10-03 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 7916210c-42c7-3ad3-900d-163dc1730622 | -5.884 | -55.4876 | 2026-10-03 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 0fc379c9-bdca-365a-895a-a53d9f886817 | -4.4506 | -47.9329 | 2026-10-03 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 7bd5bf18-9bb8-3aaa-a691-c65b7c36f2e4 | -11.6981 | -43.4891 | 2026-10-03 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| e4f7225f-c718-37ec-ac4c-0f4b461ff9c7 | -5.9381 | -43.6714 | 2026-10-03 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 1062f277-2e56-3af4-8c2e-35cab2bef26d | -2.8897 | -54.1313 | 2026-10-03 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 12b0b8dc-d3db-3cda-b691-7e51b3546c2e | -8.8704 | -66.8007 | 2026-10-03 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 3a66415b-c7a1-3324-b54a-778f875c2c73 | -11.7178 | -43.4623 | 2026-10-03 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a015a95c-aa60-3602-97a3-5b1fa38f2468 | -5.7376 | -45.1533 | 2026-10-03 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 905f85c6-0316-3d42-8e64-a8cee758f963 | -11.7182 | -43.4386 | 2026-10-03 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5c62c3a7-bf6a-33fd-8045-4e0eb817e49d | -3.13 | -53.7229 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| feb454fc-cc30-32d2-ab6e-a73c7eed5640 | -6.8578 | -59.3022 | 2026-10-03 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| eb229691-a105-343b-bcee-1e629e836e4b | -3.2952 | -53.8194 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| dc4d9fba-a6b0-33a4-8c89-fe1d6eac9c8f | -3.1655 | -54.0844 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6bfffb05-4b49-3575-af43-e322b5862ba4 | -8.8519 | -66.8012 | 2026-10-03 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| d548d8ba-8eb0-3fc7-bac2-c8ebf41074a0 | -2.9042 | -45.3944 | 2026-10-03 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 96.9 |
| e120a229-69a5-352d-a35b-c92a6d4ad0f8 | -3.4093 | -52.8233 | 2026-10-03 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 4a172b0a-e82c-3b26-b11e-77e4f3a81bd5 | -3.1116 | -53.7436 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 3005550c-dca7-32a0-beab-943f25041c60 | -3.4093 | -52.8436 | 2026-10-03 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| b3e303e6-c14f-3a01-99c5-ea5ee418a71c | -2.9265 | -54.1104 | 2026-10-03 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 749dc965-4233-351c-bb88-1c2550a180d8 | -8.8705 | -66.7822 | 2026-10-03 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 39c8203a-5d9f-3fe1-bbc1-69a359f2a136 | -2.88 | -45.42 | 2026-10-03 00:15:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b75f915f-214a-3eb2-b225-754880a9ccd8 | -2.9 | -45.42 | 2026-10-03 00:15:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 434f8b02-2454-37ee-ab8f-c7b5da628a66 | -11.47 | -43.4 | 2026-10-03 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8beafea7-c46a-3860-96a3-fc252c92fe74 | -3.1839 | -54.0839 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 2087bcad-e405-3bb1-b585-b0969d16a43d | 1.7854 | -55.6054 | 2026-10-03 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 5317b2e3-e95e-359c-9730-f40295451774 | 1.8037 | -55.5854 | 2026-10-03 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| c2a1a4fc-5cb6-30c3-8a68-f42f370708e3 | -1.2107 | -47.7735 | 2026-10-03 00:20:00 | GOES-19 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 58acc5bd-0315-36cf-94c5-87e43f1bd02f | -2.8855 | -45.4175 | 2026-10-03 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 38b20a06-306f-37e8-a738-854e4d8caf49 | -5.7376 | -45.1533 | 2026-10-03 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 83e1d649-d873-3e4d-abe3-210b70030b48 | -11.6981 | -43.4891 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| e204902a-6315-3244-b879-e9c464fd04ff | -5.7355 | -43.2916 | 2026-10-03 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| fe7cdc31-cc73-3b98-9b7d-10a28474fea1 | -11.793 | -43.5452 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| bcf6c240-c73f-3dee-90b4-5ea8b88cd897 | -2.8897 | -54.1514 | 2026-10-03 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 3cff4d2d-7012-32a4-a3ca-4bf22d1cf473 | -5.7563 | -45.152 | 2026-10-03 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 6c221be4-3e69-3824-8de8-b88189958f75 | -11.7567 | -43.4325 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| f71d45e3-5a34-30d0-a180-75a1fa4d7630 | 1.8038 | -55.5656 | 2026-10-03 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 8947a463-06fb-3fde-8668-c127823a3a9d | -2.8897 | -54.1313 | 2026-10-03 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 65ef1925-4ca9-36c2-8391-c3c8625b13c6 | -10.9879 | -59.1393 | 2026-10-03 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 138.3 |
| a7f2d873-c005-39a2-bc95-7d8e4cd3d33b | -11.8123 | -43.5422 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 8d5c946f-46d0-33b6-bddd-baf21e77f65a | -6.2091 | -60.0187 | 2026-10-03 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d58d5707-7d5c-3498-8aaa-225d00de51e0 | -3.2767 | -53.84 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1753bbba-0083-3d2a-bc2b-7a3d257c41be | -10.9881 | -59.1197 | 2026-10-03 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| bb7ca99b-49e8-3602-8462-9c1322a5456a | -5.9569 | -43.67 | 2026-10-03 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d3ecfae3-5497-30a1-9431-47af16986673 | -4.3587 | -47.7853 | 2026-10-03 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 3f896f2c-0a13-368b-951b-0a8c6112dd35 | -3.1483 | -53.7426 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 4749d95f-6d69-36b5-a8f7-8cff7a01004c | -3.4093 | -52.8436 | 2026-10-03 00:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 2d86f57c-252b-3cad-8152-09e2b7066eaa | -6.7401 | -44.1371 | 2026-10-03 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 7d01ebd4-5e85-3663-8e5b-a0b69f71a94b | -12.8676 | -44.6878 | 2026-10-03 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 53beb080-15c9-3905-b2dc-bec16318c454 | -3.2768 | -53.8199 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d2a93590-b527-3e89-9228-d53598f0a3a2 | -6.8395 | -59.2643 | 2026-10-03 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e65be943-724c-3aba-ad1b-b0a934dbf948 | -3.2951 | -53.8395 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 02cdca2e-f83d-3110-974c-c2a3582b80ce | 1.7854 | -55.5856 | 2026-10-03 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 442189fe-6792-356c-954a-712fbacfa142 | -8.8705 | -66.7822 | 2026-10-03 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 008b7332-79ab-3809-b5b7-7eb16bf55b48 | -11.7379 | -43.4118 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 92f2a24a-0acf-3a07-8cf9-08992ebc636c | -0.9147 | -47.9069 | 2026-10-03 00:20:00 | GOES-19 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 0b58c70c-e4c6-3bc1-a9bd-81cea672a15b | -3.13 | -53.7229 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 194e91f9-62a5-37f8-acd6-b1f441ea5deb | -3.4093 | -52.8233 | 2026-10-03 00:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 06bb49e5-c0b4-3df1-85a0-72cce2c2de9c | -5.9381 | -43.6714 | 2026-10-03 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 0e80120d-f1d7-3eac-9806-13c20664fb8f | -2.9041 | -45.4168 | 2026-10-03 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 143.8 |
| abcf47aa-4e4f-31ba-be03-ac1ae2706858 | -11.7375 | -43.4356 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| aa02cc62-dc2d-369c-ad25-8151f48eca6f | -2.8856 | -45.395 | 2026-10-03 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 151.9 |
| d0791a46-9cb2-3dfd-8482-e29a194b97e0 | -4.3588 | -47.7636 | 2026-10-03 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a1893026-eed9-380e-b2f0-487b655f1eeb | -5.6134 | -44.3876 | 2026-10-03 00:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 95648852-f244-36f0-868b-adb558f9d908 | -11.0067 | -59.1381 | 2026-10-03 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| a7339308-8c2e-3b7f-be99-d4194dd51113 | -5.9571 | -43.6467 | 2026-10-03 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 0ce61932-4d48-3138-b6bd-03b2f4d7398a | -3.1299 | -53.7633 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 32af6e8f-31ad-3f8d-bfcf-be08729109a0 | -11.7169 | -43.5098 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| e36e91ff-b929-3482-b11d-874e56535cbc | -3.2952 | -53.8194 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 40ea75f9-67f3-33c3-9a65-3b238a269071 | -4.7434 | -43.2679 | 2026-10-03 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 74e93a2e-937a-3fd9-a6dd-f19ef1e18e82 | -2.9082 | -54.0907 | 2026-10-03 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 329f88e6-40fd-3823-a9a3-cb75117ef5e9 | -2.8898 | -54.1112 | 2026-10-03 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 97c94474-b1ec-3b1d-b370-e1be7a279be5 | -5.9384 | -43.6482 | 2026-10-03 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 14eed4e6-7d02-3113-a819-06ec57226b84 | -11.7187 | -43.4148 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 2b0c0a07-0779-317a-92d0-23e58d7b3aee | -6.8394 | -59.2836 | 2026-10-03 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a527d3c5-c776-3c90-9d6d-4206d791fb33 | -9.6923 | -57.456 | 2026-10-03 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0c3dbf68-e7de-3d33-93d8-fd814f567573 | -11.7174 | -43.4861 | 2026-10-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |


[Clique aqui para ver as próximas entradas](README3.md)
