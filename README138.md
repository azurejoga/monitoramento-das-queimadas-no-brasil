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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d720b96-98c3-39ea-bbd8-26a80cc0dbde | -22.58759 | -46.78646 | 2025-10-01 05:14:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| e2fbf016-c8e8-3c5b-b4e3-cda4a85cb39c | -22.5746 | -51.11666 | 2025-10-01 05:14:00 | NOAA-20 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 727961d5-3cb2-3e53-befa-e6098a692da6 | -22.4385 | -48.31922 | 2025-10-01 05:14:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efc2b5ea-977b-3533-8965-2b42a2db7389 | -22.27283 | -46.72535 | 2025-10-01 05:14:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cf8a0442-73a3-3cd0-9d6e-2826b20da7d6 | -22.58312 | -46.77671 | 2025-10-01 05:14:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| a8b70603-053f-3ecb-9990-108c58b2ec2c | -23.06428 | -47.03223 | 2025-10-01 05:14:00 | NOAA-20 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 93e49b4c-78f4-3f3f-8d67-8603c5ec899f | -22.58263 | -46.7835 | 2025-10-01 05:14:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 8eb0737e-eb31-3d24-9ab0-c4445eb442f6 | -20.59947 | -45.88996 | 2025-10-01 05:14:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 638bb516-f5b6-3d83-afeb-5e1405dea102 | -22.27321 | -46.71967 | 2025-10-01 05:14:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a1a2cf9b-cc8c-3b99-80d6-b3f5286e9971 | -22.26625 | -46.71822 | 2025-10-01 05:14:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e4e0e1fa-b10b-35d5-b157-7229040fcce3 | -22.58803 | -46.77978 | 2025-10-01 05:14:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| c5436268-312d-3971-aabc-b16aff33cc8e | -9.78529 | -68.24085 | 2025-10-01 06:01:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0282ce89-f622-3f3f-ab00-5a56b925e69c | -6.9526 | -63.10189 | 2025-10-01 06:01:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57ea5c3c-8047-3ed3-b6c2-2b6c0fa846c6 | -7.87216 | -71.71584 | 2025-10-01 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fafaff5-550d-36f6-b59a-c5dce5295197 | -9.47463 | -67.89259 | 2025-10-01 06:01:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39eeb13e-a43a-3581-9b0d-6ca368e1ca59 | -7.80006 | -72.28413 | 2025-10-01 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c16328b8-bac6-3b4b-a9c0-bdeeea8bdb5b | -9.52816 | -68.29311 | 2025-10-01 06:01:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78734adf-9c77-3762-a0dd-6b9c2a3f5636 | -7.76432 | -70.74023 | 2025-10-01 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2e681db-d0e1-330f-a923-d1ef50b8be08 | -7.80286 | -72.28835 | 2025-10-01 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f163bbc-d2b6-36e9-bd14-56b9a0348d8d | -9.47522 | -67.88851 | 2025-10-01 06:01:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2878e869-4869-30cd-866d-0ca69f4b7038 | -7.80346 | -72.28466 | 2025-10-01 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d9a0e44-9f02-3b47-b288-fc8a4cfbc235 | -7.79946 | -72.28781 | 2025-10-01 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b817b706-0cc1-335a-a9c0-95aea73d5a25 | -7.86882 | -71.71531 | 2025-10-01 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b361956-6a2a-3277-92d7-67bfa76efd9b | -7.33591 | -72.87196 | 2025-10-01 06:01:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2259a313-4b48-3308-974e-5123d8e88630 | -9.47203 | -67.89151 | 2025-10-01 06:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fb9e5d99-2ff3-3ee2-a42f-259cfc34fd1b | -7.76381 | -70.74103 | 2025-10-01 06:29:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 086e713a-cc46-309d-8989-24872a02a03b | -9.47741 | -67.8923 | 2025-10-01 06:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efe87208-69e0-3271-be9d-b81508579ae1 | -18.2379 | -53.293 | 2025-10-01 06:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 83.3 |
| bb9691ae-00db-3bc1-aa6a-e356242b08f4 | -18.2375 | -53.3145 | 2025-10-01 06:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 5339a5b0-83f5-344f-acd4-8c896c3a28a4 | -18.2176 | -53.3177 | 2025-10-01 06:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 71.9 |
| eac360a6-2ab2-3ee0-bb90-d84b67239bd2 | -18.2379 | -53.293 | 2025-10-01 06:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 5c970a97-0048-33f3-be6b-1c9bfd578654 | -18.2375 | -53.3145 | 2025-10-01 06:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 848f84b5-0de3-3aa2-8232-1367998c87b2 | -18.2375 | -53.3145 | 2025-10-01 06:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 0999578c-ac60-3eca-b0a9-bedb5484f874 | -18.2379 | -53.293 | 2025-10-01 06:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 98.4 |
| a99614d6-3097-36f7-90a2-3ff2a05d4a07 | -4.40401 | -50.83783 | 2025-10-01 06:54:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 8f749fb9-b682-3641-b563-f4c39f5bac43 | -4.39671 | -50.83268 | 2025-10-01 06:54:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 23efb2f7-d98d-37a9-baf4-ddc3e75474bd | -18.24116 | -53.30245 | 2025-10-01 06:57:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 78.7 |
| fbf5bb74-66ab-3c4d-8e04-09d6a9b74d20 | -18.23521 | -53.29763 | 2025-10-01 06:57:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 122.0 |
| b29f1acb-2d8f-39af-81e3-e750a6f0ef07 | -18.2375 | -53.3145 | 2025-10-01 07:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 0ce16c0d-780e-3020-8ee8-696a41ecaa48 | -15.181 | -49.0788 | 2025-10-01 07:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 5a3d9ccf-9e96-3816-9e75-6c49dbf78f8b | -18.2375 | -53.3145 | 2025-10-01 07:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d04ef10c-4b50-3e14-ae9f-c41bd9962142 | -15.1615 | -49.082 | 2025-10-01 07:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 9946fa0d-a923-341c-800d-35ca1fcb6033 | -14.9181 | -51.6657 | 2025-10-01 07:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| fea0cb18-1e22-3e23-8725-4e6901d34f87 | -15.181 | -49.0788 | 2025-10-01 07:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 37.0 |
| bebb9ccc-5015-3748-bb85-33be5c9f93ae | -14.9177 | -51.6872 | 2025-10-01 07:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| eb7fdbb0-ebf4-3b44-be24-4c2ac6e627e0 | -14.0332 | -46.3194 | 2025-10-01 07:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 220.6 |
| a13c1a99-d243-3247-9fe8-b0bf673583b4 | -14.8016 | -45.8178 | 2025-10-01 07:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b5a70787-50b0-3667-9ab4-1580ad9e1c48 | -14.3519 | -45.9206 | 2025-10-01 07:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c2e6b25b-d840-3127-80b4-6118833a90b4 | -14.8021 | -45.7946 | 2025-10-01 07:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| bce62c8e-4fca-3626-a63d-7b1050150e51 | -14.0327 | -46.3423 | 2025-10-01 07:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 46c4245b-747f-3c3a-8126-ee7c598e5d0f | -14.3519 | -45.9206 | 2025-10-01 08:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 5299a8f6-c3c2-3e81-a68f-8211ec99b45a | -14.8016 | -45.8178 | 2025-10-01 08:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a8cf00ee-122b-3fa2-b2f6-f57e3bb2eb9a | -14.0332 | -46.3194 | 2025-10-01 08:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 0c111723-e84c-3450-af7b-9ea4ccbf8243 | -14.3514 | -45.9437 | 2025-10-01 08:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8bf0a485-2114-3cef-b3d9-32c7275eeafe | -14.8021 | -45.7946 | 2025-10-01 08:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 2828adca-f1ce-3b1a-9b56-945185858fab | -21.341 | -51.5527 | 2025-10-01 08:00:00 | GOES-19 | TUPI PAULISTA | SÃO PAULO | Brasil | 3555109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| 9334b3f9-11e2-31b3-a97d-66f95162ac4f | -14.3714 | -45.9172 | 2025-10-01 08:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c013857f-65ae-3deb-8833-10ca5b1271f6 | -14.3519 | -45.9206 | 2025-10-01 08:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 54e14666-cd73-3f12-aea7-62159ec40861 | -14.0332 | -46.3194 | 2025-10-01 08:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 58600a0d-c73b-35bd-a8f9-b19c219fee52 | -15.181 | -49.0788 | 2025-10-01 08:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| eeb5bb14-c2e3-382e-9373-ab9a87cab2c6 | -18.2375 | -53.3145 | 2025-10-01 08:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a6b3010d-14f7-359a-b02e-7aab8687674d | -14.4943 | -48.4553 | 2025-10-01 09:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 124.6 |
| cfc6bcfe-1d14-3df4-be00-5320f4f999bc | -14.8016 | -45.8178 | 2025-10-01 09:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| e2341ba6-7bec-3710-bf95-3bc6b6f10d32 | -14.0597 | -45.0444 | 2025-10-01 09:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 1f5db9c9-63df-3207-9a9c-a1fb81c4f0d8 | -14.4943 | -48.4553 | 2025-10-01 10:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 7549252d-fc3f-3e95-9416-6294bce477fa | -14.8016 | -45.8178 | 2025-10-01 10:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 286eb674-1d43-3c4a-aa6e-38adc7eeb2a9 | -14.8016 | -45.8178 | 2025-10-01 10:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 3089ce4a-32df-37be-bfbd-de1e8336a34e | -14.8212 | -45.8143 | 2025-10-01 10:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 33cda8c8-0a4a-384b-8672-0d54e13dea31 | -14.8021 | -45.7946 | 2025-10-01 10:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 7059dc8a-b86e-3653-a3b8-f64e283679b5 | -14.4943 | -48.4553 | 2025-10-01 10:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 6300561d-75e7-3794-886a-bfefbf79155a | -14.4943 | -48.4553 | 2025-10-01 10:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 2d4d9a14-3cbc-3fb2-9b2c-9356e0a7e666 | -14.8021 | -45.7946 | 2025-10-01 10:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| a3007d73-723e-317e-8c62-9c3f95b8cd3f | -14.8016 | -45.8178 | 2025-10-01 10:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 80e1c4ab-251b-3409-85a5-af5db2e59719 | -14.3714 | -45.9172 | 2025-10-01 10:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 986d35c1-fd45-389d-848a-8987d3db9d2e | -14.8212 | -45.8143 | 2025-10-01 10:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| dc8f318f-f4e6-3a8f-bd34-4f2d61199707 | -14.8016 | -45.8178 | 2025-10-01 10:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 0eb35017-7f58-39a2-9f3a-57254677ab36 | -14.4943 | -48.4553 | 2025-10-01 10:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 01e36aaf-9557-3f78-a6dd-37edeade21e2 | -14.8212 | -45.8143 | 2025-10-01 10:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 1b2cffe4-7cb3-368f-926c-aa96b535dbf3 | -14.8016 | -45.8178 | 2025-10-01 10:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 13401d77-785a-3a49-a35d-fe49996b9266 | -11.8482 | -48.0595 | 2025-10-01 10:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| f10bded2-9ce5-321f-a385-4d2ac274f19e | -14.8016 | -45.8178 | 2025-10-01 10:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| c59bcd94-4125-3cf9-80cd-fd35358f0495 | -14.4943 | -48.4553 | 2025-10-01 10:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 724d2b38-438c-3251-a4ac-71d5c22c73ea | -14.8021 | -45.7946 | 2025-10-01 10:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| b9714dfb-55b2-36ed-9088-8b0702d92336 | -14.8212 | -45.8143 | 2025-10-01 10:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| f244b967-89af-38de-8352-865854a047e3 | -14.3514 | -45.9437 | 2025-10-01 10:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 75be24e1-66fe-3386-b36b-aba20e5d0005 | -14.9738 | -46.8668 | 2025-10-01 10:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| a3c897ac-25e4-30ae-bfe1-e5a13f943448 | -12.0242 | -42.5051 | 2025-10-01 10:50:00 | GOES-19 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 166.6 |
| d9c99549-09f8-3da9-8313-aa4105b9dafa | -14.9733 | -46.8896 | 2025-10-01 10:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 356fd689-8eda-363a-bde4-baf8e14456a9 | -14.8016 | -45.8178 | 2025-10-01 11:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 246.2 |
| dc8908c9-41e2-3f5a-b232-375811f9b0e3 | -14.9733 | -46.8896 | 2025-10-01 11:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 83ea3783-86fd-3141-8e47-e8c020e0ca03 | -14.3519 | -45.9206 | 2025-10-01 11:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 3b8f5ede-e829-3545-99da-de21741d4fed | -14.4943 | -48.4553 | 2025-10-01 11:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 483161f3-d99f-3e04-ac48-8607be0f8429 | -14.8021 | -45.7946 | 2025-10-01 11:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 256.8 |
| 598335a8-5582-3f86-84b5-34ffcf607ab2 | -11.8482 | -48.0595 | 2025-10-01 11:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| caa06131-be10-3b5d-a0ef-733015f8218c | -8.8926 | -46.6296 | 2025-10-01 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| f4d23c40-362c-305a-9660-ecdd15b2cc4b | -14.5137 | -48.4522 | 2025-10-01 11:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| aa74e414-5db5-39a7-9da7-f64d694c9b44 | -8.8929 | -46.6072 | 2025-10-01 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 5859fe46-5f34-39e1-b662-1b8ddda54928 | -14.9733 | -46.8896 | 2025-10-01 11:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 0e6c18bc-3411-3659-bf55-42443a8dd1c9 | -14.8021 | -45.7946 | 2025-10-01 11:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 6996a0be-197a-3478-92f8-5278f21276b5 | -11.8482 | -48.0595 | 2025-10-01 11:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |


[Clique aqui para ver as próximas entradas](README139.md)
