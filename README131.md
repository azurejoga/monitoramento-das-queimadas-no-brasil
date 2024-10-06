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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47388017-dfc1-37fc-ac4c-ffbadb14adb4 | -7.14589 | -59.2971 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 767d6384-6499-310b-ab78-c9ddb7c45bf2 | -7.14198 | -59.29651 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b46ef153-39e5-3a72-889e-73e2d347101f | -7.13807 | -59.29594 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28591643-bb6f-3621-9aed-8bac4929bbca | -7.13734 | -59.30087 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fb976240-740d-3a06-adca-dc04412d3e75 | -7.12522 | -59.4878 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abaf9423-b516-3152-999e-ba4dd771b93f | -7.06168 | -59.29964 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c2a0699-d23a-3f0f-975b-fa29939c051f | -7.03373 | -59.40752 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4150e2d4-80cb-3b24-9c63-449fe2d075d0 | -7.03131 | -59.39725 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80b4b78e-eae1-3381-914f-9539fcce3328 | -7.03058 | -59.40211 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 073c51c1-4d1f-33d6-bb65-44da0b18409f | -7.02985 | -59.40694 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d719197-d1df-3795-855f-7a04852e1195 | -7.02913 | -59.41177 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8df01627-d39c-35de-a103-17ad5380d010 | -7.0267 | -59.40152 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a3f4c84-f197-319e-957b-e3279950eaa3 | -7.02598 | -59.40635 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d4f0880-91c7-3b01-8cb3-fe5d689ce61d | -7.02283 | -59.40094 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c46c1663-0d26-3c29-9057-c70f6cb92571 | -7.02211 | -59.40575 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ba07ac5-cc7b-3864-becf-fcbe80d9e5df | -7.01895 | -59.40036 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 284942ad-ca03-39ca-99cf-2fbf751f9164 | -7.01823 | -59.40517 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16eb6938-18b9-3b6e-a0d5-b8e2439172b4 | -7.01771 | -59.35557 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6b4be65-20f0-37e3-8e5f-8bd16f58c4a6 | -7.01698 | -59.36044 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33a0bdd2-bc30-386f-a3c1-93423550cd33 | -7.01507 | -59.39978 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a5d996e-2f7e-3ac8-9416-0a306fbe9915 | -7.01336 | -59.38474 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96acf5cc-f9d6-35ad-b82c-7cd71795f6e6 | -7.0112 | -59.3992 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42e8e10f-147c-3901-852f-bfd8bf51568f | -7.00632 | -59.37869 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b775a9b-6cc4-3e84-8891-5009b8ed67ad | -7.0056 | -59.38356 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36094143-6e4d-359d-ab66-9e1605f4456f | -7.00244 | -59.37811 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48faa5e8-1a90-3b15-8398-65ebec20381c | -7.00172 | -59.38296 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c2156e7-47cd-3166-bc14-cbce6b19a526 | -7.001 | -59.38778 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 533127c6-990c-3c23-addc-8590d51e9089 | -6.99856 | -59.37751 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cc7aed3-1fe2-3bd1-84e6-075abeeac07e | -6.99784 | -59.38235 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62323fdb-03f6-3493-a1ec-5de4037d7285 | -6.99713 | -59.38718 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33b33c69-8c02-322b-bb74-b47e254038cf | -6.99468 | -59.37691 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c89b6adb-88ee-3e19-b2f5-7469c0b39700 | -6.99397 | -59.38175 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ac77696-5f43-3d48-8041-8f0b84d0265d | -6.99009 | -59.38116 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f79a318-6917-350a-979d-f6925f9e62b4 | -3.78539 | -60.1223 | 2024-10-06 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4099be69-413c-3fb0-9e6b-62eb1a40ab76 | -5.98781 | -61.79835 | 2024-10-06 05:33:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7a70539-5c57-3856-ba2d-b4646a98dd9e | -5.49674 | -60.462 | 2024-10-06 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb4d1046-e244-3c7a-b271-1916eeb3606e | -5.0562 | -62.50951 | 2024-10-06 05:33:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b985597a-4d81-39a9-b7a6-68be511ab65d | -6.4445 | -62.86097 | 2024-10-06 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1f93da6-4332-3b3b-8b8c-2ebad959612a | -6.44396 | -62.86448 | 2024-10-06 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfe94aef-609f-3cfe-97d1-f8f35061bd1f | -6.44341 | -62.86799 | 2024-10-06 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67780f36-b750-3b87-ab44-a395f52a492c | -6.44062 | -62.86396 | 2024-10-06 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dd4a816-9cfe-32e2-8562-54ae7c16fd29 | -6.25865 | -62.46396 | 2024-10-06 05:33:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8123e802-512f-33b7-b61f-57879ac87d1b | -6.98412 | -62.91276 | 2024-10-06 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d64a77c-de93-328a-a254-82e25d152d0c | -6.98078 | -62.91224 | 2024-10-06 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5679807-dde3-3f36-a233-83658c9e340d | -6.98023 | -62.91576 | 2024-10-06 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe787e89-1a81-3243-af2d-8e665c67c902 | -6.97967 | -62.91936 | 2024-10-06 05:33:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45bd7351-e178-3994-a744-eca5b4a28956 | -10.26666 | -67.35509 | 2024-10-06 05:36:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d6d2fba-5ef4-3a0f-b780-9078b720ad87 | -9.29249 | -65.51791 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21c2648f-7f60-3c24-9c11-96b466141981 | -9.29109 | -65.33342 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b680a5f-771b-3a6d-b3cb-baf7c8cb82fe | -9.29012 | -65.42518 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6f862a4-ca21-3a32-bcfd-7593ba0fad8c | -9.28675 | -65.42464 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85ef552d-7874-3322-8ad4-fd812eec404c | -9.2806 | -65.41997 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e2dcee5-6062-3316-8b4d-f0542841c133 | -9.27247 | -65.3634 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8f01804-3dd4-3792-b88e-a83be3c3f34d | -9.27189 | -65.367 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 979068f9-f5e7-3633-b9c9-b6a1b7b81de4 | -9.26911 | -65.36285 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e847d05-ac21-3c3a-8352-71708321e2c0 | -9.26853 | -65.36645 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e60294b-f422-3044-bacd-0396c99efbae | -9.2492 | -64.3228 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f641beb-9766-3432-a559-e6e7afd72b18 | -9.24077 | -65.6022 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06512ccf-1fa8-3293-909e-a73082b0d4e6 | -9.24018 | -65.60582 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0d729d-d04c-3512-a9ae-fbf9cf5da0b2 | -9.95499 | -65.24698 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c646e63-105b-34bc-b9fb-15e37902181e | -9.95165 | -65.24644 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 379c7af2-6b83-399e-8d4a-8a8a953cca5e | -10.67605 | -64.79879 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb442623-00b4-34f2-a38b-14e9ac4f34ba | -10.41845 | -64.86896 | 2024-10-06 05:36:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cd02b8a-2140-3d55-a901-e0505164d2a5 | -9.6883 | -64.62962 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.5 |
| e0421abb-9d53-3d2e-98a6-13d147fbd94b | -9.68775 | -64.63313 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 550fd001-5449-34b8-a42c-c92a728348ff | -9.68553 | -64.62558 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c9d171ae-ec24-3727-a6c8-f1e4355eaa01 | -9.68498 | -64.62909 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.5 |
| b777ee25-796d-3dcb-9c01-d2cbb89f4f7e | -9.68442 | -64.63258 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.9 |
| e7a9f998-1e46-3cb2-8ee6-121ec5fe0c93 | -9.68221 | -64.62505 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cc40375c-c911-3d39-a366-319d9d991d24 | -9.68165 | -64.62855 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3d14a8dc-06ce-308b-a71f-f98a03832dfa | -9.5062 | -65.60064 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b9dad6a-1c80-37cd-9b8e-37b15ed528d1 | -9.50562 | -65.60426 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68579e98-242b-3d47-b19a-f67ddb4d7de7 | -9.47221 | -64.72742 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da627ddb-1587-324c-b95e-944f319b3664 | -9.3775 | -65.46836 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 477935a8-5c2f-38c6-9005-1ce20dd08b28 | -9.36937 | -65.51875 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f5e7148-d097-388e-b743-c0d53f7b7954 | -9.36716 | -65.51099 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5d5cb92-f612-36b6-8648-770515e71e6c | -9.36658 | -65.5146 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81add37d-5f10-35e4-9364-8f1e5d0290ed | -9.36321 | -65.51405 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3dd7f2c-44f7-38ab-8b8b-b4bf74cd6981 | -9.34789 | -65.43092 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd1ca441-6c5a-30b1-aa58-eeaabcf1882f | -11.66387 | -65.20804 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06445088-0a54-3597-9411-d9f390e24aa5 | -11.60475 | -64.99935 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4faea429-bb54-3150-b0ff-17a6553d8226 | -11.60419 | -65.00288 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6d31765-30c0-35ad-bba4-3a68173f909d | -11.60086 | -65.00233 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e61d06b-3c1e-3237-a227-1f6427afe69f | -11.58581 | -65.01827 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6db4746-a19a-3343-a20d-ee37e480e91d | -11.54299 | -65.13787 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd1efa5b-9bad-3ca3-a209-cdca132fe5c2 | -11.53587 | -65.05354 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f4396b95-7913-3a22-ba3b-4f40e014f7da | -11.53254 | -65.053 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d2873848-7dcb-3efb-97f6-563ff9406707 | -11.52921 | -65.05246 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e4a32bde-4a5e-37d7-a1f2-c9577971368f | -11.52866 | -65.05598 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5bafdffc-134e-366d-ac90-dd9752cfd71f | -11.52589 | -65.05192 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 62213106-146a-3c37-8f59-2b5b996d00ab | -11.52533 | -65.05545 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8400bffe-cdcd-3493-bccd-7cf086aa7fbd | -11.51475 | -65.10068 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aedaa9c8-af4e-3645-bf0c-fadf4cca0b05 | -11.51198 | -65.0966 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3c279e4-f15c-3059-a41c-3a9107f533b0 | -10.83428 | -69.56519 | 2024-10-06 05:36:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fee9e2f-e553-3efe-bb11-6577a86cc90e | -10.83341 | -69.56544 | 2024-10-06 05:36:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74e32bde-ba8c-3727-8af5-09d329cee549 | -10.63082 | -69.63043 | 2024-10-06 05:36:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbbb73a9-4a8b-3874-8096-ea16e15591e4 | -10.62679 | -69.62973 | 2024-10-06 05:36:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 522b81e4-02d6-3b66-b0f4-fc1e74c3efbe | -10.01864 | -66.95675 | 2024-10-06 05:36:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d890221e-52fe-3f47-b235-c27d1573133e | -8.86632 | -67.48405 | 2024-10-06 05:36:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dbc11ca-f0b6-31d3-bc54-6e9bf2381987 | -10.86355 | -68.24245 | 2024-10-06 05:36:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README132.md)
