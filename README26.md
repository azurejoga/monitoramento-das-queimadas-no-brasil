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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f66e55dd-08e1-3aa0-bb6d-efd53250665a | -11.5116 | -65.09458 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 75311c0f-11a3-34ea-bd7f-7c20ca1b78fd | -11.50296 | -65.2261 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea7cb061-8ce1-3468-89f4-8ff2f4ccb99f | -11.49183 | -59.09143 | 2024-10-08 02:11:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e7019734-21bf-3ff3-9866-275d326e298e | -11.48547 | -59.09829 | 2024-10-08 02:11:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 11677006-bdc4-3470-8458-dd4564760fb6 | -11.4826 | -61.9782 | 2024-10-08 02:11:00 | TERRA_M-M | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 54d53ef2-bd18-3e95-a1d2-d0f11822bf96 | -11.26399 | -60.39695 | 2024-10-08 02:11:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 25.4 |
| b7f008dd-9ff8-33d2-a1e1-4b7d9d8eb64b | -11.26163 | -60.4032 | 2024-10-08 02:11:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 433669fb-06e0-3ccc-ad76-d33dbc4f7ddc | -11.26104 | -60.37907 | 2024-10-08 02:11:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 30f6ffb8-0436-38c2-a460-f4d5392fe96d | -11.25886 | -60.38558 | 2024-10-08 02:11:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 3f1b2081-b75a-3444-a212-271ad7af54f7 | -11.25461 | -60.49321 | 2024-10-08 02:11:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5a04ff2f-bb11-3f77-881d-677265f5b6a2 | -10.978 | -63.98424 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a73eaf21-836d-30e2-bd05-e8491950165a | -10.97326 | -63.98019 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 29c09d9f-aad1-33be-ad74-72362f6facdc | -10.91777 | -63.86988 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2bdc80f5-8ac2-344a-ae56-42cd2bbf6059 | -10.9162 | -63.8593 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9c4498ba-b3fc-32df-94d3-e84f463afdb8 | -10.89531 | -63.91711 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4c3669f3-2dd7-31d6-a15c-3d511340bbce | -10.88949 | -64.17138 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b1a3af6-5bba-3888-b032-14aa2df9eaf2 | -10.88414 | -63.90818 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 87b11d8d-05e0-36e1-8364-76e74fb46d14 | -10.87772 | -63.93082 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1b2bc3b1-fbb1-3ff9-b1fe-8cf1dd2bcbca | -10.87615 | -63.92041 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 28.8 |
| c3cb5d20-243e-3dea-b30a-1ee57705ce44 | -10.8745 | -63.90951 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 32.7 |
| beb01712-2c83-36b9-a9e7-663fbd810509 | -10.87329 | -63.92693 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 49503caa-d14e-34f9-a284-fa69b1c7580b | -10.87283 | -63.89849 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 0a6a5159-3916-36c6-97e6-4012f7906552 | -10.87177 | -63.9165 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 55d2ecb2-1d4a-3659-9489-c517e47d6eb8 | -10.87015 | -63.90534 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 29.3 |
| aed9e6c0-ad40-3f11-bb3b-37e604b14499 | -10.86856 | -63.89442 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 0a43d947-adfe-3a19-97c8-96c566ab5208 | -10.86698 | -63.88361 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a1784636-311a-336e-a4dc-1a6b14f1cf99 | -10.86212 | -63.91766 | 2024-10-08 02:11:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 119d4a01-d76b-31bd-b479-b7413bf0fc19 | -10.86051 | -63.9067 | 2024-10-08 02:11:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0b6d2573-0845-3d9b-b943-3f77d19008fe | -10.84218 | -64.17897 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 220e7213-7e39-31a4-8640-f58db6a03d3a | -10.81428 | -65.18179 | 2024-10-08 02:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8c956441-912b-3cd4-897e-393f069ff9bb | -10.63553 | -55.91704 | 2024-10-08 02:11:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ff7ddb90-e1fd-379e-808c-08798220566c | -10.63551 | -55.92418 | 2024-10-08 02:11:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 3f05c7b2-f52f-356f-b20f-8f609d82dc3a | -10.33966 | -64.26062 | 2024-10-08 02:11:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d90756f7-373d-377e-b853-b0e8830ac532 | -10.20203 | -61.95831 | 2024-10-08 02:11:00 | TERRA_M-M | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a475ae41-58a4-39f2-adb2-63f51228fba2 | -10.1399 | -63.66728 | 2024-10-08 02:11:00 | TERRA_M-M | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d4083500-f793-3e7a-b85b-37577115616b | -10.02975 | -63.47972 | 2024-10-08 02:11:00 | TERRA_M-M | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fe38640f-e8c6-3e80-8e1d-4a2bd2896087 | -5.5716 | -44.8927 | 2024-10-08 02:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 358dfac8-1a35-3745-abef-1db8dcf12022 | -5.5718 | -44.87 | 2024-10-08 02:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| c9809150-a1f5-3f03-b08a-0dc74374368f | -9.3901 | -66.5444 | 2024-10-08 02:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9132e5c2-408a-3119-8b09-cb7bb30bd3be | -9.4087 | -66.5438 | 2024-10-08 02:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e04a64b5-10dd-358d-b0fb-8ab1bbc55ba7 | -9.445 | -66.7289 | 2024-10-08 02:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6ea83ee5-2a09-31bd-96dd-e8e472834c4a | -9.5537 | -63.5764 | 2024-10-08 02:16:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 8d939a4a-d7c8-331f-b329-8deb19684205 | -10.6256 | -55.9154 | 2024-10-08 02:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| beafcc4a-16ea-38e5-b509-9997148bf4cd | -10.8754 | -63.9169 | 2024-10-08 02:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 69da33ca-aae9-389b-8255-c330f62dd21a | -10.8755 | -63.8979 | 2024-10-08 02:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 166acea6-a9c5-3510-9cc1-d5f6c7d83b8a | -11.2292 | -51.2879 | 2024-10-08 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| fb264bdd-84bb-39c3-9b18-c6ecbd714baa | -11.2295 | -51.2667 | 2024-10-08 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 30984bf4-623c-3b70-9ba7-a02705f1b647 | -11.3078 | -51.0889 | 2024-10-08 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 725b920c-1c45-3e81-b76f-34b214e5d9c6 | -11.3081 | -51.0676 | 2024-10-08 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| d84d5186-1eee-3884-960e-a287d66e58f4 | -11.3271 | -51.0656 | 2024-10-08 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| c90cb148-c488-38aa-b259-33b627e874da | -11.3277 | -51.0231 | 2024-10-08 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 372230c6-b1f8-3250-b309-4ad99d3f70d6 | -11.328 | -51.0018 | 2024-10-08 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| f7824c62-9063-37f1-9fb6-959d693e8c22 | -11.3464 | -51.0423 | 2024-10-08 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 196865ce-eea8-31fd-8f4c-1f4f49afbf61 | -11.3467 | -51.021 | 2024-10-08 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| b98d337c-e670-3606-8549-307b19472d9b | -11.347 | -50.9997 | 2024-10-08 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| c7035296-609f-3072-b276-b74673948b17 | -11.3473 | -50.9784 | 2024-10-08 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 5a8a75b6-1d92-3a9e-92ba-c70671ea2871 | -11.5233 | -65.137 | 2024-10-08 02:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b5f862a3-40ca-35c3-84e5-57d604c1d7e6 | -11.5232 | -65.1559 | 2024-10-08 02:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 7377ac78-a051-3eb7-9d7c-f8147f601a76 | -12.3616 | -47.0986 | 2024-10-08 02:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| e41ae790-6cf2-362f-a98f-efadde6c9b18 | -15.6872 | -59.4544 | 2024-10-08 02:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 95e3f099-8a06-333b-9041-a863ae6a4959 | -15.7068 | -59.4326 | 2024-10-08 02:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 660bf17c-3067-3cce-a25b-4c653fc5a071 | -15.6874 | -59.4344 | 2024-10-08 02:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 46911af5-6af1-36e9-b4fb-35c52dac0312 | -16.5897 | -46.4979 | 2024-10-08 02:16:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f28020c8-de97-35fb-aaf3-8e0629683aa5 | -16.5752 | -55.9055 | 2024-10-08 02:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 41.1 |
| 2c70c79f-9548-3e6a-a4d3-f480c0675b17 | -16.5466 | -57.714 | 2024-10-08 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 57748e36-42c7-3c74-b121-83fcaa909ded | -16.5462 | -57.7344 | 2024-10-08 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 3875a838-abf9-3eaf-b634-4ea2cf242b15 | -16.5556 | -55.9079 | 2024-10-08 02:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 35.4 |
| d1b2f537-5635-305f-ad7b-140209e26edb | -16.6143 | -55.9007 | 2024-10-08 02:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 36.6 |
| ea2915e3-6f29-34ff-bbd7-71920d01e90f | -16.5948 | -55.9031 | 2024-10-08 02:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| 23f89beb-d229-3fc1-9812-5741ebfc6e73 | -16.5661 | -57.7118 | 2024-10-08 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| edf7a6b4-739e-38b9-9712-063ebc25078c | -16.5658 | -57.7322 | 2024-10-08 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.3 |
| 51e1e5df-bf8e-3d82-9ecb-54f30080c0d7 | -16.6531 | -57.1305 | 2024-10-08 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| fbf5abb4-5abd-3006-bf62-29ed1b324ed9 | -16.673 | -57.1077 | 2024-10-08 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| f887cfa3-7aee-3b31-81fc-67fd4aedf4ef | -16.6726 | -57.1283 | 2024-10-08 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.6 |
| d5d46a5c-6aa6-3f71-aeb8-2e5b24a122ac | -16.9211 | -57.4881 | 2024-10-08 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| a8e6c727-3d6b-3dcf-8113-3a6156680576 | -16.8048 | -57.4197 | 2024-10-08 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| f695fc0a-2341-3b67-8df5-7f50988402bd | -17.0992 | -57.3651 | 2024-10-08 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 9951bf66-7bfa-3146-b576-36e4c3d1e273 | -16.9407 | -57.4859 | 2024-10-08 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 0d9af7fe-b855-3e81-86f9-3704aba6f745 | -18.4931 | -53.4457 | 2024-10-08 02:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a48b5da0-f31c-36c2-94ff-e22aa334e8bd | -20.3732 | -43.9468 | 2024-10-08 02:16:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.1 |
| 97ddb00e-c567-3bb5-aab8-da9f8b0b5a4c | -20.3938 | -43.9412 | 2024-10-08 02:16:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 178.1 |
| 7f0c82ae-5ba9-38fd-b247-ee6a4682ff33 | -20.3946 | -43.9163 | 2024-10-08 02:16:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.0 |
| cca8a467-eba5-3c2f-b2f7-66896ce37da5 | -20.4258 | -47.6453 | 2024-10-08 02:16:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 3d17f434-660e-31c5-b925-2b5b12322421 | -20.6602 | -45.9105 | 2024-10-08 02:17:00 | GOES-16 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 83.5 |
| d0a32dc5-cb27-3233-b907-ddca6f9a0111 | -5.5716 | -44.8927 | 2024-10-08 02:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 6700a62c-331e-3dd4-9183-3e2d12672dce | -5.5718 | -44.87 | 2024-10-08 02:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 646977eb-c54a-32f7-9f18-ecf0c3061eda | -9.3901 | -66.5444 | 2024-10-08 02:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a52c652e-0855-3c2a-9acb-fe1719bc21c5 | -9.4086 | -66.5624 | 2024-10-08 02:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| aea9946c-9ae6-3446-a9b4-ce443a703af6 | -9.4087 | -66.5438 | 2024-10-08 02:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 23a9cb8c-1c72-3295-b4a7-5df2e58bc881 | -9.445 | -66.7289 | 2024-10-08 02:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 91431aaa-d7f8-30d9-9a54-44dff2ffa583 | -9.5537 | -63.5764 | 2024-10-08 02:26:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 0b46203d-4b88-3fa2-8aad-80c77e4ca8be | -9.5351 | -63.5771 | 2024-10-08 02:26:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 05464a7f-b82d-3515-ac51-46fa10b2148c | -10.6256 | -55.9154 | 2024-10-08 02:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| f6d0868b-b8ad-398a-86cb-3f6f147c2c9e | -10.8755 | -63.8979 | 2024-10-08 02:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6adaffc8-aabb-353d-8e31-3de82d694680 | -10.8754 | -63.9169 | 2024-10-08 02:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2e51ce3d-9fa8-3ccf-8b1c-f57784f289b4 | -11.5233 | -65.137 | 2024-10-08 02:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 498d1bbe-3b59-3ba3-bf43-f87b3c5c4b08 | -12.3616 | -47.0986 | 2024-10-08 02:26:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| f0ab3aa8-3db9-3f53-84e0-e08ea4633c98 | -15.7068 | -59.4326 | 2024-10-08 02:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| c39ee1d5-4eb4-351b-a10f-d29c2f45b1b7 | -15.6874 | -59.4344 | 2024-10-08 02:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3a2bcf9b-d870-3c09-b498-04fd1fa009a2 | -15.6872 | -59.4544 | 2024-10-08 02:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 38.6 |


[Clique aqui para ver as próximas entradas](README27.md)
