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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42af0886-2ec2-360c-9ef8-7a108f66e758 | -9.26831 | -60.79185 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77a18222-9210-3290-b659-073d4dde3580 | -9.25541 | -60.40977 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5059c98d-97ca-3ecd-a516-18902e479828 | -9.25389 | -60.50027 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4ba2f6c-fc98-3279-ad89-55533ef19e4c | -9.25345 | -60.47424 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e73a6dfc-5c2a-3775-a300-87b6788596a4 | -9.25338 | -60.4771 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1628515-3dc3-367e-b3d8-3da2b5d0be1b | -9.25277 | -60.4788 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ffe3cd0-9356-3529-a426-c69908ec26d0 | -9.25015 | -60.49971 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14ffeba2-8b37-3ddf-952a-4fc639adfa96 | -9.24964 | -60.47654 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6b86165-bbbc-3983-be96-f4bdbca5bbe4 | -9.16107 | -60.66102 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc85dcef-434b-3733-bbf7-47a8b3db227e | -9.79981 | -60.47517 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8818fc7a-d93a-3e6b-bd6b-0464e5dfc263 | -9.79912 | -60.47975 | 2024-10-06 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab4a4515-a981-3989-9645-3d8e995b3d7b | -9.48458 | -61.01436 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee0f8c30-1fa4-3300-bd03-c18177b2bfb2 | -9.48094 | -61.01379 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 291b148b-b46a-376c-a1a8-a237c0c30a4c | -9.39188 | -60.91484 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af516f72-d184-32cd-b161-445678eee84f | -7.28137 | -61.08885 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d41f54b8-a99c-3df2-b1b9-58587f60bfdc | -7.27782 | -61.08831 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf00cd20-9a47-3510-9537-31baacc8026f | -7.27722 | -61.09231 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 876818f9-e1e5-3530-957b-8f895c58c05f | -7.27661 | -61.09631 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b70d53fc-98e6-3aa0-9172-5056326e3d59 | -7.27367 | -61.09178 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce433fed-23a3-3b8f-88f1-437922c4bf6d | -7.27306 | -61.09576 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d154e733-bb64-3788-937b-8eb0ee39bcf9 | -7.26951 | -61.09524 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c02030c7-a4f4-3dde-834b-2f8dbf5db3d1 | -7.97935 | -61.40279 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d351c76-9dc4-3686-a937-19ddacc08236 | -7.97643 | -61.39829 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9c3093c-311b-38f5-91a9-da6cf285efaf | -7.97583 | -61.40224 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b30dd86f-6897-3f97-925d-57af25fdb17a | -7.93025 | -61.27467 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c8eb6f6-08c5-3f1a-837d-cc433b1d56fe | -7.92964 | -61.27867 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8d88d8f-06aa-3ca6-a7b7-4adf841ea137 | -7.9261 | -61.27811 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d4a21b5-2bfe-38a7-9758-0a2fa411bfd1 | -7.89936 | -61.524 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32347362-9560-3696-89bf-66ce48039436 | -7.89249 | -61.47506 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39182cf2-d0a8-30e5-a488-ee88235e11c4 | -7.98055 | -61.39487 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3508859-7ce2-37a4-aca0-2fac35889a68 | -7.97995 | -61.39883 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11dbd325-511e-3b7f-9197-657948a8dd66 | -7.97702 | -61.39433 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb68aff6-aefa-3633-9ae8-8774b6d23540 | -7.92732 | -61.27013 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7941ead-f4d5-377f-8431-9ce0fe74fdf2 | -7.92671 | -61.27412 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b6ec870-39de-3bce-aa88-0f918183cf46 | -7.92317 | -61.27359 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c8975a9-b2a9-3b0c-ae78-c38efacbee8e | -7.89996 | -61.5201 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 000e565f-f058-3f7a-a9e8-eb50ec772cf7 | -7.89076 | -61.46278 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d86de3e-b8dc-3126-b99e-bd8b7ae9bc7b | -7.77365 | -61.09201 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| dd3ac0e2-4091-301d-b333-3d55976dffef | -7.77008 | -61.09146 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 320947ae-a957-3078-bc49-78c31575114e | -9.25215 | -62.24625 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 888442f5-b385-3253-871b-1c7e06b1bbd1 | -9.17886 | -62.29748 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56435c50-6f5a-38f4-9861-2e18c225bbc7 | -8.99935 | -62.41946 | 2024-10-06 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a7a0d29-cf97-3818-ba46-3236652bfac4 | -8.60064 | -62.40509 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e164e134-59ef-3618-962f-4bcc88b05c7a | -8.59666 | -62.40826 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0edfb13-f4b0-3720-b280-e217e9ca28fd | -8.59553 | -62.41562 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c37f0de9-1e8d-3d35-9793-46bb0b9c3f7a | -8.59212 | -62.4151 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f52a8785-5181-3298-ac9a-5978fa027d15 | -8.56547 | -62.45242 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ade67474-8fc2-3ea6-9edf-42a639229661 | -8.56206 | -62.4519 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c18071bb-ab6e-334d-8cbc-517f9fca5316 | -8.37501 | -61.5478 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39675931-d83e-3339-b3df-a756048cf3c6 | -8.37208 | -61.5433 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6cb8009c-ccb5-3bf1-be1e-5385f93a113b | -8.22318 | -61.21743 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c15f2fab-b0b8-3fdc-a8c8-c4e31d3f337e | -8.22204 | -61.2007 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8402343-3d1b-35c0-af80-c61bca9b880f | -8.22143 | -61.20475 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d2a6dcf-8565-3c20-a25b-10ec2e7ab2aa | -8.22083 | -61.20879 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3a1b2c3-9ebf-35c0-bd3a-3e1ebd44f25d | -8.21847 | -61.20015 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2edc0b6c-6aaa-3eaf-bedc-3db821252efc | -8.21726 | -61.20825 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edebd5c4-f42d-3e52-8156-0913da7caecd | -8.21074 | -61.20311 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8afa2ae4-d024-3676-a59c-85b2c0ad2133 | -8.20778 | -61.19852 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5516b92e-3783-3ad0-8514-fae54f41111b | -8.15316 | -61.27743 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19e04b54-a454-31b4-b47e-8effcd293ef3 | -8.14961 | -61.27691 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be0cde55-53e5-3012-861c-8ad1fd7b340e | -8.14666 | -61.27238 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5866562-9f5c-3971-84ab-63d6f773f7a1 | -8.14606 | -61.27638 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3586c542-b723-3548-90df-c91b26ee71fa | -8.1322 | -61.34364 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffd3b6fc-e4dc-3d53-a2b3-64cf0153c5c3 | -9.08238 | -61.39141 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 645ccb10-df3a-35a7-9f4d-0edb55e070d6 | -8.84379 | -61.49366 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af27b247-b2b9-3766-9f6a-379b75feb5ec | -8.84025 | -61.49313 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 731dd698-669e-31cb-9c51-2c3ddde88bfa | -8.83964 | -61.49712 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98e48a6c-41af-3b49-a0e0-a3d3d218062e | -8.83904 | -61.50113 | 2024-10-06 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c80f317-4c59-3e04-9576-6c8110cec6cb | -8.74537 | -61.05894 | 2024-10-06 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae1e6c6f-5cba-3df6-84be-969d952bb26f | -8.37149 | -61.54725 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d53d126c-0e7d-351f-9cd6-c12dc57e8d13 | -8.22674 | -61.21797 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa0dccf4-7f32-30c9-8aed-bf841167c8ae | -8.22613 | -61.222 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcffa518-4592-36c6-bf2d-8be617ec099a | -8.22439 | -61.20934 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de2f712b-edb4-3d6a-9b97-993012983f8d | -8.22378 | -61.21339 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89e46147-f77d-332f-ae71-229f346664f2 | -8.22022 | -61.21284 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 590337c9-c326-3d2c-a55a-a15fc880fe2e | -8.21787 | -61.2042 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2d4a4be-b3a3-31d2-a424-14930114278a | -8.21491 | -61.1996 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c8aba94-b0c0-3164-8b4c-b0a940445643 | -8.2143 | -61.20366 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ceca72d-2a27-37eb-b1f2-89ce40d9f6ac | -8.2137 | -61.20771 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c063ed5b-d9dd-39c6-a4f4-5567762d0ed5 | -8.21134 | -61.19906 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c453f207-2ca1-3e36-a4df-1d2d5da702db | -8.21013 | -61.20716 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 430eaa64-b62d-3051-9fe5-d42004a0ad0e | -8.20717 | -61.20256 | 2024-10-06 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adc31133-3fb7-3d2c-8b69-d181fc6b7471 | -9.17367 | -61.57326 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d58d382-3b12-32f6-bdc7-029fb400ea4b | -9.17306 | -61.57724 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9deeb87b-f121-3664-8a07-c82e054341ec | -9.17072 | -61.56874 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad9799cc-6a8a-319b-859f-6e5edf1f0a30 | -9.17013 | -61.57272 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85ea87c6-bbc4-3d8a-877f-60e2e4866340 | -9.16952 | -61.57671 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6aaa900-bd61-364d-ab67-5f2f566fa1c1 | -9.16718 | -61.56821 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f055bc60-afb2-33f9-a769-78d1b6f76ad1 | -9.16658 | -61.5722 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ac69a479-91c8-3e7a-ac3a-267f3f8f2643 | -9.16598 | -61.57618 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a7a348b1-1304-3207-b641-05a9dd1bc77f | -9.16364 | -61.56767 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 1861403d-3179-33f0-ac72-b47be643f0a7 | -9.16304 | -61.57167 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f3efd9b0-720e-349a-8534-c75014ffbc90 | -9.16244 | -61.57565 | 2024-10-06 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c5423fd2-b255-3a79-b424-9df360010e99 | -7.52216 | -63.26267 | 2024-10-06 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21770045-36b3-3909-a452-343f19f332f6 | -7.50071 | -63.35609 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff49c3b9-e6ad-3e1a-8ee3-f36e492730cb | -7.50404 | -63.35662 | 2024-10-06 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9643d8f-8d1e-3d0c-b505-8e20e4f09985 | -9.3118 | -63.24809 | 2024-10-06 05:36:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44bdf84a-2b5f-3920-af56-21d0cab1b6cf | -8.96945 | -63.38752 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48d0ce87-db33-3aeb-8ab7-b870aae9e721 | -8.92193 | -63.5174 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49b063a7-c245-3ea8-9c9e-6f29acf6729f | -8.83292 | -63.02742 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README138.md)
