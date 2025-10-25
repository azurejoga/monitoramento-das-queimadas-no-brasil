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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 296d45d4-9aa8-3a38-9a7b-df46fb9c5b8d | -6.79746 | -45.42228 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 713292fe-196a-3b2b-83f0-11a25749438d | -13.33994 | -47.91338 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a77ea039-380a-39f0-9270-450b885a2887 | -13.04692 | -47.20911 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b051086a-c8e2-376a-bc1e-f7fbfd648341 | -9.24027 | -45.61774 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d85883fd-54e9-381a-8bda-6a51cf0384e2 | -11.53497 | -47.09988 | 2025-10-25 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bd16983-dfd9-32a2-b41b-44930e0e3c83 | -10.64001 | -52.18264 | 2025-10-25 04:19:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c432340d-b137-31be-94e2-69bb154299fe | -12.11114 | -46.70794 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0461586-13f2-3f4d-9627-a4760770ca28 | -7.78675 | -45.39836 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b90449c7-00bf-35a3-8a51-2d7da4ca903c | -9.23752 | -45.61372 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7985c2f7-8e5b-34b2-9aee-c3c058ac093f | -6.89808 | -45.17435 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51e2933d-8918-3dc7-bb36-707bc1aef110 | -6.92015 | -45.16362 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a61c15c5-71f0-3dba-b826-cf0b4f5c1ab6 | -6.91629 | -45.16657 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 076f6c24-4211-3117-b39f-35fcd883286c | -10.55448 | -49.77699 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07215ad9-f13b-36da-acd6-6b89fdb3397a | -13.0095 | -48.55349 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f57b56ad-7b65-3d93-98e6-0a52e310ae33 | -8.31106 | -47.86673 | 2025-10-25 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0aa28d9-b61a-3f84-8eef-a97c5ec7670b | -13.74631 | -44.33218 | 2025-10-25 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afa903ff-578d-39f5-8eb9-29bde83670b7 | -1.29865 | -49.34553 | 2025-10-25 04:19:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f791c323-becf-3b99-a810-e8722e73ed2b | -9.92822 | -47.99928 | 2025-10-25 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3debb698-e133-3dc9-9397-3d9653bdf53d | -12.08589 | -46.41952 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32b68140-768b-3b16-bf7f-ca1d86cd9427 | -12.21145 | -46.50517 | 2025-10-25 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16e51bd2-4056-31c4-b287-0a434ae2d794 | -12.2248 | -43.30746 | 2025-10-25 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7713f46-f074-3255-8435-2fdb6fa819b3 | -10.68575 | -48.08829 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1cf7c782-ed41-3f69-86e5-0f0accde1c03 | -8.33431 | -46.17936 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56ac6586-971f-3994-b8a4-b74d60aabef4 | -9.39186 | -46.26653 | 2025-10-25 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62922646-04c3-3dbd-850e-02ecc8bd86f6 | -10.17657 | -50.43718 | 2025-10-25 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36338f63-25b9-388d-9f79-f71de60a8d90 | -9.60651 | -44.62961 | 2025-10-25 04:19:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afdfb0b7-a684-3b6c-9524-210a23822255 | -13.40287 | -47.9593 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6bef82b-87ca-327c-87d2-7f701ea40da8 | -8.6103 | -54.65769 | 2025-10-25 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e84e47e-7fdc-3678-91dc-025b3d5e829d | -12.84239 | -48.64417 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 494b91c1-7a69-35f6-9c88-1e0219f5e339 | -12.87835 | -48.60163 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81c46e5e-de4c-35e8-b611-6572adac3685 | -9.83005 | -48.79123 | 2025-10-25 04:19:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d3d0acf-45bd-3eb9-aa1f-7c7de9168414 | -6.95255 | -47.77843 | 2025-10-25 04:19:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 283cad52-a386-3575-a127-6a244aaa4f20 | -12.78099 | -47.38087 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67df8634-30e7-3bdb-a891-f3d8a4ca51cf | -11.05119 | -47.89529 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c24759b-81de-3d7a-8d81-6823f568048c | -12.09418 | -46.41025 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaf09a74-b46f-343e-8fcb-73636074f4e0 | -9.32965 | -46.98426 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5826d1b9-5a6d-35c1-bbee-9936dd10431a | -12.12777 | -46.71071 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d0a85c0e-3c2e-3661-8f33-5fb7bb8438e5 | -8.19386 | -47.87405 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36bb54aa-f104-3ba8-a312-407426b90176 | -8.33707 | -46.18352 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 136eaba8-2567-370a-8e89-61581c65507c | -6.78417 | -45.42019 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d3a8625-abe0-3d6d-a060-3534a0f33eab | -6.83195 | -44.77675 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a88affdd-a021-36c4-a6b1-0fd95307406a | 0.36195 | -50.92196 | 2025-10-25 04:19:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 76bf94bb-2e63-3194-b510-93200fcd07b1 | -8.66693 | -44.77443 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee9fe008-9f40-348d-ad62-b7127b0d7356 | -8.14353 | -46.87733 | 2025-10-25 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2d8388a-d381-3e6f-b4bc-53178d4f6cf2 | -7.78399 | -45.39437 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67bdd70e-b107-3c75-8a86-9cf5a2987865 | -9.29813 | -45.20962 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3f40ff8-5c25-36e8-a0d2-7b3de0f6eaab | -10.17813 | -44.6657 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e28bedf8-db20-31be-a2a9-c5ad30f77943 | -12.79538 | -48.66236 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8c54a4a-878c-3222-b612-fe6ff70aa6c0 | -7.58712 | -43.57588 | 2025-10-25 04:19:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00d308d5-d768-34f0-a51c-6d33ae73f1e9 | -6.02182 | -48.13428 | 2025-10-25 04:19:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9932c2ca-ba4f-322a-88f0-6b9f390449d5 | -11.97426 | -44.97104 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de5157b9-ab72-3630-9c54-4dc2a517a7ca | -10.20241 | -47.54877 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04390057-c665-3a03-b03f-7f24fe5cb8fa | -6.92346 | -45.16416 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d9fa0aa-7a30-3a27-83fb-cf93b4325f5d | -14.12428 | -43.85313 | 2025-10-25 04:19:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b98fc5d7-a171-398f-9637-352e2f9aa6a3 | -12.13053 | -46.71483 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 611ce406-3c53-3708-9f2b-5aa337f0a4d1 | -7.80492 | -44.55153 | 2025-10-25 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65a89cb9-2779-384b-afe2-12fca6ceac2c | -8.5478 | -50.04487 | 2025-10-25 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 945f6f6b-cadd-3b04-b717-3c6ef8b560c7 | -12.04614 | -46.41277 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fad15225-f7cd-34f2-be3d-a728d5bdcaf7 | -11.35445 | -47.60792 | 2025-10-25 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4db49f3-efda-35c8-9496-32c7333c72a8 | -9.58241 | -45.15195 | 2025-10-25 04:19:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2411a725-894c-354b-bd25-de93cfb32089 | -10.62363 | -42.3201 | 2025-10-25 04:19:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52e6cce2-6e9f-3aec-bcab-9a22624659bd | -12.36769 | -48.12336 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68ef7e4b-4eb3-3204-8648-c0853ba2f9e4 | -7.78668 | -45.14196 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b835181-fe36-37c3-acef-c738b09ae74c | -5.7047 | -49.31183 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d61121e3-0614-3771-8f9f-3760652d6227 | -12.46551 | -44.53618 | 2025-10-25 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61129a52-e381-3699-b836-9ae3f131500e | -10.56312 | -47.99891 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd50596a-e42b-32c4-b0e0-ad57c10026dd | -8.60994 | -44.81141 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e7406e2-9901-3e7b-9cc3-ee9a66f86a30 | -10.83886 | -48.81705 | 2025-10-25 04:19:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6694b27e-e912-34e3-87b4-61510aa4c39c | -9.59786 | -46.86499 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ff5c9d3-174a-3454-8aec-5c9ea0d2278e | -8.61123 | -54.65726 | 2025-10-25 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdf5a5f6-1cd5-34ef-a74f-6d8b4076e685 | -7.42166 | -46.65496 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01ddaa8a-82ed-3af4-af0b-b27deb9ad7ad | -12.30197 | -47.45906 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0706899e-28f5-3baf-bdea-f4790374730a | -11.34517 | -44.89036 | 2025-10-25 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c312c927-4d2e-35fb-98da-c8c432542b07 | -10.65005 | -48.08665 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0828cea-6ab0-3632-a550-03f800615108 | -11.73278 | -45.23416 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4be39cf-e1bd-3081-8b77-b472f722e9ba | -9.43117 | -51.47324 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b61dad3c-d12e-369a-9394-2a91cbed0e3b | -12.06882 | -46.39854 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 62e69283-960c-3d8c-bd5c-cf18d24424c4 | -9.24912 | -45.58341 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a728e69-7c37-3155-80ff-8f789fe3e349 | -9.32071 | -45.1954 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5bd1482-3f1d-388e-863f-481cbb1e377f | -12.46215 | -44.53565 | 2025-10-25 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8c912d9-19b5-3782-9ffd-4bdd61d11ddc | -7.6427 | -44.56917 | 2025-10-25 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 822f8984-f22f-31d1-8aca-95c0f086e217 | -7.98357 | -47.38737 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 339be425-5c2e-394c-b3e5-418c830df01d | -13.03329 | -46.61587 | 2025-10-25 04:19:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b83c3284-1ded-3b48-b612-8cdf65b8d48d | -9.31026 | -45.21869 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5e6bd55-d6fd-3b74-81a2-d9d9f08fc889 | -7.9426 | -47.20169 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8a87095-42fa-35b2-be7a-67da06378f2d | -7.64293 | -42.1723 | 2025-10-25 04:19:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 79984642-037a-3b6b-80f8-e42af5f2f5ce | -6.93916 | -43.63915 | 2025-10-25 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ef23120-17c7-3392-99f5-eae9264fc3a8 | -10.41004 | -44.74555 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 720dfebd-9346-39f8-80f1-93e98ee8ac7f | -9.59565 | -47.84039 | 2025-10-25 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e5abc90-cb66-385c-99e0-3848fa135c8c | -8.19712 | -46.50455 | 2025-10-25 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d23b0334-ab15-343a-a93b-443c3cf723a3 | -7.00642 | -43.47164 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6405642a-c82f-39a4-a68e-7dbd5319b14e | -5.81404 | -50.19683 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee1b964d-3408-3d35-8c81-d16439fbd7d7 | -9.28123 | -47.00277 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06602f20-ae25-3416-b597-ad6f58ab05eb | -13.08402 | -47.56752 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00c7c524-356f-3d8d-aa12-d2fa4447623b | -7.63278 | -44.5676 | 2025-10-25 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b455822-eda3-3f17-95e9-beb8deacae7d | -11.32092 | -48.34728 | 2025-10-25 04:19:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d98747ba-093f-3f34-8cde-e66e3dddcd6e | -7.16565 | -45.84203 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e408717-0fe6-3e51-92bf-82e4cf74e4ec | -7.85034 | -46.43757 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0610588d-c362-3cea-b49f-40b4b7f765b1 | -10.92781 | -50.42199 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8e4bf7b-a75b-3061-98bf-0f2e64b8fc15 | -9.595 | -47.84433 | 2025-10-25 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README37.md)
