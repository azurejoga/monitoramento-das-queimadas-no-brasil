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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26729686-fcc4-3a4f-92d5-a5d443b76a45 | -9.92736 | -59.90298 | 2024-10-03 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16add35a-c98d-374a-a1d3-d5d8d84d5780 | -9.90777 | -60.09062 | 2024-10-03 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39bc68c6-094d-351d-8ea9-949157f880ea | -9.90409 | -60.08516 | 2024-10-03 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca09a7ab-eee8-3712-9fd1-000ca107633b | -9.90326 | -60.08979 | 2024-10-03 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d723e25-a072-3e4b-96d6-430a9bf60640 | -9.39181 | -61.04891 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cbeb718f-aa2b-35be-90b4-cc397b0b3fb2 | -9.39083 | -61.05428 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5610326c-6ca5-3343-b65a-d93856df72cb | -9.38597 | -61.05338 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 23128993-3cd9-3fe6-a2ff-6aeac0cc2f64 | -10.38388 | -61.21057 | 2024-10-03 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1d6bd80-38d4-3652-83f7-cc8bd1459603 | -10.38293 | -61.21587 | 2024-10-03 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d458be17-5612-3d5a-be79-1e23902cdc08 | -10.37908 | -61.20955 | 2024-10-03 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f12c64c-1ed3-3465-ad2a-7460d5c0be10 | -10.37812 | -61.21487 | 2024-10-03 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cee1bf3b-4b38-325e-bc80-6d89de005497 | -12.08989 | -61.19397 | 2024-10-03 04:51:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07678a6e-6359-3c01-a490-534ce78b1215 | -12.08522 | -61.19305 | 2024-10-03 04:51:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ec74375-112d-3dbe-991a-e46a1bc63bf9 | -12.05425 | -61.03534 | 2024-10-03 04:51:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1c27316f-efcd-371d-baf1-954c2487cd4e | -10.93253 | -60.94407 | 2024-10-03 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d0e4350-b78b-338e-94c8-ee865bad1ba5 | -10.92784 | -60.94317 | 2024-10-03 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7c8a65c-a541-33b1-8ffd-bed29bf980cd | -10.92315 | -60.94229 | 2024-10-03 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f640f76-8a7b-3c1d-849f-ab243af7e4ad | -13.42192 | -61.92723 | 2024-10-03 04:51:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05e80916-7c73-3032-a48f-484f96fc9a65 | -13.4207 | -61.92857 | 2024-10-03 04:51:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1983da0a-3d42-3198-9782-4049b456f88f | -13.41713 | -61.92625 | 2024-10-03 04:51:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb7472fc-e8ee-3490-824c-617e7b6fdd91 | -13.41614 | -61.93161 | 2024-10-03 04:51:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de333101-aadb-33af-ae6f-37a4aba50446 | -13.41591 | -61.9276 | 2024-10-03 04:51:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4574799c-13fd-3747-a20e-bfc445bcb3af | -13.41234 | -61.92527 | 2024-10-03 04:51:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7b69d58-4ce5-3bc1-8723-fe5daa56b857 | -13.29524 | -60.78227 | 2024-10-03 04:51:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32a00c26-cdbf-316b-bd5d-9a5dee35e158 | -12.6979 | -60.811 | 2024-10-03 04:51:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 394520d4-f28d-3cf4-b75c-7d9fe317e0f4 | -12.69339 | -60.81013 | 2024-10-03 04:51:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ae1c93e-9ddd-3780-9973-9e0ee144b809 | -12.69254 | -60.81475 | 2024-10-03 04:51:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5afd82b9-eae6-3d1b-8acd-088a59423a61 | -7.9028 | -61.47573 | 2024-10-03 04:51:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc518454-080b-3114-81aa-e37e5988ef52 | -7.90226 | -61.47874 | 2024-10-03 04:51:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5b865dd-c622-3cb7-9478-8789645a224d | -7.75654 | -61.12219 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9a0994e-e6b0-3dbd-b998-d11564960800 | -7.75548 | -61.12808 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 177cbb26-552f-3a6e-a1ef-18962acce812 | -7.75123 | -61.1256 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8c6c1dc-4354-30b3-9526-4ee74e5d67b5 | -7.58882 | -61.2336 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8762b38a-6e77-384b-8032-a14e9400e764 | -7.93063 | -61.55708 | 2024-10-03 04:51:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3feee191-931f-354e-9ae7-e48a417b329b | -7.92548 | -61.55618 | 2024-10-03 04:51:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ba76999-3c99-300a-bf5a-e8a49fbc5858 | -9.09399 | -61.13152 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01d2e16a-98a0-3074-8111-d0218f5e93bc | -9.09299 | -61.1371 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b671e006-0797-37ff-826b-71b8f30fd3c0 | -9.08907 | -61.13066 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fb257b2-e328-3fc8-b021-dae67ada7000 | -9.08807 | -61.13624 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 346da204-2c04-3800-ab46-7db85808f70b | -9.08315 | -61.13536 | 2024-10-03 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14c2d8bd-c514-3f96-956a-4c79af14b86f | -7.94131 | -61.79987 | 2024-10-03 04:51:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a079bea8-6311-3964-ba1b-4f39cf90fd78 | -7.94048 | -61.79919 | 2024-10-03 04:51:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9ac0cd0-affa-3fd7-bc8d-718b5e4db22c | -7.93608 | -61.79884 | 2024-10-03 04:51:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c156a6e-be7b-31f9-8d51-4144707fe2f3 | -7.93525 | -61.79816 | 2024-10-03 04:51:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e35b9f4-2b0c-39a3-90ca-158d2780c01f | -9.16615 | -61.66612 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2d5c0de8-9dea-393b-aca4-dc63c4991802 | -9.1656 | -61.66912 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 35c69845-9f8d-3d41-9441-a94feea7b75d | -9.16504 | -61.67211 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6a568320-8dae-3599-b68f-2ac26a046204 | -9.1645 | -61.67509 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| eccbf8c0-1892-39aa-8556-dd381e2048c1 | -9.16394 | -61.67808 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 059fe7fd-708c-30fd-8f78-0b0e2c77a2a6 | -9.16339 | -61.68108 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab9980d4-4169-32ba-988f-6ac7638dd642 | -9.01792 | -62.58698 | 2024-10-03 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4218b8c8-3b81-39da-b5c2-f2a8f4ed422c | -9.01252 | -62.58587 | 2024-10-03 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b90ac8c-273a-3ad5-bf46-574899b8f2d0 | -8.89366 | -62.33378 | 2024-10-03 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39765a41-b947-3ca7-a81a-25b7ebef8df9 | -8.88832 | -62.33281 | 2024-10-03 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03920b5b-524f-3a67-a0c0-073b0df9bd5d | -8.88771 | -62.33617 | 2024-10-03 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12fa6a59-b1e0-31cb-b3a5-84de2f5ef763 | -8.8871 | -62.33949 | 2024-10-03 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aa0c9908-20b5-31c7-90e1-22d4254d82cd | -8.88383 | -61.84882 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7881dbf6-b063-358b-abf1-6db5086c7c99 | -8.88327 | -61.85195 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ba99c4e-8aac-350d-9c78-d8518fc859c6 | -8.88237 | -62.33514 | 2024-10-03 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f830684b-22e2-3ee0-aba3-c5c060f82829 | -8.88177 | -62.33846 | 2024-10-03 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06c1a07c-8d90-3dfe-a65e-3b7a4a24252d | -8.87237 | -61.85312 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0d41fac-52b8-3b21-9544-572ad3e183b9 | -8.86776 | -61.84901 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a4d419f-2fd0-3cd5-82ed-799a171f140d | -8.58862 | -62.42002 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f9691eb-4f72-301b-adeb-024f9a33af7c | -8.58324 | -62.41891 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c856bb43-8f18-378e-a28f-f4015a59677b | -8.56136 | -62.48619 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 349528b9-d686-3d34-a2c6-e2ae98677e97 | -8.56071 | -62.48967 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b311dc2c-3bc4-3278-877a-dea5d1dd36a6 | -8.56065 | -62.4827 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 492380f7-833b-3f5b-8d73-989a9252eb56 | -8.56003 | -62.48618 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f2fbc2a-3050-33cb-90f9-58d92198c554 | -8.5594 | -62.48967 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbf34a07-7520-3239-b336-5416659bbd1f | -8.55724 | -62.47823 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 732b86f6-2888-3bed-969a-e48b82c03483 | -8.55659 | -62.4817 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d595ef52-99c4-3ee4-9314-75ab4f78516f | -8.55594 | -62.48516 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 172931d5-b1b0-3c8e-a7fa-4cbe1992ac33 | -8.55586 | -62.4782 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 514378bb-ecea-38d4-9b62-31d45848a9f8 | -8.55461 | -62.48515 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d25b7c8-0149-3b6f-b0c5-5b9e1c5bc3e8 | -8.17717 | -61.3804 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df372533-626a-3a0f-a001-578649478288 | -8.17475 | -61.36464 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c85852d5-034c-3ecb-84e8-9c82aba3d504 | -8.17422 | -61.3676 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44216842-93cc-316a-a0ae-b34efd076c90 | -8.17369 | -61.37057 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc768d32-c77c-3ca9-8f57-a92e6a911e17 | -8.17315 | -61.37355 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6896107-2538-304b-b732-efb48750f4f0 | -8.17262 | -61.37654 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90c24a19-ac16-3448-b985-054a1016999a | -8.17209 | -61.37951 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31808982-2095-3fe2-bf68-a80848b74966 | -8.14297 | -61.39567 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7dff2ee-7494-362f-9056-50ac416d6792 | -8.13789 | -61.39475 | 2024-10-03 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d2f66c5-51ac-33c8-92a7-5dd3767999a4 | -9.61111 | -62.22875 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0132cdbb-d0ef-371d-be97-f228eaa0a4af | -9.557 | -62.38406 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4ec523a-5ed3-3286-b54f-5698305ffa48 | -9.5564 | -62.38737 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b703b8d6-2e17-371f-be1c-b52d4d1172a2 | -9.55498 | -62.38317 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ea6ea89-a11a-3ebf-8e97-e62ff15da9b1 | -9.55435 | -62.38651 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e47eb53d-d716-3e92-a78a-5c1c4f0ef93d | -9.50963 | -62.05201 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61113786-5c80-3301-b417-c6465bec60b5 | -9.49511 | -62.39281 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f67d3e6-6d3e-365c-a37c-47c3a573c7d5 | -9.49449 | -62.39618 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2deee82f-e236-3c5c-a02e-c7c38a2563dc | -9.49224 | -62.37864 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adffa03b-b1a4-3716-975d-99076e44806c | -9.49164 | -62.38192 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb04f6db-73e3-32c7-a139-3b4e81efeeb5 | -9.49103 | -62.3852 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d66559ce-b7ee-3eed-8f70-40acfd72539d | -9.48919 | -62.39518 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bced7bce-fd28-31df-a928-3d64d9588827 | -9.48696 | -62.37761 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d54ea792-d5ea-3f08-b9d4-967da5eb82e4 | -9.48634 | -62.3809 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86e3221a-df31-3b19-b7b1-95292a1c59bd | -9.48449 | -62.3909 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7230cc77-3254-304d-9add-73864bcdc380 | -9.48389 | -62.39416 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 499f0b98-ef4f-3149-9f2c-8247f1b33993 | -9.48327 | -62.39746 | 2024-10-03 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README134.md)
