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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d969e16d-3a01-3737-999b-5427d610dbb9 | -11.1976 | -54.000999 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c21503c5-0676-38b6-a52f-6369a8645d4c | -6.9541 | -58.998699 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37319dd2-f700-3514-b913-a80a9da377ba | -6.8853 | -56.617298 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ceb259c-086f-3658-8299-d73851b74c91 | -10.8125 | -50.2696 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c588139c-e4ed-3159-a8ad-a91349f4207c | -14.3567 | -51.846199 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65ae9ad1-25c5-39b0-a2ab-9b952aa8bb54 | -5.595 | -43.990799 | 2026-08-21 00:14:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d5258e5-a7c4-3547-a40d-6dff9dce8083 | -6.6728 | -52.883202 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 233fdd80-b955-377d-a691-ca30f4403ec1 | -10.7187 | -44.775398 | 2026-08-21 00:14:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 679c34cd-639d-36b2-bcce-aea2778e9efb | -4.1158 | -48.928799 | 2026-08-21 00:14:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31a0e24a-07c6-377d-8a2e-ddeb2f719769 | -6.4256 | -54.926201 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 905aecc7-7b8b-3153-a311-e09a1ea603bc | -7.4675 | -49.6996 | 2026-08-21 00:14:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e57248b3-aa96-3603-bbda-c322ae452f5c | -6.3766 | -54.936798 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97c2f7af-75ac-3853-aec8-998de8883a5e | -6.9042 | -55.709999 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3d34187-e23b-3b90-9ec7-90b83223df93 | -4.4738 | -55.385799 | 2026-08-21 00:14:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa038081-94bb-3eb6-a713-f176fd79525d | -4.4627 | -54.826599 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62ff42f2-b9ce-34fa-9683-d8dda0af36ea | -5.7911 | -51.660702 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed944dc-62ee-36ed-aed2-0194320d9c7f | -8.5553 | -54.7696 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 756cc937-cdfa-37dd-95a8-b80c2edaa7c9 | -11.9227 | -50.1688 | 2026-08-21 00:14:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efc9b28e-8c7c-3bee-9770-70fb6485cb10 | -9.0519 | -57.059399 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45c19379-2302-323f-9132-f219c3331ccc | -6.2257 | -55.6063 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac2c0c0d-f86d-3faa-92d9-add7988de4e5 | -7.3703 | -45.809601 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42bbe621-e45d-3735-985a-4870d924cb0f | -16.309 | -53.159199 | 2026-08-21 00:14:00 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9a3df05-a970-3ccf-99f8-99b059ae6b98 | -13.5982 | -51.802299 | 2026-08-21 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c82f597-d320-3143-a1a0-7a8cf43be805 | -15.0009 | -52.664799 | 2026-08-21 00:14:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| db3856cb-f7e4-3f6a-a70a-1ae5e6e3f6c7 | -7.3617 | -55.504902 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96d12509-8f22-315a-aa2a-1caac144b7b8 | -11.3602 | -47.230202 | 2026-08-21 00:14:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 052b65c5-ccaf-387c-abaa-2e92aaa554a8 | -4.9202 | -56.245899 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99a46e90-5679-3e81-b766-368344f546fc | -18.0441 | -44.409698 | 2026-08-21 00:14:00 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c56122b3-16fc-3bf3-87e0-9373d13ad539 | -18.2055 | -50.7481 | 2026-08-21 00:14:00 | METOP-B | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3bd3b80a-4554-3628-939e-a92ec39ae1c5 | -11.0 | -45.209 | 2026-08-21 00:14:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90f70f48-dc5a-3b47-ad3d-a1553212d47e | -8.6546 | -54.612301 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85ac9f97-d10a-3038-89c0-fae813df55a1 | -12.6634 | -47.7701 | 2026-08-21 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1de85ff3-95d6-3d41-9a1f-22f25409bca4 | -14.5649 | -52.9786 | 2026-08-21 00:14:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29b677c7-2309-3639-9b08-561ad6452823 | -2.7563 | -48.569698 | 2026-08-21 00:14:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e5b4d0a-b79a-356a-b11c-5d9513e6c66b | -18.0273 | -46.459801 | 2026-08-21 00:14:00 | METOP-B | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0b5508c8-c1a2-30b0-a6a1-f492b4a83d20 | -10.1707 | -54.276402 | 2026-08-21 00:14:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eaede74d-8150-3ba8-b4e2-1e7e0c49029d | -6.7013 | -58.909599 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c60c5e15-a1d7-3152-ae9f-7fa5cd4da6a1 | -8.6028 | -54.7048 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08bb88c8-01b1-3277-bc29-3827c32e018e | -5.8718 | -57.653702 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3dc2b92-1aba-3947-abef-9825c45798b7 | -8.4467 | -46.9529 | 2026-08-21 00:14:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3f06d5d-5513-3990-b7d9-efa73111a358 | -10.8027 | -50.2719 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41094041-1abc-34b7-ab0f-707865b3986e | -4.9391 | -55.772301 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3461170d-3e2c-3d5f-adf5-cd9d32fa765c | -8.5561 | -55.297199 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a8369a5-1894-3588-920c-7217736f0d99 | -15.7131 | -47.792599 | 2026-08-21 00:14:00 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| e90a8ec8-0a36-39a4-bb57-1bdefc04715b | -6.8818 | -56.410999 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 657c4840-b9dd-3edb-a9bd-e09cc2ba93dc | -6.6086 | -58.3773 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2eb51066-6e6d-3cb0-b54f-c78e9d58765d | -11.3679 | -47.219299 | 2026-08-21 00:14:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dda5f80d-5e5d-3d4c-bf6f-56132de54672 | -4.0461 | -50.285198 | 2026-08-21 00:14:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c82d9f4-cf58-3675-af1a-0ac21f2c8395 | -4.0832 | -42.485199 | 2026-08-21 00:14:00 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| da5783ec-eb30-3d9a-a49b-2f98536ab63d | -10.5289 | -50.7952 | 2026-08-21 00:14:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 17884937-7990-3d50-9a5c-df43ee340f73 | -10.7452 | -50.336399 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7585fee-a6d5-3513-81a4-69f26233f42b | -9.4495 | -51.630798 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c2300c6-47b6-3d3d-8c4e-1295698a300f | -11.3865 | -50.717098 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64bfe660-4fbb-38f5-ab41-116396a3052a | -6.3334 | -46.5163 | 2026-08-21 00:14:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4ddb916-7e2d-3542-a78e-bef4ebe3c566 | -12.5064 | -47.8494 | 2026-08-21 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f23a2e40-a0ea-38ba-90d6-5bc6c8315c0c | -6.9477 | -52.777699 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24262875-e7ec-343f-9130-b23470094bb0 | -9.9991 | -48.559799 | 2026-08-21 00:14:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70f66a7f-3d2c-334d-9029-977d05952447 | -8.6005 | -54.7416 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68b24f94-7f71-3954-bdb1-1169dd75c79e | -3.2628 | -49.5191 | 2026-08-21 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4925056-8da2-3425-86b4-522d3a890a3a | -12.008 | -53.429001 | 2026-08-21 00:14:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1788286d-4bbe-3d4b-bae7-30bcf08713bf | -9.4073 | -60.385899 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c71ea40c-4deb-31b5-9e13-9f4e7e7e198d | -6.4393 | -52.712799 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83d6bf90-a19f-3cb9-bc47-9f85d8a40c9b | -3.8434 | -59.3606 | 2026-08-21 00:14:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 150c9cac-bad6-35ff-ba6f-58c858781903 | -12.8403 | -48.445301 | 2026-08-21 00:14:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0db1fa1d-78a2-339b-afcf-af41b9ececdc | -9.4031 | -60.365101 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a49827bf-9982-39e6-b3d5-2a29b19c6435 | -12.8565 | -48.4258 | 2026-08-21 00:14:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 321cb36c-9ff4-31c8-8c4d-110706152b31 | -11.17 | -54.0159 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da7cb1fd-49b2-3021-bf59-92056e26daa0 | -11.4325 | -47.230701 | 2026-08-21 00:14:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96a552c4-d0f2-3eef-be53-65c28c24ae1f | -14.5782 | -52.993301 | 2026-08-21 00:14:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 796f52a4-fb10-3cf2-a3c3-dbed16a056a5 | -16.3232 | -49.449699 | 2026-08-21 00:14:00 | METOP-B | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d7a99f3b-5b48-3c55-841a-fb984a07025a | -6.3883 | -54.9431 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 064b84f5-2df9-3096-a276-31a4241d94dd | -12.0045 | -53.412498 | 2026-08-21 00:14:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f740d919-e627-3cf8-a1a5-3a9a9ce50e3a | -6.1168 | -53.0658 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5b4617-fd18-33a0-97e2-33f5930beaf8 | -12.7489 | -48.451401 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 741e4b4e-bf2b-321e-b28d-98fab3346f84 | -10.2698 | -50.283901 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfba6069-a630-34d7-82eb-0514d46ac51f | -10.9054 | -50.270302 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83c78ab6-a5c9-38df-ba8c-ac586eb4c5cb | -6.2299 | -55.3908 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fff6081-e91f-3f0c-af06-ba6957d48c6f | -8.5908 | -54.743801 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1339b559-a4a7-396d-be84-84ee0f707b17 | -6.1446 | -57.734299 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87a4c312-fa91-30e0-9cca-ada222f0979d | -8.0968 | -51.657001 | 2026-08-21 00:14:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 402d847a-ddd4-3b6f-8a9d-df1ed5a15e28 | -7.72 | -46.151501 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef999085-9156-3972-a70d-9d8dfe93a70b | -14.3436 | -51.880901 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbb438d1-5bca-3f81-aca2-b99ff7ecdee3 | -15.4976 | -53.889599 | 2026-08-21 00:14:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3d13eac-0ea5-3ad6-8f27-9b39583b6456 | -13.9804 | -49.424702 | 2026-08-21 00:14:00 | METOP-B | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10d719e7-6bdf-3064-b056-5befbb08ecc7 | -9.0652 | -50.879799 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e3e33e2-e402-3d1c-8a69-752b44c23986 | -9.4156 | -60.427601 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b001512-a8ee-3045-9895-7905f023b2a4 | -9.4128 | -60.363201 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77882b41-47a1-3404-ae62-d90a048c449b | -11.1682 | -54.007301 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 722e96a6-001a-376d-8d93-a3a7f284bddd | -6.0131 | -57.787701 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57d800ea-1878-3a5d-99d0-7d29182f299a | -6.8877 | -59.407101 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed535fa7-8179-3fdf-b6a0-23b613c41da8 | -10.755 | -50.334202 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c149c2d8-d851-35e2-bbc1-2284383b6808 | -9.0734 | -50.870602 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 647424a7-7e05-3791-8580-d9c982d6314e | -9.4547 | -51.607601 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7b2bc68-104e-3447-8428-e0acc714594c | -4.9489 | -55.770199 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed59bd7-738b-3938-9e37-3f6658834f58 | -3.9728 | -47.2029 | 2026-08-21 00:14:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed70cba9-0398-359c-aa08-129f62ce0366 | -12.2493 | -43.164101 | 2026-08-21 00:14:00 | METOP-B | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aac223e3-731d-3f8b-9c2f-9c80ea435f60 | -7.348 | -45.8027 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15ca6290-c3e7-32fc-b53c-fa06ef20219a | -12.259 | -43.161598 | 2026-08-21 00:14:00 | METOP-B | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ead1c864-6954-3323-99fa-91b01a8dab61 | -3.5429 | -48.187199 | 2026-08-21 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27bc31a1-6d73-3fde-a0b2-b68f34fdca53 | -6.4692 | -43.5317 | 2026-08-21 00:14:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
