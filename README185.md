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

## Dados Diários - Página 185

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d17ef9f6-b5d9-386f-b21d-ed59ef79a5bb | -7.0826 | -42.0868 | 2026-09-21 18:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| 32c65f74-603f-3ca6-8ec9-fd870110adf5 | -2.9709 | -57.7197 | 2026-09-21 18:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| af755708-284d-3aec-a4f0-cc2b27e90313 | -10.8282 | -50.1601 | 2026-09-21 18:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 09a6ee80-802c-3d5a-9133-6d6b0820af0c | -8.4922 | -47.0257 | 2026-09-21 18:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| af303a31-ec91-3c72-bbea-7873ce24ad28 | -3.6632 | -58.8643 | 2026-09-21 18:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c02f0272-4aef-3c3d-a574-c0cb8923a13c | -8.754 | -44.2589 | 2026-09-21 18:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 255.8 |
| e6a94bbc-44e4-3bea-9257-8bdd12b4266c | -8.7729 | -44.2568 | 2026-09-21 18:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 4a96d1c8-25f7-3e43-94df-baa77191eab8 | -6.7517 | -55.6256 | 2026-09-21 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 0802d153-c6c4-30a2-9524-654d63756280 | -5.7504 | -43.7091 | 2026-09-21 18:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 9f7d7dc0-c421-3bb0-9725-80f5a7c38cc8 | -8.7381 | -45.4526 | 2026-09-21 18:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| bcbf875e-edc5-30cd-9dab-d64b678759fe | 3.6729 | -61.8695 | 2026-09-21 18:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 208.3 |
| 732bb9bf-9212-32e8-bc90-03088a802354 | -5.5848 | -45.5478 | 2026-09-21 18:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 51b1a941-dee6-3bb1-82fe-25937c1d143b | -8.845 | -45.9391 | 2026-09-21 18:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 8e3cdd9f-6916-32d8-89d5-03c9b1a22de6 | -11.0048 | -49.7325 | 2026-09-21 18:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e44268c1-a9fc-3d03-b025-1c4fcff4596f | -3.4974 | -59.1944 | 2026-09-21 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 4f2a3c25-3ba1-393f-a8ae-db517eb5d35c | -6.3012 | -59.9962 | 2026-09-21 18:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| f425a5bb-bfa1-361f-9646-f828821e8c4e | -10.2793 | -50.2177 | 2026-09-21 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| bf1646f4-dbe8-3257-975a-5ccd91941f00 | -9.4017 | -68.3807 | 2026-09-21 18:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 7463e0bf-df4c-35a7-be3f-43a67e9e3745 | -6.7119 | -58.9992 | 2026-09-21 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 370.0 |
| 94e7e173-2a3d-33b2-91f8-986731be7383 | -10.5582 | -46.5746 | 2026-09-21 18:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bd11eff8-0dbc-3c26-9aef-969ac6171fc9 | -11.8171 | -50.0267 | 2026-09-21 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| e3469b2a-22fa-3256-b18f-fd9a179c00b7 | -3.8265 | -59.3215 | 2026-09-21 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 915a4a9d-123b-36bb-b1dd-a2e03bf95ca6 | -8.81 | -48.7484 | 2026-09-21 18:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 198.1 |
| ac545e66-4a17-36d0-9a39-06d42a5f5428 | -9.6853 | -54.3318 | 2026-09-21 18:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| e94efd18-09af-317c-a53f-117a538b9ca4 | -10.7223 | -54.0008 | 2026-09-21 18:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 055b0211-7ec7-3e48-9d22-21eb768c1cce | -7.566 | -61.343 | 2026-09-21 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 99161bde-d865-3bad-a409-40754921c07c | -3.3321 | -59.4469 | 2026-09-21 18:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1630e9d7-0b36-3180-8169-1168dfe9bb6b | -10.5585 | -46.5521 | 2026-09-21 18:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 13e4210c-9499-3505-b040-caeb00d0fe36 | -6.325 | -55.8451 | 2026-09-21 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 4ce00df9-3b54-3888-b584-b060b6f3157f | -7.5104 | -61.3832 | 2026-09-21 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 58973cef-ce3b-39d6-a60d-f61cab4b4f4b | -10.1813 | -68.4361 | 2026-09-21 18:10:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 55834acd-d5ca-3166-aac8-7b1f2be53afb | -10.8472 | -50.1581 | 2026-09-21 18:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 233.0 |
| f41dc334-0a46-3181-a27b-c6d3c644f50d | -10.8735 | -53.9668 | 2026-09-21 18:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f527fe31-0743-3c2d-8f77-3b4870a3063d | -9.8683 | -48.4689 | 2026-09-21 18:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 825fb89c-9fb6-3096-9713-a8a7a92a46f5 | -9.0287 | -69.2191 | 2026-09-21 18:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 0d623c93-786a-3917-9172-dd7006010476 | -3.7364 | -58.8626 | 2026-09-21 18:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e752bb9f-eb2a-367f-8aef-2432a4a392bc | -11.1541 | -42.8364 | 2026-09-21 18:10:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 106.0 |
| 873cba01-5661-348b-922b-5603e784b7ce | -11.68 | -43.45 | 2026-09-21 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db5bd344-1746-3019-ba1e-73919ace89b1 | -9.61 | -43.94 | 2026-09-21 18:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e14b4c4c-211f-3684-b7f4-15baac2aff76 | -15.89 | -41.72 | 2026-09-21 18:15:00 | MSG-03 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 51b6c21b-cba9-33cf-a4dd-0220f8cd896f | -8.77 | -44.28 | 2026-09-21 18:15:00 | MSG-03 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0b986b3-ecfd-37a7-8970-eeb1600ec901 | -7.06 | -49.94 | 2026-09-21 18:15:00 | MSG-03 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbc10a0d-56c6-3013-a1ed-5e774b154301 | -7.72 | -61.23 | 2026-09-21 18:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 005edf7c-0ee1-3c5a-a711-9b13cf2dc800 | -7.59 | -57.68 | 2026-09-21 18:15:00 | MSG-03 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3f22b3f-cc3f-3feb-b0d9-fbb5cf8eb896 | -10.85 | -50.16 | 2026-09-21 18:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83fb7525-b903-3678-a0e0-dec88f317349 | -8.8 | -44.28 | 2026-09-21 18:15:00 | MSG-03 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d800eb43-06e6-3469-8435-e4c2d1cbefea | -7.59 | -57.61 | 2026-09-21 18:15:00 | MSG-03 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6855235-86c4-3b40-97f7-cc2154da8a13 | -3.51 | -55.43 | 2026-09-21 18:15:00 | MSG-03 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cabda3d-ecf3-3f25-ac06-2c5538d97c40 | -4.52 | -44.95 | 2026-09-21 18:15:00 | MSG-03 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3957edf9-b567-3dcf-b736-26166b3cb74e | -3.51 | -55.49 | 2026-09-21 18:15:00 | MSG-03 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0950a3e-7957-3f84-baa4-2a01e5e2aa32 | -8.791 | -60.8127 | 2026-09-21 18:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 741f6de4-5553-395a-b7df-2e2712abfab0 | -3.6632 | -58.8643 | 2026-09-21 18:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 16b9af68-28c2-3b81-8a0d-1372974a03a7 | -6.7518 | -55.6056 | 2026-09-21 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 80e54ddc-23b0-314d-a5dc-32b8ea5716dc | -6.4373 | -55.6212 | 2026-09-21 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| baa1340f-2e81-389e-a3ff-27b429fbc19f | -4.9421 | -55.8233 | 2026-09-21 18:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e96d7eee-c065-3127-a28b-a15c54b85b07 | -6.8796 | -41.6995 | 2026-09-21 18:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 52df9d6a-21ed-31d9-85a1-64330180fdfe | -6.9034 | -42.9341 | 2026-09-21 18:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 88585d5a-d361-3e3a-b38d-e7df86c4d0dd | -9.1708 | -50.0049 | 2026-09-21 18:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 088d29b3-a12e-3f11-90f6-731fb2f27b77 | -10.473 | -51.2808 | 2026-09-21 18:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a9992230-b062-34b0-a8c5-ab9e90a05b21 | -9.9516 | -53.9844 | 2026-09-21 18:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 053ea894-2539-3fad-8422-b501b8c15e63 | -4.6853 | -55.6343 | 2026-09-21 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 665748d4-e157-355f-951a-3418070f8dd0 | -3.753 | -59.419 | 2026-09-21 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 48ddb7b3-7dc0-3eb1-9e8a-cbe49bb7fe55 | -11.0412 | -54.1362 | 2026-09-21 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 257.2 |
| b5343473-1d5d-394d-b02d-5ce02bc67deb | -5.6223 | -43.3701 | 2026-09-21 18:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 75395ab6-0f39-39de-88fb-3da504c048cf | -6.7279 | -59.4423 | 2026-09-21 18:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| d5f0d161-2173-392a-a9be-ab4e2eb2bb0a | -6.1832 | -47.5915 | 2026-09-21 18:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f9e4ba5b-bd66-33f9-9bc3-9bdbf4b90c29 | 1.5653 | -55.7858 | 2026-09-21 18:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 366a17f0-5c9f-3425-9021-90f90e6bd94d | -9.247 | -57.1488 | 2026-09-21 18:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| c57fbc31-752e-3257-bd44-67e908d83d9f | -6.9871 | -47.4885 | 2026-09-21 18:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| c4b008f5-69cb-3cde-be76-74cd47c954c3 | -8.845 | -45.9391 | 2026-09-21 18:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.8 |
| e921a2ce-f1cd-3b33-b60a-a5c122633ef1 | -8.5982 | -54.6341 | 2026-09-21 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 868386de-8f3c-3c7c-8948-8c96a87ae267 | -6.4671 | -59.9711 | 2026-09-21 18:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 176.7 |
| b2848e1a-ca61-332d-bb38-23bdfef6a30d | -3.6946 | -60.5835 | 2026-09-21 18:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 7c84127a-ca5f-3d9b-b306-8b1774b0fc66 | -5.6594 | -43.4139 | 2026-09-21 18:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e4b416ba-5db4-37fa-84e4-1d5a5924c9fa | -4.8865 | -55.8846 | 2026-09-21 18:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 74abd389-dace-3252-9293-fd9202a687b4 | -8.6755 | -70.0345 | 2026-09-21 18:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 2c469616-9121-385a-912d-3bcec9109605 | -1.3742 | -49.3154 | 2026-09-21 18:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1c871067-8a04-3e05-89af-e80b247904ac | -9.9768 | -50.2694 | 2026-09-21 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e6f6392c-ac55-32b5-809b-b0eef4b2c633 | -3.5894 | -59.0581 | 2026-09-21 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 09ba6dc4-6ee1-3dc8-b34c-b844b91b1c73 | -3.4599 | -59.5209 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| b400d541-9929-3789-85f0-4cecfb3809a3 | -8.7919 | -44.2546 | 2026-09-21 18:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 13fdee30-93c9-353a-84b3-de6e417091bc | -3.3493 | -59.8479 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| aed1b43c-b930-3243-b771-72176dca32c4 | -8.3367 | -50.8397 | 2026-09-21 18:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| e4ebf4d5-148b-3af4-963a-11c969bc71aa | -5.9814 | -57.7867 | 2026-09-21 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 7a499fb3-5c07-3625-9025-bb675c09805f | -9.9755 | -68.7929 | 2026-09-21 18:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 223.3 |
| a85227d4-9644-3ae5-83bf-cb2080196686 | -6.7332 | -55.6265 | 2026-09-21 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| acef5876-4cee-360d-837e-fecf0771ece6 | -10.1814 | -68.4175 | 2026-09-21 18:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 9da9c3b7-0d00-3b5e-801c-cd79f987f0c3 | -5.9083 | -57.6726 | 2026-09-21 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 1d544320-f1de-387f-805c-b3ce5fcf164f | -11.6798 | -43.4446 | 2026-09-21 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 244.2 |
| f7ba1964-500f-342e-ac04-0686d3303039 | -10.2635 | -49.984 | 2026-09-21 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 01bd6941-7824-3081-aed5-ebb11e897cb5 | -5.8225 | -53.5214 | 2026-09-21 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 07b277e2-beb5-336d-9ff3-7d84731cf0f0 | -2.8791 | -57.8184 | 2026-09-21 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 107.8 |
| f42a4cf8-9afb-37f9-bad9-f296658c4cac | -3.4579 | -60.246 | 2026-09-21 18:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 18de6052-dc78-30d1-95f1-bed0dc7ecf6d | -8.7911 | -48.7502 | 2026-09-21 18:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fe6ad4f1-2d55-3470-b4b5-40545953fd52 | -9.3577 | -50.0943 | 2026-09-21 18:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| dd78cbc4-4a3e-3d02-a8be-9829400646d6 | -2.9709 | -57.7197 | 2026-09-21 18:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 7329a916-3b97-3693-99cb-b5a4c22f1508 | -11.8499 | -46.8105 | 2026-09-21 18:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 62de4dc8-3bde-399f-809d-90f5557c8ba4 | -6.4486 | -59.9717 | 2026-09-21 18:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.5 |
| a021f744-268f-37da-b033-5f19bf2e6580 | -6.283 | -59.9586 | 2026-09-21 18:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 88cbf6a8-dfd8-3298-9949-7716e25481dd | 1.7779 | -60.2324 | 2026-09-21 18:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.1 |


[Clique aqui para ver as próximas entradas](README186.md)
