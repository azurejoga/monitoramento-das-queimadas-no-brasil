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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c518962-9bb8-3a85-aa1f-0cd3432a2ddd | -6.89888 | -46.55101 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 730b286a-ed77-3f1a-b90e-72cbb0dad012 | -7.09021 | -52.74608 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff4556ac-fb68-36bb-858b-825475b271d9 | -5.41041 | -49.26922 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32c87059-cc6d-330c-b8ae-29c64b1ed14f | -6.61152 | -59.96821 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e408ee4-269c-3060-9c9d-20e20e67d033 | -12.14945 | -45.8186 | 2026-09-23 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c505cb04-5f50-3109-a47e-6189a5bef502 | -6.94391 | -52.60481 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb74f588-cf9e-3860-90df-06986bde046f | -10.29587 | -50.53222 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9d0b5598-04e9-3253-bce0-7c73b702c6c5 | -6.17989 | -52.79342 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19b9cad8-8cca-308d-98dc-5d9af9316750 | -5.99597 | -57.72205 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87512ff8-2039-3987-940c-948a823cbce5 | -6.49024 | -53.61815 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9d8fc57-12b6-3e67-946e-c615b24ea605 | -8.49686 | -57.61325 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 96fff911-8641-3557-9bce-5056fbf74df5 | -10.05518 | -48.84422 | 2026-09-23 05:04:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f58abfd2-32e8-31a7-9925-670985732ce1 | -5.84016 | -52.09557 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a07d51a-9b2e-3408-8a93-5c31b56e6cfe | -3.65065 | -58.77197 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9766f7aa-09fd-320f-a905-fdbad9cedbd2 | -6.61523 | -59.92402 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| b49b155a-8bec-3064-a86a-b9e83c26ff19 | -6.33881 | -43.36588 | 2026-09-23 05:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3639f0cd-f51a-3f48-ba71-0cbbf1a02849 | -6.18968 | -57.77995 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff236bd7-e406-36b5-8837-4004375a1849 | -8.33244 | -50.82459 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3437ef12-cf01-3c9a-b2fd-17f56953b1ec | -5.74792 | -51.93079 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66194feb-7fc8-31c5-9a10-3c583f8c6612 | -9.59692 | -63.924 | 2026-09-23 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62cf393c-ec08-31de-a6fc-dd48db2c69cd | -8.28325 | -54.77303 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f25bc14-37b7-3a80-afab-fc5ed208ed94 | -6.13014 | -57.75856 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5135124-9d8b-3c45-8e2c-d85fd0771b61 | -10.0037 | -45.1942 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 02cd4941-8680-3d0d-a818-fb67f4e0f007 | -6.89094 | -55.33615 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 45d6db6a-5c9b-32df-853d-b2e88e73c78b | -11.65239 | -47.8021 | 2026-09-23 05:04:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebd1d9ac-0102-3b08-bc29-9274255f5f2c | -6.18377 | -52.79047 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e86a80bb-fd27-312f-ac85-6e3cefb9cc67 | -10.46049 | -44.94551 | 2026-09-23 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1be5aa08-6d9d-3fe9-b33f-bed66743517b | -6.89448 | -55.33673 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e58ba16b-d9fa-3d25-8b29-b3d9c9bad0cd | -5.27973 | -60.20823 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1baa0a53-27a8-391e-8d20-1202ed032ba5 | -3.68755 | -60.5495 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53b00380-dc88-326f-a2a2-3441022e374d | -11.4027 | -44.03149 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9916522b-0395-30ea-80b0-9afd90bd58bb | -6.9346 | -46.55454 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e01f498f-6128-3b93-8bb5-02e1143746b3 | -6.38011 | -55.28126 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 407675f9-d4fd-3abd-ad33-0a29388d01f8 | -3.42706 | -61.32965 | 2026-09-23 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a8b56dd-25ac-3d03-bb2c-1f6edd32da92 | -3.72148 | -60.57425 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaf27c0d-f53f-3b18-9c40-ad19d83bb698 | -6.63871 | -59.92819 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 29d1a06c-2d4b-3f1c-bab2-25c679bbab3c | -8.0886 | -44.34647 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca600249-eaf2-3822-ac6b-2db42b474fb4 | -6.61685 | -43.73866 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 58da5856-0bc9-3010-8cd3-59a9eb7c99e7 | -5.24534 | -48.18802 | 2026-09-23 05:04:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f88ab9bd-de72-3a2c-ab0f-b3256911d782 | -5.827 | -52.20025 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be7b156e-a76e-34ff-b70b-a9d07b960a7c | -4.16473 | -60.77105 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c72fa30b-7b52-381d-9578-abdb00c2d2f5 | -5.28091 | -60.20908 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb6223d5-a49b-39e8-a682-b3774b4339f0 | -3.77711 | -60.74944 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af8f1d8b-2632-337e-8187-a45a43a40d97 | -8.91993 | -50.89491 | 2026-09-23 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f34ef0a2-3f91-3e0d-9ea8-f64c9c6dd6de | -8.17668 | -54.78264 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 381a40a4-8163-3dee-a2f1-f34687b0d302 | -6.18827 | -45.32019 | 2026-09-23 05:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c8608ef-b1da-3a9a-ade3-85aa6e9acfa1 | -6.8195 | -59.45893 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 718f9f9c-96c4-3dbc-b416-0c40738d8f57 | -6.6697 | -58.56691 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34a5467b-0f78-33ff-b164-4b605fe7bafa | -8.25066 | -54.77908 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0ed81389-1c95-327f-9573-b47a887c30bc | -6.62079 | -43.74905 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0f8b132c-b079-325d-9e01-d3608d47b90e | -4.56532 | -55.06033 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e700bb8-12dc-37dc-a3d7-c9a0015f973a | -10.86941 | -50.15116 | 2026-09-23 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 319c8496-f803-385d-bc1c-f9cf643e6e77 | -5.88921 | -52.27768 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 531dc583-0ac4-3b90-b1d6-b7c912fbb935 | -5.57073 | -52.02068 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fdb9c98-a0c8-3a7b-a083-d70d3ddae43c | -4.30357 | -55.59251 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3db7917e-1600-3525-8d13-864d7a364aca | -5.80683 | -57.73846 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce1370e8-bc65-3f26-8521-98ae85d93abb | -5.81202 | -47.76427 | 2026-09-23 05:04:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4796c149-4aac-3403-9e35-388d38f5ba7a | -9.45263 | -50.30145 | 2026-09-23 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3103524-85cd-37d0-8e7d-795f80a6d089 | -4.42844 | -55.07703 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c83dfb5f-9c55-3416-a90a-ce00f5cab511 | -9.57837 | -46.53778 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 681a0b68-0a26-3658-882f-94863b5f4273 | -6.13054 | -52.76069 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 727870bb-2d3b-3624-8832-0809662c7153 | -12.0232 | -47.80659 | 2026-09-23 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b910d94c-5fe7-3be2-83ca-d1968374df3c | -12.19611 | -47.02897 | 2026-09-23 05:04:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 04243611-e313-3f2c-816b-78fc5056f695 | -8.86062 | -62.4205 | 2026-09-23 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63914943-47cf-39bc-9665-3e7743492171 | -12.20933 | -47.2825 | 2026-09-23 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f66887dc-7de0-3024-a5d5-08257bc40a01 | -3.68142 | -60.58619 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 44332773-32bd-3fff-8cff-1cdb87963b65 | -8.33683 | -50.82502 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a34bf6a-a298-393a-bbd0-8d4702eae965 | -5.16082 | -60.30495 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f930f186-72e6-35c1-8a2f-346debe05e56 | -3.28376 | -57.86211 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8a333c1-100f-321c-b4e7-059970362c17 | -4.44704 | -55.07576 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf5c6e01-5988-3a73-91d6-ba0c9cc5034d | -10.29496 | -49.11569 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47810b15-dc39-32c2-88e7-bde41b24b108 | -5.92034 | -51.71807 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8e0826e-540a-35c4-ba13-26ed84c91335 | -5.74672 | -53.47423 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b054eb19-97e0-316d-ac43-613a37376d43 | -5.76099 | -45.11106 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9f819047-e61a-32b8-b1ba-c1834eda26cb | -6.13334 | -43.84147 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0db64476-83c4-318d-af1d-65051fcf48f1 | -6.39436 | -54.88332 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa048a51-0474-3a3b-9f51-7d4a79eaa62b | -6.69484 | -56.16015 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afeb0bd4-d1af-3576-ae3b-95c5203b5324 | -6.07861 | -57.62521 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56dc7454-04c4-30c4-9d3e-7e0143c47e19 | -11.66064 | -50.97965 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f60e6c8-9465-3a9a-b072-2793276e1906 | -3.68193 | -60.58311 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fde56317-1516-3363-a505-32bb30682425 | -7.45779 | -45.496 | 2026-09-23 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 300dff04-cefd-33b7-9b5f-531830cb755c | -3.112 | -60.68428 | 2026-09-23 05:04:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b5f0818-4d46-3fa8-98aa-187a4ca57680 | -5.86842 | -52.06792 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 92e7dfe5-055a-37a2-a9b6-18efb39389f3 | -3.1125 | -61.09153 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 289eb0cd-8ffc-340e-b514-3630378af48b | -10.0025 | -45.19412 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4e4d18f0-6025-3675-8dfd-01d121a4b5eb | -3.7252 | -60.57812 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3aa24e78-b08f-37a8-885b-697a041af3f5 | -11.39387 | -46.80555 | 2026-09-23 05:04:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30250a1f-a667-3f5c-a4cf-d7561960329f | -11.40918 | -44.02485 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80372709-5a10-3083-a1f5-16cdd05f5634 | -6.75745 | -63.1428 | 2026-09-23 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 448d060a-a8f0-35c4-889e-ba688a591888 | -4.27008 | -55.45094 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faf6d45a-8d27-3b2c-8f5e-39548a7c96a4 | -6.88564 | -59.86011 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c3350d0-601a-3afc-82ef-5487b5ce0498 | -7.32981 | -55.589 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b10547b-8256-3c63-b78c-ea7724b1a83e | -9.96765 | -50.26528 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 005ad002-8bfa-3b66-90b5-4053a08b7751 | -8.83775 | -50.48464 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cab3749d-896f-3303-8765-ad6b9023abda | -5.8301 | -52.05124 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b71eecca-e700-3a6f-b60a-67b17f4582e9 | -11.88708 | -45.76989 | 2026-09-23 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f7fa949-199a-3405-8719-ac1d0263a057 | -5.88616 | -52.10273 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f98842d-acee-3b8f-b76b-df4a72ffb6c0 | -6.5266 | -43.54684 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63cc9a4d-b46b-3df1-a9ef-74cea842740c | -8.86262 | -62.42455 | 2026-09-23 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8ab73ae-59db-3782-8b5e-43ef858caa43 | -6.752 | -50.68707 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README82.md)
