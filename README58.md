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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06259390-0821-30e4-ac58-b771a2043687 | -11.1112 | -46.4818 | 2024-10-04 04:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 7ad1e33e-7a57-34c4-8eb9-44a3f97d22af | -11.2566 | -60.5825 | 2024-10-04 04:06:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b03dbf78-bd1f-3594-8d18-b843a5de8eab | -11.2565 | -60.6019 | 2024-10-04 04:06:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 606bad66-8df9-3118-8e11-2d592993e690 | -11.8242 | -56.6009 | 2024-10-04 04:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f718250c-be7d-3eaf-9236-8c7340a6451b | -12.5898 | -53.1359 | 2024-10-04 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 0a6d994a-4452-33b9-a02b-9c04b29d49d4 | -12.5901 | -53.115 | 2024-10-04 04:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 78a17aee-af1c-3998-927b-a003a5c7f670 | -13.0598 | -51.1195 | 2024-10-04 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4a1d3aff-530a-3e3d-8d15-eccd531fc042 | -13.0786 | -51.1385 | 2024-10-04 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 68902d89-e24b-3105-a820-ad58a47ea383 | -13.079 | -51.1171 | 2024-10-04 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 1581726a-559a-3f9a-9742-706275e31171 | -15.3567 | -58.143 | 2024-10-04 04:06:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 345fc32f-9c67-3f2e-af99-9521c991ad6d | -16.3956 | -57.3845 | 2024-10-04 04:06:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| ac72d39a-96f0-38e7-80b3-6161f339f9b6 | -16.4148 | -57.4028 | 2024-10-04 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| c33a4132-f32d-3a5f-91da-177c65dc9da6 | -16.4151 | -57.3823 | 2024-10-04 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.8 |
| 057cd26e-e1e7-3c68-881a-5f2e16179a28 | -16.5935 | -57.1988 | 2024-10-04 04:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| 0fea3d4b-1b89-3cfb-8cd1-5b9cc1d449a7 | -16.5938 | -57.1783 | 2024-10-04 04:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.1 |
| 3d015649-ce16-3585-a6fe-7080f10781d6 | -16.613 | -57.1965 | 2024-10-04 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 197.3 |
| 6ad40829-5fcd-387b-a39f-cef37824138b | -16.6133 | -57.176 | 2024-10-04 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.0 |
| 77a9d4b7-efab-3aa9-b8f4-eff30c9fe7bd | -16.6868 | -57.4741 | 2024-10-04 04:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 2630c962-3d42-386c-928f-8cbdf74ddc58 | -16.6871 | -57.4536 | 2024-10-04 04:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| cfadb001-7d12-3a78-bd3a-c6fb8b76fc05 | -16.7455 | -57.4674 | 2024-10-04 04:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 94c819ff-2fb0-3d87-b6ca-8a25f9a95185 | -16.7647 | -57.4856 | 2024-10-04 04:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.5 |
| c1ab39ef-ca26-3e3a-8c15-79156d8d71d1 | -16.7859 | -57.3811 | 2024-10-04 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.1 |
| fd3f4234-45e2-35bd-bd2c-177e28ba358c | -16.9283 | -55.8405 | 2024-10-04 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 6c7e5882-c226-3397-9c16-3c8daca26bd9 | -17.0888 | -56.7915 | 2024-10-04 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 197842eb-511c-3612-aa3b-9f99e018ce9d | -17.1085 | -56.7892 | 2024-10-04 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 30ff9180-78d3-3dcc-8b73-8e68164aae03 | -17.1088 | -56.7685 | 2024-10-04 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| fa5764df-1f95-3bcc-be2b-61c313a48118 | -17.1378 | -57.4016 | 2024-10-04 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.5 |
| d1892ceb-57c2-37c5-a4a3-07f06fab708d | -17.1574 | -57.3993 | 2024-10-04 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 4914a112-19d1-3a50-8b73-97f763f766fc | -17.1577 | -57.3787 | 2024-10-04 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| d7801a61-7d13-3191-94c6-eb2e94803618 | -17.1771 | -57.3969 | 2024-10-04 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 334de08c-f91a-35db-924a-10fe408022ba | -17.1774 | -57.3764 | 2024-10-04 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.6 |
| 3957a419-1618-3165-8ff5-66f62f7dcb53 | -17.6074 | -46.9866 | 2024-10-04 04:06:44 | GOES-16 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 44.8 |
| cb65bd73-5aea-3b0b-9758-e0a6e12343a2 | -17.6079 | -46.9634 | 2024-10-04 04:06:44 | GOES-16 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 72ee0b69-4e81-362d-b3b1-482ef1b29c85 | -17.7307 | -43.8127 | 2024-10-04 04:06:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 68b968c7-7ce1-3411-9543-cb962b064031 | -17.7508 | -43.8079 | 2024-10-04 04:06:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 3bf6b919-74c3-39d0-8269-9a51e87ae544 | -18.8617 | -42.8932 | 2024-10-04 04:06:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.8 |
| 8bc69e76-e697-3a36-9784-2b6d7a6ffbc9 | -18.8613 | -43.5837 | 2024-10-04 04:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| 7890d78d-f1d3-3565-944b-cb4fc7be2f17 | -18.9081 | -42.0315 | 2024-10-04 04:06:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.2 |
| 872b4252-b807-3e01-84aa-87bad7fc8073 | -19.0344 | -43.1944 | 2024-10-04 04:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| f2e75da0-6524-3201-ac5b-c5beeaaff9aa | -19.0352 | -43.1695 | 2024-10-04 04:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |
| 133ffb92-e758-3541-8d9a-85d67e759e0c | -19.3159 | -42.5976 | 2024-10-04 04:06:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| 0fbb5d60-84ac-3644-aac4-d9d41870c63d | -19.3167 | -42.5724 | 2024-10-04 04:06:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| b79b389c-1c9b-38fa-b8a5-5f791f72b8a0 | -19.4899 | -42.8746 | 2024-10-04 04:06:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| d7b466ac-7bdd-31f6-b7ff-a617ebc2c626 | -19.5104 | -42.8691 | 2024-10-04 04:06:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.7 |
| a4765302-a152-34e4-97f6-1abaf0e85b83 | -19.8524 | -42.3484 | 2024-10-04 04:06:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 150.6 |
| e6acc6dd-c50d-3693-938b-993f8c65eea7 | -19.8516 | -42.3738 | 2024-10-04 04:06:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 229.9 |
| 4214d270-1f7a-3829-a238-467ef4f7b9d3 | -21.7773 | -48.3976 | 2024-10-04 04:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b17472c7-ad87-37c2-ae1b-38cb34fe85fb | -21.778 | -48.3741 | 2024-10-04 04:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9fbf973b-8a29-30cf-9696-be3db7433a77 | -21.7988 | -48.3691 | 2024-10-04 04:07:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 661ce5a6-bf63-305f-a92c-f5b030a576d0 | -21.8397 | -48.3826 | 2024-10-04 04:07:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 3195ec8b-8f92-3a3b-9567-f6454654ab21 | -3.49715 | -43.3123 | 2024-10-04 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b276ef47-54bd-3bc0-8711-dc7171d0b11e | -3.47571 | -43.35655 | 2024-10-04 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 901d112c-a934-3856-b16b-aabb36967db7 | -3.47159 | -43.35989 | 2024-10-04 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f623f430-f7ad-3826-b7fd-9253167ce83d | -3.43345 | -43.34268 | 2024-10-04 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c09c5fe-4017-3bbf-ac50-4f828e3f652d | -3.43283 | -43.34657 | 2024-10-04 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4a8f753-515c-3c48-8ee8-0b172be32f56 | -3.4277 | -43.33384 | 2024-10-04 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a3c808b-4203-322f-8927-af75b02d04a1 | -3.42708 | -43.33772 | 2024-10-04 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd02d839-86bb-3ccc-83bb-68698ad2c750 | -3.26572 | -43.13954 | 2024-10-04 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a5d56c4-5f9b-34a7-a9c4-8a98526d9306 | -3.26225 | -43.13898 | 2024-10-04 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14d83012-be14-36c2-b293-8a8156a031da | -5.01309 | -43.81243 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8112c53c-6ac6-38d3-a33d-cae809609996 | -4.93271 | -43.77549 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9750e474-cc83-3053-9939-949c85692ed4 | -4.93207 | -43.77943 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7206b9e8-e4fd-3dbf-b94b-a1a9bc7d5f1f | -4.92921 | -43.77492 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cde4bf41-ed86-38b3-a285-fc1f75a32970 | -4.92857 | -43.77886 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c79ead09-cc7c-39be-afc9-253cfa9d372a | -4.9257 | -43.77438 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41852c03-abf5-3fe9-b7a1-49a3430c1ec5 | -4.92506 | -43.77832 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57ed681f-4b21-3231-80b9-4f0de18327c2 | -4.80059 | -43.77971 | 2024-10-04 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fb5932b-0dfb-3fab-90c7-9ecdc0d04708 | -4.79996 | -43.78366 | 2024-10-04 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f3744cf-cf2c-33f1-85c6-e98b76b71fc6 | -4.69634 | -43.72762 | 2024-10-04 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fe39d51-23fb-3a5a-8632-24d8f9091019 | -4.69284 | -43.72708 | 2024-10-04 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8750310e-2ce1-3a87-8568-c6416e7d3ca6 | -4.50135 | -43.62965 | 2024-10-04 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be955752-7171-31ea-9edd-00ed0b16e571 | -4.8179 | -44.35493 | 2024-10-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da67fbdc-c98e-3a87-8125-da9dda2106a6 | -4.74262 | -44.09853 | 2024-10-04 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4115a487-a80c-3b1b-a45e-2f9e9a01b1f2 | -3.96534 | -44.05728 | 2024-10-04 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17228b54-211d-39f4-a1b1-f15298cbd808 | -4.53865 | -43.30449 | 2024-10-04 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| c2058128-7064-3263-9901-885d5c582b5b | -4.53805 | -43.30828 | 2024-10-04 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 0bcb0d8c-7732-3de5-8181-c8519b835f12 | -4.5358 | -43.30015 | 2024-10-04 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0da927a5-2b6a-3594-b790-9984734bb7a4 | -4.5352 | -43.30394 | 2024-10-04 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ea0c75ad-9a66-3e66-9a5c-fee553be0d56 | -4.5346 | -43.30773 | 2024-10-04 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 130dd031-fcfc-3ef9-896e-18b6a0fcf196 | -4.53399 | -43.31153 | 2024-10-04 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8b0140a-dc29-3518-8c04-0c7efb29503b | -4.53235 | -43.29961 | 2024-10-04 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bbbe47f2-6fdd-3b3a-a991-82472ff40bd3 | -4.53175 | -43.3034 | 2024-10-04 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| b82cc4ba-fceb-32cc-b1ee-f867a0245243 | -4.53114 | -43.3072 | 2024-10-04 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 65b28aaf-39e2-3df0-a9ba-fd8c913bb759 | -4.5289 | -43.29907 | 2024-10-04 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e71a8ab3-9388-32c1-8f74-bcebc5bb6fc8 | -4.02884 | -43.23732 | 2024-10-04 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18c59c37-2db6-3f1a-959e-beb0e8b41986 | -4.02637 | -43.23731 | 2024-10-04 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8e33111-10bc-3cc7-8cb9-1c681db22e6c | -4.02538 | -43.23678 | 2024-10-04 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7cdc5d4-9ca9-3044-857c-c92ae021275a | -4.02291 | -43.23677 | 2024-10-04 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fa55b58-0da7-3588-963b-377b95a6216e | -4.02231 | -43.24056 | 2024-10-04 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 620c4f4e-dc5e-38d5-bcdd-5cf60345b410 | -4.01885 | -43.24002 | 2024-10-04 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0b5a317-fca7-3b92-b9d0-4aa404dcf9c1 | -6.40007 | -44.74524 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e4019df-aae9-3161-b1a2-d083f9b8c704 | -6.39863 | -44.74629 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c34694f-d1f7-354c-889a-955e22de3f7e | -6.26136 | -44.8076 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fe02052-7fce-3fd6-8dd9-2e369d4325c3 | -6.52025 | -43.91842 | 2024-10-04 04:08:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0cf2f381-78c5-3a8a-87ae-bba04f170f1e | -6.48808 | -43.78716 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f86e1a7-f2fa-3250-bad0-45b382c4a715 | -6.48462 | -43.78659 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81d52b68-0c2b-35f4-aee4-af3a47ed5cce | -6.37453 | -43.85945 | 2024-10-04 04:08:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b4ad5a9-0255-39b2-9dbe-f79d34f1428c | -6.37196 | -43.83136 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08db8c10-dae4-3693-9d90-756e02603067 | -6.32769 | -43.73856 | 2024-10-04 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 687badb0-9d09-3023-aba5-14480b84cc8e | -6.24537 | -43.72182 | 2024-10-04 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README59.md)
