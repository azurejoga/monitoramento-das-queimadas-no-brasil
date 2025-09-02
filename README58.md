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
| 0a125ceb-a6d6-35e2-aca8-cf3438942b7b | -9.11174 | -46.05202 | 2025-09-02 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 419df0c6-83a2-3afc-be91-17013fb3628e | -6.85121 | -52.81805 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ce1f0c3-6b3e-3496-b0c9-c361d0ba1ad6 | -6.77985 | -52.81752 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7694254e-e8c2-36ad-a412-d9ce830a8237 | -6.83344 | -52.82981 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35b2aa10-0a38-3d9f-a2c8-0c21ca6b0dc5 | -6.43217 | -55.61995 | 2025-09-02 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e98230e2-b3eb-3629-8eb1-3cf077f778f3 | -8.708 | -50.44402 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d505f32-0afe-334f-b943-06311af82e4f | -5.32146 | -55.9991 | 2025-09-02 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d8ac8c3-0631-3bbd-9070-c5e1ee941ebb | -4.2218 | -47.21034 | 2025-09-02 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a7ee725-0c78-31fe-9230-2859788255ba | -6.9607 | -44.35253 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 339c4e3f-189d-39d4-b92d-75bc1e897d6b | -5.74861 | -50.20815 | 2025-09-02 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0888506-b055-3f3a-8edd-dba2b0bf0a4f | -3.22998 | -47.12493 | 2025-09-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 641afe20-eb43-3b08-8bd1-d9377e5de0ee | -7.97969 | -46.47884 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f502c300-e50e-3783-83d2-69e36a7c3b48 | -6.85728 | -52.80187 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8040852b-d399-3065-bb0c-292de480f70e | -6.00696 | -57.85532 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58d5f160-b7bd-3e06-94c4-64d3513aa08a | -6.80041 | -52.80353 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 489b1a2d-566c-38fc-8ce2-7c41be508d18 | -6.3437 | -58.16702 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98d7d911-610c-3281-9869-fa571ec910d0 | -2.55452 | -47.71063 | 2025-09-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 889031f9-63a0-3984-acb1-7bdcfe87f54e | -6.82622 | -52.82871 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c671b853-3d47-3141-8986-480d981e9e91 | -2.89605 | -52.87609 | 2025-09-02 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d35063e9-316c-335b-b6df-3293b94a5ba2 | -9.23752 | -47.05112 | 2025-09-02 05:04:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c907af3a-b1b8-3ffa-85b3-daf85184b1ca | -6.77525 | -56.29731 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c0b8329-8648-3ded-b6ff-5389a53ab1f9 | -6.79493 | -52.81546 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e150f7e8-e972-3d06-873e-033555858c78 | -7.81505 | -52.14921 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02aeaccd-673e-388b-bbfe-6090827d658e | -7.11209 | -44.75654 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 644e8c9b-865d-3e40-8416-680d9d778afe | -3.22913 | -47.13058 | 2025-09-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 2179d930-f07b-3894-88dc-a1caf20805aa | -7.70873 | -50.31153 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43eb409d-c567-30d7-b410-0dbc83075506 | -6.84257 | -52.8184 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2ee8b31-b9a0-3c40-8a56-110d462ccd78 | -6.85339 | -52.82017 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 469dfbe6-c294-30bf-8bdc-ebd921672071 | -6.78469 | -52.80976 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd2d7c67-4b07-3b5d-9eb3-c418d2b449e4 | -7.56842 | -45.23242 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d36ec02c-484a-349d-839c-6d32d52c1697 | -6.30466 | -43.55609 | 2025-09-02 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f83562dc-01fe-30c8-9a27-ae19df014f36 | -6.83407 | -52.82564 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c8b98ba-b6fd-3419-893f-82dcca3c2350 | -6.19729 | -45.38768 | 2025-09-02 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 034cfac1-5d50-3348-b7eb-8b45afeb8948 | -7.69564 | -50.28071 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b9b589b5-9ff5-3a39-929b-04b2f1d0032d | -7.11232 | -44.75781 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a73c6c00-5fe6-3449-800c-fcf206c01aef | -3.40172 | -46.90453 | 2025-09-02 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 343b1e24-510b-3391-a684-f1da726d7a8f | -9.11756 | -46.05286 | 2025-09-02 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bad8d947-505d-3132-ab38-7e358e32c281 | -6.81961 | -52.8235 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb37c798-1d8d-31f4-9cac-9cdee2f26d88 | -8.85777 | -50.58434 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a457f214-92ef-39f0-ac83-d3fd80c0f581 | -4.30655 | -48.09362 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f402813e-c58c-31f8-a6f5-39f109a0db31 | -8.86141 | -45.79089 | 2025-09-02 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 836e0772-f1e5-3339-9292-e12fbcad4a25 | -4.31013 | -48.09298 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1a3742cf-6d02-3e4c-990b-63bcb309db46 | -7.49036 | -45.36319 | 2025-09-02 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44d334ec-8b0c-34b4-b3b7-73e67f26ff37 | -8.07079 | -49.71486 | 2025-09-02 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af523de4-88fe-3265-b736-6718b2828bd1 | -6.43886 | -55.64221 | 2025-09-02 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fddf58d7-7c7f-3f83-b2d1-c4a4bb48f006 | -6.80603 | -59.96426 | 2025-09-02 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86b704f0-4db1-3633-8d1f-df26c6a0adb1 | -2.58622 | -51.92421 | 2025-09-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e97383e1-8043-3058-ad67-5599ae65882f | -6.86148 | -52.79135 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5339627e-a3e6-3815-91a0-90fa5c6097eb | -6.9986 | -43.22526 | 2025-09-02 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| df61ba54-c030-305f-a08c-a7c520791154 | -6.83959 | -52.81364 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28c3c888-64ba-33dd-8e55-4a5104fee704 | -5.14971 | -60.37122 | 2025-09-02 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb0ea324-18f9-380b-bdd2-171f35b66adc | -7.55885 | -45.70333 | 2025-09-02 05:04:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed8eb496-7ef4-3727-bec4-e22f4a6031bb | -7.70968 | -45.02147 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 065742c3-d98a-3401-83d9-0e34dd355849 | -6.80577 | -52.81716 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1dacf62e-4ce6-354f-b2a3-c52a2fa74757 | -6.79368 | -52.82384 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f88555b3-abdf-331b-8222-0743503e608f | -5.7799 | -42.59197 | 2025-09-02 05:04:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c42f59f1-894b-3c18-9aed-92bc607e302b | -8.35952 | -52.52727 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12c7427e-72fa-3305-9ac7-0c7ae3a60333 | -7.63333 | -46.54925 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84754761-df77-3dab-a687-52d2b478e450 | -6.7922 | -44.62432 | 2025-09-02 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c60759d7-c295-3813-94ed-efe50b585657 | -5.15967 | -45.17258 | 2025-09-02 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 981a11fb-b96e-34a4-8275-f2d5b9341560 | -7.70708 | -50.26153 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5b0fc88d-2806-33a0-a44c-820cd114014b | -6.52701 | -56.20804 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0c7f722-5dd3-3af3-b857-75869da6f4ac | -6.79431 | -52.81965 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47ad470f-3688-3a33-8665-06b52aac4992 | -6.99372 | -43.23198 | 2025-09-02 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d5562f84-9bdf-3c59-a996-f149ceef9119 | -6.80091 | -52.82495 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5acbabb7-b7ef-38a4-a911-c66ba8ff6164 | -6.43878 | -55.62097 | 2025-09-02 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20acef92-c4a9-3105-98a9-b5f4d0e05119 | -12.61372 | -48.19186 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| aeb58485-2c96-3e25-b927-515ff22b0940 | -12.96709 | -48.09754 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 519708c0-0864-30b8-af7c-3a9fa2cbcded | -8.75022 | -62.42705 | 2025-09-02 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b753b836-0bf8-309d-9711-379e0b5160fa | -12.75026 | -44.41187 | 2025-09-02 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c83dfa91-d5c2-3003-bc96-9e3f546bb94e | -11.67193 | -52.208 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| fb5bcb3e-0771-3fae-a97f-7f59e2662e8b | -11.31267 | -55.21405 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5e947af-6302-3987-bdac-395c1c6375c9 | -11.6514 | -52.17988 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4f06f4b4-244e-39c4-83f9-af5f85714457 | -14.62285 | -48.94264 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3190be3-c5a2-36fd-8ec1-88b17f6bea8c | -14.6132 | -48.03831 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df4c6024-66b7-3101-8241-147af9d53faf | -11.0442 | -45.14845 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8f0df43-621f-3f94-89bd-fd723b85020c | -10.44612 | -54.777 | 2025-09-02 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 164bd7b0-c7ca-38b4-a418-f9bf83009317 | -12.80382 | -48.07112 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee76e73a-e8bb-3a93-b5fa-95f958790ab5 | -7.68057 | -61.09001 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| aedfff50-df5e-3b64-a213-f2941fc68aeb | -9.68286 | -56.73633 | 2025-09-02 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c704bd85-b101-3c34-b8e6-d7b4dde06764 | -13.72029 | -46.93112 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 632c68be-4f46-3d48-99ac-7679d1144b74 | -11.66094 | -52.19923 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a5bead5a-6820-3fd6-8d66-94d1c1abdc15 | -7.54266 | -61.33872 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0e67e5c6-fed6-35bd-af71-96eafa6a965c | -12.93128 | -56.99323 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1130213-3ba1-3ebb-b5fa-b44f198a65a2 | -9.25624 | -56.89607 | 2025-09-02 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6af9ccd6-0d7f-36e6-8111-6926891761bb | -13.27665 | -46.88971 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79b437a4-a93e-3dbd-a198-9a87e1e61f5a | -10.39726 | -47.12514 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7222ea97-0e79-3e54-9ce2-80e686379f2f | -8.70903 | -62.41183 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc7e0fbf-6268-370d-b18b-5c67d225832f | -9.34498 | -65.42007 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b1d5369-01ef-3e7b-85ef-e7d476840764 | -11.92066 | -50.62082 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6ca4729-d2eb-38a1-93cb-3bcd866baf39 | -13.69516 | -46.94392 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6f069cea-f722-315f-813b-72e2051674fb | -12.9413 | -48.08571 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d918203e-35a7-3b3c-a7a9-2613e8c07ba3 | -8.68777 | -62.40812 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a087ae6-7dcc-3c96-ae24-86d07c980d8e | -11.90265 | -46.67443 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1adb3471-f89c-343e-95b4-5ea1ed464591 | -12.93344 | -56.95737 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5684ca64-6dde-3ba8-8c11-881851d7880c | -11.09832 | -44.62257 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 48e88766-d555-3536-aa22-0f6334a279ed | -12.93122 | -56.94976 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| edd4d8e0-cd84-351e-8ac8-9c31d43c0179 | -14.48742 | -45.94363 | 2025-09-02 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0126e351-c4b3-30b9-9912-5c82a7e42b48 | -11.98025 | -45.88365 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 204861f5-f58d-3ba2-a245-508463aff229 | -15.12284 | -48.18253 | 2025-09-02 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README59.md)
