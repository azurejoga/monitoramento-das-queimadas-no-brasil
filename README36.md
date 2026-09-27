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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c51884b1-6a96-37e3-9e79-cfd40c09adaa | -11.8897 | -50.52139 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 297c7cb2-e957-31eb-90d0-2778c5f25fea | -14.82364 | -49.27002 | 2026-09-27 04:53:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08e5210b-bb19-3684-81ba-116d91416d8b | -12.29763 | -50.27629 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c9089b2-dc6e-39b5-a750-bc20050c64f5 | -11.95 | -50.56865 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b3e5d1ff-ac9d-3b8d-bf5c-5d2350a2a29b | -11.938 | -50.49509 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cc729cf7-46f8-30c1-9e37-9542fac1f8f5 | -11.88363 | -50.51152 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e835df9-ac71-36bf-9677-e47d925da408 | -12.27613 | -50.69208 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 881a19e5-bcfe-38bb-8435-7ffd95e32a2a | -11.87933 | -50.51536 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 009a87e8-9939-3737-a491-2977a28c58df | -10.41961 | -53.81622 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d49163dc-cd53-33ae-9fb9-e1b8572c6dda | -10.67134 | -57.55404 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14549172-7d26-346d-9068-91488167adbe | -11.99188 | -57.60715 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a82346d-e0ee-3cd2-9843-1a24d1a07678 | -12.659 | -47.29996 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03f9d3fd-65a0-3cd4-9b8a-d0e643ae04e2 | -14.06726 | -41.93308 | 2026-09-27 04:53:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a6e6cc1a-3ea7-33aa-a714-a6b4f72d37d2 | -10.42397 | -53.78833 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1184e34b-45da-3def-9e35-18bb8958ecbf | -12.2814 | -50.28322 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b276dc1-211b-32e0-a5e4-f3032c9b5684 | -10.25548 | -59.12688 | 2026-09-27 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf26ca6f-4cc2-3697-b50a-0bd197fa689a | -8.33369 | -62.85892 | 2026-09-27 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd10fa69-0f85-334c-a223-6b59fa21e110 | -11.03596 | -51.31351 | 2026-09-27 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b5210a9-d23a-33ff-9819-a48fef3a0f9c | -10.82494 | -57.2172 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35c3d2ab-bbf0-3ecc-b9bd-760add70dea8 | -10.41907 | -53.8197 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e40e09b3-c8ab-3ab2-9886-cf14af43bf38 | -12.20546 | -50.37644 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b06697bd-1b5f-37e3-b878-ea2d2ddaeb83 | -14.82264 | -49.27758 | 2026-09-27 04:53:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dae4c155-2a74-38e0-a348-b74f5b07aed4 | -12.28706 | -50.27005 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10ddc944-0444-3bde-ac1b-77927e053ba9 | -11.89387 | -50.51543 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c8c9b97-dd47-3fc3-bff6-aa18f1e907ab | -11.89631 | -50.52477 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dae3ae40-a408-3d0e-a0e0-4bed25734e76 | -12.70875 | -47.31803 | 2026-09-27 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36aa9b07-39e0-3a21-a710-90a33aa111d8 | -9.93382 | -60.71514 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d1caec0-1852-3fa7-b8d5-f91ab3e4202b | -10.01824 | -52.09936 | 2026-09-27 04:53:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec88d47b-a27b-3eb3-ae9c-d3c561623e39 | -12.66166 | -47.31476 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03cbcf9c-e867-3d7e-9be9-7c2df4fcd7b1 | -11.77561 | -51.00082 | 2026-09-27 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83d52a26-b81a-388b-93b9-a61b52fd1d8e | -12.66328 | -47.3116 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c2d53a7-9ba3-323a-a5e4-9c2766a6ade2 | -10.01911 | -50.14394 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15b4aba1-1f22-30e5-8698-2ae7d535c62d | -10.72621 | -53.99074 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1499f08c-d56d-3b2e-9db1-19605c3e6cf3 | -9.53427 | -62.26722 | 2026-09-27 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ae5ceb2-383b-3363-93f2-d3ce108acc6c | -12.8957 | -61.71635 | 2026-09-27 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96be8be6-6d44-3f27-b8a0-814f0640be77 | -11.92547 | -50.6095 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67a78b3c-89ee-3ea2-a9cf-2aa9740ef882 | -11.89448 | -50.51104 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c40083e-581c-3a51-9cfe-0e3c30a82533 | -10.82123 | -57.1946 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19f12cd3-c639-3002-a20c-49cc3b65bd5b | -14.53335 | -48.32331 | 2026-09-27 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c1e89d7-9d72-3940-9be0-2d309a3e132a | -10.81494 | -60.72934 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e72c758-8f64-3146-af74-3737657ec317 | -9.6426 | -55.13605 | 2026-09-27 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3516aa98-21cd-3013-84e4-24250ccf3b8a | -12.89478 | -61.72139 | 2026-09-27 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a98896e7-fa29-3d2a-8f8b-c07db91a3e01 | -14.353 | -52.12281 | 2026-09-27 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19d71421-3d8b-318c-b06c-c2c26bf6cf6b | -11.27195 | -54.43467 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 292d0080-1c53-317b-96db-19d7b242ee19 | -10.40695 | -53.81063 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7c45e819-e1e7-331c-a8bd-b71a79d29714 | -14.53276 | -48.32785 | 2026-09-27 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e60e3c15-ffb4-3627-9e24-deb4ee9b2246 | -15.68366 | -48.22282 | 2026-09-27 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23dc73a3-9702-3d5e-a1ed-08c00625e815 | -8.34052 | -62.85855 | 2026-09-27 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cdb6871-d376-3281-8f52-aedcd11998d8 | -14.80003 | -45.95904 | 2026-09-27 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 50c91068-2f60-37c4-8dc7-ddc12ccc74b5 | -14.41369 | -52.8046 | 2026-09-27 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c058b512-fd61-3210-9020-c99e9d27e0a7 | -11.60545 | -49.86438 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99d2e8c8-66db-3f6e-8290-08385406101a | -12.05079 | -50.5957 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e3019037-d9d0-32ac-b7a2-abc2adfa206e | -11.87566 | -50.51481 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 284b41e0-42a8-3b23-9ad6-ed5a96d0da76 | -13.10307 | -47.41541 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5d171f7-3acd-3efe-9a03-ebe652e2cd6a | -11.01944 | -54.049 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 78ae9ae3-4ba8-3c7d-8b26-4015478c2116 | -12.71784 | -47.31929 | 2026-09-27 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| adada3a9-8709-3bfc-9ff3-ca212682e324 | -10.82317 | -60.73552 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| fc2c8c66-62f9-34bb-83a3-f1c8813b5b0e | -12.27675 | -50.68773 | 2026-09-27 04:53:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c4f619f-0202-3fb3-bcc5-808f9e9a3520 | -11.01668 | -54.04498 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1ab2241-6ad4-3fac-8d0f-4328cc878991 | -11.88491 | -50.50274 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe2e47d1-d25c-3237-931b-8816110c4cd7 | -10.42237 | -53.82023 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e12870e-7d58-32a1-8f02-58f8964d1a2e | -12.29197 | -50.28946 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4326513a-ff15-38dd-9b0d-5f05c7c0d5d8 | -11.02714 | -54.04308 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aed0bdf9-013a-3294-bb21-7088e1ec9812 | -11.01999 | -54.04551 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb8f12ea-33b4-3065-b5ac-2ae5c96917ba | -12.28642 | -50.27462 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b5dd191-d050-35b0-b944-f5a5f3f6eb87 | -11.89289 | -50.49944 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0ea3274-6201-3962-ac46-c64d8ed15f7b | -10.41355 | -53.81168 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31ef37a4-7af2-3e7e-8d9d-04e4c2419122 | -13.87533 | -49.03802 | 2026-09-27 04:53:00 | NOAA-21 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8e1fafe-5f48-3b59-9d75-48438a145a1a | -12.1809 | -47.38177 | 2026-09-27 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d63e7002-9f45-360f-b385-2e88c8820ada | -13.2121 | -42.22739 | 2026-09-27 04:53:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f0c67f59-4456-38a3-854f-544380b0d87a | -15.47313 | -46.15271 | 2026-09-27 04:53:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a82a72b-ae1c-3a75-bdde-a4b5ee45b75c | -14.80039 | -45.95593 | 2026-09-27 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 479067fa-cc60-3270-9ae2-30dbfa66c225 | -10.67356 | -57.63284 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbf2406c-7f78-33d0-a0a7-5c9442a94a67 | -11.90121 | -50.51654 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7fb8a747-9e39-36b4-ae93-6ba559cfb8b7 | -10.24724 | -59.1256 | 2026-09-27 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b66638ca-5cbd-3b67-9aba-c2507127da61 | -11.03774 | -51.32588 | 2026-09-27 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 510a8b9e-bc33-3151-bdd0-cda5565a6bd0 | -12.23833 | -50.37416 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d96c7101-9d12-3086-adfd-04fe3d4e059c | -12.1428 | -50.32338 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ffa7245a-096f-35a3-9866-09df0521ea31 | -11.90135 | -50.51865 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfbb7c6e-b305-3b9a-aac2-aa8933fc021d | -11.89529 | -50.50877 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2726308c-051b-312e-84b8-d42d06ddefdf | -9.64318 | -55.13241 | 2026-09-27 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c420b503-c78d-3f14-906e-ba2dfb94fb8d | -10.4609 | -48.32364 | 2026-09-27 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b6ac579-4156-3246-8f3a-960e5df463c8 | -10.42125 | -53.80576 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6627afd-9308-357e-bf46-c4d6ec8d85e8 | -12.77189 | -52.81956 | 2026-09-27 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 496f2d8a-3f77-3ccf-825d-e855647c8472 | -11.2747 | -54.43872 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6bd12882-4ad4-3c0e-8e09-c5a0ee1de65e | -12.89944 | -61.72229 | 2026-09-27 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9235ef7f-e37f-37f3-b6de-8f2fad041651 | -12.72026 | -47.30067 | 2026-09-27 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0325f604-f505-3ab6-983c-adca09d3527f | -11.27801 | -54.43925 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 288a709f-b7b1-3d36-b5a7-e5351b898fe3 | -14.26143 | -52.78932 | 2026-09-27 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d0dc708-5abf-33b5-98ed-da191c5ed391 | -11.42155 | -47.42634 | 2026-09-27 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fdc4964-5343-3cfd-b9ff-625c5f37ce1c | -10.59314 | -48.71438 | 2026-09-27 04:53:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e72e400-ef3c-33a9-8206-ea3e234f1090 | -11.89832 | -50.51372 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff388632-3670-3022-8cf0-28c55db640e4 | -12.29453 | -50.27116 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 837ea120-cc60-336d-8b2e-79465678ef4b | -11.99275 | -57.60185 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a4f48d0-85fa-3de4-a6b9-0f7983f28c2c | -11.83582 | -50.86462 | 2026-09-27 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59b879f3-eb35-3cba-ba5f-a0080d05a563 | -11.94043 | -50.50444 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b95c460a-78a3-3384-bf27-a6d10ca58403 | -14.82314 | -49.2738 | 2026-09-27 04:53:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da8d99c8-0342-3821-91fc-094a7ccb5cb2 | -11.883 | -50.51591 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bac4b33-c69a-3b0f-9270-896e9f4ff5c5 | -12.04848 | -51.41046 | 2026-09-27 04:53:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2f5536d-ea59-3354-8224-7c401df0afa6 | -11.7744 | -51.00912 | 2026-09-27 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README37.md)
