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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab1045ab-4ffe-32c2-9e6c-e99d361396e4 | -6.55208 | -45.58298 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8c071d8-e300-3370-b17c-94135ef5ff4b | -6.55332 | -45.57531 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b38f8675-2989-30e7-a253-7dc50fc234d0 | -4.35266 | -55.66143 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2cc9a5b-210c-3d4a-a0b6-cf378fe93234 | -3.00773 | -54.17655 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae8fca18-e293-3bb8-872f-b9670bb14bf9 | -3.89282 | -52.12107 | 2026-09-21 04:19:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a97c444e-a632-333d-8beb-73f492975db3 | -9.02996 | -44.92427 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 958996c1-092c-32da-b49e-af907206340c | -7.42227 | -44.77792 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdb0aa45-0cca-3233-bc22-8a2af6358f2f | -7.10202 | -42.08114 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8e726b1f-768d-3273-b6e5-5e350c728bd2 | -8.78574 | -48.73737 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9964c14-1bbc-3373-912f-467282a99626 | -4.09454 | -52.12341 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39f49407-7505-3c6c-9c60-5ec5b7bb0368 | -8.76536 | -45.86135 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85daa81a-f292-393b-976c-e6a7fc512230 | -4.57548 | -42.9451 | 2026-09-21 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64684e7c-3240-397f-9fa9-10e4627f521e | -5.85098 | -53.5274 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 880e602a-762a-394d-869d-c8506afa3195 | -4.0718 | -52.12647 | 2026-09-21 04:19:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b63f52bc-8057-30e5-9a4c-cf4eef3cf784 | -4.5885 | -45.16394 | 2026-09-21 04:19:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef06030e-fdac-35e3-a097-e3921b15225f | -2.64523 | -54.69382 | 2026-09-21 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fcf693e8-377d-39e4-b22f-62c43f558c4a | -6.06569 | -55.6187 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9fc8d47-ffbb-3a4e-b0f6-7d4b6bab6a87 | -8.76309 | -44.27802 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5fc59aaa-2168-3c3d-9816-47e7126e4142 | -7.43292 | -44.77596 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b050450-a391-3d21-b6dd-6bad5a2cd07f | -6.65909 | -50.89247 | 2026-09-21 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8294d415-6e30-373d-a92f-536e801ef2e4 | -5.21028 | -56.07895 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b43cb35a-7ad0-3b88-b59f-12958f09669d | -2.46117 | -49.22759 | 2026-09-21 04:19:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f2c5928-a9a9-3fb5-9f16-7dae98034a40 | -9.44488 | -45.39949 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 89e014da-4c72-3fa1-bbaf-e9e70681d4f1 | -9.27233 | -46.21609 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bccd4c66-c216-3367-b4c2-19d1c252d224 | -6.91306 | -43.7351 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae3f9464-ce4d-3bc9-b1e1-d9da5b412322 | -2.29602 | -48.58411 | 2026-09-21 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b619c9e-4405-3d4d-bfeb-1ba8453160ff | -6.3775 | -35.15265 | 2026-09-21 04:19:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 4b7f34d9-4a44-31f5-8b6d-9b4a7bd881d5 | -8.76361 | -44.29602 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f81052e-787b-3ffa-9e4b-fd3581a00757 | -8.7791 | -44.28418 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fd99a1d-72fe-3486-9b82-f4f56acc6ac3 | -5.83806 | -53.53336 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e01a697-22b9-367c-8536-3ea1aba1e35f | -6.72537 | -55.08958 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86f63c89-65a7-327a-ba5e-641b29dcad4e | -6.98059 | -45.82033 | 2026-09-21 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4090307f-44c3-39cd-99a9-0c7a811bca75 | -4.79548 | -48.23138 | 2026-09-21 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c324e01f-d251-318e-907a-a33b36ac7ce3 | -9.26288 | -46.18707 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0ced67b-b3e1-3796-a0c5-496a401b74da | -9.45835 | -45.40171 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 10315f48-0d9c-3b6a-9a0e-fa831bd97400 | -7.09865 | -42.08062 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c78844f6-344a-3b44-bb4a-f7b2b8a1a417 | -7.24876 | -55.59216 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98ba657b-0ad5-3a96-8dc5-742e4b2ee86f | -7.59438 | -57.66906 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aac0d99e-d4e7-336d-b66a-d41625cde374 | -7.2454 | -55.60393 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 10f3f5e0-ad72-3ad1-8aef-2964e7a31092 | -9.25185 | -46.18925 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e543a7bb-082f-3d6c-abdd-fe9d2d6b4f61 | -7.38356 | -46.0394 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43c6a4b1-85d9-3240-b2ed-402c592036cf | -9.56661 | -45.49012 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ae5724c-39f1-393d-9138-d610b9b2dfa7 | -7.78685 | -44.81813 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9141252-19f5-350a-bcb5-f1c8f561e6ce | -9.44446 | -45.44433 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59f0f533-0ca0-3893-b968-2443611e5c8a | -9.45776 | -45.40535 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8636df7a-69f9-37c6-ad5d-a30f21da89c8 | -3.6397 | -40.58214 | 2026-09-21 04:19:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 57407dbb-b83d-35a5-8844-6c6b26aa5c71 | -4.33652 | -46.37557 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61b46f8d-7027-387c-a968-9a01060c5f79 | -6.91472 | -43.7247 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3717442f-636a-344b-90af-3efab8a60fac | -9.24277 | -46.17969 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e95d0865-9ccc-3e0f-a84a-205313088c6b | -6.77257 | -44.14808 | 2026-09-21 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8703629a-04b4-3b76-96c4-4920f8cdfb47 | -8.46356 | -45.08538 | 2026-09-21 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02b749d0-255b-39f9-b19b-a077725536d0 | -6.2972 | -41.75885 | 2026-09-21 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ac988f78-4660-38df-ab6d-5fb85c0ba35c | -3.17303 | -51.35238 | 2026-09-21 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 492e37ff-00cb-361e-ae01-c52d0ae308ba | -6.56458 | -45.54959 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b05dc96-d0c1-312b-90e0-e7532fc937bf | -5.84818 | -53.5433 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 960f3de0-561e-3c8c-8ff0-abe2353101bd | -4.57933 | -42.94218 | 2026-09-21 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fb8c011b-5e64-335b-a8e1-d4bb2fcfce12 | -6.41666 | -55.02009 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc31446e-74eb-307d-bef5-788ea10b4f13 | -6.7628 | -48.17104 | 2026-09-21 04:19:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83cc9839-f9ec-369e-96fb-b8609c5ff808 | -8.26777 | -47.57141 | 2026-09-21 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cfaaaad-140f-35b2-b99f-dc20e6b0ee3d | -9.06069 | -48.78334 | 2026-09-21 04:19:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9146595a-5985-3f73-be6c-7429b3c6760d | -3.34424 | -42.76116 | 2026-09-21 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11bb1d58-3030-34c3-82b5-1bd1263421b2 | -9.25181 | -46.23267 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fafde363-144f-36b8-a906-7633db503a0f | -5.19879 | -56.11021 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 049f9e36-55fa-3dc1-97c3-c1d74267c461 | -8.42171 | -45.85999 | 2026-09-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc1a5161-b724-3349-8827-a2fda7d76db8 | -7.42735 | -44.76775 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1823707d-48f5-3dca-966d-09bc678189b0 | -6.61238 | -50.0649 | 2026-09-21 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 995f9053-7afd-364e-9f44-e61a10d3b438 | -9.44294 | -45.38087 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff94dd2d-77b1-3b3d-83bd-9312728bb0a3 | -2.90458 | -54.19285 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54add005-3161-3574-887a-a738af284c56 | -6.91324 | -42.93982 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9b745bcf-9d8b-3c0a-b295-c0c82bab3a51 | -6.28481 | -41.77174 | 2026-09-21 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2c0ad440-51c7-30db-9072-987c80074a8a | -6.41576 | -56.10927 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0db6b214-a019-3885-82fa-080bfe5cf066 | -3.45193 | -50.60638 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c10bd025-d6ca-3bf7-8540-851c6f9211e0 | -5.53651 | -47.42538 | 2026-09-21 04:19:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b2d997e-2a73-3f54-8b87-b6673b8fea01 | -7.51173 | -46.23307 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5ee9b72-1264-3a15-8721-4c5dc981d565 | -5.82226 | -53.52206 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1286430c-7ac8-32c8-a784-dcb25f88ac8e | -5.84099 | -53.55036 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18ca3fcd-8726-30ad-a757-e42b0620b4a7 | -3.87613 | -40.75118 | 2026-09-21 04:19:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 338576b0-9c24-37ff-b973-282672b77ca9 | -2.45739 | -49.22215 | 2026-09-21 04:19:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c18f267-6023-3300-9f93-35774852a71c | -7.41472 | -49.84359 | 2026-09-21 04:19:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc40eea1-4883-30ff-aef6-68e18a01186e | -7.0557 | -49.90609 | 2026-09-21 04:19:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54dff1a2-f6bc-3ad7-9856-5601dda73be5 | -8.6595 | -45.43304 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eab946c4-0e3d-307b-a7a1-80097698f906 | -9.2434 | -46.17588 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b92c52b2-ed81-345d-85a5-7f6fee7d4bdf | -6.41681 | -56.10365 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a87edf9e-1a67-3617-8eec-98a27f738a7e | -9.46787 | -45.40697 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9cc2ac2-a471-365b-8eef-d22ea0d2c30b | -2.91085 | -54.19402 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fada879-75b8-31d7-aab7-e4cdad24939f | -5.82438 | -53.51018 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e617c2a-d921-36d0-aaaa-07a54beb5427 | -3.88742 | -52.12008 | 2026-09-21 04:19:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b114399-528a-394b-b943-446dbdcefa5f | -7.44814 | -44.74546 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 792523b7-6ffa-3e1d-b3e2-3fe1bcb52950 | -8.77297 | -48.7401 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba0d734e-3dfa-3eb8-8f9d-1d3b81846043 | -4.68131 | -40.14286 | 2026-09-21 04:19:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ddb114b6-18cc-3743-814e-fb1a60aa346d | -7.58805 | -43.44172 | 2026-09-21 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0078b766-516f-36cd-87df-edd9b7def460 | -3.01319 | -54.18228 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 256e80d7-999f-3bf4-b1d5-107759759b6a | -7.5889 | -57.6757 | 2026-09-21 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5b79e49d-ce77-31f0-a8dd-88fd7e69ba7b | -7.5704 | -57.6766 | 2026-09-21 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 83d5253d-dd81-31fd-9a50-30aa476b0a96 | -6.4486 | -59.9717 | 2026-09-21 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 476cb1e7-54d7-31e9-9fcd-611eeee5c81c | -9.5594 | -66.0359 | 2026-09-21 04:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 7a729f2a-3e91-3ee5-b5a3-2a052c8eab04 | -14.5342 | -53.38124 | 2026-09-21 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8281351a-5ca5-3b99-bbbc-6d5bd31370a6 | -10.08308 | -50.25302 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82237723-6408-33fd-8ab3-b44447b0d79f | -10.676 | -50.73421 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14b39b73-5214-382e-b998-d1fc0da270c2 | -11.95898 | -46.49871 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README41.md)
