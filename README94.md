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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 181d1681-f984-3563-9f5d-1af9cfcfd8a5 | -8.57727 | -46.32603 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5085bfee-9969-3afc-9a31-f676294dbae3 | -11.11369 | -49.86634 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9bb55ec-a63b-33c2-90d3-6bb7c7ec78ce | -11.80941 | -46.84502 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 636a257c-aed0-307a-b06a-873c584a56b2 | -10.84651 | -47.96783 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af5984ad-a8e4-3f19-aece-e36dafa5540f | -11.11761 | -47.21058 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c6cca8c-9c12-355c-aa4a-501d4d8d1323 | -8.58952 | -46.29804 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b9dec9ae-82df-3d6b-8c21-1be406e20ded | -13.23865 | -47.26414 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7353b6ed-af22-3765-b43b-6bc0cc802a2a | -12.97187 | -50.99566 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03f25a52-82ed-313e-b20a-63575d37337e | -10.8395 | -57.19203 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0cae33a-ce07-3904-91f0-3d4d7a974709 | -11.92916 | -46.41515 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 605a5361-cbf8-3090-8464-617635791e3f | -12.39318 | -51.10153 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9663f250-b497-3ca4-8da3-c6f4fa241b12 | -13.14981 | -50.92508 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b80b9013-e6ea-3aa4-9a75-6f2406e7c9b5 | -10.54544 | -47.79935 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3db9cdbd-d777-3a8f-bb1c-30eeed651a7c | -7.51394 | -41.27257 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| abc3f804-7805-3fc5-b683-be8dfc039e3f | -7.16194 | -44.99293 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0b1daf27-d81b-3c8a-aa86-a2a3cad4a4b6 | -13.25647 | -48.48002 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32dc8b88-72be-3bf9-b78c-d7edf48eb090 | -12.11693 | -50.89868 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38210c55-80c4-3a25-b325-9262b12a0dc3 | -13.33598 | -47.58406 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b075e67-61ad-3885-bfa8-0e84dbf0d3d0 | -12.81525 | -50.53647 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fa9fa9d0-31eb-3fdf-b996-75322871b755 | -7.45808 | -47.18028 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 295afb92-4990-3892-a4f5-ac1f5620ec88 | -11.07845 | -47.91367 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d9ac4c76-1fbd-3f68-81d9-c07d89c3e7b3 | -11.78502 | -47.92637 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4b863fc-afe5-37f5-8659-62a30df412b0 | -12.38758 | -51.09321 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a5ffd95-ddd4-3aee-8fd6-e30597d87ab8 | -13.31381 | -47.56665 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6a0bb56-a3f7-33c6-8aeb-ca65ad25a973 | -12.2324 | -47.8327 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ef5a0e9-bac1-37f2-a194-2d53a2778a3f | -13.70326 | -47.35782 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbf41178-8cce-3f8f-9df4-963864dbc961 | -6.71075 | -42.82487 | 2025-10-05 04:46:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9c6a5abd-b40a-3a31-86ff-bc1be6d0273c | -13.3096 | -47.62706 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3da446c1-e1d4-32c9-b5f0-d50d5a74825e | -11.86963 | -44.95477 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7edc824-98a2-392a-b0b8-b41a61aeadb0 | -7.16629 | -44.99363 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fea5d3d5-fc59-37c2-ab77-6083184dc88f | -10.46637 | -57.48769 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6198137-52ae-38b7-adfb-9226a6a659a4 | -11.53931 | -49.80484 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84df2fb1-8194-3c7a-801d-d62a58353f0a | -11.74581 | -46.81833 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03f6c6c8-fe7e-3ece-9f83-0bbb1f71064f | -11.51119 | -46.75088 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6428220-7534-3429-ba2a-29533ff4e580 | -8.52424 | -47.21531 | 2025-10-05 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d009d7dd-34f6-3690-83e9-98a06cc3824f | -8.56127 | -46.26496 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 44a21bc8-2280-3cec-af06-4bf5ae98ce0a | -8.53898 | -46.3322 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6ada6255-8523-3e5c-beec-2ecce7685843 | -8.90043 | -46.04686 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d2e28df-13f6-31df-8e4a-a0b17d86df59 | -12.65708 | -46.99362 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d897493-6c8a-3aff-967d-8379dbed7181 | -7.74448 | -42.52076 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 912efb0d-8b42-3145-91ac-b7f3665dd351 | -12.65299 | -46.99275 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60a6050c-ac31-30db-b076-b747c2436eb4 | -7.44031 | -46.51639 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc5b05e5-c094-35d0-9809-8976be5e2b4a | -13.33827 | -48.05769 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 874bd2fc-fc07-3fbe-8b40-00525b3d01a1 | -9.85038 | -60.27768 | 2025-10-05 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 845ad0de-f989-338f-af55-a905c9594b00 | -12.82213 | -46.86826 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cb25640-be6b-32df-85a6-5b2c729c2164 | -13.35108 | -47.57486 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d1e74e8-9cc4-373a-b8b8-660a8b3de291 | -8.60632 | -46.2677 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 304f8a0e-6c8f-36bf-9bf6-ab6f13f8401b | -13.07964 | -47.90105 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6fe7a869-da45-3661-9a43-077bf13accda | -10.46305 | -47.8093 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d95303de-a0da-3da0-899c-62155ce4e051 | -12.27341 | -55.132 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e239d7b-93e5-3acf-a1e5-8c57dcef2d41 | -11.70867 | -47.50629 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f3141159-b85a-37be-b8d0-bcd0d2294e90 | -11.24063 | -47.78201 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c68e82e4-0dd7-3b7a-8caa-c1394f3801cd | -10.71639 | -47.8518 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aae0572f-e068-3a6c-bc3a-240292e5e764 | -8.55584 | -46.27059 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 38d834ef-8075-377a-b111-ecb51d1868a3 | -11.01967 | -46.69414 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49d80d72-2079-3bfb-980e-3975eccc58c6 | -10.83734 | -57.18061 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e5ae7ab6-6ca0-33e5-953e-a8292ea256b8 | -5.61151 | -51.80861 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 323951eb-59f0-3bcb-900b-ab895d8c0e2c | -10.30036 | -47.9459 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dfb1cc9-69f1-3fab-80a5-6f853712da47 | -13.50579 | -47.28247 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc09799b-426e-3417-8472-18a200f43c0c | -10.6002 | -54.35764 | 2025-10-05 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae55d2f9-b796-35fd-9cbd-6c5709d0c61f | -9.3245 | -54.53262 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 767bb31f-f38e-3e87-a33f-bea0389e50b5 | -13.30607 | -48.1189 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb06dde4-2dd2-3742-83f2-f241d8d8e35b | -13.52137 | -47.29094 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 590ff5de-e9cf-3db0-91a0-9fbe5f227fcf | -10.35712 | -58.45529 | 2025-10-05 04:46:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93cd717c-3157-3781-9406-68b43e9b218c | -10.39418 | -45.40777 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f91c03d2-512f-3f5f-ab48-4a611f7600ce | -11.8199 | -45.04264 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fdd49473-7a2f-340c-b3d1-844948dc6c6a | -12.9641 | -51.02464 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e76160c-b1fd-3e0d-9343-15692dcdb5b5 | -11.48792 | -45.0423 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4cd8036-f7e8-3ca0-9e7e-5da074bf7e99 | -8.23755 | -46.80313 | 2025-10-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81aed4b3-22f7-345d-bda9-30040b42233b | -10.58843 | -48.69609 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9cc310c-4a01-362c-b4af-a2fea64ddf7f | -11.89699 | -44.98405 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23d010d5-e0d9-3dfd-8b22-bb62acfb0a9c | -13.43629 | -47.2757 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 25a46943-874a-3b01-9c7b-9bfa60139136 | -13.34551 | -47.57431 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d13b85e-b783-300d-8e74-492b89ccd8af | -10.82964 | -57.20126 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45af6288-4a5e-3d10-9b11-bacb12c0c484 | -11.48316 | -44.97039 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab37ac3a-a30e-3235-8d72-627dac0ed42e | -12.94937 | -51.01917 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be96ec5f-764f-3a17-9ac4-e31ba0886ee3 | -10.03503 | -62.46053 | 2025-10-05 04:46:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35eda2de-5206-320b-b786-0f4ccccb1029 | -11.54651 | -47.69185 | 2025-10-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6940965e-7b79-3af5-b9c3-9f9d39462edc | -11.81774 | -45.05907 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 383fcd31-ca37-3b1c-887a-aaf6cbe1cf61 | -13.30514 | -47.62989 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a80de370-40a4-3742-9f7d-8f856e9a71bb | -8.55028 | -46.31081 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a0d75111-61b3-335a-ac0e-4c5528be8bec | -11.53299 | -47.6749 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 277989ab-1dd4-39c5-8e01-e9b7a11fb7b5 | -11.07287 | -47.89801 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 234af425-57d4-373c-bddc-3ec40bd1f28d | -13.3454 | -48.06361 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e7bc12d-a925-3c9e-a10c-48be6c865cbb | -13.23205 | -47.34351 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8889c092-66a3-3ab4-af37-5af52cbac8b1 | -7.01844 | -42.30135 | 2025-10-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 33c1f24b-4f6a-3d99-b342-33bbaa1e876e | -7.75361 | -42.60905 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7a55968f-26be-3106-a47d-632f8ccefd0e | -10.9898 | -46.66659 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a084533d-e1d6-3742-b0e8-63190ebc8b72 | -8.7541 | -47.20425 | 2025-10-05 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9344e000-a62f-365b-abec-610aef9d7512 | -13.67807 | -43.18558 | 2025-10-05 04:46:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 144e35c5-c4c2-30ee-b097-ded1ecc86b0e | -7.43417 | -46.53127 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d2e7cd7-11cd-3908-a5e4-3703daaefa97 | -6.84164 | -45.48445 | 2025-10-05 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f22e92fe-fb14-3afb-bef6-05e63cd47a44 | -8.54004 | -46.32492 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94704db3-68f2-34a7-a523-1b2fb25ce205 | -13.35459 | -47.57923 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8288050f-8587-3413-afe5-86b6a3d1dfea | -11.05517 | -47.77275 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 054d93d4-b3e0-32a3-985b-512cd00cb600 | -7.43167 | -46.52038 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d95a3670-906b-3a5b-8913-667d4702febe | -12.97202 | -51.04097 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 973cc36d-df1f-347c-93a7-043128f73a52 | -8.18645 | -44.13711 | 2025-10-05 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b7914b87-123e-3edb-b8c6-26bf23059f67 | -9.25474 | -46.77654 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bf8aad43-121a-39de-8dbc-4380231e6a1d | -13.11648 | -47.9823 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README95.md)
