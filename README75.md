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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13f3d451-cdf5-31a1-9df0-0acf265c3dfb | -9.1173 | -61.58873 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67b402f3-a3ea-397d-9ee5-b8fced13d7e3 | -10.52817 | -50.77955 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cf8dd2f-d437-3494-8870-9a93d6dafc5e | -9.12411 | -61.58986 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87a58137-18d7-3749-9d30-ffc20a04425c | -9.0493 | -60.44828 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 689d8f04-0a13-3557-b6a1-2a1f9be5b3d8 | -7.3942 | -64.63451 | 2026-08-22 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e1c2bf1-f84e-3337-8f26-9e00b30ab6fe | -9.41599 | -60.42877 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 796acae7-1b71-3cb9-b4fb-afc2310af394 | -10.89823 | -50.24036 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d76a7dd-245c-3d8e-be1c-2788bd26cd76 | -8.89071 | -60.54561 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67dae1fc-234c-3002-b096-32665a858b75 | -9.21276 | -59.76252 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e89344c6-909a-30e5-bacc-1f8301b13c4e | -9.16621 | -59.4552 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 81fc6bb9-5960-3848-b7cd-d5563a5b2b69 | -9.21475 | -60.77225 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4cb4d75-2188-30e0-a3bb-98aa77988275 | -9.04914 | -57.07021 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec502bb9-e4f9-38ec-a88d-ebd7bcef1d4e | -8.89014 | -60.54914 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03e48c7d-b147-3c17-a9ee-87a9d52e75fb | -9.11205 | -60.33263 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22adedb9-d08a-3ec5-96a9-693a6226c1a1 | -9.21751 | -60.77635 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00588251-2108-33c3-b0dc-bfa313b0ba0b | -9.16749 | -57.00515 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb1f436e-7021-3225-92b1-80ce204e3295 | -8.67808 | -62.87667 | 2026-08-22 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be6e8036-ae1c-35a9-b9af-462191fb4051 | -9.43797 | -51.61504 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2b911f0-8728-38a6-bda7-3e5106319d1a | -16.28864 | -57.66489 | 2026-08-22 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f801f6bc-1282-3271-bd68-f03d43917d46 | -9.43543 | -51.63442 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f00d294c-9a4f-3bd1-8861-7ec425e905cb | -9.43343 | -51.60956 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4c186e3-0768-3bcf-a8c6-3abc84ce355b | -9.44227 | -51.62111 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 743119d1-9652-39f1-91e6-630027b90de6 | -9.17395 | -59.47074 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9aff10a-eed3-3f49-a2d0-fc395f86dbf7 | -9.12351 | -61.59357 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 701c91ad-8702-3407-bc12-2a0d83b721a0 | -9.15958 | -59.45415 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1ca7468e-d13c-3ebd-966d-f2cb6a37e3a0 | -10.80891 | -50.97546 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2461e6e-6e32-3247-8ff0-3c4af807dcdc | -8.95164 | -60.59168 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ab077b8-52b5-3853-92ad-f7fe5d8ddd5d | -8.40565 | -62.68484 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 469055d7-4cda-3bc4-8fc9-dcb86d74cc85 | -9.39913 | -60.55573 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a21431c6-82e4-3b65-9527-12121e07bd6b | -14.49857 | -59.82593 | 2026-08-22 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4035be17-9bb0-3a41-8465-ff0f7268a2ca | -10.8784 | -50.22998 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbff9857-5588-329a-a240-2696f8a00e51 | -10.79203 | -50.98008 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2eb428c7-bf96-3cbd-bc0f-cdde2bec9e78 | -9.16952 | -59.45574 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 40fe5407-f9d5-35d5-bd24-d0e6fdb21b87 | -9.42355 | -51.64421 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4464e3e6-4a0d-3273-957a-f29d078f4a31 | -9.16981 | -57.01375 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c799bc1f-2f4a-348e-89fe-3840e725a6e0 | -7.81561 | -61.77815 | 2026-08-22 05:25:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad9e67a9-249f-38d5-9fc7-26c77f8c86c8 | -9.04853 | -57.07423 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cefd6d6d-50cc-3439-884e-ec52f957dff2 | -9.15904 | -59.45765 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a302a823-e8ce-3137-858b-780acdf2e515 | -9.2089 | -59.76547 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d19b3740-d719-3e77-99dc-4a6dd9d30f53 | -10.80358 | -50.97476 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e943db2-a69a-3fb0-adf4-27318eef5e56 | -9.4088 | -60.43121 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c8e8de1-d723-3779-8ba9-404b81e489f0 | -10.51181 | -50.82262 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55fbbeaf-8651-37fd-9b05-882c1d19fbef | -10.8138 | -50.97952 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5e12a993-fa7e-327f-995c-dba867ff59f3 | -8.89347 | -60.54967 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17adc366-4411-3996-94c7-76a407bf1bb6 | -9.05327 | -57.06676 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6ca8845-c421-3af3-8e7a-68af360fb81b | -8.39061 | -62.68661 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 29ad190f-a74d-30c6-9bb8-65ba4923a28d | -9.04822 | -60.43373 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e7269f9-5fb4-3e6a-acb5-141211265c6c | -15.67851 | -53.77942 | 2026-08-22 05:25:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39bb56d6-b8c4-358a-8722-121daa515e71 | -9.21111 | -59.77296 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 774ea89d-3bbb-3eaa-8138-3e63fd26a575 | -9.1195 | -61.59673 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f82efe6-9194-31fb-a658-c66fdaae22e1 | -10.04168 | -59.45885 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17346faf-4022-35f1-b388-08612dcf0d42 | -10.80847 | -50.97882 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| deba5cb0-2e84-36a1-abfe-77bc95a0b35b | -10.07458 | -60.4963 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae7df752-8433-343a-9b78-37cf7192d5ec | -9.41467 | -60.54383 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e98ebed1-b6e5-3331-95f6-0d58e57e83d3 | -10.68447 | -50.30082 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91cbb249-e8b7-3f83-b10b-e5ee7fe7d362 | -9.39857 | -60.55925 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd987b0b-7d8e-3d18-abba-fb99e2b0f9c5 | -9.1194 | -60.39124 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bc854ed-6ade-345c-8748-bbe110ad4cc9 | -9.21331 | -59.78046 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f4b6f24-67b7-38e2-b0bc-2af6a1de10ce | -9.18222 | -59.46134 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b153324f-d942-3fd8-8c12-b4ccc471a6e2 | -9.4094 | -60.40612 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0714e5ea-a35f-357d-b828-22d84d7c390d | -9.23544 | -60.38879 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46065c48-d849-3cd6-8e2f-163b29b31219 | -11.5998 | -46.54602 | 2026-08-22 05:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d666ba42-20ff-36e3-a3c8-7ac2f07fd6d9 | -8.39129 | -62.68248 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.2 |
| b1a3438f-607b-3776-a6e6-02ba74843927 | -9.39463 | -60.58388 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d99ba96f-6368-363f-9dfa-250729ae8a84 | -10.51432 | -50.82296 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62321330-cf9d-3454-8845-50230acdaa15 | -9.1938 | -59.45246 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f105dd7-8793-304b-bbd1-d435ae0584ed | -8.3358 | -57.68586 | 2026-08-22 05:25:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8daff227-1461-3701-b916-0ff1cd527281 | -14.3937 | -51.8012 | 2026-08-22 05:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| fbd13230-084c-3bfb-b90e-331cd20f5678 | -9.1724 | -59.4436 | 2026-08-22 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ca8c0234-4d4c-330d-98e8-603466876c20 | -8.3904 | -62.6774 | 2026-08-22 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 192.4 |
| 7548cd16-46f1-3877-81e9-d8bd4c4f100a | -8.5404 | -54.8398 | 2026-08-22 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| dfac526c-02e1-3b76-965c-dc805c050d56 | -6.7692 | -58.6679 | 2026-08-22 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| a37b54c6-e92a-3fa2-8088-13451a374ded | -8.3903 | -62.6963 | 2026-08-22 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 3c2cec47-76b0-319c-b8e8-588c5e075281 | -20.6358 | -47.4322 | 2026-08-22 05:30:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 73.5 |
| edf59a44-499f-3f0d-be8a-93c2288620f0 | -6.7691 | -58.6873 | 2026-08-22 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 7d84faba-d7c9-3e0f-9318-043178ee9698 | -9.1722 | -59.4629 | 2026-08-22 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 3b620093-a015-3fe4-b18c-1e014c1fb999 | -6.7507 | -58.6687 | 2026-08-22 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 35a62181-829f-39a6-9d69-2f553271402e | -8.4089 | -62.6767 | 2026-08-22 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 265078c9-272e-3649-8dae-6357e48654bb | -8.4088 | -62.6956 | 2026-08-22 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 778f3f4a-47cd-318a-b93f-0f51a36a24a1 | -6.8188 | -59.6696 | 2026-08-22 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b998e010-d2bc-3a7c-83c3-f454effdd830 | -8.5406 | -54.8197 | 2026-08-22 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| f102db91-bdc3-3980-b8f7-f727cb006651 | -8.522 | -54.8209 | 2026-08-22 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| fb98c67b-f3ad-3435-b8a3-27ad3409146f | -8.522 | -54.8209 | 2026-08-22 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6663d13e-7e2c-3957-8609-1e8e9c48eedb | -8.5406 | -54.8197 | 2026-08-22 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 11728cac-ff92-316a-9c7a-f68cb84a116b | -6.8017 | -59.4394 | 2026-08-22 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 295e02d7-24d1-3642-b893-ac4610ae713f | -8.3903 | -62.6963 | 2026-08-22 05:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 195.0 |
| 9e1d8484-d467-3299-9349-6d86b22822bc | -8.5404 | -54.8398 | 2026-08-22 05:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| c5852041-17d2-3717-ada6-602589e8db3d | -14.3937 | -51.8012 | 2026-08-22 05:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| a5d8e79d-44f0-384a-aa35-f9a803b20cb7 | -6.7507 | -58.6687 | 2026-08-22 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c876effc-f745-3dab-bc19-44f1bebb7d67 | -8.4089 | -62.6767 | 2026-08-22 05:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ec7f44d3-865a-3702-b3bc-d0015f8fe1cf | -8.4088 | -62.6956 | 2026-08-22 05:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 6d0513d2-c2f2-32d0-a8ce-62827934890c | -6.7691 | -58.6873 | 2026-08-22 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ff712c76-ce17-32b0-8a8e-6944593562c9 | -8.3719 | -62.6781 | 2026-08-22 05:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9359c50b-6176-30f1-8004-03e946762c3e | -6.7832 | -59.4401 | 2026-08-22 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 8358e37a-5788-333a-915d-606a42cd08fd | -6.8018 | -59.4201 | 2026-08-22 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 248.1 |
| 06ca48fa-6981-3d4f-8f96-6eed822f9939 | -8.3718 | -62.697 | 2026-08-22 05:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4c21c338-d361-310b-9431-cc35a16d29c1 | -6.7692 | -58.6679 | 2026-08-22 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 85a642ec-0caa-3e99-901e-c12025f7f97b | -8.3904 | -62.6774 | 2026-08-22 05:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 169.5 |
| a0786dea-d028-3179-b5e3-f901c7c9307c | -9.1722 | -59.4629 | 2026-08-22 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 8278aa3b-a3cd-3e01-b990-3fd565541768 | -14.3744 | -51.8038 | 2026-08-22 05:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |


[Clique aqui para ver as próximas entradas](README76.md)
