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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7d73379-0e32-3283-a89f-2994317b08a2 | -6.31982 | -43.37971 | 2025-05-28 00:20:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9bf7c921-b167-3aee-bdd0-3f9b81a0734b | -7.63287 | -45.76376 | 2025-05-28 00:20:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| e7e1cf47-56c8-35fd-8561-c09d3b455e3f | -7.97165 | -45.93505 | 2025-05-28 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2b935693-bd68-3562-83e7-333f58bad086 | -7.62117 | -45.75971 | 2025-05-28 00:20:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 503547a1-103e-358a-8212-aad7833118af | -7.22233 | -43.10986 | 2025-05-28 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 63a95a0a-2a73-3ecb-8784-72bf6346f155 | -7.21351 | -43.11112 | 2025-05-28 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| d0f3182b-2fdf-303a-aa7d-0d2b8e689ccf | -8.14595 | -46.48205 | 2025-05-28 00:20:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d7775487-2dac-3f65-a973-d94441e60f5f | -7.18703 | -43.11486 | 2025-05-28 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 1ffbed47-cdc7-3151-9d0e-a0172227ef2e | -7.6668 | -46.09708 | 2025-05-28 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 944cfc8b-f98e-38c5-a3b2-f16819e99fb0 | -8.01773 | -49.69391 | 2025-05-28 00:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| c354bdcc-5a29-3493-aac4-841b72561ee0 | -7.66647 | -46.10354 | 2025-05-28 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 721e8f36-a960-3ef8-8573-ea87f5ac7db5 | -6.32865 | -43.37846 | 2025-05-28 00:20:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5ac5b4bb-f9ca-3cd4-b3e7-ca23c33a3cf5 | -7.68525 | -46.08885 | 2025-05-28 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7f2d9245-7a7c-330b-a0d3-89a05ba00402 | -5.64823 | -43.5954 | 2025-05-28 00:20:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4bb919de-d697-323a-8980-15f03f10fa4e | -7.17868 | -45.10392 | 2025-05-28 00:20:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f0a2e68f-bbea-305d-ba12-f904cc0b0043 | -6.12219 | -43.95502 | 2025-05-28 00:20:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b3f0512b-ba35-3bef-8f16-d3e41d4a1c9b | -7.22355 | -43.11873 | 2025-05-28 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 81f2c80b-a0ca-30e4-8ebb-c14b40b8806a | -7.19586 | -43.11362 | 2025-05-28 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.6 |
| 16e3f0ca-9bf0-338e-aede-4485e860560d | -4.48775 | -47.79442 | 2025-05-28 00:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 340ab008-5971-3f96-8680-4e02dfdc98c6 | -6.3186 | -43.37085 | 2025-05-28 00:20:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f9514a4b-2077-35af-afec-77ef9d8b9d01 | -7.21473 | -43.11998 | 2025-05-28 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 9d1749f0-c209-33d5-9e1d-22a2ddac28af | -8.17553 | -46.49814 | 2025-05-28 00:20:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 51e47301-d122-3d73-a5a8-9adf308011c0 | -6.12096 | -43.94599 | 2025-05-28 00:20:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b3b06b28-34f5-3877-98f5-4f651aef7960 | -7.62296 | -45.76522 | 2025-05-28 00:20:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 39f3ff2e-9e94-31c4-b209-3309230fc761 | -7.19464 | -43.10476 | 2025-05-28 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| bec4ac99-f537-321d-869e-0d684f378513 | -7.20468 | -43.11237 | 2025-05-28 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 196547da-c11b-307c-8308-3e7f01145567 | -7.6215 | -45.75389 | 2025-05-28 00:20:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 110b1da5-9817-3b8c-852c-aec65f5608ec | -5.64701 | -43.58653 | 2025-05-28 00:20:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5e207737-a4c2-3439-bcb7-58f19aa08a99 | -7.6868 | -46.10083 | 2025-05-28 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 152e3328-4e72-328b-824f-9089880d66c1 | -7.07871 | -46.056 | 2025-05-28 00:20:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 588276e2-3828-3395-9c32-293be75f5297 | -7.18581 | -43.10601 | 2025-05-28 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 844a20a8-04b5-322c-8959-72a0e91e8196 | -7.07715 | -46.04433 | 2025-05-28 00:20:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7052cecc-ab01-3de3-a85d-081dcfd3b163 | -7.6751 | -46.09028 | 2025-05-28 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6c08af4c-78d1-3a26-8d3a-1fd0304a3d21 | -7.66842 | -46.10907 | 2025-05-28 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| b0a2caf4-bf3e-3f69-81a1-3a3c7e6ecc05 | -7.96158 | -45.9365 | 2025-05-28 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a9cffe0d-7a01-3dc7-80bd-000e737b9b07 | -7.2025 | -43.1171 | 2025-05-28 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| 57b44136-1b75-347f-8785-5138ca6a0aec | -10.235 | -52.2263 | 2025-05-28 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 9dbbb339-d2eb-3571-af43-b45ffe0b3fef | -10.2539 | -52.2246 | 2025-05-28 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b84b6ade-2909-37f2-9435-265f2a156f8b | -10.2348 | -52.2472 | 2025-05-28 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 11177eef-92f0-33e9-91b1-32af13804916 | -11.8373 | -44.2674 | 2025-05-28 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 816ab5da-fb4d-3baa-9ff1-44ca2bfa6a2f | -17.2847 | -42.623 | 2025-05-28 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 5a599c7d-cb1d-35e4-9089-90f9ddbd2b23 | -11.4062 | -44.82 | 2025-05-28 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 652e11f4-d366-331b-925b-8114bc777f12 | -7.6762 | -46.0995 | 2025-05-28 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 64e6242e-5c02-3faa-b0b3-483e3391d655 | -11.387 | -44.8227 | 2025-05-28 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 06346cfa-3ecf-3d78-b545-d653874e0e26 | -17.284 | -42.6479 | 2025-05-28 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 209.8 |
| b350618e-6b3e-3c38-8a53-97c823873794 | -11.818 | -44.2703 | 2025-05-28 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 1fe4c10c-c724-39a2-9a82-f3b8de81d235 | -16.4143 | -49.9158 | 2025-05-28 00:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1024d54b-102c-362c-8b73-bed2649f1804 | -11.4062 | -44.82 | 2025-05-28 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| e5408687-63a7-372d-9d0f-d1b404c6a6dc | -6.2226 | -43.3459 | 2025-05-28 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| e13ca770-6dd6-339c-b7a1-7d4b81c58169 | -17.284 | -42.6479 | 2025-05-28 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 196.7 |
| c7f8f331-da23-36eb-8212-c479ac95ac95 | -6.2038 | -43.3475 | 2025-05-28 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ab8addb6-3d5d-3cbb-8667-44ae735abab9 | -10.235 | -52.2263 | 2025-05-28 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| a1745128-e601-3e5d-98bc-21f875186133 | -10.2348 | -52.2472 | 2025-05-28 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 38ed37f5-d8be-3047-be7e-a1e87de9a931 | -7.6762 | -46.0995 | 2025-05-28 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1d5f28cd-e3a1-30f7-b5ee-086fe948e99c | -17.2639 | -42.6527 | 2025-05-28 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 192851b0-d2ee-35d4-8a97-e0c0f0a44af0 | -17.3041 | -42.643 | 2025-05-28 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1bc0eb24-4fc8-391c-afa5-155ee4cf109b | -10.2539 | -52.2246 | 2025-05-28 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 9e5b079f-20f8-35f3-a553-cef1a0a88066 | -11.818 | -44.2703 | 2025-05-28 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 5cd9b4bf-9448-38c2-abde-c74c3d7c0e68 | -7.2025 | -43.1171 | 2025-05-28 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 0ef517ec-0f6f-392f-9c94-b4b9a1e200c4 | -17.2639 | -42.6527 | 2025-05-28 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.3 |
| cf582963-3058-3b26-9096-eb342244caee | -6.2226 | -43.3459 | 2025-05-28 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 642baceb-47e9-3e55-99cc-4c000de05d37 | -17.284 | -42.6479 | 2025-05-28 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 5636ddee-48d2-353d-b699-52951d69cd76 | -10.2539 | -52.2246 | 2025-05-28 00:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f37724e6-65e3-37e8-b94d-4ef55145c2c2 | -6.2038 | -43.3475 | 2025-05-28 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 1fc1b079-3ce1-387a-9e4d-00e9456f5d20 | -7.6762 | -46.0995 | 2025-05-28 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f84524ec-e1bf-3fda-9704-403c33e72a2a | -11.818 | -44.2703 | 2025-05-28 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 644912c7-83cb-3323-b895-dd64ef73d581 | -7.2025 | -43.1171 | 2025-05-28 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 6fca1728-cb76-306e-bcc3-e4617a1c8447 | -11.4062 | -44.82 | 2025-05-28 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 48c49466-5282-37ae-93e9-f60f80ebd374 | -10.235 | -52.2263 | 2025-05-28 00:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 36523b85-47e0-3fbd-92d3-6774c2c7ab63 | -10.2539 | -52.2246 | 2025-05-28 01:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 3af3e4ad-d45c-31f1-95fb-e7f816a9e621 | -11.4062 | -44.82 | 2025-05-28 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 302005cb-3c60-3488-91a0-24b69532e124 | -7.6762 | -46.0995 | 2025-05-28 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 43f2421d-b012-3747-9b11-666941b7e514 | -9.4387 | -40.3419 | 2025-05-28 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.5 |
| fc3e5da9-c663-3fde-b722-b8fa4a2e3f14 | -7.1837 | -43.1189 | 2025-05-28 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 6b66e868-4ad0-34ec-9c43-87b14425498a | -17.284 | -42.6479 | 2025-05-28 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 204.5 |
| b9fdbe91-d720-3e40-97bc-3386cd5dcb6c | -11.8373 | -44.2674 | 2025-05-28 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| a47f3a6e-e020-35bb-b4d2-feb4262534dc | -10.235 | -52.2263 | 2025-05-28 01:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| d98240ea-b240-36f2-93ca-97f261988025 | -9.4196 | -40.3447 | 2025-05-28 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 107.4 |
| 5b6e7aac-2dbd-35f3-9fd6-d537a2d32e41 | -11.8176 | -44.2938 | 2025-05-28 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 1433c0dc-5c1e-3170-85d1-3dddd5bb108a | -7.2025 | -43.1171 | 2025-05-28 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 55a27dde-a7f5-3a91-b855-33be0fac1e43 | -11.818 | -44.2703 | 2025-05-28 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| b494effa-8f9e-37bc-ad65-40bd0a538c56 | -11.387 | -44.8227 | 2025-05-28 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 6f47d6c0-1e53-3dbb-968f-53a9e832fc15 | -10.2539 | -52.2246 | 2025-05-28 01:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c44dc998-b95a-359d-a444-2aea462019c8 | -9.4196 | -40.3447 | 2025-05-28 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.5 |
| ac5972c1-6c0c-3b85-a3a3-e1512cb5750c | -7.2025 | -43.1171 | 2025-05-28 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 7faa3f99-3875-32a2-b4a1-0337325f7640 | -10.235 | -52.2263 | 2025-05-28 01:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 53ed21a7-ab46-31d5-adad-44e7a55bd78c | -17.2847 | -42.623 | 2025-05-28 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 68.1 |
| fe729d56-510e-3365-ac9e-f9bbeb9dbbf9 | -17.284 | -42.6479 | 2025-05-28 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 1f8b6331-2767-3df1-ab99-bd0b054de528 | -11.4062 | -44.82 | 2025-05-28 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| ae8fb85f-29cb-36d4-ad3f-876db274028f | -7.6762 | -46.0995 | 2025-05-28 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 5ff56888-e105-3eba-9052-5d1ed66243b0 | -11.818 | -44.2703 | 2025-05-28 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| ce4ad8b6-d5cd-3ee5-a1af-0f6c6502287a | -7.6762 | -46.0995 | 2025-05-28 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 5aa76333-e04c-3e3c-ab08-50886d09770f | -10.2539 | -52.2246 | 2025-05-28 01:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ac55961f-7b3d-30a2-8bf5-083147f9b905 | -10.235 | -52.2263 | 2025-05-28 01:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 7842ca03-b30f-3a9b-b02b-58a1ee25a4e1 | -11.4062 | -44.82 | 2025-05-28 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| d29c1b5d-5a3c-3b41-99c4-1eaed67bfb95 | -9.4383 | -40.3668 | 2025-05-28 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.2 |
| f768a251-0002-303a-b000-c6f9a4c85254 | -7.2025 | -43.1171 | 2025-05-28 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| e87e14d0-6cd9-3475-8e5c-3da3149557a6 | -9.4196 | -40.3447 | 2025-05-28 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 114.9 |
| d0c122b5-f64c-36eb-9754-3d21a9401a16 | -9.4192 | -40.3695 | 2025-05-28 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.2 |
| c37f5d5d-1920-36a5-8799-52c47a14e1d3 | -17.2639 | -42.6527 | 2025-05-28 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 67.2 |


[Clique aqui para ver as próximas entradas](README3.md)
