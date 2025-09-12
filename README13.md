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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97a08f99-036a-3ceb-ae6b-19c28f74da9f | -19.2409 | -48.0265 | 2025-09-12 03:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| f5c5eacc-6a41-3aec-aefd-42a196e68b40 | -21.9679 | -47.5525 | 2025-09-12 03:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 053a90f6-b9d3-38cc-970b-7b066e447a84 | -14.1713 | -46.2045 | 2025-09-12 03:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 8933b4f9-21d7-3a23-b6ce-326ab5253627 | -12.9101 | -54.7558 | 2025-09-12 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3d0c7017-076d-3c0b-bf79-935d55664e23 | -9.3017 | -65.5959 | 2025-09-12 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4ddf2305-f72e-3907-8a30-4c097f73f7b6 | -20.2681 | -42.1278 | 2025-09-12 03:00:00 | GOES-19 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.6 |
| e39c0a49-53d2-330d-8beb-93d27b21e4ae | -6.1672 | -47.2858 | 2025-09-12 03:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 83be0940-0ebe-3797-bde2-234a6f1bcf9b | -11.9211 | -50.7009 | 2025-09-12 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| f9e970b2-bb1d-36db-af9c-0b930b7f96fa | -21.947 | -47.5578 | 2025-09-12 03:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 05d4bee6-5b67-3dbc-98b5-b171702acfca | -9.283 | -65.6152 | 2025-09-12 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 090a8c5f-0e40-30b9-8df4-ab6776f524f0 | -11.9402 | -50.6987 | 2025-09-12 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 35c47f0a-5b26-31ab-bdca-fc6c6f519db2 | -11.5235 | -50.5968 | 2025-09-12 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 328532a3-444b-3a95-bbd3-9e158580a323 | -14.3362 | -54.1242 | 2025-09-12 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 290b3b31-09ce-332a-a80b-ef9d6b5a76e8 | -9.2831 | -65.5965 | 2025-09-12 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d0cf0058-a6f2-3064-896d-e7512acc1e9d | -21.9478 | -47.534 | 2025-09-12 03:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 34af9372-f2d5-34c8-b699-6d2b72efd7c9 | -14.1907 | -46.2012 | 2025-09-12 03:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 9d42ea27-6e13-3bea-97b8-da560f4a2cff | -12.9292 | -54.7538 | 2025-09-12 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 48e19153-11fd-3eab-8e8f-7ef8f84afcd8 | -13.8983 | -48.2581 | 2025-09-12 03:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 3eabcd32-e50d-301c-b6dd-bac3906e5433 | -13.9177 | -48.2552 | 2025-09-12 03:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 3cc0a5de-3e7a-3c70-999f-ba7fa5053a1e | -11.8757 | -58.8221 | 2025-09-12 03:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 7f70032c-7991-3fc2-a0ac-9e2005e49d23 | -12.9101 | -54.7558 | 2025-09-12 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b2593f58-2d1c-320a-bcbd-cc000003643a | -13.9177 | -48.2552 | 2025-09-12 03:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 94b075df-b2a2-3798-8e98-734d625b4659 | -21.947 | -47.5578 | 2025-09-12 03:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 07b2c895-380c-35cf-80ca-a8211b8ffaa8 | -11.9211 | -50.7009 | 2025-09-12 03:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 668a2c29-6088-380d-881b-6ba124ca1cee | -9.2831 | -65.5965 | 2025-09-12 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 49cd0c3e-9164-3cf4-a494-074fe157c4a5 | -11.9402 | -50.6987 | 2025-09-12 03:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1f8e6939-e8f4-35d8-8fd1-3645ab8df048 | -11.7322 | -50.6158 | 2025-09-12 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 14fadf5e-2b7c-3849-9375-190363b80ddd | -11.8757 | -58.8221 | 2025-09-12 03:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| d0f46be2-a60d-3db2-a3f3-267796a1497c | -12.9292 | -54.7538 | 2025-09-12 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| dee1210c-9eb3-38c6-9228-fcb4d62641c0 | -11.79 | -50.5664 | 2025-09-12 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 9c02ee13-064e-375e-8494-a4d834222829 | -11.5235 | -50.5968 | 2025-09-12 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e0c2ee15-9393-3831-ad86-4e4beb0f412e | -13.8983 | -48.2581 | 2025-09-12 03:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 38d6cf2d-67df-3876-9ea7-4af4db2068dd | -9.3017 | -65.5959 | 2025-09-12 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a70211f7-8cf4-3c1e-b2ed-7f7a91d3d625 | -21.9478 | -47.534 | 2025-09-12 03:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 49f21936-8fff-3e35-a956-4b4f417131c2 | -12.0852 | -47.5842 | 2025-09-12 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 6ef35a9f-be8d-34a2-85b5-887f50018981 | -12.0849 | -47.6065 | 2025-09-12 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| a6c47607-59b6-39be-92ca-523b15cd067a | -11.809 | -50.5642 | 2025-09-12 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a342bad5-981c-34f7-b74e-5b834c40c514 | -21.9679 | -47.5525 | 2025-09-12 03:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 0bc12757-81e6-30f0-8c1b-801f40847d18 | -21.9679 | -47.5525 | 2025-09-12 03:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e4739db6-bb3f-3c55-b959-434c9721559d | -11.7322 | -50.6158 | 2025-09-12 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 08551078-e9b1-3b49-9b57-52062309827b | -12.9292 | -54.7538 | 2025-09-12 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 0ff2269b-92f3-3bde-988b-76826da7fa45 | -21.947 | -47.5578 | 2025-09-12 03:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 8e37fcc4-b4b0-3aeb-9fd9-f076b628c9a3 | -6.1672 | -47.2858 | 2025-09-12 03:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4c02d8ec-d74c-37fc-9974-fb27ff315682 | -6.1674 | -47.2638 | 2025-09-12 03:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 408ef657-5675-32ed-a3cc-bda8e635caa8 | -11.5235 | -50.5968 | 2025-09-12 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8af96965-a956-36fa-9863-63b1f04891b2 | -9.057 | -47.0355 | 2025-09-12 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 2c4adc90-eb77-3a6d-876a-44ef56ff9ca6 | -12.0852 | -47.5842 | 2025-09-12 03:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 330fc13b-b795-3265-9161-2bc58923d3ac | -12.0849 | -47.6065 | 2025-09-12 03:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 8c737413-c645-34ed-b1be-84d407d83528 | -12.9098 | -54.7763 | 2025-09-12 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 3afe0709-fa15-35e0-9da0-128bf0e80f27 | -10.8781 | -45.5826 | 2025-09-12 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| c8717ce9-9e29-3724-9e04-0a70a3aeb737 | -11.5266 | -50.3826 | 2025-09-12 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 4ef6c5c2-6ef9-3675-a710-08dab5708bbd | -12.9289 | -54.7744 | 2025-09-12 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| a8d4d4ae-46a3-3c5d-a1a6-31ae2cffdd56 | -12.9292 | -54.7538 | 2025-09-12 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 210.0 |
| f7f0354e-78cd-3c90-95d8-4025c159b3cc | -11.5263 | -50.404 | 2025-09-12 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 4e34eede-eb7c-336b-b74d-0ec8a7d8eb61 | -21.947 | -47.5578 | 2025-09-12 03:30:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 90.5 |
| fc32fb70-7eee-3a3b-a6ef-82cd64a11bce | -12.9101 | -54.7558 | 2025-09-12 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| e3788d4a-ae19-3dbd-b673-a17588bc4694 | -22.7014 | -48.6852 | 2025-09-12 03:30:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 55d540f5-cd58-3341-bcd2-5bcd3b41e485 | -21.9679 | -47.5525 | 2025-09-12 03:30:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 97ce20fe-cca3-321a-a0d3-9876c5e8a44d | -12.9294 | -54.7333 | 2025-09-12 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 20aa7d8e-e5af-3584-9bd6-fe67fb2999d8 | -11.5235 | -50.5968 | 2025-09-12 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| fedf150b-c68d-304b-93a4-875109a4fd1a | -2.92945 | -40.41577 | 2025-09-12 03:34:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0f9f4d16-9cde-366b-b396-7293a6b43f11 | -3.69901 | -38.87282 | 2025-09-12 03:36:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 62091661-1df9-3e5e-a4b2-226c3df6ecc3 | -6.67236 | -44.15176 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c8f03de5-6720-3aa1-b69c-f885b494796c | -6.98875 | -35.15297 | 2025-09-12 03:36:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 1f7f8c20-9d32-3fd6-97ee-c7889a8b86fc | -6.82313 | -45.64723 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6f0f3fd8-b83f-380f-9e38-f5acad8e7845 | -6.41734 | -44.50634 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 523c3346-c11a-375b-b0f6-58c601493606 | -8.08213 | -42.5619 | 2025-09-12 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 63684b47-1838-34ba-8cf4-71d839fb2eaa | -6.48236 | -45.15409 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 927bfa3e-4ad6-3e70-a2ce-02fb5c15b3e8 | -6.48103 | -45.16113 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| fb40272e-50af-3a11-9424-a591374d9277 | -6.67943 | -44.15257 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4b55832a-4e8a-3e7a-a250-613d9ef87bc6 | -6.21245 | -43.37557 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e7cb1ef-4346-302e-8ce1-88b8f513212c | -6.12223 | -42.96125 | 2025-09-12 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4ee68d94-93b4-3612-b589-40f1389ed13d | -6.83173 | -45.65525 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2ab32612-20e9-3040-a238-b35b4c4101d2 | -4.43667 | -38.45596 | 2025-09-12 03:36:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c2e1ee35-152f-36bc-9e56-e0d2c7c27cd9 | -6.16694 | -43.5033 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6346d4e-8b05-3fa2-9c1a-46f2edc755b1 | -6.67927 | -44.14616 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a1d72b97-860f-3b61-9b1b-985b4a05a896 | -6.59432 | -41.44848 | 2025-09-12 03:36:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f8879c01-b1e0-3684-bfdc-15f296fd4f81 | -7.5225 | -44.68513 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ca35cb9a-9fe3-39d4-a002-c33b7809df64 | -7.44819 | -44.43423 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ad59d63-071f-3434-bc95-b44ec9a4c06c | -7.4019 | -44.36232 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ceaeb588-20bb-3606-b3df-2f079069f314 | -7.05364 | -44.69437 | 2025-09-12 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d44e2c03-38d9-3e12-ac22-27dc14c3bd80 | -6.56014 | -43.14698 | 2025-09-12 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f21adafa-47aa-3a20-8d05-70638178ca83 | -5.94914 | -42.79017 | 2025-09-12 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4a3ae20a-dc2f-370b-b159-ea3a4eb1cc72 | -6.17453 | -43.36565 | 2025-09-12 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c25a2fd3-2bef-3da2-ba6e-9da746bbde38 | -7.17803 | -44.87135 | 2025-09-12 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 401138b3-b39c-35ba-91d8-7015d3ba771d | -7.46798 | -45.29834 | 2025-09-12 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49cde13a-9130-3bf2-a2b0-0b9240926a60 | -5.94969 | -42.78693 | 2025-09-12 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 58f17494-c1a6-32f0-9f38-d6eac0aaa0d2 | -8.07199 | -42.95241 | 2025-09-12 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 20900735-af90-3fa1-8fe6-491084bf19c4 | -6.41353 | -42.60409 | 2025-09-12 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 30ade62e-ae38-32ad-bc9f-88ace15040ef | -7.73375 | -44.86439 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1e6ccd5-13d9-384a-881e-187a867947b1 | -6.59589 | -44.31403 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5195c39e-9f6d-32c6-b381-74f2b2bacdf6 | -6.81594 | -45.65109 | 2025-09-12 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8905262-503c-30ce-bb13-c8ccb0ff7e10 | -8.3685 | -44.83933 | 2025-09-12 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f3be7c2-140a-3802-9bf7-1248c919f1d3 | -6.76554 | -41.59785 | 2025-09-12 03:36:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 38482c8b-0276-3f9e-836d-e90b9805ad5f | -8.17717 | -46.10231 | 2025-09-12 03:36:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1aa6312-b945-33f5-988a-fb3d64186525 | -5.65783 | -45.94262 | 2025-09-12 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e79b170f-9949-39a1-a744-9f648264ca1b | -7.04768 | -44.69365 | 2025-09-12 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 013abcf4-03bc-3708-af64-325a4afc12e9 | -6.42248 | -44.51153 | 2025-09-12 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95166a90-245c-3f44-9dc2-61331213674b | -7.24234 | -44.47987 | 2025-09-12 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32031f85-7263-374c-bb93-e308d0e7c55a | -6.62544 | -44.08339 | 2025-09-12 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README14.md)
