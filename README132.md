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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 920f751b-5691-3b05-a26b-3e3a31b4ecc2 | -4.21223 | -56.35058 | 2026-09-23 12:23:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3d418757-efb0-3113-b14e-31b60b349e36 | -3.68654 | -60.59021 | 2026-09-23 12:23:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| f37c8566-3bf5-3897-bd5d-a55126347e2a | -3.89883 | -60.58763 | 2026-09-23 12:23:00 | TERRA_M-T | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7ae8f70d-389a-3783-a731-6aa6817242da | -4.06443 | -56.21903 | 2026-09-23 12:23:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a543224d-a9be-3b09-b2b8-743d7fb328a7 | -6.10658 | -57.67512 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1432079c-f30d-3adb-bbaf-369180c71ec1 | -4.42817 | -55.07717 | 2026-09-23 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b92af453-3d77-3e9c-8654-0ba6cacb2979 | -6.19342 | -57.77529 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6e70dd35-ea6a-37e3-911e-5797f8762461 | -6.29957 | -57.74198 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 76f0d459-9c5a-3cdc-8db4-76409fff5f42 | -6.17987 | -52.79956 | 2026-09-23 12:23:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 11846aed-f859-33b6-af64-747f2ae5749a | -6.35112 | -57.77373 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 09ac4a18-1f1c-3bae-b952-af1e1a049c4e | -5.87499 | -52.06584 | 2026-09-23 12:23:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9fedd2de-8573-36dc-b01f-49ff304c5695 | -3.68678 | -60.55778 | 2026-09-23 12:23:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 97eb0ee4-d747-30d2-9e39-43b67311d5d2 | -7.54177 | -61.4986 | 2026-09-23 12:23:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| baa3885f-be12-37d8-8e94-04808ddd5796 | -7.12478 | -56.54801 | 2026-09-23 12:23:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c4841203-135c-3aff-9ef8-32ff84e81768 | -2.8601 | -57.79271 | 2026-09-23 12:23:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 92949177-f0e3-33ce-ab57-c20bdc090580 | -7.78443 | -50.23389 | 2026-09-23 12:23:00 | TERRA_M-T | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 6ddd42ff-f8ec-339d-933a-0c51d9c50719 | -6.62933 | -59.99293 | 2026-09-23 12:23:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6b58831b-0497-3f2a-bcf6-b9dd3d4be39b | -6.18552 | -52.05095 | 2026-09-23 12:23:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b6933e3d-3f0c-3472-964f-d1a3305ab389 | -6.13403 | -57.74882 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 875e195d-573d-371b-a905-ac639d5fb01a | -8.18566 | -61.18192 | 2026-09-23 12:23:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0373bb85-1eda-3795-a4e7-7cab2f788eb4 | -7.56518 | -57.67313 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4ba0673-48b6-3526-8623-304ddea7397f | -4.3384 | -55.65022 | 2026-09-23 12:23:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 120ee372-6c32-3e62-8204-7c18d58e77df | -8.79589 | -48.76517 | 2026-09-23 12:23:00 | TERRA_M-T | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 057ca5c9-4ced-3dce-82c9-ab9cb760ffbe | -3.76691 | -59.47504 | 2026-09-23 12:23:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 480c7e8e-22af-3233-8b54-49f88abd1025 | -3.72107 | -54.20284 | 2026-09-23 12:23:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e5261100-b9eb-3813-8f88-7c6906f67154 | -7.77769 | -50.22762 | 2026-09-23 12:23:00 | TERRA_M-T | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| d59f327c-33d7-3618-8c14-8028bf426cfa | -5.92621 | -59.91297 | 2026-09-23 12:23:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 8679a75f-49f2-3efc-bd33-c178a90f3499 | -3.90546 | -55.83506 | 2026-09-23 12:23:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 637aebf3-1a6a-3762-a6cd-2d949b5cdd1a | -7.02486 | -62.93155 | 2026-09-23 12:23:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f026be1a-1937-3e07-a435-3a40e80b8e6e | -5.01335 | -56.09535 | 2026-09-23 12:23:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7b3aad98-1da7-3827-b48d-680c5ef08fbd | -6.08644 | -57.62714 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ad16e11c-6205-322b-9656-bd9783272e69 | -6.64151 | -59.93515 | 2026-09-23 12:23:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| ebab0e42-bc17-3e83-a377-6e26398534f7 | -6.82817 | -47.8627 | 2026-09-23 12:23:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 6a5f9e35-7264-33bf-81eb-7bf794ecf56a | -3.16155 | -57.68516 | 2026-09-23 12:23:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2afcdd44-d43d-3abe-86e1-30ec55499686 | -5.98267 | -55.36546 | 2026-09-23 12:23:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 493eb276-a9c7-3ea9-a974-0fc55fc08c39 | -5.74566 | -53.46272 | 2026-09-23 12:23:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| e88d97fc-6b2f-343c-8744-cd3baf0323ed | -4.96811 | -55.82653 | 2026-09-23 12:23:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 14e17e4c-7145-3e62-b8e1-3eceb97389f3 | -4.01266 | -52.08823 | 2026-09-23 12:23:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 4da8bfb7-8f10-399c-a672-c3d8e2f36ad7 | -7.69901 | -61.53481 | 2026-09-23 12:23:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0c7a6b83-cfdc-3b3b-8c17-685be59f6380 | -4.06318 | -56.22786 | 2026-09-23 12:23:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 33c6dad9-537d-3126-b10c-b6a68781bf95 | -3.84973 | -58.67384 | 2026-09-23 12:23:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 2691d3d8-9c1d-3be5-98ae-4bf5641ebc8a | -8.18383 | -61.1941 | 2026-09-23 12:23:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e97c8fc3-f36c-3286-bdf4-5f8465625530 | -6.7376 | -59.42297 | 2026-09-23 12:23:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1ed92e8c-6cd1-3432-b226-52c9313b8081 | -6.43656 | -55.60918 | 2026-09-23 12:23:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 832cd238-14df-33d8-a75a-528b4cd76c16 | -7.78726 | -50.21057 | 2026-09-23 12:23:00 | TERRA_M-T | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 8d1678c7-6b86-3cbd-b4e3-f40cbff3371f | -6.43526 | -55.61861 | 2026-09-23 12:23:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5d538be6-bf09-34bb-b5f0-3e7f1fb3172a | -6.67107 | -58.56015 | 2026-09-23 12:23:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2b0a7ef8-fbf1-39a1-bda4-38d1ec1dd687 | -7.42948 | -49.8719 | 2026-09-23 12:23:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 3a535be0-9eb1-389b-9fa1-244d5f1c35e9 | -4.98242 | -56.96106 | 2026-09-23 12:23:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1377979b-1813-39e7-8a68-08d2699d4953 | -3.68486 | -60.57052 | 2026-09-23 12:23:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e86a031c-f230-3af3-bbec-ba2aca0ac11a | -6.61943 | -59.9258 | 2026-09-23 12:23:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 2204cade-8a2d-3ad6-8d13-e95a00110be9 | -3.40121 | -59.52057 | 2026-09-23 12:23:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| afef2697-8689-3ecf-af73-e0cb69adce1b | -6.008 | -57.71861 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 94e6d2ca-7b0b-3aca-8fb3-d576a8a0c689 | -6.61786 | -59.93651 | 2026-09-23 12:23:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| fc208f74-b034-3493-b814-6f3afcfd3328 | -6.61137 | -59.91374 | 2026-09-23 12:23:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| ef07bf7e-47e5-3ded-9548-9108bee8d8fd | -4.68397 | -55.62055 | 2026-09-23 12:23:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bce477f8-b600-34c5-b503-6855820de3e2 | -8.11847 | -48.23747 | 2026-09-23 12:23:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a24d24e4-d18f-371c-86b6-5a2ee14f5550 | -4.44779 | -55.07023 | 2026-09-23 12:23:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d8174bb6-b8cd-3a1f-9f95-30c0bdc13642 | -5.36403 | -56.03125 | 2026-09-23 12:23:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cec6c8c0-1cd5-3254-85c9-a9185ad94edc | -6.45772 | -54.99171 | 2026-09-23 12:23:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b39be9b8-2792-3b5c-bda4-09454a24ca57 | -3.72252 | -54.19242 | 2026-09-23 12:23:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 566acc3a-4af7-38ab-a9cb-ab5f45b6ab90 | -2.95261 | -57.72745 | 2026-09-23 12:23:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f8abdf8c-8927-389f-919c-f389ad85e4c4 | -4.98368 | -56.95229 | 2026-09-23 12:23:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 707c4e38-4b1c-377f-8b85-adc8d4065d32 | -6.64312 | -59.92449 | 2026-09-23 12:23:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 82d137f9-2284-3150-90db-ceb2db92d281 | -6.06968 | -57.80595 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9fde6465-fafa-315c-ad42-dacc36089ff7 | -3.95998 | -59.3513 | 2026-09-23 12:23:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 20ac9163-054d-3e82-966b-d66848022516 | -7.28496 | -56.46333 | 2026-09-23 12:23:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 89e35298-09f3-368d-b533-8a6133f100d0 | -7.87779 | -61.17952 | 2026-09-23 12:23:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 0c0e30e3-a3b5-37ef-b539-5e7967f5905a | -3.69204 | -60.55183 | 2026-09-23 12:23:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 79e2ea17-994c-3bd8-b93f-b6d2cc4bee08 | -7.1034 | -52.75428 | 2026-09-23 12:23:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1aac6fd7-2fc9-3392-9c00-f19d1c2b1fc2 | -6.13275 | -57.75769 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| ef1a2591-cfa1-3424-af4b-e88acffccfef | -3.16024 | -57.69426 | 2026-09-23 12:23:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a11b617c-ea8d-3e0c-bd7a-a648e03a55e5 | -8.49618 | -57.61412 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 669ee22c-0237-31fd-86b6-86eb16dc3901 | -8.23639 | -62.82816 | 2026-09-23 12:23:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 66ddf19f-4580-35f7-a960-775f4926749a | -3.85114 | -58.66404 | 2026-09-23 12:23:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 06fab361-a053-3a4f-beb9-f485929b03d3 | -9.60247 | -48.44474 | 2026-09-23 12:23:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 1237781f-bd8e-35e5-b276-2ea1e9f87027 | -6.18166 | -52.78589 | 2026-09-23 12:23:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| acaf03f0-a966-30a2-a489-482a02749656 | -3.82116 | -59.00592 | 2026-09-23 12:23:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2f17dda1-bd84-3909-8b41-4ad8fb3bb19f | -5.82119 | -57.73423 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 751310a3-4233-33f4-81ef-b0119079b2d7 | -2.86142 | -57.7835 | 2026-09-23 12:23:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| b352c341-5a1b-37fc-bb21-f8c3712c6e5b | -6.07097 | -57.79704 | 2026-09-23 12:23:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b0ec39d8-a06e-38af-a814-caea0fe7c0a4 | -3.65937 | -54.26055 | 2026-09-23 12:23:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 889ab137-d7b2-3f9e-9f9c-0e76c97bba78 | -3.68838 | -60.57738 | 2026-09-23 12:23:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 817d7d3a-91d4-3c22-9e25-d5f60c48bda3 | -6.60981 | -59.92439 | 2026-09-23 12:23:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 3655a91c-f1c4-325a-9c49-8b7898c9cad8 | -6.55294 | -56.02866 | 2026-09-23 12:23:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6622a5de-42ef-3305-8544-afa107534dd4 | -5.74402 | -53.47485 | 2026-09-23 12:23:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f6cf18c3-d4a3-3d25-ab27-686d90ea3443 | -8.23274 | -62.83347 | 2026-09-23 12:23:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 6879cfa1-6d77-32a3-bc20-15ecaec5e2bb | -9.54437 | -55.08755 | 2026-09-23 12:23:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 695c3ecd-5af8-381b-88f1-7d501e8aecfc | -5.73542 | -53.46136 | 2026-09-23 12:23:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9110c789-2a75-3204-966a-c13598e312df | -3.68293 | -60.58332 | 2026-09-23 12:23:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 09b77217-46d3-35ad-b695-ef467e89f761 | -4.0016 | -52.08665 | 2026-09-23 12:23:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| fadc306f-5bf6-3c19-b262-12567ce213f6 | -6.67872 | -58.57069 | 2026-09-23 12:23:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 0680be9f-8732-3281-aff4-cfcfc03ca808 | -3.69021 | -60.56458 | 2026-09-23 12:23:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| c4326886-33d9-3fc3-8d75-44cf843417b7 | -8.12632 | -48.24497 | 2026-09-23 12:23:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 203a7be2-5270-3e37-a084-9aaa9949b0c0 | -4.05067 | -56.31591 | 2026-09-23 12:23:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| af9ec1a3-5fb8-35a5-93f2-c62450de8bce | -6.04724 | -53.27053 | 2026-09-23 12:23:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1981f60e-022a-3d55-b5d9-bda782dc64e5 | -7.43246 | -49.84819 | 2026-09-23 12:23:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 7baa182d-4a13-3ef6-aba1-e9b5e51db0b0 | -7.10222 | -52.74787 | 2026-09-23 12:23:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b2b95f4b-4c79-3598-89dc-8c9779c1acea | -7.16212 | -52.81879 | 2026-09-23 12:23:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7f3bfdab-daf6-3675-af4d-02977288206b | -3.78926 | -55.87634 | 2026-09-23 12:23:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README133.md)
