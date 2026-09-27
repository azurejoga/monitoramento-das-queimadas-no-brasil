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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99cff404-ae80-3a0b-bfa4-740661d29486 | -12.13867 | -50.3345 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f9f24fb-e6ab-39c9-a199-607de80dc094 | -10.81928 | -60.73657 | 2026-09-27 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 238f8e5b-24b8-3bcd-874a-85a61ab544b1 | -12.67015 | -54.64278 | 2026-09-27 05:29:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01a2486b-befc-301c-8cd5-b45ebc46c2e2 | -12.70594 | -47.31684 | 2026-09-27 05:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88dd131d-b629-3c4f-88e2-0d10276873b9 | -9.08307 | -49.874 | 2026-09-27 05:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a49ef38-d28d-37a4-a43f-f464bda913d2 | -10.40809 | -53.80907 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b6d5a307-b08f-39be-85db-aec626beaa73 | -6.86694 | -59.87596 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 462a8fef-3dc5-3605-8e0c-fb4e606c9217 | -11.87644 | -50.52074 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3b6e6ad-ea68-3f24-bd9b-6feaed85a6bc | -11.88323 | -50.50945 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 82d600d6-112a-3b33-9fc6-21fa051b348f | -10.45415 | -61.30929 | 2026-09-27 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e64501fa-6993-3b9c-bb10-6c875f22f694 | -11.94828 | -50.57336 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59efb6d2-71ff-3f11-8e8f-809e53a4ee6f | -12.29705 | -50.27576 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3f1e26b-dfcb-3bc6-9e7c-abca3a2fe475 | -11.88744 | -50.52111 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d858be66-0086-32a4-9628-87ff6d7aace8 | -11.99193 | -57.60371 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dde1c45-6628-3a43-8656-2963a05a8e04 | -11.8539 | -50.52145 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a56cd58e-6c21-3138-9678-a30f285bc565 | -11.88919 | -50.50653 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0ef631d4-1cfc-39da-8c56-c7fb394e9d91 | -10.01811 | -50.15673 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f2d9d91-e0fe-3ac3-b07c-249a953b063d | -11.94367 | -50.56542 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07168e12-c421-3df1-98b1-ce135ae3ccae | -11.82258 | -50.50256 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7cc6327-ad99-3890-a454-32ea4065ef9e | -12.27734 | -50.29654 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c6b1b1b5-d535-31cd-8215-ca1189e75db5 | -10.01859 | -50.15311 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c80289a2-f4d3-3374-95ff-2e0c789a5e5a | -12.24239 | -50.37099 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 248dc435-4f97-3ad6-90da-0e942c9af91e | -11.98485 | -57.60266 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13b8c70d-133d-3fb3-8632-041868802d2f | -9.31658 | -47.6319 | 2026-09-27 05:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dcab3f3-448a-34c0-82f2-186c1cb686d7 | -12.23631 | -50.37403 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8df9549-58f9-3818-ba51-be3371f6b73b | -11.05028 | -51.32397 | 2026-09-27 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 358ffe9e-f556-33d2-9df0-9da3a06057dd | -12.12545 | -50.30193 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f03395ec-5ef2-31dc-b843-e361970bd805 | -13.71562 | -48.81099 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 068c81c0-b322-36fb-ab90-212b1dff7f47 | -12.70435 | -47.31688 | 2026-09-27 05:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c1540881-90fd-3898-b656-38ad32650179 | -10.01907 | -50.14843 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 769f6ed7-e710-3b8c-8ddc-ec7cfa838068 | -12.03476 | -50.59254 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 66a20662-fe31-33e1-a4e3-7e3f959859ac | -11.77396 | -51.0247 | 2026-09-27 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 353c328a-eca9-3e22-9faa-856dfb1c705d | -11.96153 | -50.51231 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38342347-0cea-3ba4-b343-db45e46e2573 | -11.02834 | -54.04002 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08e37375-816b-3c1c-a5bf-8a958664816c | -11.93613 | -50.49042 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| cdc8d64d-ea66-3dde-9752-c50ed7c791b8 | -11.24438 | -49.84735 | 2026-09-27 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 494b1fa7-7120-3b9b-9597-9f380856d719 | -11.85436 | -50.51783 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9fae7cdd-edb6-3595-b472-0587526787de | -6.69662 | -59.96435 | 2026-09-27 05:29:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c67ac295-5726-368f-9fb7-23e578b420f8 | -10.25038 | -59.12635 | 2026-09-27 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9822835-e590-3a28-8c7c-a3a5c91d3456 | -12.26278 | -50.68973 | 2026-09-27 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fe5e3161-a7b9-34a2-ad28-eeb228344318 | -11.76947 | -51.01728 | 2026-09-27 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2ab8b2e-c9db-3808-8d6c-236790f15b42 | -12.21296 | -50.37868 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec9104b2-06d8-388d-aba2-f5548fde8ff6 | -11.93568 | -50.49408 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d9c3632e-ca21-39e4-bffc-cb3986bf1703 | -11.93523 | -50.49774 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 537205ea-08d0-34eb-b460-f43055fbe484 | -12.2853 | -50.27814 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 2fbd203d-da9c-3f5f-b18c-76f30ab75149 | -11.89937 | -50.51529 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 465fa6c9-c3a8-39d5-b312-e8f80bdc634c | -12.67799 | -47.32012 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f065e6f6-dd05-32af-b70b-9a9bafabf4aa | -11.89848 | -50.52258 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b238aa3-405d-37ee-8095-edd90e3282db | -11.85531 | -50.55479 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 700dbf24-f3cf-30f4-997d-7a3b82db8390 | -11.24389 | -49.85134 | 2026-09-27 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7fdc02f7-cb92-399f-9b7e-52d795f21ead | -12.2564 | -50.69619 | 2026-09-27 05:29:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c7ab70e9-2202-39a0-b3dc-af8cf5745d50 | -10.01998 | -50.1412 | 2026-09-27 05:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3ab0d0b-56ad-3fb2-93bb-a24733f0933c | -9.63804 | -55.13579 | 2026-09-27 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc8f799f-40bf-3d62-a2af-934381ba9214 | -9.31785 | -47.63308 | 2026-09-27 05:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e709f4f-3e7b-34bb-8524-ea71ceddc922 | -10.03899 | -62.45643 | 2026-09-27 05:29:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b11856de-c67b-30bb-8291-0f73fa60adc4 | -9.59664 | -66.13538 | 2026-09-27 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb3f37cf-9d80-3ca5-a9e0-9b4595925001 | -12.02792 | -50.60266 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9a5ce963-0e35-398f-87ff-9adea1b3e91b | -10.81651 | -60.73246 | 2026-09-27 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d96e4fa4-a144-3272-8353-d0c90a7e641d | -11.89899 | -50.51997 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4db83a0f-34d4-3839-9b97-b27ad0b0c468 | -11.03264 | -54.04056 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55435407-66d3-3072-b6c7-eb6b5c6d948a | -11.94031 | -50.50211 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b7e8eaa0-8712-331d-a80f-55abe02d454c | -11.88381 | -50.50691 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3ef7a153-9c2a-3845-a716-f4d66ac5899c | -13.87559 | -49.03779 | 2026-09-27 05:29:00 | NPP-375D | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a1aa73c8-bad9-34d7-8cfe-5539eb3b2a54 | -6.88372 | -55.55634 | 2026-09-27 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71c1e2da-9691-3d06-9521-01107807ef5a | -6.86973 | -59.88004 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 338f212f-7929-3211-b451-a31027487dae | -12.2947 | -50.29492 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d5667cf-41d7-32fe-9893-1c618e8f0385 | -14.11814 | -46.32313 | 2026-09-27 05:29:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1ae701c-c4aa-3aca-b508-688c0c8044c3 | -12.02881 | -50.59543 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 9a5672fa-df61-3fec-acd6-02ce4dc1e98a | -10.24982 | -59.12988 | 2026-09-27 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f41ca8ca-7053-31cb-9753-b3bbd9de4291 | -12.67097 | -47.30681 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1550df7-91c4-3db2-9de4-828342a0ed02 | -10.02123 | -52.09679 | 2026-09-27 05:29:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42b4b2a3-9b97-3a32-ad47-88a4d7287590 | -12.17049 | -56.54594 | 2026-09-27 05:29:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2773ce5-7c51-37f7-8b99-b03e53c668cb | -12.28953 | -50.29036 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c37c35f4-7876-35b4-b7f4-1eeb40895909 | -6.63896 | -59.94795 | 2026-09-27 05:29:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f7ff473-d5a3-3df0-a75a-e04b8de9519f | -9.35776 | -65.74885 | 2026-09-27 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29e525c6-d484-366e-961e-e3fb8c8a5169 | -10.67691 | -57.63458 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4281819f-3b4f-3b95-aaf8-b39124d8cf78 | -11.89804 | -50.52623 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29daa1e1-7a89-3c7c-a97c-d70bed17fcaf | -12.28538 | -50.37093 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72d014ec-120d-3d01-aa72-51dcc7b03f6d | -11.2782 | -54.43678 | 2026-09-27 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| deb068f5-f21d-3af0-8074-f9564fc741f3 | -12.3055 | -50.30022 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 95e43a96-f0b8-3b02-b2a0-6b28b7d46446 | -11.89487 | -50.50835 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f7000599-4e7d-3458-a855-fcdeb6dc4ff2 | -11.24283 | -49.85297 | 2026-09-27 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86a0aa4e-f0ef-3823-ac61-c20e5a31b3d7 | -9.57152 | -62.70073 | 2026-09-27 05:29:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e188f3b1-d051-3c45-9b9b-2e1ae7b09bec | -12.23679 | -50.37028 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6fd4a60-d96a-3f3c-9b15-059e0a28232c | -10.45014 | -61.31247 | 2026-09-27 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3e8e74b-d068-325c-b3d1-d7d2f41c4d90 | -11.98363 | -50.5596 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 127c2d31-242d-36a1-8328-4b1bc8dfada2 | -12.05128 | -50.59471 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85a27f7c-cac2-36fe-9fa5-0e38696749bc | -10.67342 | -57.63405 | 2026-09-27 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 610c8a80-dcd0-3d58-83ac-0a843a778846 | -9.64268 | -55.13144 | 2026-09-27 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef8a10ab-f062-3359-ae7e-41cddf50db13 | -10.24704 | -59.1258 | 2026-09-27 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0051f02-1457-3f68-87c4-f674bde17371 | -12.02286 | -50.59834 | 2026-09-27 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 55bd784f-46bc-367f-8ad7-b930b776124c | -12.66507 | -47.31182 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 451222e9-3041-3d60-881f-6a5fe857a842 | -13.09931 | -47.42155 | 2026-09-27 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a9789e9-6f5a-32cf-a4c1-6ea3416ebabf | -6.87567 | -55.55958 | 2026-09-27 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d91a4222-6096-3011-a5b3-c8ca921118dd | -6.8717 | -55.58566 | 2026-09-27 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b845c8c-74c9-33f4-8d78-f2cbcf57778b | -6.87699 | -59.87758 | 2026-09-27 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ead331ca-8eff-36f9-b023-fab007592460 | -8.33525 | -62.85933 | 2026-09-27 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d54bef2-6fbf-38fb-b87f-e7aaeb332b59 | -10.31463 | -54.26465 | 2026-09-27 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a359abe0-7641-333e-abc0-1e96a57794af | -13.37975 | -51.31702 | 2026-09-27 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 896c66f1-29e8-302e-bfef-d03f69fdbaee | -8.59693 | -54.64772 | 2026-09-27 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README46.md)
