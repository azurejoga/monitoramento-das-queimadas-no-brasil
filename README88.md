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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b5116bf-5853-357c-825c-8f86c8eba85c | -3.6997 | -54.06592 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b36f2d1-4907-39e8-95d6-23796df52de9 | -3.69915 | -54.06946 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ab0487c-8ff2-390e-8c1c-5697777ee9b7 | -3.69635 | -54.06541 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 888a5f16-8066-3f8a-a67e-93c0467e466a | -3.6958 | -54.06895 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3fb03c1-c82e-3b16-a426-0cefe278fa0f | -3.69408 | -54.25558 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a3d99a0-687a-3483-bfd8-60d3e6c3018d | -3.6902 | -54.25854 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e356ee73-7cd6-38eb-a6e3-f15fca6cfce9 | -3.68965 | -54.26202 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7104e5e-7159-3b16-a051-489f8fe2e557 | -3.68673 | -54.21502 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f043695-83ab-3d06-b4ba-514b28357497 | -3.6737 | -54.32036 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c948f6d-2e1d-35e7-9f9a-560a339940f3 | -3.67091 | -54.31635 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c2fe03c-c7fb-37b4-8e13-5255207ba04b | -3.66757 | -54.31583 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9251e055-c8e1-3b48-a76a-1404331caf14 | -3.6594 | -54.36808 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce4a25ea-2d51-3258-a4b0-70bed92c6664 | -3.65368 | -54.31725 | 2024-10-29 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aa7f996-c316-3c60-82c6-897def1367d6 | 1.60159 | -55.6359 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee8c8a6f-67d6-33b5-ad76-1bd42fc08751 | -2.14225 | -55.75063 | 2024-10-29 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2cacdbd-03fa-37f2-b4d7-4c2bcb097127 | -2.03185 | -55.67579 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9affb994-b2ca-3f56-b387-13c8cfd75363 | -2.0274 | -55.7688 | 2024-10-29 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 238ef2a6-88ed-37ab-8f94-99f8e7737c1f | -2.0054 | -56.39291 | 2024-10-29 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a44bb2b7-5e46-346e-957d-fe741681c00b | -2.00514 | -56.39317 | 2024-10-29 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00724721-c777-3b5a-8fdb-3f523b0a0573 | -2.00459 | -56.37438 | 2024-10-29 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b97344d-8f98-30dc-9ea1-d5d66475019e | -2.00068 | -55.71023 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c69d4f8f-4c3a-39a0-a6c8-7f1ad1f19429 | -2.00013 | -55.71375 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b49b07e-4eb8-3fcd-a227-210ec16c71df | -1.99678 | -55.71323 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36ac4b79-ce64-34a6-9d7b-5d68b9551b5c | -1.82892 | -54.99219 | 2024-10-29 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9b97ae1-3fab-35c4-a922-f386ba87616b | -1.78219 | -55.41811 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12290b85-68e6-3897-a087-addb73e59ac6 | -1.77128 | -55.55241 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5487eded-c250-30f9-8c24-181fc898e19c | -1.76794 | -55.55188 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86efa315-0f35-3ae4-b072-6db11256527f | -1.76133 | -55.2261 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 645abd52-347d-3b9f-aeab-95fbaba30e01 | -1.76078 | -55.22956 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ddc51fe-604e-3aac-9761-e21a57a95444 | -1.758 | -55.22557 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7db2a52d-1851-3e29-8524-fbe3eda268d5 | -1.74373 | -55.25529 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e43d780-be3d-320c-a7ce-3f1591b00667 | -1.74319 | -55.25877 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 705e26b8-683f-379e-a7e5-775c8f193836 | -1.74079 | -54.99256 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39a8986c-3e4f-3ab6-a3e2-da65c063c105 | -1.74025 | -54.99601 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a220a6c7-0920-3d13-8315-357386ce38e0 | -1.73693 | -54.9955 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 715d578e-2e10-337f-8638-11ed931a13fc | -1.72811 | -55.00827 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b12c7dd7-0ecd-39cd-bb48-014236c7e3a7 | -1.72424 | -55.01121 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8590f23-c601-302f-a158-bcf9408913ff | -1.69286 | -55.08065 | 2024-10-29 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f59cff3c-dae5-33a8-b06a-54227e998b75 | -1.68953 | -55.08014 | 2024-10-29 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 985c63c1-c2e7-3828-bca4-dbaf2c257680 | -1.64468 | -55.13296 | 2024-10-29 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c6a75f5-6bb6-368c-a009-7852b35313f6 | -1.63725 | -55.05031 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd975e7a-a7c2-31ba-a7bc-d4296089433b | -1.62585 | -54.92826 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a98f18c-a395-315f-acbb-800052ed7611 | -1.62253 | -54.92774 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e817d634-7703-3a09-aabb-c4e6450d3a8f | -1.53878 | -55.47993 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 041be784-4b96-3c83-89a3-96eda6016fa8 | -1.42765 | -55.07094 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27ce6cd0-2eb8-3970-ac91-158b511143be | -1.41527 | -54.99815 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11c87372-2a60-3ef8-b718-4ecee953bf01 | -1.40293 | -55.38029 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdda7ba1-0a84-39cd-a94e-dbc365c33d69 | -1.39959 | -55.37976 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be3aaeef-c871-3e20-9bb7-fd9d417f4095 | -1.39904 | -55.38326 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db55c288-73d3-364f-82ea-1762f4b2fdb7 | -1.39585 | -55.20801 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60a23c89-80c0-3e33-ae66-10178d18cb03 | -1.3953 | -55.21148 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caed154f-c606-357e-b76e-89b0d704f62e | -1.38038 | -55.24118 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06a835b9-b1b8-3f1f-b20b-c87807bee714 | -1.34359 | -55.1501 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 03a66c38-9d4f-39b2-a30e-4042cc238ebc | -1.34304 | -55.15356 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e0d70681-7dfb-37d3-a55d-cb4fc88f2fce | -1.34026 | -55.14957 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f356e570-d7b0-3db9-bbe2-c1785210bd06 | -1.33971 | -55.15304 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58815e04-b85a-39f0-a323-99715f5300fb | -1.32681 | -55.45071 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aef7a7eb-e633-348e-b126-9cbd21e12442 | -1.32626 | -55.45422 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 681a3220-9094-3d4e-961b-ab0be1557d2a | -1.32235 | -55.43562 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea382129-572d-3f61-8a5d-25a8212bc802 | -1.90687 | -55.65238 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f78d536c-4ca5-3803-998b-e2c05b49b9e3 | -1.85654 | -56.36226 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fcc0330-253b-3006-927b-85cc65565152 | -1.80322 | -55.70826 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adba7016-2f66-3f7e-989b-9cea2d6ac6e5 | -1.79876 | -55.67146 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5acc9c5b-78e7-3f04-a8f1-80992b64c6c3 | -1.76871 | -55.6995 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8323406-90ae-3124-a55b-24e1dc283ede | -1.76417 | -55.64104 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b671472f-4fad-389e-8092-073063887a39 | -1.76362 | -55.64455 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da2dae84-823a-3413-8cdc-149018645be1 | -1.76082 | -55.64053 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efa332fe-65cd-3022-a7f4-acc5e03c4f50 | -1.76027 | -55.64404 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 956feed5-4cd4-3d2e-ac79-d7523a29d67a | -1.7575 | -55.66161 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c36ed8a6-fb84-3ad9-8888-ca2c1209a486 | -1.75662 | -56.19805 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a1c74f2-860e-3944-9c4a-327fa538adf9 | -1.72679 | -55.66043 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8713f70e-80cf-33e8-a347-8b14d1e90534 | -1.64552 | -55.6839 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ae08179-d9d1-3444-a1eb-ed40229674a7 | -1.59966 | -55.88734 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed8f0ec6-7c15-3315-a205-ba291e6dd561 | -1.59629 | -55.8868 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fdcaf6d-8556-3e18-a623-1feabffd4374 | -1.50099 | -55.8279 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 118b83b1-5b84-3477-80e9-a4c3da210909 | -1.40069 | -55.99556 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 342760bc-05ea-3eb5-aa65-69ede3314052 | -1.3973 | -55.99503 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71e7e48c-ba2e-358f-8003-f1f6bb0de2d1 | -1.37764 | -55.85629 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2145ae58-b370-3c7b-9e8b-33d0f19b6a4e | -1.37708 | -55.85986 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04dc7dc1-c6ab-30db-817f-5db3bb846772 | -1.37652 | -55.86342 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 151704c3-ed39-3693-a337-11e1e50f4a2d | -1.37371 | -55.85933 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8df3e308-de9b-312c-a7f5-21b0a62e5175 | -1.37314 | -55.8629 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78cd9acd-30a9-3567-a11a-354a9a23369c | -1.37033 | -55.85882 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eabdc559-d650-3e02-a86b-20ea3cd2bfc2 | -1.36977 | -55.86238 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7cb8856-666c-3bc2-a58e-85211fbb91cb | -1.36921 | -55.86595 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2195c201-b807-3bec-b0bb-68bb89748097 | -1.35922 | -55.68985 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0e0a635-9578-3d08-a977-d50d8510d72a | -1.35783 | -55.68991 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b811b130-4723-3d79-b450-d9210e02c206 | -1.32213 | -55.82975 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3099f7d3-72c3-3c49-a06d-497060cb79db | -1.31876 | -55.82923 | 2024-10-29 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d533dee9-5bcd-3e05-ba75-481630307502 | -1.30075 | -55.72452 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62d8ec2f-f1d5-337c-982c-0bbb717c0ea5 | -1.29739 | -55.72399 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8454f73-72de-3cd4-b2d3-aea8dfab77a0 | -1.29683 | -55.72754 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 868778fb-576c-3d86-99db-44791b244444 | -1.29627 | -55.73108 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9bc77e0-85fe-391a-a0eb-e4561480761f | -1.29515 | -55.71637 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e589d6dd-285a-37c4-bb44-05c70b0b3c33 | -1.29459 | -55.71992 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 007f1814-d498-3d83-8cac-2c2af505e232 | -1.29403 | -55.72346 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b443af8-c1c9-3579-81ea-56f68cee8f63 | -1.29347 | -55.72701 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b466e60-47ef-3073-8f37-201320eb10b2 | -1.29291 | -55.73055 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbfe77b2-dc2c-3b9f-ad38-73791cff4522 | -1.29235 | -55.73409 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab70b33a-82b4-3ea4-9e56-ae4b48531caf | -1.29179 | -55.71584 | 2024-10-29 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README89.md)
