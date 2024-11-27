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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0148e5f-8e78-3ee2-bb94-f946a1d33a35 | -0.02736 | -49.6415 | 2024-11-27 04:18:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 479e3479-a864-385c-b610-fdad3156d4c3 | -1.61054 | -52.75359 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5acdcaf6-6dce-386b-a88c-a1e64ec32582 | -3.08002 | -53.27411 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 301001e6-b2f2-3469-ad5b-6e968f886760 | -1.18994 | -51.77191 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dfb2f48-df18-302a-91c4-bcaaf7f85562 | -4.32956 | -45.88808 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d1804fe-7530-3fa1-b937-700dab2134f0 | -2.72025 | -48.66849 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67a3d7cd-7dc2-3b3d-8080-6179b56a547d | -3.49636 | -50.49842 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dd972035-1563-3e3d-867a-457f627dcfa6 | -1.96998 | -48.43033 | 2024-11-27 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ca3e402-1e3f-3dc3-9413-9235671f9fc1 | -3.94125 | -46.9058 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc82dc79-bf18-32a8-8edd-32c4c58f10cc | -4.72029 | -46.57285 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 100d2a42-2823-3549-8d1d-32a1d93221eb | -5.42494 | -37.60806 | 2024-11-27 04:18:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ddefde2b-073b-3b2c-81ba-6b14ad662335 | -2.68212 | -48.5928 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e499e9a9-90ed-3ad2-8578-c74940e3c824 | -2.09818 | -53.35795 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c23cc76d-dd31-3d29-963f-6b96fc0932b1 | -2.54619 | -46.40746 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a85e8e03-9f17-3ce6-90ee-65a02d65028a | -2.81367 | -46.81075 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de3e590b-8027-3f43-848e-f70dc79cccdd | -4.05181 | -48.33143 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33b01c5c-2d38-3f5b-96d2-e4d4a445dd31 | -3.097 | -53.2732 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38a36362-a7ce-3fa0-8fbb-54149e6ccd9b | -2.1388 | -46.47796 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1b57631-3ab2-36ab-b220-9bff5ba5f036 | -3.16498 | -48.44072 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 8b8ec712-2eca-3500-ae81-70cf89985ce7 | -2.86111 | -46.81409 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d8935708-6fec-3fea-8f71-3d0905c01087 | -2.18532 | -53.77518 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| cce3d568-9a58-3092-b37b-18152617aaa8 | -3.80043 | -45.22064 | 2024-11-27 04:18:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a3ffe29-c401-3f45-ba94-47ec1d65da16 | -2.52989 | -47.32914 | 2024-11-27 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6b5d8d7-9835-3c0e-b101-3d5f7db3f116 | -2.81531 | -46.82364 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8f5c0da-0083-3cd7-850f-ad0910031383 | -4.52651 | -45.79124 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 560ad2e9-84aa-36bc-910d-1e3603afe2a4 | -3.81203 | -47.47327 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47141bf2-deb2-3bf2-9f09-b2f34745aca7 | -3.08436 | -53.28182 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e896a964-7a5f-31a1-a923-559e421aa62a | -1.18544 | -51.97905 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4ce308e-cba4-39c7-b3c5-962ea8853c50 | -4.2184 | -47.2197 | 2024-11-27 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 246887c8-9756-3be5-9904-74e6f8b1371f | -3.84647 | -46.5106 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32fb2785-a677-3146-a8fc-26d1ae7ecec7 | -4.39046 | -45.90154 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f81168a8-8593-34b5-ac1d-269db2224f17 | -3.94755 | -46.69063 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8b4f57d-3494-3590-869e-7f58b476db88 | -2.54556 | -46.4114 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae15f4a1-e635-33da-9860-99969d77d811 | -3.77014 | -46.51473 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3720b0cc-3800-35e0-91ff-3df4894d6091 | -3.9435 | -46.91446 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02eaa57f-ac5b-39ed-ac8a-b355bb4d288e | -3.09758 | -53.26965 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5023272-f8a3-3c76-825a-1f3ac4689c88 | -4.15363 | -43.8214 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c193ed85-d7dc-3054-8d0f-841b575e96ed | -4.01836 | -47.65444 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1271c3e9-98d2-3201-8244-3e3248df7511 | -5.25831 | -40.60258 | 2024-11-27 04:18:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f8cbea16-8ebe-36d6-b531-eb4d6a6746a6 | -5.18772 | -37.97478 | 2024-11-27 04:18:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fcb83d6d-1a02-32ad-8bd2-2992327bfeb8 | -3.59162 | -50.35506 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a82f1846-f043-33a8-9769-7170d8efa257 | -3.50671 | -50.46354 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b873530-ee52-3d9b-b637-2b6fad519085 | -1.98414 | -53.29431 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e34ed176-2a82-3ed9-b0b5-5068a49f24c5 | -2.71439 | -46.2558 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9afa2612-172c-380a-a3ca-cc7de2ab3637 | -2.59604 | -51.82894 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37d480c9-cfb7-3e62-ac77-88b42a308ba5 | -2.72216 | -48.60583 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1c06420-2ca7-3ba5-8126-de5d6034318b | -3.41449 | -50.20512 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78ca8828-be44-3e0e-b430-d645563dcb59 | -3.2897 | -50.75939 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 485d6380-0ad5-304b-8172-71ffc8b34be1 | -5.02798 | -47.01629 | 2024-11-27 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74d539d1-96da-3534-86c4-9cb7ddc10d3d | -2.0375 | -46.51584 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51881778-0cc5-3d20-ae66-1b8efacde148 | -1.81084 | -45.92889 | 2024-11-27 04:18:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21ed0b2a-1501-3f4c-b92a-1594607cdd6f | -3.98382 | -48.06334 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9abcca2c-d50a-3a5b-b206-7118df4f4cdb | -1.78861 | -52.73882 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b4b177c-4b1d-3ced-a65c-56eb787313e0 | -2.83768 | -51.85007 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 10b1e1b4-f8a3-3a04-98a0-e5284d00f285 | -3.29895 | -47.02126 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebaf6a42-081f-3f25-b80f-3f45f80d9b6f | -4.05952 | -48.3327 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88a8ece2-4ab9-3e3a-8cb5-a488674cd28f | -3.08604 | -51.02887 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a547e591-cd10-3959-bd73-2552347ace4f | -1.83134 | -47.21144 | 2024-11-27 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9de2dd66-eb8f-31ba-aa28-95a187c28a0c | -3.19305 | -50.83037 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85d2dfe0-0982-3991-a83f-cf5f2e296838 | -3.97212 | -46.73824 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0de8f3b-5944-37f3-b1d9-4e1f746657fa | -4.09843 | -46.11032 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20a108c8-e5ae-3ecf-b7f3-9d0cd31c6548 | -3.28012 | -50.55942 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 230a9096-d8d0-31db-a82b-55542a436fad | -2.81105 | -46.82719 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6afe150-e003-303a-b41c-f5837b3636a9 | -2.72498 | -49.3348 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3008664d-f627-34e1-8fe4-a71d0d501455 | -3.09866 | -53.26812 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7b93306-cb4c-3a21-a3a4-de63130c7556 | -2.71712 | -46.28418 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e67f154a-80aa-3dfa-8ded-415b7357d280 | -0.02804 | -49.63709 | 2024-11-27 04:18:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3aa63c69-b033-3a54-bf34-eb557d06ad30 | -3.77384 | -46.51217 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ba19eeb-b9bf-3fad-aa73-d462dbcdfd03 | -4.31545 | -47.5197 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6c9ab314-97e8-3895-9a5e-718812c3cb4a | -3.10038 | -50.36899 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27d85a42-88ff-352c-b79d-9256e6b97769 | -3.70845 | -47.6674 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79182e51-c8b6-3e95-94af-f8deaa6ba0c5 | -2.63105 | -48.42725 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e624a0c-84a8-35a5-af42-67c780cd431b | -3.6133 | -49.89524 | 2024-11-27 04:18:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be0e6673-9726-3363-b2e7-a6e8e82a457e | -3.50085 | -50.49918 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| df9bbe94-c9d8-39b5-87e4-0bb4d16d2a26 | -1.49396 | -48.03287 | 2024-11-27 04:18:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32afe49b-4fc9-3866-85d8-7803a683edd2 | -3.10736 | -53.27845 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92fc9a4d-6924-3203-b8b4-38aabbaa9ac3 | -3.34561 | -50.18705 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e859984b-1c5e-3fef-8e35-f53d2f26b9ca | -2.81873 | -48.60213 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1249d8ab-0107-39e6-9265-c341c32256df | -3.32795 | -53.71902 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d30acaa1-2f09-311d-af27-032a84822e80 | -2.59401 | -46.26574 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f69ebeeb-45df-313a-92a3-b249004cc56f | -1.66622 | -52.71738 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6b08b34-e65a-31d5-9ead-4c0a003f8a56 | -3.09745 | -53.27521 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91f17e6a-160e-3b6d-bb31-d073660aa101 | -3.32683 | -50.21883 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04264cd1-6167-3022-a559-6eff35405d1e | -2.58343 | -46.19619 | 2024-11-27 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ed63bbb-155c-3ab0-b6ad-fc0a4c3b4895 | -2.60042 | -46.27079 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffed1355-54e2-3cc4-8dd4-45e3bff42f4d | -2.73076 | -54.13498 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c919459-b122-38f4-ba2e-4033cd14de4b | -1.73247 | -52.04099 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 672cdfb9-fb0e-3efb-86f9-dea032bf499d | -3.28657 | -50.26997 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07593327-6447-3ba5-b259-085742ff5b7c | -4.14331 | -50.41599 | 2024-11-27 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b451efc8-8d9c-3386-a4eb-941820d6836c | -3.71568 | -47.12093 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81b72671-c707-3e5b-992c-e88872ba316a | -3.59088 | -50.35949 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 253531fa-cf29-3d1d-8188-ea249f615c5c | -4.13919 | -43.80498 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a48752f-16f3-34c3-939e-a8ec227c09e8 | -5.31921 | -43.06901 | 2024-11-27 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9324f8d7-c45c-3218-8885-3aa30529a539 | -4.47645 | -45.82078 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b16f9461-0337-324f-aee2-36414e442187 | -3.97631 | -46.73478 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9fce625-0178-3f0d-a384-984e36e0332c | -0.98686 | -51.72054 | 2024-11-27 04:18:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e910c33-7751-35e9-84c8-3304866beec7 | -2.59545 | -51.82956 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62ef4a9f-77e2-372e-bbb8-1c964f5a699e | -3.10077 | -53.2845 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01c47df9-db5e-3054-88f2-1e24369d3c26 | -4.10548 | -46.94327 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17b79a80-4699-3138-a914-71900733b443 | -2.76974 | -52.90656 | 2024-11-27 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README42.md)
