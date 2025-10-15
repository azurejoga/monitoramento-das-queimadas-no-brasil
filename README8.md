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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b22e55b-ce6b-3cdc-b896-69ecb4a20444 | -4.8916 | -43.4446 | 2025-10-15 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| e868e274-a4e6-3dcb-8819-3475b470f94e | -5.409 | -44.2185 | 2025-10-15 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 22075ac7-ece7-316e-b379-7ee8002ab6c8 | -4.6696 | -43.1326 | 2025-10-15 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2b23dd85-9c8a-3391-94a0-6c1dbc462fe9 | -4.9102 | -43.4666 | 2025-10-15 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 213.7 |
| 63c97548-8854-3de3-9fd5-eec2a78f6909 | -4.8916 | -43.4446 | 2025-10-15 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 6529e33c-305d-3dae-8f12-b8596011f619 | -4.6511 | -43.1104 | 2025-10-15 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| bb9f4db1-544f-3f5a-8a5d-1b69d1248e2c | -5.4276 | -44.2402 | 2025-10-15 02:10:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 69df889d-f7b3-3199-a194-c5dc3d4f3726 | -8.2275 | -44.0853 | 2025-10-15 02:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| f122fd4b-b3f0-3ce3-b566-d1700e213680 | -5.4465 | -44.2159 | 2025-10-15 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 276.9 |
| f05ca296-696c-3722-9903-934c35820cc8 | -4.6509 | -43.1337 | 2025-10-15 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| ed337131-a233-3a3a-b917-dee0ea225f63 | -4.8915 | -43.4678 | 2025-10-15 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 165.2 |
| a285a790-a140-3b67-9c55-432bfcd1e401 | -7.9628 | -44.1362 | 2025-10-15 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| aff49214-08f9-3015-b1e6-aec510c69661 | -8.2278 | -44.062 | 2025-10-15 02:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 4ac99dba-6205-3752-aea3-2ee8c57cb700 | -5.4278 | -44.2172 | 2025-10-15 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 383.9 |
| 86017cad-b668-3052-8833-f2aeaba18be3 | -4.9104 | -43.4434 | 2025-10-15 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 2ceb9cca-6070-3597-abe8-66f9f2d64584 | -5.4463 | -44.2388 | 2025-10-15 02:10:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| b8ebd508-14a4-3c06-ac09-ee9f1ef60174 | -7.9439 | -44.1381 | 2025-10-15 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| fbd14df0-f35b-31bc-bb47-b55e908c3364 | -5.428 | -44.1942 | 2025-10-15 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9125f11f-fa70-3eba-b8aa-f955b09cb6f4 | -7.9442 | -44.115 | 2025-10-15 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 2d6c0c68-e9c3-32d7-94f5-cab2ddafcf67 | -8.2278 | -44.062 | 2025-10-15 02:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 95a9f517-601d-3ff2-b18a-02cedfede76f | -5.9 | -43.744 | 2025-10-15 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| a5a3a6ae-a9cd-3c80-b2d9-cc22a19dfc14 | -5.409 | -44.2185 | 2025-10-15 02:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 888d80b4-36da-3d4a-beb0-2b7413d40527 | -7.9439 | -44.1381 | 2025-10-15 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 72894677-84fc-3ec3-9f79-69c3409e1cdb | -4.6511 | -43.1104 | 2025-10-15 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| da44b681-06d6-31dd-bd7d-c8f6791a96fa | -4.6698 | -43.1092 | 2025-10-15 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6ad7719f-c55a-3cf7-ba3a-74e09105f934 | -5.4463 | -44.2388 | 2025-10-15 02:20:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 67a65fa3-aece-3d2d-8afc-2204bcfdb919 | -4.8916 | -43.4446 | 2025-10-15 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 6a4d02c3-760d-3d0e-beae-344e9c1d6825 | -4.9104 | -43.4434 | 2025-10-15 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 174.1 |
| e534bd03-1ef7-3d47-8734-6daa82c4740d | -4.9102 | -43.4666 | 2025-10-15 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 346.1 |
| 739df63e-df24-3c9b-9023-e1cd85bbb5d7 | -8.2089 | -44.0641 | 2025-10-15 02:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 56a1485e-fc6b-30bb-ac38-7b99b500b006 | -8.2275 | -44.0853 | 2025-10-15 02:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 216.0 |
| 6380e62d-3aee-3a09-91f3-40de0931ce25 | -5.4278 | -44.2172 | 2025-10-15 02:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 386.8 |
| 63d6df9c-d911-3abe-a65b-4430917fc434 | -5.4276 | -44.2402 | 2025-10-15 02:20:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 0c5caefb-8578-3527-96e3-e47ac0e376f8 | -5.8998 | -43.7672 | 2025-10-15 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1f2966cc-7cb3-30e9-91f7-1c1db3ee0a02 | -4.6509 | -43.1337 | 2025-10-15 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 2f40c687-e763-388b-80c4-e6c3949d1b9b | -5.4465 | -44.2159 | 2025-10-15 02:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 205fd0d4-ac0b-3176-861c-ff89b6f82bf3 | -8.2086 | -44.0873 | 2025-10-15 02:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| cb70d2a6-b81d-336c-8652-d1b698a9d791 | -5.8812 | -43.7454 | 2025-10-15 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 52f73a88-7578-35b4-956b-ddda9f70ab4f | -4.6696 | -43.1326 | 2025-10-15 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6f65a254-fd48-3ebc-835d-8edcc79e12ec | -4.8915 | -43.4678 | 2025-10-15 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 315.0 |
| 080e3c44-d506-3fe7-aca4-bb6970016314 | -4.6698 | -43.1092 | 2025-10-15 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 264acf89-6dba-37f7-b083-a6ef6ffa0347 | -4.8915 | -43.4678 | 2025-10-15 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 311.1 |
| d75cae64-25ec-31c7-9144-e77d9db914cd | -7.9439 | -44.1381 | 2025-10-15 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 841091bc-cf26-3686-b15d-76f66c5875e6 | -5.4276 | -44.2402 | 2025-10-15 02:30:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 945fda55-c126-33ff-bf76-06876f9216bc | -5.4465 | -44.2159 | 2025-10-15 02:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 5ef440d0-85dd-38eb-b7bb-6051a52a763d | -4.9102 | -43.4666 | 2025-10-15 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 281.5 |
| fa7d17ec-89a9-3413-99be-5f1493c1c5e7 | -4.6696 | -43.1326 | 2025-10-15 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f39ac0a4-73cd-3af3-bfc1-528076642a8f | -4.6509 | -43.1337 | 2025-10-15 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 05ea9e4e-b930-384c-975c-ae759bb2a6f7 | -8.2275 | -44.0853 | 2025-10-15 02:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| af775d32-5622-3b1c-ad8a-28f30878eefc | -4.9104 | -43.4434 | 2025-10-15 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 7fd9015b-d06b-3752-834c-e57476cc04ec | -5.4463 | -44.2388 | 2025-10-15 02:30:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 88f56540-e95d-35ac-9978-598f41ed9bb5 | -5.9 | -43.744 | 2025-10-15 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e1dd4923-3dab-386b-802f-0b89adc2285b | -5.4278 | -44.2172 | 2025-10-15 02:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 320.6 |
| 1c09425f-1a58-3b4a-83fd-a75f4ccfe587 | -4.8916 | -43.4446 | 2025-10-15 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 4277942f-acf8-3ccf-bc7c-a0e9cffe2fa3 | -5.4463 | -44.2388 | 2025-10-15 02:40:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 52fb5dd4-30e8-358f-a37c-bce89e11f3a9 | -4.8915 | -43.4678 | 2025-10-15 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 220.5 |
| 5280d6d3-12c2-3325-ac30-d26839fbc015 | -4.9104 | -43.4434 | 2025-10-15 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 81374489-0cc7-38d0-af76-d626a1cb7207 | -5.4187 | -40.9841 | 2025-10-15 02:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| 783487be-1ba2-39a1-9baf-bca6e031423a | -4.8916 | -43.4446 | 2025-10-15 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 79c25f37-1de8-3b2c-b8e7-3845456ee280 | -4.9102 | -43.4666 | 2025-10-15 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 369.8 |
| 5bd40c0c-7504-318e-b3a4-87e713b5b772 | -5.409 | -44.2185 | 2025-10-15 02:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 9f1e8b13-19ae-3ccf-bcf0-ac9c6fd43a91 | -5.4276 | -44.2402 | 2025-10-15 02:40:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 173.4 |
| f2847fa1-7cc9-38d4-9cbe-58c131b2eb31 | -4.6696 | -43.1326 | 2025-10-15 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| cb8de290-30f7-32ca-9a8b-43a19eae8ed6 | -5.8812 | -43.7454 | 2025-10-15 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| e49790f2-8307-3b8c-96e2-01b76338f336 | -4.6509 | -43.1337 | 2025-10-15 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 5f5b820b-2c31-3168-947e-56387bc1d1a4 | -5.9 | -43.744 | 2025-10-15 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 78e2e121-56c6-32c5-b726-f2bfde098534 | -5.4278 | -44.2172 | 2025-10-15 02:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 239.6 |
| 1af397d7-3316-3a2a-b86f-8a9dd8af0f67 | -5.4465 | -44.2159 | 2025-10-15 02:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 160.4 |
| de41167a-d15f-359e-ae3e-67d237349474 | -5.4375 | -40.9826 | 2025-10-15 02:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 48a05194-6cd0-38d4-a79b-32d21a2795a0 | -7.9439 | -44.1381 | 2025-10-15 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ccaaaf9c-2c98-3c63-bb21-004d90561a78 | -4.6511 | -43.1104 | 2025-10-15 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c59e9d3f-614a-381f-a3cd-af3474be1ffa | -4.6509 | -43.1337 | 2025-10-15 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| d16434d7-0ed6-3195-b341-34781f7e7f28 | -5.4465 | -44.2159 | 2025-10-15 02:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 319e3403-bef6-3d8f-941e-5e778994528c | -7.9439 | -44.1381 | 2025-10-15 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| fba98a63-0efc-315f-8e31-1dafdb013258 | -5.4276 | -44.2402 | 2025-10-15 02:50:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 62def629-2c3a-3e85-8772-ac7d1217cdf1 | -4.8916 | -43.4446 | 2025-10-15 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 17c1044f-067c-32dd-89f6-e7b5e8db3c79 | -5.4278 | -44.2172 | 2025-10-15 02:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 237.0 |
| 76c0dbaa-1b8c-3629-8621-8199d808ee02 | -4.9102 | -43.4666 | 2025-10-15 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 272.6 |
| 68730fab-09c4-3a5c-b86a-60b3a8e75773 | -4.8915 | -43.4678 | 2025-10-15 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 25beef77-ef5e-3317-a29a-f5ae530ec544 | -4.6696 | -43.1326 | 2025-10-15 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7b51ceb6-48be-3c78-b8fa-0ec45ff72620 | -4.9104 | -43.4434 | 2025-10-15 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| fc27b570-225e-3d9e-82fc-1355e73fd9ff | -5.4463 | -44.2388 | 2025-10-15 02:50:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 38662576-4bd9-3106-b744-a959b92a6276 | -4.8916 | -43.4446 | 2025-10-15 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 23f82e13-17a3-3495-99b7-56039bac696b | -4.9102 | -43.4666 | 2025-10-15 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 231.5 |
| a533df0d-0617-35fb-9eab-fa9984297645 | -4.6696 | -43.1326 | 2025-10-15 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e9580bcf-346c-3c4a-a3c9-95776a4f484c | -4.8915 | -43.4678 | 2025-10-15 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 250.2 |
| c9ac322c-5513-3990-928f-cb2948a03e65 | -5.4276 | -44.2402 | 2025-10-15 03:00:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 4a3a90c6-22ee-30d6-8a49-4c797cef3468 | -4.6698 | -43.1092 | 2025-10-15 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 1ceeb9f5-420a-3aa6-848d-266be8e0554a | -4.6509 | -43.1337 | 2025-10-15 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 1af15778-3286-3b8d-8dcf-478a11aef7dc | -5.4463 | -44.2388 | 2025-10-15 03:00:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 4b1fa8ef-171b-38ae-99d3-b2133505ef23 | -7.9439 | -44.1381 | 2025-10-15 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ffb0cace-2439-31f5-8fcc-322a27412bd3 | -4.9104 | -43.4434 | 2025-10-15 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 55ad0e18-637b-37e1-8048-037c5b35a84e | -8.2278 | -44.062 | 2025-10-15 03:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| abeb83bd-35e1-38d1-b21f-2cfbdeebdbca | -8.2086 | -44.0873 | 2025-10-15 03:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| c4b6301f-aa7a-3566-aa7d-7807ed8ab4ac | -8.2089 | -44.0641 | 2025-10-15 03:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 937a882d-0a47-3d5c-9100-44838d989d17 | -5.4278 | -44.2172 | 2025-10-15 03:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 226.9 |
| 9f58e16d-6c48-30a0-b758-73a3ee1ca472 | -5.4465 | -44.2159 | 2025-10-15 03:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 2f44aafc-de4a-3343-934b-23d4f0f11ba1 | -8.2275 | -44.0853 | 2025-10-15 03:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 8c7e129a-e4a0-3389-b8c7-cff4c206ed3b | -5.4278 | -44.2172 | 2025-10-15 03:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 194.1 |
| 3cf40f85-c01c-373e-8096-ffb5723ef6e8 | -5.4276 | -44.2402 | 2025-10-15 03:10:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |


[Clique aqui para ver as próximas entradas](README9.md)
