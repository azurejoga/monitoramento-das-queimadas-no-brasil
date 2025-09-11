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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c137671-a5db-3b4e-b75b-cacdaea7e0d2 | -5.28517 | -44.19909 | 2025-09-11 04:44:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cca3cfcc-1e12-3706-bb26-1460dfdae6df | -7.47857 | -45.29171 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8dc02f8-27ff-38e9-9455-87981737326c | -8.50803 | -45.66019 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eaf34b61-b06a-3904-8461-beb178717046 | -1.86236 | -47.98947 | 2025-09-11 04:44:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e9fde8e-a37f-3315-83ea-cdd715f05892 | -6.31261 | -43.40759 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e32d7cf7-8747-38b6-9e2c-05b87ca37cbc | -7.85683 | -48.15705 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c087323e-e0b2-366f-845b-501aedc29445 | -5.89547 | -45.80486 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54a6d9dc-b709-3a6c-9cf9-f6ae373b7d8f | -7.37317 | -47.4185 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0008bb7d-ad9e-324a-b233-688339cbe030 | -8.51085 | -45.70068 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ce785c5-a2c4-3367-b117-ae144d807017 | -8.53488 | -45.56472 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d5dbe9d-16fb-36bb-898e-4b256354d3e0 | -6.19857 | -42.48872 | 2025-09-11 04:44:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7e3da967-5462-30e5-8fe0-94f0b018c3e0 | -4.8729 | -42.7691 | 2025-09-11 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| db49f098-1dbd-3643-b087-64a7488f6fb3 | -6.90763 | -47.90454 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f82d20bf-96bf-328a-a932-9fd663631825 | -5.46753 | -43.43945 | 2025-09-11 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab15253c-e549-3557-98b7-341a8b6a3782 | -7.37183 | -47.42749 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d261fb85-d4e5-3460-bf63-ac38fc4642cd | -8.65379 | -45.7242 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 35598f24-19dd-32bb-b4df-e2393d7adcf1 | -7.87587 | -46.72956 | 2025-09-11 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e48fb4cd-d19a-3e38-b1e5-35b7de939ee1 | -6.48963 | -44.49225 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4686588-9a36-3fa9-90e3-acb2f7c310c9 | -5.92023 | -53.83467 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29c8fbdc-7600-34ab-a10c-b81c88a21759 | -7.77463 | -50.77973 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cf997f2-a384-3654-97b8-99ef7ba73e61 | -8.04656 | -52.39132 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3766ccd2-9ee4-33c1-940a-ce5de16b3802 | -7.10748 | -47.84483 | 2025-09-11 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8d795e6-91af-3366-bb0c-c06d5ac17f7c | -7.4933 | -48.25613 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b429aec6-1a6e-38c0-9fd7-1b90da7f2ebc | -6.3227 | -53.45387 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b0e46ee-3e66-3fe5-9873-8bb9b0db90f2 | -9.06785 | -45.6988 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69c49138-c74f-3466-bd1b-031f9b4c9eca | -8.03464 | -48.66375 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60b04095-29bc-30e8-9afe-c0554583f27a | -4.86307 | -42.76764 | 2025-09-11 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47f0ce67-65d6-37f3-ad33-49b90dfd0951 | -3.89262 | -42.55119 | 2025-09-11 04:44:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ff2c7de6-f212-3ac6-823b-de67758006d9 | -7.20161 | -44.97252 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5cfab8c7-d07a-388f-9dd5-2c6147d2f5ed | -5.73082 | -45.28911 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77877fa6-7a37-332e-8d1a-9d533c37308b | -5.5385 | -46.42257 | 2025-09-11 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7990f336-c136-3c23-a25b-292d5956f06e | -7.76532 | -50.77443 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7a3c8f5-7d48-3ebc-b073-6be4d1a77bf6 | -8.5162 | -45.69366 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4550e740-4fc5-3f15-a0b4-075da9106ac4 | -2.22087 | -48.22879 | 2025-09-11 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 322f91fd-37a7-3796-97df-5580d93850dc | -7.77196 | -50.77548 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb8ed1e4-65dd-32f2-9869-c7f0c50ec3d3 | -7.48306 | -54.95078 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4929b47-0829-3cb5-a09a-c70a268c19ae | -7.50514 | -48.27464 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b525819-1a98-3e2b-8be3-b5cb88ab7298 | -5.50434 | -49.21186 | 2025-09-11 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86570691-a69d-3d23-8e66-32ed596eea31 | -3.07717 | -49.46754 | 2025-09-11 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f4dd008-bfac-3542-b1f1-861992c7e146 | -6.25731 | -43.41899 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06e0ceac-513f-3b1e-9f36-24f814836442 | -9.08382 | -47.09298 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d77bd666-330a-3e38-b59e-dc6ccd923663 | -6.55256 | -47.50907 | 2025-09-11 04:44:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cdc800a-34aa-3db4-b31d-0660876ff342 | -9.04988 | -45.73273 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c25e7a8-ed32-3121-acde-efaf8976a27d | -6.17283 | -41.07225 | 2025-09-11 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 092f1e05-d0cc-386d-878d-be7f545e582d | -7.7145 | -44.80386 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bfa83059-179d-38e9-b73a-bd3f46acbc88 | -5.78665 | -42.68286 | 2025-09-11 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| afd84a53-9cfb-3e2d-87fb-1bb6198588e2 | -8.03817 | -48.66433 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e159315-7d0c-3f77-8282-a9e87e4e8d0b | -7.18413 | -44.96992 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef40f1ad-82c4-303e-ada8-b4af309738ac | -7.65831 | -49.84705 | 2025-09-11 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97b8248a-6746-347c-acea-2cbda19f9a85 | -5.35953 | -45.22565 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc63de6d-378d-3bc9-9408-666b1e1ff880 | -6.65168 | -53.19508 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f750845-f680-3e62-8f7f-7ab7ff8e2560 | -6.63318 | -44.07867 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 330bed4a-6143-300c-aea6-fb699614e4dc | -4.41219 | -48.96085 | 2025-09-11 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aba8d63c-eac9-36fc-97c2-71be0eddf523 | -7.83396 | -47.2575 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1471ebb1-62fb-3d4e-811c-f7be7a6315fe | -5.23604 | -45.4572 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01c63320-12c9-34c8-98fb-ddb67152083d | -8.20288 | -50.10421 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 08eff4af-e507-327a-a9a8-e1202a37bd00 | -7.77795 | -50.78026 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f2f5e19-501c-3c84-822a-efec433d5abb | -6.27418 | -53.42206 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f943aa89-b308-3849-ae42-2a1ee9591057 | -5.87251 | -43.9999 | 2025-09-11 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 802185cd-6dcc-318f-9d50-94fe530bf447 | -5.33935 | -44.80733 | 2025-09-11 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 124a2d25-b30f-32d9-830a-a5f65435c846 | -7.44954 | -44.96573 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41af1a7f-81a2-372c-9343-6438ff619b5a | -6.40384 | -42.61277 | 2025-09-11 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c3ee1ac3-ec45-3393-83ce-df3311c4cc92 | -7.50048 | -48.25719 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc3dd74c-1d15-3f83-85ce-738cab5a72d1 | -4.86565 | -42.7643 | 2025-09-11 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bcc569c-49a7-3140-8eab-24a280b3bd18 | -8.11369 | -49.25617 | 2025-09-11 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dc531c1-9ccc-3edc-8a99-4c3bd69b2b11 | -7.44919 | -44.96841 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d328dcfd-71fb-3b76-9b5c-ffffc8708e3e | -5.93722 | -45.69342 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ebd74d9-67ec-376d-8f5e-6639ebee46ad | -9.06713 | -47.07074 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f37a104-8ed5-3895-bb6e-107973bce3f9 | -8.04001 | -48.15265 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1efd4270-9bb4-3a1e-99c8-ba69938a7a92 | -4.36284 | -55.28824 | 2025-09-11 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c520c276-35a7-3139-aefa-8bee40a4db9b | -5.88724 | -52.10477 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73d6ba8c-e16b-35be-8699-8e3a5453f130 | -6.32176 | -43.44661 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3c206570-0290-3222-a6d7-ee2c8dfdd4d7 | -9.06318 | -47.07043 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 735dcf86-a58b-33c2-ae57-03b1a80fe625 | -8.03579 | -48.65613 | 2025-09-11 04:44:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b91e9f3e-1af6-3120-ab07-d21d0aa8db4f | -5.76609 | -45.52551 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a59aab95-9376-3317-ba9c-60d6d719b22c | -9.05744 | -47.05505 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1cc0f2d-0162-3db8-af7d-5d08bb4bb818 | -8.08199 | -52.35681 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6789f3a-ff98-3905-a8fd-63102ea5f20b | -8.05004 | -52.32646 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f4e34a3-3ff7-302f-8dd4-a9a0dda9626c | -5.42703 | -45.88016 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24f34636-dc84-3c7e-bb6b-3a15e3d5d89f | -9.06785 | -47.06588 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 336534d4-b36c-3f8b-b1b7-70c1d4bae0bd | -5.28069 | -44.19845 | 2025-09-11 04:44:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcb7bc44-8b6d-3307-873b-801bd84941f8 | -6.19731 | -43.49625 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 22c70df3-1623-3787-8780-d60917963c08 | -7.83465 | -47.25284 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb44f531-e06e-3279-a00f-33c37c080833 | -6.5403 | -55.30024 | 2025-09-11 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ef96dfd-a11f-3383-9e1c-cac108c0ae18 | -5.20156 | -45.72076 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efe9e489-2a4e-334f-9078-a848c7b35916 | -8.08533 | -52.35734 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bd4b93d-d998-39e1-b8cf-334b3c72c92c | -7.88306 | -46.04713 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ec975a6-0cf0-3200-bc37-36bfa695e426 | -6.25883 | -43.40857 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04be75a2-ae30-30a0-a7b8-15cf80345cce | -9.15507 | -46.0551 | 2025-09-11 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebccca98-c610-3a6c-8dc3-1de51b557575 | -7.75174 | -50.90431 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 363c11a9-28df-3092-86cb-24acfb4e2c05 | -7.0819 | -43.87664 | 2025-09-11 04:44:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1311edfe-8dc6-3e6d-b6a1-1c9461ef16bc | -1.95508 | -48.11381 | 2025-09-11 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 030ddbfc-1846-3d3f-8092-f2a675b1a299 | -6.37062 | -45.16372 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62d18ee4-a2cf-3fe3-8506-dbd1b0460ab4 | -7.16138 | -48.88997 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d461fad-8889-3ab3-8364-383ed75529f8 | -8.06878 | -50.17893 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cf009faf-a8cb-3004-b336-7938ef9b3855 | -4.90043 | -49.92299 | 2025-09-11 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8fe56cd8-4a96-371b-b8b7-f5807502e6b7 | -9.07968 | -47.06698 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3885536-8aaa-3c96-a3be-6f1b894e9c86 | -5.60272 | -48.11308 | 2025-09-11 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07ef8914-d37d-395a-8ed6-cb30fb9a5c93 | -8.03933 | -49.04498 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 64843fa5-def3-3ec7-8514-5d96a7d04684 | -6.61845 | -43.99036 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README85.md)
