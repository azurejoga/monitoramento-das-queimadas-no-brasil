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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfe73138-4ff6-356f-9435-a31fbd9287cd | -9.78409 | -64.2441 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6679cb69-c4e9-36b3-9dd3-2e458d277880 | -9.12586 | -65.8134 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0cd8745-477c-3761-9e67-40169a053c19 | -10.24068 | -68.09144 | 2025-08-30 06:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b04afef6-e254-3b1a-b027-f566a1b14a8e | -8.66263 | -70.0439 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ecd93ce-233d-39c1-b927-7a8409ae33bc | -9.82476 | -63.85464 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d5824a6-af23-3d96-a44f-3719a04f3cb9 | -8.79201 | -71.02045 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b258d15-07f3-31d2-9415-49da6354b8a6 | -9.17771 | -65.5613 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 189276e4-fd21-3372-b5fd-edd512b0e304 | -9.13821 | -65.8137 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca83fd50-f296-38e7-ae68-ea6e34f14321 | -9.11684 | -65.78754 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4292ccf5-bee6-3561-8198-ebc0db3df56e | -8.93215 | -71.27505 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f9c0a0e-f2ee-3434-aaa2-2574a7c14218 | -8.91298 | -70.60162 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be3f2cb9-4e76-3e15-8b58-fa30d9ccee1b | -9.72908 | -64.91552 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 901be70f-5763-363e-85c6-087b2075e8dc | -10.24026 | -68.0947 | 2025-08-30 06:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b89a9ea-aa28-355b-b594-80f5f686f003 | -8.56642 | -70.06608 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 564b5d67-a810-3f27-885e-10c5883b695a | -8.84711 | -70.62887 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18eca188-a0f5-30e4-9f7e-2ef8279d7e95 | -9.13747 | -65.8196 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4609be5-8bb6-3351-a9d3-e304684e3458 | -9.25867 | -65.84715 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbb0d040-ea22-3c2e-b821-46a09893781e | -9.1376 | -65.81837 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58cf41a5-a2d2-30d0-a86c-6f37b332117b | -8.6636 | -70.04131 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70855f3a-9b7c-3047-9536-f7c6ccce4b19 | -9.67654 | -65.02177 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be544363-fa5a-33b1-a4bd-f67e16d35c2e | -9.13253 | -65.80954 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed7300d3-06c3-3996-bc62-9fc0afabc036 | -9.82233 | -63.86562 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 785bb369-60fd-317d-abce-0085bdce4db2 | -8.61569 | -72.38901 | 2025-08-30 06:29:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbe334b4-9596-3099-b572-c4b13e1b9076 | -9.10706 | -65.76727 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 07c94c18-2d17-38bc-a1c2-248046f12d75 | -9.76843 | -64.26036 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb4e8fc0-4631-3219-a83f-c2456e855dab | -9.1199 | -65.76402 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4a46813a-fbb3-394a-b33c-1bcfb43dac92 | -9.11625 | -65.79208 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c676d4ac-5664-3d39-b950-d8a48097985d | -8.85269 | -70.621 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a449e66-9f6a-3ccf-bedd-fe4c1ef4f833 | -9.11826 | -65.77451 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6108eef6-2f1f-323c-b6db-b948bde7bf1b | -9.13806 | -65.81491 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1e09e4b-620b-30f6-9d6b-4ac5ba73c438 | -10.82931 | -68.23489 | 2025-08-30 06:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 590ed08f-2889-3f19-a0a0-c8eda503c4dd | -9.17834 | -65.55652 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 734ea81b-7dd7-3475-9969-ac995c5d6450 | -9.10767 | -65.7625 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3585a05f-f5e0-3170-8c15-47cbd4598247 | -9.1315 | -65.81766 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddde39cf-6903-3d5f-8245-d1317c7c0b35 | -9.13211 | -65.813 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52b2f8f2-1732-3b96-a60a-5708b9cbebd1 | -8.90967 | -70.59863 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c16ffbc-62c7-3e32-86d9-92496721a16c | -9.7759 | -64.25521 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10b949b6-c85a-3559-b563-9f6f460957fe | -9.12643 | -65.80875 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c9c1bf6-637a-3320-b447-5218bbeca16d | -9.823 | -63.86001 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a9c402b4-5bef-39ad-b69e-044ac1c510d9 | -8.57162 | -70.06215 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55198e2c-3415-3e68-aaf6-be749e4b520f | -9.13195 | -65.81421 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa223a9b-d044-3381-ac57-acce3f105fa3 | -9.33489 | -68.22083 | 2025-08-30 06:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01447fa2-68bd-3361-bcac-e05c1a4dae34 | -9.12552 | -65.76594 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2df6114a-c0db-308d-8114-c66505c21ef1 | -8.53926 | -70.74718 | 2025-08-30 06:29:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baf7a28b-5d6d-3552-9f1e-9e6cb1e1c946 | -9.77662 | -64.24918 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fe03ea0-3b91-3f38-850f-1cf8bf078965 | -9.126 | -65.76493 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e5b0f28-6846-3ae1-9fcb-aa0eec71b357 | -9.03313 | -68.33103 | 2025-08-30 06:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ac5e582-204e-392a-9a64-c3aef656d372 | -9.21261 | -71.78094 | 2025-08-30 06:29:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b58c031-d207-36a0-9114-4b864f4b30bb | -9.10454 | -65.73863 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4206cf0-f906-331d-8349-f9530e499f8f | -8.66298 | -70.0459 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1373fa30-013f-3181-9c45-e4410d2cf427 | -9.77438 | -64.25492 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 863e8fec-ac24-38e0-b296-a3c046f76816 | -9.11065 | -65.73953 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e60cdb3-4b1a-351e-990d-95b69f0600da | -9.11378 | -65.7633 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 382f4ded-ec34-38d2-824d-8d12b53e9599 | -8.79628 | -71.02105 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 638d5687-6106-3899-afbe-f774d3f6336c | -9.11195 | -65.77745 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ef20ab3-fd89-3039-bb8a-a055b83fd828 | -9.67586 | -65.02708 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 180f4240-7149-3190-8532-0c2e920fecb6 | -8.85149 | -70.62952 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e57ecd1-d184-37eb-b6d4-2ead77a633a6 | -9.11929 | -65.76871 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bc3f7049-457a-3881-9e81-cf8a0f0e9f8d | -9.81713 | -63.85949 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2fc6952-c029-3b5e-bd5f-0a698a8570ce | -9.11316 | -65.76809 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 176a18e4-4d79-3ee3-9ceb-432c58213176 | -9.17698 | -65.5524 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26fe1264-1b6d-3336-8582-97b8707ebdf5 | -8.91407 | -70.59924 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e07b5dd6-c09f-30d6-8a2d-03f2395b378b | -9.11868 | -65.77346 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd602e0c-16b2-3183-a931-e38f217fe46e | -9.77514 | -64.24892 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a87848c-866c-392a-9f3e-c220556d29ac | -8.5717 | -70.06393 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2479f279-cd6b-3ed6-a6d7-0abcba989c60 | -9.11135 | -65.78206 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72f2645f-ca05-3eb4-942b-bd3f0ff5ea8b | -9.6765 | -65.02274 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 518928df-ce13-377b-af1c-f05a0da99e4a | -8.93153 | -71.27605 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e300d66-0409-35e0-b403-1d1cb0aab63a | -9.25925 | -65.84248 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 238f0805-bed1-3aa9-940c-37b8451d2ea5 | -9.72975 | -64.91016 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29cf1246-1bc0-3733-bb47-424aa90e6437 | -9.33531 | -68.21771 | 2025-08-30 06:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef59305b-944b-3f9a-8fe7-c8b7aed37a1f | -8.81242 | -69.29656 | 2025-08-30 06:29:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0149645e-d865-37dd-8caa-706e5f344603 | -8.65808 | -70.0432 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88e0feab-0bfc-315e-bba0-2ff96abe2894 | -9.82333 | -63.86605 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18b95974-9ac6-3865-a87f-53b3d0aee6b5 | -10.82399 | -68.23421 | 2025-08-30 06:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 66096d1d-7296-39a2-bf7e-cc3918223d6e | -8.85209 | -70.62527 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e84a1637-f818-3199-875d-67af8b5031b3 | -8.92803 | -72.82551 | 2025-08-30 06:29:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 319b5fa4-fe94-3f27-874a-02d2aa108f77 | -8.75978 | -71.06426 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d171717f-b16d-3d74-bebb-a26552634491 | -9.11943 | -65.76503 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5bf3968-9821-3e89-a731-99a97969bbe5 | -9.13688 | -65.82433 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4d8452c-fba9-3c1b-a0a0-bfdb044ea447 | -8.84771 | -70.62459 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b99abeb-60ee-3bb6-9624-6a1f0f0f5024 | -8.9287 | -72.82082 | 2025-08-30 06:29:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc672196-f12b-3e4c-9885-4f36491592ba | -8.66328 | -70.03931 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfe9610c-0a18-3baa-80a6-14fbdad0526d | -9.78266 | -64.25606 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1acf12c-7516-3d42-8b26-b3085e39d3df | -9.82403 | -63.86047 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a73a0f19-14c8-3b79-b6aa-d4fcd9cba098 | -11.39265 | -63.24405 | 2025-08-30 06:29:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cb30d40-19d1-38ec-a96f-1c482a54fece | -11.3991 | -63.25246 | 2025-08-30 06:29:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8687705d-edc7-32c9-a3f9-e94b8fdf1f86 | -9.67585 | -65.02805 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 985aa869-7e6d-3f2b-be5d-27dc6b7b5517 | -9.82369 | -63.8542 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 253ce06d-3128-3ffc-ab05-4f65bd4a7cbb | -8.56716 | -70.06327 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 500d625e-27a4-3b1a-a932-c4c1e1d2ff34 | -9.11885 | -65.76975 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dde6b7d-59d9-33c7-b93e-9aecac2cc252 | -9.13698 | -65.82307 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 389fa9b8-1027-3474-a482-3c3984ca9336 | -8.75923 | -71.06823 | 2025-08-30 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6364ba7e-0cf1-38a9-b1f6-e36a2abdd08a | -8.99101 | -69.37699 | 2025-08-30 06:29:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2b1648b-4eb5-3fc0-aaa5-231a49f50046 | -9.11255 | -65.77282 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00bc6955-6d5c-31de-a0e3-65db585f4a05 | -9.78337 | -64.25008 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e81ac05-1b74-3b05-a348-61847ea31dd8 | -9.76114 | -65.08862 | 2025-08-30 06:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72d89a25-7341-38d4-8032-f92c2a1e93c0 | -9.11675 | -65.74046 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b75979e-900e-32fa-88b4-212ef57e6f11 | -9.12541 | -65.81684 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ccd825f-6da5-3b1a-ba8f-142d32ee3c59 | -9.17638 | -65.55721 | 2025-08-30 06:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README88.md)
