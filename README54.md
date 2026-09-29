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
| e1005f85-c8e3-3258-a3f5-e12a1c886651 | 1.85267 | -55.57188 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00547826-3ea5-3bc7-b1d2-272ec35b804a | 1.69167 | -55.94867 | 2026-09-29 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 977f3227-29af-3b4e-bc58-4fa83c549d57 | 1.82298 | -55.62439 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00c70298-a3c6-371f-8a10-e84e7609435a | 4.0781 | -59.94554 | 2026-09-29 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b51e2aa-648c-3c21-9105-e20fc9a44d22 | 3.65957 | -51.8113 | 2026-09-29 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3a475e0-b3aa-3119-be31-915e855ac7f7 | 3.82806 | -51.76972 | 2026-09-29 05:08:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| affe3045-c94a-30e8-bb41-6ff23d9307c6 | 1.87402 | -55.56476 | 2026-09-29 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9656a8b-cb6b-3f4b-b13d-4d35c9ee12f3 | 1.3256 | -60.71339 | 2026-09-29 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2ed897b-86ca-32ce-8c68-f7f62494f55f | -6.31374 | -43.62001 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dc0d12ec-69a8-3bcf-875c-fd8bf817ad42 | -3.71123 | -54.22645 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 580b3da0-d59b-3142-a134-9be5b69976c3 | -6.68565 | -55.1177 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29b64757-716f-3864-90b5-ec56a952f628 | -7.42821 | -46.88038 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8872d104-5f61-3aca-befe-11caa68a08c8 | -6.30736 | -43.60821 | 2026-09-29 05:10:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89cf0adf-fc7d-35fe-9512-a55f024122ee | -3.70453 | -54.22541 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c90822f6-d09b-3a1f-9277-e3d1e9cde6cb | -8.21715 | -45.46115 | 2026-09-29 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f2a9fc3-42f6-3621-a1c5-b9f504829dfa | -2.89778 | -54.08901 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d16b039d-d097-3494-97ee-0f7c7cb8b38c | -4.29739 | -49.0907 | 2026-09-29 05:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a48a095d-7328-3fae-9c79-67596f9a2918 | -2.90893 | -54.12679 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a499beae-f6fa-3e56-8eda-182cfc5acc92 | -7.53461 | -45.88929 | 2026-09-29 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d3ac2dc-3f27-3b2b-a199-8faa22a49e5a | -6.67287 | -55.11209 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1296c862-283b-3f58-9200-285f7e71a321 | -6.67009 | -55.10806 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7b5f0dd-f296-35f1-9283-6b5e31394501 | -7.56914 | -47.36879 | 2026-09-29 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0649519-64d8-32b2-bfee-721903bc413f | -6.14452 | -51.73744 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cd27036-33ef-3521-895f-6181eef0f794 | -7.42869 | -46.87689 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a0bdf36-ba54-3152-a58f-b789f5a8dbab | -5.61135 | -45.00162 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9ad9f0a0-2661-306b-884e-cc6e39a16fbb | -2.85662 | -54.13303 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fc4c548-a4dc-3cea-bfcd-26eedb7b4ce6 | -3.70733 | -54.22945 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24896f51-0fbd-3572-96ef-137a0ff87411 | -5.42313 | -43.45139 | 2026-09-29 05:10:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 464c0a2e-49ea-3ac9-bc1b-191a5fec7bb5 | -3.51071 | -50.31126 | 2026-09-29 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58824970-2d06-3d5e-a38d-4547c71b4aea | -6.12487 | -43.73851 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f28f8d68-f1b2-3b25-a3bd-57f8a206e456 | -5.48037 | -45.12881 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c079675-1666-3caa-abac-7201b5666832 | -7.26163 | -45.33914 | 2026-09-29 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f255e927-38e1-3425-88c5-82748d2ba9af | -4.45536 | -47.92431 | 2026-09-29 05:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7318688a-90b7-3dbd-835d-e47ac5ed8551 | -6.38039 | -55.13446 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e428397e-3687-3a55-b902-a3dedbe2789d | -6.20448 | -52.90892 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66e01c9e-9ab5-3caf-b742-ec1ba6620fa8 | -2.89889 | -54.08196 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f12f8f01-dd14-310e-af9b-ab6fe85b0482 | -8.24409 | -45.44193 | 2026-09-29 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cd29ea5-f8b8-3b40-8945-ca909f3abb37 | -3.70843 | -54.22242 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e199f43-0e99-34ae-bbce-9bb85dd7dd28 | -2.90335 | -54.09708 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d079270b-8286-37c1-b7d4-23a82c7e1ba4 | -7.24385 | -43.3774 | 2026-09-29 05:10:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 81401aae-5ee2-3110-9b5e-a12da6939a5d | -6.17978 | -53.28451 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76e49b6b-2101-3ab9-94d6-ecfdcea4a97a | -5.97992 | -53.52957 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f6b2a2d-e7dc-3ce8-b12e-e0b039078a6c | -7.00574 | -45.29886 | 2026-09-29 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75ae1a93-ca80-3658-8c10-bf466a601ee6 | -3.1506 | -54.08154 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46bf5c51-07db-3588-9c73-1ea4a4efc6a5 | -6.31971 | -43.61593 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61af3aac-6158-3065-b206-fbe78fc15675 | -6.1352 | -53.05788 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a5bb260-dc5b-39a1-829e-93ed1726541a | -3.82015 | -55.90388 | 2026-09-29 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cddfbb74-353d-318e-8010-ec76b2a9a018 | -3.15004 | -54.08507 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5607f55e-6ca6-3c39-8bc9-6822fbd916bf | -5.73291 | -45.1766 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c898d68-e800-34fb-bf08-eb95e9d74b03 | -6.31899 | -52.6212 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9829d4ca-e178-345e-a0db-1e9f6cc1818e | -5.86709 | -43.59336 | 2026-09-29 05:10:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42830074-0f2d-38de-8276-a6448430c75f | -5.48687 | -45.12556 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1bae6a3-2c1d-35cb-811c-07267d5b3c70 | -3.15395 | -54.08205 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99c50f80-f15d-3f43-ac39-fe78d775c4f6 | -3.15451 | -54.07851 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9543584-96ab-3be3-828d-0c7446da241f | -5.73067 | -45.06289 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70f60897-0fa4-3ca5-add0-be902715fd67 | -3.82292 | -55.90787 | 2026-09-29 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c32180eb-9bb3-31f6-a0f2-6ced2db78770 | -6.14776 | -52.90589 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d5ca56c-8ded-3632-bd61-370056163951 | -7.53849 | -47.11871 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfa328cd-8967-365d-b5ae-d9d81bb1c4f9 | -2.57304 | -54.74725 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7157777d-51ba-3657-b627-efcff2e1e1dd | -6.67954 | -55.11313 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 653af21d-0b3b-3a5f-b3d0-1a937a096d06 | -4.12872 | -51.06165 | 2026-09-29 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 292ea8cd-e9ed-369a-a1c4-c8758bb53d09 | -3.70954 | -54.21536 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c91644f0-637f-3fd2-b293-e5e70eb760b2 | -6.66954 | -55.11157 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a6d158b-440e-3c1d-a766-c9d15ff5b270 | -3.95457 | -47.6403 | 2026-09-29 05:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a5765df-c0fb-3f6d-b5ca-cf95e760947d | -4.0463 | -54.92577 | 2026-09-29 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fa342f4b-54ca-382f-ad1b-75347ba3fc1c | -2.97332 | -54.14782 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e25c7602-3357-3722-8719-3f58b0e30d1d | -5.00961 | -48.04688 | 2026-09-29 05:10:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4afa5b87-d4d4-3251-ac8f-0a2ab1df96c8 | -6.66675 | -55.10754 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e45e708-c3fe-35f3-a8d2-56e9b3c1285c | -4.71704 | -50.64402 | 2026-09-29 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c66d09ee-f61f-3f2f-8846-95d265a514b0 | -2.92732 | -54.18357 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39c0d0d5-9afc-319d-a060-17c82dfd50dd | -6.68232 | -55.11718 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 652bf3f4-c2c6-3c7f-b46c-bbaa6eb37ff1 | -3.00954 | -54.22182 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 533fe033-bdb1-30cd-bf71-74db798ab1e3 | -6.37848 | -45.81481 | 2026-09-29 05:10:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f669bda-3e89-3f05-93d4-78f5974737aa | -7.51421 | -47.34121 | 2026-09-29 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ba8a586-c1e0-387e-9e39-a70f04290f12 | -7.60959 | -46.46339 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6b17bcfb-7cf4-3c3b-8e3c-f73a2a677515 | -5.60937 | -44.99598 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 61702be2-c08c-3955-b80f-ed83ce928ab9 | -3.15506 | -54.09672 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e940a28-eeab-3598-a47a-357dd0797d4a | -6.31793 | -52.62695 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| af3c10e8-63ea-3737-a6f8-fdd6b5ad7026 | -2.9515 | -54.09044 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97c24847-d54a-3326-82f7-75c07d3b328a | -4.46093 | -47.9198 | 2026-09-29 05:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d55326f-0cd6-3120-a439-77bda0eeb8c0 | -7.24144 | -45.26478 | 2026-09-29 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b050fec-5658-3fa7-9b59-46e5d7881e41 | -6.6857 | -46.99177 | 2026-09-29 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa353593-2236-3c8f-9926-0bfeac2651af | -7.38217 | -47.01581 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ae5f69a-9c3a-3213-9a96-6ad47923d020 | -3.70229 | -54.21784 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 867dbd20-b93e-3a59-a18c-ef10d85c87ca | -2.97666 | -54.14835 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26a6f5a3-15d4-30cf-9ea6-840f4726a951 | -2.90614 | -54.10112 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cc3455d-08cd-36c0-9519-9de383a248be | -8.72838 | -44.93126 | 2026-09-29 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 64f8dae9-346b-3161-be04-ce0ffd59fee2 | -7.8344 | -45.81464 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d66df1b4-0936-3938-a6c5-fb723e226302 | -2.91172 | -54.13082 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fac0439f-1bed-36d1-a6db-ff40cd4dbcfe | -3.01343 | -54.21885 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6110a972-3ebd-3948-8b8d-99f0e952488c | -3.39745 | -54.06155 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46c94189-d647-35b3-bec9-d424614491cd | -6.30238 | -56.03951 | 2026-09-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68cbf601-34f6-359f-890a-82ed616a7c1e | -4.81893 | -45.64241 | 2026-09-29 05:10:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f4b2401-3aaf-3380-8ecd-e8da9bbfd8f5 | -2.91453 | -54.19954 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4151a6c9-dead-3bad-aa1f-0d1d2f2f52f9 | -2.29752 | -48.54727 | 2026-09-29 05:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2e771bb-b72a-3ad9-a745-10caac50d528 | -7.84041 | -45.81613 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 30e60a4a-0155-39ff-94ee-d6ea5dcee72e | -7.5341 | -45.89314 | 2026-09-29 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29afa69a-3f10-3e52-81af-1ed8febc6b02 | -7.67367 | -44.88847 | 2026-09-29 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 850e06cd-1fec-38c1-be68-e11a98aa94d7 | -5.72273 | -53.4565 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43dd696a-dd28-32e7-85a6-40df7e9c4660 | -3.14781 | -54.0775 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README55.md)
