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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e4bc587-c1e9-3c6b-9c9f-a729dce951b9 | -3.0447 | -49.528301 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec6180f3-c03e-360b-b7cd-9730cfd459d2 | -3.1062 | -50.150799 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac33110-f81d-3506-bbac-46c2c7178d04 | -3.2387 | -46.215801 | 2024-11-11 00:51:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bdbabc74-32e1-3742-9c38-302fb0d229bf | -1.5013 | -52.143501 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb6936f2-73d0-3dc1-a122-5c907a76bd0a | -2.6007 | -51.7192 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3eb171e5-0a2a-38c7-91a7-4998cb695f90 | -3.541 | -45.710499 | 2024-11-11 00:51:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8e1ce6-cab7-3583-8136-e6a787e39b13 | -2.8463 | -49.428902 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d991bcf-6fa4-3d73-96d5-e78899c14fc5 | -2.0309 | -53.962002 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e58c9d2b-17af-3ce9-abf8-3414be131330 | -3.1049 | -54.289299 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49f4e69e-437f-33bc-9c6d-b13c9cc832cc | -3.2687 | -53.695301 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45b59ea3-43ca-3357-aeba-d90ca9ff950d | -3.0319 | -48.054901 | 2024-11-11 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c02d1359-5619-37f7-b230-e6d85f1a02e6 | -3.6179 | -50.5798 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4af6b448-24ad-32e2-b27b-d5a6b8bdc76a | -3.579 | -52.252399 | 2024-11-11 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f35236e5-2806-3355-b79c-5c27e4d2fbdc | -2.935 | -54.4482 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c69a31fc-acbf-3577-ae4c-8104ca5cfeee | -3.1 | -53.316299 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0df4d5d9-6961-3949-8d9d-5d278ec39224 | -3.6189 | -54.103699 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03d96127-2c63-36af-91ba-c8d6de661681 | -3.1408 | -54.492699 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eed82282-4f73-3f1e-838b-a6836518f2a7 | -1.3235 | -47.7089 | 2024-11-11 00:51:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20d61982-b1d3-3ae8-9c26-6e7ea7956e6c | -2.7526 | -49.336498 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 782534f7-a69d-377c-91f2-a0874fd7f965 | -3.4501 | -51.464699 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18842587-6ec8-3498-a000-9f722a42c46a | -2.8365 | -49.431099 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed16de4-9220-31a0-a437-b8c6f0469a39 | -3.4287 | -54.536499 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1474d53d-416b-399e-bd11-cd0f3b8e3834 | -2.4367 | -51.948898 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dccb49ec-927a-3974-ab29-00e90761ff7d | -3.2573 | -53.690201 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 974c7a25-5bc9-37f1-bcf5-42003caf5155 | -1.8239 | -47.868099 | 2024-11-11 00:51:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d9ae8b2-d65f-31b3-9422-b19ae1017c0b | -3.6858 | -45.2379 | 2024-11-11 00:51:00 | METOP-C | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 54096c20-73f9-3dd1-8b3c-e5c5a249900f | -1.2506 | -51.770302 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a0661a9-f3eb-3108-b953-bd38168d1b26 | -0.6504 | -51.717602 | 2024-11-11 00:51:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9480b0c6-3fc8-3e64-b6c8-4327e6b5de93 | -17.626101 | -57.511799 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91edc891-eeb1-3798-976b-47c4111b8ac7 | 0.4606 | -50.966099 | 2024-11-11 00:51:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d6aa826e-ae0d-3163-a6c9-496a776d1cdb | -1.3993 | -52.373199 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02f74ca2-ddbe-340c-bcdd-41e9b0e8bf11 | -2.7142 | -49.304401 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22ec7cf1-b607-3651-80bf-6dd644c8a52e | -2.4625 | -50.401501 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1165a933-7932-3b9e-8e5b-bca1bca2e99b | -3.7925 | -55.876499 | 2024-11-11 00:51:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c929670-492d-3935-9b76-59d04124cc43 | -2.6882 | -46.807098 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 959a8a4f-9e72-3c81-9b4e-c6d6375f6e3e | -1.195 | -53.687302 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd76fb29-1314-3d5f-8e53-7452ccffe123 | -3.6081 | -50.582001 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84846c5c-ae32-3a28-9cef-d25bdb9ee455 | -17.271999 | -57.498199 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75b71d0b-9f86-37d1-8dc5-df4a1bd96a9f | -2.9791 | -46.993401 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e34e01ee-a813-31c8-b860-8c5593697f66 | -2.2903 | -48.544498 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2804c0eb-5e5c-3a58-86d3-514c9fe90e16 | -2.848 | -49.436501 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4553fa1-6fea-3beb-a21f-68dc4faf6f3c | -2.9159 | -45.633801 | 2024-11-11 00:51:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb0c3bd-b8d9-30cc-9971-a81b0717dc2c | -1.3962 | -52.3596 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 167c32b3-7a25-3149-8039-cd574f9938b3 | -3.8863 | -52.1982 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 265c58f9-0b60-341d-91c4-0c53247ed11a | -4.1015 | -49.103298 | 2024-11-11 00:51:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d8b4482-8b22-364d-875a-fc9a5f295f00 | -2.2399 | -53.7934 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0325924b-afc6-30f7-8013-fc5f36063892 | -1.6196 | -52.5242 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5608a828-90e4-3ed1-8208-02505c2c6553 | -3.5284 | -45.7006 | 2024-11-11 00:51:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 72ebfa01-9bb9-3485-826f-023824043a14 | -2.8168 | -51.806801 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46460af9-7422-3559-a008-a415e3f4df85 | -17.2978 | -57.473701 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a524a67e-cfae-3ade-a6f7-50475af81b5c | -2.1776 | -53.701099 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 346128d6-efc4-3dbf-aa46-3b71afd6d3ee | -2.8237 | -52.963902 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 510276df-5e19-38ed-9128-db18b0a92f8f | -2.3451 | -48.514099 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f45f794-9e52-315c-b879-fa5175717770 | -2.6636 | -49.3974 | 2024-11-11 00:51:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 557673cb-5e84-3884-8b4d-83ea53f65942 | -1.5388 | -55.868599 | 2024-11-11 00:51:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 143af1b4-9cb0-301d-9831-6b0c646e622b | -3.7019 | -54.652401 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b582b93-6764-3c36-984a-cc42c46bb034 | -2.8154 | -54.0126 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e22515a-a36a-3163-8f6d-f8e065bcaec4 | -2.8418 | -52.546299 | 2024-11-11 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cac7ce6c-8520-37a4-808b-11e0be39badf | -3.0366 | -49.538101 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73e59c7d-8416-3815-9825-4ed06eacd36f | -2.652 | -49.391899 | 2024-11-11 00:51:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20258ac6-9512-3aae-9445-d49195859e9c | -3.0445 | -50.330502 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51b2930b-a11c-3ebe-a615-2f4be36456c2 | -2.1874 | -48.367901 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0455d953-da8f-3ea5-b6df-53383d00ed93 | -2.2003 | -49.5345 | 2024-11-11 00:51:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca071a5-cf18-3e65-9bab-9d1dbd141a84 | -3.0384 | -49.545601 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebb4e47a-cf48-3718-8044-716b58877fe5 | -2.9815 | -47.003601 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9308d11d-d8dc-3681-bc32-8bb535da0de9 | -17.6089 | -57.415199 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 019f4605-aa74-3c92-aae1-ab08faf1e90d | -2.8092 | -51.593899 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c7da40-3572-333d-827a-8a852f7e4ba1 | -2.5578 | -54.737 | 2024-11-11 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c3b093b-3982-319c-925d-489fe1e429cb | -3.1086 | -45.275799 | 2024-11-11 00:51:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 971a233c-e196-30ce-b8f5-4f10ae54aeb1 | -1.5419 | -54.302601 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ee916b4-f1a7-3781-a6c8-5380d8e66f7e | -2.2518 | -46.526798 | 2024-11-11 00:51:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 349bf645-248a-3f04-ae9f-c1d5660779a4 | -17.301201 | -57.492802 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a8aec396-386c-30bc-900d-324ffa5e812e | -1.5469 | -51.847401 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0b90494-a80f-38e2-b8da-bdb52e0282ee | -2.2496 | -53.745701 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0910f56-b5e1-39b7-9ebd-5de38116b3d3 | -3.4565 | -54.6138 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a017d28-46e1-393a-bd40-a9b6165d6076 | -3.1313 | -50.438 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6620dde-115b-3190-94b8-b28e025f9dda | -3.1586 | -54.480499 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdfe424d-5676-3b55-bccc-8d34962c1b19 | -2.9493 | -52.565601 | 2024-11-11 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1147a419-03e0-329b-a8df-15284a049477 | -4.1095 | -49.0933 | 2024-11-11 00:51:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc8de4eb-b7b6-318a-ae82-cc47bc2c66b2 | -2.7215 | -54.143101 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03ed346e-a146-3d97-a761-714640f1c59a | -2.5763 | -47.340599 | 2024-11-11 00:51:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af24fa95-f0eb-3f59-a4b1-91f799e85fe3 | -3.0822 | -50.493599 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d68dca06-0e9e-3008-9d0c-84b0202779a6 | -2.8431 | -53.9986 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26403897-9f09-37c1-aece-3853d5c74db3 | -1.1768 | -53.923401 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eab4a349-3dfa-33ad-b6d1-d94fb747be11 | -17.622101 | -57.432598 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52e91863-22dd-3ea0-b020-771a152f7252 | -1.5396 | -52.2206 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e11953ab-eb11-3d18-a06f-3a7f98ea9642 | -2.914 | -49.365002 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09e85d82-9dc6-370f-b873-dbde283806ea | -2.9122 | -49.3573 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6628fab-d64d-3b65-9dba-a7e6f2cdda15 | -2.4707 | -50.392101 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dca5285-92b6-377c-972b-d2b9a486ac73 | -2.2332 | -46.447601 | 2024-11-11 00:51:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40d5da58-3fa2-319c-96d9-8e6fb515d43c | -17.288099 | -57.475498 | 2024-11-11 00:51:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8685d245-5978-3e3a-a073-370352c27233 | -2.207 | -48.3634 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe21d4d0-69ec-3576-b96b-bf44a71068ad | -2.9278 | -51.4813 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 208b130d-a0b4-3aca-85d7-0a389f5357c3 | -1.6675 | -55.168999 | 2024-11-11 00:51:00 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d1609c8-8e82-3a47-bb97-8128caa14bcf | -2.4523 | -53.6856 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 586c77c4-2723-32d2-8268-bcc0a7fc98b3 | -2.416 | -46.5247 | 2024-11-11 00:51:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4901aa3b-9ea0-3be2-a5bb-004791ac03e2 | -1.431 | -52.781399 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 061a8eb4-1ac7-3d19-99b5-b1a45829051f | -1.0211 | -48.849499 | 2024-11-11 00:51:00 | METOP-C | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c58c8ba1-8eab-370d-b070-e2535ae56130 | -2.6782 | -48.660599 | 2024-11-11 00:51:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e86358-c2ad-3c2b-9b47-0afe882454b8 | -2.5499 | -53.978001 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
