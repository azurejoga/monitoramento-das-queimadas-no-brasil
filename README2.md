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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 325f6b08-aa41-39e1-bf20-1e49b9ccfe3a | -4.3705 | -43.1274 | 2025-12-02 00:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 2751e854-bff8-34eb-89ad-6c0174acd5ce | -11.1193 | -53.9241 | 2025-12-02 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a84ce46c-c7a4-3bf0-aaf1-164b97a52417 | -4.4077 | -43.1486 | 2025-12-02 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| cf8416fe-5ee3-3833-b0d2-85342690d29b | -11.1382 | -53.9223 | 2025-12-02 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 79da9025-9d15-37ed-9c6a-03bfab05ebf6 | -4.389 | -43.1497 | 2025-12-02 00:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 322.3 |
| 51320f06-d3a5-30d9-aa0d-5e253fe5d672 | -3.8618 | -47.0438 | 2025-12-02 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 404bf22a-d6df-3db2-b026-7eb8ee5cf722 | -11.119 | -53.9446 | 2025-12-02 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 10d7afb1-39e1-316c-a9d5-18203cb1f5f4 | -12.8853 | -52.4962 | 2025-12-02 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 09c2c5f3-61be-325f-8c16-eb74d62ce5a1 | -13.0392 | -53.7107 | 2025-12-02 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 0257835e-a23f-31b8-be4e-cc4c119fcca1 | -17.5338 | -57.1901 | 2025-12-02 00:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 9cb95fed-b620-3b99-8118-803caeb75f88 | -3.8618 | -47.0438 | 2025-12-02 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 309f5948-f8bc-3007-b894-fb55f52cedc5 | -17.5141 | -57.1925 | 2025-12-02 00:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.5 |
| 6fa68aea-6293-310c-b883-1dda96f4f0d9 | -17.4944 | -57.1949 | 2025-12-02 00:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 3c349501-a1a0-3d5b-b90e-76b337f60d34 | -3.4901 | -43.592 | 2025-12-02 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6a732831-4537-3038-b291-1a42e410effe | -12.5211 | -56.9222 | 2025-12-02 00:40:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| d3726ada-1252-3199-9d91-1397b45eda84 | -12.885 | -52.5172 | 2025-12-02 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 57f9e88c-5d2b-383e-b3c7-3821b88c67c2 | -12.5213 | -56.9022 | 2025-12-02 00:40:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 0f23ab01-53d9-33a5-ab1b-ea69b1e396aa | -11.1193 | -53.9241 | 2025-12-02 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0b15e26f-84e1-30be-8f97-f651bb4346b2 | -12.5023 | -56.9038 | 2025-12-02 00:40:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3a9a4788-876b-312a-bdb5-5d12248265be | -8.163 | -43.229 | 2025-12-02 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| e4c23e7e-d3cc-3773-a48e-787044fe9796 | -11.1382 | -53.9223 | 2025-12-02 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| e906e657-66b4-3496-a93d-baa959984baa | -4.3703 | -43.1508 | 2025-12-02 00:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 25f721e4-70de-358c-890c-ab195696309d | -17.5138 | -57.2131 | 2025-12-02 00:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.6 |
| 2d0fb8f8-2696-35d4-8f40-5744122a4fd5 | -17.5335 | -57.2107 | 2025-12-02 00:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.6 |
| 4badc590-44e2-3717-be60-c854942c2aef | -4.3892 | -43.1263 | 2025-12-02 00:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c7d77724-2831-3141-b35d-3da74c9f012c | -4.389 | -43.1497 | 2025-12-02 00:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 82c60a6c-6d0b-38b5-bf94-e72963cc7bbc | -8.1633 | -43.2055 | 2025-12-02 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 1b1a4647-68e5-32fe-895d-48505ef82622 | -1.4923 | -45.7903 | 2025-12-02 00:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 6c56cf2c-6842-3600-8b74-8c147d31955f | -11.1379 | -53.9429 | 2025-12-02 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 7a9dd613-e411-3c4f-853b-5d238f63e4c7 | -1.4737 | -45.7907 | 2025-12-02 00:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 105.6 |
| b7f331e2-1764-3b77-84c9-a5a04df087c8 | -4.4077 | -43.1486 | 2025-12-02 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1ecbb8fa-92dd-3834-82cc-b5b5b6108288 | -17.56672 | -57.18091 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 8bad9b23-b971-3460-9c21-9ea91f17dcd7 | -20.31957 | -57.28201 | 2025-12-02 00:49:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| a8e647cc-1625-3cc3-9806-292f34c7a19f | -17.52721 | -57.2139 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| f0580769-18af-3d16-b359-051b85f0a963 | -17.51495 | -57.20155 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 06096f9d-cd8b-3687-8ce6-05acef6aaaea | -17.55605 | -57.18229 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.8 |
| bb6428dc-945a-3da2-9d2d-d0c2992dd549 | -21.0201 | -47.26339 | 2025-12-02 00:49:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| eb4a2033-7f56-3d8b-b8f9-660950da95aa | -17.73575 | -57.2451 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| cbcb6406-1850-32b5-a906-c359fd39a81b | -20.31784 | -57.26659 | 2025-12-02 00:49:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 20.5 |
| a0728265-062b-378f-988f-c60a3358d754 | -17.7465 | -57.24371 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 2c216a93-9795-3ad5-9cf8-986864a379cd | -21.93015 | -46.70854 | 2025-12-02 00:49:00 | TERRA_M-M | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 2c9263a3-853a-3e5c-93c8-747558ad7544 | -17.52563 | -57.20015 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 75bac0a8-49e8-3489-91a1-73c3014d9649 | -17.51653 | -57.21528 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.6 |
| 827cfc08-fa6a-3242-9b68-0c0db32820fd | -17.48844 | -57.19744 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| c153b8e9-199c-3546-93cd-f4d033ffb323 | -15.06424 | -54.51724 | 2025-12-02 00:49:00 | TERRA_M-M | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| da12ee4e-9fb6-3726-9986-5ac8acb88001 | -14.57017 | -52.86374 | 2025-12-02 00:49:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 850456c8-b24a-3046-9ae6-89a0d066a333 | -14.07832 | -56.16277 | 2025-12-02 00:49:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| a0351973-8010-3079-93fb-7fe67841fafa | -12.929 | -52.53761 | 2025-12-02 00:49:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 84243ba5-2228-3635-98a2-f2ee6a19d0d8 | -17.50978 | -57.1947 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.9 |
| b33aba5c-6631-3201-be04-56ee61eb4586 | -13.20037 | -53.15077 | 2025-12-02 00:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| e0d20b0c-2612-32cf-978f-23256c631ec6 | -15.97368 | -56.62683 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1980eca6-7691-3c1b-ad56-0359bd110b0b | -17.52212 | -57.20702 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.2 |
| 4291d059-827b-3bca-8ac8-8f2036105324 | -17.49911 | -57.19607 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| d94b196e-c8b4-389c-bcb1-b63d615f2f63 | -12.99333 | -51.96799 | 2025-12-02 00:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 4c667008-0446-3aeb-8252-48e5f04b1195 | -12.99478 | -51.97791 | 2025-12-02 00:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 69968d5c-d53d-32b4-a0ae-a5352580316c | -17.52045 | -57.19332 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 20d847a9-e00b-3240-ab16-586324dc7d5e | -17.52379 | -57.22075 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 60f2bca5-0dd6-3089-8654-873690d8b2b1 | -17.48681 | -57.18376 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| 6c57532f-9837-32bb-8f73-9dff38125859 | -12.93943 | -52.54575 | 2025-12-02 00:49:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ae4ba8d2-47fe-320a-a476-d4346fcd16c2 | -17.49747 | -57.18241 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 170bd65a-c4e0-36dd-b77e-fc31600a461f | -12.98406 | -51.96942 | 2025-12-02 00:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 766e8089-ec7b-3f84-9c44-7df462f0251d | -14.07969 | -56.17327 | 2025-12-02 00:49:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6d50a26c-2200-3f47-8054-6b44114bb95d | -17.51144 | -57.20839 | 2025-12-02 00:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 67ba3d48-a246-3e7a-94a5-6073361bbe93 | -12.5211 | -56.9222 | 2025-12-02 00:50:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 04780d81-8371-3f85-ad98-9c3b35855597 | -4.3703 | -43.1508 | 2025-12-02 00:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| a9e9f67e-7dec-30c0-9290-89e16b447430 | -11.1193 | -53.9241 | 2025-12-02 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 7dfb9ac5-6bb9-3ebf-bd26-1325d82d1bd8 | -3.4903 | -43.5689 | 2025-12-02 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 8901ae04-3ed1-35d9-a536-e56ff2da6d50 | -12.0424 | -54.2473 | 2025-12-02 00:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1fc39bf5-478a-3ad7-b8e2-9ef5435e0e0a | -12.8853 | -52.4962 | 2025-12-02 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5a4e8b1c-878c-3c30-8deb-e484bf0d211d | -3.4901 | -43.592 | 2025-12-02 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| aa66d6e9-5492-3b63-8898-dc3fa00d2c29 | -4.3892 | -43.1263 | 2025-12-02 00:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 5d775fd5-4658-36c5-ac08-600945c88123 | -12.5213 | -56.9022 | 2025-12-02 00:50:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a4d50918-b2b8-3e50-bf7f-f47fb4ee0c77 | -12.885 | -52.5172 | 2025-12-02 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 2388c83d-f5a7-3a72-8d91-ed422694e7c6 | -1.4923 | -45.7903 | 2025-12-02 00:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e8eac69a-5b5f-3301-84d2-ac1b313b79f5 | -17.5138 | -57.2131 | 2025-12-02 00:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.4 |
| 1594c921-b387-35f3-b1d3-94a908f2e805 | -17.5141 | -57.1925 | 2025-12-02 00:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| ab3cbc39-a5ad-3b83-b91b-f307643ebfa9 | -11.1379 | -53.9429 | 2025-12-02 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.8 |
| da6ce7ea-a819-34e7-8126-287c44f51039 | -19.7873 | -56.6851 | 2025-12-02 00:50:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 80c0bff2-477d-3c80-98be-a5b365a0be3b | -11.119 | -53.9446 | 2025-12-02 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 9771c597-5d57-3d9b-b938-3d86833f0462 | -11.1382 | -53.9223 | 2025-12-02 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| d3c8221c-82d8-370e-9cf2-d814ed42ee53 | -13.0392 | -53.7107 | 2025-12-02 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 21889215-1d17-32fb-99a8-df04965df6a6 | -4.389 | -43.1497 | 2025-12-02 00:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 9be0a0b3-4c44-3ef8-9bc8-a40f0d02c4fb | -12.8468 | -52.5216 | 2025-12-02 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a7736df5-ebd6-3924-a5aa-db603d151783 | -1.4737 | -45.7907 | 2025-12-02 00:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 106.3 |
| afc877b6-18c9-312a-8db9-4b1bf09f6e43 | -1.4737 | -45.813 | 2025-12-02 00:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e22cb8d0-60f0-3f9a-a452-9d273a513e3b | -17.5335 | -57.2107 | 2025-12-02 00:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.7 |
| 2da2b7e1-6c21-3d6c-ad60-40ea2ba2d424 | -12.51466 | -56.92506 | 2025-12-02 00:52:00 | TERRA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 047ba8d9-4e39-3859-b3e6-1f7595db6cda | -12.51177 | -56.90285 | 2025-12-02 00:52:00 | TERRA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4b38e117-5efc-33a0-80b2-4e103baacfbe | -12.0495 | -55.35658 | 2025-12-02 00:52:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c9b5a10d-dd6a-3ff7-a7d4-37f716c6b137 | -12.06255 | -52.53966 | 2025-12-02 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 81715a70-14df-3e17-a088-92c6bab2aba3 | -11.12804 | -53.9336 | 2025-12-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| d9281fb2-afb4-379d-b4c8-4308c73e4ac4 | -10.59879 | -53.44897 | 2025-12-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5129c2a0-3484-3d21-8723-7f71d3015866 | -12.4096 | -54.8885 | 2025-12-02 00:52:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 472eac4f-ef7d-3833-9095-e44520719703 | -12.52152 | -56.90155 | 2025-12-02 00:52:00 | TERRA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 556e6967-97c3-37dd-91f5-1161b23d4a06 | -12.65594 | -52.43171 | 2025-12-02 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 55d8b2a1-4d56-3cb4-97fa-4ad43b23de9a | -12.65732 | -52.44136 | 2025-12-02 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ba85a903-7f2d-3bcc-967c-a71ee204f1fc | -13.04107 | -53.71592 | 2025-12-02 00:52:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| f5fa1203-293d-3cad-b535-13362063a188 | -11.1369 | -53.93231 | 2025-12-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| eb78877a-3ce5-3444-9ab1-ffb5cae21f11 | -12.40068 | -54.88979 | 2025-12-02 00:52:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 74461288-31cd-3206-8e86-e272862bff2a | -12.52297 | -56.91267 | 2025-12-02 00:52:00 | TERRA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |


[Clique aqui para ver as próximas entradas](README3.md)
