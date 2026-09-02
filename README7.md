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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbfad4c0-16bb-395d-b77f-c969a1c423fe | -9.0097 | -65.411102 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08ec69c6-a3f2-3637-93b5-4f44af7ddf08 | -9.036 | -65.390404 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09575615-fa93-3838-bc5c-5847289c7ec7 | -8.2658 | -62.7551 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fd9a961e-7801-3c30-85af-4211a86812ab | -10.279 | -64.501999 | 2026-09-02 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c231cd78-438c-3f44-b13f-83d712f996c9 | -6.683 | -59.949299 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e44e4bc6-ac3e-3c69-ae62-ce66760e0beb | -9.8697 | -64.975304 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8626016a-8a92-3710-959a-8f952f75eb74 | -7.4367 | -61.401501 | 2026-09-02 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ccde4bfe-2721-3bd3-b8c4-306eac60da0e | -6.7552 | -59.428699 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c7c56071-df8a-3786-9ef7-d8c75e9522e6 | -7.4387 | -61.41 | 2026-09-02 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 954206ec-0d69-3c16-a127-099478fc08ce | -4.9574 | -55.851799 | 2026-09-02 01:10:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82ed21a0-6c5d-3313-8aa8-1b33698f4fbb | -3.6107 | -60.545101 | 2026-09-02 01:10:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ded9b1b3-98e5-344a-b511-0ce3ba12b807 | -7.6152 | -57.6124 | 2026-09-02 01:10:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c81afa44-77af-3f9c-807e-c3f338972e90 | -6.6426 | -59.431702 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b7563fa-381f-38a6-97d7-7508e2b9001a | -8.7532 | -62.588001 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 62f86a9b-db0c-3af8-8716-b1decd0393ca | -11.9994 | -60.529099 | 2026-09-02 01:10:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2daa8874-43a5-3f0a-b49f-395b13f1fe81 | -5.5413 | -60.2183 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c76806e6-8e6a-3346-8bda-882460302dda | -7.6914 | -67.124397 | 2026-09-02 01:10:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d33ea9a3-54e0-3652-8744-2eabfe8c1ac9 | -8.4282 | -54.682999 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13010b07-ab16-3ad0-a21e-27e301f50ece | -9.0948 | -65.377296 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45f09b89-a5fb-3a2b-a08e-e3fdb1635a8e | -10.496 | -64.321404 | 2026-09-02 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aacbda29-aa34-3e80-a0a9-55596f95bc93 | -9.016 | -65.439301 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e67c0305-b7dc-3200-b04f-d0166760a4c9 | -7.4504 | -61.371498 | 2026-09-02 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d02dda1-88d9-3f1b-a1de-782b2be34d7b | -9.4429 | -67.439003 | 2026-09-02 01:10:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf9d4961-599a-366f-8beb-14cad6ad7349 | -8.7613 | -62.5784 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0035396f-6cca-30a1-a7f3-38912737fd14 | -10.4683 | -64.4739 | 2026-09-02 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 81d8661e-a47c-3b9e-91ea-8f7929aef1dc | -8.4394 | -54.7271 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d43296e-b66a-32f5-bf96-914e6789b149 | -6.7455 | -59.431 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38511057-d924-33f7-a33e-939af4b98a73 | -6.8174 | -58.869598 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 251a1e36-f91e-3934-80b2-5bcf0c7e03d8 | -9.1375 | -60.956001 | 2026-09-02 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99da1e40-0b4f-3b65-a1aa-e6273abc3981 | -8.0966 | -54.953999 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a985b92-12a1-38d7-9c27-cb2d06f65203 | -10.4881 | -59.5994 | 2026-09-02 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02161623-ebd1-3f6f-b713-4384d4473780 | -6.8722 | -59.400799 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b73a9d4-8dee-360b-8d9f-2539e5ecf33a | -5.5754 | -60.188202 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0a33831-eafc-3b40-947f-b2d7a1333747 | -6.5965 | -58.5923 | 2026-09-02 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4fae5152-eedd-379e-b29b-0b49d8a83abf | -5.5778 | -60.1987 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d97e3d7-cee8-3209-beee-07aecc57e8a0 | -9.0376 | -65.397499 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c774aa09-3433-3a1c-b351-d40bda3100d0 | -7.1914 | -60.6623 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bde0c59d-c816-34e0-8d21-a32db858b9ed | -8.4146 | -54.709999 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8f919ef-6b31-3ae7-93ec-7771e1597f11 | -4.1843 | -63.161301 | 2026-09-02 01:10:00 | METOP-B | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6742a5f-8c64-3afd-a06a-854b393a91b9 | -9.4377 | -64.5606 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93326da7-4339-3ee0-9ebe-3d6c7fefaba2 | -7.2055 | -60.678699 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53f3606c-9f3e-34bd-93d9-46d5ba36a4c3 | -7.1936 | -60.6716 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0d35213-ba97-3494-849a-746c66adf0f2 | -2.1105 | -56.812599 | 2026-09-02 01:10:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 364ecd6f-72d0-34e1-8f66-9b0b14594889 | -6.5934 | -58.579498 | 2026-09-02 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d716e6f1-b644-3287-a32b-b07c9e18f55d | -3.6132 | -60.555698 | 2026-09-02 01:10:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98d35182-64c9-3602-a55c-bb83dd066253 | -7.3509 | -60.5951 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a0c964c-c77c-342b-94aa-139bc41f7dbd | -6.8491 | -59.4771 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe26e22c-dc9c-3174-87b3-7fb35898fd3c | -10.1649 | -69.2985 | 2026-09-02 01:10:00 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b8120e13-b8cd-30ba-bd4a-4d4160206250 | -8.1008 | -54.930099 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9672fae-9149-3f23-a447-450b7b169aa7 | -7.1958 | -60.681 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb452e36-6734-3a7c-9410-4386149374c1 | -6.7676 | -59.437599 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fc212a65-4fbf-3528-8b2d-4c5373b8ff9d | -3.6156 | -60.5662 | 2026-09-02 01:10:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88250fc7-c522-3911-bd82-432759087bed | -10.4927 | -59.6189 | 2026-09-02 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b91d9208-38d1-3da3-ba29-d0696842f7ca | -12.14 | -47.09 | 2026-09-02 01:15:00 | MSG-03 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b8ef39f-4725-36a5-b03d-83fd6e26f5f9 | -8.45 | -54.69 | 2026-09-02 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9782709c-1c87-3c33-92ac-d4b7e34799bf | -9.8806 | -64.9764 | 2026-09-02 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 2f99c3a6-e26d-30ee-bce0-fefba286781a | -12.1312 | -47.1309 | 2026-09-02 01:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| beb7c507-de09-3211-b9c8-25f85ad307c2 | -6.6948 | -58.7678 | 2026-09-02 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| bd6cc3b2-96e8-37ed-854f-464977d6d61d | -6.6949 | -58.7485 | 2026-09-02 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 75017c79-7b07-38bd-911b-8cf0774cdd33 | -11.3334 | -50.618 | 2026-09-02 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| ddba2665-4aa9-3171-8e2f-b8f5ec25b455 | -10.9009 | -45.3509 | 2026-09-02 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| a01e2976-c194-3f3a-a58e-86c7110576cf | -9.862 | -64.9771 | 2026-09-02 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| dc73a592-44ca-3d29-b4f5-12526f1c7036 | -12.1504 | -47.1283 | 2026-09-02 01:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 51ada497-34f3-3d6f-a305-09b89e047c55 | -11.6624 | -50.1954 | 2026-09-02 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a0874291-d698-3c71-a1c8-3a10fc17f937 | -7.2006 | -60.6706 | 2026-09-02 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| a645b19d-ab50-31b3-9af0-285f49d0c12c | -11.3521 | -50.6373 | 2026-09-02 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 50b1a429-b2ad-332e-a72d-ed65dec28586 | -10.9013 | -45.3279 | 2026-09-02 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 52582e04-e082-3521-99d4-6c39969c3db5 | -12.1512 | -47.0833 | 2026-09-02 01:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 104c68c0-be62-3073-b746-60f288e6f390 | -11.3331 | -50.6394 | 2026-09-02 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 48daab54-e839-3c27-94e7-8d16106a93ef | -11.3524 | -50.6159 | 2026-09-02 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 2b56bba7-756c-3f2f-abc7-a895b6cc590e | -8.5728 | -63.1807 | 2026-09-02 01:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| aa07deaa-1d38-3866-874c-fbc8de719179 | -8.7613 | -62.5869 | 2026-09-02 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5149fe95-7415-3d7d-8bad-6dde6489869a | -12.4727 | -41.3059 | 2026-09-02 01:20:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 53.5 |
| 23623134-d357-3cd9-8848-a0a685badf35 | -12.1508 | -47.1058 | 2026-09-02 01:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| b90893f8-64ac-37c7-9802-99cd03cdf3cf | -9.8807 | -64.9576 | 2026-09-02 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 88e2220f-5a66-33c3-9f5f-c89a82c319cd | -7.2005 | -60.6897 | 2026-09-02 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 80aae2db-1461-3113-94f9-d240e6182c4b | -6.6765 | -58.7492 | 2026-09-02 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 518c97ed-78b4-344e-abea-dd35c943930e | -8.1298 | -54.9471 | 2026-09-02 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d3b53dc1-0b26-3186-956d-fa87980194c9 | -6.6764 | -58.7686 | 2026-09-02 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 6ccf606e-431a-37d2-8f55-0a0394dd2f97 | -7.2191 | -60.6699 | 2026-09-02 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 74d83247-6d4f-3c58-8664-3dce39dbceac | -8.5727 | -63.1996 | 2026-09-02 01:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f73aba4f-59e5-39ce-9a20-d4f73c58da32 | -12.1516 | -47.0608 | 2026-09-02 01:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e855b9aa-265e-34cb-ac65-bbd16a073e7a | -12.8843 | -45.8183 | 2026-09-02 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 1b4d26dd-6c4c-3629-9d79-b02805164d66 | -8.911 | -62.372 | 2026-09-02 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e4a7ecb6-4e10-3f07-b1dd-b924983dea8f | -12.4727 | -41.3059 | 2026-09-02 01:30:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 3c1151c8-0bf1-3402-aca2-9a97db9e4339 | -7.2005 | -60.6897 | 2026-09-02 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 1a0e937c-fb09-36fe-8111-a30f542e6eee | -10.9009 | -45.3509 | 2026-09-02 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| e5787979-3433-3d8f-82c0-e32051ce8a07 | -12.1516 | -47.0608 | 2026-09-02 01:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 7a75a124-8056-3f45-a564-5b35caeb6a97 | -8.5727 | -63.1996 | 2026-09-02 01:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 36dddc0d-dc61-38de-892d-12e0fba4db95 | -9.8806 | -64.9764 | 2026-09-02 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 5fbe29ea-81c6-3b89-bc0b-6ada89c64ddc | -10.9013 | -45.3279 | 2026-09-02 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| dab57ba3-6bed-3f23-b045-91e8994c617a | -12.1504 | -47.1283 | 2026-09-02 01:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| a2b0f606-1ef9-33cf-88c6-b300bd8a811d | -8.5728 | -63.1807 | 2026-09-02 01:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a7195a9c-a61e-361e-a6bc-1476e9677213 | -6.6949 | -58.7485 | 2026-09-02 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f381762d-eeb3-3ef3-816f-cd89b1a05773 | -9.862 | -64.9771 | 2026-09-02 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 1384b479-6149-3b6d-8560-240743d1b4f0 | -8.1298 | -54.9471 | 2026-09-02 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 73356fd3-7251-3999-a8ca-c7127816b0f3 | -7.2191 | -60.6699 | 2026-09-02 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| fcf7848c-ffce-3443-bea1-412f8e0488da | -7.2006 | -60.6706 | 2026-09-02 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| d35a9454-2d04-3a2d-b531-7206d46eeba9 | -12.1312 | -47.1309 | 2026-09-02 01:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| ccd94653-ac23-3003-a54d-c5a262f54e91 | -12.1512 | -47.0833 | 2026-09-02 01:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |


[Clique aqui para ver as próximas entradas](README8.md)
