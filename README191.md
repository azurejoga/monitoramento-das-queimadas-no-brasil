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

## Dados Diários - Página 191

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62ee6912-475e-3e06-a9ee-3e4c038123d8 | -3.0637 | -43.1229 | 2026-08-31 19:00:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6b82be01-a847-3038-ad58-3b13f4eed726 | -10.1328 | -45.837 | 2026-08-31 19:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 7a80f22b-9f0e-3f25-9fea-87db3fe7c6e9 | -10.7405 | -54.0606 | 2026-08-31 19:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 2b3716aa-ad39-3b69-ad32-b3c53459ef78 | -10.1138 | -45.8394 | 2026-08-31 19:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 209.2 |
| bd1fe9f0-547f-3ec8-88d3-90709a829250 | -11.2103 | -45.1017 | 2026-08-31 19:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| a80b66ce-0aa1-38b4-b236-055fda0a4776 | -15.3434 | -52.8218 | 2026-08-31 19:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 261682d9-ce6c-3b04-a01b-a765002e7466 | -5.2548 | -55.8907 | 2026-08-31 19:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 08cf0de1-aac9-3da1-a010-7b86a537cfa2 | -13.5513 | -48.2435 | 2026-08-31 19:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 399623ce-d443-3c99-ab21-a9cf6750d094 | -9.1459 | -60.5266 | 2026-08-31 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 8d6038b7-d08f-3265-8fc7-9a5e237a5323 | -6.406 | -54.7637 | 2026-08-31 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 120b53e2-88d2-3cbc-a331-d85830cba2ee | -9.173 | -59.3659 | 2026-08-31 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 7736fa96-13bd-39df-9474-1b0e7df8a0d7 | -3.6215 | -60.566 | 2026-08-31 19:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 188.1 |
| f9cbe5be-ebd6-3369-b38a-ad1eeeb0efa8 | -10.1134 | -45.8621 | 2026-08-31 19:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 900.8 |
| 78306ea3-17c2-3d45-bb1e-1c5c623340c8 | -4.9787 | -55.8615 | 2026-08-31 19:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| abd56066-87c0-3ffd-be2c-2eae873aa0ea | -6.4055 | -49.9228 | 2026-08-31 19:00:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 9dff67d4-d122-3ddf-b794-c45e96668292 | -15.8649 | -56.4841 | 2026-08-31 19:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 05ebcc57-1f65-3310-8c0f-e44356ab77cb | -11.2478 | -45.1425 | 2026-08-31 19:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 18717bc1-b5bd-3b75-bc18-630fee7b0eea | -6.6233 | -58.383 | 2026-08-31 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 16773d2a-50d4-3247-9da1-6e953488b7c7 | -5.2362 | -55.9112 | 2026-08-31 19:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 4aaa1e90-ea72-3dc0-a882-58899369582d | -3.218 | -61.1796 | 2026-08-31 19:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e14bda1e-539b-32ef-85c0-282ddfce979f | -6.1109 | -57.684 | 2026-08-31 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 83df5f85-f374-3d0f-b72d-ad7f17769b49 | -8.5969 | -54.7755 | 2026-08-31 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| ef3b32ff-e4a0-3176-8948-77cf5f72d631 | -11.2286 | -45.1452 | 2026-08-31 19:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5ec72f66-14a4-3601-b6df-b23dc8f69774 | -6.7813 | -59.7864 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 771f4bf6-0679-36ef-9ca5-35b57b607465 | -14.1263 | -52.8106 | 2026-08-31 19:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| da9557f0-e77a-367e-8634-2572702a67f2 | -10.1324 | -45.8598 | 2026-08-31 19:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 471.1 |
| fe5f2c6b-4a35-37a4-91ca-5b1d4588fa74 | -6.8009 | -59.5742 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 9fbf9ff7-3eb1-3915-ab73-a9670df406f3 | -9.8434 | -64.9777 | 2026-08-31 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8d6e9303-8491-391a-8c81-b086374cc508 | -8.8207 | -71.243 | 2026-08-31 19:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a82f2e90-379f-3b68-b351-f1e2f6cb254c | -15.8844 | -56.4819 | 2026-08-31 19:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 771ff122-f6e6-33e3-b6e0-15478511f4b7 | -3.1083 | -61.2191 | 2026-08-31 19:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 0c98595d-3ea1-3622-aaef-e287d5af2640 | -8.9481 | -62.3704 | 2026-08-31 19:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 46434075-7c0b-3a89-b15d-70847f5845f8 | -4.2275 | -59.8671 | 2026-08-31 19:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 63ee0851-259a-37fe-b2d5-239298894b54 | -9.4149 | -45.6953 | 2026-08-31 19:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 509ea865-bf58-3ff3-adcc-79c8d98b8fa1 | -7.7941 | -44.0609 | 2026-08-31 19:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 57a881ce-51bd-31fc-aab4-70da2abd8b74 | -11.1807 | -55.1024 | 2026-08-31 19:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c45694b0-94f2-3535-bcdb-25ef9dadeafd | -14.5871 | -54.0944 | 2026-08-31 19:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 69810bf8-68aa-35ca-b2fe-9630b17afe7a | -7.4633 | -59.9316 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| dd35da3e-f944-30e2-b563-6322dbfb09b9 | -5.8866 | -52.2507 | 2026-08-31 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 2508c96e-fed5-37bc-9e8e-277f09629212 | -8.7968 | -62.8695 | 2026-08-31 19:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| c8971fd2-ef00-3501-a6d2-c6cca0a9eba8 | -16.5777 | -52.4975 | 2026-08-31 19:00:00 | GOES-19 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 2cce824f-c9a1-38e3-8736-48122f37c15c | -2.7304 | -47.0424 | 2026-08-31 19:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| a75ef102-f9ae-357f-9931-e95e81e3dec7 | -2.7119 | -47.043 | 2026-08-31 19:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 5407ba79-9769-351b-b4d0-cf34298ddfbc | -6.9521 | -58.9506 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 4d0f9cea-bf4b-36c0-a6a8-85c4d5784ddf | -9.0797 | -65.491 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 4f7f9a43-bf2c-3353-ba21-c7e42912d9f1 | -7.0293 | -55.6312 | 2026-08-31 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 11de8a53-071a-326a-9f08-1790da123dee | -6.8233 | -58.8786 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 53572b8b-fb87-33b8-a73d-fd94312f5fd6 | -6.7998 | -59.7665 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 7731afa6-c28a-3e51-9c1d-2b2dbb3bb47d | -9.2086 | -59.5773 | 2026-08-31 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4ede36a8-2daa-375b-9daa-05018c4cf9de | -13.5341 | -59.7589 | 2026-08-31 19:00:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ba895175-14b2-3b14-8156-85d5097ef903 | -8.0443 | -61.7237 | 2026-08-31 19:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 881496cc-df4c-3f67-8682-220274df7a3d | -3.6259 | -59.0765 | 2026-08-31 19:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d88f55aa-721b-387d-aba5-19fc622d77aa | -10.9862 | -48.4088 | 2026-08-31 19:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 80cc10c0-608b-36c1-9f63-9f79af72b93b | -15.3625 | -52.8404 | 2026-08-31 19:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d276d588-8a1e-3c43-8cfd-942bc826768b | -3.6216 | -60.547 | 2026-08-31 19:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 26f10ae6-6f2d-321f-848d-491142b51ec4 | -7.1435 | -72.864 | 2026-08-31 19:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 53187339-68f7-3c86-ae8c-961d6444f2d0 | -8.6674 | -62.8179 | 2026-08-31 19:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 91bd3d5e-882f-35b4-a55b-9cfa1c1f054e | -20.2778 | -47.8425 | 2026-08-31 19:00:00 | GOES-19 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 93.0 |
| d5735264-5e14-368a-98c3-2c35a754abfe | -4.1515 | -60.7068 | 2026-08-31 19:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 131.3 |
| d89f2462-f344-3e50-aa40-a01d28a89e0b | -9.8937 | -46.6316 | 2026-08-31 19:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| fca7dbed-20ea-3a3b-afc2-a2049249999c | -10.107 | -68.4008 | 2026-08-31 19:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 96.7 |
| b60d8edf-4a77-384e-b7b7-6d5cd20ddbdb | -3.3871 | -59.4075 | 2026-08-31 19:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 89c43a7f-2f00-3426-a332-e28f8396bab7 | -9.971 | -53.9214 | 2026-08-31 19:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 08b9be59-135e-3376-8655-d8002716d2ac | -11.1995 | -55.1008 | 2026-08-31 19:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 1ef66f5d-fead-3a12-99c8-62a6db86bf3e | -15.0244 | -48.1689 | 2026-08-31 19:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 82b06f30-6b8f-3320-84f6-745f4c520bbb | -7.6149 | -44.8833 | 2026-08-31 19:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 74688ebe-6c82-3282-bc05-3209e00b5ef8 | -10.5719 | -57.495 | 2026-08-31 19:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 1a526f8d-7408-3c39-b2fc-b88261763ae9 | -10.4451 | -46.5211 | 2026-08-31 19:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 720ec707-20d2-3169-9688-b08904fb19b9 | -11.0055 | -48.3846 | 2026-08-31 19:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| b9170c0a-9258-3003-a5d4-2301e595d9df | -9.1953 | -48.0138 | 2026-08-31 19:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 88d6f9ef-b9b8-3307-a659-e765fdb02541 | -8.2415 | -54.94 | 2026-08-31 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 9ae16fe4-2e6d-388a-a9c0-b7e3d15b72c2 | -9.6673 | -47.9649 | 2026-08-31 19:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| face96e9-7822-35b4-81eb-b988e86290a1 | -9.153 | -59.5415 | 2026-08-31 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 138.3 |
| ec242b47-e939-35b1-81d4-d1489e06e7ac | -9.4721 | -57.0156 | 2026-08-31 19:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 23efc9cb-762a-3a41-9cbb-7b3f51234dbd | -13.5729 | -55.1382 | 2026-08-31 19:00:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 7e2d7b09-cda2-34f2-ae28-8da7cfb5247c | -15.7349 | -56.1093 | 2026-08-31 19:00:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Pantanal | 133.1 |
| a339cfa6-67fc-3ee3-b7f7-b1cb7e208b88 | -9.1897 | -59.6171 | 2026-08-31 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9ec4e1c5-a42b-3c29-b469-dee4bc3d1e4d | -9.4908 | -57.0144 | 2026-08-31 19:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 47575fad-2727-393a-b16e-b9da8ddad377 | -14.2599 | -52.8782 | 2026-08-31 19:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 9cbeb22c-f25d-3c44-b680-c63fb3d5b009 | -15.5038 | -56.0128 | 2026-08-31 19:00:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9e73d4c8-b354-31f4-8139-1d0ba645826a | -7.7938 | -44.084 | 2026-08-31 19:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 0dbdd9d1-a473-3866-91ee-2a1a94f43415 | -6.3875 | -54.7646 | 2026-08-31 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 54fb71ac-22bd-3327-a64a-9155b9b33e95 | -9.4719 | -57.0354 | 2026-08-31 19:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 122b4374-1019-3e47-9dcf-27b8a06d5033 | -7.6804 | -55.3555 | 2026-08-31 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 88a1bc33-3c3b-3557-a08e-9bd1cbdcf3e4 | -17.3027 | -42.6926 | 2026-08-31 19:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 34cfe969-c768-3edf-b185-d6bdd1814270 | -9.445 | -66.7289 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 9af6a5fb-2840-3c92-b8e5-a3be0da480af | -20.3187 | -47.8331 | 2026-08-31 19:00:00 | GOES-19 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 128.7 |
| e3b1b68e-1edd-3201-b085-12f985cb444c | -5.5831 | -60.2307 | 2026-08-31 19:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9cc719b2-d2e5-3515-9c11-d6c66d440a90 | -14.2369 | -51.9498 | 2026-08-31 19:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 7040f8f6-b0db-38a8-9d88-2fd2f9ed3448 | 0.1914 | -60.4878 | 2026-08-31 19:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4c7f71ff-74ca-3419-ace5-12070b39427f | -7.0242 | -59.2374 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 1abe9a21-4861-36dc-9042-8b14f285dd30 | -3.4185 | -61.3461 | 2026-08-31 19:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 2f432efd-6079-3f05-84a7-6ca82afa0582 | -8.9428 | -63.2797 | 2026-08-31 19:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ad960581-4149-3063-ace4-f6775056e5bb | -3.1839 | -60.1559 | 2026-08-31 19:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 100010e4-53a4-3bbf-a685-4e0484beafb6 | -15.657 | -48.6894 | 2026-08-31 19:00:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 35eccca1-9b3e-3806-ad3c-95e6fc924b4f | -5.2547 | -55.9105 | 2026-08-31 19:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e361ce18-b3b1-3c9c-980c-29b5ddb9a16d | -7.2933 | -60.5905 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| b253e97a-dd45-3080-8153-a17d147c9e0f | -7.5526 | -60.4651 | 2026-08-31 19:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| bd29dbdd-d6bb-3cf1-bfee-5a0ef1506b26 | -14.2792 | -52.8758 | 2026-08-31 19:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 6f88c0c7-6a56-387f-b655-5b1d0c90daee | -6.6765 | -58.7492 | 2026-08-31 19:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |


[Clique aqui para ver as próximas entradas](README192.md)
