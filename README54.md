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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc3b1507-3d82-3be7-aa31-9033eab17203 | -3.60674 | -48.92271 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bc7a10c9-f4ee-3dfc-8091-e1793bed3d04 | -6.30911 | -42.7526 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 99c0b67d-7905-3450-a3b6-5f235c996783 | -5.80997 | -44.4792 | 2024-11-09 04:33:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89a7a634-76a7-31e2-ada4-5b57fe8e4e77 | -3.29053 | -49.61872 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2dc6aac-71e3-3383-aff7-47f7463c5a80 | -4.75357 | -48.98107 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ed4fd5b-1226-3ad2-ba61-5f80a80d0320 | -3.47883 | -50.80747 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83726caa-3b65-33d7-acd1-ee8181cd9795 | -2.93389 | -51.05363 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e055109-ffc5-3409-a947-b28ebe655cc0 | -3.10857 | -51.1288 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3197179-bcfd-3130-a852-8928de4d1af0 | -2.95717 | -49.36964 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec428928-bb5b-337a-a324-39a5a74c996d | -4.20536 | -48.5536 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0458ca4-cd6e-338c-af80-44913c3eab39 | -4.04296 | -48.28748 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 548da45f-a319-3274-9f53-40bee87928b3 | -3.59147 | -50.24139 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8171cdd2-b740-3dab-9e8c-e2e4bab08903 | -4.77676 | -48.68307 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd515956-e373-3451-a4ec-b83650876aef | -3.65413 | -50.1436 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99ac3076-0ae1-303d-a8c0-b58395f945c0 | -5.44302 | -44.82294 | 2024-11-09 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62a25084-c106-308d-befc-f122721eea5f | -3.58857 | -50.23672 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dfc06fa-05fd-33de-9bfe-e70263bc487c | -2.8449 | -48.67927 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed87a81e-0e56-3f09-a2b6-aa1646036dac | -3.20936 | -46.50052 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 818f185a-90ab-3e9c-ba9d-c00b13a368b9 | -6.20528 | -42.07866 | 2024-11-09 04:33:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a387c309-4a38-382f-8de0-0b78676abc2d | -6.26944 | -41.6545 | 2024-11-09 04:33:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f3f1de30-c254-3385-9ba9-a26e342dab73 | -11.09372 | -43.33968 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 672a2a10-7104-36aa-a9ff-30f1e30f9852 | -4.2929 | -48.64642 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a989bbd-d4e3-313c-ad93-0733cea790d8 | -7.98628 | -46.74335 | 2024-11-09 04:33:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cf1526e-8fd9-3f35-bcd1-b0af8998123d | -3.35703 | -50.2557 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3bc8a29-2da8-3083-bcda-821b7cc90b81 | -4.46788 | -46.30353 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23772b71-65aa-3b45-acba-9520db729a6c | -3.03318 | -47.93684 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24d4b963-0565-305e-908d-42542912312e | -3.36393 | -53.3859 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69cd296b-c5fe-371f-89db-2cb8c7284d79 | -3.89302 | -46.43505 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a78211c0-3034-35d2-a4c4-85df4f439760 | -4.11936 | -46.88339 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4b25026-f514-328b-8d00-8351202f61c2 | -3.09127 | -51.11689 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b328dfad-b262-3cac-a525-a1ef2017d6b1 | -3.59479 | -47.34794 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 348f77ee-be02-3484-9f1e-e4d751e57bd7 | -4.90807 | -45.70645 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c3a8ec1-7f8e-3f49-b86b-55a19681b6c5 | -3.02902 | -50.35815 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f89d9ae-d19a-338d-82d5-496ab45b52a9 | -4.5887 | -48.53818 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76408dd9-9e44-381b-bbdd-2c0fc14df45b | -3.58921 | -50.23271 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17011a7c-7c7c-36d1-8172-fa21567c40d9 | -4.57552 | -48.01652 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b70de21b-3c08-3b21-b550-0ab9663ecf81 | -3.59755 | -47.35188 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 6cb4a7a8-f7bb-35de-9e20-7aeaa415f84c | -2.72891 | -51.71362 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c80fb2be-f5b6-375c-b3bb-db9a867a1559 | -4.23027 | -50.64101 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aae31568-f152-34fc-821f-80f0934b03fc | -3.15512 | -54.48205 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9d4cfe6c-bd13-3d39-a8c8-c5b808547703 | -2.18802 | -53.73386 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85fe7716-8f70-32c8-891f-b1743ff6c79f | -4.2478 | -48.54205 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d661568-b229-30fb-ae2b-c4949f7b2251 | -4.04925 | -46.10792 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf152056-c448-3fbb-9934-b63ae2111b11 | -3.95743 | -48.13881 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8c66a5ed-31b9-3ad8-859a-11a02f1053b2 | -3.02617 | -48.02461 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f316acd-a684-34ff-80b7-2a6e1305f871 | -2.6106 | -51.77449 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 946cc639-d416-389b-a270-65d22cc51131 | -3.01975 | -47.95602 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c89f311-8ef9-3c48-bf41-2eea4732450d | -2.66652 | -49.89883 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f7c3864-a11f-3326-a476-5f219371d695 | -11.08947 | -43.34643 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6555d241-7810-3a88-8a41-1993a8848041 | -3.22591 | -50.30316 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b3a7b174-2f66-377e-beeb-7d3204b3c2d4 | -4.22442 | -49.81598 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce14934d-80f8-3de2-9e84-22d32a5c897c | -4.35002 | -48.627 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 270b1ce3-e7ac-328c-95ef-6537a9323cdb | -2.86805 | -50.32713 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0fdd8dfd-f954-343f-ae71-598c9140191e | -5.2 | -44.92004 | 2024-11-09 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37ec76df-d738-3413-ba29-daa2571daf0b | -2.87647 | -51.46618 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea551dff-d497-399a-8fd9-407a12d2df5d | -3.22845 | -50.37928 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42f2a54c-f81e-3b9e-b53f-97977f9e1e93 | -8.85307 | -47.67056 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de739d31-c97a-3e6c-bfda-47653025d29c | -3.18789 | -50.58662 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba05f487-bd71-3abc-8c16-a59ebd6f95c9 | -2.93952 | -49.43649 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdac9f63-73aa-3ef6-8a50-c5446cacbfda | -3.20227 | -46.5243 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3794221d-36d5-388a-8ea3-9096bbb80330 | -3.03328 | -50.35458 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5ace2fe7-17a9-3e56-a32a-b1bf2ad610de | -6.23049 | -47.28357 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94043f39-fb7d-3747-ba43-b49db9fe275a | -8.69301 | -47.96097 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1478178f-efd7-3558-bec3-bc0bef948613 | -3.65196 | -45.50312 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9d8d603-073c-34fa-a65b-fc434b2c54d2 | -3.9671 | -46.41743 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b88db93-807c-3da2-8803-54e6937642ad | -2.24688 | -53.66858 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| db95a796-43db-3ebc-963a-e70274ece8f3 | -3.18538 | -50.4406 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f63e810a-1b70-3a37-9576-37d4c461da80 | -3.08232 | -49.5592 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be7699b1-09d1-3a0d-a53b-33135223f057 | -3.02405 | -48.08129 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6046224c-b889-3fa6-b30c-7ac36cafb47b | -3.18899 | -50.44115 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b4a876d5-b6ff-3d81-b123-24e373a7c288 | -2.67131 | -49.89145 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae7a68de-68f6-3c33-b808-d98ecc197755 | -4.21871 | -48.55564 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 735f8142-623f-3f4c-abde-9623a145a71a | -3.30285 | -50.14088 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96522803-dad0-3cbd-a5da-5029dbe55c59 | -4.23165 | -46.90427 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dab7c70f-b4aa-3400-8048-9d4eb782aa4c | -3.83967 | -49.9585 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7882cc25-6532-3bbb-b375-0fe3757e00f3 | -3.58991 | -50.27423 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5bb75ef5-5b0a-30a4-8f86-7beb6d3bf89b | -11.08953 | -43.33905 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 22b708d3-e560-3516-be4e-9885ffc82767 | -3.83835 | -50.0345 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ffef15c-d9f5-3b68-b8ed-1994d4eb7dc4 | -4.21835 | -46.02032 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11dd40ce-2fc0-3b7e-9ca4-f2cb211e1b87 | -4.92956 | -45.3372 | 2024-11-09 04:33:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88066bdf-536c-308a-983c-22cb8bf3885a | -2.4611 | -53.68412 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be9be891-bae3-3f33-80d9-4e836a75307c | -4.24707 | -47.56999 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 83d25696-e6c5-33a0-b686-c8d93ee41f13 | -3.04336 | -48.04507 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 485dc79c-e757-332f-ad32-35b02b307ae0 | -6.21034 | -41.62679 | 2024-11-09 04:33:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 08c9051b-f342-345c-938c-838b24b9978a | -4.05364 | -44.5769 | 2024-11-09 04:33:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b18dd2bd-94f7-3715-add6-39f1e709a3c2 | -2.39822 | -53.86189 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4968488c-01ef-3d44-b7c4-c09642a840da | -4.03354 | -48.28244 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ba244a4-4a2c-3853-b30e-4286f580fca8 | -3.01122 | -53.4431 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20a2ca0d-6735-3c7f-b02d-e6edd34c8051 | -3.79827 | -49.94016 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e419f89-a10f-38db-8667-30efae16a47c | -3.57873 | -50.55431 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26ac39e7-150d-35fa-ab4a-0309d1bc1994 | -3.98407 | -48.16439 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe0e8fc6-7153-37f8-82a4-bbbe2bb84397 | -2.91974 | -51.67834 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fba04cb8-353c-3ee1-ade1-5061f2b1ffc4 | -2.92338 | -51.04737 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 532625d0-00ea-3494-9540-98dfc2654bfd | -4.38042 | -47.23877 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22d9e5e9-cf0b-3131-be8a-caf689d210fb | -5.73363 | -41.99518 | 2024-11-09 04:33:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e133b083-efbd-3b07-a95e-6a87bf46eba4 | -4.51989 | -45.69808 | 2024-11-09 04:33:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f91f1eec-a0a9-3f5d-a2d8-9ba5d0721611 | -4.32019 | -48.64702 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5120621-c360-31f5-b99f-29f0f7e4d98d | -3.403 | -50.01263 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85ec8412-0d37-3f7e-856b-a85adbdc7a7e | -3.62102 | -54.79459 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d85b6511-e7c1-30b7-9a3f-6153c539782d | -3.87544 | -46.65736 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README55.md)
