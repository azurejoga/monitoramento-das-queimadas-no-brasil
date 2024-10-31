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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5eb5dfc1-45a3-3339-9a27-3cf8282e8da7 | -19.61983 | -56.71237 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 95586e24-24ae-35f5-8adc-06af25030f9e | -19.6259 | -56.7173 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9ff29a98-0fc5-3fce-a447-b3591524a8dc | -19.62256 | -56.71669 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f1b53f89-d38a-3b09-b8d2-9c584dbc362d | -19.62196 | -56.72041 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0d641e61-3e7c-3c8c-8d2a-69ac11cc8420 | -19.61741 | -56.72723 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 906834de-7079-357d-994b-9d645acfeac9 | -19.61711 | -56.70805 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 91f72e7f-dfe1-3037-85eb-c91567ae7a97 | -19.61498 | -56.70002 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e10e08ef-647b-371e-a529-278223981e2b | -19.61407 | -56.72663 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| d98eab8c-42af-34ef-ad15-18adccd2645d | -19.61377 | -56.70745 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 517bfbbc-cf91-3d7f-b72a-ba5ecd4d745f | -19.61347 | -56.73035 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 1d22502f-04b3-3c59-8290-6849d34c991e | -19.61317 | -56.71116 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a883e0f4-b841-3eae-83ae-9a2eaf75cecb | -19.61286 | -56.73406 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 3ca8837c-890e-3328-93c2-063c1ff22a0f | -19.61104 | -56.74522 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5970f844-ed5e-3e62-b0d6-f0f5e904bd80 | -19.61043 | -56.74894 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ab31ab58-c8e7-3a95-8183-451f320592ae | -19.61013 | -56.72974 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 1faf2cf5-b34d-33f1-9305-df637eb1fb76 | -19.60921 | -56.75637 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 26cb0b7a-0cdd-3fb7-a978-12b9ef356d76 | -19.60892 | -56.73717 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 62bd1852-7316-3d3f-9848-8b1457f82ff6 | -19.60801 | -56.7217 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| f60fef91-d3d2-3b83-8610-0868fc5c5cf1 | -19.6071 | -56.70624 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a5060833-08a2-3355-a9d8-5b53b4276d03 | -19.60466 | -56.76321 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 69a0d914-5303-310d-8647-74e74535e7dc | -19.60407 | -56.72481 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 9727151c-b9ae-36fc-a402-0a73ad5d15ef | -19.60376 | -56.74773 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 248.2 |
| 49800279-ce65-3398-93a9-158938a7ed22 | -19.60375 | -56.62164 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e7cf9fa1-eee9-3f3b-a991-e763f6a89cc7 | -19.60315 | -56.75145 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 1d4aa5ba-451a-3fe6-abf1-8cf1058026d8 | -19.60225 | -56.73596 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| c5d22ebb-0505-3dec-ba49-441632ba8ad3 | -19.60061 | -56.62601 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cc0f5cbb-5235-3e58-8a05-70b3e8984e5f | -19.60012 | -56.72792 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 660e5bbc-ba64-3130-acfa-542d7d64cd08 | -19.59982 | -56.70874 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 635c05a5-2fc5-3017-aa29-af4a235e1929 | -19.59952 | -56.73164 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| bdbdb5c3-1a2c-3eb2-93a3-eb5439691edd | -19.59769 | -56.74279 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 239.0 |
| 275d65e5-a992-35f2-964c-ea15b426836f | -19.59739 | -56.7236 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 672b94d0-fd3b-3152-9bbb-71ed7df06b1b | -19.59588 | -56.71185 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9652fa48-1c76-3eda-a163-541e7561c52c | -19.59496 | -56.73847 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 4e42cc74-8145-3969-ac09-9793b0784330 | -19.59437 | -56.7001 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2867305c-c04d-3e62-b2f8-98d70109ed67 | -19.59345 | -56.72671 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 4353b723-5bb1-3c23-93e4-dcb5c478add9 | -19.59316 | -56.70753 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 50785358-334c-3761-8a04-b631e515dc8b | -19.59285 | -56.73043 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.2 |
| ee44fa64-d318-383d-8528-3fe69bca3564 | -19.59253 | -56.75335 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 23.0 |
| b68ddcb7-b64a-3794-af3c-02cdbe2c2bfc | -19.59224 | -56.73415 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 6fb94941-c0f9-3188-9686-899f7fef4d76 | -19.59194 | -56.71496 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c4c759a5-1a8e-3500-8616-ee54a4acdd98 | -19.59192 | -56.75706 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 25.2 |
| c21d6943-bd09-39ce-8ffd-3bd410a3d378 | -19.59133 | -56.71868 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| cd914737-af69-329f-a5af-351a5a50f43b | -19.59061 | -56.6242 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3bef6b88-9e2a-340f-bd59-639901f68ded | -19.58951 | -56.72982 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 25.5 |
| e7f1a3a2-99db-3ba9-b98c-3d6e814c7de5 | -19.58921 | -56.71064 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 84279aa9-a8f8-3dcd-b426-f6f5e4c5edaa | -19.58848 | -56.61619 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4543c5c4-f892-3452-b59e-d8475b0be6b3 | -19.58395 | -56.623 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0d832b12-5029-344a-841d-82ef4794c50b | -19.58261 | -56.73738 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 6909fd1f-ead3-3e7b-8417-bd51c98af3de | -19.582 | -56.7411 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ee832113-097b-3a34-92a4-7adf035b415f | -19.58168 | -56.7219 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ac885e4e-5cbf-3bc0-b069-1be4dc1a6e7a | -19.57621 | -56.71325 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f11fa760-064a-33ee-9c64-229f38e96cc9 | -19.57408 | -56.70522 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| db52c514-32d8-3b31-9e9c-f61fe3d300f1 | -19.57167 | -56.72008 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6223e52c-2c11-3dea-80f7-60ba8ee091d6 | -19.56861 | -56.69658 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ddf65861-bdee-3906-8b7d-772924c2a4d7 | -19.60121 | -56.62231 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 19836e7e-b83e-3e9c-b88d-d1b831d3dfee | -19.5983 | -56.73907 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 4b9d7e42-ed36-3276-afe2-d160ab0e1e04 | -19.59647 | -56.75023 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.0 |
| 29ac44cb-7123-38be-b311-0a95fd93aef4 | -19.59618 | -56.73104 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.2 |
| e8f7050b-764a-35dc-bd84-866196320866 | -19.59122 | -56.6205 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| faafe51d-4138-32cf-937c-58eaaba640e7 | -19.59102 | -56.74158 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 0c1febeb-a445-3ea9-a2c7-bf3bad971ce1 | -19.58669 | -56.62731 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 664eeef7-06ab-3f03-8cf1-4f127a9f23ce | -19.58621 | -56.71507 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bebae928-6c70-3a00-bec3-2f377d8b2d6d | -19.58617 | -56.72922 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 292e1790-0432-3b1b-9392-111eb9a0b627 | -19.58556 | -56.73293 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 66aa5709-7e3f-304e-b9b6-c1082d7eaba2 | -19.58501 | -56.7225 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b78a1ff9-bff7-37d1-9c6c-49d7c02fcc89 | -19.58434 | -56.74037 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| e1965616-f8c8-374e-9581-0ceb69f1a476 | -19.58348 | -56.71075 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4348531c-27af-3039-beab-502eddc80960 | -19.57801 | -56.7021 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6db2cd35-0b15-317b-97eb-e458cb8110fe | -19.57741 | -56.70582 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f13d66d8-330f-3f56-b25f-394833370172 | -19.57714 | -56.72873 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d5b457d9-bfc9-3223-8186-6e1e876f6e9e | -19.57014 | -56.70832 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4fa9628f-618a-37d6-b3d2-95de4b11c085 | -19.56689 | -56.55899 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fe259251-0b7b-3e7a-8593-ac4165bdf586 | -19.61771 | -56.70434 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2d307034-ccd0-3584-a5bb-0333ec2b6804 | -19.61256 | -56.71487 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f6ec9339-86c5-394f-ae24-154596eab44b | -19.61165 | -56.69942 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2369193e-b097-392f-96aa-bbf8dac72b64 | -19.60922 | -56.71427 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 936cf488-1d27-3b98-aef9-f212facfa4f4 | -19.59043 | -56.70321 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8a75565a-95ba-37d5-ba6b-a6ad903b4890 | -19.58861 | -56.71435 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 918bffa4-58c0-3082-9153-3962df07264d | -19.58788 | -56.6199 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 03a84bf8-06ba-3f94-802b-fb8dbd0b6482 | -19.58728 | -56.6236 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0b279429-d604-36ed-99cb-1055d27f2175 | -19.58408 | -56.70704 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 058973e7-01ae-393e-85f4-0e61d3a86113 | -19.58288 | -56.71446 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 694165e2-e269-36eb-8150-173078cc5d46 | -19.58276 | -56.63041 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d31c3823-36fd-357a-80d3-4dcc5053781d | -19.57287 | -56.71265 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 332a8263-b125-3839-8b07-5ee301c255c8 | -19.57074 | -56.70461 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ceb2edc5-803d-33e5-b633-56264c4b136f | -19.61862 | -56.7198 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c6416a70-6e20-3b89-9fcd-98b3464b5dbb | -19.61468 | -56.72291 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3e6ffaf8-60b6-3efe-bd27-5186e0d109c6 | -19.61135 | -56.72231 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| df6f2fed-9c42-3d59-a25b-8ae2ff059c67 | -19.61074 | -56.72602 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| d2944a3a-c278-33cb-8a7a-249d60817395 | -19.6074 | -56.72542 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 9780ac36-ec02-32b8-856a-1ea13cb90220 | -19.60649 | -56.75205 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 9f329849-ea16-3a04-be39-11b11b69b002 | -19.60619 | -56.73285 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 06774872-3c7e-3b01-8923-ba24e5aca45a | -19.60588 | -56.75577 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.8 |
| cba4b495-6b63-3f54-9a6e-934af318bed7 | -19.60468 | -56.7211 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b7fda7fe-489e-310b-bf90-7a43386424e8 | -19.59859 | -56.75828 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 48.4 |
| b7c48c7f-8661-37f5-8df7-1efa5f2d72da | -19.59679 | -56.72732 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 09049263-d3ec-3fbf-9825-218386015565 | -19.59526 | -56.75768 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 78d55100-5f74-3090-b1ee-63ba5177d54f | -19.59012 | -56.72611 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 25.5 |
| ce42e8c2-c906-35b6-89f8-b85373d88242 | -19.58919 | -56.75274 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 23.0 |
| ac91d4b5-9951-32f4-9972-9dc5bd9bf964 | -19.58858 | -56.75646 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 25.2 |


[Clique aqui para ver as próximas entradas](README44.md)
