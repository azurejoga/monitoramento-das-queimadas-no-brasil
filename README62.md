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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc26a02c-eaff-3b41-85c6-9d39393ffcaa | -1.90942 | -53.33912 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eae9b783-2a1e-36c9-9148-01d29f388788 | -2.76735 | -49.86852 | 2024-11-21 04:53:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5c73878-bf1b-3e19-b68d-1012aaba7a72 | -0.40095 | -51.54377 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f32d3a4-3dab-32d5-8e9a-08c1f383bb12 | -1.44588 | -53.38964 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d9f0a0b-6fcd-3ab7-b5b1-fbb7afaeac9e | -2.13926 | -53.77668 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03868c69-1a3b-34b3-9881-06e4f7558d03 | -1.95614 | -53.32178 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 042a38f9-8b52-3c3b-afea-a3d379048338 | 0.81922 | -51.26888 | 2024-11-21 04:53:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfdf3c96-5d82-33a2-8904-c1467d79a83a | -1.60403 | -52.25453 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 293aba18-535d-3953-bedc-8ea7d47606c3 | -2.14643 | -53.77426 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b076269e-f06c-389c-aa8a-057d216a6a25 | -1.12336 | -53.40897 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86ccba32-5293-3f49-b03c-ce0bba672623 | -2.15251 | -53.77875 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc02233a-4d21-33c3-bd8f-49a9848165c3 | -1.25124 | -51.75423 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65db57a7-e376-337e-aec7-296cae804fa0 | -0.83111 | -52.30784 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea7706e3-2c7d-3613-8e32-a4f333b643a2 | -1.11037 | -52.34774 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78eddbc4-97cd-3315-9cf7-7d892834c8ae | -1.20211 | -51.76113 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc1559f3-dcbe-3ef0-ad66-5137c948cd73 | -1.18568 | -53.72677 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f340cc1-a5eb-3ea6-978e-378f14631190 | -1.75466 | -55.06393 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a69765d-610e-39a5-92dc-63a9ab41bacb | -1.41054 | -54.26283 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca988748-9c0e-3a4f-9bd1-92be46abab82 | -3.28494 | -45.97872 | 2024-11-21 04:53:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8739fbd-3d30-36a0-b3fb-6d7ce22e0724 | -2.78843 | -54.0348 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 842b1ec6-3480-354a-9ba9-f8ba979dd0d8 | -6.81593 | -46.78128 | 2024-11-21 04:55:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 136bde42-884f-333c-b818-1b1f79c0dbfd | -3.79224 | -51.37336 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24feb191-29fe-3280-bfd9-5601cbd26fa3 | -2.54308 | -53.99575 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c540d07-dacb-3fc9-9029-9ac58d1422a0 | -2.55914 | -54.06624 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 270338a5-0b3f-3829-bfe5-923202894219 | -6.12281 | -42.52148 | 2024-11-21 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 45c73adf-50fd-39d9-be6b-424515b9562d | -2.59453 | -54.03611 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10555176-480d-3e0c-8e09-4a5e22042dc5 | -2.80721 | -54.02353 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a50fcf2-cf9c-3a6a-a0bc-9b1b3955a8a7 | -5.46842 | -46.53331 | 2024-11-21 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c180331d-b732-3049-baf4-a5c177d75cbc | -4.39102 | -45.59278 | 2024-11-21 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4db32a3c-79a9-3179-8f2d-463bbd8e7c4f | -3.48765 | -51.59863 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcfd9fee-0d54-342a-817b-731534897756 | -3.3332 | -51.13073 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a66ccb82-0d76-3513-aec1-3ae8586dbeb5 | -3.04373 | -54.39939 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a49edad-a264-3e90-ae1a-2c0c6e300338 | -2.59892 | -54.00836 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6acce38c-031f-3478-80bd-6cbebbc043bd | -2.82102 | -54.02214 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12fc2d74-1b1a-3d3b-90c8-ba1923389502 | -2.78734 | -54.04173 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a8f5d22-f6f9-34a7-b6e1-e1a52c7c09e6 | -3.47064 | -50.01302 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d6f2c9a3-e1f4-3624-af5d-c0d453b92b38 | -2.80444 | -54.01955 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f25b9048-b12e-352a-874f-abbdca7387c8 | -3.71215 | -51.18983 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32b32d7e-e224-34e0-8b65-97609e4cdcb4 | -3.341 | -53.31033 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64515fc3-15f7-3687-978a-996f97ffc326 | -3.29574 | -53.856 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ea98ee5b-e041-3c79-b2fa-504906b54730 | -3.91464 | -50.11775 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e159a50f-dab1-3799-8648-fae5688c727a | -4.1452 | -49.2247 | 2024-11-21 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9702cdf-c2bc-344b-9db5-57745b657252 | -3.39532 | -53.72009 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 246df817-ffe2-33d5-9a95-fe42a9201bf0 | -2.88224 | -53.97851 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 928296de-1ff4-3881-a5de-250f53333eb7 | -3.10113 | -53.21287 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 930b6424-1ac7-3dc1-86b7-5a27dcbc00df | -3.44147 | -53.03687 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e17e430b-6b94-32fb-87d1-ac690d0b8306 | -3.72712 | -52.33815 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d704420-254b-306d-83a0-b0d952049554 | -3.53919 | -50.53189 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 792a7a92-101c-3af8-83d7-60df32f3447e | -6.8221 | -46.7719 | 2024-11-21 04:55:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 05cbee79-4919-344b-959e-41911186acd1 | -2.79766 | -54.45113 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e812e3dc-9a1f-329d-921e-8509c2ea75da | -3.71552 | -49.4289 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f8370b8-46a9-3b23-a494-cd27937dea29 | -2.56523 | -54.07075 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a28012df-8f3e-3a77-8838-d7b6770ae82a | -3.40103 | -49.78493 | 2024-11-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca1af064-09dc-3338-8c9f-8e010e995607 | -3.6652 | -50.44464 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 515b45f6-c6be-38f7-9fba-3247fce7e112 | -2.45728 | -53.69982 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| acfc3ae2-3092-3c0e-b0ff-64a173cf72ed | -3.32146 | -51.56285 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7707311-831d-3046-8b06-1af5fe782bea | -3.21935 | -53.84371 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c18fac01-cdd6-368a-8739-4f461a546005 | -2.80554 | -54.01262 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15d851f4-d296-337c-afbd-55ae7c8f4e8d | -3.5027 | -48.2262 | 2024-11-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7a05acc-a4b1-3ed4-a2d5-e3b16200e0cf | -2.62867 | -54.27343 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aa5eda0-23f5-3c8a-8a89-722fd4e440ef | -2.8866 | -50.42252 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 445fdae6-620a-34f9-ad33-0ba5edfdebf4 | -3.5355 | -51.60596 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16da1c50-bb47-3df7-8199-39211a3abab8 | -4.6608 | -46.40131 | 2024-11-21 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d205ec7b-7db3-32e9-b2cd-f1d977cb86b9 | -3.45478 | -54.09705 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af3b89f3-a46c-3b2d-af43-32fbc6895284 | -4.4915 | -47.10961 | 2024-11-21 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc04b637-ecc4-3580-a42f-557af71c46fe | -3.53729 | -51.52652 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31620d66-87fb-3999-b2cb-49f607bafa1a | -3.71838 | -49.43126 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 747a9341-0aff-3898-ab2c-d69ae10594e1 | -3.19753 | -54.32697 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7912a575-74ed-34ac-aeea-600dd4be2bc2 | -3.24644 | -52.82924 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82203eed-e367-3998-9c64-816baf768461 | -2.58679 | -54.04205 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4ea8ea3-fdf2-3960-a8b1-00b10ad64626 | -2.38469 | -53.66345 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d633414-41f4-3b10-ad46-20edc97992d7 | -2.6179 | -51.80672 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf067630-04a5-3b76-ac6e-3a59aa644d95 | -2.77017 | -52.11439 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7698e7aa-2ece-3469-bd9a-0d01c9cce6ea | -4.88823 | -45.83681 | 2024-11-21 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 236234ad-eb17-3cca-9b11-8ca69325abaf | -2.85518 | -53.97783 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8448b39-0e0c-3735-86f4-3db6705f31f9 | -5.46766 | -46.5386 | 2024-11-21 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9940716-ae06-3b28-8391-d18953b5ca67 | -3.035 | -49.47139 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4e4043de-cd77-3f6a-867c-4e92326eda56 | -3.05023 | -54.52632 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3bf115b1-a1bd-3aaa-a1e8-0dea61512281 | -3.3398 | -54.07162 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11ac92ea-a46c-3fab-9ab4-79877ba086f0 | -3.40035 | -49.78936 | 2024-11-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 661a8241-063f-35da-9cb8-4f8b400a1f53 | -3.80977 | -47.79417 | 2024-11-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ae1cb330-1a3e-319f-8168-2f9d83b21d96 | -2.8083 | -54.0166 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb9e6ebc-644f-3ebd-b2be-8294807e8223 | -2.80776 | -54.02006 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55e51f0d-f042-3bcb-9052-ebffd4a14d70 | -3.0553 | -54.40831 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42be046b-449c-321c-9ae5-1f8886fce143 | -11.04352 | -44.57378 | 2024-11-21 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0d54821-75a9-322c-aecb-27348b9b9901 | -3.92198 | -50.11886 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cec9aae-d394-328c-a8a2-1d77b1da8ed4 | -4.94777 | -47.80397 | 2024-11-21 04:55:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 268fcf26-3da5-3403-803c-83e15a091a34 | -2.87838 | -53.98145 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f8960801-0f6b-3033-a51d-74c2b81c0e69 | -4.13844 | -47.73437 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1ca3db4-f6c0-3757-bd54-ab8961ae05a7 | -3.27861 | -53.83569 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2288d0b8-c0f4-336b-90f1-9142df9d6add | -3.58341 | -50.37732 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0850da06-6055-32e4-9d47-470cadb13d5a | -3.82741 | -52.25839 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbef7ae4-2e37-3505-b1de-d760f6d308a7 | -2.7392 | -51.72582 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6dfaa22-fdc6-3f60-b23f-05b466989e51 | -2.34123 | -54.77316 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 021fdcb7-4b45-3da7-93a5-788f42373cca | -7.56813 | -49.40577 | 2024-11-21 04:55:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 080d0945-bb37-33c9-a778-8128c0a4a905 | -3.18918 | -54.7698 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5aa97acb-de76-3f13-9591-2f1084569120 | -3.26392 | -50.62421 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d49d0145-2579-3f85-80fb-8b002a65e190 | -3.80703 | -52.36799 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8210eac9-b62f-3027-be45-634373e9963b | -2.74946 | -52.10109 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ed1bf60-1ac6-3ba1-80db-bf084cb9764a | -3.10491 | -53.98836 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README63.md)
