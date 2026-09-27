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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34e8c233-02fc-3440-a1c2-4c38a45fcd08 | -1.21636 | -54.56232 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fab2e729-5e32-3ecc-b4e3-dd05e13ceea8 | -3.88963 | -51.96006 | 2026-09-27 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce3056f4-1bf1-33ef-bbf8-bf5f759d4e49 | -3.83984 | -55.91288 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f1e7939-1ab2-3b1f-ae19-9ce544a444a1 | -1.33825 | -55.47688 | 2026-09-27 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9332b88-731d-330c-9bdc-b31728bc5311 | -5.7349 | -45.02712 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c4eff30d-a446-358f-b94e-2bff535763e9 | -4.36178 | -55.27574 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a597fa8-a6ee-31ae-811b-89f710ed2df7 | -3.84474 | -50.6429 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 912b021d-9af3-3091-bcf7-0dd349a07d1a | -2.73913 | -49.46353 | 2026-09-27 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a32f5f39-c5a1-323c-a8f7-c2daf46af752 | -6.09152 | -57.63246 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5185d0c1-18be-32d4-8bab-5f07927b7100 | -1.61993 | -55.10627 | 2026-09-27 05:27:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8301498-c1e9-3dda-a462-b6d783f47884 | -6.28205 | -53.38319 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d94f214-ae95-3d04-a98b-c7e90acb4971 | -6.09208 | -57.62888 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36a4f701-5fb7-39a8-a73d-0cf8afe154c1 | -2.06157 | -56.87217 | 2026-09-27 05:27:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25397904-dd7b-35e6-9fec-54badcd657b8 | -2.89236 | -54.19345 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 167a6985-8bd2-3870-9b9b-357c6ebd3db4 | -3.2257 | -54.32895 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22d08001-594b-31c8-9868-ea4352fe3e62 | -3.97019 | -59.34641 | 2026-09-27 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bfb8e75-fddf-3128-a324-f1d8f9c460ec | -0.50381 | -49.14055 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b9e86c3-c2df-393e-b89d-bc81c85e9af4 | -2.49786 | -56.14011 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f3967a9-8c31-3f54-b86c-d7cb2e43c790 | -1.2212 | -54.22272 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9529ed62-78cf-3e87-a1e6-c27b84c2d451 | -0.50428 | -49.13754 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6fb50bf-a575-34e1-ba1c-43266185fb1a | -2.57373 | -54.03419 | 2026-09-27 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d941abd4-f7d6-3fe9-a559-5992c56521de | -6.06368 | -57.81063 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e48510d-3340-303e-bb1d-d06f71b17ac6 | -4.14809 | -48.21741 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46439844-c38f-3d53-a76a-2ffcdbab672c | -4.4955 | -54.9424 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 459a481e-f1f7-3cc6-9bfc-0f40a0e7c4e1 | -3.85165 | -49.13623 | 2026-09-27 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4fd0f21-4bbe-3a75-893b-352bff805549 | -3.96441 | -56.12802 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aefd00d8-bf93-362a-a433-ea3c8f230ea6 | -4.44448 | -55.02793 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7abc2859-132b-3305-9c76-46b13f3b46fb | -4.55352 | -54.94466 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c3d5b96-30c4-3041-87f1-c4c26e4c8b7f | -4.2552 | -51.05367 | 2026-09-27 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a7dfdfd-2e04-335f-8a54-318eb209f57e | -2.92846 | -45.5075 | 2026-09-27 05:27:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01e79195-5ccd-3f14-a93c-a520315a5451 | -2.66726 | -56.45885 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62f03769-ddf4-3d32-8e43-126035078312 | -6.13195 | -53.05664 | 2026-09-27 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e63112e-01cb-303d-822e-b2bf0d50172f | -3.00847 | -54.21436 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 235510d6-dff0-3410-8c1c-81d2f75ee592 | -5.47787 | -48.57869 | 2026-09-27 05:27:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74509161-3c96-3046-b3e7-38c4a36f0431 | -3.00919 | -54.2098 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34b53eab-587d-3be2-99b0-5b0e81c605f2 | -6.14048 | -53.05795 | 2026-09-27 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2def73b-06f4-3703-882f-a532f4dfacd6 | -3.96509 | -50.71778 | 2026-09-27 05:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5113cb76-e8b0-3262-9683-5bbfe1657810 | -2.73865 | -49.46664 | 2026-09-27 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9461c807-765d-3363-9081-59d30c0762f6 | -5.73844 | -45.01752 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fef2db8c-ba3d-39e3-a6b6-c49d5b5b5cb9 | -6.0704 | -57.81169 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6400e3a9-b77b-3181-9ef8-5a831a13c0a3 | -3.8519 | -55.81085 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26d8f355-069d-3ece-a9d4-99bbc12d4bb9 | -6.09601 | -57.62584 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5866213-6fc6-3a66-a0c5-54ab37836778 | -4.49785 | -54.95168 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96411f3d-b980-3b55-8fad-7a0275095576 | -6.06762 | -57.82943 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc98051e-8ece-35de-8167-3d054599c71e | -2.50793 | -56.22821 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61d17cd4-7574-3c05-a800-387a71838dd2 | -4.51965 | -54.98198 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2498c67-892c-3534-b604-6e3bf1461b55 | -4.29463 | -55.24989 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4397129d-062b-3a57-94a8-c48f743c0739 | -6.09264 | -57.6253 | 2026-09-27 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6f6a5e5-a0f7-3ac0-acea-97f1840ea038 | -2.9474 | -57.71563 | 2026-09-27 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b6afd91-7f97-3933-bca2-1a16436bf269 | -1.62476 | -55.16816 | 2026-09-27 05:27:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fe1c723-7ec2-3e4c-9d0e-790c0a8ba37f | -2.94795 | -57.71215 | 2026-09-27 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 719c9f64-2747-381e-85ab-718c32086f71 | -1.05473 | -53.58149 | 2026-09-27 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afcfb5a5-3710-3aa9-b8c8-c271e9509512 | -1.61957 | -54.92072 | 2026-09-27 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ec361c4-59e5-3eb3-851f-b8c0e3b8b90a | -3.41413 | -50.42306 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3371c81e-0358-356a-ba34-a1511a4c45d2 | -3.01586 | -52.49451 | 2026-09-27 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a6f7db0-3d16-38ad-9d23-8dedb630f677 | -4.5458 | -54.97044 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8830501-2503-382d-8b11-f613ebde7a45 | -4.9803 | -56.15544 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce11663c-2193-39c0-98cc-6075a9a9e689 | -3.54322 | -52.45245 | 2026-09-27 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 399636fb-58c7-31a8-8b53-89b5e7d66afd | -3.30113 | -54.68964 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97baec8c-7fc6-3439-9860-3c892e51b650 | -4.36416 | -55.28458 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0dd331e-caaf-3471-a1e3-429f2d3df83b | -0.50475 | -49.13453 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b04fe1a6-92ee-3b47-a4c9-6e9c3a6e34bd | -3.84557 | -50.63741 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c46f6809-a84c-35ed-bc2b-346732801530 | -0.51035 | -49.13233 | 2026-09-27 05:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11b15a41-fc9d-3c8c-8c95-dd4f519f50ee | -3.22261 | -54.32383 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad6e194c-742c-34ff-be9e-0f954c9430a6 | -4.46227 | -55.03488 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9c33926-bbf9-34fd-b219-7ba3476f6a84 | -4.56836 | -54.94688 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a60bf9e6-0d5d-3197-8285-1b2106ead5ee | -3.4321 | -50.33655 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d48813e2-ca7f-3b98-a125-8c132c583b8c | -4.49416 | -54.95108 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 559a40e3-f844-3c9b-b23c-c20f4e718707 | -3.29676 | -54.69338 | 2026-09-27 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ba18064-88c3-3137-b7a1-f404fddb26ac | -5.84178 | -53.84661 | 2026-09-27 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 342ac67a-7433-3531-bc0c-170a98055423 | -2.97084 | -49.55929 | 2026-09-27 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3727767d-59cf-3566-9dd5-7749e54477fa | -5.1627 | -56.00123 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecf16ff1-19b2-344d-9965-0b629b1ca445 | -4.27154 | -55.42434 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63e8b8ca-8f6b-3f98-a964-aaae44851194 | -3.19602 | -51.03335 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2d1001c0-ff53-32f3-9c6e-2e550f3e6241 | -4.49852 | -54.94737 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cf640d3-1c69-3d68-be20-bbc47f05f456 | -3.94767 | -56.09803 | 2026-09-27 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd8c5c51-78bb-36eb-ac88-ae6345b70522 | -2.96521 | -49.5616 | 2026-09-27 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cab9773b-1a70-39e4-b15f-7cd94618767f | -3.00837 | -54.21174 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40021203-dc0a-3670-adef-d9d1bab9bd3e | -2.67067 | -56.45939 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d408145-0b44-3710-ab73-21794586b68b | -4.9802 | -56.15585 | 2026-09-27 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d99ebe00-30b7-327c-9284-16024cb2c7e8 | -3.96143 | -48.11855 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3861e01-792f-3170-8a40-f8577b2d6f9a | -4.47597 | -55.42804 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb1bcee6-8f67-3377-b2a2-b16ee5b8fbb8 | -3.87079 | -51.79713 | 2026-09-27 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab3cb1f4-f9dc-376b-98e9-bf41dda383db | -1.1492 | -54.09239 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46062623-1dd0-32e3-81db-b9d7ec8e0ba0 | -2.9245 | -54.15449 | 2026-09-27 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 788a5dd4-8092-3b18-9e1e-9ba209776a89 | -2.65794 | -56.45047 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8150b403-96d4-38ae-8763-60a7c8f78319 | -2.50851 | -56.22453 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4df97a63-68a7-39f3-85a7-02e3dfcad978 | -4.36478 | -55.28045 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a79b6d2-a019-3d84-a0dd-9fb8c95116a6 | -3.0287 | -57.86299 | 2026-09-27 05:27:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e66ec60-cc7f-376c-a44a-68a7d59a6119 | -1.34582 | -55.47415 | 2026-09-27 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34922000-ebfb-301c-a7ed-96fafce466f7 | -4.36353 | -55.28872 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 433f92c4-441c-3a67-9b9e-6b818f3e862c | -3.67697 | -50.84671 | 2026-09-27 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1e88dc9-709c-39de-9581-56a13c3d8160 | -5.73906 | -45.06768 | 2026-09-27 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f69f6f8d-3386-391c-adfa-e5e1e585c387 | -1.21543 | -54.54474 | 2026-09-27 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fb4d6ea-250d-33f3-a04c-30134e027c0f | -2.51422 | -56.23295 | 2026-09-27 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13e2e38c-e366-35a5-96fe-6020db1c13d1 | -4.51792 | -54.97946 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2448823d-0e72-3778-a4fe-b083eebfacf2 | -4.50155 | -54.95229 | 2026-09-27 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c97edd2-ab04-37da-b554-5cb88e585e7a | -3.96719 | -48.11958 | 2026-09-27 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59a38ca5-0813-3b2d-8358-faee9559c445 | -2.37452 | -50.40946 | 2026-09-27 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c1d6324-9e64-3590-a48c-b6e0be995e7d | -1.0568 | -53.58364 | 2026-09-27 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README43.md)
