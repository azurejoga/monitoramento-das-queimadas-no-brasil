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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 576c11eb-6a4e-3077-9e35-c4d76d63374d | -1.2862 | -51.731602 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91bd3126-9026-31aa-b22f-dfa89389aeab | -4.4105 | -44.125702 | 2024-11-23 00:45:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 377a3fa8-bcb4-3fb0-9d34-4c71b699f80b | -2.9037 | -54.004501 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3272b837-c67e-3620-bff0-7690dcf65b8b | -1.7848 | -53.6134 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a988ed04-995c-31a0-b9e9-85a325f7d58d | -4.2635 | -46.2897 | 2024-11-23 00:45:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eed21b65-dede-3670-9552-4cec26bcd5b9 | -3.2301 | -54.218201 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99f560f3-3773-3378-9bab-d5fc82ca0177 | -4.6068 | -46.4813 | 2024-11-23 00:45:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6338e670-83e9-3847-8b7a-9d932d78a195 | -0.7647 | -51.747601 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| fa92bcc2-160b-30a3-a7a7-e63a301d6a77 | -1.139 | -51.672501 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 546ae27c-43cf-33ce-86b9-0bf1ab7e0749 | -2.1515 | -50.918201 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f11a674c-f3f0-3105-af74-4b4b7d25e178 | -3.5742 | -51.554001 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dac7b846-15b7-37b1-b90e-5cfb60c55c2b | -2.785 | -53.980801 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf7948a2-9946-395f-8fe9-74fbcbf1238e | -1.2622 | -51.761799 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27f60a0d-9fbc-3848-90e9-c5732073989a | -3.2544 | -54.2342 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9053bc98-6e4d-3cc4-956c-ef53a750d168 | -2.4625 | -53.693699 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79e194c9-20b0-339f-8e45-39f129da8bc7 | -1.7417 | -52.376598 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93b80708-0d6a-3be2-986e-f73baa316d66 | -3.5195 | -53.810501 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41f5451d-8432-3a29-922c-8be7a484f449 | -0.8823 | -51.721401 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 38f952a5-7e0c-3332-a820-8f4c6d67ba36 | -1.6609 | -52.7019 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b3651d0-919c-35c4-bea3-61ab7a756927 | -1.206 | -51.7411 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea12fc02-f338-3c15-990b-8e41785acd4a | -2.8795 | -51.580502 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f03c7fe2-7b1f-31c7-b6a2-0fe7835fe901 | -1.4571 | -53.3951 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d359c82-bac8-31ac-b4d5-e05886df4173 | -4.5156 | -42.879902 | 2024-11-23 00:45:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ee1b42c-1bc2-3dd9-b235-7cff9f0b1bc0 | -2.1614 | -53.775002 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f8cdb64-cfbb-3d96-be4a-445d4e0fd8a5 | -2.5804 | -54.033298 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0347c6c9-f5cb-3604-8ffb-963961760e83 | -4.8996 | -47.4128 | 2024-11-23 00:45:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb1dbf74-bbb6-3b29-ada9-1b6b7e0e144d | -3.505 | -53.792301 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78d0ae0f-1902-3302-8f02-eeed9e3f5bbb | -2.8128 | -45.1408 | 2024-11-23 00:45:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 260af80d-5ee6-34ff-8f0f-e636ae287d3a | -1.7279 | -52.7248 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0ae8ff1-486c-324b-bc95-0ee9da577583 | -3.5233 | -53.508202 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f276b60-cf78-3ec2-8c9e-2e1a1ceeb562 | -0.9382 | -51.649899 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4ac660b-0d3d-31d1-9aa1-be96ec3494f6 | -2.5654 | -54.058102 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64da7b50-653b-307b-8873-71682ee6e631 | -3.4693 | -50.4217 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa405fd6-dcbe-36c8-bc58-71afab0fc3be | -1.427 | -52.670101 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74f2fa88-a0b4-370b-b0a3-c341b57aced8 | -3.2633 | -53.27 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80f2f36b-86d0-3dc3-856f-e431e947f6ce | -3.461 | -48.250401 | 2024-11-23 00:45:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40d08a6c-3121-3c00-9421-c65ab9f0d1ea | -3.1897 | -54.313 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70fdec79-775e-30e1-9fcf-28b7e93930b2 | -1.0402 | -51.736401 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 692c1442-14c4-3362-9ae1-e40239f6836b | -2.6243 | -54.044998 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcbfe81b-d0e5-34fc-b060-6c9fe5c210f4 | -3.1245 | -53.111698 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c96e3a1-2875-3a45-9c41-d96f343e24b7 | -0.2704 | -51.610699 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a9d2bfbb-55ce-3b78-8582-61f0cae77a18 | -3.3363 | -53.319 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b924d44-91b9-3324-bc4d-15f0810762dd | -3.946 | -47.9496 | 2024-11-23 00:45:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eccf29e-e08b-39f1-96c8-3a223772fd72 | -1.2632 | -53.357601 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f887d44e-ccc6-39b8-8cb6-bf9d3a844fd4 | -3.5179 | -53.803699 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8855254-df72-3300-84fb-4379c7a1e4d8 | -3.2918 | -54.721298 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98000888-97ea-3b54-bb31-e66926ec7699 | -3.7963 | -51.7593 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f01b5a4c-4bdb-3f0c-a72a-2f0362edd876 | -4.0245 | -48.8591 | 2024-11-23 00:45:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b75d0d5-0e36-34c6-95d7-f0d1e513abe4 | -1.0518 | -51.742199 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 392c7130-db95-3d6c-8baa-44ca9fa39d6f | -3.9778 | -49.012798 | 2024-11-23 00:45:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 487ecd2c-94d1-3640-b1fd-8ec0fd78cf7d | -3.2633 | -53.817299 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df58f065-32bb-3bd1-877f-2db9bed0efc3 | -1.7246 | -52.7104 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 785f6146-922b-3777-baf5-c23594cbff46 | -0.9821 | -51.7075 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 70a8c120-f8e3-37a2-8e74-b3df453c9e27 | -1.723 | -52.703201 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e2c418e-1807-3196-bfb1-68904d75cfff | -2.6958 | -46.251499 | 2024-11-23 00:45:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0fc5bbe9-df7c-3bb1-bdfc-f117ec245e7f | -3.7293 | -46.0271 | 2024-11-23 00:45:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e904dc28-7f62-3527-8cbe-84e7ed12a343 | -3.5247 | -53.787899 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92c5ce22-db03-3194-8732-a5ef46f63e7a | -0.261 | -51.5695 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 81a528f2-e9ef-3127-bca3-c40e15ae5174 | -2.9605 | -51.439098 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b7ec4b4-3d2e-3c39-bb92-3bb8c7db8ae3 | -1.3112 | -51.7509 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca2cd9b-3ea0-32ac-902d-82a7e90e5901 | -4.1027 | -42.484901 | 2024-11-23 00:45:00 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7b98a619-b7a1-366f-90d9-c07918f7d406 | -2.8521 | -53.958698 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12a3e89c-0b0c-3886-82c4-6df5afed9c08 | -1.2247 | -51.959301 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07550e8a-16b3-34bc-a2dc-642d16f6859d | -1.2372 | -51.7425 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b76e421-10a1-3844-af22-3303aaf41f86 | -2.7311 | -54.107201 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9367394-7692-3a2a-9085-4be6c1fa696f | -2.5623 | -54.044498 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5e98d35-0c29-3af8-b7b1-b9182aacc25c | -3.4831 | -50.436798 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8843942d-9fe6-37cb-ae2e-1b4b438470ea | -0.2671 | -51.5508 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d13826cc-16c6-3a54-a113-c784798a1b1a | -1.1998 | -51.759201 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc449efc-0413-39e2-981a-cdc7070e92da | -4.3666 | -47.8134 | 2024-11-23 00:45:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48c4df48-358b-3c66-9494-002bc9c8f7e6 | -3.226 | -53.9258 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a72a8007-d617-3cbf-9dd3-de92ae165973 | -1.1144 | -53.383301 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fccf14eb-1197-327f-b928-0b86b8c0a8d1 | -2.9516 | -53.714401 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d9953a1-1952-3ac0-8c63-07b060baaa70 | -3.2358 | -53.923599 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de960be5-739f-3ede-adc7-8217e560f887 | -2.5479 | -54.026199 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d011f1b-3641-30c5-81b0-9edb33fc183c | -2.5949 | -54.051601 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75080e97-1995-34cc-b8e0-2008c177b364 | -1.1371 | -53.392799 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23928ab0-5afa-3223-98b8-0ada0e927881 | -3.4157 | -53.214199 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 377f6ce1-2089-3093-b026-1144aa2e622e | -3.4713 | -50.430401 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7e5374-9922-3125-a886-4556ba5e8145 | -4.3694 | -47.8255 | 2024-11-23 00:45:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 227d65e0-ce9c-3c57-b184-628732bb9cc0 | -0.2592 | -51.561298 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 61197614-d3cd-33b2-8e97-07c3c81e0b8e | -3.5081 | -53.805901 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8675890-0c98-3033-8856-cf17d0427b04 | -3.3248 | -54.089901 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e580a822-04a2-3567-a0e7-209521c1ca7d | -2.9507 | -51.441299 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8181f76-5ca6-3284-9b13-17204c6d2a65 | -0.797 | -51.799 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 499bd6d3-35a2-3120-890b-f248c9f4474e | -2.8417 | -54.003899 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e887213e-3d4f-309a-889e-932c32ac506a | -1.7623 | -52.6945 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5dbfc56-9bbe-39c3-9616-9be517babfbf | -6.4971 | -47.033901 | 2024-11-23 00:45:00 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02873445-31dc-3b64-872a-28454ffe7dd9 | -3.4582 | -48.238701 | 2024-11-23 00:45:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 920f7caf-69d4-3931-ac4b-0881a0a7813b | -3.7439 | -50.0037 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73fcccb8-4780-36bc-be3c-a3d979f9f38e | -2.8813 | -51.588299 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 136d2c3e-9d7e-33c1-aed7-8808295d0c85 | -3.3223 | -54.765099 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9170786c-d623-3ff1-b0e1-84204eae39a1 | -2.5903 | -54.0312 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe95bad0-57c6-38bf-b844-8d32457c59f6 | -3.3442 | -50.504799 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60aece6d-4f85-39ab-b6e1-fc1d0464a4e0 | -3.102 | -54.289501 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4d5e075-d3db-30ca-8c27-cdc6d68597cf | -0.2629 | -51.577801 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e1a860ba-dcfc-3f4e-ae1b-e45bf425fb5b | -2.9036 | -54.598499 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a91f04-aee8-3efa-ac13-b5452d00782e | -1.3071 | -52.277599 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e242b62-9427-3cc0-8e30-a8589a787eba | -1.1998 | -51.9403 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e382a1f7-2276-3e56-b39c-f999f4d73d94 | -4.0976 | -51.049 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
