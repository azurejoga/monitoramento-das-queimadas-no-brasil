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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 226b5e37-c120-3df0-812c-f848022b1da8 | -18.63531 | -57.23348 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0d3445e7-22b1-318a-a10e-92d84717ca4b | -18.63198 | -57.2329 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 40002ba8-bb03-320c-bb04-0bc88b168972 | -18.62833 | -57.27732 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d7fb180b-4413-32ac-841a-d57bff7c8649 | -18.62807 | -57.23597 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 084944b3-8092-318c-8768-e831291bf407 | -18.62749 | -57.23962 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bfbeba3d-1786-3c49-95fa-4dcc9f7b6679 | -18.62358 | -57.24269 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| adfeda63-5a15-39f3-b02f-0eb732474ed6 | -18.61575 | -57.24883 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 37559dfc-1c03-31d7-a161-2f00a8c4b3a7 | -18.61517 | -57.25248 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 040c556e-dd94-34f7-96d2-713898121083 | -18.614 | -57.25978 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0b469a14-40f4-3214-ad56-bc9e58a1ca8a | -18.61342 | -57.26344 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6914c546-2441-3e6c-803d-a6c5508a61b5 | -18.61242 | -57.24824 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9b23b257-5664-3a05-aaef-e26b44a68660 | -18.61184 | -57.2519 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 50388cf9-9b4a-3226-bb7a-997e92584c2a | -18.61125 | -57.25555 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0cb42059-cd6f-3ce6-bc00-376fa181a47e | -18.61067 | -57.2592 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 433ddae5-d5de-35b1-be37-b953e6f38c30 | -18.61009 | -57.26286 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 3133e3e7-bcea-3272-8b64-8565426419f6 | -18.60909 | -57.24766 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d38f5d5f-c899-3180-b0e1-e42e0c5b5e28 | -18.6085 | -57.25131 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 0087f949-66b6-3875-bf67-424fdd5959ea | -18.60792 | -57.25496 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| c74db281-1d5f-3e40-86ba-252e01de56d9 | -18.60734 | -57.25862 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 7aee56ca-90d1-3636-ae47-514c8103a917 | -18.60517 | -57.25073 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 85d4eab7-13c6-34ea-9c9e-43a0bb7a334c | -18.60459 | -57.25438 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 87e5eb02-9fbc-388c-89da-9e03d07fd60b | -14.85777 | -58.02632 | 2024-10-08 04:59:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90e42aac-8688-3179-a150-7e6c0402dc7d | -15.70697 | -59.42284 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd29c21b-01ce-3156-a22d-c7e94a70f94c | -15.70624 | -59.4271 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7223a3c7-37ad-33e6-b9ef-8c9a13a34d15 | -15.70478 | -59.43567 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5409950c-1340-375f-a239-11cb7fb086ac | -15.70403 | -59.44003 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff59fcc2-41e4-3e2e-825f-09d90c85e71a | -15.70262 | -59.42648 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17585035-eec4-311c-b0bf-4c1ee38f5e23 | -15.70041 | -59.43937 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a1e4679-bc45-3e14-a827-1c39d59aee29 | -15.69966 | -59.44381 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa8b896e-cd08-3cbb-b856-e3526472cce4 | -15.699 | -59.42587 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b12264d1-d387-3cae-91ef-75e6982a1a0b | -15.69828 | -59.4301 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2349a8e9-850e-327f-b4f6-b0f2f028b29e | -15.6968 | -59.43871 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cecd060-45ce-331d-ac1d-df5d449216ff | -15.69604 | -59.44314 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 291b6fa1-52f0-3499-8494-85d1c63bf0ad | -15.69466 | -59.42945 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6e96c59c-34cc-3fd7-a4de-927a003d74e0 | -15.69393 | -59.43372 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 14d1c25f-e5d3-3be8-91ec-008b11c4e069 | -15.69243 | -59.44245 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 132d6802-cd57-37bf-a5ce-e79b684d4fa7 | -15.69168 | -59.44685 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91593f57-a3a5-3d6c-8087-cc1f2aa1f301 | -15.69032 | -59.43305 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e8f8f7d9-ec7b-3c6e-a253-507a6cd75748 | -15.68806 | -59.44618 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ed936cb-24ea-3e03-8ae2-293143ffff67 | -15.68672 | -59.41064 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a29d80dc-9192-3edd-9971-2700cc01f3ff | -15.68385 | -59.40567 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97863fdf-e141-3027-bcbb-d995c7d728b5 | -15.68371 | -59.44981 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d26d4a0-3e2d-3d36-aa1d-a58a79f0022e | -15.68312 | -59.4099 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24e18c5d-972c-3dd5-9a87-126b797efed2 | -15.68025 | -59.40498 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95bf252d-4b1e-37cf-9218-217a19a1f2ea | -15.67952 | -59.40918 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acb2ab0c-50f7-3b19-9b2e-ad9186a13e0a | -15.67879 | -59.4134 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c945bfbe-91da-37ed-acc9-d45f131e93dc | -15.67806 | -59.41765 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab7804a0-8caa-3702-b57c-9fa73aa48e8a | -15.67732 | -59.42193 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| badda3f2-f5df-3e32-8662-54de3da75568 | -15.67444 | -59.41706 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8ee5ffb-5c97-3e30-95fa-0c9dddcd851e | -15.6737 | -59.42131 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b0100e4-85fe-3b11-99c9-4b7b97bf3f75 | -15.67297 | -59.42556 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3585f74c-c9ed-356b-946b-f087fb7c09c2 | -15.67008 | -59.42069 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10eb470a-63b0-3b06-aa35-779b4b07b91e | -15.66935 | -59.42491 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ff1b7a2-7ee9-3488-a8bf-9362ddefc92a | -15.66862 | -59.42915 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69d51acd-79d8-32b2-bf80-e35c0b01022d | -15.66501 | -59.42847 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1b05d75-cfed-3cc4-beed-54f0b9f585eb | -15.66427 | -59.43277 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d887b82-2128-3c99-8149-4dc130a26e9f | -15.22502 | -59.3561 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdb9e533-3fb5-360d-b1b0-ea6871ba7e68 | -15.34295 | -58.13218 | 2024-10-08 04:59:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7ccb8a9-083f-366f-9c11-0e7ab3441106 | -15.34231 | -58.13602 | 2024-10-08 04:59:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff4d67b7-df6c-3bcc-8577-e6a59ab8f499 | -15.33886 | -58.13548 | 2024-10-08 04:59:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b40e365e-ed25-379d-a716-3f23eb26da3f | -15.1809 | -58.5811 | 2024-10-08 04:59:00 | NPP-375D | ARAPUTANGA | MATO GROSSO | Brasil | 5101258 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 255b2018-09ac-372b-bac0-d5e8346a7a07 | -15.12831 | -59.02233 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 452efa72-a1b9-3f2c-af13-cb44318b5276 | -15.12759 | -59.02657 | 2024-10-08 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 122385cb-415f-3e3c-a9b3-2f7e39177a65 | -13.42564 | -61.91914 | 2024-10-08 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91adda68-6792-3b90-add8-66f75a8bdcee | -13.41112 | -61.92508 | 2024-10-08 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42d15d0b-652b-3b9d-8147-56e2b1fdd9d0 | -13.40958 | -61.93357 | 2024-10-08 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4dceaeec-698f-3c2f-9f46-c78ec16d7dad | -13.40679 | -61.92424 | 2024-10-08 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e17bf0f4-9c5f-3df5-980a-a3dfa4d2b459 | -13.42131 | -61.91829 | 2024-10-08 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49e786df-5d51-3f29-96c7-07a8ea4583a3 | -13.40602 | -61.92847 | 2024-10-08 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de1df18f-696a-33b1-8393-072a60ce7e88 | -13.40524 | -61.93273 | 2024-10-08 04:59:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04b0f0b3-5507-3a0d-a711-2ad5fc548495 | -21.97592 | -46.56318 | 2024-10-08 05:01:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fb1e8271-9489-3c9a-9204-29a803a0c75c | -21.97362 | -46.56441 | 2024-10-08 05:01:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4cb6dd8a-bae5-32ac-b682-dc50ed0af161 | -21.97005 | -46.5624 | 2024-10-08 05:01:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9572ee72-52ca-317c-8741-d597af1cfc16 | -21.96852 | -46.55472 | 2024-10-08 05:01:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ee33ad16-b393-300e-b7f6-caf780a7b796 | -21.96815 | -46.55906 | 2024-10-08 05:01:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 69923671-2c6e-3a0e-b455-c8cefb1c36a4 | -21.96501 | -46.5527 | 2024-10-08 05:01:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b6f8abef-4aa6-3a3c-ab38-89ca97beef28 | -21.9646 | -46.55713 | 2024-10-08 05:01:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d655da58-dd3a-3fe5-af92-7c3e6b67bed7 | -21.96266 | -46.55374 | 2024-10-08 05:01:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ac4ea139-3c2d-3e8a-959b-49a97ff8299d | -23.45254 | -47.27287 | 2024-10-08 05:01:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 3d4316dc-be3b-3f45-9792-401c95fb5ebc | -22.58326 | -46.66358 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 169c8721-1128-341c-9f2e-67ac03e0220d | -22.57743 | -46.66228 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d04be542-a0f2-3afc-bd36-0afa435c6ee0 | -22.57687 | -46.69403 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 8a95d6fb-20d2-3f37-912b-0443bc76ef35 | -22.57651 | -46.6981 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 0f82d755-6438-3fde-8a90-b75dbc39ec86 | -22.57511 | -46.68998 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1a291678-1d51-3a8c-81a2-2c260f5887b3 | -22.57472 | -46.6946 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 6517e9d8-d1d6-380f-9ad0-daabd7eb114c | -22.57439 | -46.6985 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 2d77443d-584b-3b1e-966b-dc74ea953a52 | -22.574 | -46.66021 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5128bb38-6c05-381e-942c-c063c709703b | -22.5736 | -46.66461 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7619f882-ea14-38e1-942f-99347b64661f | -22.5716 | -46.66091 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fa5c8a68-ec44-3cd7-ba58-194e95c139f5 | -22.57142 | -46.68874 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b7c8e556-0e4f-372f-856c-bb6ee9f0be8b | -22.57106 | -46.69275 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8f0a9d30-0849-3e72-8d3e-8820659e7ff0 | -22.57072 | -46.69653 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e5f0ac7e-0b2a-3b7f-9033-577080a67bae | -22.56921 | -46.68969 | 2024-10-08 05:01:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f6c7605d-e8a3-315c-a455-b67f45760b74 | -21.85084 | -48.4072 | 2024-10-08 05:01:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76ec54e4-c231-3509-b26c-184145ea1a1a | -21.85051 | -48.41055 | 2024-10-08 05:01:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3dec00c7-5748-3ccc-a839-f942701edf6e | -21.85016 | -48.41393 | 2024-10-08 05:01:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1a2bc44c-6d69-38a8-8a0a-a9871daa1985 | -21.84982 | -48.4173 | 2024-10-08 05:01:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 989de6e1-a1e2-3434-8918-b8926cd5b3fd | -21.84948 | -48.42064 | 2024-10-08 05:01:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9903d266-cfa6-3bab-8e1a-9dd73c156ce9 | -21.84459 | -48.41671 | 2024-10-08 05:01:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acf45e27-06f6-3128-80e2-c8b14e63417c | -22.80284 | -48.46143 | 2024-10-08 05:01:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README108.md)
