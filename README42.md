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
| f3d3c76f-de7e-3a7a-b743-91377ec9f3eb | -3.234 | -50.5789 | 2026-09-04 13:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| ab1a7a31-6ece-3b8b-b06c-42465330fdd6 | -6.6882 | -59.9628 | 2026-09-04 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| bcd92e6a-b040-30a0-9b33-b8ec2279be5a | -19.0948 | -57.3641 | 2026-09-04 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.0 |
| 5d508b88-0a1e-34ff-b87b-8d5a2b99cfdc | -5.5982 | -43.9748 | 2026-09-04 13:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 6b410aff-d04a-3e0f-a1ef-addad1a62fe8 | -5.5978 | -44.0209 | 2026-09-04 13:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| bb06ca7c-4a37-3ac7-a4a8-7d79d4ceb0c1 | -19.0748 | -57.3668 | 2026-09-04 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 779d25dc-4f8a-3b4a-acfb-e8993258f57a | -6.6881 | -59.982 | 2026-09-04 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.3 |
| c6f7f1dc-b135-38fc-bff9-95dbda0fa023 | -10.28751 | -68.85284 | 2026-09-04 13:10:00 | TERRA_M-T | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 29b943eb-b465-378c-871e-d18ac19a9155 | -10.28878 | -68.84393 | 2026-09-04 13:10:00 | TERRA_M-T | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 27a0d1cc-3dc6-3789-a332-46307a55134d | -10.29006 | -68.83501 | 2026-09-04 13:10:00 | TERRA_M-T | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 55914823-d75b-340c-8d88-7a8d2e2f00dc | -6.6881 | -59.982 | 2026-09-04 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 292cbe82-c948-330f-b851-5416733d0f5f | -19.0948 | -57.3641 | 2026-09-04 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 245.7 |
| ba133eac-1212-3e69-b7e0-948bb7d163a3 | -4.4087 | -55.7823 | 2026-09-04 13:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 454d3c5a-82a3-38e4-8982-0d68e84f9cca | -19.0944 | -57.3849 | 2026-09-04 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 4109f5d0-edf6-3506-91cf-7a22a9a39992 | -15.9199 | -50.1506 | 2026-09-04 13:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| e0f475d5-1ddc-35f0-a068-457810eb4275 | -6.6882 | -59.9628 | 2026-09-04 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 8b2985ac-e634-3691-8005-b2dcbf23e8e9 | -5.598 | -43.9978 | 2026-09-04 13:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 319.5 |
| 7bc13cec-086b-3dc2-b3a2-f00ef9d32117 | -19.1147 | -57.3615 | 2026-09-04 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 8f5939df-7ab0-3fc4-99ff-8e070c811e7e | -5.5978 | -44.0209 | 2026-09-04 13:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 59b61a82-c294-3386-a8f6-f91856f0321b | -5.5793 | -43.9992 | 2026-09-04 13:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| aeee63b9-a604-3c3c-9dd8-6e617f09d1fa | -5.6168 | -43.9965 | 2026-09-04 13:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5186f0c2-db67-390a-99b1-31668088dc28 | -6.6697 | -59.9635 | 2026-09-04 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a0ffc22c-289f-35a7-a6c4-22f6bcb7ff3a | -19.0748 | -57.3668 | 2026-09-04 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| 06701c37-10b6-3081-9c15-b0b0088a5c49 | -5.5982 | -43.9748 | 2026-09-04 13:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 143.4 |
| ca302447-0cea-373d-9c2a-cc797d1a955c | -19.0944 | -57.3849 | 2026-09-04 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 7ec2e89e-7fa8-3826-af06-80662614473b | -13.4054 | -43.8911 | 2026-09-04 13:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 793b5cd0-49f4-3b3b-a9c6-e64b1ff221b3 | -5.5793 | -43.9992 | 2026-09-04 13:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 7a4df309-b7f1-3802-91b0-703a4d82f86f | -10.5103 | -51.3194 | 2026-09-04 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 45ba0d29-23cd-37f1-9962-77cfcb407abd | -5.6168 | -43.9965 | 2026-09-04 13:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7ffe621f-ef74-3e6a-b0d9-9f4b7cca3fca | -19.0748 | -57.3668 | 2026-09-04 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 169.2 |
| fd6ae458-31a4-336b-9f31-21f900bee677 | -19.0948 | -57.3641 | 2026-09-04 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 410.9 |
| 45653960-d4d8-32a9-b827-f64ee4fe744e | -5.5982 | -43.9748 | 2026-09-04 13:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 819fb9bb-423f-3e3a-a3af-84d244353770 | -13.382 | -51.3352 | 2026-09-04 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 5df5ef5b-267f-38d7-b862-eabec53c6124 | -3.3685 | -59.5036 | 2026-09-04 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 59bb7a35-c4e9-35b8-a609-07e0856be2bc | -19.1147 | -57.3615 | 2026-09-04 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.7 |
| e35afd76-d595-36d9-a0da-2cd6c5f43770 | -9.6987 | -45.7077 | 2026-09-04 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 124.0 |
| e0a04d8a-a84d-3fdc-b575-a3f99d3ab3ef | -3.7645 | -61.7548 | 2026-09-04 13:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 14c3f5dd-8b2a-3922-9c6a-c7877ecadc41 | -6.6696 | -59.9827 | 2026-09-04 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 64a7339a-8372-3475-8dba-f96e4bab08c7 | -12.9036 | -45.8152 | 2026-09-04 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 7212ee04-4c2a-3a20-8de5-84026d0ce71c | -19.0751 | -57.346 | 2026-09-04 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 304f548b-20e3-32e6-a773-ad196d991cbf | -6.6697 | -59.9635 | 2026-09-04 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| dcc687d2-98a2-37ec-b19b-55f3d65bf273 | -13.3628 | -51.3377 | 2026-09-04 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| ee1d3e4a-b1db-3f77-8456-167349c9fa78 | -6.6881 | -59.982 | 2026-09-04 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 176.9 |
| 06dc8dfa-42b0-3707-85a4-e11eff43593c | -6.6882 | -59.9628 | 2026-09-04 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 0371d547-6e6b-393f-b32f-5a852bef93b0 | -5.598 | -43.9978 | 2026-09-04 13:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 464.5 |
| 122c823e-08c0-38ff-926f-628bc0c4b053 | -6.6698 | -59.9443 | 2026-09-04 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 07b300e6-bb6a-3037-ad29-35c7c1863e91 | -5.5978 | -44.0209 | 2026-09-04 13:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 03aea544-729e-384c-97c1-e685d84b57c2 | -19.0948 | -57.3641 | 2026-09-04 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 287.9 |
| 85098ea4-f350-37af-b305-eb0da9732d22 | -19.0748 | -57.3668 | 2026-09-04 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.2 |
| acfdb512-383c-3361-befe-dda7367a3c11 | -13.4054 | -43.8911 | 2026-09-04 13:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| bb1cbd25-bebd-3a5b-a33e-34a5147f26b7 | -12.9036 | -45.8152 | 2026-09-04 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 456c1261-8e47-31be-9341-014a1fb8df15 | -5.5978 | -44.0209 | 2026-09-04 13:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 63ad9245-6ba2-3bbf-8861-06a682466ad5 | -10.6545 | -50.4137 | 2026-09-04 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 9d81ccb0-c50f-3b83-abbc-5d9c245319cf | -3.3 | -57.8875 | 2026-09-04 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 3c2cac95-4569-36a6-9a63-d03b39290741 | -17.3271 | -49.6026 | 2026-09-04 13:40:00 | GOES-19 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 2ced95c1-b246-3dc4-9bad-32f5b63ff357 | -3.234 | -50.5789 | 2026-09-04 13:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| be5326df-c5b0-341e-92bc-ded7f38e827e | -6.6882 | -59.9628 | 2026-09-04 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.8 |
| e8f60f3d-afba-3f5d-84b9-dadd4131f796 | -11.2584 | -50.5623 | 2026-09-04 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 48982e82-e504-3cf5-84cf-bb1b741dcd0d | -11.3334 | -50.618 | 2026-09-04 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| d2aba1c9-8ebd-3418-a77f-505d97bfbd8f | -5.5793 | -43.9992 | 2026-09-04 13:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 63459565-1077-3a77-a35d-e441ac7aeb3a | -19.1147 | -57.3615 | 2026-09-04 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.6 |
| 13e0e25f-c101-3b01-9649-57d4d95b3bc9 | -5.5795 | -43.9761 | 2026-09-04 13:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 2cebbdf6-c7ef-3f9e-a1e7-47de99fdda07 | -5.5982 | -43.9748 | 2026-09-04 13:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 6c0d1f30-04ec-3d60-80d8-c485b0d500f1 | -6.6697 | -59.9635 | 2026-09-04 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.4 |
| ce99fcc9-272d-3346-abe3-d7c87f062c4a | -10.6548 | -50.3923 | 2026-09-04 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 3cd8ad4f-9ec2-33e0-bd00-62a69dcd09d3 | -13.382 | -51.3352 | 2026-09-04 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| b7ece591-d55b-3737-abf7-e11662ef8258 | -12.9032 | -45.8382 | 2026-09-04 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 08effe18-97d4-3c13-a8d1-e1a9ae4f2d15 | -6.6696 | -59.9827 | 2026-09-04 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| e1e3fd08-e742-3156-9192-e9f48239f578 | -3.3685 | -59.5036 | 2026-09-04 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 132.8 |
| b59cf43e-a239-3398-9ce9-823e7d8fe6c3 | -13.4059 | -43.8673 | 2026-09-04 13:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 57fe9a43-f61a-386f-8306-926ccea07912 | -6.6698 | -59.9443 | 2026-09-04 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 6dedfd9d-c517-3c91-9203-7e5122d7429b | -13.3625 | -51.359 | 2026-09-04 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| d987da6c-bc26-31cd-8832-0de99a49e1a7 | -6.6881 | -59.982 | 2026-09-04 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 197.7 |
| cc520547-8f12-3596-b6b6-4ebf439f9b02 | -19.0944 | -57.3849 | 2026-09-04 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| a5602ad4-7e39-3315-bd1c-4ef952c54114 | -12.9589 | -45.944 | 2026-09-04 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| de016184-9e8b-30d4-8eb0-35acab05457f | -11.277 | -50.5815 | 2026-09-04 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 84da5be8-5e3e-387e-9637-07bd9d24f7f8 | -11.3144 | -50.6201 | 2026-09-04 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 06529730-cc12-3c51-977b-e5f5c44c72e7 | -11.258 | -50.5836 | 2026-09-04 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 906cf590-c3e6-395c-b3ea-625010649922 | -13.3628 | -51.3377 | 2026-09-04 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 39977ea8-47b7-37e4-af61-8f3391e45951 | -12.9036 | -45.8152 | 2026-09-04 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 1c3885cf-6d7e-3c83-b8ee-138bdfc75dba | -3.3 | -57.8875 | 2026-09-04 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| e88c4484-6eea-35f2-b93c-8e00d97a9742 | -3.3685 | -59.5036 | 2026-09-04 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 170.8 |
| bf1f63ab-d338-354a-b1e0-4d470ed58327 | -11.8248 | -46.0448 | 2026-09-04 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 5223d43e-e76b-3849-a65d-0344de96c36a | -3.234 | -50.5789 | 2026-09-04 13:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 31ed6712-b225-301a-b07b-ebe9f53ee7a4 | -6.6881 | -59.982 | 2026-09-04 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 183.1 |
| a1717869-a74b-3f7a-9050-950f44a1948f | -8.9598 | -44.4204 | 2026-09-04 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 57bc5ead-0f14-3499-b8e2-fdc69dfdd9e8 | -13.4059 | -43.8673 | 2026-09-04 13:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 47c2ffdb-1dfc-31f2-abc3-7f227c15bf4a | -17.3266 | -49.6249 | 2026-09-04 13:50:00 | GOES-19 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e877b958-e354-3fb2-9dd9-e4a88e473f6e | -6.6882 | -59.9628 | 2026-09-04 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 535dea54-6973-39ed-998e-d0a4dbccb7eb | -17.3271 | -49.6026 | 2026-09-04 13:50:00 | GOES-19 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ff7c2d7b-4156-38fa-b6da-8f94a9a58319 | -6.6698 | -59.9443 | 2026-09-04 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| d117a984-8432-3cd9-ba40-bed27ef89c7d | -6.6697 | -59.9635 | 2026-09-04 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 1e959e0e-3318-3325-a3ce-9e72fa90dbf6 | -3.7645 | -61.7548 | 2026-09-04 13:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4f8a42fd-e256-3b4a-89fe-6d6e4a379333 | -13.3628 | -51.3377 | 2026-09-04 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 0d2033cd-4cf6-328f-be3c-d92451ec9933 | -5.598 | -43.9978 | 2026-09-04 13:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 246.5 |
| 5ff9b24e-9b64-36b4-b66d-7bdd5d328629 | -5.5793 | -43.9992 | 2026-09-04 13:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 1e14b5ac-49f0-3964-9254-3ff6c2d78dc4 | -9.6987 | -45.7077 | 2026-09-04 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 091836d3-d285-3620-8748-331dab1bb63c | -6.6696 | -59.9827 | 2026-09-04 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 258d21dc-30e4-383f-9d7b-3d1a889b4df8 | -4.1307 | -56.3434 | 2026-09-04 13:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 2be5a4af-9d65-3c90-a102-5171944b7477 | -12.9589 | -45.944 | 2026-09-04 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |


[Clique aqui para ver as próximas entradas](README43.md)
