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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6fe77b3-76d7-374c-92e3-86afa27f2e58 | -3.14536 | -57.89355 | 2026-09-20 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5d0f96ab-0227-3907-a11e-f6a34b74331a | -6.64629 | -62.87639 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8989f9ca-06b5-3df7-b36d-1006bceab499 | -7.55872 | -61.32438 | 2026-09-20 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 990f0da7-fce3-3ffa-9808-b71ccaa67ff8 | -3.73464 | -54.64412 | 2026-09-20 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5cd10c5-d7ab-31f7-a7ff-75d74649d7b1 | -6.36713 | -58.3128 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34aa186a-6306-3578-9be4-bc97567e0b59 | -9.39321 | -60.34915 | 2026-09-20 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b160f6de-289d-3f41-8a26-01f2e0e4b48b | -3.35982 | -59.87438 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec3ea57e-4913-39ec-8fc5-894a907f1bed | -2.82856 | -46.71088 | 2026-09-20 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d849fa4-2a95-39a5-9516-11c7c43e7829 | -2.64545 | -54.68995 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 2451289c-5e9d-3b32-a25d-63b992f8aa35 | -3.36259 | -59.87832 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0122075b-800b-34d9-97f1-65d84291dae6 | -1.51691 | -49.47034 | 2026-09-20 05:23:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75253993-c107-32e8-8526-0db532cb8120 | -10.6027 | -51.88439 | 2026-09-20 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b999981-ed31-3d2d-a052-323ab6971955 | -9.6996 | -48.31785 | 2026-09-20 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 46e21a78-efa6-390e-afb1-97119b16b055 | -3.44629 | -50.60371 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 881eb92d-3c25-3031-90d4-b7a0da8f87c9 | -6.15 | -62.61829 | 2026-09-20 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d52af8e5-df91-36e0-943c-8559f5f55f10 | -8.46915 | -57.624 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74cffd88-15d2-35b8-b19a-1600d0629f22 | -6.7337 | -55.0747 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4276968b-6664-3c70-97a4-16e61ab609a7 | -3.19348 | -61.1306 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44024afe-f44f-37c0-ae75-099c54663cb1 | -3.37226 | -57.9697 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db133f90-b8ad-3572-944e-ac7d40824b4c | -2.82699 | -50.47642 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f47f08a1-208d-3b31-b62c-5577cfd8e064 | -6.92764 | -63.11475 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40218c58-8725-3537-8751-1a5673c42c51 | -8.2514 | -50.67247 | 2026-09-20 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0545fbf3-8464-36ea-a083-da9efbb8ed13 | -3.35759 | -59.867 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3cb1fef4-af4b-3f29-a8a6-0e5fc4064abf | -10.46483 | -51.27939 | 2026-09-20 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1d0033a5-7c29-33b4-bd28-a427ebb1fb96 | -3.00852 | -54.17051 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4780cecc-8105-3c90-8cb5-5640290a4440 | -1.18787 | -55.6742 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa141827-04c8-38a3-8fa1-089d0a1198a1 | -3.89134 | -55.88609 | 2026-09-20 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a19668f-5259-3a81-94d8-325031140b31 | -8.16442 | -54.7565 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ff791605-32ae-3621-96bd-58be0d991f68 | 0.01052 | -60.60369 | 2026-09-20 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 570b0acd-067a-337c-818b-b0249d4639b1 | -2.30571 | -48.40072 | 2026-09-20 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2bd2e01-b41f-3d17-8f60-6dfc59250427 | -4.26374 | -48.63427 | 2026-09-20 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4debd7f-38bd-39c0-b252-42981612eafd | -8.61746 | -54.59758 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7eabd645-33e4-3a28-8e7e-d39daca64c8d | -3.38615 | -50.4413 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2160d6a3-1f4d-3edd-9e72-d9d9b551e67b | -10.27811 | -50.24966 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf65c2ad-a253-3d69-b5e0-cf9df8a7f739 | -3.7391 | -51.82347 | 2026-09-20 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 950cf1ee-41e2-3663-9db9-08d9fd594033 | -2.64491 | -54.69356 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b1f3eee8-0a75-38d7-935a-f74dbcd3190b | -10.72187 | -50.24482 | 2026-09-20 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0c6bfccc-849c-3664-a0bb-2e1d51c30ad2 | -2.21758 | -60.17365 | 2026-09-20 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11054bcd-5a4e-3838-a2fc-c1bb697fc8ae | -6.94202 | -62.91513 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1769ce6c-dc10-3be8-8379-124ca9228777 | -2.98325 | -54.77002 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed1f27a3-87a5-3bf1-a159-41954f30e056 | -9.17336 | -51.5092 | 2026-09-20 05:23:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41aa6937-263e-3de8-b01b-c858164c5cde | -6.44311 | -59.97024 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fa60250-b3c7-3978-ac48-96f28284579c | -7.61045 | -57.61353 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b86a77e6-437d-3252-8160-9a6aef164650 | -3.16144 | -60.57611 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dee9f81-ce01-3fa5-aeff-ab4bdb3c03b7 | -3.33231 | -58.13837 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f144c0bc-ad1b-34b1-9502-b1f7eaf489c7 | -3.38564 | -50.44487 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fd28dc9d-ed5d-3fdd-9df1-06a7a1ab2c5f | -8.79811 | -60.7929 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5e80d1f2-35dc-38c8-9815-b38ae2a84c37 | -2.82971 | -50.46805 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ae6936d-a221-30d2-8c28-e43347445713 | -6.79983 | -58.7882 | 2026-09-20 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20042e40-2472-3bd4-b1a5-ddabbd72c105 | -3.33185 | -59.81037 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1334bf0-f072-32f8-9a30-68d3c2d44785 | -8.22078 | -62.85165 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57a5b7b5-aae0-349c-ba77-35e7caa0f7f0 | -8.76572 | -61.39269 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd19d439-b871-32c7-ab9f-6b3fab19caad | -7.86285 | -62.54068 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8326f437-96f7-31ef-bae1-4c79cbe5581a | -2.99584 | -54.16839 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 903fb776-3735-3233-8ef2-da06ba4cf339 | -6.72892 | -55.07801 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0fa79a5-93a2-342e-b882-bcb8720088dd | -8.63161 | -47.61855 | 2026-09-20 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2db3325c-d516-3388-a6d1-8708f3951ed3 | -3.33854 | -59.8325 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c884168f-6d7e-3d06-8a63-e89a84dbfb2f | -3.47912 | -56.87721 | 2026-09-20 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9377776-4129-3276-b710-93c0c6b0d7e8 | -6.44203 | -59.97721 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 657b994f-7b49-3171-8c94-e68e5c3e9e1b | -10.30818 | -50.25851 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e19e9868-b6c7-3d30-be6a-814c5db55a8c | -6.1371 | -59.9476 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20b05eff-ca85-3f75-9c4a-6ec42c9d64e1 | -7.40996 | -49.84367 | 2026-09-20 05:23:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| be793da6-0a06-332b-9562-d3e0fa6c981e | -2.61446 | -54.75869 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 0b020f1f-e58f-3740-8787-3810f104e14d | -6.49025 | -58.38187 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 395bc111-7735-38c0-a04f-e547937197bb | -3.35268 | -59.8768 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 025192ae-8974-39c2-bc08-2300d408e9ac | -9.81174 | -48.32112 | 2026-09-20 05:23:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01b5fb07-ea69-3769-8664-6a9f4f911acc | -7.0447 | -62.95417 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0abec733-8296-3491-a78c-912c7a985e6c | -10.31972 | -50.21642 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c2728a75-5091-3cbb-82e7-0a6113e5ec55 | -6.94194 | -59.99802 | 2026-09-20 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e347e7ca-ff7d-37be-8b09-a359d03ca9d4 | -2.4519 | -49.21465 | 2026-09-20 05:23:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 21bb2505-3afd-3b65-8b3f-64e5271d4f5c | -3.36857 | -50.44621 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 780aedec-b9a2-3dca-bbfe-86af54ff17ae | -2.88222 | -57.80469 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0a76dbf6-da4b-33a7-89f8-df5e65afb2e5 | -3.67193 | -54.27531 | 2026-09-20 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87980415-befb-3470-b99f-b7615ad4186c | -8.7948 | -60.79238 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 93cc29fe-e80c-3c80-9ddb-aa430585914e | 0.94479 | -59.53062 | 2026-09-20 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd1339a7-f374-30cf-bd50-5731c86f74d4 | -6.34741 | -58.30188 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d3456e7-b010-31d2-a7dc-e5bc4ae2799e | -9.67076 | -54.32341 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a4b5831-3446-309f-9f53-9c8cbe15db44 | -6.1354 | -59.93665 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69076656-8332-3797-80cf-ec4c68751d7e | -8.7344 | -52.3628 | 2026-09-20 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77ce0615-d9ea-3cfd-a5c5-6c1f46be58f7 | -2.8965 | -57.82608 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d4265c4-3aff-37e5-88b5-49ef6a75b0e7 | -8.88566 | -62.40315 | 2026-09-20 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 86226e06-9bd3-367c-aed5-7d1634f6775e | -8.63081 | -47.62533 | 2026-09-20 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f5f9c292-4585-37d7-b559-7041b2b615a5 | -9.59117 | -60.52177 | 2026-09-20 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5e3e9fe-2379-3446-ab38-c502cb6af27a | -3.35694 | -50.44769 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e48951a1-9a84-3acd-8f6b-9302622453b9 | -4.43555 | -49.11159 | 2026-09-20 05:23:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1a299e6-eee1-3e41-8507-e05a0adabbd2 | -10.31053 | -50.23951 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cbb449d6-c806-3d35-89ee-2af4b2e1940f | -3.34188 | -57.869 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e01dd01e-7afe-319f-ade6-b8b3ac7fb918 | -9.28131 | -60.63581 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29cfc44a-6507-3f46-a77e-68af4eb00799 | -10.78689 | -50.87874 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| baf326f6-da1c-3ee0-9b6b-5a6649ece111 | -9.69088 | -58.18713 | 2026-09-20 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13aeeed2-7a16-3ff0-8eb8-35f91fa75e79 | -2.88079 | -51.73733 | 2026-09-20 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91922296-0a55-31f9-9bdd-e93583442e91 | -7.61108 | -57.60925 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a38314fb-a73d-38c7-a626-f6d59903d436 | -8.79095 | -60.79535 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 893b4b14-b030-30b9-990d-504bf410d946 | -8.4239 | -54.73291 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8010de5c-6dcb-3184-a58a-350e9cd3b8b9 | -6.13818 | -59.94064 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e790265e-9885-3b10-b7d4-3ecdc9beee62 | -3.12068 | -61.2498 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 837604c2-141c-3a06-91ab-d7c6453e4481 | -3.34077 | -59.83987 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46ca398e-cb98-32ed-8802-a81c16e3b3e8 | -7.5604 | -61.3353 | 2026-09-20 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6160dd93-6151-3e39-9652-e20d1fd3803c | -3.36701 | -50.4571 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad48e9e2-4c08-320c-ad8c-c6d236f2de5d | -8.23866 | -61.37238 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README92.md)
