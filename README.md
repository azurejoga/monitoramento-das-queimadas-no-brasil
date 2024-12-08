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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75682953-2bb6-33ba-9561-6c7270cac79d | -2.802 | -52.8396 | 2024-12-08 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 998c3b8c-cc30-323f-9b45-e0171ba41277 | -11.771 | -54.7237 | 2024-12-08 00:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 1204a6cb-00cc-3e43-a712-54a34bdf7539 | -11.752 | -54.7255 | 2024-12-08 00:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| b084cf35-7b9e-3767-a428-375baf31464a | -5.4239 | -47.0049 | 2024-12-08 00:00:00 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 67c28906-d771-310f-b49a-4199d9b861e2 | -2.8203 | -52.8595 | 2024-12-08 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| cc9fcc29-ab45-3d63-a23a-eb5ee3b01b51 | -2.7834 | -52.8808 | 2024-12-08 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a872f665-73e9-3994-8287-4fff2fd1a977 | -2.7835 | -52.8604 | 2024-12-08 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 4545343b-7cda-3a8a-ab9c-cfc3506a701b | -2.8019 | -52.86 | 2024-12-08 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 243.8 |
| 2317f574-a30d-3d98-b5fe-3ce7caff575e | -2.8018 | -52.8803 | 2024-12-08 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| eff6ae30-67b5-39d9-8dd3-63d2aa6f269a | -11.771 | -54.7237 | 2024-12-08 00:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 6b4fd88a-cc71-3478-8980-96f1e3236e1c | -11.752 | -54.7255 | 2024-12-08 00:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 82cca898-ff98-3cef-a9ca-1186865ae9b0 | -11.7523 | -54.705 | 2024-12-08 00:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 4e1f6a1e-9b57-3526-ab4e-83600149713e | 1.9955 | -61.1394 | 2024-12-08 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 092e7252-638a-353a-9bb6-e73403808326 | -10.1445 | -36.1678 | 2024-12-08 00:10:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 139.9 |
| fa7a88f9-104a-300c-a5ba-0621c8c86859 | -11.7518 | -54.7459 | 2024-12-08 00:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| da82acdb-daa6-3bab-9334-686315b1cd3d | -10.1638 | -36.1643 | 2024-12-08 00:10:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.9 |
| e06d40c2-96c0-374f-836f-e263747a3174 | -7.1137 | -35.1192 | 2024-12-08 00:10:00 | GOES-16 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 88.3 |
| acb1bff7-8527-3da5-a6ae-77f159231ddf | -14.51635 | -39.7378 | 2024-12-08 00:13:00 | TERRA_M-M | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7045c269-b872-3cb9-a7a8-3da65f746575 | -17.81586 | -40.12022 | 2024-12-08 00:13:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.2 |
| 49d510d0-961c-3c6a-8a54-dc6156aa64b4 | -15.4798 | -41.64948 | 2024-12-08 00:13:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| c7154d03-091c-3e59-afef-6581a5bc91fc | -17.80519 | -40.11589 | 2024-12-08 00:13:00 | TERRA_M-M | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| e4198fba-7974-318e-8621-cf4abbf337be | -19.25942 | -40.10799 | 2024-12-08 00:13:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 2007aa1b-a5df-3da5-b93e-2d151be55c33 | -17.81668 | -40.12628 | 2024-12-08 00:13:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| e02b4d20-82f2-3d9b-998d-8ce5c93ed857 | -17.81519 | -40.11448 | 2024-12-08 00:13:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 50.2 |
| 1b79f7f5-d681-320c-984b-d30722759b6d | -17.80668 | -40.12775 | 2024-12-08 00:13:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 19aced8a-8bef-3d88-839a-8d5b0698a2f1 | -17.46985 | -40.11895 | 2024-12-08 00:13:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 37310344-9388-330b-802b-f6d0826e8e20 | -17.46841 | -40.10716 | 2024-12-08 00:13:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| eab512b3-fa3b-308f-9cab-8d51df31fe5b | -9.60736 | -42.13903 | 2024-12-08 00:15:00 | TERRA_M-M | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| a602d1ad-04de-3279-b9ea-0e313bcb16c5 | -9.44619 | -35.94418 | 2024-12-08 00:15:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| cdb0fd0d-2ab9-3442-92c5-a8b3284847cc | -10.15532 | -36.17897 | 2024-12-08 00:15:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 149.9 |
| 9cc822ca-4167-37f6-8d6e-26aeafd5daa6 | -10.14433 | -36.17004 | 2024-12-08 00:15:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| d69b11e8-5f57-3272-833e-fc800e5295e2 | -10.22822 | -36.67957 | 2024-12-08 00:15:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 79acb7cf-2dc6-3736-ab48-65c64416826f | -10.14586 | -36.18043 | 2024-12-08 00:15:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| fe4f1c17-7d93-395d-87e5-94053dd6cd40 | -9.44938 | -35.96561 | 2024-12-08 00:15:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3a17dc3d-2e69-3f07-ab67-2b72276e37a0 | -10.1538 | -36.16861 | 2024-12-08 00:15:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 219.5 |
| 2072d070-5c4e-3bb9-b761-470466afdefc | -9.44778 | -35.95488 | 2024-12-08 00:15:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 54.2 |
| 0cb63576-e769-35a1-b94f-729656269bf2 | -11.49114 | -39.04464 | 2024-12-08 00:15:00 | TERRA_M-M | TEOFILÂNDIA | BAHIA | Brasil | 2931509 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d8ba0c13-eb3d-3874-950e-359d109e1728 | -5.63471 | -38.64334 | 2024-12-08 00:17:00 | TERRA_M-M | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| da21412f-2434-3270-a0c7-a8fde2ad42f3 | -5.25163 | -37.50513 | 2024-12-08 00:17:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 33e7c53a-241c-3dbe-a9b7-64fb1f8e1922 | -5.43882 | -47.03119 | 2024-12-08 00:17:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b9fa759e-2156-3ea7-915d-f87f08b0f7f5 | -5.53254 | -42.87735 | 2024-12-08 00:17:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 56bafc68-2051-327d-96bf-f3be53b6912d | -8.10245 | -35.11586 | 2024-12-08 00:17:00 | TERRA_M-M | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 927c7655-ffaf-36b7-8ec9-ff2fac3f9c3c | -5.4311 | -44.71863 | 2024-12-08 00:17:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 248b5c1b-7b28-31d9-bb96-818fb1cfd752 | -8.09471 | -35.11026 | 2024-12-08 00:17:00 | TERRA_M-M | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| ae58110c-2dbe-3668-b61a-08de3e76fe22 | -7.96026 | -39.93932 | 2024-12-08 00:17:00 | TERRA_M-M | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 749d0343-c007-3e83-977f-9dd6f2ced3c1 | -5.42913 | -47.02695 | 2024-12-08 00:17:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 0597fdfb-5cd0-3d57-9c98-549e47a1106a | -5.57628 | -45.22203 | 2024-12-08 00:17:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2d4bbd09-98f6-3f2f-bc6c-1aac165974d0 | -5.43556 | -47.00702 | 2024-12-08 00:17:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| b51be405-422b-39c8-9d7a-8b25593e5e3e | -5.55283 | -42.8745 | 2024-12-08 00:17:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6283f2dd-fbec-398b-ae3e-94c2078feee8 | -5.47485 | -39.41118 | 2024-12-08 00:17:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| c1486e95-d864-3168-9a91-be26a4f04097 | -5.69627 | -39.40675 | 2024-12-08 00:17:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 69162643-a374-3b44-9eb7-5e01ae199c2e | -7.11196 | -35.12604 | 2024-12-08 00:17:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 17ccd98e-38bf-3646-b7e0-8116083356f6 | -5.47608 | -39.42002 | 2024-12-08 00:17:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 21.6 |
| d6a0450f-6c0c-34d6-8ef4-68b82ee511da | -8.26876 | -35.18633 | 2024-12-08 00:17:00 | TERRA_M-M | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| b2b567c5-0c10-36f2-b9e2-fd851de78430 | -5.54268 | -42.8759 | 2024-12-08 00:17:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c6b48ce7-5686-360a-9541-768cb1ddbea0 | -5.42899 | -44.70258 | 2024-12-08 00:17:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 9492be7b-150c-3439-b276-9dbe84581867 | -5.7775 | -39.19921 | 2024-12-08 00:17:00 | TERRA_M-M | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 74cdebf5-ca0d-36a6-af3b-74e436440c75 | -7.11003 | -35.11324 | 2024-12-08 00:17:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 117.0 |
| 7c01d24a-8bdc-3c4d-8fd7-8ef07b2bf57f | -5.42605 | -47.00262 | 2024-12-08 00:17:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 8d3cc4c1-c3bc-3323-b856-93648b9b87e9 | -5.25305 | -37.51501 | 2024-12-08 00:17:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 59f5068f-c529-3461-ba44-299f39a2ba83 | -7.98762 | -45.80333 | 2024-12-08 00:17:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e00b0c1a-6ffe-315e-90d2-0224b3d1d590 | -3.41236 | -39.08603 | 2024-12-08 00:17:00 | TERRA_M-M | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7722ac6d-ab8a-30e5-843c-3e88316bbe2a | 1.9955 | -61.1394 | 2024-12-08 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f4a79d49-45c2-31aa-9d20-ea732f4b2b8b | -5.9186 | -48.0232 | 2024-12-08 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 4fbf4c8e-1c60-3b99-8249-7c8aacff3fc2 | -11.752 | -54.7255 | 2024-12-08 00:20:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 3bc6933c-bf19-3fea-aea6-3c21754064a3 | -5.9373 | -48.022 | 2024-12-08 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| aa3621c8-62c7-3685-b760-e20a1044ea23 | -5.9185 | -48.0449 | 2024-12-08 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4afd5a5c-b807-34b2-8328-d2730efd2fae | -11.771 | -54.7237 | 2024-12-08 00:20:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b7ecaf7f-df99-3577-bda6-5939b5f9d4c6 | -11.7518 | -54.7459 | 2024-12-08 00:20:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 8f7843bf-b1e8-353f-a5a0-3365e899b473 | -5.9373 | -48.022 | 2024-12-08 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d9d401e1-8331-30b7-a399-c7bc78b53d0b | -5.9185 | -48.0449 | 2024-12-08 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 66cfe715-fc02-37a9-aff0-11481c650beb | -11.752 | -54.7255 | 2024-12-08 00:30:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 169.2 |
| c2dccbdd-4fc1-38ed-adc7-7ff6498a4386 | 1.9955 | -61.1394 | 2024-12-08 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 26f7bfea-c2ba-3c2c-ad41-5b101a88db0a | -5.9 | -48.0244 | 2024-12-08 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e901e564-01b0-353f-a58d-a87266fdbbc7 | -9.326 | -40.2338 | 2024-12-08 00:30:00 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 3a762914-7c97-39ff-b4b8-8ed10185815a | -5.9186 | -48.0232 | 2024-12-08 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| be17798c-fa9f-355e-a0b5-4d9f42b11b50 | -9.3069 | -40.2365 | 2024-12-08 00:30:00 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 3ebf2435-4408-3649-bbe5-9a9c043ae39d | -7.9815 | -50.691601 | 2024-12-08 00:30:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6cd7980-9148-3426-9f94-ec71241f2eee | -3.8836 | -54.199902 | 2024-12-08 00:30:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aa67b83-bebd-3aad-a30f-6180e0717a16 | -3.0799 | -54.053699 | 2024-12-08 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2240b19c-7476-3f4e-b0b2-16e3c14920fd | -9.224 | -50.6772 | 2024-12-08 00:30:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28153d41-7164-3362-b04f-22330954664b | -3.0764 | -54.037899 | 2024-12-08 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a19378-9301-3512-8790-93b4d451546a | -16.2017 | -55.917301 | 2024-12-08 00:30:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 34fcf540-01d5-31be-a866-5b004612398b | -4.5805 | -48.012501 | 2024-12-08 00:30:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90877441-f229-3f69-9a54-2d61f04d983c | -3.8203 | -54.610001 | 2024-12-08 00:30:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cdc7a5e-ef48-338b-8f49-e4359484a486 | -15.3646 | -53.098202 | 2024-12-08 00:30:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23e00eba-20c9-330e-a9f5-618aa6b07967 | -3.1112 | -54.055302 | 2024-12-08 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58d145a1-b86e-38a9-b398-fe821203fd40 | -9.2225 | -49.471001 | 2024-12-08 00:30:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72fb8f30-efc5-3956-a87c-1aee4238ff71 | -3.0782 | -54.045799 | 2024-12-08 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 548bb391-271a-3e4c-ba53-7d93d6c63593 | -3.1094 | -54.047298 | 2024-12-08 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 773decbd-3b50-3b76-9dba-2e3e75d967d0 | -15.3784 | -53.116402 | 2024-12-08 00:30:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| baf6efc4-4a85-326d-b27e-fbf778cf422d | -9.2255 | -50.6842 | 2024-12-08 00:30:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa3d884d-add7-3d51-84e2-fc309fa8e493 | -12.5382 | -48.313301 | 2024-12-08 00:30:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5dbb29aa-58e6-3137-a323-adf8c2172a4a | -3.0817 | -54.061699 | 2024-12-08 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee27c57-1fa7-39ed-8c71-390f53726d18 | -13.8818 | -47.369999 | 2024-12-08 00:30:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 16c0a085-6fb7-34c6-bb71-3bd12634b382 | -7.98 | -50.684601 | 2024-12-08 00:30:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2483aa27-84d5-3f2f-b35d-452cca01b4eb | -3.0996 | -54.0494 | 2024-12-08 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52ed0559-9756-3820-9bc2-8cec5179f53e | -3.1192 | -54.0452 | 2024-12-08 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b82c83c-3b71-3aae-ae89-c5c5be9641ae | -4.5787 | -48.004398 | 2024-12-08 00:30:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca996118-1ecd-33a6-89c1-2a091d673bb0 | -12.8611 | -51.911999 | 2024-12-08 00:30:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
