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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d0c1d31-9a8c-382c-ad5d-8b494b9e3d63 | -3.54717 | -54.48552 | 2026-08-28 17:28:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 0ecaaae4-4588-300d-95c7-e6cf6d4dee58 | -4.39368 | -55.45864 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| b4d5e40c-aba2-3d0c-a10c-cb5dcf9b9458 | -6.32223 | -54.74223 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ec2c8d00-8703-3696-9466-2b0cee7ad975 | -9.76242 | -64.97353 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.1 |
| e97fb55d-bf07-3f0e-94c5-a481b0af265c | -6.38879 | -65.23785 | 2026-08-28 17:28:00 | NPP-375 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cab12343-6206-37bc-8cf5-2fb05808842f | -6.54569 | -55.23791 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| ccbc5956-eb79-3951-b7f1-8c2240cff8d7 | -6.35003 | -54.89784 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eb1e915b-0fee-394d-93cb-d470236e7fcc | -2.37018 | -49.13095 | 2026-08-28 17:28:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f99df679-05af-3b12-af11-93d7d7f389e1 | -6.60389 | -55.43106 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 79452512-c856-384f-878d-c8cf8ff446e8 | -9.46203 | -70.49333 | 2026-08-28 17:28:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 370c966d-1870-33f0-85fa-ea2399523db8 | -10.27655 | -64.50375 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 98453694-86b4-3ba2-8e4b-087ea1ce2580 | -5.88546 | -57.76857 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 330.2 |
| 9db53a15-54a5-3a0a-b6a6-bfd789274e36 | -8.82279 | -49.62806 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 54d0e687-4987-3aee-8401-9994c0e5e83d | -6.79512 | -59.81319 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e3315069-f564-3b6e-9cbe-8f364f7b3652 | -6.73211 | -59.64417 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f576d4e0-6790-376a-9eb3-3db0bb6a22c0 | -9.51035 | -56.92873 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0184e357-6eee-3aa6-8389-13a00aa38e64 | -6.02627 | -61.64819 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f9e8aa61-53cc-3f72-92d2-cc3c02ae5321 | -6.8442 | -55.60706 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c11145ec-10a7-3eec-b429-dbd67f5d1ed5 | -6.21067 | -55.41551 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d457ad04-4d45-39a9-a758-fe91185c3f41 | -6.81257 | -52.50116 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d7227d83-5add-3405-88b4-7b0358159cba | -10.4038 | -61.2011 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f35bc5e-652f-3ba7-9b8d-72cbcfbc0edd | -6.2705 | -53.13725 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 33530c53-b52b-3047-b8e4-3752aad8eabd | -6.52463 | -55.25679 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a532350f-a32e-3b43-ab4d-3689f01dfd67 | -5.25955 | -50.96706 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 64126700-bb52-3ffa-8a4c-c398713f2ce7 | -6.82573 | -59.94789 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a312f4ca-5c4a-3d1f-b661-57e752605d0d | -10.27106 | -64.50142 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 7e5b31c3-e005-336b-80c2-5fc89f4f5b25 | -4.31383 | -59.47835 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c11409ba-2b28-3297-9c8e-9d0f5b9a8731 | -9.40137 | -51.63688 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 73f0c97a-8df6-3c86-930b-f47b25626141 | -6.79349 | -56.32281 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 07e1fa22-5ce0-3552-852f-fbed4118e674 | -9.69281 | -65.09327 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 85401d12-efab-3b2b-ae35-f0f04ee97389 | -7.85319 | -63.33018 | 2026-08-28 17:28:00 | NPP-375 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1f2a688d-24fe-30c0-8b44-c1b04699a53e | -6.72065 | -56.33772 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 55ea7c7a-c804-327e-aeb3-b6d8939d9b0d | -6.57786 | -55.44256 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 8b417fcb-a19f-3a43-8a5e-fe66eb715fe9 | -6.14813 | -56.10888 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f7080c98-a849-3437-9b36-80a257b670b1 | -7.35571 | -55.17287 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| deae4a5f-f963-3749-9c1e-9d8d80444e46 | -6.11692 | -57.6892 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b54cb81-0073-3cc3-b9ab-358bcae7b7d1 | -9.67482 | -55.0736 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 360e5404-725c-3785-8f61-5becec17c4d6 | -6.93767 | -58.94874 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 24728444-664f-3b2d-848c-1f7f4bed2031 | -7.35514 | -55.16925 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| c9086f6d-e5e3-3daa-a73d-846306a4b95a | -8.67185 | -49.54285 | 2026-08-28 17:28:00 | NPP-375 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e3d94658-ca8b-36e3-854f-dbd2f4be2966 | -9.4169 | -50.43696 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| e28ee7a6-4961-3d88-947f-e85504d7bae8 | -8.87291 | -66.89852 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6e253184-7f7f-3ae4-ae10-c2d51ba44c42 | -6.76527 | -55.68248 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0a505e7e-14d0-3271-9a2e-e9dfdcf4df37 | -6.93936 | -42.71836 | 2026-08-28 17:28:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 71b65df1-1de6-3eab-b1c3-eafa84d0f95b | -6.73734 | -55.45821 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 26c3c1c1-9651-32f1-a13a-38c80555bdc7 | -9.31867 | -70.42013 | 2026-08-28 17:28:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f4860906-0ba4-3816-a963-6d95dcda2a03 | -8.80882 | -50.04722 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 63e65e92-8cd6-3df7-b885-227ccdeee91e | -6.59711 | -55.45444 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5df7aea6-9876-3088-8f92-97be919c7734 | -9.04679 | -65.43504 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5d648e07-61bc-3dc5-a0cb-7273247c281d | -3.49674 | -57.0178 | 2026-08-28 17:28:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3d82247a-f70f-3ca0-a0a1-0b50178102c6 | -6.14539 | -56.0912 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ae8d13b-bbba-30fb-bd2b-4c91d8c76380 | -10.39151 | -61.23232 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d920b24d-0f42-3307-a5d0-fd7389f7db23 | -8.60354 | -54.71613 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f48327ea-5da1-301a-a03f-78ab130f2267 | -7.55425 | -61.41689 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44e17fb2-9d27-3fbc-b46f-af02a88a8b88 | -6.32371 | -57.73967 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3ae3aa62-16f5-3ed7-b2b2-e2ec9aa24097 | -6.75459 | -55.68045 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 04a75793-44c1-34cf-a725-d5c2bd69d15c | -9.6664 | -55.08597 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ab61abd6-d242-3d45-bd41-ef9271d9dc3d | -8.68129 | -62.95385 | 2026-08-28 17:28:00 | NPP-375 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2fda814c-468c-32e4-8c8b-fcdafd99daa2 | -2.71547 | -47.0409 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ad78ae68-5678-3913-9f8d-6a839779ab39 | -3.50008 | -57.01729 | 2026-08-28 17:28:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 493583e8-0f79-35c3-91ff-ab07c7562ee0 | -1.87902 | -44.83479 | 2026-08-28 17:28:00 | NPP-375 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2e51ce62-a703-327c-a4d7-0dff89cb250b | -9.68269 | -55.07978 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 97a82311-7162-30d5-954e-5779bdd8116d | -5.97376 | -61.47893 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d03fa6c1-ba29-36ea-8025-a315bd5c4fb6 | -7.6177 | -61.3507 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 58a81c73-166d-3ac5-8798-659798711deb | -4.60545 | -54.87057 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d27a385e-a536-3342-ac17-53382193a296 | -6.78487 | -59.42113 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 61805306-003f-37c7-a6dc-0bd5010744fd | -6.86811 | -56.52514 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6f779e63-da75-3bce-a533-cf8d861b1746 | -9.47381 | -48.17622 | 2026-08-28 17:28:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 69c6ea69-8711-3892-9099-f05ff2cd5a07 | -8.0348 | -51.81819 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| df188c64-3623-3914-bfb0-6ed743fbee8b | -6.21464 | -55.41866 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9823ea9c-8fe1-35a6-b243-8a5dea219306 | -6.16724 | -53.49957 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b19a63f9-b835-3208-98c6-6449d4c8dd84 | -6.61315 | -56.34077 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6b549bc1-8561-3518-8832-d8eae1b91f84 | -9.61456 | -55.11672 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e7d2c9a9-f61e-3bb9-90e1-30ac53bd9037 | -4.17331 | -55.44262 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d179f4c3-e941-3112-b041-2d5eba33bfaa | -8.63914 | -66.54626 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 95d2fce5-3068-34d3-b7e6-34e819b021cc | -5.91896 | -61.29753 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fa2103f0-8b49-31f4-8c4f-440645526e9b | -6.88483 | -59.41475 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d4cfc023-88dd-3f93-a4d6-fe131117ca4f | -7.60583 | -61.35243 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e1777a4d-4da6-34d1-a56b-5ce4f5a213fb | -6.52003 | -55.23065 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| eeada1ca-b31d-344b-b2cd-e25a05188fd3 | -10.08534 | -68.56451 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.5 |
| fb5edc96-1fc3-37b0-bd31-dbf011b0ec2e | -6.75692 | -58.7189 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8ad61e24-75b7-30cb-9c53-90419d6d51a6 | -2.85834 | -48.55489 | 2026-08-28 17:28:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 058da7a8-a0b9-35b5-b4aa-e6526960180a | -8.0511 | -45.8611 | 2026-08-28 17:28:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7a91307e-4d37-33c9-8ca1-c0e2f914a7b1 | -6.19986 | -55.48056 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5d968502-be79-3c33-b87c-d4ecd4a3f10f | -8.79249 | -50.50109 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6f7e55f5-0b43-35fb-9a73-9e99298e1110 | -6.925 | -42.68169 | 2026-08-28 17:28:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0902a795-a1fe-3ecf-8ada-0a1ae79f6f6d | -5.29095 | -50.94069 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7097f854-dd3f-3b5b-b5f2-1f0557bcaebd | -9.11402 | -60.92558 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6f7f9206-fdf6-358d-8d5f-947602aac59f | -5.99628 | -57.83018 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2d2c3ce6-be47-3a31-9ca5-92609a09c2c1 | -8.59745 | -54.78931 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 7973ad2e-46f6-3905-8102-84d997be459b | -5.89107 | -57.76051 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 6392bcc8-1bda-3815-989b-2c8f34b293aa | -2.72743 | -47.03914 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 8d302a93-a022-32bc-8562-cff59164a07c | -6.84681 | -59.94048 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 422f7d36-9c8a-3c06-b343-33cd43900709 | -8.15742 | -54.96574 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| eb06a47b-c6a1-3098-bd8f-5f387e34fcfc | -6.26382 | -53.11966 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1bafd4d4-a786-32e6-88ae-03235af75ce6 | -3.91354 | -56.01224 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cca52b7c-2ff2-3cf7-ac3b-835508279230 | -8.03245 | -51.81572 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ceec0ed0-c43f-3c6e-8619-4523a3b5985f | -6.52403 | -55.23379 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ee83f520-1a53-3f58-9f47-82957a094188 | -6.5406 | -55.25003 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| fdaf3023-ae0f-39eb-8e6c-1b4e67b2ac6c | -8.79854 | -50.0401 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |


[Clique aqui para ver as próximas entradas](README131.md)
