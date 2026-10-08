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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bda2b20d-3909-3f6c-bfa8-d3c082e19c84 | -3.11445 | -54.16962 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d5b0b97c-67d2-34bd-b905-dedb2348ea64 | -3.0833 | -53.95492 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 377a688e-4fe6-38f4-b40b-134938cb17a8 | -3.86362 | -50.40946 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1303a529-8383-3bf5-a5e6-b3be98b370bc | -6.72341 | -55.06258 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 548578e9-dbc0-3647-b1df-ca4cba8fb034 | -2.77331 | -54.07163 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cefd4737-0d3a-3856-9c58-9ca5f0c2fe94 | -2.83259 | -54.12816 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74ae8d25-f65a-3bcd-90c6-254f92fdd364 | -4.96309 | -55.82516 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c59f2638-c9c0-347a-9175-53905b34d873 | -3.16664 | -50.59847 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 54a48b9f-781d-3e1a-9fb0-c13b35a7a09d | -2.21807 | -53.70294 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 803bc929-f06e-363d-a99e-be817b7ff5c8 | -2.87184 | -54.47473 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 105aaeb7-c58d-3b5f-b2f4-1a1d94410419 | -2.87024 | -54.88629 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d4f1986-303e-3242-8ef1-c62534d40d69 | -3.74431 | -51.20837 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9aad4027-f198-3c11-b2c5-b87c5670c5fc | -4.5644 | -55.0538 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b141e42a-2d11-3e00-a8a6-fa9a813396e3 | -3.31045 | -53.86235 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58f8b13d-5fa1-3016-a06e-a0581e04e5b9 | -2.40253 | -51.30446 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1e70e1c-5e6f-38c9-ac9a-c55e74d0396b | -2.77852 | -54.08429 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6328cdc9-f641-349f-9b95-a79b95552477 | -5.06907 | -56.90536 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17bf5daa-a172-3282-a7c8-1e2382863f7e | -6.73384 | -55.13468 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4931aca2-f069-385b-a83c-9ff5f2e663d7 | -5.8215 | -53.83808 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f2cc44b-3ddf-35ab-a1f8-c4cf56230334 | -3.01847 | -54.76265 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e225641a-5bea-3365-8e8b-fd3ab8bf1a85 | -2.84841 | -57.46728 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a28d0ad-6dbe-3b73-91e8-d9a49072bd25 | -5.68871 | -53.48303 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a7e5568-bf9f-3ea7-8de8-97c9694d68ee | -1.51876 | -54.53466 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e9bd8bf-111b-3343-bd67-ef6c3e6e5c8b | -2.87365 | -54.8868 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2a394eed-d682-3968-b511-64ce2329aed5 | -3.02023 | -54.10475 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 18d96093-18b0-3109-af1c-b6159b0091d0 | -3.05915 | -54.24457 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b9d3b9a-0ac6-3a87-9189-fe852e425629 | -3.07861 | -54.26233 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 767e33de-5379-3712-90e6-04b0fa1154b2 | -2.5014 | -56.18136 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ba933d33-5f1c-3c40-a7cc-abf866c235b2 | -3.02965 | -54.09037 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fbcacfc6-e4bb-31ec-9caa-53057d782a7e | -3.57551 | -59.4607 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 652f9aab-4e2f-3136-9eba-ff13cef5c210 | -1.49431 | -55.66174 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e609e68-1bf0-3d50-af55-017a04ec9553 | -3.59212 | -54.57533 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 434b0784-98c7-3b32-a357-3c885e43d0f7 | -5.04107 | -49.77128 | 2026-10-08 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5891f67d-805b-35ee-9c2a-7372229073c8 | -7.21966 | -55.08805 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22aafa98-13af-3e44-9fc8-94f850e79d50 | -2.79103 | -57.65414 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df706685-e603-3177-ad7d-b11eef105e65 | -5.36947 | -55.88414 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8c69ee6-83cb-340e-8703-2312fe39fbd1 | -3.01973 | -54.08488 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 02122dbd-6154-39be-86bd-2df1bd73f04b | -2.93734 | -54.17096 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c82b9af5-c4f0-3b68-843b-88075e015f42 | -8.53241 | -67.01026 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d952016-f912-3d1a-be2c-12894145a233 | -5.29203 | -60.10356 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c24c2c0d-900e-3192-95fd-97b92f09baec | -2.79603 | -54.08701 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c750ad8e-c65c-32c0-a6e8-55b43477a7e6 | -11.32363 | -46.66362 | 2026-10-08 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d587661-54e5-303f-98e1-ce9af8061ec1 | -3.04678 | -53.95732 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 53c9dfed-bec6-3abf-929e-85e6c3e6a1a9 | -3.67097 | -54.50248 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84997069-e73e-3b43-93cb-c4a3c282c38b | -3.35089 | -50.48046 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5b8d1853-0f55-35a5-bef4-f33788b0dffb | -3.56218 | -59.47506 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99987cb1-f72e-365d-944b-99c945a0a559 | -4.74888 | -55.65763 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f1d7a573-fa83-3f0e-a948-5e2ae51cb738 | -2.99065 | -54.06066 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47bc4b02-b2e2-3080-bf4c-244fbd236e23 | -4.92163 | -55.86969 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68920a10-167a-3202-bf59-a65331564cbb | -3.52803 | -54.63124 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9b2a1c5-ba4b-3c88-af11-ea0a04c5dbc9 | -3.06082 | -54.25658 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dfda298-09dc-34dc-ad07-bcfeed3486aa | -3.03146 | -54.07875 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7bc6b50d-601c-3a9d-82be-aee84e10a49f | -6.50963 | -55.39465 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 174d83a5-ae00-3f5a-9ee2-9bfa6852304e | -3.78735 | -59.37745 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fa72b16-7fc8-3d60-a0e7-7407f6444312 | -6.67503 | -55.09106 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd67a8c1-f420-3c31-a6d2-89f6c98b4d8d | -2.46743 | -56.09456 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89c91bd0-5dc4-39f1-9b4c-08d12eff61b5 | -3.17755 | -58.64246 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8839bba5-221c-309f-957e-51c9823a6be3 | -2.76647 | -54.08724 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3e7bbaf-b8bd-3d44-9b76-cb5b53939138 | -4.11317 | -55.17173 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c830eaa8-36ec-342a-8697-b8383efab136 | -2.50856 | -56.15769 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c12bfdda-dd2a-3b15-a7c1-468717885fe0 | -3.27617 | -54.03489 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e96ae82-40ed-3eb7-9bce-51b6d8c239b1 | -2.13773 | -54.4635 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bb80045-3f62-35e3-a249-68aa47e22ea4 | -2.55018 | -57.38843 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e901d722-ad2c-3a71-bba9-5e1a68a15f87 | -3.50158 | -59.27326 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a080680d-edc0-3c08-9f34-0cb60bfbb9f2 | -3.61471 | -55.27702 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e59d3da4-6fa8-3021-a6e8-8568bb134f40 | -3.00624 | -54.2404 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b289bedf-33b7-35b5-8bcf-d4b984561d08 | -3.98489 | -59.34321 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0facebb2-7d90-3486-b576-5fba57d6e1f7 | -5.20998 | -56.07734 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b584e875-3fea-31b0-9f49-81e2e54f43d1 | -5.51988 | -50.01849 | 2026-10-08 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fadb1c60-9684-3ccb-84db-3f1340da346e | -3.29022 | -49.51481 | 2026-10-08 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3372c9df-1dad-3d09-9140-dff6e78a32dd | -3.00899 | -51.12344 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb441138-ccda-36f8-a6b3-830d47a80c96 | -3.07623 | -53.95386 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 6083d020-6522-3447-922d-be0d8c59d879 | -3.08621 | -53.95939 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5ef8ba85-f4b7-3cbd-ae20-1c7c642fafef | -3.10202 | -54.98827 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31ff64ba-55a8-3b8a-9309-679578ce1169 | -2.98697 | -54.08769 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46227e01-bd69-37fc-b5b9-bf32f814763b | -1.12722 | -49.19128 | 2026-10-08 05:23:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 927b7517-8d86-351d-9d1a-50d3a03a7687 | -3.88096 | -55.8238 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccbd9697-9d41-3821-abec-0122d818199b | -2.99293 | -51.05183 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05513cb2-2ea7-3022-a494-10735febb166 | -3.99098 | -56.25922 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68d7df4f-3d4b-3a36-9c03-ec87f757a535 | -3.58788 | -54.67057 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7071fcb5-84a4-3747-8caf-f296fde677a7 | -2.89809 | -54.07806 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9926032a-93e4-3076-94f6-1fbe48ddee44 | -3.70545 | -58.29184 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aac0721-517f-3560-ab67-7619edceeadf | -2.99453 | -54.75889 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8eec560-1ee6-3330-97da-9ef6d6ac617a | -2.7587 | -54.11358 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae77f82b-bd6a-39d6-aefa-80265fbd3fa9 | -3.04899 | -57.48109 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d9139f5-7a81-3a83-901b-f03a9916d48d | -3.05261 | -53.96625 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 71c1f067-5e8d-3eb2-a99d-80815ac546fb | -2.4924 | -56.1091 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 047e7dba-6e3a-3a47-b7ea-4e59b85e297a | -3.42906 | -58.60099 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50cde6d8-8b90-3f66-a83c-dabdbd82d3b3 | -2.50777 | -56.33454 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cbf0149-0854-3a91-a330-b8f63be73b00 | -5.72837 | -45.15033 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fb8f13eb-3cdf-3a3c-9046-fc914719c620 | -2.64282 | -56.54731 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bf414e2-f201-3df5-9b3a-9cb671ab4c1c | -3.54459 | -54.66058 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a5499b1-bae9-37b7-94f3-97375106d8b8 | -3.0033 | -54.09816 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d04a25fa-c25b-303c-9bef-6878c3e49a66 | -3.0899 | -59.18661 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21801e0c-5e30-3eeb-aed4-6bb1c4c76f19 | -3.47263 | -59.56545 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99223efe-e5be-3a5d-9d71-13bd5a471806 | -3.52676 | -54.66167 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4be0372-bffe-3be5-88fe-5bb2b030d9df | -2.94024 | -54.17531 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35dd7d4f-586a-3c13-9ed5-862b2ee61d87 | -2.80979 | -57.05255 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3841a867-09ca-36a8-b464-93fa4a53f229 | -3.47652 | -59.58704 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30ea4bd9-9506-3f59-a7c9-b86a7aa62483 | -4.93729 | -55.81383 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README132.md)
