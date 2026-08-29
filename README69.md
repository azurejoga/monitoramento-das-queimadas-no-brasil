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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a74f8089-32c7-36f4-995d-910dd2b0b1f1 | -9.43026 | -67.40981 | 2026-08-29 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00fc451b-f0cd-3ef7-bd53-f4de0fa0cb88 | -9.9199 | -60.42945 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b5fcf89-2518-3e6d-ad0f-f17e7806fee0 | -9.93164 | -60.43084 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b809869-e7f3-3b55-9bac-c6adea1b4911 | -9.51163 | -65.58365 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e17a21f1-3f4f-3b0b-a858-d6d53bfbcdc8 | -9.86417 | -65.02872 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ad5dcfe-87ad-3ad1-8a92-8ca7939094bb | -9.10227 | -68.62469 | 2026-08-29 06:14:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b23b1b3-44f5-38bd-b198-067463ecb7be | -8.37695 | -70.85213 | 2026-08-29 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43bd1b6d-0507-3007-83fe-e4a242ddd08b | -8.3465 | -70.85081 | 2026-08-29 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e902deb9-1cfe-30c8-a90c-f5ac8753b0fc | -7.0081 | -71.66083 | 2026-08-29 06:14:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2dc62f2d-8d66-33d9-b3a8-5a7a8b4c1ffa | -10.08282 | -62.3051 | 2026-08-29 06:14:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1adb83a-8fe2-3a2e-a8c5-dfd4e27b0b9b | -8.99078 | -65.43857 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7f075d1-f3ea-3717-a201-b7808bbd4176 | -9.51626 | -65.58053 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6b30c02-54b8-3d54-9251-81c870f23d38 | -9.86359 | -65.03277 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f9730ff-56a2-3e7f-940c-0666b481c467 | -8.94907 | -63.28393 | 2026-08-29 06:14:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c012be60-4459-30b3-adcc-f01db811fec8 | -9.20958 | -71.86019 | 2026-08-29 06:14:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee42d3d2-0a40-35d9-bc4e-962186869a7f | -9.0273 | -70.91355 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9150aae-a1be-3890-a2c4-243bcb352460 | -8.59765 | -70.20811 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c6de458-d860-376d-80af-c52de5f0dac2 | -7.55788 | -61.30795 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ccd0a8e-7a06-39e7-8710-f8ec2d6eafcc | -7.56368 | -61.30537 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 953a817e-a28c-3599-89b7-a2e9253b08d3 | -9.20378 | -67.77998 | 2026-08-29 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2c411e5-e66d-3b8e-be53-c1a1fd9a2d29 | -11.03569 | -57.22993 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c45683db-dd8d-37ed-b8eb-32066aafe3c6 | -8.94744 | -62.41349 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb7b7e2b-1a67-3336-a889-98632ff9bd7e | -9.50558 | -65.57988 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d35cbd4f-013e-3a0f-831a-68eef43d8e5f | -10.05341 | -68.83591 | 2026-08-29 06:14:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5311bc1-bfd3-3df7-ab73-8cad41ab07a0 | -7.98486 | -69.91059 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5f05359f-e816-33db-8f0c-ced605a6ab49 | -8.60597 | -70.21347 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d32fc1be-e7cf-3844-a063-535a1a3fb81a | -7.57503 | -61.38161 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f2933a3-1758-393b-bfef-1b0bebc3986a | -10.27641 | -68.86082 | 2026-08-29 06:14:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75165ad7-481e-3723-a5b8-346eab19b2b2 | -9.87159 | -65.03807 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d9a3f53-dd19-31b1-96fb-cebbcb661dd3 | -8.5982 | -70.20461 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81683209-f98f-3da1-a106-c2897c76bc22 | -8.99686 | -65.43629 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e1cf28a-05a5-3d30-9324-614b58fe0544 | -8.63459 | -66.54149 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1949e1e9-0523-33ca-9885-5d592238df8e | -10.48834 | -64.49793 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2790befb-46f1-32b4-8306-d03c014c8234 | -9.86845 | -65.02935 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64a9bbf5-e55d-38f0-b163-7a9d72057dbe | -6.7688 | -63.04863 | 2026-08-29 06:14:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4466d58-e9ae-3920-8cc2-d5e259d597d5 | -9.00157 | -65.45148 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| add4acbc-8933-3d04-ba26-f0add02d0eb5 | -6.76692 | -63.04644 | 2026-08-29 06:14:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2b6b312-699f-3ceb-a766-7924294cf510 | -10.50968 | -64.31065 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82457e09-c88a-37bc-a0ef-295ccdfd3d98 | -9.0651 | -65.41916 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6a3b9ad-0463-338e-a548-75e42302d8a4 | -7.82196 | -69.99606 | 2026-08-29 06:14:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4aff171b-655d-3711-b9ce-2272652b76d2 | -8.86374 | -70.6621 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7fdc751-0ef6-3d2f-a081-35c0fbf68728 | -7.00414 | -71.66389 | 2026-08-29 06:14:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42ff307e-e0c6-3e45-90da-04d65c972244 | -10.48 | -64.49216 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 0516b600-1e1a-33b1-86cb-405854384c53 | -8.99694 | -65.45455 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4e2e0e6-0b48-3385-8999-146c239062d7 | -9.09406 | -65.48018 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d886dff5-9fe8-339f-a6a4-f2cd5a3517e6 | -9.92524 | -60.43431 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16dec476-956c-36c8-bcbd-68e6d2a10ff7 | -9.86673 | -65.0415 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14704a2f-9da8-37ca-9dfc-f3d9fb329741 | -11.03007 | -57.22803 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ada3155d-23ff-3bfb-835a-261d7e120fa5 | -8.90255 | -71.39613 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1e990cd-4310-3679-9617-80f013ae5aaa | -10.55503 | -59.61532 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d8779d4-0917-3af4-a2af-2e551675c7cc | -8.60045 | -69.71072 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c7dafb7-4fa0-3602-9d8c-797a27936131 | -9.93699 | -60.43562 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58f78013-0dce-3cbe-ba34-578ca488d955 | -11.02851 | -57.22881 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d7cc6e2-c93f-3b53-8f5f-73ba29f2f435 | -7.55299 | -61.30379 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57346db6-3c65-3e0c-80ca-f0f4f60658ba | -8.99026 | -65.44227 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b8c91c6-8695-3f8e-858a-d44dc13a02b5 | -7.55253 | -61.30717 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9278d1c-f7d3-34dc-af62-086f4e78c7fd | -9.87127 | -60.30528 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f17d9199-8da9-3d6a-b6e3-0338d89eb22c | -8.22467 | -69.84039 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c72bf62-a035-3a26-bf18-288db848cd13 | -8.98342 | -65.44184 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 766ad869-6982-37f5-83be-badb8f6bc039 | -9.87759 | -65.02657 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 235b2ef1-ddde-39b8-88c3-8acd1cf4ceeb | -10.48773 | -64.50239 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e6a13477-fff0-39c9-a729-0bc17a41c023 | -11.04611 | -57.21536 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa69dc9c-2062-382e-a172-904535337861 | -6.92564 | -69.99332 | 2026-08-29 06:14:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9be67b4-a1c8-3b61-94b3-c9f5828530f0 | -10.56227 | -69.97289 | 2026-08-29 06:14:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32b01845-5a5b-3b69-b976-00d9bc49de32 | -7.58628 | -61.33937 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0608ec69-aed1-3a1a-9cc1-9f1ee0ec72c0 | -9.13657 | -61.01178 | 2026-08-29 06:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 061bd5fe-5429-30a4-8e6c-7b37f94be67f | -11.03744 | -57.21515 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e98e70d2-e3dc-38e8-8562-1a8e127bf448 | -8.99849 | -65.44349 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5a3fdfb-3550-3d24-a27e-3822063ce053 | -9.86302 | -65.03682 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adbb6cb9-f73d-32d7-9440-bc3a68a67c42 | -7.29885 | -72.84656 | 2026-08-29 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b7a2ca3-1225-36f2-9233-5d765defd5d4 | -8.63472 | -70.71867 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55b2d9c0-c617-33ba-a36e-b313f3e7855e | -8.95372 | -62.40535 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 255af792-bcb5-3bc0-a6c7-ac3cc0dd595c | -9.06617 | -65.41174 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbada4ee-27d5-3a41-9232-827e9c0960d0 | -8.93347 | -62.40245 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffdc30c2-459c-36ce-9d1a-f3d78c83d2cf | -8.98862 | -65.43507 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e51b7022-e47a-3854-a51f-b08c8977e414 | -8.9523 | -62.37805 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2835baa8-d37b-363c-b1b0-6c1ac3598355 | -9.08995 | -65.4796 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1377b8a-1f91-390d-b140-d4b61ebd9406 | -9.04592 | -65.43534 | 2026-08-29 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30d9fe70-e88f-38ee-b38e-64e9a6ac00b6 | -7.48192 | -61.40471 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ea423ee-0cab-3a2f-bdf2-8b41c96d290c | -11.0381 | -57.22162 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed2caaf4-27ae-320e-8a64-8464a8d8e76f | -8.34705 | -70.84732 | 2026-08-29 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3304494-dccd-3568-8b44-59f6d8576545 | -7.56323 | -61.30873 | 2026-08-29 06:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97c81c5a-db23-3ea4-933b-ce48f92a92fd | -8.95291 | -62.41127 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3ba0749-d0d2-3d24-96d3-d320bc7cd93d | -9.92419 | -60.4426 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78e9ab4b-5301-3d73-800d-8a5c532f9835 | -10.51213 | -59.62351 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6b9db38-8f1b-3ed7-997c-e96f02cb934e | -9.93112 | -60.43497 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0d473b8-f8f6-368c-a239-bd55667782ff | -11.03091 | -57.22056 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b68a3f6c-065c-37cb-a1ed-ca328cefcdb8 | -11.02939 | -57.22139 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43b734d0-db36-30ed-ba6c-a580c79a2e20 | -10.50527 | -59.62783 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a32371b0-e8d7-3ace-ba6f-0a62b801587a | -8.24562 | -70.09894 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad71773c-c6e6-35fa-b1a6-8affdb306ab9 | -10.39228 | -61.24211 | 2026-08-29 06:14:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 671fc5f6-44a0-30b5-88f5-9564d50719cc | -8.95108 | -62.38693 | 2026-08-29 06:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2dc2901-0423-379b-b35a-e08365c38052 | -10.50916 | -59.62926 | 2026-08-29 06:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52f40629-5d28-37a7-b080-92178be19908 | -11.03725 | -57.2292 | 2026-08-29 06:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2803d806-307c-3162-b9ec-1be4e1e2b057 | -6.76949 | -63.0437 | 2026-08-29 06:14:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58e1764b-c134-3454-90c5-25d0f8cd03ba | -9.86903 | -65.02528 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33785d30-3bc4-39c8-988d-be6d1d65da96 | -10.50511 | -64.3102 | 2026-08-29 06:14:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b4c0b99-8648-3afa-ad6b-6218d707742f | -9.09881 | -68.62415 | 2026-08-29 06:14:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7479cf3a-389e-3203-8e6b-3012db0cbf05 | -8.96031 | -70.71311 | 2026-08-29 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 373f6da0-dc24-34f7-ba9d-ba5520da0770 | -9.50612 | -65.57619 | 2026-08-29 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README70.md)
