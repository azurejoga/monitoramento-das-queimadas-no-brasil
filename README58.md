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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af2904ea-cfde-3fea-b565-30086ab7ca55 | -3.85328 | -44.04892 | 2026-10-10 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 03c8ff77-51f4-3cdf-947e-5cbf638d55cf | -4.66915 | -50.44777 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea4981b0-a357-38ab-a91f-690f98ea475f | -3.54492 | -54.69061 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6de8b655-7367-32a6-9460-8c61e58e8ec3 | -3.26244 | -54.18175 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8619c0ab-dbb6-3a34-8d02-f90ce8fc21bd | -3.18772 | -50.59085 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05788f0e-bcd3-3124-b7f5-f394f8f1b25c | -3.20495 | -50.81644 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25443d87-7b10-37b4-ae6c-9240ecbeca34 | -3.17803 | -50.58032 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffa50bcc-6300-3bf6-96f9-eb1b87ce1a46 | -2.75244 | -54.09896 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9b85bf0-7c57-3a76-b8c6-8d5a91709113 | -6.23802 | -44.09971 | 2026-10-10 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78c1b3fa-1f3e-3ef1-8797-3f7bbe0cea87 | -3.95964 | -55.34306 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 91409071-ad88-3ed2-bcad-df3725514f15 | -3.11408 | -54.19363 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5da6f14e-785a-39da-b7e9-807cc43e7c47 | -7.24207 | -44.18288 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a614da9-1c1f-3149-b666-98065cbb9ab8 | -5.7467 | -45.13848 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa9d3cfd-7263-3f33-bc11-036d96d993fe | -3.74573 | -55.9493 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bb9102bc-0e4c-328c-bced-db884d01403c | -3.1035 | -53.78426 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8656812-b698-3ffd-8cb7-35d96fd1af10 | -3.36231 | -50.48336 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2e3121f9-6a2f-3386-9e96-4d49a83430af | -2.52565 | -56.27197 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b46dab70-60c5-3181-bcce-9880c71418b9 | -3.01375 | -51.0172 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c8d76b2-df09-3f53-9390-29d435986b8f | -2.99111 | -54.17147 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11348567-b38a-30ce-8a83-8cfd49eac27a | -3.26788 | -54.06265 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1eeeb9d9-6926-3cca-acbb-942b541bc943 | -4.40675 | -49.77016 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5be3af8e-42cb-3042-90a9-9c48d4797e57 | -6.28647 | -44.69487 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28bd8240-7e3e-3f08-a8fc-104d9d038a6d | -2.51264 | -56.14605 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2f80ba1-1762-3cae-a4f1-86b9519aedeb | -7.22926 | -40.35632 | 2026-10-10 04:44:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8dec0aff-00f4-38ed-9f33-353c4cbf04f3 | -5.08532 | -46.21761 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a9bc22b-ce62-3857-b30a-5d9b3267221d | -3.22401 | -54.29675 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4896334-fb35-32ce-ba44-2cbb45d65144 | 0.29286 | -51.40724 | 2026-10-10 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49e4a5b2-d080-3314-8976-ede0fe69c7fe | -2.99804 | -53.9127 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a401a21-c9f1-3a36-ad67-ad7103a305c2 | -3.1833 | -50.59464 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8545d6f8-71cf-310a-be4c-6251aeb0e218 | -2.51582 | -56.16042 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 047bb552-fd62-3d7b-815b-484db526f101 | -6.15302 | -47.96139 | 2026-10-10 04:44:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79fc85ac-3115-3e87-83b9-3e70152f6b15 | -3.88256 | -51.42836 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 850e2c65-28c7-3ea2-9297-7ce1c55acbf6 | -2.34811 | -54.75621 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ff2c6474-8e46-32a3-aca0-58d3dec98950 | -4.90688 | -48.77045 | 2026-10-10 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ee60868-9af8-34f4-a2a1-8f8354b5e7a4 | -4.85041 | -46.09295 | 2026-10-10 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7153e759-1024-3fa0-b25c-59012c17cb3c | -7.18379 | -41.99504 | 2026-10-10 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 498773dc-7c10-3871-8414-0ff81edee073 | -3.30278 | -53.99539 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75752247-26ab-3333-9a1c-41b19ffa07f7 | -3.56421 | -54.6938 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ca4899f8-ad95-348a-ac14-a83ff7827f6a | -3.1863 | -50.5996 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3a51d61-e37a-362c-8b25-782ceee0d3e9 | -6.40722 | -43.74021 | 2026-10-10 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c04b364e-445f-36d2-a113-5715b8dc5a58 | -3.10548 | -50.31427 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 869d648a-0a76-332b-9abe-a777b1a4e625 | -3.11266 | -53.78555 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c96e9ad-0b61-3840-b0e4-d642148711e4 | -3.31453 | -53.83876 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0da0a95d-d4e9-33ab-ae95-b7b679caf330 | -3.98343 | -54.46233 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 88f9102f-a422-34a8-9d29-142f9662a8fe | -6.06204 | -44.65413 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0732e100-2a13-3425-bb4d-d34ea2ab5460 | -5.11456 | -46.22949 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47da866d-99f1-35c7-a8ef-ffa099fca9e2 | -6.05537 | -51.73378 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2539afda-3fc9-306d-b2c7-bf90c6cbedc8 | -3.20423 | -50.82094 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08b37533-1973-3b22-81f2-782b9f331a18 | -7.18991 | -41.99416 | 2026-10-10 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 659fc07f-2fbb-3ae3-8994-0d09e08e64d4 | -2.39303 | -51.28993 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd0f7b78-2ad0-390d-998b-5d896ac61fc5 | -5.71282 | -53.47378 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a54073ba-49ad-3f7d-9508-a6f185380a02 | -4.81846 | -56.08194 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92141b1e-0320-3a2c-8aa3-1e546b13941e | -1.62705 | -54.44009 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eee1d41f-3ea2-3ba0-b683-25b7dba60e37 | -3.4921 | -50.49034 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4767b9c9-d724-35b9-b679-929262bd50fb | -3.86053 | -44.05 | 2026-10-10 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b009bf92-c6d0-3e5b-9d85-2ba0783d9956 | -5.80045 | -53.7999 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca1dd7d6-fd7d-35a7-b927-fdad91626a5a | -4.22497 | -53.82473 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2f03bd7-73a0-3ed8-a160-06f4f2426be4 | -3.30125 | -54.00466 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe180cd2-d063-3e9e-b3fa-aad79da27f3a | -2.52529 | -56.27272 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e71a0a4-d6d6-3631-b70e-2f5f0cbda962 | -4.1323 | -50.83535 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b443f307-0def-344f-9601-07b22a6d2a61 | -5.7072 | -53.48089 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2307e528-b7ab-3696-816d-ba82a93b6194 | -3.17622 | -44.29777 | 2026-10-10 04:44:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c2ec56c-eeb8-3e6b-b5a3-08feab968910 | -4.23689 | -48.72406 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67f6a40b-5d0c-352e-b3da-3c740dd5b385 | -5.92945 | -51.81616 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3199a28-bb4b-319a-9b2d-de84d2ae4853 | -3.01626 | -53.9668 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2122cafa-b39d-3db6-86c0-c16f077d192e | -5.87739 | -43.55891 | 2026-10-10 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3b479e1-ba8e-33d4-995f-723fa153d9e9 | -2.83717 | -49.87924 | 2026-10-10 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a781baf-80a9-38c2-af81-90c3e2a195d7 | -3.38388 | -44.48514 | 2026-10-10 04:44:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a9f0915-7c48-3f28-9e38-faad73e0c6a0 | -5.23493 | -50.68581 | 2026-10-10 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cab864a4-254e-35e7-8475-3cbb6a716b9e | -6.20307 | -45.42682 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf618f13-6218-3fd4-9c85-583790813029 | -1.33269 | -56.39521 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47f7f38f-827f-3b1d-b4b7-5309ee7db740 | -4.85124 | -42.82975 | 2026-10-10 04:44:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 96cb069b-9b59-357f-b7ba-d9aa1ef78c78 | -2.19424 | -46.83491 | 2026-10-10 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e58f23f0-c849-3063-84e5-3d1969b6e822 | -2.2198 | -53.69458 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74477569-28af-3556-871b-984a22e5ea6c | -2.93554 | -54.08923 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 641072e1-41b7-3187-8ebd-dfaff7cdb828 | -3.2799 | -50.09211 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ca9af98-1f79-37c2-91f6-16c034cb0093 | -2.97606 | -54.07604 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0ace85c-29f4-3cae-a0ea-e516ab0fc6c0 | -3.90471 | -55.89725 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06f465e5-5666-3a11-9497-88612d0646ef | -4.83484 | -43.349 | 2026-10-10 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd0f0f22-5828-3975-8c1b-b7ab91994cb9 | -1.26479 | -55.75229 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9473a849-e92b-3681-b209-e4ab1ce9731d | -5.87984 | -53.51334 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b3ad180-079e-35cb-bc46-8b18c7b6185f | -6.64785 | -47.91187 | 2026-10-10 04:44:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a88b3e4-596e-3fbd-a8b1-e1d0609424b3 | -3.86794 | -55.99018 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 498004db-8804-3828-b4f7-b6f665d54756 | -5.92483 | -51.82025 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f008c844-d966-3ac7-b84c-526f06bea14b | -5.48622 | -44.40081 | 2026-10-10 04:44:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d48129ab-b25e-3e38-9808-695ff7204273 | -3.16348 | -58.62428 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f757fbe-b204-30e6-839e-760afd5d1dc0 | -2.37898 | -47.60977 | 2026-10-10 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2ab4a25-41f7-3f5b-bb33-3e40ce7e2e0e | -4.81589 | -42.75097 | 2026-10-10 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e0bac95-a63e-346d-a8cb-af0574eaef21 | -5.087 | -46.20686 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3eb3a60b-ce3e-329d-8dd9-674ccc5c6e97 | -2.74146 | -54.1072 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 502cfb40-145f-3cc1-aa96-c3343fafe381 | -5.08476 | -46.22119 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17b937e3-84c9-370e-9093-1b410c9d4200 | -3.35357 | -50.42042 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4e1fc2b-06d5-3d48-b095-559bf750cf95 | -4.3846 | -55.15995 | 2026-10-10 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 968799ba-9d75-3f5e-9506-76934ebc7c03 | -3.59565 | -54.58886 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| adaf18f5-b161-3e6a-846e-51da9f71b6f4 | -5.745 | -45.12632 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 33ce9fab-5a73-36d8-a11f-97f7f28c8100 | -7.19308 | -42.00277 | 2026-10-10 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 194cc923-9b73-36dd-9250-064d0dbe833b | -3.76411 | -45.96235 | 2026-10-10 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53235262-69dd-3dd4-9b01-3efe7e70a500 | -2.45864 | -56.05811 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 968e8ea5-b785-34e1-8b9e-779e844e3e69 | -2.46582 | -56.06138 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d19ce2fa-54b2-320a-b2f0-5cc08e23e4dd | -3.00579 | -54.11315 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README59.md)
