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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17704daa-c903-3eaa-b7ae-f553dabf01e2 | -9.725 | -50.8246 | 2026-09-04 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 7f6bd113-8049-3caf-9e93-9824aeeeb405 | -8.1126 | -54.7871 | 2026-09-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 24716949-c4e2-3db4-b5df-ff59667c7e85 | -9.7059 | -50.8476 | 2026-09-04 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6dfb60fd-59a3-3d7c-9a00-1a40b0af31cf | -8.1312 | -54.786 | 2026-09-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 2bccb5c1-f03a-3743-975f-b208c642352f | -10.584 | -50.0362 | 2026-09-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| c6001392-a88a-3551-8c63-7f261637aaf7 | -6.3088 | -46.0791 | 2026-09-04 00:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 474ab3ec-b9fb-3625-81d0-54411416b21f | -10.5653 | -50.0168 | 2026-09-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 0dba92be-459f-35ac-850c-be3d1ad2e515 | -18.1305 | -51.7971 | 2026-09-04 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 841a3af2-c2a8-354c-8eba-a36b7f2c4fd8 | -8.1128 | -54.767 | 2026-09-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 9345b443-3451-306f-915b-7670cb4cac8b | -8.5048 | -54.6606 | 2026-09-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 273.4 |
| 16c1c7e4-23d0-369b-b4b1-708a03a950ce | -18.7358 | -48.9307 | 2026-09-04 00:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 104.2 |
| e90e4eee-8944-396c-b76a-656c9a59f4a2 | -9.7062 | -50.8264 | 2026-09-04 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 5baea391-90eb-382a-959e-1a1482fff2ff | -7.0047 | -62.9902 | 2026-09-04 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 8b6b2a61-ae34-3bfb-804c-b41bd3b600c8 | -18.7363 | -48.908 | 2026-09-04 00:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 274.6 |
| caee3879-0670-3ac0-9234-aae0a5c594bd | -6.3086 | -46.1015 | 2026-09-04 00:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| fae34b81-6284-3936-aef5-f3d4c6911ecd | -8.4861 | -54.6619 | 2026-09-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 397bf04c-1a08-352f-baf3-f05887fb4a69 | -18.1505 | -51.7937 | 2026-09-04 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4ea83c3b-8a85-3e0e-80e1-5b5360cd35a1 | -8.505 | -54.6404 | 2026-09-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 245.5 |
| e397b653-13b5-30f5-94a3-0e725470dc99 | -7.566 | -61.343 | 2026-09-04 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| daad9761-c78c-3157-8828-c9ed0539ffe2 | -4.3774 | -47.7627 | 2026-09-04 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 8a0c7378-08ac-3c15-9322-e842224f54f4 | -8.4863 | -54.6417 | 2026-09-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| c2d43506-f533-30c1-bae6-bc8417e6a44b | -7.5476 | -61.3437 | 2026-09-04 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 15dd1e99-4d71-3273-9363-f9cd4d660032 | -10.8438 | -51.8123 | 2026-09-04 00:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| a413738a-65fd-384a-aa78-649f45fb5084 | -10.565 | -50.0382 | 2026-09-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| e3f5e55d-2a23-37ec-a3dc-043f2ba5be4d | -4.3772 | -47.7844 | 2026-09-04 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| ed9dabae-a156-302a-9e1b-700d60067ad6 | -10.2031 | -50.2681 | 2026-09-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 6bf8bd29-cfc3-3e2d-a3e6-f3d76043ff33 | -10.5843 | -50.0148 | 2026-09-04 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 5efc1c8a-4239-349d-8aaa-f341cc231952 | -18.7162 | -48.912 | 2026-09-04 00:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| d23c7cd0-de60-31c2-88be-b71e7cf2a8aa | -8.1312 | -54.786 | 2026-09-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 36841315-d9c3-36b6-92dd-4c4dd553eec2 | -10.92 | -45.3483 | 2026-09-04 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| e3a434ef-82ae-3c9b-84c6-f554d9e58a40 | -7.566 | -61.343 | 2026-09-04 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 147.5 |
| bdcc30af-b7f2-3fac-9ae4-4d9dc8f62738 | -8.1128 | -54.767 | 2026-09-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| fe7a2f04-19a4-38b1-a515-997f858c4ec4 | -8.505 | -54.6404 | 2026-09-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 273.7 |
| 99344d69-26ec-3c57-991b-29123339502a | -4.3587 | -47.7853 | 2026-09-04 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 7ac53e33-cf09-3667-acb4-6cbccf259045 | -6.1689 | -47.0877 | 2026-09-04 00:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| c1ea035f-686f-3054-9922-849e2a0211d5 | -8.1126 | -54.7871 | 2026-09-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 8bd0c456-8ebc-3896-aead-31e863652e0c | -6.3086 | -46.1015 | 2026-09-04 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| ae9e42a3-4b5c-3313-b940-e2184481a24b | -18.7363 | -48.908 | 2026-09-04 00:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 220.7 |
| 1232b769-f3a5-3fc1-a95a-ba50ae2ba871 | -6.3275 | -46.0777 | 2026-09-04 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 277d5b86-c020-31e2-b161-a4d41cc8923b | -8.5048 | -54.6606 | 2026-09-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 302.7 |
| cf8ab4c9-e535-38d9-a72c-0dcfa355800a | -10.9009 | -45.3509 | 2026-09-04 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| b26dd5e6-41e8-330d-9d4b-ef6c0bd75b67 | -18.7358 | -48.9307 | 2026-09-04 00:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 2f2b4a58-aa79-3810-b54e-a94fa930fea1 | -18.1505 | -51.7937 | 2026-09-04 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| d3e0213e-20c5-3d7e-8786-d33e0d2df09a | -8.4861 | -54.6619 | 2026-09-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| b832c25d-dd43-3d45-8dcd-33f43fc6db1f | -11.5205 | -58.5132 | 2026-09-04 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 568e9b7a-8c34-340b-a52c-7fd0ba352e41 | -7.5661 | -61.3239 | 2026-09-04 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 294f9d66-b2b5-32ab-9813-63dca6045b3b | -8.4863 | -54.6417 | 2026-09-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| c0853b3d-26d9-3ada-aabb-432e4d2b7cf7 | -7.5659 | -61.362 | 2026-09-04 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b5e4361d-6a30-3dce-948c-c752de120f51 | -7.5476 | -61.3437 | 2026-09-04 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 7a52fc80-f11c-3c8c-8c0e-30c1d5c01863 | -6.3088 | -46.0791 | 2026-09-04 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 154.9 |
| d70e4662-d526-3937-8969-d5da15c39187 | -8.505 | -54.6404 | 2026-09-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 218.7 |
| da80bc65-b38c-3d37-b697-6c60f727a04a | -7.5477 | -61.3247 | 2026-09-04 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7d41ca50-f31f-35e3-99c9-49befc4f1825 | -18.7162 | -48.912 | 2026-09-04 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f09d9f53-d3e8-3b10-95bd-6ed55b00c618 | -8.4863 | -54.6417 | 2026-09-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| ca14ec7b-7397-3c27-b5db-1ccb40fd4eb2 | -10.92 | -45.3483 | 2026-09-04 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 364.5 |
| 8e6e0994-8b74-3b9b-8516-2405e8f204c1 | -7.5476 | -61.3437 | 2026-09-04 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 130.9 |
| c610bb0c-b104-3595-b618-f5c4d49d70af | -7.0047 | -62.9902 | 2026-09-04 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 142a177e-efbf-3cb2-8c08-0556e608f7b0 | -4.3772 | -47.7844 | 2026-09-04 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 9450441a-2478-3953-aee1-275f6fb8ace2 | -8.5234 | -54.6594 | 2026-09-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d4157a02-de66-3360-9e4f-051dd424e4d9 | -6.3088 | -46.0791 | 2026-09-04 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 485b134c-d639-3d18-94a2-1c56812b3046 | -18.7363 | -48.908 | 2026-09-04 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 170.7 |
| ad62dfd5-89ca-3047-a760-fc140f5f72b0 | -8.4668 | -54.7439 | 2026-09-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 85bf0e35-68d1-360f-bac8-7a33e59615e5 | -10.9009 | -45.3509 | 2026-09-04 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 2de6d0ce-8b67-3bb3-8e26-e3ded5f9b5d3 | -7.5661 | -61.3239 | 2026-09-04 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 71ec6a9a-b52e-3727-a0b2-dcdf457f2bbe | -6.3273 | -46.1001 | 2026-09-04 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 32a1dfe5-8d37-3bc4-9336-39a0ebf32d7a | -8.1312 | -54.786 | 2026-09-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 22acd632-aa07-38a5-9a2a-f1142fc1e085 | -8.5048 | -54.6606 | 2026-09-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 254.5 |
| bac6da8a-db8b-3913-827a-a3c4e6f080f2 | -8.1863 | -62.7986 | 2026-09-04 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 8392a974-4c2b-3be6-b3a0-5c05d58a543c | -7.566 | -61.343 | 2026-09-04 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 192b8a38-6396-3745-a137-dc55dda16967 | -6.3275 | -46.0777 | 2026-09-04 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 291d601d-0984-3a87-a93b-22aab0f1d0f9 | -8.1128 | -54.767 | 2026-09-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| e7af689a-2012-3e50-bde4-b6d197461117 | -10.9204 | -45.3253 | 2026-09-04 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 60f4c8d6-c49c-3b46-9625-4c7667f38b7d | -8.4861 | -54.6619 | 2026-09-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| d397f4b9-bb67-35ba-9dd5-0c3e4ccd1446 | -18.7565 | -48.9039 | 2026-09-04 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 73e8945d-28e0-35d6-9c28-c92df67bce3d | -8.1126 | -54.7871 | 2026-09-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 8b77d203-c39d-3417-91e6-35e46a4ea997 | -18.1505 | -51.7937 | 2026-09-04 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| b0942c14-fea2-34e1-a6ff-5f68d5dd68ab | -10.9197 | -45.3712 | 2026-09-04 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 1f02f2c7-07fc-3942-9e9d-7c558cbc3155 | -18.1305 | -51.7971 | 2026-09-04 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 2f109554-5509-3c7a-a7e8-aefb7ed3f5ff | -18.7358 | -48.9307 | 2026-09-04 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8034a771-7925-39f6-8b14-7a15e4aebdad | -6.3086 | -46.1015 | 2026-09-04 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| ff4517dd-c2af-31a3-a65d-9310d25fbee6 | -10.9143 | -49.6194 | 2026-09-04 00:25:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e824dc85-7fc4-37f8-bda0-ff0b02a4bdd7 | -17.0896 | -56.834099 | 2026-09-04 00:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e02d025-67a7-34cb-9be8-939e15b89688 | -8.4898 | -54.639599 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b8199d6-d701-31a2-b4a3-6a9ec9a8a362 | -4.4823 | -55.409698 | 2026-09-04 00:25:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4548962-d280-3c3d-bdf6-0fbe2530409f | -3.6282 | -54.593498 | 2026-09-04 00:25:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22fbf56d-3e39-3327-9041-073fd49572b3 | -10.1983 | -50.258301 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b191b699-3fb7-3767-ab44-712a42dcf4e6 | -8.498 | -54.630402 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e7d48a-46af-36c3-aadc-a6b76d90fa2d | -8.6277 | -54.8428 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b95bb88-7383-330c-b626-ed70bd80c3d8 | -8.1198 | -54.780701 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28d0fcf9-8fe8-3e01-aba0-32e0ec9cf605 | -3.2441 | -47.247002 | 2026-09-04 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83cf4504-f349-3703-abe2-600f06599a7d | -14.8208 | -48.071602 | 2026-09-04 00:25:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c3e4bfa4-06a8-36cc-9992-f1c383b838e2 | -8.4882 | -54.632599 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 129598aa-ea47-3032-a185-528053fac14e | -11.5184 | -49.207802 | 2026-09-04 00:25:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb3e3dda-70cd-38d7-aad4-0b159c3d778f | -6.3092 | -46.091499 | 2026-09-04 00:25:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acc95482-21a2-39a7-9f32-881ba7384465 | -11.5282 | -49.205399 | 2026-09-04 00:25:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 861e5323-baf1-3c7e-ac77-7d97a952d89c | -21.7216 | -47.149899 | 2026-09-04 00:25:00 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 214d638b-1cac-360f-b63a-0dd5ae10b614 | -7.0157 | -62.955601 | 2026-09-04 00:25:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 990857d6-aa72-3964-8ef0-9f497ec68100 | -8.1115 | -54.789799 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaad7b03-d704-3d25-8efe-174a66a252b1 | -8.1937 | -62.772598 | 2026-09-04 00:25:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9c05636-bbd8-3102-af35-806eb39cc3d1 | -8.1802 | -62.7561 | 2026-09-04 00:25:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
