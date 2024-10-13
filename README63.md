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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5293a4f0-8f51-3fdc-bb20-954782277886 | -6.23744 | -47.39305 | 2024-10-13 04:40:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be29b575-e7ec-37d3-83c5-78542736b7fb | -6.17436 | -46.75092 | 2024-10-13 04:40:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f58e06f7-5a88-3dac-92fc-625e3ed3c1d2 | -6.17376 | -46.75483 | 2024-10-13 04:40:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ceebffc6-ad7b-3020-9ba9-b1235438fa3f | -6.13616 | -47.27478 | 2024-10-13 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d38ab23-f797-3821-89ec-539fa69eac15 | -6.13559 | -47.27853 | 2024-10-13 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 14989390-e03f-310e-8fea-228bd480f77d | -6.13272 | -47.27424 | 2024-10-13 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c5cc3e0e-e43f-30a8-90b1-dc6b7fd44f36 | -6.13216 | -47.27799 | 2024-10-13 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f4f7876c-883c-3ddb-9571-68a134c46dc8 | -6.12934 | -47.27459 | 2024-10-13 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 162a8bef-e8bf-3de5-a21b-4c5e4619fc9a | -6.12929 | -47.2737 | 2024-10-13 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 721617f5-a6f9-332f-9985-4a82aa6c7934 | -6.12876 | -47.27834 | 2024-10-13 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccd98c53-7eb4-3181-acb7-05f816f725a5 | -6.12872 | -47.27745 | 2024-10-13 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bf549c03-f7a9-397b-a4b4-d28e66200b7b | -6.80525 | -47.05444 | 2024-10-13 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6b72eb7-c38e-3c00-a71b-40986a05a06a | -6.74112 | -48.1751 | 2024-10-13 04:40:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a5826e2-982d-3321-b72f-2c11e82d394c | -6.74057 | -48.17865 | 2024-10-13 04:40:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46cb4b1c-31c1-3d1b-a64f-067ec56be511 | -6.70869 | -46.95224 | 2024-10-13 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f70af50-b577-37a2-b000-e8b95e62a6dc | -6.68656 | -47.36836 | 2024-10-13 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dd5c54c-0e2f-346d-b2d8-adbb2e5c52ac | -7.67681 | -47.31083 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4e4fc1d5-35a2-3798-9337-5cf22eae913f | -7.67623 | -47.3147 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 2642ef23-8367-31d3-8cda-9166d5aba5e0 | -7.67565 | -47.31857 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| dc63a657-7e8a-3e03-bb91-80530ab8c05d | -7.67333 | -47.31028 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6a74eb70-393c-31e9-ad77-90a16b9dfab8 | -7.67275 | -47.31416 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| a7c05319-3eae-3266-a378-16bd52063d14 | -7.6727 | -48.17045 | 2024-10-13 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38cd1e1c-b917-39fd-a2be-a3276eca47ba | -7.67217 | -47.31802 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| a8346768-47a2-353a-91d4-42f4d159fc11 | -7.67159 | -47.32189 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ddeb64e9-4dcb-3d43-a59a-172d189a464e | -7.66928 | -47.31361 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4e7bfe7a-1f9d-36cd-af09-ed3d10aafc2b | -7.66869 | -47.31748 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ea929f7c-8420-3595-8d7d-a86176a227a4 | -7.66522 | -47.31694 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6ca8d0fd-59d9-3db3-9aaf-9c8a1b445f0f | -7.66464 | -47.3208 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23e8a764-a4c1-35d1-a0b0-c8f1d529967a | -7.60474 | -47.74271 | 2024-10-13 04:40:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7b44775f-c646-3822-beb2-5ed33ee61017 | -7.57337 | -47.37028 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 218fd5b8-a2d0-30f4-bc67-06c60fdb7446 | -7.56991 | -47.36975 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 905d2cf4-e749-3696-bfa4-ed0141d8d08e | -7.52985 | -47.95462 | 2024-10-13 04:40:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fc2401f-b3be-3c59-b2ab-984b96e1f1c8 | -7.47038 | -46.99375 | 2024-10-13 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cc7f12d-05a2-36c4-b4aa-207ef86833a6 | -7.45726 | -47.55955 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05f7d03a-1644-3fd6-af43-9a9cab1d4438 | -7.43211 | -47.86094 | 2024-10-13 04:40:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1e3cffd-fe37-31b4-93e9-806e268ba729 | -7.42719 | -47.32217 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f20ab3e7-deb2-355e-83d7-f00bcf4c0e71 | -7.4261 | -47.32098 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35315d4b-6033-3974-bc56-d6bc4671e765 | -7.38449 | -47.25265 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 86bd575e-e5de-3ea5-8e26-d92ed39cfe07 | -7.3839 | -47.25652 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6095cd93-2796-3d85-9580-3f4ee030c496 | -7.38159 | -47.24825 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 41276a3b-cb27-34eb-95d5-99c078367809 | -7.38101 | -47.25213 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d8155339-8503-38a8-929c-567728472472 | -7.38042 | -47.256 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6ad0c3f9-fa63-3a68-91e7-d297438b0cd6 | -7.37812 | -47.24771 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 563ea3f6-ea9c-32ce-a95e-e7472640360f | -7.37753 | -47.2516 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 2722ff47-6ec3-31eb-853d-035b80248998 | -7.37694 | -47.25547 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2589da97-b8ec-3cd7-b76f-4b8d9fd59811 | -7.32328 | -47.44692 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4c39900-cfe8-3042-ac44-5fdf8a3799cd | -7.23375 | -47.64512 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0156f48-3594-3bb1-bf2b-2928d91ba3a5 | -7.18826 | -47.39256 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d69e065f-fafb-3c34-9fd0-22e734a6dc47 | -7.13873 | -47.60069 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3072975f-2658-3972-85d7-2b52b0b41c6f | -7.13531 | -47.60015 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cd70097b-5ac3-31c6-aca2-96698f56f24c | -7.10399 | -47.84948 | 2024-10-13 04:40:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fda57a84-5321-3cd9-ba42-4ad8d59617d6 | -7.095 | -46.98812 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2f626c4-2652-3c95-915e-fdd7dd9c1486 | -7.02254 | -46.81941 | 2024-10-13 04:40:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6121df55-8184-39b5-98b4-2ebb683ab8e6 | -7.01901 | -46.81885 | 2024-10-13 04:40:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56539a21-c7ce-3b23-8288-5a1806e0df60 | -7.01609 | -46.81429 | 2024-10-13 04:40:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 755e03b1-06a6-374f-9bcd-87a19f3b7870 | -7.016 | -46.8388 | 2024-10-13 04:40:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d35d5308-1d0b-39b4-8abe-b6d8f7d2ea1e | -7.01427 | -48.31953 | 2024-10-13 04:40:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64981615-de90-3cfb-b47a-7b8c99412562 | -6.99281 | -47.33641 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 367daddb-85fd-3a17-b3ac-33cf96019053 | -6.99224 | -47.34023 | 2024-10-13 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d92dcd8-a95f-3899-b981-ce21bd6c5434 | -6.93009 | -48.16053 | 2024-10-13 04:40:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c559e39a-c254-3017-8bb7-87e123ed022d | -6.92954 | -48.16411 | 2024-10-13 04:40:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a23ac4c9-36da-360d-8457-d9a6f3eb9c83 | -9.21005 | -47.56125 | 2024-10-13 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eaa3c1ae-6e62-3023-8669-2bdcd6d3c02a | -9.16463 | -47.6023 | 2024-10-13 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 509d3397-1b95-3f57-a214-a3c731a3c573 | -9.16115 | -47.60175 | 2024-10-13 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55753c73-5add-3a8c-b3c9-48fa3ca87627 | -9.09992 | -47.75087 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8bede6ed-00a8-3aa9-9cc1-e8f5a49f41de | -9.09735 | -47.75148 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf5a158a-6289-3de7-9858-87f86ff48671 | -9.09218 | -47.73893 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03040884-c497-34f1-8147-fe6448171d20 | -9.03389 | -47.67858 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b56414fc-1e98-3e50-a5a4-752adf5a3c85 | -9.03042 | -47.67805 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8a0def5-f272-3f53-84f5-a1ac3f3f9a15 | -8.91167 | -47.91058 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3051a6d-6ed8-3ce4-9d7a-2b5b3be8b6b1 | -8.9111 | -47.91436 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5db0d52-c044-39eb-b6a2-623a066fb3c0 | -8.85626 | -47.95223 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2b38875-8ad7-358d-ad86-ab04a81f077e | -8.85283 | -47.95168 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3229370a-591b-3f31-862e-ea44ee2afdb5 | -8.85282 | -47.95186 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04831fb4-25a3-337a-9376-c584fc9fbd59 | -8.85227 | -47.95543 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7170779d-9f1e-3ea5-888f-eda8f0a904b4 | -8.85225 | -47.9556 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fab2441-d339-3bfa-a275-815f5cbefaae | -8.83913 | -47.92663 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c53749e-9c6a-367e-947b-d26e5b893e8c | -8.75829 | -47.721 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e7817ac-2c6a-3727-b5c9-023ec86a6ec1 | -8.53207 | -47.25783 | 2024-10-13 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5e9f0436-9729-32c6-a110-4eece96d9065 | -8.44555 | -47.22974 | 2024-10-13 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e0e64d1-130c-3518-bb06-1b12999b85b2 | -7.9293 | -48.42388 | 2024-10-13 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63d3bf8e-c30d-3473-b082-4e501b516f76 | -9.20466 | -48.68635 | 2024-10-13 04:40:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acaf8f60-d1e4-337b-85a4-df428572c247 | -8.78559 | -48.58167 | 2024-10-13 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f99a9cc7-4b47-3e6c-955e-14099a50808a | -8.78504 | -48.58531 | 2024-10-13 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d6c8aad3-0c63-3f12-947b-85b76c4e497c | -8.46028 | -48.6198 | 2024-10-13 04:40:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95145a42-1a16-3318-835c-44977a892276 | -8.45693 | -48.61929 | 2024-10-13 04:40:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a67d0ab-0002-38a2-a5c4-ec4d5045170f | -8.45358 | -48.61877 | 2024-10-13 04:40:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3553f8c3-a5d2-3a7f-aa9f-a0e74ca96570 | -10.32327 | -48.79867 | 2024-10-13 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0eeb347c-4f43-3f0c-9bfc-9ab51f15a7a4 | -10.30144 | -47.91885 | 2024-10-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccbd6926-03a3-3484-9c6a-1358096e9eca | -10.25781 | -48.55962 | 2024-10-13 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fc0e375-797c-39ad-9e57-b3bacd53a78c | -10.23391 | -48.93321 | 2024-10-13 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b38afb6-d315-3808-94ae-bad3191ae4a9 | -10.23336 | -48.93682 | 2024-10-13 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dbf8aaa-4c94-3f11-adaa-9b495e054a42 | -10.16707 | -48.04522 | 2024-10-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7b6857a-9176-3b8c-a959-4aa6e47a9dd0 | -10.16419 | -48.0646 | 2024-10-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8f1e011-d1ad-3ef8-a848-1c9691e4b250 | -10.11856 | -48.71467 | 2024-10-13 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf2ec847-798a-3da4-a085-10dddca78cdb | -10.08653 | -48.18648 | 2024-10-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 269cbbbe-8c27-3595-bd99-e344c56d20b0 | -10.01003 | -48.22875 | 2024-10-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa8432f0-d4c0-3918-9bce-8856b5a20465 | -9.98326 | -47.96336 | 2024-10-13 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95d888e5-0ffb-347e-ad22-78fced2b620a | -9.98269 | -47.96717 | 2024-10-13 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10a217e1-3871-31cb-80ea-79c20ce6fc08 | -9.93756 | -47.92119 | 2024-10-13 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README64.md)
