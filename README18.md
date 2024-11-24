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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37e1f888-8daa-3395-9e83-a84cdf47651c | -2.80459 | -46.80782 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5bec2b54-750f-342a-9e88-e39d29f81bd5 | -2.14741 | -50.92467 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| a2241082-eba9-31c8-bc36-95469d1bf2d7 | -2.0769 | -47.06927 | 2024-11-24 00:49:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d20a53d9-7d8a-36c7-9158-30525d462848 | -4.05566 | -48.32059 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b355cd05-c8b5-3ed0-a9f6-4590fff643a1 | -2.59407 | -46.55497 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e6af2266-72ce-39e4-8684-82ab7e80530a | -2.73785 | -49.11197 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 81b98f38-8683-3991-8009-26598056937c | -3.31105 | -45.69123 | 2024-11-24 00:49:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d00c81a2-8aa0-3f79-b4bd-3a844d0b7d22 | -2.55809 | -46.56012 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f2100d15-5232-323f-847c-23ca0b646fc9 | -0.2545 | -51.57038 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 842b45b7-5c8f-3146-86ed-973d0b32fa3b | -0.28509 | -51.49991 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8b1739e3-4fb7-3915-884c-2926bfe3df29 | -2.24635 | -49.21718 | 2024-11-24 00:49:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 390d73d8-40db-39a5-aa04-137109e2c901 | -1.25884 | -51.74678 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6852321e-0866-3fc9-bc7f-371f90043131 | -2.38532 | -48.95865 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d0f13f2a-98a0-3fcf-addb-0e44e92f607e | -4.09349 | -50.36115 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 34eb4eab-d690-32f0-843f-ada3458d1df9 | -1.82414 | -46.64771 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 03c5f060-5a5c-3233-a0ee-b29610223956 | -2.4396 | -49.08657 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 30763545-c9ba-30eb-b8b7-b470c9fa4f58 | -1.21711 | -53.67378 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a7b421ab-6ae7-326f-b4d1-cfd8a8bcc1f4 | -4.53703 | -42.90544 | 2024-11-24 00:49:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 1ccc0f23-e228-3e56-a472-fa2a8302e631 | -2.53609 | -46.40441 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b2f9dc3e-c6c4-390f-8a15-ec2633a12f8d | -1.43002 | -46.06805 | 2024-11-24 00:49:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 462bf44a-ccaa-32cd-bbef-2f6a5df61c80 | -3.94814 | -50.20317 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 0ee45848-22e4-3a17-b5d6-73f725b8e91c | -4.24141 | -48.66524 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6c88d863-fdae-39a3-a84b-d5bff02df371 | -4.95081 | -47.79769 | 2024-11-24 00:49:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 27effba5-0bf2-3544-8a56-da700504b29c | -1.82285 | -46.63855 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 223.9 |
| 4bb8e348-7144-371a-bde3-ff50c791bead | -3.62009 | -45.06427 | 2024-11-24 00:49:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6661541c-ede7-32a5-88db-03e70b776a31 | -4.43893 | -45.39974 | 2024-11-24 00:49:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a2980467-b90d-3017-9cb6-5075007efd22 | -2.58919 | -54.22301 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| fb875a8f-b71a-3682-b32e-205f37b856f9 | -3.61644 | -52.46019 | 2024-11-24 00:49:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 46b83a9e-83a1-3455-9b38-534803112ad2 | -3.96079 | -45.98982 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0e61e60-ab07-3e97-be0e-ffeeb4c343f3 | -3.76492 | -44.06015 | 2024-11-24 00:49:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9866d272-04be-339b-8f5e-c0c13934ed52 | -1.40829 | -54.4696 | 2024-11-24 00:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 9979f459-dbab-31c9-b819-f07a162ea95d | -3.10866 | -53.99842 | 2024-11-24 00:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 043bca71-dc78-3c80-8010-90cb8baa633e | -2.71462 | -46.10107 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 924f35c7-4443-342c-afe6-ef2bcdbfcbbd | -1.12828 | -48.33592 | 2024-11-24 00:49:00 | TERRA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26963374-b051-3689-9513-2034ad71ea40 | -2.7018 | -46.20791 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b59d11c0-f988-311b-b3dc-aadbe265ed56 | -1.82148 | -47.55451 | 2024-11-24 00:49:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5d7b65c3-7821-30a7-9b4b-90a75d35cda9 | -2.64598 | -46.13628 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| fd1ebd89-bdcb-3582-aa06-c14de6935a3a | -3.05023 | -45.07804 | 2024-11-24 00:49:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 29.8 |
| ee68ee8a-0fe5-3b50-83da-7f5713f3e519 | -1.72737 | -53.25298 | 2024-11-24 00:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0dc3e993-2349-348b-a13e-3e8da732b5dd | -2.57441 | -49.19486 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0efa973a-f0f6-3e12-bc71-32e0c3c81b08 | -2.87067 | -45.83379 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 86d2bc11-4be7-3616-a1a6-f3a239fe00a5 | -4.48059 | -46.08303 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 153a24d8-a6e9-3ce7-8352-aae18ca614ce | -1.2484 | -51.74824 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1f81d1f5-77e4-3376-881b-564a4e3dcdec | -2.46172 | -49.04561 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 82ed276e-7645-3783-ad2c-fae69dbb8329 | -2.75103 | -48.6722 | 2024-11-24 00:49:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f0cb8a57-571d-3ca5-96d5-f1949a84a336 | -3.8441 | -46.00909 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 863329fa-56e5-30fc-b33f-613c4ed80af3 | -3.17418 | -45.30428 | 2024-11-24 00:49:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 30c687e9-3d19-3a2d-a4c7-c770ce388f12 | -1.73713 | -52.73122 | 2024-11-24 00:49:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 3938c84a-f8d4-3296-b755-faa14be59d4c | -1.6132 | -52.57906 | 2024-11-24 00:49:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| f38bd17b-1398-3447-80f6-fd5e3d104e52 | -2.59279 | -46.54586 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5ed36611-0be8-3a2c-a76c-ebbba670025c | -2.86454 | -51.8309 | 2024-11-24 00:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 32ab7f25-df90-3574-9746-e1647a735250 | -2.21411 | -48.91992 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d6cad1f7-8e1b-320b-b68f-8a1a76282381 | -2.16901 | -47.93641 | 2024-11-24 00:49:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 96c1c72b-40e4-3bf1-a077-c684347d1ee0 | -2.0756 | -50.3239 | 2024-11-24 00:49:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 490a3819-6153-3276-bb13-28057fa3c9a2 | -3.15389 | -50.5917 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1dfa2c82-87f1-3ff7-85d3-e3c80cacc8ce | -2.66547 | -46.60378 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2828719e-d7a1-3121-b2f4-5f5a6c245ccb | -3.28775 | -45.52566 | 2024-11-24 00:49:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 99ad55f8-8f3b-30d1-92b6-f9d2ec276dd7 | -3.67844 | -47.12797 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 40e56156-208a-3b8b-8a18-515dc5edcbca | -2.22076 | -46.38866 | 2024-11-24 00:49:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 82a356fb-37f6-35de-a24c-669680f1cc4d | -3.24399 | -45.55194 | 2024-11-24 00:49:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f123cbb4-cd9f-3818-8a7b-4c18a7532295 | -1.28844 | -51.72989 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ee32e739-ff7f-3e68-8cec-f57bd664d2cc | -0.91896 | -51.64224 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7d67970d-aeda-3b68-b980-3668dbd8a1e7 | -3.24455 | -54.23907 | 2024-11-24 00:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| faf365d9-a87f-370c-8fc1-6ea9edf84141 | -2.91676 | -45.37026 | 2024-11-24 00:49:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 372.2 |
| cc6fe1b0-d016-3a04-9648-5c5f07e06f38 | -3.97267 | -46.72691 | 2024-11-24 00:49:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d53502f6-6424-3bbd-a159-ee2bb945d6ab | -5.19403 | -49.16024 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 5393b27b-865f-370d-aabe-00bfc2ece6c2 | -4.76963 | -44.79694 | 2024-11-24 00:49:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6f9cc4f0-ad78-3fe6-b567-a890a517876a | -3.20613 | -52.5713 | 2024-11-24 00:49:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 9a56536f-5d45-3d97-b7eb-46780e9e727f | -1.93977 | -49.5254 | 2024-11-24 00:49:00 | TERRA_M-M | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 87ea6b48-ec0e-3a57-a320-3c983f713b19 | -2.24374 | -49.19847 | 2024-11-24 00:49:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e15d033b-ffd7-3fed-9ea7-cf707a466eb8 | -2.43198 | -49.0309 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| dabb8f64-e648-32ba-b58c-3acf5e5d83e0 | -1.29888 | -51.72843 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 73da3873-04c9-3ed7-b962-08602b77d667 | -3.29802 | -45.73238 | 2024-11-24 00:49:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 3c35f02f-6168-3df4-af9c-3cc08df877ba | -1.61252 | -54.43047 | 2024-11-24 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 00d1c6ff-c560-3997-8213-3ec5313f71f7 | -4.31578 | -48.07262 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| eb9595f7-d524-398c-8081-2da3e9472789 | -3.91389 | -47.96247 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e8cc8888-7c6b-300d-9eb5-3c4bd59ad27d | -3.83503 | -46.01043 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5d6c576a-74cb-3908-89d6-cf553cdcc374 | -2.39821 | -47.92147 | 2024-11-24 00:49:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| abfbe6f4-1b98-3cde-b82d-7e87cefd6114 | -4.71034 | -45.43126 | 2024-11-24 00:49:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3793206c-9ba0-3a10-aa37-3726d4b2334d | -1.22705 | -51.79597 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 58fed9b9-a34d-340f-97a8-6ac5cb4a6a63 | -0.97906 | -47.12431 | 2024-11-24 00:49:00 | TERRA_M-M | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d49af5f0-9182-3a23-9d39-9056954f902c | -3.25494 | -54.21618 | 2024-11-24 00:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| c33467cf-975a-3ae3-a201-a1758945bc9c | -3.2709 | -50.62679 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c659a9e7-8ce8-3783-8c6c-92407d0efa38 | -1.23625 | -51.73716 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2115dfcf-92f0-3eab-aabc-00e7ef9ec61e | -2.73914 | -49.12137 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| fe0c71a2-5584-349b-aa5c-a52606632941 | -3.04877 | -45.06763 | 2024-11-24 00:49:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9b9c296a-51b5-3525-8925-cff032f7bb72 | -1.9648 | -48.38873 | 2024-11-24 00:49:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 1b5d7691-4b2b-3fc0-8c42-8ef498b68cba | -4.26465 | -48.69985 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0116d704-cdeb-3144-a4dd-174369810def | -4.10866 | -48.50183 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 65251824-65d5-3406-8cd1-60364cc0cb15 | -0.19253 | -51.49556 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4c6088e2-3f8d-39bc-971a-4eed685fc613 | -3.49411 | -50.46358 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5894ce63-51c4-3638-bbaf-f129a498bb39 | -2.66675 | -46.61286 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8d420088-3014-3fef-b8b2-03232726af09 | -0.87745 | -51.72302 | 2024-11-24 00:49:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0d394e64-143f-3605-b5d4-47dab8eee45b | -1.36156 | -53.84348 | 2024-11-24 00:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| e19db899-ebc4-3ca9-a3df-a32ee263ba14 | -2.20383 | -48.91204 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 05ae42be-1ad0-3b47-9521-a138db43d04a | -2.78946 | -51.67932 | 2024-11-24 00:49:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 49b4afe0-e6e9-3655-8d3f-541b1345a6c4 | -2.93647 | -46.69436 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 655f13b9-35e1-3cde-859e-6301f60c1acb | -3.05554 | -53.22592 | 2024-11-24 00:49:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a55b1606-a8fe-3a83-bddb-bc5605012de4 | -2.22206 | -46.39796 | 2024-11-24 00:49:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 272fc917-36dd-3579-94d7-19477346fcb2 | -3.07111 | -50.96008 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |


[Clique aqui para ver as próximas entradas](README19.md)
