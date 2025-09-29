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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22cb58af-93e5-30ea-8e97-f939ec723d9d | -6.90202 | -45.72819 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d8c6ec9-7d5d-354c-abc5-cb0bf9603fb1 | -9.44804 | -50.89979 | 2025-09-29 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fddcc55f-9384-3140-994f-a93445d656af | -6.82792 | -44.83748 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 84ce0665-9087-3b2a-9057-fec5cf045603 | -10.41225 | -48.1111 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e1d7201-09f0-35cd-b788-c0c4919af8d8 | -9.39695 | -54.69635 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27aeef2c-0c30-38c8-96c9-99c31e27610f | -6.82947 | -44.82638 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 74777fe5-5a91-3376-857d-e7525983c0a3 | -8.30214 | -45.48185 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| db560a15-d0c6-3952-aa44-7d0f25a30579 | -11.45486 | -44.98133 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a48fa0c9-2011-3d6b-a7c1-1bdf222d344c | -7.7648 | -45.73397 | 2025-09-29 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4875ebae-7146-3353-8344-e6463715cde8 | -9.77893 | -46.94115 | 2025-09-29 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| eb24ba65-d7a1-3784-85e4-bcfc0ef903a7 | -10.68462 | -46.76313 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53afaf2c-dcb5-3e38-963f-54ebae21c03a | -9.4176 | -54.72086 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba01cdf-0662-3d28-a4f6-9e8c6518fc06 | -5.93202 | -48.19239 | 2025-09-29 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3805d3ca-c144-3237-aa0d-b87e61a0a682 | -5.24726 | -45.35359 | 2025-09-29 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe2d7d23-01ca-3fa5-b115-b864db4a9409 | -7.29544 | -42.83816 | 2025-09-29 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 541af703-d377-3265-adbf-7ab58c84a3e0 | -11.43485 | -44.9521 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4bc4a85-7edf-346a-b6e9-f6485aacf8a8 | -6.43453 | -42.81971 | 2025-09-29 04:57:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 276bdf5a-8171-3506-b327-b6b8e3b4f68d | -3.50363 | -52.47073 | 2025-09-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5edbb7b4-2da9-3270-981a-a8a96f954c0d | -6.56819 | -43.49546 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9528359b-0afb-34e2-b541-2bb016a6414b | -11.51013 | -43.54802 | 2025-09-29 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a00160a6-3e4f-3ccd-a89e-2480f7ed69c8 | -6.2219 | -44.20658 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c4724228-59a5-37ee-87b5-af1edd781952 | -8.27251 | -45.50003 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3541eb42-009e-3908-a065-491c2fb7eadf | -7.82362 | -45.1404 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37417a65-d007-3713-a707-1fd1e8e51c7e | -6.1182 | -41.81804 | 2025-09-29 04:57:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7bc049c7-8ed8-30c2-addc-07edc0259b7a | -8.24675 | -45.48883 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67c4e316-d136-3be9-994b-557ca54a7c45 | -9.27905 | -45.73673 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5a26e8fd-5391-3018-8329-47d78c88e6cb | -9.41754 | -54.6995 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09ac767b-5601-3f9b-815d-5c87af6fd3d1 | -9.51425 | -47.69154 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0aa167ee-430f-35f5-9a1e-a19f2ac54123 | -8.24899 | -45.48667 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afbedbfe-8532-37ea-8c15-97dbc54e06eb | -8.27687 | -45.50828 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8912c8ae-0d91-3956-bc47-aad18a02e812 | -9.10413 | -45.85363 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a415bc53-1c3d-3122-9c67-3f9506ef7c60 | -6.49621 | -44.24967 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1e7131b-615b-3daf-9af6-d5853aba68b9 | -8.8849 | -45.02845 | 2025-09-29 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 467f0680-c0d3-392d-b7ad-1745fa5695db | -8.29799 | -45.51318 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ee10c303-9c18-3882-92a8-844156304498 | -8.14314 | -46.40228 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 28ba1fd7-1129-31c9-b710-bff88fe0a0bf | -7.73566 | -46.99956 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12a35bda-93d6-3237-be67-759d0f493369 | -9.31619 | -45.70101 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a294c71-a79f-3e2f-83cf-c14203af4ed3 | -8.28432 | -45.49307 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da93539c-2836-3aff-b918-83dbc059ebb8 | -10.05199 | -50.19704 | 2025-09-29 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ed9bc83-26c9-3898-a41a-f701aae308d9 | -9.31663 | -45.6976 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9323f2a0-93b1-38a0-bcdd-4aadeed3981e | -7.50969 | -44.29241 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99f9aa52-c185-3238-a286-704e6990949b | -5.96445 | -43.27695 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e247ba57-479d-3482-9281-d83a8b2edf69 | -8.82388 | -46.19716 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a41c12e9-b9cf-3486-b259-6a2a5989d0a2 | -7.22101 | -44.76579 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31475ac0-5113-3380-804d-9c4707d6104c | -7.22402 | -44.78526 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d7528f67-bb1d-3ea4-b222-b4822c68f16d | -10.04801 | -50.19646 | 2025-09-29 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c5b9412-a89c-37bb-91bf-535bd3a8364a | -10.4454 | -49.17551 | 2025-09-29 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 216b27b9-ac91-36a7-8016-f601bfa654ea | -9.46655 | -45.49055 | 2025-09-29 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f816418-cd55-3745-8db2-3de06f9fa9ac | -11.3601 | -45.07684 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3057b269-2688-3c8b-9342-bd59a41cfc40 | -3.3348 | -50.25193 | 2025-09-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0fc43e3-7b79-3695-af14-d09edca097a1 | -10.42004 | -46.14682 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 757ff2f6-eba1-3e39-b6f9-b584567f3528 | -8.29446 | -45.49873 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c674cdf2-1145-39db-a6b9-5c0a612da4e5 | -6.89415 | -44.52492 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e85e24d1-c657-3e56-9e88-1e9e32b3db38 | -6.44973 | -45.88986 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a605aed-7d8d-3d3b-abf3-3f3740de989c | -9.05292 | -46.70378 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f0869e42-8202-35e3-93ce-0c1dee51d4b7 | -11.45906 | -44.99518 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ba1d3b4-f21a-34c3-b93a-057318d67b70 | -7.6082 | -46.61294 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a9c9e52-a3dd-3f41-8809-9458d3d0bb1c | -9.77147 | -46.1912 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d08734b-d10e-3b90-8be8-9bfb4b244434 | -6.57746 | -43.42754 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e86121e3-522d-3dc6-8b51-4f92c614e797 | -3.8072 | -51.13801 | 2025-09-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0f778f1-b062-35c5-918a-d65847f32344 | -6.5831 | -46.77552 | 2025-09-29 04:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e20ba0f-66de-38dc-a604-df2ccc4daef8 | -8.73343 | -47.14055 | 2025-09-29 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d3ce2697-5164-3519-92eb-294ba22a04de | -8.8569 | -50.51398 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e5772d3-848a-3389-b317-7884c4b435f8 | -8.25431 | -45.48757 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5ce895a-3edf-359c-aae8-44b6786fcdee | -9.4129 | -54.70242 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84b9914c-906b-38be-8bb3-c65bcc9014c6 | -6.62741 | -45.89627 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 780cba0a-86e2-372f-af2a-d3ec977270c5 | -7.50098 | -45.42339 | 2025-09-29 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c431f7f-81c5-377e-96e4-b91cd21f596b | -6.11087 | -41.82285 | 2025-09-29 04:57:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 629afa9a-ca97-32c4-835e-62371d4e4693 | -6.21483 | -57.77515 | 2025-09-29 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccbc43b3-5fcc-3c7d-a4d3-87e9d5fdb647 | -3.45035 | -49.27264 | 2025-09-29 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b57835b-7c4e-394a-8e59-7e67b60c229e | -10.92222 | -45.71752 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c94eb6f9-f8a9-341d-b099-991dde258f0b | -6.67968 | -44.60432 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92ef1c93-9656-3ddd-bda0-7d7eb2b04ff4 | -9.41015 | -54.69843 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01cb59d0-f41c-3e89-a256-5a33a7abb963 | -11.44303 | -45.03139 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7acdc99c-1ca3-3b3f-b43f-80361331f461 | -5.19715 | -43.76039 | 2025-09-29 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| eaf5fe1a-f41e-3660-8354-0a595db4d0ee | -11.35905 | -45.08544 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b35f84fe-d8c7-3b55-b326-2ec5f3d479b7 | -9.54672 | -47.7674 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18f28a02-c3fe-344f-a921-016bbd2f552e | -9.41069 | -54.69495 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8364d511-ef90-30d6-80d5-7db772de4466 | -7.15888 | -45.50095 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b3bd22d-f949-318d-846c-06707ded93c3 | -10.41982 | -46.14957 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 365beccc-0f3f-3de0-aad7-194a5f80ec75 | -10.82719 | -47.93615 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2c43599c-71cf-3501-8352-29e99ad82e02 | -5.89113 | -43.29921 | 2025-09-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0ee17ec-3bf6-302a-a0f1-15e49baffa47 | -7.73164 | -46.99355 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1af1f3fb-df40-3dea-a49b-9f16505a15a7 | -6.61987 | -44.95134 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b9f2eb6-e7b2-3fa1-a01d-f167533c0a88 | -5.72006 | -42.86868 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fe495ed0-a9b5-3979-9da0-39dc961c6fb1 | -4.70937 | -41.982 | 2025-09-29 04:57:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| eaa2d651-ee97-31c1-bd31-e626928c2b07 | -7.76302 | -45.74693 | 2025-09-29 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a518c31a-bb79-3ede-8304-3380957499a3 | -10.60517 | -46.29229 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8bb8befc-7b81-3980-b6d7-0b8f21543f33 | -10.39224 | -48.156 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 15b9c74c-340a-3445-a0fa-23715fda2dee | -9.04742 | -46.70694 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4bf8066f-4332-3bfe-aa93-a91224e14c31 | -6.62627 | -44.96036 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1432fd8-c134-3448-80c8-cbca9470873a | -10.87541 | -47.78555 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 70d4e87f-8f57-3160-83c2-9a76480906be | -6.74935 | -44.75266 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87b8af52-1fb9-3186-9339-7b65850ac242 | -5.81915 | -42.78497 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 25417773-7ed1-3f72-8644-f624f6989078 | -6.69506 | -42.78185 | 2025-09-29 04:57:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c9daf9d6-0584-393c-9406-bb27363b0bc6 | -7.58667 | -44.8092 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0aa3ce51-3eba-32ef-9832-24a24566aca1 | -9.41538 | -54.71339 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0461537e-fa34-3a4d-9678-80a1ccb933f4 | -10.46591 | -48.19889 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fc8419f3-762b-3b71-b6db-d58874c91b34 | -6.75027 | -44.75085 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ebc3606-b042-37f3-a15b-cbebc705abf4 | -7.89522 | -44.60402 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README61.md)
