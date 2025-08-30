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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baf9e200-b19c-3d7d-8c57-0a846c4f2175 | -7.50306 | -45.0495 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d65424d-0117-33e1-8249-76536e3a2f72 | -7.6795 | -44.98555 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77faa216-c4c9-38e9-9001-5b52faaf7cad | -8.04803 | -45.41301 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 268e1b8d-be8e-3cdb-858c-a7bcc31887b1 | -7.15841 | -44.13767 | 2025-08-30 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d9febf1-c682-3b6f-9081-a5ab1138ba6c | -7.6056 | -42.73463 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c9a46e23-74c6-3438-9fce-ffab60ed09b8 | -3.0697 | -49.46234 | 2025-08-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91a2a553-952a-32c8-adba-7c120b347a59 | -5.72848 | -45.53842 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fd4d975-b71b-326d-9641-a0ac193f491d | -7.59753 | -42.71756 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b23f21d-2e8b-393b-8b26-ebfcbbfc10cf | -5.92511 | -43.35963 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78e288a1-e37a-3fb9-9572-36e859315ad8 | -7.10073 | -44.59614 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e24070f3-2f06-3156-b580-99efdb38c77b | -7.61899 | -42.72851 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c2b54e6f-4cd1-3879-82b1-6d9b449ce278 | -7.81036 | -44.80035 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57447e96-4ebe-32e7-8d12-c5a02dc64756 | -6.59615 | -43.64168 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 841837d2-c96f-3ec4-a569-57d2f49de976 | -7.60777 | -44.7254 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b56f95c-491c-3471-8b31-9a4cf01ec3c7 | -7.77638 | -45.47611 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5774fa1-c482-3a17-998c-00cbd62182df | -8.45348 | -43.64025 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b0fcd88-de1f-3c36-b4e0-1407fa1099df | -8.45172 | -43.64367 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f787c536-38c9-3d5e-87c3-2f82597cd309 | -6.60408 | -43.64992 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a724db63-9638-3851-91a4-aa655615a9d6 | -6.1756 | -43.32445 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c319af5b-5e83-343b-8339-18b9cae8c312 | -7.73458 | -50.26624 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 15ed5f68-fbed-304e-99e7-87cfcba4bf70 | -6.17394 | -43.33527 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2667fe52-3bbe-3342-82c1-89224be611ea | -5.96494 | -44.50944 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cdc81fd-cb09-3f4c-bceb-5114bab837a3 | -6.59505 | -43.64879 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8455696d-bf34-37b3-9a9e-35c3a8a425c6 | -6.52403 | -44.87296 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16c1de58-22ae-35ed-84ee-e03f09e182c7 | -5.20704 | -40.69175 | 2025-08-30 04:19:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b29b93ce-09b8-3eda-bd07-c087c06393a5 | -6.1846 | -43.33321 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1aaa53e3-9ac4-3036-802f-964d51a38576 | -6.94554 | -44.30444 | 2025-08-30 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 561a6bef-260b-3cf4-98be-4745b3f80d4f | -6.56135 | -44.21623 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6200632b-527d-3694-9d12-2c238741ba5b | -7.41812 | -42.05752 | 2025-08-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a006bb07-06c3-36f1-9f96-f62c5950c233 | -7.32623 | -44.37125 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8c45053-d2a4-3aab-a5c6-3d8288999782 | -5.18089 | -46.07281 | 2025-08-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 034aaa8a-9b29-3560-9dc1-142a52ed937c | -7.25027 | -45.44588 | 2025-08-30 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8a2f2a3-ca13-378c-b50b-dda626124642 | -7.67245 | -42.65697 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1d2df707-3334-34a3-bd73-1aaf527e4bc4 | -6.16438 | -43.33013 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bdec054-e10c-35c5-bfc9-2b5261221cd4 | -6.48458 | -44.07566 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30ead15f-450b-340a-bdbd-370f6e496813 | -3.07382 | -49.46297 | 2025-08-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c8e64f8-2df4-3611-b131-2279f09e9dcc | -9.0275 | -40.52164 | 2025-08-30 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5758b335-4566-3798-bee1-6d2cc450768a | -5.79095 | -42.56291 | 2025-08-30 04:19:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2a9418de-d95c-3d66-bff0-acd9af076fe7 | -6.18268 | -44.79065 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad91f20a-85a1-3c5f-981c-3dd01c298b8d | -6.2488 | -43.37603 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bd92664d-c493-3531-a4bd-708d5a4d609f | -7.60507 | -42.71476 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e5d85a91-3df8-3ac5-8000-bb8a016aff52 | -6.50579 | -43.54423 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea4f153b-962e-3e3c-a699-faf0d1fe2af3 | -7.23701 | -45.42246 | 2025-08-30 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 777bf386-41fd-36ce-b455-c35615b4839d | -7.71498 | -50.27993 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| abc871fe-3865-3b0c-bc96-8cd5bf95289a | -6.1829 | -43.32185 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ae1540f-666f-3d33-b464-ce6489be68d5 | -6.34439 | -47.73154 | 2025-08-30 04:19:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09bf608d-66a4-3d0b-bfdd-11a26af194d5 | -7.61551 | -42.72799 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 71687d59-d9b5-35fa-bb3c-bfc6b3696df8 | -7.61145 | -42.73134 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b065ed78-61d7-3a6d-be20-31d7630000fc | -3.59724 | -49.45714 | 2025-08-30 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f246216-c9d8-3d27-96ab-64c75efbba50 | -6.48979 | -44.39345 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 89d169f0-596b-384a-80f2-91dc6a3aa05c | -6.38355 | -44.33081 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c65d8f49-ebd6-3830-ba93-a127939b1829 | -6.4134 | -45.59696 | 2025-08-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e07bf104-b1fc-3195-a688-b7fcf82df250 | -6.18273 | -39.26449 | 2025-08-30 04:19:00 | NOAA-21 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 96344263-6975-3172-84ac-14cfee921786 | -5.06503 | -45.47278 | 2025-08-30 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed813f5f-a53b-3811-8727-f49213b8aade | -4.37564 | -48.0674 | 2025-08-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ecc1797-5407-340c-87f7-2b66948f8963 | -3.07095 | -49.46271 | 2025-08-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e17fe4e1-26f5-3f3e-8f14-0874ddd194d2 | -7.16785 | -44.14272 | 2025-08-30 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0da4627b-050c-366d-b434-59b2683a390a | -6.63738 | -44.38432 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b385e89f-0b17-3699-b241-1abcb9087581 | -7.63633 | -46.55429 | 2025-08-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c205e6d-4cfb-3d9c-af9d-1e3d9a8a39b9 | -6.18012 | -43.33993 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 5e2ed71f-6d46-3755-8d91-8d76c5b58bb5 | -7.40987 | -49.52203 | 2025-08-30 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 518b9363-4fad-3279-a017-4ac6a0ad3fb4 | -6.49629 | -43.539 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3996ef24-8ee6-3f32-b575-9e2beeb82baf | -7.09202 | -44.30278 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16dbf1aa-560e-3492-9583-4db402afedc5 | -6.60175 | -43.64978 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 04dab0ac-8580-3f40-8eac-66e1cbd7c54d | -4.88087 | -45.51969 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31bc3a96-ef55-3f8a-8e50-7791f19e3536 | -8.11469 | -45.00834 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b547aa2-578e-350c-b855-68f3956db0e0 | -7.61315 | -42.73184 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6caee026-dfb3-3933-82dd-b7ba5cdd07d7 | -4.98955 | -38.60287 | 2025-08-30 04:19:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| f64dcaec-4093-35de-8b12-c18fafd7a801 | -4.41197 | -40.71541 | 2025-08-30 04:19:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5c1bc9eb-7217-329d-9661-6a6bd7259407 | -6.22507 | -42.74942 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| af7c8953-347f-3854-b31e-bf15dd978a54 | -7.15854 | -45.1648 | 2025-08-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a971b665-11bb-3617-930a-aea863887ef9 | -7.59004 | -42.69653 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1355cda1-7d1b-3ad5-8b68-19ab1858d07b | -5.82605 | -46.36378 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 70bc4c91-eaeb-30c2-bd5a-ecd389734c42 | -6.13545 | -46.31982 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d15ac746-ea60-35ca-9be9-0c76bc2ef8e3 | -6.41357 | -47.86272 | 2025-08-30 04:19:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9dd12022-c1a7-345b-9a41-27277d1c1afd | -4.41703 | -47.60482 | 2025-08-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c807bb9-61f8-3636-92de-2291e0e1671f | -7.11126 | -44.44139 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a95bda7-b49f-39af-a28d-6b75c52b74ab | -7.2183 | -45.43372 | 2025-08-30 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 613bc1d4-5946-3b60-b5e8-5b4212fef39f | -7.0958 | -44.60602 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 38a15235-ac0e-332f-879c-498aadc5c9bf | -7.0297 | -43.86797 | 2025-08-30 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f283091-a10d-3f57-87b4-04b1f6216450 | -6.31833 | -43.60985 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d968ff35-ea0a-3ad3-94ef-c4a33c565f19 | -5.75842 | -45.21886 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a48e400a-8828-3028-9b32-4ac55755b5d7 | -5.7444 | -43.60489 | 2025-08-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84819af7-f76f-3600-bd38-9a27b969167c | -5.54204 | -43.74986 | 2025-08-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46e171ca-d6e7-37f6-8613-f0b1ce619d5a | -9.40091 | -40.5507 | 2025-08-30 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b9a4c22f-e8e5-355a-9f18-75d3b5f5f09a | -7.90405 | -45.8748 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8460e402-1e77-3b75-9c14-cc064464806c | -3.04863 | -47.01902 | 2025-08-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aef1b78d-a15a-3d34-99ff-aedc9286af7f | -7.96006 | -46.37844 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 645191ca-a1cf-3097-ba52-eec2e64210e3 | -6.59169 | -43.6483 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5cc4516d-561c-37f4-b941-a6b0a971c201 | -8.12418 | -45.05599 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1a1f44c-5979-30aa-be2e-32e1d7208226 | -5.87298 | -44.33552 | 2025-08-30 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b36333e-c395-39b8-8320-a6edc96b74ad | -7.58597 | -42.69987 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8062b200-2580-35fc-bb26-28787c723566 | -6.90927 | -44.38447 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b65b0c86-fa9a-3e7c-9656-bdf3e71af492 | -7.15006 | -39.42049 | 2025-08-30 04:19:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 644537aa-c0a9-34a2-abee-d44a1188a27c | -7.24587 | -45.4523 | 2025-08-30 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b4b24195-920e-3083-9f26-2671729150c3 | -7.71985 | -50.30371 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c316d6c-4a30-313d-a642-18d3f02f385d | -6.80279 | -43.75661 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| fe0a54ef-160c-3474-8338-91dbcdf6b9e3 | -6.17112 | -43.33114 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cfdabe8-d3a1-3cd1-94a8-90551b90e421 | -6.49042 | -44.41135 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4a89e38-4598-3520-95e2-751da475b723 | -6.80334 | -43.75306 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |


[Clique aqui para ver as próximas entradas](README22.md)
