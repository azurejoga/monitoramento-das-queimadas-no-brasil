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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f27267cd-daf1-33e2-bd3e-9a79cbb7cf04 | -9.16836 | -59.67042 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a5c5565-e946-3f07-958d-9c1c37da1d60 | -8.53937 | -54.74069 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 331c7f3e-d021-3817-88c1-33b6c9c18e97 | -8.90219 | -60.55096 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c49ad6d-a3c9-313e-8cf0-7fefdd179f16 | -9.40588 | -60.59008 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c78ec44-3f91-38f6-bcca-be1a3370a701 | -8.10383 | -51.6591 | 2026-08-19 05:23:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d83fa79c-2326-35e3-8574-a6d02d8d865a | -9.21492 | -60.81509 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f0609bd-93bd-3cb8-89cf-5d48346b988f | -9.44428 | -60.2955 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25f560ad-b690-3823-9e92-5e0751d5079f | -8.58498 | -54.73567 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48e13529-e952-31dd-b735-839105dfdfbd | -9.54792 | -56.79488 | 2026-08-19 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 647fd283-6b5d-3887-af8b-17e99a7d5035 | -3.68532 | -47.65323 | 2026-08-19 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f3c6e82-d6d3-3fa3-b060-d73bc446ffaf | -8.54193 | -54.75444 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27a2dd18-ea54-354d-b0b5-2f94ffb9aa7b | -8.57957 | -54.67959 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b713b03-bcee-3217-914b-d49936e9b18a | -9.39799 | -60.5528 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 55f4a29f-6d7a-3c38-a125-b602fce5aff6 | -6.86352 | -59.03479 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cadfebad-b71f-3def-b6fd-cffe4d71d3cb | -8.9456 | -60.51096 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5627e382-8fdb-3387-ae4e-bae7aed645ce | -9.01585 | -60.49678 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c4b7304-8c1d-3381-8964-80ae52870731 | -6.85455 | -59.01904 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32019df8-6f0b-36ce-8fa2-58ca84c78159 | -6.8011 | -59.44744 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2349ae0d-c0d6-3a6c-9154-e15c2edecab9 | -8.56772 | -54.76265 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 089bac25-6c23-3675-a430-78a88cbdb846 | -8.53237 | -54.72649 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e27145e7-1e9b-3fd9-ae3a-f9c6e2eca06a | -6.7549 | -59.17183 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74ac050b-fe65-3207-acb9-d0165b7c40a4 | -9.17984 | -58.06896 | 2026-08-19 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0f6c2ed-88ef-309b-961e-2739b24aec72 | -8.57019 | -54.74533 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 987b4eae-a0aa-33e8-a24b-5fcd3175ae71 | -4.00471 | -48.05953 | 2026-08-19 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff75c61d-4c0f-322b-ba9d-9a2a3d2fbd52 | -9.01017 | -60.44539 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de56e3f9-4d47-30a1-b479-184d89237e2b | -8.58617 | -54.72691 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd491c72-8334-34c6-b667-c321b7d1b2b8 | -9.54721 | -56.79988 | 2026-08-19 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a622ec3-82c8-3899-9ec2-c84710f2c0ac | -8.56877 | -54.7558 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0cb1df44-4353-3852-9161-1534e26d30ec | -8.90177 | -60.59754 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33557d45-9545-3b53-87f4-39256e69cac7 | -8.57645 | -54.69882 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dae1ce5-afd8-3e65-8ae0-eb1cc953805b | -6.95752 | -59.03417 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ab7805c-7e0b-3eb0-8ac0-d05b6864ad55 | -8.55123 | -54.72038 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3990924a-976d-359d-888e-130b0fca50b7 | -9.39691 | -60.55984 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 43d123fa-d538-3ae7-b530-b0658c01e210 | -8.95527 | -60.58072 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b3f9072-4f5a-3bd3-9755-41efe16eebe9 | -7.07886 | -56.4879 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c35cf7e-e31d-33ec-acc3-f44bcc5dafd2 | -7.42925 | -60.03006 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44648339-d617-3c3d-8bc8-5ff1b9ee822a | -8.98926 | -50.70321 | 2026-08-19 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2258b521-227a-3630-be61-dc73f1b7f87a | -8.57649 | -54.73274 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cb0794a6-dc12-3334-b54d-bfd26e2b925a | -8.50876 | -54.86318 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2652efca-4b59-357e-9285-d62fc835182f | -6.89015 | -59.04256 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f6c22a1-aa4a-318b-9ab6-0a11ee938628 | -7.60186 | -60.95495 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6189b0aa-4382-3ebd-aa39-0bfd53d0470a | -9.42525 | -60.4197 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 71f9a159-8cd1-39c0-bf50-4be82f5ac817 | -6.77315 | -59.45816 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9daf0f78-8a9f-3c25-856b-0640ab618596 | -8.55565 | -54.721 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 91fedf1d-555a-3315-b38f-381939f76960 | -8.55892 | -54.76136 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3f58316a-f9fd-37b4-b59e-596fdf122109 | 1.67779 | -60.13594 | 2026-08-19 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 323e1a84-304e-3293-8ad5-8bdced92f3c0 | -8.55882 | -54.76297 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 85201e93-7a3c-3a62-b6ad-bc702aedd084 | -8.09846 | -51.65808 | 2026-08-19 05:23:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4b86975-a7e1-3a20-b545-775e194de19b | -9.39304 | -60.56285 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 31159338-7466-3c9e-914b-d1403c43adcc | -6.96946 | -59.3039 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bc5ae58-b959-3dc8-80b4-180fbeb3b637 | -6.74168 | -59.0465 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f40821b4-5410-30c0-a506-1afde6f3b2f0 | 1.68865 | -61.08179 | 2026-08-19 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4be525ff-eddd-32d9-8fcc-a71f5bd35e30 | -6.74676 | -59.03604 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 205c8a25-9be6-3b64-b057-cdd669cc4ede | -8.58057 | -54.735 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3300d82c-0681-3430-a33c-6f576dd6f38f | -6.81009 | -59.45615 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcb7c799-0478-3fd8-8ec4-c342dacb4da2 | -3.09849 | -61.21709 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a3eddc3-01e9-327d-85ea-69793583cb10 | -8.90164 | -60.55446 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c493e61-16ef-3434-968a-402684deafe0 | -8.22047 | -55.03623 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b74d70bd-156b-3495-b8ac-ccaa64520542 | -7.88462 | -61.19162 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff32023e-b039-3fd0-8997-40c3e6b01e21 | -6.8783 | -59.05201 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 810f5111-2e7d-3ced-b728-da020dda5a75 | -9.40634 | -60.56493 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23b00859-7aae-3090-97a9-749ba64736c8 | -9.41307 | -60.5876 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44f3ca47-fd6f-3165-8f8c-b076ba33e95f | -8.57823 | -54.68567 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b66aeb85-6b4b-325e-a6da-240a8cb8e5da | -8.53435 | -54.7444 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 649c5a56-aa13-3743-bb76-b3d38d417cb7 | -8.5665 | -54.77115 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 976e890f-0d90-3790-8ef3-2fd32f411771 | -8.57397 | -54.75034 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f08eac20-c382-3e0c-b278-e2cb7c5b5b4f | -3.45963 | -56.80564 | 2026-08-19 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 054aad39-eca6-3ab6-b03e-944dd676c52e | -3.22484 | -61.25856 | 2026-08-19 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8721bded-30cb-301e-8b89-3ff6502b6db1 | -6.84435 | -59.01751 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d875af72-4c0c-39d2-ba7c-e191e8e106f1 | -9.21161 | -60.81457 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0de9bc3c-3305-33ea-9cb5-c0d8bdb3f6b3 | -7.05442 | -59.83879 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 62d3756f-1288-39e1-855c-365d303ed6d4 | -6.84491 | -59.01387 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6443840e-b47f-39d1-b89c-36bd64af18e8 | -6.7966 | -59.43983 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28600da0-0345-33bd-ac9c-2eccc0246d3b | -8.56006 | -54.72166 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 58712446-cf17-308d-a255-084f4bccc216 | -6.88343 | -59.06403 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 446efdf8-5dd4-343a-9c1e-7c8d648e6e5a | -8.53692 | -54.75811 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| db480b16-8504-3198-b7ff-2989c5253979 | -7.56577 | -55.56931 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c38889d-aaef-39a8-a703-21d5313dd987 | -6.76553 | -59.14733 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 284f9f2c-4c2c-37bb-834d-a48de00dd4ae | -2.74479 | -54.59517 | 2026-08-19 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c5a4f23-b897-3f6e-a5f3-d2315df84aa1 | -8.55938 | -54.75882 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08bb7a5e-d605-3f66-bc95-896115a248ee | -9.14052 | -60.61365 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1052525-7279-3f39-bac9-81a2c7222244 | -6.75089 | -59.15255 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ae12f3a-74cd-314d-9242-b1a2a5800b5b | -6.7462 | -59.0397 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79343f49-87f8-37d6-9373-2c3df6db35df | -7.90529 | -61.73038 | 2026-08-19 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edeee253-ace8-3b3e-8d54-ef4528cef743 | 0.30775 | -60.44497 | 2026-08-19 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d312b1b2-533d-36ff-bcd2-092b7aa06e65 | -6.88051 | -59.03738 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c5aae39-4ab8-32bd-9578-2ad5301b9b26 | -6.85059 | -59.02219 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65ddb1f1-8c43-3b03-ba15-88ab91e22195 | -7.55808 | -55.56443 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61001eb6-b855-33b5-9967-e15f65d5f2e0 | -8.562 | -54.73966 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ab40453-45f4-3c38-8a8f-044bc82df7c7 | -9.4635 | -51.62953 | 2026-08-19 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e7877b5-5631-3d70-b1ec-9dba190a8742 | -3.42862 | -51.5153 | 2026-08-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d9d6cac-4ffc-3b2c-b5e1-f052a701eb2a | -8.5601 | -54.75306 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 193c5c04-168c-322b-9f9e-5f26e9027dce | -6.89337 | -56.43668 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3ab40fd4-4d60-3d1e-a3e2-de34b0e3453e | -8.57523 | -54.74155 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0177f12-f621-3ebd-9126-597f57d4c437 | -2.3267 | -60.06354 | 2026-08-19 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b7ba3ae-4ce6-3bdb-a137-64179d7043fe | -8.90334 | -60.56549 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42a1fa69-f9e8-3986-910a-e28518b6cbe0 | -6.64661 | -56.34657 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2cad77f-abf7-3d51-8ef3-a0a64c638fb2 | -9.11012 | -60.39223 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ea90d3d-06a6-3b6b-9ceb-93d6cb0e31a3 | -6.88738 | -59.06089 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2b8b744-d1bd-3e6f-8f6c-4c690a97e535 | -3.09514 | -61.21657 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README50.md)
