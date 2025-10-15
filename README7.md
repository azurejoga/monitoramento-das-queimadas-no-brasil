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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49155cea-8829-369c-8d7f-2e81290b0361 | -5.4276 | -44.2402 | 2025-10-15 01:20:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 337.7 |
| c517087f-0623-3d50-87e9-d0bd53b71720 | -5.4278 | -44.2172 | 2025-10-15 01:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 489.2 |
| 47ff8af3-ed2a-3312-9f84-109840ac5b61 | -4.6509 | -43.1337 | 2025-10-15 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 96cb36a3-e210-3617-87fe-3b0171a246ad | -4.6698 | -43.1092 | 2025-10-15 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| aae77584-ffac-3e08-bac6-7c7214fe7e1a | -14.0482 | -44.6722 | 2025-10-15 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 8644f9bf-e6e8-309d-ae9f-3e956e7de31c | -7.9628 | -44.1362 | 2025-10-15 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.9 |
| c6680d54-7e70-31a6-8416-17bdef91b340 | -4.6696 | -43.1326 | 2025-10-15 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 6e16d86d-fb03-38af-aadd-5f318b85b86e | -3.5639 | -51.1312 | 2025-10-15 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 9e33750d-a76a-3b63-a485-c294d23e3c85 | -4.8916 | -43.4446 | 2025-10-15 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 145.0 |
| f6285b29-8026-3838-85c2-46df413aab06 | -5.4465 | -44.2159 | 2025-10-15 01:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 267.3 |
| 743756fb-39a8-33c8-96f4-52bbf1fba299 | -4.9102 | -43.4666 | 2025-10-15 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 295.8 |
| 672d3b83-6a84-3dbd-82f4-3b6801b1dc2f | -4.6511 | -43.1104 | 2025-10-15 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 87d3c7bf-0f4a-3f35-b04d-07cbddb674eb | -14.0287 | -44.6757 | 2025-10-15 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8c0bc2ab-4cff-3b6d-8956-64ea10c81c68 | -3.564 | -51.1104 | 2025-10-15 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| ae53c60b-4ce1-356e-967b-5387ba8a572d | -5.8802 | -43.8613 | 2025-10-15 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 64dd501b-800a-32d4-a554-84b01bd7f50d | -5.8614 | -43.8627 | 2025-10-15 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 06c12df1-cdfc-3630-a3f0-becff9db7228 | -4.6511 | -43.1104 | 2025-10-15 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 96fae082-b28e-336b-88c7-cf45ae555c31 | -3.564 | -51.1104 | 2025-10-15 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 85bc0ffb-d333-3731-80fe-47ca61e879c3 | -7.9628 | -44.1362 | 2025-10-15 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 6c8177f2-6cd7-3570-bfb5-04dabbb94c30 | -4.6696 | -43.1326 | 2025-10-15 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| a3067ddc-0207-3422-adf3-43be316a218d | -12.1928 | -50.3689 | 2025-10-15 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 2dd898a9-a736-3464-b589-a8c9618bf411 | -6.694 | -67.6624 | 2025-10-15 01:30:00 | GOES-19 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 489172df-3790-3409-8f08-74d7b7ebff46 | -7.9442 | -44.115 | 2025-10-15 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 0043c846-2757-3505-b400-1a764d6d955b | -4.8916 | -43.4446 | 2025-10-15 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| eebdf822-9d92-3914-b34b-8b109b1292e7 | -4.6509 | -43.1337 | 2025-10-15 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 84313e3b-4848-3873-86b9-79eeff0f9711 | -3.6674 | -45.2285 | 2025-10-15 01:30:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 01108205-2ca9-3a27-9ee4-b511f2dbfa0e | -7.9439 | -44.1381 | 2025-10-15 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 1a9546be-241b-38ab-b66c-8fa62b3a9b64 | -5.4463 | -44.2388 | 2025-10-15 01:30:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| b59dbe45-a46f-3e9e-80bc-f6f9e0d578f3 | -5.4278 | -44.2172 | 2025-10-15 01:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 463.7 |
| 13b0061f-04ef-3f6d-96b0-3ab2c704b706 | -5.3919 | -44.0356 | 2025-10-15 01:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 964a2401-12e1-395b-aebf-a0305d325370 | -4.9102 | -43.4666 | 2025-10-15 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 91d1752e-7c2d-32c9-9790-a38d8a71b2a2 | -4.8915 | -43.4678 | 2025-10-15 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 8abf8e5d-e081-331a-907c-8c760079d0d1 | -3.5639 | -51.1312 | 2025-10-15 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 2fb674d4-0acc-3583-826b-535bf56dfc0b | -4.6698 | -43.1092 | 2025-10-15 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 0aa754f0-3cca-358c-bf6e-9e5edde2c328 | -5.4465 | -44.2159 | 2025-10-15 01:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 248.2 |
| a1488f8a-1e32-3162-8d0c-2e93e04a9e04 | -4.9104 | -43.4434 | 2025-10-15 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 55dfbd07-0aff-3a66-9e4a-60759ae2807f | -5.4276 | -44.2402 | 2025-10-15 01:30:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 232.4 |
| f859eed4-a3c9-3d7e-ba45-e53aa0711f86 | -5.409 | -44.2185 | 2025-10-15 01:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 17b913ef-e9cb-395a-ab2d-e2edffbba986 | -3.5639 | -51.1312 | 2025-10-15 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 5903bed1-c2d5-3efa-b61a-7e7429e0c147 | -5.409 | -44.2185 | 2025-10-15 01:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c4aae862-39b7-3921-88c6-197171e31747 | -2.9435 | -49.3443 | 2025-10-15 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b8670bea-9deb-3cd5-afaa-4c1498b8904d | -4.6696 | -43.1326 | 2025-10-15 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c8163356-b870-3aad-af97-1d7e1746f336 | -5.8614 | -43.8627 | 2025-10-15 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a47667a5-59cc-3e0a-af4d-a3ba178c1be8 | -5.3919 | -44.0356 | 2025-10-15 01:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 89683782-4e1c-340a-aaaa-6b82392cf2ca | -4.6511 | -43.1104 | 2025-10-15 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 08716d60-4839-3e32-9c2e-327d646865d2 | -5.881 | -43.7686 | 2025-10-15 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e8010064-6edc-3724-9b44-d365b432cd2a | -7.9442 | -44.115 | 2025-10-15 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 64ec77c2-6242-30de-a395-912443a38eca | -5.4465 | -44.2159 | 2025-10-15 01:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 229.4 |
| b866dcb1-b64c-3a4a-81de-7ba01d57b671 | -5.4276 | -44.2402 | 2025-10-15 01:40:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 8e3daa75-f1f6-3150-bd9c-35d74e9c5e1b | -4.9102 | -43.4666 | 2025-10-15 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 292.8 |
| fae0039a-44b4-334c-9961-3534157ba999 | -7.9628 | -44.1362 | 2025-10-15 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 51.4 |
| a1cb3f50-4b44-3df1-94e7-1deaaa9c1f41 | -4.8916 | -43.4446 | 2025-10-15 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 18b2ddd1-080c-30b9-b413-6ea30de6bb68 | -7.9439 | -44.1381 | 2025-10-15 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 41b120bf-e186-343b-81f5-70f6f0d80ce3 | -5.9 | -43.744 | 2025-10-15 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 859942d8-b4f4-3c88-b34d-bf56f06ea992 | -5.8812 | -43.7454 | 2025-10-15 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 29d60334-2663-34cb-ba1a-b9a445c47ff9 | -3.564 | -51.1104 | 2025-10-15 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| e122744d-ebb7-38a9-a0a6-61fcad71ad1a | -5.8802 | -43.8613 | 2025-10-15 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 9bc0cac7-45cc-3677-9115-8078043caeae | -4.9104 | -43.4434 | 2025-10-15 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 177.1 |
| f2cc2272-747f-34e0-b8c3-d8257065a894 | -4.6698 | -43.1092 | 2025-10-15 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| f3dd27e6-a6b7-3207-aa09-6c8d597a2f9e | -5.4278 | -44.2172 | 2025-10-15 01:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 370.1 |
| 1377e57b-1666-3a73-b5e7-73db39611e50 | -4.6509 | -43.1337 | 2025-10-15 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 2510460c-7fe3-3c27-b276-a6bb346d9250 | -4.8915 | -43.4678 | 2025-10-15 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 235.1 |
| 7900da3b-549c-3bb8-889a-682bd52008d7 | -5.4463 | -44.2388 | 2025-10-15 01:40:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 81ac79f0-de0f-322b-8fd0-b5322df586b0 | -5.8614 | -43.8627 | 2025-10-15 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 490e12e5-84a1-3a65-9f94-f687a9f7d186 | -5.4463 | -44.2388 | 2025-10-15 01:50:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 6d833099-7b59-3913-b567-78c836b29001 | -4.8916 | -43.4446 | 2025-10-15 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 28c1bc67-cf54-37a5-bf09-d99237815fbf | -5.409 | -44.2185 | 2025-10-15 01:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 8ec9dc8a-9a08-3ff5-af1e-ca3f4d0886d6 | -5.8812 | -43.7454 | 2025-10-15 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| abbb9960-896b-3623-aa45-805521ab9424 | -7.9439 | -44.1381 | 2025-10-15 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 40fb715c-3c6e-390c-b6ec-572fcb171396 | -4.9102 | -43.4666 | 2025-10-15 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 246.2 |
| 95b97d0d-53d3-3c30-916e-0676f6dcb318 | -5.4465 | -44.2159 | 2025-10-15 01:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 308.6 |
| 017ba181-d442-389a-a0d7-08a07bbd9515 | -9.6299 | -40.3143 | 2025-10-15 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 89d3d299-1a6b-3094-9a6f-6143696d059e | -5.4278 | -44.2172 | 2025-10-15 01:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 449.7 |
| d0402184-814c-379d-a24d-59a6eacb2194 | -4.6511 | -43.1104 | 2025-10-15 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ef53d928-69db-3c9d-a0dd-4a4059dd82b7 | -5.3919 | -44.0356 | 2025-10-15 01:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 44e98e30-c0d3-30c6-b8cf-adc695899b39 | -4.9104 | -43.4434 | 2025-10-15 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 179.6 |
| c5d97b0c-83e0-3d08-92de-f6b75f4d858c | -4.8915 | -43.4678 | 2025-10-15 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 8e62f898-75fe-3a11-9426-c596205b8403 | -4.8586 | -42.8863 | 2025-10-15 01:50:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 6f0a61f1-2fff-3908-a496-7b89b475484c | -4.8398 | -42.8875 | 2025-10-15 01:50:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 4684a1a9-3b5f-3d52-984f-8514d5e1f2b5 | -3.564 | -51.1104 | 2025-10-15 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| dc0fa77d-8e77-34b8-a8a5-ad1fb82b7960 | -4.6696 | -43.1326 | 2025-10-15 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3f0d46ca-4d0e-33f2-8ba8-b2a9b6515be8 | -4.6509 | -43.1337 | 2025-10-15 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 33875432-dab2-31bc-8b04-6b3b081283be | -5.4276 | -44.2402 | 2025-10-15 01:50:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 210.9 |
| a4726b09-1a81-3efc-a4e4-3fbad8ee5ac4 | -4.6698 | -43.1092 | 2025-10-15 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2fa12e8b-40dd-377b-aac5-cbd99fc9aa10 | -5.8614 | -43.8627 | 2025-10-15 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 1a17be68-026e-390f-a0d7-fbb6e9287694 | -5.4278 | -44.2172 | 2025-10-15 02:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 568.0 |
| 0e137e1e-c604-36f9-bda4-1e08a45e36ce | -4.6698 | -43.1092 | 2025-10-15 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 3df9f190-d9db-3625-941d-ac447d8d63f2 | -4.8398 | -42.8875 | 2025-10-15 02:00:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 3f883123-d26c-3861-86fb-ccd109d7652f | -4.8915 | -43.4678 | 2025-10-15 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 734ac3b6-b3e4-3c63-b8f3-ee20413c087f | -4.6509 | -43.1337 | 2025-10-15 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 1ea6bbb0-e3d5-30f4-b50b-dc8a7ba088b6 | -7.9628 | -44.1362 | 2025-10-15 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 97b86105-7c6a-3337-84b8-97731a75adad | -4.6511 | -43.1104 | 2025-10-15 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 702a53e8-8789-31fe-8abd-ca0eb49b0fad | -4.9102 | -43.4666 | 2025-10-15 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 184.8 |
| a77db337-a3d1-3f0d-9f4d-b4c33d95bb9d | -4.9104 | -43.4434 | 2025-10-15 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 366bbc60-4b04-388d-adcd-618932c43887 | -7.9439 | -44.1381 | 2025-10-15 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 1eae3997-d94c-37ac-82d0-4fa6c7b3f851 | -5.4465 | -44.2159 | 2025-10-15 02:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 332.0 |
| be38a53c-3949-355b-8246-e13b508253e5 | -5.4276 | -44.2402 | 2025-10-15 02:00:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 241.9 |
| 6308e213-8dae-358a-8c22-833c3aad90f3 | -5.409 | -44.2185 | 2025-10-15 02:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 60f59f6c-f9e8-3c97-b1be-b66474dda5d4 | -5.4463 | -44.2388 | 2025-10-15 02:00:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| e140660d-ba2b-347c-9f51-929381724188 | -4.6696 | -43.1326 | 2025-10-15 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |


[Clique aqui para ver as próximas entradas](README8.md)
