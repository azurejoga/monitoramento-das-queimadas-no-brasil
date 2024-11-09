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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed21b28c-fe72-3480-a968-0ca27f0b26fc | -2.6296 | -54.65756 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dd16ba7-27f0-3417-b536-55870b987002 | -2.38683 | -46.77784 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f09b4f41-17ff-399d-bd8f-71931e6ce475 | -3.95312 | -48.16257 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 85e9f2a2-ff8c-3461-b0af-fb8c41d0f3ff | -2.25582 | -53.72683 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e45f8c0-c90c-3ed7-aa22-06c7863ea7e1 | -3.53257 | -50.33369 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a046023d-e5ff-3be3-b3e8-7dab4d6116a7 | -5.44579 | -44.82178 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e013c7f3-df7e-35d4-b972-cbcbc42401b7 | -1.38437 | -60.35197 | 2024-11-09 04:55:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9fef13b-c0f1-3d42-9834-8923f9bdafb7 | -2.35848 | -54.75607 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca76113d-a8d5-31c5-a6f2-41a51ee2837a | -3.3091 | -50.13943 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1cfb2cc-7aea-3b4e-80e1-64835048c9a0 | -2.29082 | -48.55044 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eaa41ec8-f9a2-3f1f-9d37-b354861bf43d | -3.58568 | -47.3492 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fcdb2b5c-717a-386a-aa40-17b7b5b7ea3b | -2.20927 | -50.77947 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10965f9d-7a32-30a8-8be6-d4288b4f9570 | -3.96554 | -48.16455 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79614313-ecc3-36ac-901f-ad2455e55d06 | -4.05926 | -46.94006 | 2024-11-09 04:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 484aac61-4a48-3f13-b16d-c4468e2ddc46 | -1.49663 | -52.555 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ecd10fb-60bc-3ec0-a3a6-dfb52996798d | -2.53403 | -47.30284 | 2024-11-09 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23cca991-ea3a-30fb-b386-2a4b544b107a | -3.55024 | -47.37754 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bad76cff-616a-3c5f-ab07-7b92ce3cc96b | -2.85001 | -51.36456 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de655278-825d-3179-9d14-4138598478ee | -2.61323 | -46.24328 | 2024-11-09 04:55:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc04cd6f-2f76-3d4b-ad48-28381d4a8fd3 | -2.26435 | -48.97876 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8287fe07-b27d-3944-9017-e98fdb110058 | -4.51868 | -45.69847 | 2024-11-09 04:55:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c658ed32-f09c-384a-a2a7-c6f9c0598bef | -3.27072 | -52.73889 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 626e3309-c7d0-3641-a0e3-24d34c784f1b | -1.76826 | -55.10617 | 2024-11-09 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af59394a-f699-3da6-aea8-ee984ac9b01b | -3.53625 | -49.25803 | 2024-11-09 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e965c9c0-290d-3d4b-81a9-db7e446b9c1e | -1.1604 | -53.65487 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d79ac2d-3bca-3743-aa91-2c755cf0febe | -3.08231 | -49.57224 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fdc5a2eb-15b6-3bf7-be5b-10c478701229 | -2.80228 | -52.9427 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ab627b0-8c0e-3721-a0ad-7d60d087795f | -2.96384 | -48.02876 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15575bde-e962-33e1-ba3b-df06b4302212 | -2.9822 | -49.57296 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 471c846d-1061-3353-9ec4-665da66b3b7f | -4.30685 | -52.69556 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfebf348-e6ba-3528-8a51-cf4f2f339c25 | -2.22786 | -50.52332 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0668c281-80e3-385d-b80b-796170a2d4e9 | -2.42021 | -50.42054 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ab0cd82-fbe0-33b3-bacc-07636b59c5bd | -4.20143 | -48.5547 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77b048b4-8562-3bef-94d8-04a045045f3c | -7.63131 | -43.54195 | 2024-11-09 04:55:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bebd190-d7e6-35cf-b1c1-36425be885cd | -4.23034 | -46.89037 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbcdd9af-cbe3-3ea8-b87c-453a216da6f5 | -1.44087 | -54.48784 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3309b020-b5fc-3d79-943e-d5dc864b06de | -3.8857 | -50.24086 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6de8ea43-9476-3d61-b947-8cb8336c05e0 | -2.69011 | -51.69688 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4418a5ec-b6a4-3e11-b296-55bfc6c0f019 | -4.94036 | -48.23957 | 2024-11-09 04:55:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56994618-6fd2-37ef-841d-9061116f0422 | -2.21425 | -50.72498 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42c54ecd-7aaf-3bbc-94c7-03e380f7248e | -2.47714 | -53.97845 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6158710a-7ba7-3229-849f-77baa7c76ed8 | -5.52467 | -50.06425 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ca0dcef-74bd-3341-b0bd-8c7753044023 | -3.07509 | -50.56853 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3af94dce-6fbd-383e-a77a-e6f45bc7c355 | -2.94684 | -54.46588 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee42776b-ed2f-33ce-89b1-18aaa1e17f7f | -3.53618 | -50.33426 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73b45093-9642-365a-a012-84ad8b27996d | -2.66422 | -49.89955 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e15adad6-e889-3938-9a54-5be24b8e1881 | -1.23545 | -51.77801 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f9dffbd-308f-348c-8a97-c83cd13f8e89 | -2.14347 | -53.64552 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82a69e52-3d4c-3a0b-8b1d-1140e1f7d057 | -3.58787 | -53.0933 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad7f19b0-c853-39e4-bb3a-21bffe9806ec | -4.06403 | -48.31115 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7ea3726-0dc6-3991-900a-313e46da4d25 | -3.03431 | -50.32246 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0d9af9a0-8ada-3a76-8325-9f596ffa5400 | -1.56019 | -52.21664 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 112a906b-571f-35d6-b49d-8e40eabc6e0e | -3.11758 | -51.10478 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f61d9c97-4e00-3d20-b514-9dcfb996b371 | -1.31822 | -54.17903 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d31510f-cecb-37bf-9658-23eb427c17c5 | -1.10228 | -54.19713 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2342536-f86b-3e02-8b7e-b943e3b691a0 | -3.03405 | -53.27612 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a80fe16-e56f-330e-93ae-acfec3f6c33e | -2.84355 | -51.967 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7c20ef4-d5b9-3e4c-ad49-344bbea950fb | -3.25427 | -52.24122 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 236fb094-548d-3dd1-95d0-1c139d289bca | -2.87754 | -49.22606 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa63785e-abef-3413-a155-6f80b21d6b82 | -3.27561 | -53.41958 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78d6bbfb-a743-3bcf-9c7d-b2ad791f9d17 | -2.57904 | -53.99846 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dd1a261-3ec4-36ad-8c12-62773e31341e | -1.93089 | -52.67215 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff0dd4a0-5a31-3b44-b739-092794cc0ab9 | -2.28897 | -50.47486 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9770c404-3269-3524-9166-125f0f0904a9 | -2.20151 | -48.3745 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4983a1fc-1cf3-3c2d-8fe5-d1405d5cbcba | -2.65722 | -49.87231 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3384d46-c53b-3aee-a6be-1d260c7a85c5 | -2.22697 | -46.53978 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6be31a5f-3037-3ce7-bfe0-f5212c7ae645 | -2.13302 | -50.76376 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 312e4083-ed2f-3a19-b0f9-d5916c21aa7d | -2.18848 | -47.9477 | 2024-11-09 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeb9adca-4f48-316d-a341-0ccc66351f44 | -2.62847 | -54.02375 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebfe2d3c-5bc6-3519-ae6c-948ca6a90f3c | -2.44812 | -46.32066 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ca683228-52e4-39e8-9ce8-4693c6c91726 | 0.49794 | -51.74032 | 2024-11-09 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c5d4b40-f693-3916-81b4-b298bdc5895a | -1.34606 | -51.42574 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71cd89b0-9203-3453-8d4c-5b10ecd7d62a | -4.2076 | -48.54106 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b3268d00-020f-36f2-8aea-2ec583078142 | -3.25164 | -48.74517 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af2a6591-7e84-38a4-a50f-be35b6da7e7d | -4.35166 | -46.82491 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f675023b-7149-396c-9423-9f7a32ef7abb | -3.10687 | -51.35387 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f26555c-33b3-36c6-95df-478e1a02fa1e | -3.78771 | -51.82178 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d070663-8ee9-3b6e-9333-14fd3e47070e | -1.09788 | -51.73547 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fee8d8a1-a16c-314e-8d44-92870bf7e563 | -2.71176 | -52.96074 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f64d874-737e-3d43-a35c-61f64526a589 | -2.77881 | -52.87541 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2fa028a-ec0a-372f-bdde-2c9dbd5d2532 | -4.61711 | -46.53856 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8234c94b-a045-3e32-8742-4ed4a451ae2e | -2.81029 | -48.45541 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c6bba04-59e9-3f07-8d19-fd72c6342522 | -1.81195 | -52.26656 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaefdae0-618f-3488-9634-6e848ed1f1f8 | -2.92767 | -51.04931 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e6987c9-0e4d-30d4-a81c-c01de6e7b072 | -4.19738 | -48.55405 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e59ffb5c-7b71-32d1-bfac-7609a30d5cb7 | -2.63852 | -49.84758 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c49970d-23cf-3e09-b4c1-8113024e39d4 | -3.04651 | -50.36203 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a29df63-0bcc-3e74-a25f-eaa6a4ac7f51 | -4.7745 | -48.68151 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5880a8cb-b6dc-3067-9055-98d2edf89d76 | -1.59913 | -53.32259 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8051a0b-eb0b-3628-9207-e25a6f1770a1 | -4.36423 | -48.14953 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 919193e4-809f-3519-921d-35f48899eb4a | -3.15491 | -50.63244 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e62f3ea0-7c87-3b6e-b516-8380db513ed3 | -3.17343 | -51.25999 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 848fe8ff-5ac3-357b-8ff0-8efe13f7b8b3 | -2.45859 | -49.78411 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| fd421232-f2c0-3a1b-9b6c-6cb6eca5c799 | -0.30484 | -51.71765 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c6bcd7c-9e77-3417-8a52-aa491c679a67 | -1.93421 | -52.67267 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c873414-92fb-3f2e-a37d-6d14dab2527a | -2.81949 | -52.96306 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96c8ff3f-2e91-357c-be62-861306b75488 | -3.9254 | -50.24966 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b5ff835-3e72-347d-b31d-4629746d31f5 | -5.51398 | -49.19936 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46ee2c2d-825f-39ef-bb51-104157742f1e | -1.63909 | -52.27145 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15a1b9aa-9267-3e18-a862-ad1870b01a34 | -2.40239 | -50.3079 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README79.md)
