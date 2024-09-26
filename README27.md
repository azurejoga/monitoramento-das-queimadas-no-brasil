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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 736af116-9eba-36b0-b61b-8e3f26bbf1de | -8.2911 | -54.674801 | 2024-09-26 00:56:43 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ffbce7e-fe65-37dc-8873-f711dc233e22 | -8.2927 | -54.681999 | 2024-09-26 00:56:43 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a50b61c1-349e-37f2-8151-a50aa3334d96 | -8.3529 | -55.048401 | 2024-09-26 00:56:43 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 841ae64a-e370-3e52-89df-adafbb594374 | -8.3545 | -55.055698 | 2024-09-26 00:56:43 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46ab629f-0026-3077-afbe-6dd62b45e003 | -8.3561 | -55.063 | 2024-09-26 00:56:43 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de63d0fe-37e6-3afa-a1fc-02bf000e29d6 | -8.3447 | -55.0578 | 2024-09-26 00:56:43 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 641ba733-2ea3-3a6a-a1b7-ebf3919393ce | -8.3188 | -54.986801 | 2024-09-26 00:56:44 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f87b074c-91c3-317f-a3eb-8d2747ba3a81 | -8.3204 | -54.994099 | 2024-09-26 00:56:44 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3274f72d-e50e-36ca-85f2-62e86b4db43d | -8.322 | -55.0014 | 2024-09-26 00:56:44 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaa52915-0852-3f78-98ab-36f52a0e38da | -8.309 | -54.988998 | 2024-09-26 00:56:44 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d35fb89-50c9-3def-998d-abe507196b8e | -8.3106 | -54.996201 | 2024-09-26 00:56:44 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26678c7a-c9fc-3656-98ab-d04371176594 | -8.3122 | -55.003502 | 2024-09-26 00:56:44 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0279662-0f07-37d9-ac31-71edff6967a2 | -9.3917 | -60.278702 | 2024-09-26 00:56:44 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8e7138-8c6e-39f3-b9fa-dc9aacbc7020 | -9.382 | -60.280701 | 2024-09-26 00:56:45 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf177936-ba22-3062-819b-76d3133ab2d0 | -8.2447 | -55.210999 | 2024-09-26 00:56:46 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 452f7376-0e77-39e2-add5-6533e7209577 | -8.1207 | -54.787701 | 2024-09-26 00:56:46 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29f92614-8d04-3aa4-a7a8-5099174bd7e9 | -8.1223 | -54.794899 | 2024-09-26 00:56:46 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8b8bc1d-0849-3a9b-b66c-e4d6728d0a84 | -8.1093 | -54.7827 | 2024-09-26 00:56:46 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6a97c38-ea0f-3168-ae3d-1b52f7985eb0 | -8.1109 | -54.789902 | 2024-09-26 00:56:46 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dfe0687-8aa9-3397-a902-79e9812e2f4a | -8.1125 | -54.7971 | 2024-09-26 00:56:46 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94d04914-00a6-3f7c-8217-4b70750a5240 | -8.8065 | -58.199299 | 2024-09-26 00:56:47 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95c238b2-c20d-342f-8de3-126a191a7491 | -8.8087 | -58.2099 | 2024-09-26 00:56:47 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20d8a416-b1d1-3722-ab50-582484ec5dfd | -8.811 | -58.220501 | 2024-09-26 00:56:47 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5455012-6c5a-338d-b083-b5474e90aef9 | -8.0538 | -54.764801 | 2024-09-26 00:56:47 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfe18e28-47ed-36e9-891a-374e00278d89 | -8.0554 | -54.771999 | 2024-09-26 00:56:47 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e65729b1-72c8-31e7-be1f-949813fa2e95 | -8.79 | -58.1698 | 2024-09-26 00:56:47 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e2646b7-5262-3faf-bb5d-0653e85ac929 | -8.7923 | -58.180401 | 2024-09-26 00:56:47 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d141d1e-aada-3978-b7da-39e1b1c9a60d | -8.7989 | -58.212002 | 2024-09-26 00:56:47 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| afbe83a7-8955-3169-a35c-2d3778d225b3 | -8.7781 | -58.161301 | 2024-09-26 00:56:47 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f37d3087-c22c-3474-af33-736da1e6b256 | -8.775 | -58.195 | 2024-09-26 00:56:47 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12e29df5-df58-3618-aef7-04061e20a05e | -8.7772 | -58.205502 | 2024-09-26 00:56:47 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3180269b-f8fc-3536-80af-92c8086bebdd | -8.763 | -58.1866 | 2024-09-26 00:56:48 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d05ac7cc-734d-328f-be16-6b06a512ad66 | -8.7652 | -58.197102 | 2024-09-26 00:56:48 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b1d5f30-9f55-3dd3-95f1-90e84ddae38f | -8.7487 | -58.1675 | 2024-09-26 00:56:48 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b830a42-57c5-3c7c-9087-5e0d9f68b583 | -8.0959 | -55.376099 | 2024-09-26 00:56:49 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc2f43d4-b70a-30c5-89e7-f0758c076054 | -8.0976 | -55.383598 | 2024-09-26 00:56:49 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdf8b136-0173-3fc9-ab08-e8764156365c | -8.3413 | -56.5023 | 2024-09-26 00:56:49 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26679686-84f1-3f51-bd9a-5154737581f8 | -7.974 | -55.055 | 2024-09-26 00:56:49 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0e7fab4-1f83-3017-ac3f-c0688473921f | -7.9756 | -55.062302 | 2024-09-26 00:56:49 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2194d1f-780b-3a88-84e1-bf9156d9e1dc | -7.8894 | -54.718601 | 2024-09-26 00:56:50 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 529bb358-ad5d-3b74-afe4-a1026b8b5576 | -9.208 | -61.119801 | 2024-09-26 00:56:50 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2fbae7d-4a37-30c7-8599-fa3f63ec0701 | -9.0529 | -60.409801 | 2024-09-26 00:56:50 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8d1fe0a-c642-3cd6-86a5-0782e5a9bfc2 | -7.9133 | -55.106602 | 2024-09-26 00:56:51 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93ce3ef3-886f-3907-865f-f72a1913a32c | -9.0401 | -60.396999 | 2024-09-26 00:56:51 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72752acb-64d0-3a87-a389-a5366767e8a7 | -9.0431 | -60.4119 | 2024-09-26 00:56:51 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3863aea8-2340-30f2-8a95-a9fa00e0f3c4 | -9.0462 | -60.4268 | 2024-09-26 00:56:51 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6e95664-af21-34c3-9ee3-9189ae7e0692 | -7.8176 | -54.719601 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 245cb195-4876-3481-ab7e-01ac0bb2178f | -7.8192 | -54.7267 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2498790c-4427-3cd7-8bdc-0ab945ae2188 | -7.803 | -54.700401 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc7a1f62-d7b6-3a36-a280-f1fe60d5d929 | -7.8046 | -54.7075 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db02dfb9-28ab-3af8-ae16-b478d21d7aa7 | -7.8062 | -54.7146 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7d864f2-3e3b-32a4-a8e9-471c5c0697f0 | -7.8078 | -54.721802 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b850c4a4-0c3a-3f5a-8edf-9b51774f828d | -7.8094 | -54.728901 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e232e65b-6ed7-3094-a4d6-3d7b8037cdc8 | -7.8109 | -54.736 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53a3429f-8ac3-3573-8521-7da02ad76b1e | -7.7932 | -54.702599 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c4b846e-e713-3299-897a-a3b2712ac2f5 | -7.7948 | -54.709702 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c96cee7-428e-3973-8d8a-9417a8690a65 | -7.7964 | -54.716801 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 581ffe0e-9a89-37a0-a80e-4e5e78c39bba | -7.798 | -54.7239 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5d0fc1e-393b-310d-afeb-30453f84111f | -7.7996 | -54.730999 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26e483e7-86f3-34f7-bb38-366aa5faa031 | -7.8011 | -54.738201 | 2024-09-26 00:56:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 054b8f27-360d-371f-9832-e047b83a9481 | -8.002 | -55.697701 | 2024-09-26 00:56:51 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa0c5f26-3ed8-3f99-8894-8bfddad17146 | -7.9905 | -55.692299 | 2024-09-26 00:56:51 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44b468d8-0565-3121-81b6-79b0751ca162 | -9.1004 | -61.089401 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7415221c-e39a-3b1d-aa77-429c12ad9c10 | -9.1038 | -61.106098 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7add531-dbcb-3746-8e6c-7b459b52fbaa | -9.0907 | -61.0914 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cecb558c-e405-31a7-8f68-55e1c9eb1ec7 | -9.0941 | -61.108002 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5aac3097-ab46-3132-a81e-bd76cd4f4b05 | -9.0809 | -61.0933 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2e0d9cf-264f-3416-a6dd-0de2c981dfe9 | -9.0843 | -61.110001 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83251ca0-34f6-3a5d-820f-6fc396f1af6b | -9.1118 | -61.245098 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cef92e5-9a3b-323f-be29-644136168f6b | -9.1257 | -61.313801 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2add5379-3de9-36be-915e-a6c1464db256 | -9.1292 | -61.3311 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a14afef-b593-3478-ae54-ac1139be3cea | -9.0986 | -61.23 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1ee8a2c-b9a1-3ae9-959b-ecf835859f6d | -9.1021 | -61.247101 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 030f8c70-5640-3ca5-a5ef-4be4202ac55f | -9.109 | -61.2813 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6c74baf-c4d3-398b-80de-501865e0b309 | -9.1125 | -61.2985 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe0a8c80-9019-3c2a-90af-f662cd6b112a | -9.116 | -61.3158 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65392360-6f28-39bd-8976-7b18549ea147 | -9.1195 | -61.333099 | 2024-09-26 00:56:52 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dab4dc58-ee57-3463-a37e-ee0c9d3b8368 | -7.932 | -55.7533 | 2024-09-26 00:56:53 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd998354-c268-39aa-81d0-f6c3b6e7664a | -9.0889 | -61.231998 | 2024-09-26 00:56:53 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d33747b7-3c22-32fc-b41c-f266b9d2aa84 | -9.0923 | -61.2491 | 2024-09-26 00:56:53 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c86c6501-0070-3ef8-8688-ed40be06351c | -9.0993 | -61.283298 | 2024-09-26 00:56:53 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ed5b2b9-9585-302d-9112-c03e6f5d0743 | -9.1028 | -61.300499 | 2024-09-26 00:56:53 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96b89dad-afd5-301e-8b80-bc3f49f1f62b | -9.1063 | -61.317799 | 2024-09-26 00:56:53 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68e7ed0d-514d-3d56-9339-69f1d5b2817e | -9.1098 | -61.335098 | 2024-09-26 00:56:53 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72913619-d8a0-3b11-951e-123f3e254e00 | -7.8689 | -55.512299 | 2024-09-26 00:56:53 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e86053c-72f0-34d5-adb4-d06e72d27567 | -9.093 | -61.302502 | 2024-09-26 00:56:53 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b292aca-de65-3fdf-b5ac-6b6f48633788 | -9.0965 | -61.319698 | 2024-09-26 00:56:53 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b7386b7-d73c-3c1f-ad4a-53a31d688245 | -9.0709 | -61.342899 | 2024-09-26 00:56:53 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb2427f6-b565-3ef5-ac37-19cdde39500c | -9.0611 | -61.344898 | 2024-09-26 00:56:53 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5705c3d9-3d2f-3e60-adf8-368e34b80271 | -9.0646 | -61.362301 | 2024-09-26 00:56:53 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0fd569f-f20f-3f3a-9827-1ceb3b13e0c8 | -9.039 | -61.385601 | 2024-09-26 00:56:54 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 748c75a2-77ac-3184-9aa2-fce80f2ad229 | -9.0425 | -61.403 | 2024-09-26 00:56:54 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac699b11-cd29-3b49-a095-752f54c22362 | -9.0461 | -61.420502 | 2024-09-26 00:56:54 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a65cdd7-2079-35c9-bef7-1db61ddddb08 | -9.0328 | -61.4049 | 2024-09-26 00:56:54 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 388c79bc-b5f6-3f0f-86ae-d52ace270f4b | -7.7663 | -55.6534 | 2024-09-26 00:56:55 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 406ef064-caa4-3656-957f-7ce8b7ff0ed3 | -7.7679 | -55.660999 | 2024-09-26 00:56:55 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9be90e81-e245-3958-8d7f-3edb75745ae8 | -7.6532 | -55.278999 | 2024-09-26 00:56:55 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b984f71b-5ef9-35c5-a556-d0f9cf2dc7c2 | -19.929 | -43.7959 | 2024-09-26 00:56:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.4 |
| 8c544891-c891-36cf-929a-8ad8cd2bea63 | -19.9298 | -43.7711 | 2024-09-26 00:56:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| 7a1b8c2b-7f0c-399f-b5a3-fd409b7c3547 | -7.7206 | -55.679298 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README28.md)
