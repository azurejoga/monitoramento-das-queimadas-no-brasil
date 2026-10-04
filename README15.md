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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bc643ee-7af5-3e2c-8466-1fb13574927a | -2.21471 | -53.71215 | 2026-10-04 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| b3366f02-50c7-324f-9913-6a835326260c | 1.91361 | -55.76247 | 2026-10-04 00:39:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 2063a4a4-1e58-3e64-a7e8-cca4826dc234 | -2.77253 | -57.00744 | 2026-10-04 00:39:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7322906a-85b7-37d0-b789-0c77c3647835 | 1.90778 | -55.79816 | 2026-10-04 00:39:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bf3211d1-2865-3689-96bf-5acdfd24c230 | -3.51334 | -59.81295 | 2026-10-04 00:39:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f738c9f1-8ba1-3a3e-a2de-456b9e8b277c | 2.01408 | -61.08828 | 2026-10-04 00:39:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7683aa03-ca0a-3d23-a5a9-7e5943b6542c | 1.91377 | -55.75265 | 2026-10-04 00:39:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| af941b81-44d4-35e7-8882-15e02444aae8 | -3.18947 | -57.8661 | 2026-10-04 00:39:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 233f212b-fac5-3a94-bcf2-0e454945d9ab | -2.53227 | -58.03722 | 2026-10-04 00:39:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a74325be-1ea2-3525-be96-5ba03f68eb00 | 4.16806 | -60.38105 | 2026-10-04 00:39:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2d17504d-e906-3e84-9b0d-ede39895aa42 | -1.0941 | -54.12667 | 2026-10-04 00:39:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 9cd88cbe-6766-3dca-a931-da7b07a334d8 | 1.75924 | -55.63531 | 2026-10-04 00:39:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| a26a6c6c-b1b6-38c3-baba-b07c3d3146f6 | -2.68637 | -54.42403 | 2026-10-04 00:39:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| ed8e9d07-5b98-32b6-86b5-b070b2c875ac | -2.68876 | -54.44041 | 2026-10-04 00:39:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 34c35276-9dd7-3b4f-bcd3-335337879ba6 | 4.15919 | -60.3798 | 2026-10-04 00:39:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| aa4aecc1-dd7f-3688-a96c-c4c773bf470a | -2.5843 | -51.8417 | 2026-10-04 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 93d429b8-a438-39e7-8d2b-f56c87432f3c | -3.0548 | -54.2277 | 2026-10-04 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 025d58cd-14af-34e6-8a29-9c08cc093743 | -3.1299 | -53.7431 | 2026-10-04 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| adcfd764-98b4-3f57-a780-62cee5c60f4c | -4.2745 | -46.3624 | 2026-10-04 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a06ee9a9-a559-3749-9106-e53251584b10 | -4.2886 | -50.2886 | 2026-10-04 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| b93f5a44-3ea4-30f1-9225-1dc26241557a | -3.514 | -59.8065 | 2026-10-04 00:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 137c6795-32c7-3cdc-af0f-b9be02ac561a | -2.5658 | -51.8628 | 2026-10-04 00:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 8627658c-a6de-3a03-ae91-39ae241277b9 | -3.756 | -49.5499 | 2026-10-04 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 841188c9-3115-30b3-a40d-a61020287cd3 | -2.8163 | -54.1129 | 2026-10-04 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 589f7496-5b5d-379b-8d46-688f92fd9d05 | -2.8164 | -54.0929 | 2026-10-04 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 28be0e14-d9df-35e2-a8f0-f8b629216e36 | -4.2887 | -50.2675 | 2026-10-04 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 258.4 |
| a07914b6-427c-3b44-b2ac-ec63cf2d8907 | -4.2744 | -46.3846 | 2026-10-04 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| fec6ea31-b168-3427-be66-0567afcd759d | -3.13 | -53.7229 | 2026-10-04 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| f5ff9dae-0770-3c4a-9dcb-9cd9ce138f71 | -3.072 | -49.5525 | 2026-10-04 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 2cd90092-335e-31b4-8edc-a0fb85f206ae | -8.5551 | -67.0686 | 2026-10-04 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| fdeef960-871d-3781-9da1-d94dd28c6d66 | -3.5128 | -54.6162 | 2026-10-04 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| c1d34b44-f29e-3e77-9301-550e86efdb5b | -3.1838 | -54.104 | 2026-10-04 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 04fab942-2aab-3178-b072-6e15cfd39d34 | -3.0721 | -49.5313 | 2026-10-04 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 7547563c-6277-37eb-a4a4-c5bd698508ee | -2.5842 | -51.8829 | 2026-10-04 00:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 6a9e8197-d7f5-3ce3-a59c-4d3d009d02db | -2.2113 | -53.7029 | 2026-10-04 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| aeb3d710-28e6-30b1-b169-29f7b23ebe9a | -4.2558 | -46.3855 | 2026-10-04 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 20be2e61-2c1a-3ffc-b282-150b1c7c0f24 | -3.1115 | -53.7637 | 2026-10-04 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 03006e3f-6819-3ebd-a4ea-a782b10cd835 | -3.4761 | -50.1094 | 2026-10-04 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| b4397b79-fe4b-3337-84eb-95b586d9ebbb | -8.3526 | -62.8302 | 2026-10-04 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 70eccec2-2ac1-393e-a192-f47a84b99d79 | -9.0857 | -61.1629 | 2026-10-04 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e89e98cf-f6d5-3abf-a53f-b9d80239c7be | -2.2297 | -53.7026 | 2026-10-04 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 2813245e-f5f7-3ff5-8c0d-d8f3591804f8 | -2.8163 | -54.133 | 2026-10-04 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 39728450-c48e-3d2c-a898-7ebdcbcea7cd | -3.4762 | -50.0883 | 2026-10-04 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 8994de75-9a87-3470-8186-4a24b05bbcfc | -2.7979 | -54.1134 | 2026-10-04 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 03d5d659-d0c0-3ee1-96f4-895bcf4b98f8 | -2.798 | -54.0933 | 2026-10-04 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| e0592918-d41f-3843-ae5f-849389aec23a | -4.2888 | -50.2465 | 2026-10-04 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| a0a3b0d8-54f3-3e6b-baa2-fa3cb30f9f5d | -3.4577 | -50.089 | 2026-10-04 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 462f0118-fafb-3daa-94a2-606f7f7c9b44 | -7.7551 | -49.2067 | 2026-10-04 00:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b6ea5780-a51c-3774-9702-f08d3ce58a0a | -3.7559 | -49.5711 | 2026-10-04 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0661265e-f2f4-3fc0-8629-97a309a06370 | -3.2951 | -53.8395 | 2026-10-04 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 1b278e33-1ccf-3ba9-8771-25b29b72453e | -2.5842 | -51.8623 | 2026-10-04 00:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 8e891b2d-c6e3-30e9-8390-7793efc453d7 | -8.593 | -66.8081 | 2026-10-04 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 3cc1fcac-f95a-3cd9-978d-d29765315ac7 | 1.767 | -55.6451 | 2026-10-04 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5181f580-8ec2-3a3a-8ef9-a281ab9b14ec | -3.1116 | -53.7234 | 2026-10-04 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 245.6 |
| 0dcca4f6-c2f4-392d-8ca8-c453509a1585 | -5.8642 | -55.7071 | 2026-10-04 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f04f2cc8-bc12-372d-ac62-9c7aff2000af | -4.2702 | -50.2683 | 2026-10-04 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 759bb459-a681-32f7-aaeb-50ce83315cba | -4.4845 | -45.5478 | 2026-10-04 00:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 30a972b8-8a89-30b1-929a-0f2422920810 | -4.2559 | -46.3633 | 2026-10-04 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 9ce4bcb5-c872-3b59-8ae3-9c81e9775dff | -4.7434 | -43.2679 | 2026-10-04 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| a7cc71f8-bc65-3a61-be7b-472a83c5fc51 | -3.0364 | -54.2282 | 2026-10-04 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a7f39f23-7548-3750-96cc-abbc7bdd6545 | -3.1116 | -53.7436 | 2026-10-04 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 287.1 |
| dec6ed6d-de7e-33c6-9069-8076db8f2b03 | -3.1839 | -54.0839 | 2026-10-04 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4546606a-2ad7-3f57-a2c7-b392a3b5b82d | -2.5843 | -51.8417 | 2026-10-04 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d15a4103-3a5c-3ffd-b088-91d07913d5f0 | -3.1299 | -53.7431 | 2026-10-04 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 8f242f21-5991-3a1a-8ef7-e02f8787ed70 | -3.2951 | -53.8395 | 2026-10-04 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0fa018bc-c129-3819-b351-4ef6014ff465 | -2.8163 | -54.133 | 2026-10-04 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 1608d8d8-be9c-3931-a22d-5a42fc9d30ed | -3.756 | -49.5499 | 2026-10-04 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 25db180a-27d6-3879-b203-737d86dc2007 | -3.5128 | -54.6162 | 2026-10-04 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c88b6e89-2d23-3fcf-a0e4-ea7c7b912bee | -2.6026 | -51.8619 | 2026-10-04 00:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 18d3b883-9c24-32ee-93a5-ea89585938c2 | -8.5551 | -67.0686 | 2026-10-04 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| dc364299-0398-3572-b736-80d6e92f2098 | -2.5842 | -51.8623 | 2026-10-04 00:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 144.0 |
| a32a3a13-3455-3f72-a5be-fc26ad370de0 | -3.4762 | -50.0883 | 2026-10-04 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| e4e4d10d-6ff1-3b38-b01e-88d814bf73b0 | -4.2888 | -50.2465 | 2026-10-04 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2648bd1f-61a3-3f08-add1-831a06d53755 | -4.2558 | -46.3855 | 2026-10-04 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 105.9 |
| ba63aae1-3088-3ea9-a50e-1f6dd94f045c | -4.2745 | -46.3624 | 2026-10-04 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 128.5 |
| a3b979a5-d325-3425-ab4d-eaa67b1d6b84 | -3.1116 | -53.7436 | 2026-10-04 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 275.9 |
| 6927a29d-651c-38b8-96bf-d516130af85a | -2.8164 | -54.0929 | 2026-10-04 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 579fcb4c-e73d-37ae-8a8d-319ec981dfd4 | -3.1839 | -54.0839 | 2026-10-04 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 23d942ba-1eab-3356-a6f6-9566a064191b | -3.8756 | -55.8184 | 2026-10-04 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2a6904ab-da1d-3534-b8a4-fb3b6da8e811 | -2.798 | -54.0933 | 2026-10-04 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 7a929cc7-f214-3ff7-9f7b-9bf63937ad5f | -4.2887 | -50.2675 | 2026-10-04 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 252.8 |
| cbca2825-fe1b-32bd-8b65-921438dfed1e | -3.13 | -53.7229 | 2026-10-04 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 157.6 |
| 45037e55-db9b-37d4-b5f0-39c063a8b95f | -2.2297 | -53.7026 | 2026-10-04 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 908c7fc2-fcc8-3850-9a79-6a38d818c949 | -4.2886 | -50.2886 | 2026-10-04 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| cce5ab5f-967d-35e6-b326-96630049479a | -3.0548 | -54.2277 | 2026-10-04 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2dc004d6-3c60-33c0-a3f3-47523b657ca5 | -8.593 | -66.8081 | 2026-10-04 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 23decb8c-c5e8-3b27-aad1-af86f4fbdb9f | -1.0911 | -54.1001 | 2026-10-04 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f910d6df-c340-35b8-9920-364b9f848ce6 | -2.5842 | -51.8829 | 2026-10-04 00:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 31bcbc57-7bdb-3676-aca4-2b19f8645370 | -3.1115 | -53.7637 | 2026-10-04 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 408e41e2-f638-35c3-a3f0-2db025c35e64 | -2.7979 | -54.1134 | 2026-10-04 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 7f528e1b-0c84-3922-b54d-a59011bef624 | -4.2559 | -46.3633 | 2026-10-04 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 1c6204e3-b2f0-381e-93cb-be9e4017a663 | -4.2702 | -50.2683 | 2026-10-04 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b6eb2a3e-6827-3b34-9839-4158e3a9b2e2 | -3.7559 | -49.5711 | 2026-10-04 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| c99d8318-0f5c-357a-9191-574287358fe2 | -3.1116 | -53.7234 | 2026-10-04 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 275.1 |
| 72c86af4-f08a-3316-ba93-6573ceaf353d | -3.072 | -49.5525 | 2026-10-04 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 06a2a0ac-e8d7-39b6-a824-f2908e9940b8 | -3.8757 | -55.7986 | 2026-10-04 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8a785529-f0b9-36a8-841c-3067c55285b2 | -9.0857 | -61.1629 | 2026-10-04 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 53b1c49e-6fe0-305b-b8ca-a282efedf0f9 | -3.4761 | -50.1094 | 2026-10-04 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 42c6dada-6f37-317c-8f22-46cd52cfb7d3 | -2.8163 | -54.1129 | 2026-10-04 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 46336e2f-95b0-3a53-8891-4ae548670c2f | -4.2744 | -46.3846 | 2026-10-04 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |


[Clique aqui para ver as próximas entradas](README16.md)
