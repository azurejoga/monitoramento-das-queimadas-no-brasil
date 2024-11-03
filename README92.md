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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80dfe8f3-bbd0-3ac3-b9bb-297338aff41e | -13.86106 | -42.89828 | 2024-11-03 12:21:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 62.4 |
| e3f6f529-a54b-3f12-9691-81c3fe2c713d | -13.84156 | -43.47249 | 2024-11-03 12:21:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ce01a5cd-16da-3d65-92e2-ebc4ad66ad76 | -15.23628 | -43.33609 | 2024-11-03 12:21:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 665e7f1c-fa71-3e19-bd22-24b3521ad0b3 | -2.3061 | -46.5046 | 2024-11-03 12:35:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f615f530-035b-3e07-a1f5-0245cc69a71a | -2.9432 | -49.4292 | 2024-11-03 12:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| a789d359-362a-39e3-ab25-d091cee708f5 | -4.4054 | -43.4746 | 2024-11-03 12:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| f45bc110-c345-34e5-bfb1-335bda078837 | -4.4241 | -43.4735 | 2024-11-03 12:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| e6c876fc-6138-3125-8d77-39b20515aa08 | -4.4056 | -43.4514 | 2024-11-03 12:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5f97b89b-f86a-3c90-838b-cb4e2e68030a | -2.7035 | -49.2875 | 2024-11-03 12:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 4924057c-6e35-32f5-9d54-cbc705ec5db4 | -2.9432 | -49.4292 | 2024-11-03 12:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| c0af9cb6-f756-3860-9ee7-e725ca7b5017 | -4.4054 | -43.4746 | 2024-11-03 12:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 3316d859-3dcc-35d3-ac80-466d98d9e3aa | -4.4241 | -43.4735 | 2024-11-03 12:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 6247d0e9-0c5b-30a0-8b5f-984e4a09eb23 | -4.4056 | -43.4514 | 2024-11-03 12:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| b80bb4bf-7822-36d2-9042-4b8795affe44 | -2.722 | -49.287 | 2024-11-03 12:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 84e452b6-8c31-315b-8b05-fb15f10541bc | -2.7035 | -49.2875 | 2024-11-03 12:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 0edbb5b4-eb98-3616-950c-611d720a0a9a | -2.9432 | -49.4292 | 2024-11-03 12:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 178.9 |
| cb6c71f0-82f3-3821-b39d-4aa9d3801a5d | -3.1501 | -48.5689 | 2024-11-03 12:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 4216eacf-c586-314a-9938-3396c2cfae73 | -4.4056 | -43.4514 | 2024-11-03 12:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 4a739a85-43b3-3c30-8e06-764b6cebf437 | -4.4241 | -43.4735 | 2024-11-03 12:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| f812ae56-0171-339b-af6c-50bc9d9d0542 | -5.6005 | -41.6456 | 2024-11-03 12:55:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 259.8 |
| 2545c9c2-5928-3617-8ed0-4f9db380825c | -5.6 | -41.65 | 2024-11-03 13:04:54 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 26a3e668-88b8-3584-a2df-ca85f881f0c0 | -3.48 | -42.19 | 2024-11-03 13:05:07 | MSG-03 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f43bf324-1c99-3a01-8255-336a896ed021 | -2.3061 | -46.5046 | 2024-11-03 13:05:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 4bfe3d0f-164e-3ffc-9468-18ab2f540f45 | -2.7035 | -49.2875 | 2024-11-03 13:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 3820354e-8e1a-33e5-85ee-f966dba12fb2 | -2.722 | -49.287 | 2024-11-03 13:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 528af05f-9b4b-33ed-bbd4-4c374bf4b626 | -2.9432 | -49.4292 | 2024-11-03 13:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 0c0155cc-a336-3099-8a8b-a152b3d5e685 | -3.1501 | -48.5689 | 2024-11-03 13:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2242d2e6-4eb8-36ff-9254-8c3f5b803de4 | -5.6005 | -41.6456 | 2024-11-03 13:05:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 247.8 |
| 1c7c19ef-6103-337d-adb5-a4f855fae636 | -6.4662 | -38.2181 | 2024-11-03 13:05:42 | GOES-16 | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 27600815-249c-31d6-b835-8e5fbff886fa | -2.7035 | -49.2875 | 2024-11-03 13:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 5286470f-1135-348e-b953-22af4633b1f3 | -2.722 | -49.287 | 2024-11-03 13:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| bfbf830f-44a3-3382-b095-40c021a68f45 | -3.2827 | -40.562 | 2024-11-03 13:15:25 | GOES-16 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 92.2 |
| c8ef7d22-f7dc-39c8-b9e9-532f760d4127 | -4.4056 | -43.4514 | 2024-11-03 13:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 71f86ad8-ccee-38ee-b902-afd8f69a674b | -5.6005 | -41.6456 | 2024-11-03 13:15:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 608a1753-0b89-39fe-af0a-45e230b7a9d5 | -6.4662 | -38.2181 | 2024-11-03 13:15:42 | GOES-16 | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 107.7 |
| f38ed096-fd31-306a-9b8c-d394bfcd6aba | -6.5241 | -41.4688 | 2024-11-03 13:15:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| c104757f-f79f-3c59-bf3c-adc20ac85d5b | -6.5239 | -41.4929 | 2024-11-03 13:15:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| c1cb112e-f0f0-3f42-8b39-22f370b596a6 | -1.2756 | -53.3734 | 2024-11-03 13:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d8009860-5000-3cba-a9a0-fe461ae285c3 | -1.2755 | -53.3936 | 2024-11-03 13:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0b5a5d84-18fb-31f8-95bd-e8c3318e53b6 | -2.1764 | -46.4859 | 2024-11-03 13:25:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| c6815622-833f-3077-9a1d-6877c6718c97 | -2.4252 | -49.6764 | 2024-11-03 13:25:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 166d94c4-fbe9-39ff-9522-0f5fce1cc610 | -2.6325 | -48.456 | 2024-11-03 13:25:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 08518adf-08e7-3d7d-98fd-40a89aff6dd7 | -2.5932 | -49.1203 | 2024-11-03 13:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 09e56f62-4961-3424-b363-cc75ba6699f2 | -2.722 | -49.287 | 2024-11-03 13:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 5a80a621-fe00-392a-83c8-6ee7753ba77f | -3.1501 | -48.5689 | 2024-11-03 13:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 1a843119-a62f-3895-a76a-c2bdc543b1c3 | -3.5549 | -45.3911 | 2024-11-03 13:25:26 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 12fb9dd6-e1b0-36dc-ae5d-c00bc1e4555d | -3.765 | -44.4297 | 2024-11-03 13:25:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| bf0ba2bf-ea9f-3f60-b906-cf90850626ee | -4.4241 | -43.4735 | 2024-11-03 13:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| fe40b82e-b24b-315f-a626-632d22940b81 | -4.4056 | -43.4514 | 2024-11-03 13:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 14637868-e16d-32bc-92d8-643b14b045b0 | -5.6005 | -41.6456 | 2024-11-03 13:25:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 98f93184-458f-3077-9f29-46ae9718acc0 | -6.4662 | -38.2181 | 2024-11-03 13:25:42 | GOES-16 | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 123.4 |
| 81fa8eb4-acc5-3a70-908d-a2e9cee68e7f | -6.5241 | -41.4688 | 2024-11-03 13:25:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 5480c1e2-8b1f-3ce7-baf8-f3c1db763090 | -6.5239 | -41.4929 | 2024-11-03 13:25:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 3e81b119-d011-367a-91b3-8f9c421780a2 | -6.9613 | -42.8108 | 2024-11-03 13:25:45 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 2cbb23dd-46de-34dd-85e5-161dbb34da2f | -7.976 | -38.8582 | 2024-11-03 13:25:51 | GOES-16 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 9d89ca1f-0c0f-37c1-a41b-1951a59e3483 | -1.2755 | -53.3936 | 2024-11-03 13:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 39932414-fd09-359c-b190-ff276822b314 | -1.2756 | -53.3734 | 2024-11-03 13:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b2d04f33-818f-32b8-b04d-24c44a7034c9 | -2.6326 | -48.4345 | 2024-11-03 13:35:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| eb4e920d-5389-32a4-be3e-4ef32bdbbe96 | -2.6325 | -48.456 | 2024-11-03 13:35:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| ddd1c048-cbfd-3092-804b-ec1ac3d4c131 | -3.0203 | -44.3934 | 2024-11-03 13:35:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 32f49de5-d659-378b-8996-9dce2c5f29e0 | -3.1501 | -48.5689 | 2024-11-03 13:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 3243d839-0421-3108-9960-e402eb185cb6 | -3.765 | -44.4297 | 2024-11-03 13:35:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| cc91898d-5ca0-371a-a648-91327c68077a | -3.8227 | -44.1293 | 2024-11-03 13:35:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 12c634e8-6aa4-3414-9f8d-87cf44f8611f | -4.4056 | -43.4514 | 2024-11-03 13:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 465bf0e6-88ce-3f48-997c-42aaa1a8697f | -4.4054 | -43.4746 | 2024-11-03 13:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| c7fe0a6c-fbfa-340a-b91d-f51b472633b3 | -4.4241 | -43.4735 | 2024-11-03 13:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 7aaa2b97-7c92-30da-b196-892c07cd3dfe | -5.3724 | -46.4334 | 2024-11-03 13:35:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 9ddc4735-bf5d-30f9-8baf-2b574919142c | -5.6005 | -41.6456 | 2024-11-03 13:35:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 9576dc24-0c29-3623-be47-25c3c324c316 | -6.5239 | -41.4929 | 2024-11-03 13:35:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| d0aca3bb-859f-36e5-9a55-879efdedf36c | -6.5241 | -41.4688 | 2024-11-03 13:35:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 7f43d6e6-4bd3-3ff7-acf2-c2ad81858c73 | -6.9613 | -42.8108 | 2024-11-03 13:35:45 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 77c368a5-27e8-30bf-a177-b0fcc5ac776f | -7.6591 | -42.7646 | 2024-11-03 13:35:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 56.6 |
| d63ee41e-d705-3b6e-91fd-73e27bf6d02c | -1.2756 | -53.3734 | 2024-11-03 13:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 1b97a030-a134-3e85-a8ea-6848e31a71e3 | -1.5307 | -54.4959 | 2024-11-03 13:45:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 87ef103b-0fc0-3fe5-9516-e072e9f10f41 | -1.4944 | -54.2763 | 2024-11-03 13:45:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 26b756ba-a17b-36a5-8d77-a9556c6b0116 | -2.3363 | -48.5713 | 2024-11-03 13:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 8b671be6-29e5-32ef-bbef-5a3d590b2b4e | -2.6326 | -48.4345 | 2024-11-03 13:45:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| bdd50a51-19c0-345e-ba5d-408db13e6521 | -2.6325 | -48.456 | 2024-11-03 13:45:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 9b5c4880-ad36-3ee0-ad5d-14308930dc25 | -2.6507 | -48.5629 | 2024-11-03 13:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 98172bfe-ac77-3bef-b476-5d7ae003dc68 | -2.722 | -49.287 | 2024-11-03 13:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8aee1e2f-7929-3040-9591-70202fa5e10f | -3.0203 | -44.3934 | 2024-11-03 13:45:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| e53f8410-a015-38f7-b391-3e05a4f6f0ec | -3.0202 | -44.4163 | 2024-11-03 13:45:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 06e3f5f6-3ec8-3850-899f-8ff5dee00877 | -3.1316 | -44.4804 | 2024-11-03 13:45:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 802c49bd-183f-329e-bd4f-261c34cbf49e | -3.2302 | -43.3718 | 2024-11-03 13:45:24 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 925cae71-a873-3413-9d8a-7221fac608bd | -3.1501 | -48.5689 | 2024-11-03 13:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 71493133-0805-35bf-85b7-893f81193d26 | -3.5209 | -44.7825 | 2024-11-03 13:45:26 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 31a2369a-d1f4-362a-8600-6580a5a49c62 | -3.614 | -44.7783 | 2024-11-03 13:45:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 9eb21dcb-6cef-382c-90c4-8a95c3e9cabc | -3.765 | -44.4297 | 2024-11-03 13:45:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5099a7db-e34a-3b5b-ac47-fd622a8f10e5 | -3.6527 | -44.5263 | 2024-11-03 13:45:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 3d711411-8f44-3c0d-a6f1-b6da1b460088 | -3.8413 | -44.1283 | 2024-11-03 13:45:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 18ea49bc-8a0d-31ae-87bf-8b971cbe6f74 | -3.9308 | -44.7406 | 2024-11-03 13:45:28 | GOES-16 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 1fe3f5fe-0d34-3a25-8477-823319d03fac | -3.8227 | -44.1293 | 2024-11-03 13:45:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 6be60c9b-c8cd-3a0e-a11e-58c1418691dc | -4.447 | -42.8889 | 2024-11-03 13:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| fac5e677-e32c-301b-9cc0-95629402f476 | -4.4056 | -43.4514 | 2024-11-03 13:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| abb946bd-c129-3401-86b2-bf78a02e13af | -4.6116 | -46.0333 | 2024-11-03 13:45:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 350e6b4e-b448-3ff8-a750-98a49dac91ab | -6.5241 | -41.4688 | 2024-11-03 13:45:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 576fb338-4e95-3595-b6d3-902ad054b2d5 | -7.6589 | -42.7883 | 2024-11-03 13:45:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 7c94a998-7bab-3d89-97c9-ddf577bcb23b | -7.6591 | -42.7646 | 2024-11-03 13:45:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 2b36eaec-3648-3188-b607-3fb9f62892e6 | -8.347 | -43.607 | 2024-11-03 13:45:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 510201dc-1b16-3f10-ab1c-cd0edd011b9a | -11.81 | -48.06 | 2024-11-03 14:04:16 | MSG-03 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README93.md)
