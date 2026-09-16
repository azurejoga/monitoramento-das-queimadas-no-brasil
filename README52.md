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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41a67912-f01a-3c15-8cbb-1d7174d073a3 | -6.09508 | -57.69642 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 612fa987-9b78-3d4f-b65f-f570ddd414bc | -3.45178 | -59.52575 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e66ae69-bc81-3275-87c0-6183d27d347b | -1.61304 | -55.56599 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89ffbfd5-e2ba-3134-a679-39370cefb931 | -4.57415 | -54.91018 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40417475-a4e4-3aee-9601-ba0997aec715 | -6.02959 | -57.77379 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73824104-f889-396e-b8a4-7206dcf0d44d | -2.91507 | -50.42647 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0a5f475-cfcd-32e4-836d-8422ad30c2a6 | -2.10391 | -52.04064 | 2026-09-16 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 11eda290-46da-3995-b8f4-ead81da378f8 | -5.75597 | -57.59126 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 81c4dea0-d9d0-3a50-8451-3a16b6ac4cb7 | -2.89483 | -50.41274 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2398080a-b71e-388a-a3a0-939af06ad349 | -5.86114 | -52.0346 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3dd838ae-d9a9-3848-87d5-3f81dc256c3f | -3.16851 | -58.64249 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3c6912d-a3ed-3802-a1b2-485bceb6e686 | -2.58002 | -55.99314 | 2026-09-16 05:33:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 403ce91d-35f8-35d8-8d31-de51b288cc75 | -2.10794 | -52.04656 | 2026-09-16 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 573c4032-be6b-39ee-8552-0a0db7160c31 | -5.64263 | -60.21885 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 022dd52e-34de-30d4-9ec2-f950cb46bb40 | -2.91433 | -50.39433 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e38cb21-b536-3ef5-8313-47290a467b9b | -1.84923 | -55.80817 | 2026-09-16 05:33:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e200eef-8c3e-33b5-8ed2-cae718980f34 | -5.24328 | -59.9852 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab9c2244-82cc-3b3b-89d0-87f53ae03d17 | -3.26563 | -57.89097 | 2026-09-16 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17da6622-fb2c-34ce-9460-d2a372569ee5 | -3.4465 | -58.0059 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1dc03947-947f-3db2-ad79-1f73fe4da9fc | -3.53831 | -59.06485 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| aba092b0-ba7d-334c-942c-411597c2f061 | -3.84871 | -51.76362 | 2026-09-16 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75e990ae-a5b8-35c0-82ed-452bb43a6d3e | -3.3281 | -59.44963 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8d614ec-df3c-35e6-aaaa-044cfe634cfe | -4.54723 | -54.92171 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a45f1604-9db4-3461-aba1-0bfad28f9e74 | -4.57358 | -54.91396 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d2becf0-f4cd-3b67-bd44-6354f3f6b05d | -2.87857 | -51.74059 | 2026-09-16 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 253e5da8-60fb-342d-b6f3-7e44c9c68051 | -3.71889 | -60.59314 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e45b2981-41a8-3570-85c3-7f9fc453b6fb | -3.44592 | -58.00961 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e88b237-9030-36b1-9c16-ed811d79db25 | -2.90909 | -50.42914 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc681d01-1ca5-3667-aa06-97a7d52a263e | -2.82348 | -51.34211 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da4f1c59-fe78-33a0-81ca-eed906a35854 | -3.42291 | -58.2246 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d589ca6-10eb-301b-b9f5-fc4cac09a307 | -4.37779 | -55.03251 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdff0bad-f7f6-3f49-9a8c-edd93bd201ae | -5.1503 | -55.93534 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| b7a29092-ff9a-362b-ac2a-c51bf013528d | -3.81056 | -55.89239 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cedfb3e4-b56b-3ff2-93ba-e6a451c97ba7 | -3.39592 | -61.30295 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e6db10f-7cb3-312d-ac65-b10901a5be84 | -2.90261 | -50.43522 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7ee2579-937d-3f3b-9fcf-72dabbd9d0e8 | -6.02666 | -57.76925 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4b2e8905-0c15-38c7-a03b-68a8e7452c1f | -3.01652 | -51.3428 | 2026-09-16 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d54aff7-2fc1-3c21-832b-981a98ea939b | -3.59847 | -59.06379 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f735c976-f69e-38d7-a06a-f74e1cdbefca | -4.53221 | -54.97187 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e6c00c0-487c-3576-92b5-55d72897cf4f | -4.34657 | -46.61208 | 2026-09-16 05:33:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d14b1efe-3e42-3c25-9f4c-02ca2c626b3c | -5.12473 | -55.94434 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73d1edd3-9424-352a-94ba-d6f6af1cf5d6 | -5.1457 | -55.93962 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3ddf9a6-9cb8-3968-bf95-0ecd2122a933 | -3.17502 | -61.11362 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba8b59ba-de3b-398e-a5dc-580023199b64 | -4.26521 | -56.0105 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aed36e0e-6487-333a-9a42-ce1a0eb32bab | -5.10155 | -47.61791 | 2026-09-16 05:33:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8f5d911e-7487-3c1a-972f-453be845ab35 | -4.49381 | -55.49957 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7108cb10-e5c7-3bc6-9c20-e62afef353d1 | -6.16094 | -55.71183 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50df0328-5e20-375b-9af3-0c694c84f6bd | -3.80865 | -58.89795 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cb49ec6-c1f0-3ed9-afe2-2d4f64a06785 | -2.90888 | -50.39346 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d8b1f14-fcc5-336a-b21b-e63c2723b906 | -3.58721 | -58.53494 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a4f1c5b-b10f-3b03-a1ed-a04a66cb00f1 | -4.18067 | -49.40474 | 2026-09-16 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 780fda3b-f82f-3097-a6f5-398cf6754425 | -3.8855 | -58.74584 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17e6bf40-056c-3f6c-9733-e975a7dcdd35 | -5.50002 | -60.13611 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a62f966-7f59-3c47-bec2-769f291909c4 | -5.99942 | -52.10339 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fc0a012-59e7-363a-9c80-d84b7a9636a1 | -2.92052 | -50.42725 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7865b6b-58fb-3d6a-ab37-1492275b4090 | -4.5706 | -54.90578 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee983d0b-9968-3480-b290-c64ed913cab9 | -4.53689 | -54.93493 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20a77ffe-5a92-3039-b7cd-d7b2fd34d690 | -3.02165 | -51.34361 | 2026-09-16 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 443960e3-47cc-3380-965c-9782468e5552 | -6.10497 | -57.6314 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52400a89-791f-3a18-953c-3841a94b02f7 | -1.28495 | -55.71735 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2aa2b60a-0155-39b5-bc25-7f1b460e8224 | -2.26637 | -57.08694 | 2026-09-16 05:33:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d1aa93de-82cd-3633-b0aa-2b80cd1886e6 | -3.5889 | -58.54625 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3b6b86a-f11d-3837-b3d6-74cc83b335ce | -2.92104 | -50.42384 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36411cb7-8bb2-3ac1-8893-2e3aef9977dd | -3.32478 | -59.4491 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 278bcfe8-4c0c-375b-9083-60ffe9b1c208 | -3.2959 | -59.466 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ae22e90-dfe1-3153-bf21-313980809b74 | -2.91769 | -50.40913 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 125550f3-fcb7-3020-b447-4d1bbec1c946 | -2.91403 | -50.43337 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28f25bac-9a5a-30db-ad6a-6885afd1905b | -6.03021 | -57.76981 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 76a62249-ab0b-33a4-a4ae-857c74416d37 | -5.3558 | -55.89497 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da8c836b-e9a9-3b26-9323-74d2dd622077 | -3.11966 | -61.41489 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14ecd84b-30e0-36ed-a930-ac5fd4a62f7a | -3.75284 | -61.75808 | 2026-09-16 05:33:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ad9a444-3f1c-3cfb-a9ee-76b2beb4a4c9 | -3.73964 | -55.94809 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59720ed3-ae16-3a7c-b485-f69a3938594d | -4.53278 | -54.96819 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcd66007-b225-3b8d-a4da-67ac001646a9 | -2.89976 | -50.41707 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4a7e86d-2f7a-38f7-aec7-16e870026ce3 | -6.78552 | -47.87239 | 2026-09-16 05:33:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42cf2b59-7136-3df5-be05-32d708875018 | -5.11072 | -47.60131 | 2026-09-16 05:33:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d7bce0b-827f-3cf0-86cf-b719a73299fb | -3.04781 | -61.27391 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4590fb8-e019-3825-be32-b90010e535c5 | -2.91275 | -50.40482 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b79355f-ff90-3f78-afad-2a1c52d9fb4c | -2.96221 | -50.41146 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2332189-3f40-3824-9b5e-296786991510 | -5.9805 | -57.76218 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acfbdcc5-c876-3d16-8bca-26e1e22048d0 | -2.90468 | -50.42138 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce2f4ddc-2461-3e46-b254-929460034f58 | -5.63413 | -51.67686 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3fe7ca47-766d-3743-b16c-351b49e3f7cb | -3.74599 | -61.75699 | 2026-09-16 05:33:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aa8e8e0-af6b-32de-a450-1c7c7bab1bfb | -6.28392 | -56.04107 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e97e41bf-9de0-3bb5-970c-8ee294a90297 | -3.0762 | -61.01052 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9061f9f3-ea58-3c4c-9e97-aabcd105a0c8 | -3.33575 | -58.1329 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4acb6981-5821-3fe5-a024-d5bf003d62be | -1.21596 | -47.89346 | 2026-09-16 05:33:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5a50372-d967-3197-94a6-1442bdf3eb4e | -6.01708 | -52.16027 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab2436f3-1fa0-3910-a0c4-029cdfd818cb | -3.75225 | -61.76177 | 2026-09-16 05:33:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b84614a-3c43-3545-9918-7e1758a0fdf2 | -3.47795 | -54.68478 | 2026-09-16 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e34d838-52be-3f77-bf6a-eed583fc7467 | -3.7637 | -59.38987 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 473c10ae-2415-3992-aba4-f6c64e2c8627 | -3.70778 | -60.61995 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1611f7b6-3763-3836-9fe1-e1d6df39603c | -5.13012 | -55.93518 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c30b963-29a0-3edc-8f18-288b87303daa | -4.6063 | -55.70489 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b21d4a64-7e40-36aa-977a-f9b852b90484 | -5.13862 | -55.93156 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b70904ab-4294-33d1-9d1b-f1cc0d763e2e | -3.07569 | -51.2027 | 2026-09-16 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ceecaa3d-b027-32bb-8d6d-33034a13e4f3 | -3.17323 | -53.92828 | 2026-09-16 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95758cf4-ef44-3ffd-923f-116fa8433429 | -3.44104 | -50.65937 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf562887-8e6c-34e9-aae9-a4645c50004d | -3.31275 | -57.883 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bacd2fe0-2728-3a68-99ba-9204e7f66d4b | -2.74615 | -57.61734 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README53.md)
